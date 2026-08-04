#!/usr/bin/env python3
"""2983_kmem2_analysis.py — K-MEM-MEAS-2 frozen analysis (prereg 2981 §2–§3).

REFUSES to run unless the manifest is COMPLETE (all 1280 legs present):
the prereg forbids interim looks; this gate enforces it mechanically.
Implements verbatim: paired differences on the 2967 response statistic;
block bootstrap (chunks of 8 pairs, 10,000 resamples, percentile CI,
alpha = 0.01); the sigma_ctrl = 3.93e-3 engine-consistency check (factor 2);
blind engine-fault exclusions (NaN/Inf only — resume mismatch cannot occur
under the leg-atomic driver, disclosed); PSD chatter subtraction over
(0, 0.6*omega_N]; the 2967 tail statistic and settle windows; the
domain-scaling discriminator; branch semantics printed in §3 language only.
"""
import glob
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.normpath(os.path.join(HERE, '../data/kmem2'))
N_PAIRS, N_DOMAIN = 512, 128
T_STEP, T_END, T_BALL = 24, 240, 36
ALPHA = 0.01
SIG_CTRL_REF = 3.93e-3
CHUNK, NBOOT = 8, 10000
BOOT_SEED = 29832983          # frozen here (analysis-level constant)


def load(pair, branch, tag):
    p = os.path.join(DATA, f'leg_{pair:04d}_{branch}_{tag}.json')
    if not os.path.exists(p):
        return None
    with open(p) as fh:
        return json.load(fh)


def resp_S(F):
    """The 2967/2968 response statistic: F_0 (early post-step window mean,
    after the ballistic transient) minus F_inf (late window mean)."""
    F = np.asarray(F)
    early = F[T_STEP + T_BALL: T_STEP + T_BALL + 40]
    late = F[T_END - 40:]
    return float(early.mean() - late.mean()), float(late.mean())


def main():
    missing = 0
    for p in range(N_PAIRS):
        for br in ('step', 'ctrl'):
            missing += load(p, br, 'std') is None
    for p in range(N_DOMAIN):
        for br in ('step', 'ctrl'):
            missing += load(p, br, 'dom') is None
    if missing:
        print(f"REFUSING TO RUN: manifest incomplete — {missing} legs "
              f"missing of 1280. The prereg forbids interim looks.")
        return 2

    D, excl, ctrl_sig = [], [], []
    for p in range(N_PAIRS):
        s, c = load(p, 'step', 'std'), load(p, 'ctrl', 'std')
        Fs, Fc = np.array(s['F']), np.array(c['F'])
        if not (np.isfinite(Fs).all() and np.isfinite(Fc).all()):
            excl.append(p); continue          # blind engine-fault exclusion
        Ss, _ = resp_S(Fs); Sc, _ = resp_S(Fc)
        D.append(Ss - Sc)
        ctrl_sig.append(np.std(Fc[T_STEP:]))
    D = np.array(D)
    n = len(D)
    print(f"pairs used {n}/{N_PAIRS}; engine-fault exclusions: "
          f"{sorted(excl) if excl else 'none'}")

    # engine-consistency check (prereg §2)
    sig_ctrl = float(np.mean(ctrl_sig))
    consistent = SIG_CTRL_REF / 2 <= sig_ctrl <= SIG_CTRL_REF * 2
    print(f"sigma_ctrl (ensemble) = {sig_ctrl:.3e} vs ref {SIG_CTRL_REF:.2e} "
          f"-> ENGINE-CONSISTENCY {'OK' if consistent else 'FLAG'}")

    # block bootstrap, chunks of 8 pairs, percentile CI at alpha = 0.01
    rng = np.random.default_rng(BOOT_SEED)
    nch = n // CHUNK
    chunks = D[:nch * CHUNK].reshape(nch, CHUNK)
    boots = np.array([chunks[rng.integers(0, nch, nch)].mean()
                      for _ in range(NBOOT)])
    lo, hi = np.percentile(boots, [100 * ALPHA / 2, 100 * (1 - ALPHA / 2)])
    Dbar = float(D.mean())
    detected = not (lo <= 0.0 <= hi)
    print(f"D_bar = {Dbar:.3e}; {100*(1-ALPHA):.0f}% CI [{lo:.3e}, {hi:.3e}] "
          f"-> step response {'DETECTED' if detected else 'not detected'}")

    # PSD chatter subtraction over (0, 0.6*omega_N]; tail statistic
    def band_psd(sig):
        f = np.fft.rfft(sig - sig.mean())
        return (np.abs(f) ** 2)[1:]
    ps = np.mean([band_psd(np.array(load(p, 'step', 'std')['F'])[T_STEP:])
                  for p in range(N_PAIRS) if p not in excl], axis=0)
    pc = np.mean([band_psd(np.array(load(p, 'ctrl', 'std')['F'])[T_STEP:])
                  for p in range(N_PAIRS) if p not in excl], axis=0)
    nb = int(0.6 * len(ps))
    resid = ps[:nb] - pc[:nb]
    # tail statistic: low-frequency residual excess (lowest decade of band)
    ntail = max(3, nb // 10)
    tail = float(resid[:ntail].mean())
    tail_scale = float(np.std(pc[:ntail]) / np.sqrt(n))
    tail_sig = abs(tail) > 2.576 * tail_scale        # alpha = 0.01 two-sided
    print(f"tail statistic = {tail:.3e} (scale {tail_scale:.3e}) -> "
          f"{'SIGNIFICANT' if tail_sig else 'consistent with zero'}")

    # domain-scaling discriminator on matched pairs 0..127
    Dd = []
    for p in range(N_DOMAIN):
        if p in excl: continue
        s, c = load(p, 'step', 'dom'), load(p, 'ctrl', 'dom')
        Ss, _ = resp_S(np.array(s['F'])); Sc, _ = resp_S(np.array(c['F']))
        Dd.append(Ss - Sc)
    Dd = np.array(Dd)
    ratio = float(Dd.mean() / D[:N_DOMAIN].mean()) if abs(
        D[:N_DOMAIN].mean()) > 0 else np.nan
    print(f"domain discriminator: D_bar(2Rmax)/D_bar(std) on matched pairs = "
          f"{ratio:.3f} (ballistic scales with the box; memory does not)")

    # passivity secondary: in-band residual sign
    passivity_ok = bool(np.median(resid) >= 0) or not detected
    print(f"passivity secondary: in-band residual median "
          f"{np.median(resid):.3e} -> "
          f"{'no anomaly' if passivity_ok else 'SECONDARY-ANOMALY flag'}")

    # §3 branch language ONLY
    print("-" * 70)
    if not consistent:
        print("BRANCH: UNRESOLVED-BY-FLOOR / ENGINE-CONSISTENCY — the "
              "instrument disagrees with its own calibration; reading stands; "
              "no retune; standing NONE; next step is instrument diagnosis.")
    elif tail_sig:
        print("BRANCH: RESOLVED-FALSIFIER candidate — tail statistic "
              "significant; the domain discriminator above determines "
              "memory-type vs ballistic; panel adjudication required. "
              "The worker does not soften this branch.")
    elif detected:
        print("BRANCH: RESOLVED-CONSISTENT candidate — step response "
              "detected, tail consistent with zero. Panel adjudication "
              "required before any standing attaches.")
    else:
        print("BRANCH: no detection and no tail — record as-is for panel "
              "adjudication.")
    print("Evidentiary standing: NONE until panel-adjudicated (prereg §4).")
    return 0


if __name__ == '__main__':
    sys.exit(main())

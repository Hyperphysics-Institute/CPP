#!/usr/bin/env python3
"""3026_kmem_tail1_disposition.py — OPEN-KMEM-TAIL-1 frozen disposition
analysis (kmem_tail1_disposition_prereg.md, Patch 3024, gate as amended
Patch 3025). Implements §1–§3 VERBATIM. Route A: committed data/kmem2
ONLY. Refuses on an incomplete manifest (no interim looks).

Discriminants: T-A transient-exclusion tail (PSD on F[T_STEP+T_BALL:]);
T-B tail domain-scaling ratio on the 128 matched dom/std pairs with a
99% block-bootstrap percentile CI (chunks of 8 pairs, NBOOT=10000,
frozen seed 30241001, matched resampling — the same chunk draw applies
to both subsets, preserving the paired design); T-C window-robustness
qualifier at the three frozen tail fractions; T-D the D_bar-scale
definitional audit (derivation printed; no new data statistics).
Disposition printed in §3 mapping language ONLY. Standing NONE until
panel-adjudicated.
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.normpath(os.path.join(HERE, '../data/kmem2'))
N_PAIRS, N_DOMAIN = 512, 128
T_STEP, T_END, T_BALL = 24, 240, 36          # carried from 2981/2983
BOOT_SEED, CHUNK, NBOOT = 30241001, 8, 10000  # frozen at 3024 §1
Z = 2.576                                     # alpha = 0.01 two-sided, carried


def load(pair, branch, tag):
    p = os.path.join(DATA, f'leg_{pair:04d}_{branch}_{tag}.json')
    if not os.path.exists(p):
        return None
    with open(p) as fh:
        return json.load(fh)


def band_psd(sig):
    """Identical construction to 2983: rfft power, DC dropped."""
    f = np.fft.rfft(sig - sig.mean())
    return (np.abs(f) ** 2)[1:]


def tail_stat(ps_mean, pc_mean, n_used, ntail=None):
    """The 2983 tail statistic on given mean PSDs; returns
    (tail, scale, significant, nb, ntail)."""
    nb = int(0.6 * len(ps_mean))
    resid = ps_mean[:nb] - pc_mean[:nb]
    if ntail is None:
        ntail = max(3, nb // 10)
    tail = float(resid[:ntail].mean())
    scale = float(np.std(pc_mean[:ntail]) / np.sqrt(n_used))
    return tail, scale, bool(abs(tail) > Z * scale), nb, ntail


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
              f"missing of 1280.")
        return 2

    # Blind engine-fault gate, identical to 2983 (frozen: carried set).
    excl = []
    F_step_std, F_ctrl_std = {}, {}
    for p in range(N_PAIRS):
        Fs = np.array(load(p, 'step', 'std')['F'], dtype=float)
        Fc = np.array(load(p, 'ctrl', 'std')['F'], dtype=float)
        if not (np.isfinite(Fs).all() and np.isfinite(Fc).all()):
            excl.append(p)
            continue
        F_step_std[p], F_ctrl_std[p] = Fs, Fc
    used = [p for p in range(N_PAIRS) if p not in excl]
    n = len(used)
    print(f"pairs used {n}/{N_PAIRS}; engine-fault exclusions: "
          f"{sorted(excl) if excl else 'none'}")

    # ---- T-A: transient-exclusion tail (PRIMARY) ----
    ps_A = np.mean([band_psd(F_step_std[p][T_STEP + T_BALL:]) for p in used],
                   axis=0)
    pc_A = np.mean([band_psd(F_ctrl_std[p][T_STEP + T_BALL:]) for p in used],
                   axis=0)
    tail_A, scale_A, sig_A, nb_A, ntail_A = tail_stat(ps_A, pc_A, n)
    cls_A = 'T-A-SIG' if sig_A else 'T-A-ZERO'
    print(f"T-A transient-exclusion tail (PSD on F[{T_STEP + T_BALL}:], "
          f"nb={nb_A}, ntail={ntail_A}): tail = {tail_A:.3e} "
          f"(scale {scale_A:.3e}) -> {cls_A}")
    # Reference: the original-window tail, recomputed for the record.
    ps_O = np.mean([band_psd(F_step_std[p][T_STEP:]) for p in used], axis=0)
    pc_O = np.mean([band_psd(F_ctrl_std[p][T_STEP:]) for p in used], axis=0)
    tail_O, scale_O, sig_O, nb_O, ntail_O = tail_stat(ps_O, pc_O, n)
    print(f"    [reference: original-window tail (F[{T_STEP}:], nb={nb_O}, "
          f"ntail={ntail_O}) = {tail_O:.3e} (scale {scale_O:.3e}) -> "
          f"{'SIGNIFICANT' if sig_O else 'consistent with zero'}]")

    # ---- T-B: domain scaling of the TAIL itself ----
    dom_used = [p for p in range(N_DOMAIN) if p not in excl]
    m = len(dom_used)
    Sd = np.stack([band_psd(np.array(load(p, 'step', 'dom')['F'],
                                     dtype=float)[T_STEP:])
                   for p in dom_used])
    Cd = np.stack([band_psd(np.array(load(p, 'ctrl', 'dom')['F'],
                                     dtype=float)[T_STEP:])
                   for p in dom_used])
    Ss = np.stack([band_psd(F_step_std[p][T_STEP:]) for p in dom_used])
    Cs = np.stack([band_psd(F_ctrl_std[p][T_STEP:]) for p in dom_used])
    print(f"    [T-B leg lengths: dom F -> {Sd.shape[1]} bins, "
          f"std F -> {Ss.shape[1]} bins; per-subset windows per §2]")

    def subset_tail(S, C):
        nbins = S.shape[1]
        nb = int(0.6 * nbins)
        ntail = max(3, nb // 10)
        resid = S.mean(axis=0)[:nb] - C.mean(axis=0)[:nb]
        return float(resid[:ntail].mean()), ntail

    tail_dom, ntail_d = subset_tail(Sd, Cd)
    tail_std, ntail_s = subset_tail(Ss, Cs)
    R_point = tail_dom / tail_std
    print(f"T-B tails: dom = {tail_dom:.3e} (ntail={ntail_d}), matched std "
          f"= {tail_std:.3e} (ntail={ntail_s}); R_tail = {R_point:.3f}")

    rng = np.random.default_rng(BOOT_SEED)
    nch = m // CHUNK
    order = np.array(dom_used)[:nch * CHUNK]
    idx = np.arange(len(order)).reshape(nch, CHUNK)
    draws = rng.integers(0, nch, size=(NBOOT, nch))
    Rb = np.empty(NBOOT)
    Sd_c = Sd[:nch * CHUNK].reshape(nch, CHUNK, -1).mean(axis=1)
    Cd_c = Cd[:nch * CHUNK].reshape(nch, CHUNK, -1).mean(axis=1)
    Ss_c = Ss[:nch * CHUNK].reshape(nch, CHUNK, -1).mean(axis=1)
    Cs_c = Cs[:nch * CHUNK].reshape(nch, CHUNK, -1).mean(axis=1)
    nb_d = int(0.6 * Sd.shape[1]); nt_d = max(3, nb_d // 10)
    nb_s = int(0.6 * Ss.shape[1]); nt_s = max(3, nb_s // 10)
    for i in range(NBOOT):
        d = draws[i]
        td = (Sd_c[d].mean(axis=0)[:nt_d] - Cd_c[d].mean(axis=0)[:nt_d]).mean()
        ts = (Ss_c[d].mean(axis=0)[:nt_s] - Cs_c[d].mean(axis=0)[:nt_s]).mean()
        Rb[i] = td / ts if ts != 0 else np.inf
    lo, hi = np.percentile(Rb[np.isfinite(Rb)], [0.5, 99.5])
    excl_1 = not (lo <= 1.0 <= hi)
    excl_2 = not (lo <= 2.0 <= hi)
    if excl_1 and not excl_2:
        cls_B = 'T-B-SUPPORT'
    elif excl_2 and not excl_1:
        cls_B = 'T-B-MEMORY'
    else:
        cls_B = 'T-B-ND'
    print(f"T-B bootstrap (matched resampling, {nch} chunks x {CHUNK}, "
          f"NBOOT={NBOOT}, seed {BOOT_SEED}): R_tail 99% CI "
          f"[{lo:.3f}, {hi:.3f}] -> {cls_B}")

    # ---- T-C: window robustness of T-A ----
    fracs = [nb_A // 12, nb_A // 10, nb_A // 8]
    classes = []
    for f in fracs:
        nt = max(3, f)
        t, s_, sg, _, _ = tail_stat(ps_A, pc_A, n, ntail=nt)
        classes.append(sg)
        print(f"T-C ntail={nt}: tail = {t:.3e} (scale {s_:.3e}) -> "
              f"{'SIGNIFICANT' if sg else 'consistent with zero'}")
    cls_C = 'T-C-STABLE' if len(set(classes)) == 1 else 'T-C-UNSTABLE'
    print(f"T-C -> {cls_C}")

    # ---- T-D: D_bar-scale definitional audit (derivation; no new stats) ----
    print("T-D audit (derivation from the frozen texts; no new data "
          "statistics):")
    print("  (1) The 2918 scale 0.026*beta = 2.6e-3 is defined in the "
          "MEAS-1 record §4.1 as the SUSTAINED motion response.")
    print("  (2) MEAS-1's statistic S = |F_inf - F_0| used F_0 = PRE-step "
          "window — sensitive to a sustained shift.")
    print("  (3) MEAS-2's frozen resp_S = mean(F[60:100]) - mean(F[200:240]) "
          "uses two POST-step windows — a sustained shift cancels "
          "EXACTLY; only decay BETWEEN the windows registers.")
    print("  (4) The theory's own prediction (finite support, settle within "
          "T_BALL = 36 < 60) is early = late, i.e. D_bar = 0 PREDICTED.")
    print("  (5) The 2981 power computation applied the sustained scale to "
          "a statistic structurally blind to it; the survival-to-window "
          "premise was never derived and contradicts (4).")
    print("  -> T-D-EXPECTATION-DEFECT: the scale does not apply as "
          "assumed; the observed D_bar = -2.8e-5 ~ 0 is CONSISTENT with "
          "the no-memory prediction, not anomalous. Routing per §2: not "
          "to Route B, never to retune.")

    # ---- §3 frozen total disposition mapping ----
    print("-" * 70)
    if cls_A == 'T-A-ZERO' and cls_B in ('T-B-SUPPORT', 'T-B-ND'):
        disp = ("DISP-A SUPPORT-ARTIFACT — the excess is the transient "
                "leaking into the low band. The exportable falsifier is "
                "UNFIRED; the MEAS-2 record re-reads as no-memory-detected; "
                "the L-4/L-6 indictment LIFTS; OPEN-KMEM-TAIL-1 CLOSES; the "
                "1B promotion bar re-arms pending D-KAPPA and a fresh "
                "promotion round.")
    elif cls_A == 'T-A-SIG' and cls_B == 'T-B-MEMORY' and cls_C == 'T-C-STABLE':
        disp = ("DISP-B MEMORY-CONFIRMED — the registered exportable "
                "falsifier FIRES: T-3 §6 + B-1 L-4 + L-6 are contradicted; "
                "charter revision/HALT routing to the panel; the worker "
                "does not soften this branch.")
    elif cls_A == 'T-A-ZERO' and cls_B == 'T-B-MEMORY':
        disp = ("DISP-C MIXED (conflict class T-A-ZERO ∧ T-B-MEMORY) — "
                "Route B activates: extended-control re-run under its own "
                "fresh frozen preregistration; the falsifier is neither "
                "fired nor retired.")
    else:
        disp = ("DISP-C MIXED — existing data cannot disposition; Route B "
                "activates: extended-control re-run under its own fresh "
                "frozen preregistration; the falsifier is neither fired "
                "nor retired.")
    print(f"DISPOSITION ({cls_A} ∧ {cls_B} ∧ {cls_C}): {disp}")
    print("Evidentiary standing: NONE until panel-adjudicated (prereg §4, "
          "gate as amended Patch 3025).")
    return 0


if __name__ == '__main__':
    sys.exit(main())

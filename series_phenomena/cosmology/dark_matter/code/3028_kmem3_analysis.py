#!/usr/bin/env python3
"""3028_kmem3_analysis.py — K-MEM-MEAS-3 (TAIL-1 Route B) frozen analysis.

Implements `kmem_meas3_routeB_prereg.md` (Patch 3027) §2–§3 VERBATIM.
REFUSES to run unless the manifest is COMPLETE (all 384 legs): the
prereg forbids interim looks. Disposition printed in §3 tree language
ONLY, evaluated in the frozen order. Standing NONE until
panel-adjudicated.
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.normpath(os.path.join(HERE, '../data/kmem3'))
N_PAIRS = 64
DOMAINS = ((24.0, 'd24'), (28.0, 'd28'), (32.0, 'd32'))
T_STEP, T_END = 24, 384
BOOT_SEED, CHUNK, NBOOT = 30281001, 4, 10000     # frozen at 3027 §2
Z = 2.576
PRE_W, POST_W = (12, 24), (300, 360)             # S3 windows, frozen
SUST_REF = 2.6e-3                                # 2918 sustained scale


def load(pair, branch, tag):
    p = os.path.join(DATA, f'leg_{pair:04d}_{branch}_{tag}.json')
    if not os.path.exists(p):
        return None
    with open(p) as fh:
        return json.load(fh)


def band_psd(sig):
    f = np.fft.rfft(sig - sig.mean())
    return (np.abs(f) ** 2)[1:]


def main():
    missing = sum(load(p, br, tag) is None
                  for p in range(N_PAIRS)
                  for _, tag in DOMAINS
                  for br in ('step', 'ctrl'))
    if missing:
        print(f"REFUSING TO RUN: manifest incomplete — {missing} legs "
              f"missing of {N_PAIRS * len(DOMAINS) * 2}.")
        return 2

    # Blind engine-fault gate; an exclusion voids the pair in ALL domains.
    F = {}
    excl = set()
    for p in range(N_PAIRS):
        for _, tag in DOMAINS:
            for br in ('step', 'ctrl'):
                arr = np.array(load(p, br, tag)['F'], dtype=float)
                if not np.isfinite(arr).all():
                    excl.add(p)
                F[(p, br, tag)] = arr
    used = [p for p in range(N_PAIRS) if p not in excl]
    n = len(used)
    print(f"pairs used {n}/{N_PAIRS}; engine-fault exclusions: "
          f"{sorted(excl) if excl else 'none'} (voids the pair in ALL "
          f"domains)")

    rng = np.random.default_rng(BOOT_SEED)
    nch = n // CHUNK
    draws = rng.integers(0, nch, size=(NBOOT, nch))

    # Per-domain PSD stacks, tail statistics, per-pair chunk means.
    tails, sigs, chunk_means, peaks = {}, {}, {}, {}
    for x_half, tag in DOMAINS:
        S = np.stack([band_psd(F[(p, 'step', tag)][T_STEP:]) for p in used])
        C = np.stack([band_psd(F[(p, 'ctrl', tag)][T_STEP:]) for p in used])
        nb = int(0.6 * S.shape[1])
        ntail = max(3, nb // 10)
        resid = S.mean(axis=0)[:nb] - C.mean(axis=0)[:nb]
        tail = float(resid[:ntail].mean())
        scale = float(np.std(C.mean(axis=0)[:ntail]) / np.sqrt(n))
        sig = bool(abs(tail) > Z * scale)
        tails[tag], sigs[tag] = tail, sig
        Dm = (S - C)[:, :ntail].mean(axis=1)     # per-pair tail contribution
        chunk_means[tag] = Dm[:nch * CHUNK].reshape(nch, CHUNK).mean(axis=1)
        # S2: peak-|residual| bin in the lower half-band, as period
        half = nb // 2
        k = int(np.argmax(np.abs(resid[:half]))) + 1   # +1: DC dropped
        Tpost = len(F[(used[0], 'step', tag)]) - T_STEP
        peaks[tag] = (Tpost / k, k <= ntail)
        print(f"S1 {tag} (x_half={x_half}): tail = {tail:.3e} "
              f"(scale {scale:.3e}, nb={nb}, ntail={ntail}) -> "
              f"{'SIGNIFICANT' if sig else 'consistent with zero'}; "
              f"S2 peak period P = {peaks[tag][0]:.0f} Moments "
              f"(in lowest ntail bins: {peaks[tag][1]})")

    # S1 ratio CIs, matched chunk draws across domains.
    def ratio_ci(tag_a, tag_b):
        Ra = np.empty(NBOOT)
        ca, cb = chunk_means[tag_a], chunk_means[tag_b]
        for i in range(NBOOT):
            d = draws[i]
            tb = cb[d].mean()
            Ra[i] = ca[d].mean() / tb if tb != 0 else np.inf
        lo, hi = np.percentile(Ra[np.isfinite(Ra)], [0.5, 99.5])
        return lo, hi

    lo1, hi1 = ratio_ci('d28', 'd24')
    lo2, hi2 = ratio_ci('d32', 'd28')
    c1 = lo1 <= 1.0 <= hi1
    c2 = lo2 <= 1.0 <= hi2
    print(f"S1 ratios (matched bootstrap, {nch} chunks x {CHUNK}, "
          f"NBOOT={NBOOT}, seed {BOOT_SEED}): R(28/24) 99% CI "
          f"[{lo1:.3f}, {hi1:.3f}] (contains 1: {c1}); R(32/28) 99% CI "
          f"[{lo2:.3f}, {hi2:.3f}] (contains 1: {c2})")

    # S2 class over the three domains.
    P = [peaks[tag][0] for _, tag in DOMAINS]
    lowest_all = all(peaks[tag][1] for _, tag in DOMAINS)
    monotone = (P[0] < P[1] < P[2]) or (P[0] > P[1] > P[2])
    if monotone and not lowest_all:
        s2 = 'GEOMETRY'
    elif lowest_all:
        s2 = 'MEMORY-LOC'
    else:
        s2 = 'AMBIG'
    print(f"S2 peak periods {[f'{v:.0f}' for v in P]} -> {s2}")

    # S3 sustained-response positive control.
    s3_pass = False
    for x_half, tag in DOMAINS:
        Ds = []
        for p in used:
            def sust(br):
                a = F[(p, br, tag)]
                return a[POST_W[0]:POST_W[1]].mean() - \
                    a[PRE_W[0]:PRE_W[1]].mean()
            Ds.append(sust('step') - sust('ctrl'))
        Ds = np.array(Ds)
        cm = Ds[:nch * CHUNK].reshape(nch, CHUNK).mean(axis=1)
        boots = np.array([cm[draws[i]].mean() for i in range(NBOOT)])
        lo, hi = np.percentile(boots, [0.5, 99.5])
        det = not (lo <= 0.0 <= hi)
        mean = float(Ds.mean())
        in_band = SUST_REF / 2 <= abs(mean) <= SUST_REF * 2
        ok = det and in_band
        if tag == 'd24':
            s3_pass = ok
        print(f"S3 {tag}: S_sust = {mean:.3e} (99% CI [{lo:.3e}, "
              f"{hi:.3e}]) detected={det}, within factor 2 of "
              f"{SUST_REF:.1e}: {in_band}")
    print(f"S3 positive control (pass criterion = x=24 domain): "
          f"{'PASS' if s3_pass else 'FAIL'}")

    # §3 frozen disposition tree, frozen order.
    print("-" * 70)
    all_sig = all(sigs[tag] for _, tag in DOMAINS)
    if not s3_pass:
        disp = ("DISP-I INSTRUMENT/EXPECTATION — the sustained-response "
                "positive control failed; no tail interpretation issues "
                "from this campaign; route = instrument diagnosis; the "
                "falsifier is untouched; no retune.")
    elif all_sig and c1 and c2 and s2 == 'MEMORY-LOC':
        disp = ("DISP-B' MEMORY-CONFIRMED — the registered exportable "
                "falsifier FIRES: T-3 §6 + B-1 L-4 + L-6 are contradicted; "
                "charter revision/HALT routing; the worker does not soften "
                "this branch.")
    elif s2 == 'GEOMETRY' and not (c1 and c2):
        disp = ("DISP-A' GEOMETRY-ARTIFACT — the excess is domain-geometry "
                "structure, not a memory kernel; the falsifier is UNFIRED; "
                "the L-4/L-6 indictment LIFTS subject to the panel's design "
                "review at the single round; OPEN-KMEM-TAIL-1 CLOSES there; "
                "the 1B bar re-arms pending D-KAPPA.")
    else:
        disp = ("DISP-M' IMPASSE — conflicted or insufficient pattern; the "
                "single panel round convenes with both instruments' designs "
                "and records on the table.")
    print(f"DISPOSITION: {disp}")
    print("Evidentiary standing: NONE until panel-adjudicated "
          "(prereg 3027; single-round rule per Patch 3025).")
    return 0


if __name__ == '__main__':
    sys.exit(main())

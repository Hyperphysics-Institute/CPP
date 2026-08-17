#!/usr/bin/env python3
"""3163_routeC_s3c_diagnostic.py — Route C S3-C instrument characterization.

Implements `routeC_s3c_diagnostic_prereg.md` (Patch 3163) VERBATIM.
Readings frozen in that document BEFORE this script was run.

PRODUCES NO DISPOSITION. Moves no ledger item. Does not re-site the band,
does not re-run the frozen tree, does not re-read the falsifier.
Read-only on data/kmemC.
"""
import json, os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.normpath(os.path.join(HERE, '../data/kmemC'))

T_STEP = 24
NBOOT, BOOT_SEED = 2000, 31630817

# (tag, class, x_half, T_END, beta, N, DT)
ARMS = [('a0', 'iso', 24.0, 384, 0.10, 128, 0.0),
        ('a0p', 'iso', 16.0, 264, 0.10, 128, 0.0),
        ('a1', 'iso', 32.0, 384, 0.10, 128, -12.0),
        ('a2', 'iso', 28.0, 504, 0.10, 128, 6.0),
        ('ak', 'margin', 28.0, 104, 0.60, 512, 6.0)]


def windows(x_half, T_END):
    t_post = int(T_STEP + 1.5 * x_half) + 6
    return t_post, max(12, min(48, (T_END - t_post) // 3))


def load_arm(tag, n):
    S, C = [], []
    for p in range(n):
        s = os.path.join(DATA, f'leg_{p:04d}_step_{tag}.json')
        c = os.path.join(DATA, f'leg_{p:04d}_ctrl_{tag}.json')
        if not (os.path.exists(s) and os.path.exists(c)):
            continue
        S.append(np.array(json.load(open(s))['F']))
        C.append(np.array(json.load(open(c))['F']))
    return np.stack(S) - np.stack(C)


def sust_on(D, lo, hi, LATE):
    """Sustained statistic on an explicit window, baseline-subtracted."""
    return float(abs(D[:, lo:hi].mean() - D[:, LATE].mean(axis=1).mean()))


def boot_sust(D, lo, hi, LATE, rng, nboot=NBOOT):
    m = D.shape[0]
    return np.array([abs(D[rng.integers(0, m, m), lo:hi].mean()
                         - D[rng.integers(0, m, m), LATE].mean())
                     for _ in range(nboot)])


def ci99(x):
    return float(np.percentile(x, 0.5)), float(np.percentile(x, 99.5))


def main():
    rep = json.load(open(os.path.join(DATA, 'pilot_report.json')))
    nmap = {a[0]: (int(rep['N_projected']) if a[0] == 'ak' else a[5])
            for a in ARMS}
    rng = np.random.default_rng(BOOT_SEED)

    D, W = {}, {}
    for tag, cls, xh, TE, beta, N, dt in ARMS:
        D[tag] = load_arm(tag, nmap[tag])
        t_post, base = windows(xh, TE)
        W[tag] = (t_post, base, TE, slice(TE - base, TE), beta, dt)
        avail = TE - t_post - base
        print(f"  loaded {tag:4} pairs={D[tag].shape[0]:4}  t_post={t_post:3} "
              f"base={base:2}  clean Moments={avail:3}"
              f"{'   <-- 40-wide window DOES NOT FIT' if avail < 40 else ''}")

    # ---------------- D-1: beta-scaling at matched Delta and geometry -------
    print("\n" + "=" * 70)
    print("D-1  BETA-SCALING  (a2 vs ak; both x_half=28, Delta=+6; beta 0.10 vs 0.60)")
    print("=" * 70)
    COMMON = 20                      # AK admits only 20 clean Moments
    r = {}
    for tag in ('a2', 'ak'):
        t_post, base, TE, LATE, beta, dt = W[tag]
        lo, hi = t_post, t_post + COMMON
        s = sust_on(D[tag], lo, hi, LATE)
        b = boot_sust(D[tag], lo, hi, LATE, rng)
        lo99, hi99 = ci99(b)
        r[tag] = (s, b, lo99, hi99, lo, hi, beta)
        print(f"  {tag:4} beta={beta:.2f}  window {lo}:{hi} ({COMMON} pts, "
              f"matched)  sust={s:.4e}  99% CI [{lo99:.3e}, {hi99:.3e}]")

    ratio = r['ak'][0] / r['a2'][0] if r['a2'][0] else float('nan')
    rb = r['ak'][1] / np.where(r['a2'][1] == 0, np.nan, r['a2'][1])
    rlo, rhi = ci99(rb[np.isfinite(rb)])
    print(f"\n  R = sust(ak)/sust(a2) = {ratio:.3f}   99% CI [{rlo:.3f}, {rhi:.3f}]")
    print(f"  band assumes R ~ 6.0 (beta scaling);  R ~ 1.0 means NO beta scaling")

    has6, has1 = (rlo <= 6.0 <= rhi), (rlo <= 1.0 <= rhi)
    if has6 and not has1:
        d1 = "BETA-SCALING-CONFIRMED"
    elif has1 and not has6:
        d1 = "BETA-SCALING-FALSIFIED"
    else:
        d1 = "BETA-SCALING-UNRESOLVED"
    print(f"  >>> D-1 READING: {d1}")

    # ---------------- D-2: detuning dependence (isolation arms, beta fixed) --
    print("\n" + "=" * 70)
    print("D-2  DETUNING DEPENDENCE  (a0, a0p, a1, a2; all beta=0.10)")
    print("=" * 70)
    iso = {}
    for tag in ('a0', 'a0p', 'a2', 'a1'):
        t_post, base, TE, LATE, beta, dt = W[tag]
        lo, hi = t_post, t_post + 40
        s = sust_on(D[tag], lo, hi, LATE)
        b = boot_sust(D[tag], lo, hi, LATE, rng)
        lo99, hi99 = ci99(b)
        iso[tag] = (abs(dt), s, lo99, hi99)
        print(f"  {tag:4} |Delta|={abs(dt):5.1f}  window {lo}:{hi}  "
              f"sust={s:.4e}  99% CI [{lo99:.3e}, {hi99:.3e}]")

    z0 = [iso['a0'], iso['a0p']]
    m0 = float(np.mean([v[1] for v in z0]))
    lo0 = min(v[2] for v in z0)
    s6, lo6, hi6 = iso['a2'][1], iso['a2'][2], iso['a2'][3]
    s12, lo12, hi12 = iso['a1'][1], iso['a1'][2], iso['a1'][3]

    ordered = (m0 > s6 > s12)
    separated = (lo0 > hi12)
    print(f"\n  mean(Delta=0) = {m0:.4e}   |Delta|=6 -> {s6:.4e}   "
          f"|Delta|=12 -> {s12:.4e}")
    print(f"  ordering (0 > 6 > 12): {ordered}")
    print(f"  Delta=0 low CI ({lo0:.3e}) > |Delta|=12 high CI ({hi12:.3e}): "
          f"{separated}")

    if ordered and separated:
        d2 = "DETUNING-DEPENDENT"
    elif not ordered:
        d2 = "DETUNING-INDEPENDENT"
    else:
        d2 = "DETUNING-SUGGESTIVE"
    print(f"  >>> D-2 READING: {d2}")

    # ---------------- D-3: AK on a clean non-overlapping window -------------
    print("\n" + "=" * 70)
    print("D-3  AK CLEAN WINDOW  (72:92, zero overlap with baseline 92:104)")
    print("=" * 70)
    t_post, base, TE, LATE, beta, dt = W['ak']
    lo, hi = t_post, TE - base
    s = sust_on(D['ak'], lo, hi, LATE)
    b = boot_sust(D['ak'], lo, hi, LATE, rng)
    lo99, hi99 = ci99(b)
    print(f"  ak window {lo}:{hi} ({hi - lo} pts)  sust={s:.4e}  "
          f"99% CI [{lo99:.3e}, {hi99:.3e}]")
    print("  (No pass/fail computed: D-1 may show AK's band mis-sited, and "
          "comparing to a suspect band would be circular.)")

    # ---------------- summary + exhaustion trigger --------------------------
    print("\n" + "=" * 70)
    print(f"D-1 {d1}   |   D-2 {d2}")
    if d1 == "BETA-SCALING-UNRESOLVED" and d2 == "DETUNING-INDEPENDENT":
        print("EXHAUSTION TRIGGER FIRES (prereg S4): no principled account of "
              "the universal undershoot -> PANEL.")
    else:
        print("Exhaustion trigger does NOT fire; findings feed the successor "
              "calibration campaign design.")
    print("NO DISPOSITION PRODUCED. DISP-I3 stands. Item 1B remains OPEN.")
    print("=" * 70)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

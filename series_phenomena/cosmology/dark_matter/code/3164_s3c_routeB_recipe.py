#!/usr/bin/env python3
"""3164_s3c_routeB_recipe.py — S3-C recomputed under the ACTUAL Route B recipe.

Implements `routeC_s3c_routeB_recipe_prereg.md` (Patch 3164) VERBATIM.
Readings frozen in that document BEFORE this script was run.

THE DEFECT BEING REPAIRED
  prereg v2 §4 mandates "Route B recipe". Route B (code/3028_kmem3_analysis.py):
      sust = D[POST_late] - D[PRE_prestep]      signed; det = signed CI excl. 0
  Route C (code/3055_kmemC_analysis.py) implemented instead:
      sust = |D[early_post] - D[LATE]|          abs(); det trivially true
  The latter is a DECAY statistic: a perfectly sustained response reads ZERO.

PRINTS NO DISPOSITION. Does not re-run the frozen tree. Read-only.
"""
import json, os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.normpath(os.path.join(HERE, '../data/kmemC'))

T_STEP = 24
SUST_REF0 = 2.6e-3
NBOOT, BOOT_SEED = 10000, 30530811
PRE = slice(12, 24)                      # Route B PRE_W, pre-step, all arms

ARMS = [('a0', 'iso', 24.0, 384, 0.10, 128, 0.0),
        ('a0p', 'iso', 16.0, 264, 0.10, 128, 0.0),
        ('a1', 'iso', 32.0, 384, 0.10, 128, -12.0),
        ('a2', 'iso', 28.0, 504, 0.10, 128, 6.0),
        ('ak', 'margin', 28.0, 104, 0.60, 512, 6.0)]


def windows(x_half, T_END):
    t_post = int(T_STEP + 1.5 * x_half) + 6
    return t_post, max(12, min(48, (T_END - t_post) // 3))


def main():
    rep = json.load(open(os.path.join(DATA, 'pilot_report.json')))
    nmap = {a[0]: (int(rep['N_projected']) if a[0] == 'ak' else a[5])
            for a in ARMS}
    rng = np.random.default_rng(BOOT_SEED)

    print("=" * 78)
    print("S3-C UNDER THE ROUTE B RECIPE   sust_B = D[LATE] - D[PRE(12:24)], SIGNED")
    print("=" * 78)

    s3_pass, powered, rows = {}, {}, []
    for tag, cls, xh, TE, beta, N, dt in ARMS:
        t_post, base = windows(xh, TE)
        LATE = slice(TE - base, TE)
        band = SUST_REF0 * beta / 0.10
        n = nmap[tag]

        S, C = [], []
        for p in range(n):
            ps = os.path.join(DATA, f'leg_{p:04d}_step_{tag}.json')
            pc = os.path.join(DATA, f'leg_{p:04d}_ctrl_{tag}.json')
            if not (os.path.exists(ps) and os.path.exists(pc)):
                continue
            S.append(np.array(json.load(open(ps))['F']))
            C.append(np.array(json.load(open(pc))['F']))
        D = np.stack(S) - np.stack(C)
        m = D.shape[0]

        # per-pair Route B statistic, then bootstrap over PAIRS
        per_pair = D[:, LATE].mean(axis=1) - D[:, PRE].mean(axis=1)
        sust_B = float(per_pair.mean())
        boots = np.array([per_pair[rng.integers(0, m, m)].mean()
                          for _ in range(NBOOT)])
        lo, hi = (float(np.percentile(boots, 0.5)),
                  float(np.percentile(boots, 99.5)))
        det = not (lo <= 0.0 <= hi)
        inband = bool(band / 2 <= abs(sust_B) <= band * 2)
        s3_pass[tag] = det and inband

        half = (hi - lo) / 2.0
        powered[tag] = half <= band / 2
        # the OLD (defective) statistic, for side-by-side
        old = float(abs(D[:, 60:100].mean() - D[:, LATE].mean(axis=1).mean()))

        rows.append((tag, cls, dt, beta, band, old, sust_B, lo, hi, det,
                     inband, half, powered[tag]))

    print(f"{'arm':4} {'cls':6} {'DT':>5} {'beta':>5} "
          f"{'band':>21} {'OLD(defective)':>15} {'sust_B(signed)':>15} "
          f"{'99% CI':>25} {'det':>5} {'inband':>7} {'pass':>5} {'powered':>8}")
    for (tag, cls, dt, beta, band, old, sB, lo, hi, det, inband,
         half, pw) in rows:
        print(f"{tag:4} {cls:6} {dt:5.0f} {beta:5.2f} "
              f"[{band/2:.2e},{band*2:.2e}] {old:15.4e} {sB:15.4e} "
              f"[{lo:.3e},{hi:.3e}] {str(det):>5} {str(inband):>7} "
              f"{str(det and inband):>5} {str(pw):>8}")

    print("\n--- RESOLUTION FLOOR (prereg §3; CONV-022 §9 claim hygiene) ---")
    for (tag, cls, dt, beta, band, old, sB, lo, hi, det, inband,
         half, pw) in rows:
        print(f"  {tag:4} CI half-width {half:.3e} vs band/2 {band/2:.3e}"
              f"  -> {'ADEQUATE' if pw else 'UNDERPOWERED'}")

    iso = [r[0] for r in rows if r[1] == 'iso']
    n_iso_pass = sum(1 for t in iso if s3_pass[t])
    any_under = any(not powered[t] for t in iso + ['ak'])

    print("\n" + "=" * 78)
    print(f"isolation arms passing: {n_iso_pass}/4    ak passing: {s3_pass['ak']}")
    if any_under:
        reading = "S3C-UNDERPOWERED"
    elif n_iso_pass >= 2 and s3_pass['ak']:
        reading = "S3C-RESTORED"
    elif n_iso_pass == 0 and not s3_pass['ak']:
        reading = "S3C-GENUINE-FAILURE"
    else:
        reading = "S3C-MIXED"
    print(f">>> FROZEN READING: {reading}")
    if reading == "S3C-RESTORED":
        print("    Tree item 1 would NOT have fired. NOT re-run here (prereg §6).")
        print("    NOTE THE DIRECTION: item 2 would then evaluate, and S1-C")
        print("    returned SIGNIFICANT at a2 (Delta=+6) -> DISP-T fires against")
        print("    Candidate (B). This repair can only convict, never rescue.")
        print("    CONV-025 warranted on economy-rule 2.1 (closed falsifier campaign).")
    elif reading == "S3C-GENUINE-FAILURE":
        print("    Exhaustion trigger FIRES (prereg §5): three worker hypotheses,")
        print("    all failed -> PANEL.")
    print("NO DISPOSITION PRODUCED. DISP-I3 stands. Item 1B remains OPEN.")
    print("=" * 78)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

#!/usr/bin/env python3
"""3165_establishment_curve.py — when does the sustained response establish?

Implements `routeC_establishment_time_prereg.md` (Patch 3165) VERBATIM.
Readings frozen in that document BEFORE this script was run.

QUESTION: AK returns no sustained response at 6x the drive of four arms that
all detect. Two explanations remain and Patch 3163 D-1 could not separate them:
  H-HORIZON  the response takes time to establish; AK's LATE window sits only
             68 Moments post-step (vs 240-432 for the isolation arms).
  H-BETA     the response does not scale with beta; AK's band is ~6x mis-sited.
Separable on existing legs, because each isolation arm's own series contains
the establishment curve.

  g(t) = D[:, t:t+24].mean() - D[:, PRE(12:24)].mean()      SIGNED

PRINTS NO DISPOSITION. Does not re-site the band, re-run the tree, or re-read
the falsifier. Read-only.
"""
import json, os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.normpath(os.path.join(HERE, '../data/kmemC'))

T_STEP = 24
PRE = slice(12, 24)
WIDTH, STEP = 24, 12                     # frozen: Route B PRE width; v2.1 min baseline
NBOOT, BOOT_SEED = 2000, 30530811
AK_HORIZON = 68                          # AK's LATE end (104) minus T_STEP (24) minus 12

ARMS = [('a0', 'iso', 24.0, 384, 0.10, 128, 0.0),
        ('a0p', 'iso', 16.0, 264, 0.10, 128, 0.0),
        ('a1', 'iso', 32.0, 384, 0.10, 128, -12.0),
        ('a2', 'iso', 28.0, 504, 0.10, 128, 6.0),
        ('ak', 'margin', 28.0, 104, 0.60, 512, 6.0)]


def windows(x_half, T_END):
    t_post = int(T_STEP + 1.5 * x_half) + 6
    return t_post, max(12, min(48, (T_END - t_post) // 3))


def load(tag, n):
    S, C = [], []
    for p in range(n):
        ps = os.path.join(DATA, f'leg_{p:04d}_step_{tag}.json')
        pc = os.path.join(DATA, f'leg_{p:04d}_ctrl_{tag}.json')
        if not (os.path.exists(ps) and os.path.exists(pc)):
            continue
        S.append(np.array(json.load(open(ps))['F']))
        C.append(np.array(json.load(open(pc))['F']))
    return np.stack(S) - np.stack(C)


def main():
    rep = json.load(open(os.path.join(DATA, 'pilot_report.json')))
    nmap = {a[0]: (int(rep['N_projected']) if a[0] == 'ak' else a[5])
            for a in ARMS}
    rng = np.random.default_rng(BOOT_SEED)

    tau = {}
    for tag, cls, xh, TE, beta, N, dt in ARMS:
        t_post, base = windows(xh, TE)
        D = load(tag, nmap[tag])
        m = D.shape[0]
        pre_pp = D[:, PRE].mean(axis=1)

        print("\n" + "=" * 74)
        print(f"ARM {tag}  ({cls}, Delta={dt:+.0f}, beta={beta:.2f}, "
              f"T_END={TE}, t_post={t_post}, pairs={m})")
        print("=" * 74)
        print(f"{'t':>5} {'t-T_STEP':>9} {'g(t)':>13} {'99% CI':>27} {'excl 0':>7}")

        ts = list(range(t_post, TE - WIDTH + 1, STEP))
        excl_run, first_stable = [], None
        for t in ts:
            per_pair = D[:, t:t + WIDTH].mean(axis=1) - pre_pp
            g = float(per_pair.mean())
            boots = np.array([per_pair[rng.integers(0, m, m)].mean()
                              for _ in range(NBOOT)])
            lo = float(np.percentile(boots, 0.5))
            hi = float(np.percentile(boots, 99.5))
            ex = not (lo <= 0.0 <= hi)
            excl_run.append((t, ex))
            print(f"{t:5} {t - T_STEP:9} {g:13.4e} "
                  f"[{lo:11.3e},{hi:11.3e}] {str(ex):>7}")

        # tau = smallest t-T_STEP where CI first excludes zero AND stays excluded
        for i, (t, ex) in enumerate(excl_run):
            if ex and all(e for _, e in excl_run[i:]):
                first_stable = t - T_STEP
                break
        tau[tag] = first_stable
        if cls == 'margin':
            print(f"  -> AK horizon covers only t-T_STEP <= {AK_HORIZON}; "
                  f"tau NOT computed (curve too short by design).")
        else:
            print(f"  -> tau({tag}) = "
                  f"{first_stable if first_stable is not None else 'NONE'}"
                  f" Moments post-step")

    print("\n" + "=" * 74)
    print("ESTABLISHMENT TIMES vs AK's ENTIRE POST-STEP HORIZON "
          f"({AK_HORIZON} Moments)")
    print("=" * 74)
    iso = [a[0] for a in ARMS if a[1] == 'iso']
    for t in iso:
        v = tau[t]
        mark = ("no stable establishment" if v is None
                else ("EXCEEDS AK's horizon" if v > AK_HORIZON
                      else "within AK's horizon"))
        print(f"  tau({t:4}) = {str(v):>6}   {mark}")

    vals = [tau[t] for t in iso]
    if any(v is None for v in vals):
        reading = "H-NO-CURVE"
    elif all(v > AK_HORIZON for v in vals):
        reading = "H-HORIZON-CONFIRMED"
    elif all(v <= AK_HORIZON for v in vals):
        reading = "H-HORIZON-REFUTED"
    else:
        reading = "H-ESTABLISHMENT-MIXED"

    print(f"\n>>> FROZEN READING: {reading}")
    if reading == "H-HORIZON-CONFIRMED":
        print("    AK could NOT have seen the response regardless of beta.")
        print("    Its null is uninformative about beta-scaling, and its S3-C")
        print("    reading must be WITHDRAWN from the item-1 test rather than")
        print("    counted as a failure. (Not enacted here - prereg S6.)")
    elif reading == "H-HORIZON-REFUTED":
        print("    AK had time to see a response and did not. H-BETA survives;")
        print("    the band's beta/0.10 scaling is implicated.")
    elif reading == "H-ESTABLISHMENT-MIXED":
        print("    Neither explanation eliminated. Successor must lengthen AK's")
        print("    horizon AND vary beta independently.")
    else:
        print("    The response is not a step-and-hold phenomenon; the S3-C")
        print("    control design is mis-conceived. EXHAUSTION TRIGGER FIRES")
        print("    (prereg S5) -> PANEL.")
    print("\nNO DISPOSITION PRODUCED. DISP-I3 stands. Item 1B remains OPEN.")
    print("=" * 74)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

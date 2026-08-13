#!/usr/bin/env python
"""Patch 3114 -- THE BOUNDARY LOCATION PASS + F-CLI-2-POINT (prereg:
3113, committed before this file existed). Instrument: the 3111
memoryless array, imported VERBATIM. Locators, escapes, and the point
confrontation exactly as frozen. Usage: pass a part number {1,2,3} to
split the compute; part 3 aggregates and runs the confrontation."""
import sys, json, os
import numpy as np
import importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location(
    "m3111", os.path.join(HERE, "3111_memoryless_campaign.py"))
m3111 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m3111)
run = m3111.run

STATE = "/tmp/3114_state.json"

def load():
    return json.load(open(STATE)) if os.path.exists(STATE) else {}

def save(d):
    json.dump(d, open(STATE, "w"))

def do_cells(cells, tag, st):
    for ds, sd, mixed, sig in cells:
        key = f"{tag}:{ds}:{sd}:{int(mixed)}:{sig}"
        if key in st:
            continue
        z = run(ds, seed=sd, mixed=mixed, sig_n=sig)
        st[key] = {k: (None if (isinstance(v, float) and not np.isfinite(v)) else v)
                   for k, v in z.items()}
        save(st)
        print(f"  {key}: phase={z['phase']} r={z['r']:.4f} stat={z['stat']:.2f} regen={z['regen']}")

part = int(sys.argv[1]) if len(sys.argv) > 1 else 3
st = load()

if part == 1:
    print("PART 1 -- primary grid, seed 5")
    do_cells([(ds, 5, True, 0.30) for ds in (1.5, 2.0, 2.5, 3.0, 3.5, 4.0)]
             + [(5.0, 5, True, 0.30)], "P", st)
elif part == 2:
    print("PART 2 -- primary grid, seed 11 + sensitivity + comparison")
    do_cells([(ds, 11, True, 0.30) for ds in (1.5, 2.0, 2.5, 3.0, 3.5, 4.0)], "P", st)
    do_cells([(2.5, 5, True, 0.15), (3.5, 5, True, 0.15)], "S", st)
    do_cells([(2.5, 5, False, 0.30), (3.5, 5, False, 0.30)], "C", st)
else:
    print("PART 3 -- aggregation, locators, and F-CLI-2-POINT (frozen rules)")
    grid = [1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0]
    print(f"\n{'d_s':>5} {'r(seed5)':>9} {'r(seed11)':>10} {'r(mean)':>8} {'phases':>22}")
    rmean = {}
    for ds in grid:
        vals, phases = [], []
        for sd in (5, 11):
            k = f"P:{ds}:{sd}:1:0.3"
            if k in st:
                vals.append(st[k]["r"]); phases.append(st[k]["phase"][:6])
        if vals:
            rmean[ds] = float(np.mean(vals))
            s5 = f"{vals[0]:.4f}" if len(vals) > 0 else "--"
            s11 = f"{vals[1]:.4f}" if len(vals) > 1 else "--"
            print(f"{ds:5.1f} {s5:>9} {s11:>10} {rmean[ds]:8.4f} {'/'.join(phases):>22}")
    # sensitivity + comparison lines
    for lbl, keys in (("sigma_n=0.15", [f"S:{d}:5:1:0.15" for d in (2.5, 3.5)]),
                      ("pure-e      ", [f"C:{d}:5:0:0.3" for d in (2.5, 3.5)])):
        got = [(k.split(":")[1], st[k]["r"]) for k in keys if k in st]
        print(f"  {lbl}: " + "  ".join(f"d={d}: r={r:.4f}" for d, r in got))

    # PRIMARY locator: r = 0.5 crossing, seed-averaged, linear interp
    ds_sorted = sorted(rmean)
    cross = None
    for a, b in zip(ds_sorted, ds_sorted[1:]):
        ra, rb = rmean[a], rmean[b]
        if (ra - 0.5) * (rb - 0.5) <= 0 and ra != rb:
            cross = a + (0.5 - ra) * (b - a) / (rb - ra)
            half = (b - a) / 2
            break
    # monotonicity check for the escape clause
    diffs = np.diff([rmean[d] for d in ds_sorted])
    monotone_dec = np.all(diffs <= 0.05)   # decreasing with d_s (5% tolerance)
    print("\nPRIMARY LOCATOR (r = 0.5 crossing, mixed, sigma_n = 0.30):")
    if cross is None or not monotone_dec:
        print("  UNLOCATED (no unique crossing / non-monotone) -> VERDICT DEFERRED per prereg escape.")
        sys.exit(0)
    print(f"  d_s* = {cross:.2f} +/- {half:.2f} l_P")

    # SECONDARY locator: FAITHFUL-attainability edge
    faith = {ds: all(st.get(f"P:{ds}:{sd}:1:0.3", {}).get("phase") == "FAITHFUL"
                     for sd in (5, 11)) for ds in ds_sorted[:-1]}
    lost = [d for d, ok in faith.items() if not ok]
    sec = f"below {min([d for d, ok in faith.items() if ok], default=float('nan'))}" \
          if lost == [] else f"edge near {max(lost, default=0)}-{min([d for d in ds_sorted if faith.get(d, False)], default=0)}"
    print(f"  SECONDARY (attainability): FAITHFUL lost at {lost if lost else 'no cell'} -> {sec}")

    # ---------------- F-CLI-2-POINT (fold verbatim, 3111 inputs) ------
    ALPHA = 1/137.035999
    BAND = (0.6, 0.9)
    r_e, x_q, eta_e, eta_g, s_m = 0.274, 0.700, 0.0700, 1.91, 1.797
    SE = dict(r=0.02, xq=0.02, ee=0.005, eg=0.05, s=0.05)
    def phi(re, xq, ee, eg, s, C):
        rq = min(re*xq/(1.0-xq), 1.0)
        return ((1-re)*ee + re*eg + C*((1-rq)*(s*ee) + rq*eg))/4.0
    def cli(P, a, d):
        return np.sqrt((4.0/3.0)*25.338*a*ALPHA*P)/d
    P_c = phi(r_e, x_q, eta_e, eta_g, s_m, 61.2)
    c_central = cli(P_c, 1.0, cross)
    # residual band
    import itertools
    lo, hi = 1e9, -1.0
    for re_, xq_, ee_, eg_, s_ in itertools.product(
            [r_e-SE['r'], r_e+SE['r']], [x_q-SE['xq'], x_q+SE['xq']],
            [eta_e-SE['ee'], eta_e+SE['ee']], [eta_g-SE['eg'], eta_g+SE['eg']],
            [s_m-SE['s'], s_m+SE['s']]):
        for C_ in (53.9, 68.5):
            P = phi(re_, xq_, ee_, eg_, s_, C_)
            for a_ in (0.78, 1.35):
                for d_ in (cross-half, cross+half):
                    c = cli(P, a_, d_)
                    lo, hi = min(lo, c), max(hi, c)
    print(f"\nF-CLI-2-POINT (fold verbatim; central inputs at d_s* = {cross:.2f}):")
    print(f"  central c_Li = {c_central:.4f};  residual band [{lo:.3f}, {hi:.3f}];  BAND [{BAND[0]}, {BAND[1]}]")
    print("="*68)
    if BAND[0] <= c_central <= BAND[1]:
        print("VERDICT: the central point falls INSIDE the band.")
        print("F-CLI-2-POINT: PASS (bracketed by the residual band, reported above).")
    elif c_central < BAND[0]:
        print(f"VERDICT: central below the band (shortfall x{(BAND[0]/c_central)**2:.2f} in rho).")
        print("F-CLI-2-POINT: FIRES (shortfall), in those words.")
    else:
        print(f"VERDICT: central above the band (overshoot x{(c_central/BAND[1])**2:.2f} in rho).")
        print("F-CLI-2-POINT: FIRES (overshoot), in those words.")
    print("="*68)

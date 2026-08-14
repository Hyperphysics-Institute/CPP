#!/usr/bin/env python
"""Patch 3126 -- THE CALIBRATION (per R-CC-CALIBRATE): the fold
INVERTED. Sweep the certified instrument (3124 run_cell, unchanged)
across spacings, measure the 3104 read-outs AT each spacing, fold each
(a = 1.0, C = 68.4841, the 3107/3112 mappings verbatim), and locate
d_s^emp where c_Li(d) = 0.8 (the adjudicated observed value, 0723).
Outputs: d_s^emp, its sensitivity band, and the first back-engineered
constants. Lambda enters ONLY as the anchor c_Li = 0.8, per ruling."""
import json, importlib.util, os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("m", os.path.join(HERE, "3124_fcli3_inputs.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
run_cell, phi, cli = m.run_cell, m.phi, m.cli

TARGET = 0.8
GRID = [2.6, 3.0, 3.5, 4.0, 4.5, 5.5]
st = {}
print(f"{'d_s':>5} {'r_e':>7} {'x_q':>6} {'eta_gas':>8} {'eta_e':>7} {'s':>6} {'Phi':>7} {'c_Li':>7}")
for ds in GRID:
    cells = [run_cell(ds, 5, sd) for sd in (5, 11)]
    z = {k: float(np.mean([c[k] for c in cells])) for k in cells[0]}
    P = phi(z["r_e"], z["x_q"], z["eta_e"], z["eta_gas"], z["s"])
    c = cli(P, 1.0, ds)
    st[str(ds)] = dict(z, Phi=P, c_Li=c)
    print(f"{ds:5.1f} {z['r_e']:7.4f} {z['x_q']:6.3f} {z['eta_gas']:8.3f} "
          f"{z['eta_e']:7.4f} {z['s']:6.3f} {P:7.2f} {c:7.4f}")
json.dump(st, open("/tmp/3126_cal.json", "w"))

ds_arr = np.array(GRID); c_arr = np.array([st[str(d)]["c_Li"] for d in GRID])
# locate c = 0.8 crossing (monotone-decreasing expected), linear interp
emp = None
for a, b in zip(range(len(GRID)-1), range(1, len(GRID))):
    ca, cb = c_arr[a], c_arr[b]
    if (ca - TARGET)*(cb - TARGET) <= 0 and ca != cb:
        emp = ds_arr[a] + (TARGET-ca)*(ds_arr[b]-ds_arr[a])/(cb-ca)
        break
print(f"\nCALIBRATION: c_Li(d) = {TARGET} at  d_s^emp = "
      f"{'NOT BRACKETED BY GRID' if emp is None else f'{emp:.3f} l_P'}")
if emp is not None:
    # sensitivity: arrangement bracket + alpha_s +/-10% shift the target crossing
    for a_, lbl in ((0.78, "a=0.78"), (1.35, "a=1.35")):
        cs = c_arr*np.sqrt(a_)
        e2 = None
        for i in range(len(GRID)-1):
            if (cs[i]-TARGET)*(cs[i+1]-TARGET) <= 0 and cs[i] != cs[i+1]:
                e2 = ds_arr[i] + (TARGET-cs[i])*(ds_arr[i+1]-ds_arr[i])/(cs[i+1]-cs[i]); break
        print(f"  [{lbl}] d_s^emp = {'unbracketed' if e2 is None else f'{e2:.3f}'}")
    print(f"  floor offset: d_s^emp - d_s*(2.450) = {emp-2.450:+.3f} l_P "
          f"(the D-EQUIL-KINETICS target, fixed today)")
    # back-engineered constants at the calibrated spacing (interp of nearest cells)
    lo = max([d for d in GRID if d <= emp]); hi = min([d for d in GRID if d >= emp])
    f = 0.0 if hi == lo else (emp-lo)/(hi-lo)
    be = {k: (1-f)*st[str(lo)][k] + f*st[str(hi)][k]
          for k in ("r_e", "x_q", "eta_gas", "eta_e", "s", "Phi")}
    print("  back-engineered Sea constants at d_s^emp:")
    for k, v in be.items():
        print(f"    {k:>8} = {v:.4f}")
    # exit-anchor consonance (3098 mapping): T_exit/T0 = 1e30 * d_s/l_P
    print(f"  3098 exit-anchor mapping: d_s^emp -> T_exit ~ {emp:.2f}e30 * T0 "
          f"(vs the 3098 working decade [6,16] -- consonance reported, not enforced)")

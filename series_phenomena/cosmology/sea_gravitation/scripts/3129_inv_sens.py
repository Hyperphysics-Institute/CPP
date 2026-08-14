#!/usr/bin/env python
"""Patch 3129 -- OBL-INV-SENS: the blinded fold-inversion sensitivity
suite. BLINDING: this analysis reports Delta d_s^emp per perturbation;
no band, no verdict, nothing to steer -- the calibration is already
frozen and labeled. Perturbations: (1) sigma_n in {0.15, 0.45} vs the
0.30 operating point; (2) the gas-threshold definition 0.75*ds vs the
standard 0.5*ds; (3) the Phi-plateau regime-mixing check: the
bound/gas decomposition of Phi under all variants."""
import json, importlib.util, os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("m", os.path.join(HERE, "3124_fcli3_inputs.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
run_cell, phi, cli = m.run_cell, m.phi, m.cli

GRID = [2.6, 3.0, 3.5, 4.0, 4.5, 5.5]
TARGET = 0.8
import sys
STATE = "/tmp/3129_sens.json"
st = json.load(open(STATE)) if os.path.exists(STATE) else {}
sigs = [float(x) for x in sys.argv[1:]] or [0.30, 0.15, 0.45]
for sig in sigs:
    for ds in GRID:
        key = f"{sig}:{ds}"
        if key in st:
            continue
        st[key] = run_cell(ds, 5, 5, sig_n=sig)
        json.dump(st, open(STATE, "w"))
        print(f"    done {key}")
if len(sys.argv) > 1:
    sys.exit(0)   # run-only invocation; analysis in the final bare call

def invert(curve):
    ds_a = np.array(GRID); c_a = np.array(curve)
    for i in range(len(GRID)-1):
        if (c_a[i]-TARGET)*(c_a[i+1]-TARGET) <= 0 and c_a[i] != c_a[i+1]:
            return float(ds_a[i] + (TARGET-c_a[i])*(ds_a[i+1]-ds_a[i])/(c_a[i+1]-c_a[i]))
    return None

print("== (1) sigma_n bracket ==")
base_emp = None
for sig in (0.30, 0.15, 0.45):
    cs, Ps = [], []
    for ds in GRID:
        z = st[f"{sig}:{ds}"]
        P = phi(z["r_e"], z["x_q"], z["eta_e"], z["eta_gas"], z["s"])
        Ps.append(P); cs.append(cli(P, 1.0, ds))
    emp = invert(cs)
    if sig == 0.30: base_emp = emp
    d = "--" if (emp is None or base_emp is None) else f"{emp-base_emp:+.3f}"
    print(f"  sigma_n={sig:.2f}: Phi(range)=[{min(Ps):.1f},{max(Ps):.1f}]  "
          f"d_s^emp={'unbracketed' if emp is None else f'{emp:.3f}'}  Delta={d}")

print("== (2) gas-threshold variant (0.75 ds vs 0.50 ds), sigma_n=0.30 ==")
cs75 = []
for ds in GRID:
    z = st[f"0.3:{ds}"]
    P = phi(z["r_e75"], z["x_q75"], z["eta_e75"], z["eta_gas75"], z["s75"])
    cs75.append(cli(P, 1.0, ds))
emp75 = invert(cs75)
print(f"  threshold 0.75ds: d_s^emp={'unbracketed' if emp75 is None else f'{emp75:.3f}'}  "
      f"Delta={'--' if emp75 is None else f'{emp75-base_emp:+.3f}'}")

print("== (3) Phi-plateau regime-mixing check (bound/gas decomposition, sigma_n=0.30) ==")
print(f"  {'ds':>5} {'Phi_total':>9} {'Phi_bound':>9} {'Phi_gas':>8} {'gas_share':>9}")
for ds in GRID:
    z = st[f"0.3:{ds}"]
    re_, xq_ = z["r_e"], z["x_q"]
    rq = min(re_*xq_/(1-xq_), 1.0)
    C = 68.4841
    Pb = ((1-re_)*z["eta_e"] + C*(1-rq)*(z["s"]*z["eta_e"]))/4.0
    Pg = (re_*z["eta_gas"] + C*rq*z["eta_gas"])/4.0
    print(f"  {ds:5.1f} {Pb+Pg:9.2f} {Pb:9.3f} {Pg:8.2f} {Pg/(Pb+Pg):9.3f}")
print("  [the plateau's composition: if Phi_total stays flat while the")
print("   components move, the compensation is structural; its robustness")
print("   under (1)-(2) above is the regime-mixing verdict]")

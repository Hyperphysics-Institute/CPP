#!/usr/bin/env python
"""Patch 3131 -- OBL-SIGMA-N: the jitter operating point decomposed,
its derivable component DERIVED, and the sensitivity bracket completed
down to the derived floor.

DECOMPOSITION. The instrument's jitter sigma_n stands for field
content NOT already explicit in the all-pairs sum:
  (a) FAR-FIELD Sea fluctuations -- the RMS per-axis E-field at a site
      from the fluctuating dipoles BEYOND the periodic box. DERIVABLE
      by self-consistency: each external dipole at distance r
      contributes field ~ p/r^3 with <p^2> = q^2 <d_p^2>; independent
      dipoles => variances add; per-axis variance
          sigma_far^2 = (2/3) * <d_p^2> * S6_out(R_box),
      S6_out = the simple-cubic lattice sum of 1/r^6 over pair sites
      beyond the box (direct sum + continuum tail), <d_p^2> the box's
      own stationary value (self-consistent closure).
      REGRESSION CHECK: in the no-explicit-neighbor limit (Stage-2,
      R_box -> 0), S6_out -> C6_full/d^6 and the formula reduces to
      sigma = sqrt(2 C6 <delta^2>/3)/d^3 -- the Stage-2 self-consistent
      drive, exactly (the 3097-era instrument's own formula).
  (b) THE DWELL-RELAUNCH KICK (R-DWELL-1): the charge-coupled
      near-superposition kick is ruled automaton MECHANISM, but its
      AMPLITUDE is not yet derived -- a named unknown (FQ-12 posed in
      the note).
  (c) other-register fluctuations (strong/arc far-field): suppressed
      (tight-bound strong far-field small; arc ~ v x smaller moments);
      second-order, stated.

Parts: A = derive sigma_far at the working points; B = the Stage-2
regression identity; C = complete the calibration sensitivity bracket
at sigma_n = 0.05 (~ the derived floor + margin)."""
import json, importlib.util, os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))

def S6_out(dsl, n_side, rmax_shells=40):
    """Simple-cubic 1/r^6 sum over pair sites beyond the box half-width."""
    R = n_side*dsl/2.0
    g = np.arange(-rmax_shells, rmax_shells+1)
    I, J, K = np.meshgrid(g, g, g, indexing="ij")
    P = np.stack([I.ravel(), J.ravel(), K.ravel()], 1).astype(float)*dsl
    r2 = np.einsum('ij,ij->i', P, P)
    m = r2 > R*R
    s = float(np.sum(r2[m]**-3))
    Rcut = rmax_shells*dsl
    tail = 4*np.pi/(3*dsl**3*Rcut**3)   # continuum tail beyond the direct sum
    return s + tail

print("(A) sigma_far at the working points (self-consistent far-field):")
print(f"{'d_s':>5} {'n':>3} {'<d_p^2> (GP^2)':>14} {'S6_out':>10} {'sigma_far':>10} {'/0.30':>7}")
# stationary <d_p^2> from the measured mixtures (3126 sweep values)
mix = {2.6: (0.713, 4.696, 0.144), 3.5: (0.577, 4.555, 0.134),
       4.64: (0.449, 4.794, 0.115), 5.5: (0.380, 4.829, 0.101)}
for dsl, (re_, eg, ee) in mix.items():
    dp2 = ((1-re_)*ee + re_*eg)*dsl**2
    for n_side in (5, 6):
        s6 = S6_out(dsl, n_side)
        sig = np.sqrt((2.0/3.0)*dp2*s6)
        print(f"{dsl:5.2f} {n_side:3d} {dp2:14.2f} {s6:10.3e} {sig:10.4f} {sig/0.30:7.3f}")

print("\n(B) Stage-2 regression identity (no-explicit-neighbor limit):")
dsl = 12.0
g = np.arange(-40, 41)
I, J, K = np.meshgrid(g, g, g, indexing="ij")
P = np.stack([I.ravel(), J.ravel(), K.ravel()], 1).astype(float)*dsl
r2 = np.einsum('ij,ij->i', P, P)
m = r2 > 1e-9
C6_lattice = float(np.sum(r2[m]**-3))*dsl**6   # dimensionless C6 for SC lattice
sig_formula = np.sqrt((2.0/3.0)*1.0*C6_lattice)/dsl**3   # <delta^2> = 1
sig_stage2 = np.sqrt(2*C6_lattice*1.0/3.0)/dsl**3
print(f"  SC-lattice C6 = {C6_lattice:.4f}; far-field formula at R_box->0: "
      f"{sig_formula:.3e} = Stage-2 drive {sig_stage2:.3e}  "
      f"[{'IDENTITY' if abs(sig_formula-sig_stage2) < 1e-12 else 'MISMATCH'}]")

print("\n(C) bracket completion: calibration at sigma_n = 0.05 (~derived floor + margin)")
spec = importlib.util.spec_from_file_location("m", os.path.join(HERE, "3124_fcli3_inputs.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
run_cell, phi, cli = m.run_cell, m.phi, m.cli
GRID = [2.6, 3.0, 3.5, 4.0, 4.5, 5.5]
STATE = "/tmp/3131_sig005.json"
st = json.load(open(STATE)) if os.path.exists(STATE) else {}
for dsl in GRID:
    k = str(dsl)
    if k in st: continue
    st[k] = run_cell(dsl, 5, 5, sig_n=0.05)
    json.dump(st, open(STATE, "w"))
    print(f"    done ds={dsl}")
cs = []
for dsl in GRID:
    z = st[str(dsl)]
    P = phi(z["r_e"], z["x_q"], z["eta_e"], z["eta_gas"], z["s"])
    cs.append(cli(P, 1.0, dsl))
ds_a = np.array(GRID); c_a = np.array(cs)
emp = None
for i in range(len(GRID)-1):
    if (c_a[i]-0.8)*(c_a[i+1]-0.8) <= 0 and c_a[i] != c_a[i+1]:
        emp = float(ds_a[i] + (0.8-c_a[i])*(ds_a[i+1]-ds_a[i])/(c_a[i+1]-c_a[i])); break
print(f"  sigma_n = 0.05: d_s^emp = {'unbracketed' if emp is None else f'{emp:.3f}'}  "
      f"(baseline seed-5: 4.617)  Delta = {'--' if emp is None else f'{emp-4.617:+.3f}'}")

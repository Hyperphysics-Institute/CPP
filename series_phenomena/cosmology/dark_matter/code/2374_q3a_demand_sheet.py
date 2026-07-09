#!/usr/bin/env python3
"""Patch 2374 -- Q3a: THE DEMAND SHEET (Q3 opened on founder GO). What must the
substrate derivation produce? All numbers from REGISTERED relations + the 2372
pipeline; no new physics, no fabricated couplings (0865 discipline).

PRE-REGISTERED (fixed before run):
  (A) FREEZE-OUT INVERSION AT SURVIVOR N: the registered 0881 inverse map
      E_bond/kT_form = 2 ln(N/sqrt(phi)), phi bracket recomputed exactly as
      0881 does, evaluated at the survivor demand N in [3, 6] (vs the
      registered band N in [5, 60] -> ratio 24-41). Question: does the
      small-N demand stay inside the fragmentation-window closure
      (E_bond in [0.78 keV, 1.95 MeV] at kT_form <= 19 keV)?
  (B) ISODESMIC BASELINE: equilibrium (Flory) linear self-assembly gives
      number dist P(N) = (1-x) x^(N-1), mass fraction w(N) = N x^(N-1)(1-x)^2.
      At number-average <N>_n in {3, 4.5, 6} report w(1), w(2), w(3-6),
      w(>6). This is death mode (ii) made quantitative: generic equilibrium
      POPULATES the dimer; the sheet records how much.
  (C) TOLERABLE CONTAMINATION AT THE CORRIDOR POINT (S_c = 0.012,
      rho = 0.3): dimer (N=2, folded, L=1.15 fm) and monomer (N=1, POINT
      potential -- L=(N-1)*1.15=0, folded shell undefined at L=0, convention
      stated) per-bin counts at reference mass fraction f=1 through the 2372
      pipeline; counts are exactly linear in f (NDM prefactor), so
      f_max = min over bins of threshold/predicted(f=1). Both signs reported
      (sign is a Q3b deliverable, not a choice). THE DEMAND: the derived
      distribution's w(2) must be < f2_max and w(1) < f1_max while keeping
      the N=3-6 carriers at their corridor abundances. The suppression
      demand beyond generic equilibrium = w(2)_isodesmic / f2_max.
  READINGS, hurting-first:
    (thin) suppression demand >= 10x-class and/or the small-N freeze-out
           ratio exits the fragmentation closure -> the derivation needs a
           strong specific mechanism (nucleation barrier / ring-closure);
           the generic-equilibrium death mode is quantitatively ARMED.
    (mild) demands O(1)-few -> corridor reachable from near-isodesmic
           kinetics with modest suppression.
    Either way the sheet is the deliverable; NO verdict moves.
  VERIFY (3, pre-stated):
    (V-a) 0881 REPRODUCTION: same phi bracket + N in [5,60] returns the
          registered ratio window ~24-41 (integer round).
    (V-b) LINEARITY: dimer counts at f=0.5 = exactly half of f=1
          (rel dev < 1e-9), validating the f_max linear inversion.
    (V-c) 2372 ANCHOR: N=3 at its Q1 fraction, attractive, corridor point
          reproduces the stored 2372 XQC-SAFE verdict fresh.
"""
import math, sys, json, io, os, contextlib

here = os.path.dirname(os.path.abspath(__file__))
os.chdir(os.path.dirname(here))
src = open('code/1879_xqc_recomputation.py').read().split("if __name__")[0]
g = {}; exec(src, g)
M_EL = g['M_EL']; E_C = g['E_C']; BINS = g['BINS']; SAT = g['SAT']

results = {"prereg": "header", "V": {}, "A_freezeout": {}, "B_isodesmic": {},
           "C_contamination": {}}

# ================= (A) freeze-out inversion =================
# phi bracket exactly as 0881
rho_DM = 1.4e-6; kT_now = 2.35e-13; kT_form_max = 19e-3
phis = []
for mel in (1.0, 2.0):
    n_now = rho_DM / mel
    for kTf in (5e-3, kT_form_max):
        zfac = (kTf / kT_now) ** 3
        for V in (1e-39, 1e-36):
            phis.append(n_now * zfac * V)
phi_lo, phi_hi = min(phis), max(phis)
ratio = lambda N, phi: 2 * math.log(N / math.sqrt(phi))
# V-a: reproduce the registered window at N in [5, 60]
r_reg_lo, r_reg_hi = ratio(5.0, phi_hi), ratio(60.0, phi_lo)
va_ok = (round(r_reg_lo) == 24 and round(r_reg_hi) == 41)
results["V"]["a_0881_reproduction"] = {"lo": r_reg_lo, "hi": r_reg_hi, "ok": va_ok}
print("V-a 0881 reproduction: N=[5,60] -> ratio %.1f-%.1f (registered ~24-41) -> %s"
      % (r_reg_lo, r_reg_hi, "OK" if va_ok else "FAIL"))
# survivor demand
r_lo, r_hi = ratio(3.0, phi_hi), ratio(6.0, phi_lo)
results["A_freezeout"] = {"phi": [phi_lo, phi_hi], "ratio_survivors": [r_lo, r_hi],
                          "ratio_registered_band": [r_reg_lo, r_reg_hi]}
print("\n(A) survivor freeze-out demand: N=[3,6] -> E_bond/kT_form = %.1f - %.1f"
      % (r_lo, r_hi))
print("    closure check (E_bond in [0.78 keV, 1.95 MeV] at kT_form <= 19 keV):")
win = (0.78e-3, 1.95)
rows = []
for kTf in (1e-3, 5e-3, kT_form_max):
    for r in (r_lo, r_hi):
        Eb = r * kTf; ok = win[0] <= Eb <= win[1]
        rows.append((kTf, r, Eb, ok))
        print("    kT_form=%5.0f keV  ratio=%4.1f  E_bond=%8.4f MeV  in-window: %s"
              % (kTf * 1e3, r, Eb, "YES" if ok else "no"))
results["A_freezeout"]["closure_rows"] = rows
results["A_freezeout"]["closes"] = any(ok for *_, ok in rows)

# ================= (B) isodesmic baseline =================
print("\n(B) isodesmic (Flory) baseline mass fractions:")
def flory(Nn):
    x = 1 - 1.0 / Nn
    w = lambda N: N * x ** (N - 1) * (1 - x) ** 2
    w36 = sum(w(N) for N in (3, 4, 5, 6))
    wgt6 = 1 - w(1) - w(2) - w36
    return {"x": x, "w1": w(1), "w2": w(2), "w3_6": w36, "w_gt6": wgt6}
for Nn in (3.0, 4.5, 6.0):
    d = flory(Nn)
    results["B_isodesmic"]["Nn=%s" % Nn] = d
    print("    <N>_n=%.1f: w(1)=%.4f  w(2)=%.4f  w(3-6)=%.4f  w(>6)=%.4f"
          % (Nn, d["w1"], d["w2"], d["w3_6"], d["w_gt6"]))

# ================= (C) tolerable contamination =================
def pin(N, sc, f_ab, rho_gev, folded):
    g['N_ROD'] = N; g['M_ROD'] = N * M_EL
    g['E_RN'] = (3.0 * E_C / (8 * N)) * sc
    g['L_ROD'] = max((N - 1) * 1.15, 1e-9)
    g['NDM'] = (f_ab * rho_gev * 1e3 / (N * M_EL)) * 2.5e10
    assert g['E_RN'] == 3.0 * 0.30 / (8 * N) * sc
    return folded

def counts_at(N, sign, sc, f_ab, rho, folded):
    pin(N, sc, f_ab, rho, folded)
    with contextlib.redirect_stdout(io.StringIO()):
        c, sat = g['predicted_bins'](-1 if sign == "attractive" else 1, folded)
    return c, sat

SC, RHO = 0.012, 0.3
print("\n(C) tolerable contamination at the corridor point (S_c=0.012, rho=0.3):")
for label, N, folded in (("dimer  N=2", 2, True), ("monomer N=1", 1, False)):
    for sign in ("attractive", "repulsive"):
        c1, sat1 = counts_at(N, sign, SC, 1.0, RHO, folded)
        # V-b linearity (dimer attractive only, pre-registered spot check)
        if N == 2 and sign == "attractive":
            c05, sat05 = counts_at(N, sign, SC, 0.5, RHO, folded)
            rel = max(abs(a * 0.5 - b) / max(b, 1e-30) for a, b in zip(c1 + [sat1], c05 + [sat05]))
            vb_ok = rel < 1e-9
            results["V"]["b_linearity"] = {"max_rel_dev": rel, "ok": vb_ok}
            print("    V-b linearity: f=0.5 vs 0.5*f=1, max rel dev %.1e -> %s"
                  % (rel, "OK" if vb_ok else "FAIL"))
        fmax, bind = 1e30, None
        for (lo, hi, obs, f), p in zip(BINS, c1):
            if p <= 0: continue
            th = obs + 5 * math.sqrt(obs + 1)
            if th / p < fmax: fmax, bind = th / p, "%d-%d eV" % (lo, hi)
        if sat1 > 0:
            th = SAT[1] + 5 * math.sqrt(SAT[1] + 1)
            if th / sat1 < fmax: fmax, bind = th / sat1, ">4 keV"
        results["C_contamination"]["%s,%s" % (label.strip(), sign)] = \
            {"f_max": fmax, "binding_bin": bind}
        print("    %-11s %-10s  f_max = %.4f  (binding bin: %s)"
              % (label, sign, fmax, bind))

# V-c: 2372 anchor -- N=3 at its Q1 fraction, attractive, corridor point
Q1 = json.load(open('code/2371_results.json'))
NA, NB, gA2, gB2, w, Rs = Q1["audited_central"]["best_params"]
f3 = w  # central species A = N=3 at fraction w
c, sat = counts_at(3, "attractive", SC, f3, RHO, True)
viol = sum(1 for (lo, hi, obs, ff), p in zip(BINS, c)
           if p > obs + 5 * math.sqrt(obs + 1))
sviol = sat > SAT[1] + 5 * math.sqrt(SAT[1] + 1)
stored = json.load(open('code/2372_results.json'))["perbin"][
    "central,N=3,f=%.4f,attractive,Sc=0.012,rho=0.3" % f3]["verdict"]
fresh = "XQC-SAFE" if (viol == 0 and not sviol) else "EXCLUDED-class"
vc_ok = (fresh == stored == "XQC-SAFE")
results["V"]["c_2372_anchor"] = {"fresh": fresh, "stored": stored, "ok": vc_ok}
print("\nV-c 2372 anchor (central N=3 @ corridor point): fresh=%s stored=%s -> %s"
      % (fresh, stored, "OK" if vc_ok else "FAIL"))

# ================= the demand sheet =================
f2 = min(results["C_contamination"]["dimer  N=2,%s" % s]["f_max"]
         for s in ("attractive", "repulsive"))
f2_loose = max(results["C_contamination"]["dimer  N=2,%s" % s]["f_max"]
               for s in ("attractive", "repulsive"))
f1 = min(results["C_contamination"]["monomer N=1,%s" % s]["f_max"]
         for s in ("attractive", "repulsive"))
w2_iso = {k: v["w2"] for k, v in results["B_isodesmic"].items()}
supp = {k: v / f2 for k, v in w2_iso.items()}
supp_loose = {k: v / f2_loose for k, v in w2_iso.items()}
results["demand_sheet"] = {
    "dimer_mass_fraction_max": {"binding_sign": f2, "loose_sign": f2_loose},
    "monomer_mass_fraction_max": f1,
    "suppression_beyond_isodesmic_w2_over_f2max": {"binding": supp, "loose": supp_loose},
    "freezeout_ratio_demand": [r_lo, r_hi],
    "coupling_demand": "S_c in [0.012, 0.0125-0.0215] per 2373 walls (sign/composition dependent)",
    "sign_demand": "Q3b deliverable: substrate must state the rod-nucleus sign",
}
print("\n" + "=" * 78)
print(" THE DEMAND SHEET (what a viable derived population must satisfy):")
print("=" * 78)
print(" D1 freeze-out ratio  : E_bond/kT_form = %.1f - %.1f (survivor N=3-6)" % (r_lo, r_hi))
print(" D2 dimer contamination: w(2) < %.4f (binding sign) / < %.4f (loose sign)" % (f2, f2_loose))
print(" D3 monomer contamination: w(1) < %.4f" % f1)
print(" D4 suppression beyond generic equilibrium (w2_iso/f2_max, binding sign):")
for k in sorted(supp): print("      %-9s: x%.1f" % (k, supp[k]))
print(" D5 coupling: land S_c at the island floor (walls per 2373)")
print(" D6 sign: derived, not chosen (corridor width depends on it x2-15)")
results["V"]["passed"] = "%d/3" % (int(va_ok) + int(results["V"]["b_linearity"]["ok"]) + int(vc_ok))
print("\nVERIFY:", results["V"]["passed"])
json.dump(results, open("code/2374_results.json", "w"), indent=1)
print("wrote code/2374_results.json")

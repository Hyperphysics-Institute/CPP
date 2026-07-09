#!/usr/bin/env python3
"""Patch 2374 companion (expansion OWNED, 2366/2366b precedent): the D2/D3
contamination bounds in 2374_q3a_demand_sheet.py are SINGLE-CONTAMINANT bounds
-- each contaminant tested against the full bin threshold alone. But the
pre-registration's own words ("while keeping the N=3-6 carriers at their
corridor abundances") demand the JOINT budget: carriers + contaminant must
stay under threshold TOGETHER, per bin. This script computes it. Correction
pre-stated before running: joint bounds are NECESSARILY tighter; the knife-edge
corner (extended-attractive, headroom x1.07) should have almost no room.

  f2_max_joint(comp, sign) = min over bins (threshold_bin - carriers_bin)
                                            / dimer_bin(f=1)
  (carriers at their Q1 fractions, corridor point S_c=0.012, rho=0.3;
   monomer analogous; dimer and monomer budgets quoted separately -- their
   binding bins differ (36-128 vs 29-36 eV) but any joint (w1, w2) pair must
   satisfy BOTH rows plus the shared-bin linear combination; the two-row quote
   is the rectangle bound, stated as such.)
"""
import math, sys, json, io, os, contextlib

here = os.path.dirname(os.path.abspath(__file__))
os.chdir(os.path.dirname(here))
src = open('code/1879_xqc_recomputation.py').read().split("if __name__")[0]
g = {}; exec(src, g)
M_EL = g['M_EL']; E_C = g['E_C']; BINS = g['BINS']; SAT = g['SAT']

Q1 = json.load(open('code/2371_results.json'))
comps = {}
for fname, tag in (("audited_extended", "extended"), ("audited_central", "central")):
    NA, NB, gA2, gB2, w, Rs = Q1[fname]["best_params"]
    comps[tag] = [(int(round(NA)), w), (int(round(NB)), 1.0 - w)]

def counts_at(N, sign, f_ab, folded=True):
    g['N_ROD'] = N; g['M_ROD'] = N * M_EL
    g['E_RN'] = (3.0 * E_C / (8 * N)) * 0.012
    g['L_ROD'] = max((N - 1) * 1.15, 1e-9)
    g['NDM'] = (f_ab * 0.3 * 1e3 / (N * M_EL)) * 2.5e10
    assert g['E_RN'] == 3.0 * 0.30 / (8 * N) * 0.012
    with contextlib.redirect_stdout(io.StringIO()):
        c, sat = g['predicted_bins'](-1 if sign == "attractive" else 1, folded)
    return c, sat

TH = [obs + 5 * math.sqrt(obs + 1) for (lo, hi, obs, f) in BINS]
THS = SAT[1] + 5 * math.sqrt(SAT[1] + 1)

out = {"note": "joint rectangle bounds at corridor point (0.012, 0.3)"}
print("JOINT contamination budgets (carriers at Q1 fractions occupy the bins first):")
print("%-9s %-10s %10s %10s   %s" % ("comp", "sign", "f2_joint", "f1_joint", "binding bins (dimer; monomer)"))
for tag, sp in comps.items():
    for sign in ("attractive", "repulsive"):
        carrier = [0.0] * len(BINS); carrier_sat = 0.0
        for N, f in sp:
            c, s = counts_at(N, sign, f)
            carrier = [a + b for a, b in zip(carrier, c)]; carrier_sat += s
        d1, ds = counts_at(2, sign, 1.0, folded=True)
        m1, ms = counts_at(1, sign, 1.0, folded=False)
        def joint_max(cont, cont_sat):
            fm, bind = 1e30, None
            for i, p in enumerate(cont):
                if p <= 0: continue
                room = TH[i] - carrier[i]
                if room / p < fm:
                    fm, bind = room / p, "%d-%d" % (BINS[i][0], BINS[i][1])
            if cont_sat > 0 and (THS - carrier_sat) / cont_sat < fm:
                fm, bind = (THS - carrier_sat) / cont_sat, ">4keV"
            return max(fm, 0.0), bind
        f2j, b2 = joint_max(d1, ds)
        f1j, b1 = joint_max(m1, ms)
        out["%s,%s" % (tag, sign)] = {"f2_joint": f2j, "f1_joint": f1j,
                                      "dimer_bind": b2, "monomer_bind": b1}
        print("%-9s %-10s %10.4f %10.4f   (%s; %s)" % (tag, sign, f2j, f1j, b2, b1))

json.dump(out, open("code/2374b_results.json", "w"), indent=1)
print("wrote code/2374b_results.json")

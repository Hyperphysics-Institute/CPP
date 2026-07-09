#!/usr/bin/env python3
"""Patch 2366 -- STAGE 2 of the F-DM3-4 rate computation: sigma_dimer via the
P2-channel machinery at A_dimer (the 1879/1888 partial-wave pipeline at N=2).

PRE-REGISTERED (fixed before execution):
  Dimer: N=2, M=2*1408=2816 MeV, L=(N-1)*1.15=1.15 fm, E_rN=3*E_c/(8N)=0.05625 MeV.
  Coupling: island convention per 1888 -- effective coupling = E_rN * S_c,
    S_c in {0.012, 0.035, 0.05} (post-DAMIC island edges + ruling point).
  Both signs (attractive/repulsive); folded rod-extension (dimer ~point anyway).
  Abundance: mass fraction {0.94, 0.99} x rho_chi {0.2, 0.3, 0.6} GeV/cm^3.
  sigma_T (momentum-transfer) at v=300 km/s on A in {14.5 atm, 22 rock, 28 Si};
  per-nucleon-equivalent sigma_eff = sigma_A/[A^2 (mu_A/mu_n)^2]  (Stage-1 convention).
  XQC: 1879 pinned exposure verbatim, N_dm rescaled by (f_ab*rho/M_dimer)/(0.3e3/M_rod).
  OUTCOME MAP (graded as written):
    O-A sigma_eff < deep ceilings AND > 1e-38: ACTIVATES underground.
    O-B sigma_eff > ceilings: underground blind -> XQC counts decide:
       B1 > 314 (folded kill-high) at ALL island x abundance pts -> dimer corner
          EXCLUDED-class by 2007 data (CANDIDATE exit-(d) firing, hurting direction;
          founder + panel confirmation required before any verdict moves).
       B2 in [5.3, 105] folded confirm band -> XQC-channel-active (and candidate
          explanation of the F5 excess).  B3 in (105, 314): tension, stated.
       B4 < 5.3: XQC-blind -> gap regime stated honestly.
    O-C sigma_eff < 1e-42: fails-as-too-weak, deactivation path.
  HURTING-FIRST: B1 test at S_c=0.05 x f=0.99 x rho=0.6 computed first.
"""
import math, sys, json, io, contextlib

# import the 1879 machinery (1888's own pattern)
sys.path.insert(0, 'code')
src = open('code/1879_xqc_recomputation.py').read().split("if __name__")[0]
g = {}
exec(src, g)

# ---- re-pin globals for the DIMER ----
g['N_ROD'] = 2
g['M_ROD'] = 2 * g['M_EL']                 # 2816 MeV
g['E_RN']  = 3.0 * g['E_C'] / (8 * 2)      # 0.05625 MeV
g['L_ROD'] = 1.15
M = g['M_ROD']; AMU = g['AMU']; HBARC = g['HBARC']; CKMS = g['CKMS']

results = {"prereg": "see header", "sigma_T": {}, "xqc": {}}
VREF = 300.0
kv = lambda mu_, v: mu_ * (v/CKMS) / HBARC   # fm^-1

def sigma_T(A_nuc, m_nuc, sign, sc):
    """momentum-transfer cross section, fm^2, at v=300 km/s."""
    mu_ = M*m_nuc/(M+m_nuc)
    k = kv(mu_, VREF)
    V = g['make_V'](A_nuc, sign)
    Ceff = sc
    Vs = lambda r: Ceff * V(r)
    lmax = max(12, int(k*60)+10)
    d = g['phase_shifts'](Vs, mu_, k, lmax)
    # sigma_T = 4pi/k^2 sum (l+1) sin^2(d_l - d_{l+1})
    s = 0.0
    for l in range(len(d)-1):
        s += (l+1) * math.sin(d[l]-d[l+1])**2
    return 4*math.pi/(k*k) * s   # fm^2

mu_n = M*0.9383e3/(M+0.9383e3)
CEIL = {"SNOLAB": 8.9e-32, "LSM": 1.1e-31, "MINOS": 2.3e-30, "surface": 6.7e-29}
targets = {"atm14.5": (14.5, 14.5*AMU), "rock22": (22.0, 22.0*AMU), "Si28": (28.09, 28.09*AMU)}
for sign, sgn in (("attractive",-1), ("repulsive",+1)):
    for sc in (0.012, 0.035, 0.05):
        for tn,(A,mA) in targets.items():
            st = sigma_T(A, mA, sgn, sc) * 1e-26      # fm^2 -> cm^2
            mu_A = M*mA/(M+mA)
            seff = st / (A**2 * (mu_A/mu_n)**2)
            results["sigma_T"][f"{sign},Sc={sc},{tn}"] = {"sigma_A_cm2": st, "sigma_eff_cm2": seff}

# ---- XQC counts for the dimer at implied abundance ----
def xqc_counts(sign, sc, f_ab, rho_gev):
    g['E_RN'] = (3.0*g['E_C']/16) * sc
    g['NDM']  = (f_ab * rho_gev * 1e3 / M) * 2.5e10
    with contextlib.redirect_stdout(io.StringIO()):
        counts, sat = g['predicted_bins'](-1 if sign=="attractive" else 1, True)
    g['E_RN'] = 3.0*g['E_C']/16
    return sum(counts) + sat

# hurting-first: B1 test at max coupling x max abundance
order = [(0.05,0.99,0.6),(0.05,0.94,0.2),(0.035,0.99,0.6),(0.035,0.94,0.2),
         (0.012,0.99,0.6),(0.012,0.94,0.2),(0.035,0.94,0.3)]
for sign in ("attractive","repulsive"):
    for sc,f,rho in order:
        c = xqc_counts(sign, sc, f, rho)
        results["xqc"][f"{sign},Sc={sc},f={f},rho={rho}"] = c

# ---- grading ----
seff_all = [v["sigma_eff_cm2"] for k,v in results["sigma_T"].items()]
above_all_ceilings = all(s > CEIL["surface"] for s in seff_all)
below_deep = all(s < CEIL["SNOLAB"] for s in seff_all)
xq = results["xqc"]; xv = list(xq.values())
B1 = all(v > 314 for v in xv)
B2 = all(5.3 <= v <= 105 for v in xv)
B4 = all(v < 5.3 for v in xv)
results["grading"] = {
 "sigma_eff_range_cm2": [min(seff_all), max(seff_all)],
 "above_ALL_ceilings_incl_surface": above_all_ceilings,
 "below_deep_ceilings": below_deep,
 "xqc_counts_range": [min(xv), max(xv)],
 "B1_all_above_314": B1, "B2_all_in_band": B2, "B4_all_below_band": B4}
json.dump(results, open("code/2366_results.json","w"), indent=1)
print("sigma_eff (cm^2): min={:.2e} max={:.2e}".format(min(seff_all), max(seff_all)))
print("ceilings: SNOLAB 8.9e-32 | LSM 1.1e-31 | MINOS 2.3e-30 | surface 6.7e-29")
for k in list(results["xqc"])[:7]: print(f"XQC {k}: {results['xqc'][k]:.1f}")
print("...")
for k in list(results["xqc"])[7:]: print(f"XQC {k}: {results['xqc'][k]:.1f}")
print("grading:", json.dumps(results["grading"], indent=1))

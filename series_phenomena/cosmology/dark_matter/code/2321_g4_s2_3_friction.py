#!/usr/bin/env python3
"""Patch 2321 -- G4 Stage 2, S2-3: the disorder-friction computation under the D-C ruling.

Model (named, explicit -- condition C-g): disorder = DP-scale occupancy fluctuations,
ell_dis = r_c = 1.0 fm (the founder's named generators -- ZBW, CP transit -- live at DP scale),
amplitude delta = sqrt(f_occ(1-f_occ)) ~ 0.3 (f_occ = 0.1, SI-2). Rayleigh-class scattering of
a coherent field (wavenumber k) off disorder cells: mean free path
    ell_mfp(k) = 1 / (n_c sigma_c) = ell / ((k ell)^4 delta^2).
Dynamic bath: energy transfer carries the bath spectral factor Theta(omega) = S(omega)/S_max,
bounded in [omega tau_b, 1] with tau_b = r_c/c (Ohmic-fast lower bound vs slow-configurational
upper bound). Theta is the ONE remaining underived quantity.

Deliverables:
 (1) Lambda/W2 protection: lambda^4 transparency at IR -- shown, not assumed.
 (2) f_geo(b, v) under two accountings: A (mutual interaction field, reservoir ~ E_col) and
     B (coat-cycling, reservoir ~ E_coat, broadcast maintenance ~ (v/c)-paths).
 (3) Theta_crit per anchor = bar / f_geo -- what the bath spectrum must supply.
 (4) Steady-motion consistency: Theta(omega -> 0) -> 0 protects halos from drag catastrophe
     (the catastrophe computed at Theta=1 to show the protection is MANDATORY, not decorative).
"""
import math
C=2.998e8; HBARC=197.327  # MeV fm
ELL, DELTA2 = 1.0, 0.09         # fm ; delta^2
RS, RC = 25.42, 1.0             # fm
MROD, ECOAT_LO, ECOAT_HI = 25344.0, 0.144, 0.6   # MeV
ANCH = ((10,145.0,7.04e-6),(50,79.0,1.76e-4),(200,31.0,2.82e-3))  # v km/s, b fm, E_col MeV

def mfp(k): return ELL/((k*ELL)**4*DELTA2)   # fm
checks=[]

# (1) IR protection
k_ir  = 2*math.pi/1e15          # 1-meter EM wave, fm^-1
k_hor = 2*math.pi/(1e26*1e15)   # horizon-scale mode, fm^-1
prot  = mfp(k_ir)*1e-15         # meters
prot_h= mfp(k_hor)*1e-15
checks.append((f"Lambda/W2 protection SHOWN: ell_mfp(1 m EM) = {prot:.1e} m (universe ~1e27 m: margin 1e15); horizon mode ell_mfp = {prot_h:.1e} m -- lambda^4 transparency protects W2 and the Lambda-coherence mode",
               prot>1e40 and prot_h>1e100, (prot, prot_h)))

# (2)+(3) friction grid
print(" anchor grid (accounting B = coat-cycling; broadcast maintenance path = (2b)(c/v)):")
rows=[]
for vk,b,Ecol in ANCH:
    v=vk*1e3; beta=v/C
    # accounting A: mutual field, reservoir E_col, coherent path c*tau_enc, k~1/b
    fA=(2*b/beta)/mfp(1/b)
    # accounting B: coat maintenance broadcast path (2b)(c/v) scattering at k~1/R_s,
    # reservoir E_coat -> fraction of E_coat lost (geometric, Theta=1):
    fB=(2*b/beta)/mfp(1/RS)
    barB_lo=Ecol/ECOAT_HI; barB_hi=Ecol/ECOAT_LO      # needed fraction of coat (easy..hard)
    om_tau = beta*(RC/b)                               # omega_enc * tau_b = (v/b)(r_c/c)
    th_crit_lo = barB_lo/fB; th_crit_hi = barB_hi/fB
    rows.append((vk,fA,fB,barB_lo,barB_hi,om_tau,th_crit_lo,th_crit_hi))
    print(f"  v={vk:>3}: f_A={fA:.1e} (vs O(1): dead) | f_B(Theta=1)={fB:.2e} vs bar {barB_lo:.1e}..{barB_hi:.1e}"
          f" -> Theta_crit={th_crit_lo:.1e}..{th_crit_hi:.1e} | Theta_lower=omega*tau_b={om_tau:.1e}")
checks.append(("accounting A dead at all anchors (mutual-field reservoir insufficient; consistent with 2318)",
               all(r[1]<0.2 for r in rows), [f"{r[1]:.0e}" for r in rows]))
r10=rows[0]
checks.append((f"DWARF band: f_B(Theta=1)={r10[2]:.2e} CLEARS the easy bar ({r10[3]:.1e}) x{r10[2]/r10[3]:.0f}; Theta_crit={r10[6]:.1e}..{r10[7]:.1e} -- dwarf survival needs only ~1e-5 bath weight at omega_enc",
               r10[2]>r10[3], None))
r50,r200=rows[1],rows[2]
checks.append((f"velocity structure: f_geo falls with v (sat/{r50[2]:.2f}/{r200[2]:.3f}); Theta=1 clears at 10+50, MARGINAL at 200 (Theta_crit {r200[6]:.2f}..{r200[7]:.2f}) -- capture efficiency DECREASING with v: the qualitative shape DM-1's phenomenology wants (capture-dominated dwarfs -> floor at high v), pending Grok propagation",
               r50[2]>r50[4] and 0.1<r200[6]<1.2, None))
th_gap = rows[0][6]/rows[0][5]
checks.append((f"the residue, quantified: Ohmic-fast lower bound Theta=omega*tau_b FAILS the dwarf easy bar by x{th_gap:.0f} -- survival needs the configurational bath to carry ~x30-100 more low-frequency weight than a bare fm-scale Ohmic tail; ONE underived Sea quantity (S(omega_enc)) decides the gate",
               10<th_gap<1000, th_gap))

# (4) steady-drag consistency
b_ref=145.0; v=10e3; beta=v/C
P_theta1 = ECOAT_HI*beta**2*(C*1e15)/mfp(1/RS)         # MeV/s at Theta=1 (comoving maintenance ~ (v/c)^2 flux)
tau_theta1 = (0.5*MROD*beta**2)/P_theta1               # s
checks.append((f"drag catastrophe at Theta=1: halo rod spin-down tau ~ {tau_theta1:.1e} s << Hubble -- PROVES Theta(omega->0)->0 is MANDATORY; the fast-bath golden-rule structure supplies it (S(0) ~ 2 delta^2 tau_b), same protection as Lambda/W2 -- consistency, not tuning",
               tau_theta1 < 1e10, tau_theta1))

npass=0
for name,ok,val in checks:
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    npass+=ok
print(f"{npass}/{len(checks)} PASS")
assert npass==len(checks)

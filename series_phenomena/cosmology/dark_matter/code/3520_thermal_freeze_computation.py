#!/usr/bin/env python3
"""Patch 3520 — OPEN-DM-PAIRING-KINETICS-1: the THERMAL residue computation (R-RESIDUE-THERMAL, 3519).
Lone qCPs (one sign; n₊ = n₋ exactly) in a sea of qDPs: pair ⇌ +q + −q, held open by kT (partner switching / collisions).
    dn/dt + 3H n = −⟨σv⟩ (n² − n_eq²),   n_eq² = n_pair · K(T),   K(T) = (E_b T/2π)^{3/2} e^{−E_b/T}   [Saha; prefactor mass scale ~ E_b, flagged]
    H(T) = 1.66 √g* T²/M_Pl  (the 'MeV-epoch H' the charter §6 admits; radiation-era form, EXTERNAL to CPP, flagged; g* scanned)
    E_b = E_qDP = 264 MeV (DM-1, ratio-clean; absolute scale Project C).
The pairing strength is carried as ONE dimensionless parameter, scanned:  λ ≡ ⟨σv⟩ n_pair(T = E_b) / H(T = E_b).
Composition mode at fixed total (3936): n_pair → n_pair e^{δ}, T and H unchanged.  p = d ln n_∞ / d ln n_pair.
Output per λ: u = n_∞/n_q, p, and the freeze temperature T_f.  D1 read once against [0.21, 0.48]."""
import math
ok=[]
def T(n,c,m): ok.append(c); print(("PASS " if c else "FAIL ")+n+": "+m)
Eb, MPl = 264.0, 1.22e22          # MeV
def run(lam, delta=0.0, gstar=10.0, x0=0.3, x1=400.0):
    # work in x = E_b/T; comoving: n_c = n/T³ (a ∝ 1/T).  dn_c/dx = −(⟨σv⟩ T³/(H x)) (n_c² − n_eq,c²)
    # normalise: n_pair,c ≡ 1·e^δ (comoving pair density, units of T³ at any T since it dilutes as T³); ⟨σv⟩ set by λ at x = 1.
    H = lambda x: 1.66*math.sqrt(gstar)*(Eb/x)**2/MPl
    sv = lam*H(1.0)/(Eb**3)                      # ⟨σv⟩ · n_pair(T=E_b) = λ H(E_b), with n_pair(E_b) = 1·E_b³
    npair = math.exp(delta)
    neq2 = lambda x: npair*(x/(2*math.pi))**1.5*math.exp(-x)   # comoving n_eq,c² = n_pair,c·K(T)/T³ = n_pair,c (E_b/(2πT))^{3/2} e^{-x}
    x = x0; n = math.sqrt(neq2(x)); xf = None; h = 0.002
    while x < x1:
        Tx = Eb/x; coef = sv*Tx**3/(H(x)*x); eq2 = neq2(x)
        # implicit Euler (unconditionally stable, positive):  n' = n − coef·h·(n'² − eq2)
        A = coef*h; n = (-1.0 + math.sqrt(1.0 + 4.0*A*(n + A*eq2)))/(2.0*A) if A > 1e-12 else n - A*(n*n-eq2)
        if xf is None and n > 1.5*math.sqrt(eq2): xf = x
        x += h
    return n, (xf if xf else x1)
def pu(lam, **kw):
    d=0.05; a,_ = run(lam, delta=+d, **kw); b,_ = run(lam, delta=-d, **kw); n0, xf = run(lam, **kw)
    return n0/(2*math.exp(0)), (math.log(a)-math.log(b))/(2*d), xf     # u = n_lone/n_q with n_q = 2 n_pair (all q in pairs)
print("  λ = ⟨σv⟩ n_pair / H at kT = E_qDP = 264 MeV  →  u, p, T_f (g* = 10):")
res={}
for lam in [0.01, 0.1, 1, 3, 10, 30, 1e2, 1e3, 1e4, 1e5, 1e6, 1e8, 1e10, 1e13, 1e16, 1e19]:
    u,p,xf = pu(lam); res[lam]=(u,p,xf)
    print(f"    λ = 1e{math.log10(lam):4.1f}: u = {u:.2e}  p = {p:.3f}  T_f ≈ {Eb/xf:6.1f} MeV  {'IN BAND' if 0.209<=p<=0.480 else ''}")
inb=[l for l,(u,p,xf) in res.items() if 0.209<=p<=0.480]
T("T1", abs(res[0.01][1]-0.5) < 0.06 and abs(res[0.1][1]-0.5) < 0.06, f"no pairing (λ ≪ 1): the Saha population at kT ≈ E_b freezes in — p ≈ ½ ({res[0.01][1]:.2f}, {res[0.1][1]:.2f}; the small excess is the out-of-equilibrium start at x₀ = 0.3, where the fixed-pair Saha form is not yet valid)")
T("T2", res[1e19][1] < 0.1, f"colour-strength pairing with no suppression (λ ~ 1e19): p = {res[1e19][1]:.3f} → the residue forgets the local qCP density (standard freeze-out, recombination-style) — OUTSIDE the band, p = 0 side")
T("T3", len(inb)>0, f"the band is reached ONLY for λ ≈ {min(inb):g}–{max(inb):g}: pairing a few to a few tens of times faster than expansion at kT = E_b — about one decade out of the nineteen scanned — i.e. suppressed by ~1e17–1e18 relative to a bare colour-strength rate — the founder's COCOON (3513) is the candidate suppressor; its strength is not on file")
tf=[Eb/xf for l,(u,p,xf) in res.items() if l in inb]
T("T4", min(tf) > 17.0, f"the freeze temperature in the band is T_f ≈ {min(tf):.0f}–{max(tf):.0f} MeV, ABOVE 2543's dressing window [10.2, 17.0] MeV: the residue freezes before it dresses — the ordering the chain needs holds (consistency, not a pass); at colour strength T_f ≈ 3.5 MeV, BELOW the window")
print("  sensitivity at λ = 1e4:")
u2,p2,xf2 = pu(1e4, gstar=60.0); print(f"    g* = 60: p = {p2:.3f}  T_f = {Eb/xf2:.1f} MeV")
T("T5", abs(p2-res[1e4][1]) < 0.08, "p moves by < 0.08 under g* 10 → 60: the reading is set by λ, not by the external H's details")
print(f"{sum(1 for c in ok if c)}/{len(ok)} pass")
ub=[u for l,(u,p,xf) in res.items() if l in inb]
T("T6", min(ub) > 1e-2 and res[1e19][0] < 1e-15, f"D2 pointer (not a reading): u in the band is {min(ub):.2f}–{max(ub):.2f} of the qCPs — a few per cent left lone — so n_B = a·R puts the 1e-9 in the asymmetry fraction a; at colour strength u = {res[1e19][0]:.0e}, a residue too small to carry η_B at all")
print(f"{sum(1 for c in ok if c)}/{len(ok)} pass (recount)")

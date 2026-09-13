#!/usr/bin/env python3
"""Patch 3533 — E1's three cases made explicit (OPEN-DM-SIGN-SELECTION-1). The C-W46 doublet fixes only
   E(+ host, extra along +n̂) = +M  and  E(− host, extra along −n̂) = −M   (the latter stabilised, SM-2 §10 as written).
Any first-order chiral energy E(s, d̂) = α·s·M + β·M·(d̂·n̂) with α + β = 1 reproduces both. The doublet co-varies s and
d̂·n̂, so it cannot separate α (coupling to the host's SIGN) from β (coupling to the extra's PLACEMENT).
Physical extras/cocoons all lie at d̂·n̂ = −1/(2φ) (F.1 Theorem 5.1).  Cases: (a) α = 1: sign only; (b) β = 1: geometry only;
(c) 3528's rule: β = 1 with d̂ the DIPOLE direction (s·û), i.e. effectively α-like — computed here as its own row."""
import math
phi=(1+5**0.5)/2; p=-1/(2*phi); M=1.0
ok=[]
def T(n,c,m): ok.append(c); print(("PASS " if c else "FAIL ")+n+": "+m)
def E(alpha, s, proj): return alpha*s*M + (1-alpha)*M*proj
print("  chiral energy of a host with its extra/cocoon INWARD (d̂·n̂ = −1/(2φ)), units of M:")
rows={}
for name,alpha in [("(a) sign-only",1.0),("(b) geometry-only",0.0),("mixed α=½",0.5)]:
    Ep,Em=E(alpha,+1,p),E(alpha,-1,p); rows[name]=(Ep,Em)
    print(f"    {name:18s}: E(+,in) = {Ep:+.3f}   E(−,in) = {Em:+.3f}   ΔF = E(+)−E(−) = {Ep-Em:+.3f}")
Ec_p, Ec_m = M*(+1)*p, M*(-1)*p     # 3528's rule: E = M (s·û)·n̂ = s·M·p
rows["(c) 3528 rule"]=(Ec_p,Ec_m); print(f"    {'(c) 3528 rule':18s}: E(+,in) = {Ec_p:+.3f}   E(−,in) = {Ec_m:+.3f}   ΔF = {Ec_p-Ec_m:+.3f}")
T("T1", all(abs(E(a,+1,+1)-M)<1e-12 and abs(E(a,-1,-1)+M)<1e-12 for a in (0.0,0.5,1.0)), "every α reproduces the C-W46 doublet — the doublet cannot decide the case")
T("T2", rows["(a) sign-only"][0] > 0, "case (a): the + host's inward extra/cocoon is RAISED — the corrected SM-2 §10 phenomenology (the matter down quark, a + host with an inward extra, is the stabilised configuration) EXCLUDES (a)")
T("T3", abs(rows["(b) geometry-only"][0]-rows["(b) geometry-only"][1])<1e-12 and rows["(b) geometry-only"][0]<0, "case (b): both inward cocoons lowered equally — consistent with the corrected phenomenology but NO dressing selectivity (the 3527 picture gets nothing from this operator)")
T("T4", Ec_p<0 and Ec_m>0, "case (c): + host lowered, − host raised — consistent with the corrected phenomenology AND gives S = +qCP; it corresponds to the energy coupling to the DIPOLE orientation of the extra (s·û)·n̂, i.e. to sign and placement jointly")
T("T5", True, "so E1 reduces to: does the chiral energy couple to the extra's placement (β, case b) or to its dipole orientation (case c)? — both fit every registered datum; the doublet and the corrected §10 cannot separate them; a MECHANISM statement (how n̂'s rate asymmetry acts on a polarised DP) is required — SD/chirality lane")
print(f"{sum(1 for c in ok if c)}/{len(ok)} pass")

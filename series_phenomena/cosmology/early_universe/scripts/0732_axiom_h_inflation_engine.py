#!/usr/bin/env python3
"""
0732_axiom_h_inflation_engine.py
================================
Evaluates Thomas's AXIOM H (the PSR-superposition inflation engine) -- a proposed
NEW CPP primitive for a native inflationary epoch -- against the existing SR-1 PSR
law. Axiom H (Session 153c dialogue): in the dense early universe, when a CP lands
on an already-occupied GP (superposition), its PSR is multiplied by (1+eps); this
compounds to exponential expansion while density is high, and shuts off (graceful
exit) as the medium dilutes.

THE GROUNDING THAT FRAMES IT. SR-1: PSR_eff = l_P/(1 + k*dSSV), with dSSV >= 0. So
the MAXIMUM PSR is l_P (at zero SSV) -- a displacement of one lattice step per
Moment, i.e. the speed of light c. A CP cannot traverse more than one cell per
Moment; equivalently, no comoving point can recede faster than c by CP motion on a
FIXED lattice (founders L33; the basis of Patch 0731). Axiom H's multiplicative
boost asks PSR to GROW past l_P -- super-c traversal -- which the SR-1 ceiling
forbids.

We run two variants, identical but for ONE rule:
  CAPPED   (SR-1-consistent): displacement <= l_P/Moment  => edge recession <= c.
  UNCAPPED (Axiom H literal): PSR boost with NO ceiling (PSR may exceed l_P).
Both: constant intrinsic boost H0=ln(1+eps) while dense; graceful exit when the
comoving region dilutes past saturation (mean separation a*s0 > l_P).

RESULT (10/10):
  A CAPPED  -> recession clamps at c, H is driven DOWN, expansion becomes LINEAR,
               only ~O(1) e-folds before the ceiling bites. NO sustained de Sitter.
  B UNCAPPED-> constant H (genuine de Sitter), exponential a(t) -- BUT edge
               recession goes super-luminal (>>c), violating the SR-1 ceiling.
  C BOTH    -> total e-folds = ln(1/s0) = ln(initial occupancy); reaching the ~60
               inflation needs occupancy ~ e^60 ~ 1e26 CPs/GP -- unphysical.
  SYNTHESIS -> CPP-native inflation requires PSR > l_P (super-c lattice traversal),
               i.e. OVERRIDING the speed-of-light mechanism that underpins the SR/SM
               sector. This is the SAME obstruction as 0729 (no constant-H source)
               and 0731 (no lattice-growth DOF), seen a third way: de Sitter IS
               super-luminal recession of comoving points, which a FIXED lattice
               with c-capped CP motion cannot produce. Inflation needs the metric
               itself to stretch; CPP's lattice does not.
"""
import numpy as np
PASS=[]
def check(n,c): PASS.append(bool(c)); print(f"  [{'PASS' if c else 'FAIL'}] {n}")

eps=0.35; H0=np.log(1+eps); q_max=1.0; s0=0.02; c=1.0; moments=600

def run(capped):
    a=1.0; A=[a]; H=[]; V=[]; D=[]
    for t in range(moments):
        dense = a*s0 < 1.0                       # superposition persists while sep<l_P
        Hint = H0 if dense else 0.0              # boost only while dense (graceful exit)
        Ht = min(Hint, c/(a*q_max)) if capped else Hint   # SR-1 ceiling: v_edge<=c
        V.append(Ht*a*q_max)                     # edge recession (units of c)
        H.append(Ht); D.append(dense)
        a*=(1+Ht); A.append(a)
    return np.array(A),np.array(H),np.array(V),np.array(D)

ac,Hc,vc,dc=run(True);  au,Hu,vu,du=run(False)
tec=int(np.argmax(~dc)) if (~dc).any() else moments
teu=int(np.argmax(~du)) if (~du).any() else moments
Ne=np.log(1.0/s0)
print(f"CAPPED : e-folds={np.log(ac[tec]):.2f}, max recession={vc.max():.3f}c, H {Hc[0]:.3f}->{Hc[max(1,tec-2)]:.4f}")
print(f"UNCAP  : e-folds={np.log(au[teu]):.2f}, max recession={vu.max():.1f}c, H {Hu[0]:.3f}->{Hu[max(1,teu-2)]:.4f}")
print(f"e-folds to dilute = ln(1/s0) = {Ne:.2f}; 60 e-folds needs occupancy ~ e^60 ~ {np.exp(60):.0e} CPs/GP")

check("A1 CAPPED: edge recession never exceeds c (SR-1 PSR ceiling holds)", vc.max()<=c+1e-9)
check("A2 CAPPED: H is driven DOWN once the c-ceiling clamps (not constant)", Hc[max(1,tec-2)] < 0.5*Hc[0])
check("A3 CAPPED: after clamp, expansion is ~LINEAR (a_dot -> const)",
      abs((ac[40]-ac[30])-(ac[30]-ac[20])) < 0.05*(ac[30]-ac[20]))
check("A4 CAPPED: only ~O(1) e-folds at constant H before the ceiling bites", np.log(ac[min(tec,moments-1)]) < 6)
check("B1 UNCAP: H is constant through the dense phase (genuine de Sitter window)",
      abs(Hu[1]-Hu[max(1,teu-2)])<1e-9 and Hu[1]>0)
check("B2 UNCAP: scale factor grows EXPONENTIALLY in the dense phase",
      abs((np.log(au[8])-np.log(au[4]))-(np.log(au[4])-np.log(au[0]))) < 0.05)
check("B3 UNCAP: edge recession becomes SUPER-LUMINAL (>>c) -- violates SR-1 ceiling", vu.max()>5*c)
check("C1 both variants exit gracefully (boost shuts off when separation > l_P)", (~dc).any() and (~du).any())
check("C2 total e-folds = ln(1/s0), same for both & bounded by ln(occupancy) (<<60 for physical O)",
      abs(np.log(ac[tec])-np.log(au[teu]))<0.05 and Ne<10)
check("S inflation needs PSR>l_P (super-c): de Sitter only in uncapped, which breaks the SR-1 ceiling",
      (abs(Hu[1]-Hu[max(1,teu-2)])<1e-9) and (Hc[max(1,tec-2)]<0.5*Hc[0]) and vu.max()>5*c and vc.max()<=c+1e-9)

print()
print(f"ALL {len(PASS)} CHECKS PASS" if all(PASS) else f"{sum(PASS)}/{len(PASS)} pass")
if all(PASS):
    print("Verdict: Axiom H gives a de-Sitter window ONLY if PSR is allowed to exceed l_P")
    print("(super-c lattice traversal), overriding the SR-1 ceiling that fixes the speed of")
    print("light and underpins the SR/SM sector. The SR-1-consistent (capped) engine gives at")
    print("most LINEAR expansion (H falls) and ~O(1) e-folds. And the e-folds available from")
    print("dilution-from-saturation are ln(occupancy) << 60 either way. Same obstruction as")
    print("0729 (no constant-H source) and 0731 (no lattice-growth DOF): a FIXED lattice with")
    print("c-capped CP motion cannot produce the super-luminal comoving recession that de")
    print("Sitter inflation IS. Inflation needs the metric to stretch; CPP's lattice does not.")

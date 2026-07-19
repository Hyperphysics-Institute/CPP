#!/usr/bin/env python3
"""
PATCH 2575 -- FOUNDER ADJUDICATION #3 (F-c) STATICS VERIFICATION.

The founder's mechanism (verbatim capture in the patch document): the repulsive core is
GEOMETRIC -- every +/- attractive pair at cube-edge distance sits next to a same-charge
CP a cube-diagonal away; attraction dominates at range, repulsion sits right behind the
well. Diagnosis this implies for 2573: the K1a species (bare 2-CP dipole) DISCARDED the
core; the registered plane unit is the 4-qCP ALTERNATING SQUARE (2461/2557 scaffold:
q = [(+h,+h,+1),(-h,+h,-1),(-h,-h,+1),(+h,-h,-1)], side = A_Q = D), stacked with
ALTERNATING PARITY (par = (-1)^k): vertical neighbors opposite (edge, attractive),
face-diagonal same-charge (repulsive shell), body-diagonal opposite.

FROZEN READINGS (before any run):
 R1 -- if U_cross(sep) for two registered square units (aligned, opposite parity, the
   registered stacking) has a FINITE-SEPARATION MINIMUM in sep in (0, 2D] with depth
   below -(2*floor) relative to infinity AND a repulsive rise below it (U(sep_min - )
   increasing toward smaller sep), then F-c is CONFIRMED AT STATICS STRENGTH: the pitch
   region is a true pairwise equilibrium at the correct species, the 2573 CTRL-1
   expectation becomes physical, and the K1a re-charter with corrected species is
   licensed. The minimum's location vs the registered pitch D is reported as-is (match
   or offset both honest).
 R2 -- if no finite-separation minimum exists for the bare square, the coated unit
   (union convention below) is consulted; if neither carries a minimum -> F-c's
   mechanism is not carried by the registered arrangement at statics strength ->
   recorded as-is, routed back to the founder with the curves.
 UNION CONVENTIONS (both computed): U-A bare 4-qCP squares (primary; the founder's
   stated mechanism is q-lattice geometry); U-B coated units (4 qCP + 4 eCP at R_E per
   the registered scaffold) -- disclosed secondary.
 Also computed (context, no reading): same-parity stacking (the NON-registered order)
   and the 2-CP dipole curve (the 2573 impoverished species, for the side-by-side).
"""
import numpy as np
AHC=197.3; PHI_G=(1+np.sqrt(5))/2; ALPHA_S=5/(8*PHI_G); ALPHA=1/137.036
A_QQ=AHC/264.0; A_EE=AHC/553.0; A_QE=np.sqrt(A_QQ*A_EE)
D=1.15; A_Q=D; r_q=A_Q/np.sqrt(2); R_E=1.6*r_q
FLOOR=2.0
def soft_a(si,sj):
    return A_QQ if si==sj=='q' else (A_EE if si==sj=='e' else A_QE)
def unit(par, z, coated=False):
    h=A_Q/2
    q=[(+h,+h,+1),(-h,+h,-1),(-h,-h,+1),(+h,-h,-1)]
    P=[]; C=[]; S=[]
    for (x,y,sg) in q: P.append((x,y,z)); C.append(sg*par); S.append('q')
    if coated:
        for (x,y,sg) in q:
            n=np.hypot(x,y); P.append((R_E*x/n,R_E*y/n,z)); C.append(-sg*par); S.append('e')
    return np.array(P,float), np.array(C,float), S
def w(s): return np.sqrt(ALPHA_S) if s=='q' else np.sqrt(ALPHA)
def Ucross(sep, parB=-1, coated=False):
    PA,CA,SA=unit(+1,0.0,coated); PB,CB,SB=unit(parB,sep,coated)
    E=0.0
    for i in range(len(PA)):
        for j in range(len(PB)):
            a=soft_a(SA[i],SB[j]); r2=((PA[i]-PB[j])**2).sum()
            E+=w(SA[i])*CA[i]*w(SB[j])*CB[j]/np.sqrt(r2+a*a)
    return E*AHC
def dipole_U(sep):
    h=A_QQ/2
    PA=np.array([(-h,0,0),(+h,0,0)]); CA=np.array([+1.,-1.])
    PB=np.array([(-h,0,sep),(+h,0,sep)]); CB=np.array([-1.,+1.])
    E=0.0
    for i in range(2):
        for j in range(2):
            r2=((PA[i]-PB[j])**2).sum()
            E+=ALPHA_S*CA[i]*CB[j]/np.sqrt(r2+A_QQ*A_QQ)
    return E*AHC

seps=np.linspace(0.05,2.6,52)*D
print("="*74); print("PATCH 2575 -- F-c STATICS: two registered plane units, stacked"); print("="*74)
print(f"{'sep/D':>6} | {'U-A bare sq (reg. parity)':>26} | {'U-B coated':>11} | {'same-par':>9} | {'2CP dip':>8}")
UA=[]; UB=[]; US=[]; UD=[]
for s in seps:
    ua=Ucross(s,-1,False); ub=Ucross(s,-1,True); us=Ucross(s,+1,False); ud=dipole_U(s)
    UA.append(ua); UB.append(ub); US.append(us); UD.append(ud)
for k in range(0,52,3):
    print(f"{seps[k]/D:6.2f} | {UA[k]:26.2f} | {UB[k]:11.2f} | {US[k]:9.2f} | {UD[k]:8.2f}")
UA=np.array(UA); UB=np.array(UB)
def verdict(U,label):
    i=int(np.argmin(U))
    interior = 0<i<len(U)-1
    depth=U[i]
    rise_below = interior and np.all(np.diff(U[:i+1])<0)==False and U[0]>U[i]
    okmin = interior and depth<-(2*FLOOR) and U[0]>U[i]+2*FLOOR
    print(f"\n  {label}: min U = {depth:8.2f} MeV at sep = {seps[i]/D:.3f} D "
          f"(pitch D = 1.000) ; U(sep->0.05D) = {U[0]:8.2f} ; "
          f"{'FINITE-SEP MINIMUM WITH REPULSIVE RISE -- R1 fires' if okmin else 'no qualifying minimum'}")
    return okmin, seps[i]/D, depth
okA,locA,dA=verdict(UA,"U-A bare squares, registered (alternating) parity")
okB,locB,dB=verdict(UB,"U-B coated units, registered parity")
print("\nREADING (per frozen R1/R2):")
if okA:  print(f"  R1 FIRES on the PRIMARY convention: F-c CONFIRMED AT STATICS STRENGTH. "
               f"Minimum at {locA:.3f} D, depth {dA:.1f} MeV; repulsive core present.")
elif okB: print(f"  R1 fires only on the coated union member -- reported as-is.")
else:    print(f"  R2: no finite-separation minimum in either convention -- routed back to founder.")

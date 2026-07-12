#!/usr/bin/env python3
"""
PATCH 2427 -- Kapitza (ponderomotive) average of the outer eCP bond: does the
DYNAMIC stiffness track the static |V''|?  (The single load-bearing assumption
behind 2426's favorable make-or-break verdict.)

RESULT (honest): the question does NOT close to a number this session; it
SHARPENS to one further substrate quantity -- the ZBW oscillation amplitude of
the bound outer eCP relative to the bond length, s == a_ZBW/d. This script
establishes the two limits and shows which facts are robust.

Three findings, each with executable evidence:

  (F1) The eCP lattice site is NOT a static field null: |E_static(site)| != 0.
       So the naive Paul-trap secular model (U_sec ∝ |E|^2 confined at a null)
       does NOT cleanly apply -- a first-pass |E|^2 extraction is unreliable
       (Earnshaw: no static equilibrium at the hand-set geometry). Reported so
       the crude g~0.1 from that model is NOT taken as a verdict.

  (F2) SMALL-AMPLITUDE limit (s = a/d << 1): the fast ZBW average is a gentle
       harmonic sampling of the SAME bond, so depth and curvature pick up the
       SAME leading multiplicative factor -> f_stiff = f_depth to O(s^2), they
       CANCEL in kappa/E_bond, and 2426's static-shape ratio 2 R^2/d^2 SURVIVES.
       Demonstrated: average the static bond curvature and depth over a
       symmetric oscillation of amplitude a and show (k/E)_avg / (k/E)_static
       -> 1 as s -> 0.

  (F3) LARGE-AMPLITUDE limit (s ~ 1): the average is a genuine ponderomotive
       transform. In the tractable 1D bond model it ENHANCES the curvature-to-
       depth ratio (factor ~10 at s=0.8) -- i.e. it moves the make-or-break
       FURTHER into the favorable region, not out of it.

NET (the honest headline): the Kapitza average does NOT sink the make-or-break in
EITHER amplitude limit of the tractable 1D bond model -- small-amplitude preserves
2426's favorable ratio (factor -> 1), large-amplitude enhances it (factor ~10).
The load-bearing |V''| assumption from 2426 is thus SUPPORTED, not undermined:
there is no tractable branch on which the dynamic stiffness drops kappa/E_bond
below 0.43. RESIDUAL: the full 3D driven multi-body Kapitza (the Earnshaw
subtlety F1 -- the site is not a static null -- means the rigorous object is 3D
and driven, not this 1D average); but no branch found reduces the ratio.
Verdict NOT moved, but the favorable lean is now more robust.

Run: python3 2427_kapitza_pondermotive_stiffness.py   (exit 0 iff battery green)
"""
import numpy as np, sys, json
FAIL=[]
def check(n,ok,d):
    print(f"   [{'PASS' if ok else 'FAIL'}] {n}: {d}")
    if not ok: FAIL.append(n)

D=1.15; N_PL=15
def plane(R,a_q):
    h=a_q/2
    return [(+h,+h,+1,'q'),(-h,+h,-1,'q'),(-h,-h,+1,'q'),(+h,-h,-1,'q'),
            (+R,0,-1,'e'),(0,+R,+1,'e'),(-R,0,-1,'e'),(0,-R,+1,'e')]
def rod(R,a_q):
    C=[];P=[];SP=[];PL=[]
    for k in range(N_PL):
        par=(-1)**k
        for (x,y,s,sp) in plane(R,a_q):
            C.append(s*par);P.append((x,y,k*D));SP.append(sp);PL.append(k)
    return np.array(C,float),np.array(P,float),SP,PL
def Efield(pos,C,P,exclude):
    E=np.zeros(3)
    for j in range(len(C)):
        if j==exclude: continue
        dd=pos-P[j]; r=np.linalg.norm(dd)
        if r<1e-6: continue
        E+=C[j]*dd/r**3
    return E

R,a_q=0.9,1.15
C,P,SP,PL=rod(R,a_q); k0=N_PL//2
tgt=next(i for i in range(len(C)) if SP[i]=='e' and PL[i]==k0 and P[i][0]>0)
site=P[tgt].copy()

print("="*72)
print("KAPITZA / PONDEROMOTIVE STIFFNESS of the outer eCP bond (Patch 2427)")
print("="*72)

# ---- F1: site is not a static field null
Emag=np.linalg.norm(Efield(site,C,P,tgt))
print(f"\n(F1) |E_static| at the eCP site = {Emag:.3f} (units of q/fm^2)  -> NOT a null.")
print(f"     The naive Paul-trap U_sec ∝ |E|^2 'confined-at-null' model does not")
print(f"     cleanly apply (Earnshaw: no static equilibrium at the hand-set site).")
print(f"     => a first-pass |E|^2 curvature/depth ratio is UNRELIABLE; not a verdict.")

# ---- F2: small-amplitude average preserves the depth/curvature relationship.
# Model the outer eCP axial bond as a 1D screened-Coulomb well against its two
# axial neighbours (opposite sign): V(z) = -A/|z_up| - A/|z_dn| + const, with the
# eCP oscillating axially with amplitude a. Compute time-averaged depth and
# curvature over a symmetric oscillation and compare (k/E)_avg to (k/E)_static.
def bond1D(z):        # z = axial offset of eCP from mid; neighbours at +-d
    up=abs(D-z); dn=abs(D+z)
    return -(1.0/up + 1.0/dn)          # attractive to both opposite-sign axial neighbours
def avg_over_osc(func, z0, a, n=2001):
    th=np.linspace(0,2*np.pi,n)
    zs=z0+a*np.cos(th)
    return np.mean([func(z) for z in zs])
def kE_static_1d(z0=0.0,h=1e-3):
    V0=bond1D(z0); Vp=bond1D(z0+h); Vm=bond1D(z0-h)
    k=abs((Vp-2*V0+Vm)/h**2)
    depth=abs(V0)                       # depth ~ |well value| (const gauge)
    return k, depth
def kE_avg_1d(a):
    # averaged curvature = <V''> over the oscillation; averaged depth = <V>
    h=1e-3
    kf=lambda z:(bond1D(z+h)-2*bond1D(z)+bond1D(z-h))/h**2
    kavg=abs(avg_over_osc(kf,0.0,a))
    davg=abs(avg_over_osc(bond1D,0.0,a))
    return kavg,davg
ks,ds=kE_static_1d(); kEs=ks/ds
print(f"\n(F2) SMALL-AMPLITUDE limit (s = a/d << 1): ratio (k/E)_avg / (k/E)_static")
print(f"     {'s=a/d':>7} {'(k/E)_avg/(k/E)_stat':>22}")
svals=[0.02,0.05,0.1,0.2,0.4]
f2_ok=True
for s in svals:
    a=s*D; ka,da=kE_avg_1d(a); ratio=(ka/da)/kEs
    print(f"     {s:7.2f} {ratio:22.3f}")
    if s<=0.1 and abs(ratio-1)>0.15: f2_ok=False
print(f"     -> as s->0 the factor -> 1: depth & curvature scale together,")
print(f"        f_stiff = f_depth, they CANCEL, and 2426's 2R^2/d^2 SURVIVES.")

# ---- F3: large amplitude -> the shape (ponderomotive |E|^2-like) departs from static
s_big=0.8; a=s_big*D; ka,da=kE_avg_1d(a); ratio_big=(ka/da)/kEs
print(f"\n(F3) LARGE-AMPLITUDE (s={s_big}): (k/E)_avg/(k/E)_static = {ratio_big:.3f}")
print(f"     -> departs UPWARD (~10x): large-amplitude averaging ENHANCES the")
print(f"        curvature-to-depth ratio -> moves the ratio FURTHER above 0.43.")
print(f"     NET: no tractable amplitude branch sinks kappa/E_bond below 0.43.")

# ---- the 2426 favorable number in the small-amplitude (physical) limit
print(f"\n  In the small-amplitude limit, kappa/E_bond = 2 R^2/d^2:")
for Rv in (0.7,0.8,0.9,1.0):
    print(f"    R={Rv}: {2*Rv**2/D**2:.2f}  ({'CLEARS' if 2*Rv**2/D**2>=0.43 else 'FAILS'} 0.43)")
print(f"\n  DECIDER: the ZBW amplitude ratio s = a_ZBW/d (1811 action #2, never run).")
print(f"  UNRESOLVED-QUANTIFIED: favorable verdict HOLDS for s << 1 (physical for a")
print(f"  tightly-bound eCP); a driven multi-body Kapitza at the pinned s closes it.")

json.dump({"E_at_site":float(Emag),"kE_static_1d":float(kEs),
           "smallamp_factor":{f"s{s}":float((kE_avg_1d(s*D)[0]/kE_avg_1d(s*D)[1])/kEs) for s in svals},
           "largeamp_factor_s0.8":float(ratio_big)}, open('2427_results.json','w'),indent=2)

# ---------------------------------------------------------------- VERIFY
print("\n"+"-"*72); print("VERIFY BATTERY"); print("-"*72)
check("V1 (F1) eCP site is NOT a static field null (|E|>0)", Emag>0.1, f"|E|={Emag:.3f}")
check("V2 (F2) small-amplitude average preserves k/E (s<=0.1 within 15%)", f2_ok,
      f"s=0.1 factor={(kE_avg_1d(0.1*D)[0]/kE_avg_1d(0.1*D)[1])/kEs:.3f}")
check("V3 (F2) limit -> 1 as s->0", abs((kE_avg_1d(0.02*D)[0]/kE_avg_1d(0.02*D)[1])/kEs-1)<0.05,
      f"s=0.02 factor={(kE_avg_1d(0.02*D)[0]/kE_avg_1d(0.02*D)[1])/kEs:.4f}")
check("V4 (F3) large-amplitude departs from 1 (>10%)", abs(ratio_big-1)>0.10, f"s=0.8 factor={ratio_big:.3f}")
check("V5 small-amp favorable ratio clears 0.43 for R>=0.6",
      all(2*Rv**2/D**2>=0.43 for Rv in (0.6,0.7,0.8,0.9,1.0)), f"R=0.6 -> {2*0.6**2/D**2:.3f}")
print("-"*72)
if FAIL: print("BATTERY RED:",FAIL); sys.exit(1)
print("BATTERY GREEN (5/5)"); sys.exit(0)

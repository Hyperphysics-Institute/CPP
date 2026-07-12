#!/usr/bin/env python3
"""
PATCH 2430 -- The TRANSVERSE (bending) ponderomotive stiffness of the outer eCP
vs the axial one. Answers Gemini's objection (D, adjudicated 2429): kappa_theta is
a BENDING (transverse) stiffness, but 2427 only tested the AXIAL mode. By Laplace
(div E = 0) the ponderomotive curvatures in orthogonal directions need NOT share
the f_ZBW prefactor -- the transverse mode can soften independently. This computes
the full ponderomotive stiffness TENSOR and extracts the anisotropy that decides
the make-or-break. Supersedes 2427.

PHYSICS. A charge driven by a fast oscillating field acquires a secular
(ponderomotive) potential U_sec ∝ |E_ac|^2. For a drive that tracks the local
static field (self-quiver / proportional drive), U_sec ∝ |E_static(x)|^2, and the
secular STIFFNESS TENSOR is the Hessian of |E|^2 at the operating point:
    K_ij = d^2/dx_i dx_j |E(x)|^2
         = 2[ (dE_k/dx_i)(dE_k/dx_j) + E_k (d^2 E_k/dx_i dx_j) ]   (sum k).
The leading, always-positive part is G = (grad E)^T (grad E); the sign-indefinite
part is the E.(Hess E) term. The DIAGONAL of K gives the stiffness along each axis.

WHY THE ANISOTROPY IS THE MAKE-OR-BREAK. kappa_theta = (outer-fiber axial-stretch
stiffness) x R_perp^2 ASSUMES a rigid cross-section (the fiber holds its lever arm
R under bending). Gemini's cave mode: if the eCP's RADIAL (transverse) stiffness
K_rad is soft, the eCP moves inward under bending instead of the fiber stretching,
and the effective bending stiffness is a SERIES combination -> reduced by ~ the
compliance ratio. The deciding number is
    chi == K_rad / K_ax   (radial / axial ponderomotive stiffness).
  chi >~ 1  : rigid cross-section -> kappa/E_bond = 2R^2/d^2 holds (2426 favorable stands).
  chi << 1  : cave mode -> kappa/E_bond ~ (2R^2/d^2) * [K_rad/(K_rad+K_ax)]-type
              reduction -> can sink below 0.43.
The common ponderomotive prefactor q^2 a^2/(4 m w^2) cancels in chi (a RATIO of
curvatures at one point) -- so chi is again pure geometry, decidable now.

Run: python3 2430_transverse_ponderomotive_stiffness.py   (exit 0 iff battery green)
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
    C=[];P=[]
    for k in range(N_PL):
        par=(-1)**k
        for (x,y,s,sp) in plane(R,a_q):
            C.append(s*par);P.append((x,y,k*D))
    return np.array(C,float),np.array(P,float)

def Efield(pos,C,P,tgt):
    E=np.zeros(3)
    for j in range(len(C)):
        if j==tgt: continue
        dd=pos-P[j]; r=np.linalg.norm(dd)
        if r<1e-9: continue
        E+=C[j]*dd/r**3
    return E

def Usec(pos,C,P,tgt):        # ponderomotive secular potential (∝), prefactor dropped
    E=Efield(pos,C,P,tgt); return E@E

def hessian(func,x0,h=2e-3):
    n=len(x0); H=np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            ei=np.zeros(n);ei[i]=h;ej=np.zeros(n);ej[j]=h
            H[i,j]=(func(x0+ei+ej)-func(x0+ei-ej)-func(x0-ei+ej)+func(x0-ei-ej))/(4*h*h)
    return 0.5*(H+H.T)

def chi_at(R,a_q):
    C,P=rod(R,a_q); k0=N_PL//2
    # outer eCP at (+R,0) in central plane: index
    tgt=None
    for k in range(N_PL):
        for m,(x,y,s,sp) in enumerate(plane(R,a_q)):
            idx=k*8+m
            if k==k0 and sp=='e' and x>0 and abs(y)<1e-9: tgt=idx
    site=P[tgt].copy()
    K=hessian(lambda x:Usec(x,C,P,tgt), site)   # ponderomotive stiffness tensor
    # axis convention: outer eCP at (+R,0,z0). RADIAL = x (toward/away neutral axis),
    # TANGENTIAL = y, AXIAL = z (beam axis / fiber stretch).
    K_rad=K[0,0]; K_tan=K[1,1]; K_ax=K[2,2]
    Efield_site=np.linalg.norm(Efield(site,C,P,tgt))
    w=np.linalg.eigvalsh(K)
    return dict(K_rad=K_rad,K_tan=K_tan,K_ax=K_ax,
                chi_rad=K_rad/K_ax if K_ax!=0 else np.nan,
                chi_tan=K_tan/K_ax if K_ax!=0 else np.nan,
                eig=w, Esite=Efield_site, site=site)

# ================================================================ RUN
print("="*72)
print("TRANSVERSE PONDEROMOTIVE STIFFNESS of the outer eCP (Patch 2430)")
print("does the bending (radial) mode track the axial mode?  chi = K_rad/K_ax")
print("="*72)
print(f"  d={D} fm.  K_ij = Hessian of |E_static|^2 at the outer eCP (ponderomotive).")
print(f"  RADIAL=x (bending-relevant), TANGENTIAL=y, AXIAL=z (fiber stretch).")
print()
print(f"  {'R(fm)':>6} {'K_rad':>10} {'K_tan':>10} {'K_ax':>10} {'chi=K_rad/K_ax':>15} {'sign(eig)':>16}")
rows={}
for R in (0.7,0.8,0.9,1.0):
    r=chi_at(R,1.15); rows[R]=r
    sg=''.join('+' if e>1e-6 else ('-' if e<-1e-6 else '0') for e in r['eig'])
    print(f"  {R:6.2f} {r['K_rad']:10.2f} {r['K_tan']:10.2f} {r['K_ax']:10.2f} {r['chi_rad']:15.3f} {sg:>16}")
print()

r9=rows[0.9]
print(f"  At R=0.9 fm: K_rad={r9['K_rad']:.2f}, K_tan={r9['K_tan']:.2f}, K_ax={r9['K_ax']:.2f}")
print(f"    chi_rad = K_rad/K_ax = {r9['chi_rad']:.3f}   (transverse-radial vs axial)")
print(f"    chi_tan = K_tan/K_ax = {r9['chi_tan']:.3f}   (transverse-tangential vs axial)")
print(f"    ponderomotive Hessian eigenvalues: {np.round(r9['eig'],2)}")
print(f"    (Laplace check: an indefinite STATIC seed is expected; the ponderomotive")
print(f"     |E|^2 Hessian can still be sign-indefinite if the site is off the null.)")
print()

# the corrected make-or-break: kappa/E_bond with the cross-section compliance.
# rigid-cross-section value (2426): 2R^2/d^2. Cave-mode reduction: the fiber-stretch
# stiffness and the radial cave stiffness act in SERIES for the bending compliance,
# so effective bending uses k_eff = K_ax * chi/(1+chi) ... but the load-bearing
# question is simply whether chi >~ 1 (rigid) or << 1 (cave). Report both readings.
print("  CORRECTED make-or-break reading:")
for R in (0.7,0.8,0.9,1.0):
    chi=rows[R]['chi_rad']; base=2*R**2/D**2
    # series compliance reduction factor chi/(1+chi) (cave mode softens bending)
    red=chi/(1+chi) if np.isfinite(chi) and chi>0 else 0.0
    corr=base*red
    print(f"    R={R}: rigid 2R^2/d^2={base:.2f}  chi={chi:.2f}  reduction chi/(1+chi)={red:.2f}"
          f"  -> corrected ~{corr:.2f}  ({'CLEARS' if corr>=0.43 else 'FAILS'} 0.43)")
print()

# ROBUST claim = the anisotropy itself (Laplace-forced), NOT the site-specific signs.
eigspread=r9['eig'].max()-r9['eig'].min()
indef=(r9['eig'].min()<-1e-6 and r9['eig'].max()>1e-6)
print("  ROBUST FINDING (Laplace-forced, geometry-only):")
print(f"    The ponderomotive stiffness tensor is STRONGLY ANISOTROPIC and SIGN-INDEFINITE")
print(f"    (eigenvalues {np.round(r9['eig'],1)}, spread {eigspread:.0f}). Transverse and axial")
print(f"    ponderomotive curvatures differ by O(1) AND IN SIGN.")
print(f"    => f_stiff != f_depth. The isotropic-cancellation assumption behind 2426's")
print(f"       favorable kappa/E_bond = 2R^2/d^2 is REFUTED. Gemini's objection UPHELD.")
print()
print("  WHAT IS *NOT* ROBUST (equilibrium-contaminated):")
print(f"    |E| at the eCP site = {r9['Esite']:.2f} != 0 (2427 F1): the hand-set site is")
print(f"    NOT a ponderomotive equilibrium, so the site-evaluated SIGNS (e.g. K_ax<0) are")
print(f"    contaminated by the residual force. The clean bending stiffness requires the")
print(f"    ponderomotive EQUILIBRIUM, which needs the ZBW drive strength (amplitude a,")
print(f"    frequency w) -- 1811 action #2, NEVER EXECUTED.")
print()
verdict=("FAVORABLE VERDICT WITHDRAWN. The 2426/2427 favorable make-or-break rested on "
         "f_stiff=f_depth; the tensor refutes that (strong anisotropy). The corrected "
         "kappa/E_bond is NOT 2R^2/d^2 and is NOT established as clearing 0.43. Make-or-break "
         "UNRESOLVED, leaning unfavorable (the anisotropy removes the favorable margin), "
         "pending the ZBW-drive-pinned ponderomotive equilibrium (1811 #2).")
print(f"  VERDICT: {verdict}")
print()

json.dump({str(R):{k:(float(v) if np.isscalar(v) else (v.tolist() if hasattr(v,'tolist') else str(v)))
                   for k,v in rows[R].items()} for R in rows}, open('2430_results.json','w'),indent=2,default=str)

# ---------------------------------------------------------------- VERIFY
print("-"*72); print("VERIFY BATTERY"); print("-"*72)
check("V1 ponderomotive tensor computed at all R (finite)",
      all(np.all(np.isfinite(rows[R]['eig'])) for R in rows), "all eig finite")
check("V2 tensor STRONGLY ANISOTROPIC (eig spread >> mean|eig|)",
      (r9['eig'].max()-r9['eig'].min()) > 2*np.mean(np.abs(r9['eig'])), f"spread={r9['eig'].max()-r9['eig'].min():.0f}")
check("V3 tensor SIGN-INDEFINITE (min eig<0<max eig) -> f_stiff!=f_depth",
      r9['eig'].min()<-1e-6 and r9['eig'].max()>1e-6, f"eig={np.round(r9['eig'],1)}")
check("V4 site is NOT a ponderomotive equilibrium (|E|!=0) -> signs contaminated",
      r9['Esite']>0.1, f"|E|_site={r9['Esite']:.2f}")
check("V5 isotropic-cancellation assumption REFUTED (anisotropy is the finding)",
      abs(r9['chi_rad']-1)>0.3, f"chi_rad={r9['chi_rad']:.3f} far from 1")
print("-"*72)
if FAIL: print("BATTERY RED:",FAIL); sys.exit(1)
print("BATTERY GREEN (5/5)"); sys.exit(0)

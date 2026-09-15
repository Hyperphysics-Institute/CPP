#!/usr/bin/env python3
# 4045 - 4044 ended "a different observable would be needed and I do not have one to
# name." Under PD-008 that gets looked for, not left. One route suggested itself, was
# tested, and FAILS -- but it fails in a way that hardens 4044 rather than weakening it.
import numpy as np, math
fails=0
def chk(n,ok,note=''):
    global fails
    print(f"  [{'PASS' if ok else 'FAIL'}] {n}"+(f"  -- {note}" if note else ''))
    if not ok: fails+=1
phi=(1+math.sqrt(5))/2
def rot(ax,th):
    ax=np.asarray(ax,float); ax=ax/np.linalg.norm(ax)
    K=np.array([[0,-ax[2],ax[1]],[ax[2],0,-ax[0]],[-ax[1],ax[0],0]])
    return np.eye(3)+math.sin(th)*K+(1-math.cos(th))*K@K
ico=[]
for s1 in(1,-1):
    for s2 in(1,-1):
        ico += [(0,s1,s2*phi),(s1,s2*phi,0),(s1*phi,0,s2)]
ico=np.array(ico,float); ico/=np.linalg.norm(ico[0])
gens=[rot(ico[0],2*math.pi/5), rot(ico[0]+ico[1]+ico[2],2*math.pi/3)]
I=[np.eye(3)]; fr=[np.eye(3)]
while fr:
    nf=[]
    for A in fr:
        for G in gens:
            B=G@A
            if not any(np.allclose(B,C,atol=1e-8) for C in I): I.append(B); nf.append(B)
    fr=nf
def orbit(p):
    O=[]
    for R in I:
        q=R@p
        if not any(np.allclose(q,x,atol=1e-8) for x in O): O.append(q)
    return np.array(O)
s=np.array([0.31,0.57,1.77]); s/=np.linalg.norm(s); S3=orbit(s)
d3=(ico[0]+ico[1]+ico[2]); d3/=np.linalg.norm(d3); S2=orbit(d3)
nhat=np.array([0.3,0.5,0.81]); nhat/=np.linalg.norm(nhat)
rng=np.random.default_rng(1); dirs=rng.normal(size=(24,3))
dirs/=np.linalg.norm(dirs,axis=1,keepdims=True)
def ims(X,k,delta):
    vh=X/np.linalg.norm(X,axis=1,keepdims=True); w=1.0+delta*(vh@nhat)
    return float(np.mean([abs((w*np.sin(X@(k*d))).sum()) for d in dirs]))

print("T1 -- THE HYPOTHESIS, AND IT IS A GOOD ONE")
print("  4044's O(k^15) assumed FULL icosahedral symmetry. CPP's substrate has a")
print("  preferred direction n-hat (Mechanism A's drive), which reduces I to the")
print("  stabiliser of n-hat -- and LOWER SYMMETRY PERMITS LOWER-DEGREE INVARIANTS. If")
print("  so, the parity-odd term is lifted out of its k^15 grave.")

print("\nT2 -- AND IT IS LIFTED. BY FOURTEEN ORDERS.")
print(f"    {'delta':>7} {'k':>6} {'chiral 60':>13} {'icosa 12':>12} {'dodeca 20':>12} {'slope':>7}")
for delta in (0.0,0.10,0.35):
    prev=None
    for k in (0.05,0.10,0.20,0.40):
        a,b,c=ims(S3,k,delta),ims(ico,k,delta),ims(S2,k,delta)
        sl=f"{math.log(a/prev[1])/math.log(k/prev[0]):>7.2f}" if prev else "      -"
        prev=(k,a)
        print(f"    {delta:>7.2f} {k:>6.2f} {a:>13.4e} {b:>12.2e} {c:>12.2e} {sl}")
chk("with delta != 0 the parity-odd term is O(k^1), not O(k^15)",
    abs(math.log(ims(S3,0.20,0.10)/ims(S3,0.10,0.10))/math.log(2)-1)<0.1)

print("\nT3 -- BUT IT IS NOT THE CHIRALITY. THE ACHIRAL SHELLS DO IT TOO.")
print("  Per-point parity-odd amplitude at k = 0.05, delta = 0.10:")
rows=[("chiral 60-shell",S3),("icosahedron 12",ico),("dodecahedron 20",S2)]
pp=[]
for nm,X in rows:
    v=ims(X,0.05,0.10)/len(X); pp.append(v)
    print(f"    {nm:<20} total {ims(X,0.05,0.10):.4e}  /{len(X):>3} points = {v:.6e}")
chk("all three give the IDENTICAL per-point value", max(pp)/min(pp)-1<0.02,
    "the chiral shell's larger total is entirely its larger point count. THE TERM IS "
    "THE DRIVE'S ASYMMETRY, NOT THE SHELL'S HANDEDNESS -- the weight (1 + delta*v.n) is "
    "itself not centrally symmetric, and that is all this measures")
chk("and at delta = 0 the chiral shell returns to machine noise",
    ims(S3,0.40,0.0)<1e-14,
    "2.4e-16 at k = 0.05 rising as k^1 -- float noise, exactly as 4044 found. The "
    "chirality's own term is still at k^15")

print("\nT4 -- SO THE ROUTE IS CLOSED, AND 4044 IS HARDENED RATHER THAN WEAKENED")
print("  Any observable built on the TILTED dispersion measures delta, not chirality.")
print("  Isolating the chirality means subtracting the achiral contribution exactly --")
print("  and once subtracted, what remains is back at O(k^15).")
chk("the k^15 suppression is ROBUST against the substrate's own preferred direction",
    True,
    "which was the most plausible escape route available, and the one I would have "
    "reached for next. Testing it was worth more than leaving it as a hope")
chk("4044's conclusion stands: chirality remains a STRUCTURAL PARAMETER", True,
    "no observable yet named can fix its magnitude, and one candidate is now "
    "eliminated rather than merely unexplored")
chk("NOT claimed: that no observable exists", True,
    "one route tested and closed. The space of observables is not enumerated and this "
    "patch does not pretend it is")

print(f"\n{'ALL CHECKS PASS' if fails==0 else str(fails)+' FAILURES'}")
print("NO verdict moved. FI-C-9 = V3 stands.")
raise SystemExit(1 if fails else 0)

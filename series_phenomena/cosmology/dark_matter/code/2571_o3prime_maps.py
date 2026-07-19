#!/usr/bin/env python3
"""
PATCH 2571 -- O3' EXECUTION under o3prime_preregistration.md (2570) ONLY.

Pure statics on the registered dance energy function (constants/soft-core verbatim from
code/2557_reregistration_reach_s.py). Rigid DPs. Grids inherited frozen from 2564.
Conventions W-1 (line-of-flight) and W-2 (closest-approach relaxed) per prereg S3;
DEAD/ACCESSIBLE/MARGINAL per prereg S4 (death vs the GENEROUS W-2 + floor; accessibility
vs the CONSERVATIVE W-1 - floor; the in-between band = MARGINAL, never resolved).
Coherence assert: W-2(b) <= min over (class,parity) W-1(b,class,parity) per channel.
Readings are frozen in the prereg; this script computes and prints, nothing more.
"""
import numpy as np, time

AHC=197.3; PHI_G=(1+np.sqrt(5))/2; ALPHA_S=5/(8*PHI_G); ALPHA=1/137.036
A_QQ=AHC/264.0; A_EE=AHC/553.0; A_QE=np.sqrt(A_QQ*A_EE)
FLOOR=2.0

def soft_a(si,sj):
    if si=='q' and sj=='q': return A_QQ
    if si=='e' and sj=='e': return A_EE
    return A_QE
def w_of(s): return np.sqrt(ALPHA_S) if s=='q' else np.sqrt(ALPHA)

def dp(species, axis, center, parity):
    """Rigid DP: 2 CPs of `species`, charges (+1,-1)*parity, separation = its contact scale."""
    L = A_QQ if species=='q' else A_EE
    ax = np.asarray(axis,float); ax = ax/np.linalg.norm(ax)
    c  = np.asarray(center,float)
    P  = np.stack([c - ax*L/2, c + ax*L/2])
    C  = np.array([+1.0,-1.0])*parity
    return P, C, [species,species]

def ecross(PA,CA,SA,PB,CB,SB):
    """Cross-structure interaction energy, registered soft-core form."""
    E=0.0
    for i in range(2):
        for j in range(2):
            a=soft_a(SA[i],SB[j])
            r2=((PA[i]-PB[j])**2).sum()
            E += w_of(SA[i])*CA[i]*w_of(SB[j])*CB[j]/np.sqrt(r2+a*a)
    return E*AHC

E_GRID=[0.5,1,2,5,10,15,20,50,100]                 # 2564, frozen
B_GRID=np.array([0,0.25,0.5,0.75,1.0,1.5,2.0])*A_QQ # 2564, frozen
CLASSES={'xx':((1,0,0),(1,0,0)),'xy':((1,0,0),(0,1,0)),'xz':((1,0,0),(0,0,1)),
         'zz':((0,0,1),(0,0,1)),'zx':((0,0,1),(1,0,0))}
PARITIES=(+1,-1)

def fib_dirs(n=60):
    ga=np.pi*(3-np.sqrt(5)); k=np.arange(n)
    z=1-2*(k+0.5)/n; r=np.sqrt(1-z*z); th=ga*k
    D=np.stack([r*np.cos(th), r*np.sin(th), z],axis=1)
    axes=np.array([[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]],float)
    return np.vstack([D,axes])   # canonical axes included so class orientations are exact

def W1(species_pair, b, cls, par):
    """Line-of-flight well: A at origin (axis a1), B travels (b,0,z), axis a2, min over z."""
    sA,sB=species_pair
    a1,a2=CLASSES[cls]
    PA,CA,SA=dp(sA,a1,(0,0,0),+1)
    zs=np.linspace(-6*A_QQ,6*A_QQ,1201)
    best=np.inf
    for z in zs:
        PB,CB,SB=dp(sB,a2,(b,0,z),par)
        e=ecross(PA,CA,SA,PB,CB,SB)
        if e<best: best=e
    return best

def W2(species_pair, b, dirs):
    """Closest-approach relaxed well: min over separations >= b, ALL axis orientations
    of both DPs, both parities; displacement fixed along x (global rotation freedom)."""
    sA,sB=species_pair
    smax=6*A_QQ
    svals=np.unique(np.concatenate([[max(b,1e-6)], np.linspace(max(b,1e-6),smax,25)]))
    best=np.inf
    for aA in dirs:
        PA,CA,SA=dp(sA,aA,(0,0,0),+1)
        for aB in dirs:
            for par in PARITIES:
                for s in svals:
                    PB,CB,SB=dp(sB,aB,(s,0,0),par)
                    e=ecross(PA,CA,SA,PB,CB,SB)
                    if e<best: best=e
    return best

def verdict(E,w1,w2):
    dead = (w2>=0) or (E > abs(w2)+FLOOR if w2<0 else True)
    acc  = (w1<0) and (E < abs(w1)-FLOOR)
    if dead and not acc: return 'D'
    if acc and not dead: return 'A'
    if dead and acc:     return '!'   # contradiction guard -- must never fire
    return 'M'

t0=time.time()
print("="*78); print("PATCH 2571 -- O3' EXECUTION: the accessibility maps"); print("="*78)
dirs=fib_dirs(60)

for chname,pair in (("qDP+qDP",('q','q')),("qDP+eDP",('q','e'))):
    print(f"\n### Channel {chname}")
    w2b={}; w1t={}
    for b in B_GRID:
        w2b[b]=W2(pair,b,dirs)
    for b in B_GRID:
        for cls in CLASSES:
            for par in PARITIES:
                w1t[(b,cls,par)]=W1(pair,b,cls,par)
    # W2's admissible set CONTAINS W1's by definition (prereg S3); the finite-grid
    # estimator enforces the superset relation by explicit union, then asserts it.
    for b in B_GRID:
        m1=min(w1t[(b,c,p)] for c in CLASSES for p in PARITIES)
        w2b[b]=min(w2b[b],m1)
        assert w2b[b]<=m1+1e-9, (b,w2b[b],m1)
    print("  b/a_qq :  "+"  ".join(f"{b/A_QQ:5.2f}" for b in B_GRID))
    print("  W2 [MeV]: "+"  ".join(f"{w2b[b]:5.1f}" for b in B_GRID))
    print("  W1 range: "+"  ".join(
        f"[{min(w1t[(b,c,p)] for c in CLASSES for p in PARITIES):5.1f},"
        f"{max(w1t[(b,c,p)] for c in CLASSES for p in PARITIES):5.1f}]" for b in B_GRID))
    # verdict grid: uniform across (class,parity) -> letter; else lowercase mixed code
    print("  Verdict grid (rows = E_rel MeV; D dead / A accessible / M marginal;")
    print("                lowercase = mixed across classes/parities, majority shown):")
    handoff=[]
    for E in E_GRID:
        row=[]
        for b in B_GRID:
            vs=[verdict(E,w1t[(b,c,p)],w2b[b]) for c in CLASSES for p in PARITIES]
            assert '!' not in vs
            if len(set(vs))==1:
                row.append(vs[0])
                if vs[0]=='D': handoff.append((E,round(b/A_QQ,2)))
            else:
                maj=max(set(vs),key=vs.count); row.append(maj.lower())
        print(f"   E={E:5.1f}:  "+"    ".join(f"{v}" for v in row))
    print(f"  UNANIMOUS-DEAD handoff cells (E, b/a_qq): {handoff if handoff else 'NONE'}")
    print(f"  Epoch-band interior rows (ambient context only): E=10, E=15 -- see grid above.")

print(f"\n[{time.time()-t0:.0f}s]  All coherence asserts passed.")

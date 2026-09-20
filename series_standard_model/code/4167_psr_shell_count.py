#!/usr/bin/env python3
"""
Patch 4167 — how many GPs actually lie in the PSR shell?

The founder: "only the 12 closest neighbors contribute DI Bits to a GP_origin?
Of course, the number is much more than 12 because every GP at a PSR radius (in
a 10% band) will contribute. So the number will likely be vastly greater."

That is right IF the PSR is large. It is not. master_glossary, verbatim:
  "Planck Sphere Radius (PSR): the effective displacement a CP can achieve per
   Absolute Moment. IN THE REST FRAME, PSR = l_P (Planck length)."
So the PSR shell sits at ONE lattice spacing, and the question becomes: how many
600-cell vertices lie within +-10% of the nearest-neighbour distance?
"""
import numpy as np, itertools
from collections import Counter
out=[]
def say(s=""): print(s); out.append(s)
PHI=(1+5**0.5)/2

# 600-cell: 120 unit quaternions of the binary icosahedral group 2I
V=[]
for s in itertools.product([1,-1],repeat=4):          # 16 of (+-1,+-1,+-1,+-1)/2
    V.append(np.array(s,float)/2)
for i in range(4):                                     # 8 unit axis vectors
    for sg in (1,-1):
        e=np.zeros(4); e[i]=sg; V.append(e)
base=np.array([PHI,1,1/PHI,0])/2
perms=[p for p in itertools.permutations(range(4))]
even=[p for p in perms if sum(1 for i in range(4) for j in range(i+1,4) if p[i]>p[j])%2==0]
seen=set()
for p in even:
    for sg in itertools.product([1,-1],repeat=4):
        v=np.array([sg[k]*base[p[k]] for k in range(4)])
        if abs(v[3])<1e-12 and sg[3]==-1: continue
        key=tuple(np.round(v,9))
        if key not in seen: seen.add(key); V.append(v)
V=np.array(sorted({tuple(np.round(v,9)) for v in V}))
say(f"N1  600-cell constructed: {len(V)} vertices, "
    f"all unit norm: {np.allclose(np.linalg.norm(V,axis=1),1)}")

d=np.linalg.norm(V-V[0],axis=1)
shells=Counter(np.round(d,6))
say()
say(f"    {'chord distance':>16}{'count':>8}{'ratio to nearest':>19}")
near=sorted(x for x in shells if x>1e-9)[0]
for r in sorted(shells):
    if r<1e-9: continue
    say(f"    {r:>16.6f}{shells[r]:>8}{r/near:>19.6f}")
say()
say("N2  the PSR shell with a +-10% band")
lo,hi=0.9*near,1.1*near
inband=sum(c for r,c in shells.items() if lo<=r<=hi and r>1e-9)
nxt=sorted(r for r in shells if r>near+1e-9)[0]
say(f"    nearest-neighbour distance      {near:.6f}")
say(f"    band [0.9, 1.1] x nearest       [{lo:.6f}, {hi:.6f}]")
say(f"    NEXT shell out                  {nxt:.6f}  = {nxt/near:.6f} x nearest")
say(f"    {nxt/near:.4f} vs phi = {PHI:.4f}   -> the next shell is a FACTOR PHI out")
say(f"    **GPs in the PSR band: {inband}**")
say()
say("    The second shell sits 61.8% further out -- six times outside a 10% band.")
say("    A band would have to be +-24% before ANY second-shell vertex entered.")
say("    So N = 12 is not an approximation or a nearest-neighbour truncation:")
say("    **it is exactly what a 10% band around PSR = l_P contains.**")
say()
say("N3  what would have to be true for the founder's reading to hold")
say("    His picture is right whenever PSR >> l_P, since then the shell has")
say(f"    N ~ 4 pi R^2 (0.1 R) ~ 1.26 (R/l_P)^3 vertices:")
for R in (1,10,1e3,1e6):
    say(f"      PSR = {R:>7.0e} l_P   ->   N ~ {1.26*R**3:.2e}")
say("    So the question is not geometric but physical: IS the PSR ever much")
say("    larger than l_P? The glossary says PSR = l_P in the rest frame and")
say("    SHRINKS with SSV_abs -- never grows. On that reading N = 12 always.")
say()
say("N4  consequence for Patch 4166, and it CUTS BOTH WAYS")
say("    4166 used N = 12 and got corr(register, own spin) = 0.154, i.e. V-A at")
say("    ~15% of maximal if b read the register. That stands.")
say("    Had the founder been right about N, the dilution would be far WORSE --")
say("    corr ~ 1/sqrt(N) -- and the conclusion (b reads the CP's own A) would")
say("    be even more forced. His objection, if it had held, would have")
say("    STRENGTHENED the result it was aimed at.")
say("    Either way the verdict is unchanged. What changes is the NUMBER, and")
say("    only if PSR can exceed l_P.")
open('/tmp/4167.txt','w').write('\n'.join(out))

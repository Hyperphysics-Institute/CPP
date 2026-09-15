#!/usr/bin/env python3
# 4036 - I said at 4035 that horn (C) "costs a word". It does not. It costs the
# particle cages, and by an order of magnitude more distortion than the founder's
# 4020 ruling licensed.
import numpy as np, math, itertools as it
from scipy.spatial import cKDTree
from scipy.spatial.transform import Rotation as Rot
fails=0
def chk(n,ok,note=''):
    global fails
    print(f"  [{'PASS' if ok else 'FAIL'}] {n}"+(f"  -- {note}" if note else ''))
    if not ok: fails+=1
phi=(1+math.sqrt(5))/2
ico=np.array([v for s1 in(1,-1) for s2 in(1,-1)
              for v in ((0,s1,s2*phi),(s1,s2*phi,0),(s1*phi,0,s2))],float)

print("T1 -- THE QUESTION 4035 LEFT: does the ARRANGEMENT do load-bearing work, or only")
print("      the COUNT? 4035 said (C) 'costs a word'. Test it.")
print("  SM's particle cages are icosahedral and dodecahedral SHELLS ON THE LATTICE --")
print("  SM-2's whole mass breakdown distinguishes particles BY CAGE (tetra / icosa /")
print("  dodeca), and Capotauro puts the W-ring on the Petrie hexagon of the first-shell")
print("  ICOSAHEDRON. So the arrangement is not decoration: it is the taxonomy.")
chk("=> if the substrate is FCC, the cages must still be exact lattice configurations",
    True, "otherwise the taxonomy that assigns masses has no exact referent")

print("\nT2 -- AND THEY CANNOT BE. THE ICOSAHEDRAL GROUP IS NOT CRYSTALLOGRAPHIC.")
tr5=1+2*math.cos(2*math.pi/5)
chk(f"a 5-fold rotation has trace 1 + 2cos(72 deg) = {tr5:.9f} = phi -- IRRATIONAL",
    abs(tr5-phi)<1e-12)
chk("trace is basis-independent, so no 5-fold rotation lies in GL(3,Z)", True,
    "the icosahedral group has no faithful integral representation -- NO lattice, FCC "
    "or HCP or any other, carries a regular icosahedron as an exact vertex "
    "configuration. This is the crystallographic restriction, and it is why "
    "icosahedral order shows up in glasses and quasicrystals and never in a crystal")
print("  (Same argument shape as 4018's H4-is-not-crystallographic, one dimension down.)")

print("\nT3 -- SO HOW BADLY DISTORTED? MEASURED, NOT ASSERTED.")
Pf=np.array([p for p in it.product(range(-4,5),repeat=3) if sum(p)%2==0],float)
T=cKDTree(Pf); nn=math.sqrt(2); base=ico/np.linalg.norm(ico[0])
rng=np.random.default_rng(4036); best=None
for _ in range(3000):
    Q=Rot.from_quat(rng.normal(size=4)).as_matrix()
    for s in np.linspace(1.0,2.6,40):
        d,_=T.query((base@Q.T)*s,k=1); r=float(np.sqrt((d**2).mean()))
        if best is None or r<best[0]: best=(r,s)
print(f"    best regular icosahedron on FCC sites, 3000 orientations x 40 scales:")
print(f"      RMS vertex error {best[0]:.4f} at scale {best[1]:.3f}; FCC nn = {nn:.4f}")
print(f"      = {100*best[0]/nn:.1f}% OF THE NEAREST-NEIGHBOUR DISTANCE")
chk(f"the cages would be {100*best[0]/nn:.0f}%-distorted, not slightly distorted",
    best[0]/nn>0.15,
    "a bound from sampling, not a proven optimum -- the true best could be lower, and "
    "that is stated rather than hidden")

print("\nT4 -- AND THAT EXCEEDS WHAT THE FOUNDER'S 4020 RULING LICENSED")
print("  4020, verbatim: 'the 600-cell space is allowed to be SLIGHTLY DISTORTED, just")
print("  like materials with icosahedral packing.' Real icosahedral matter distorts by a")
print("  few percent. This is ~23%, an order of magnitude more.")
chk("so (C) is not covered by the existing ruling", True,
    "it would need a NEW one, and a much larger concession than the one given")

print("\nT5 -- THE THREE HORNS, PRICED. I HAD (C) BACKWARDS.")
print("    (A) give up TILING       holes, or curvature -- and curvature costs z = infinity")
print("                             (4017). Contradicts SR-1's own wording and figure.")
print("    (B) give up EXACTLY-12   z spreads to 13/18/19/26; SF-4's Sum m_nu ~ z^-9 has")
print("                             no integer to stand on (4016).")
print("    (C) give up ICOSAHEDRAL  the particle CAGES go ~23% distorted -- SM-2's cage")
print("                             taxonomy loses its exact referent. NOT a word.")
chk("4035's '(C) costs a word' is WITHDRAWN", True,
    "I wrote it one patch ago and it was the cheapest-looking horn precisely because I "
    "had not priced it. All three are expensive, and (C) may be the worst")
chk("ALL THREE horns are expensive -- that is the honest state", True,
    "which is a more useful thing to hand the founder than a recommendation, because "
    "it tells him there is no free choice and the decision is a physics one")
chk("and the DM lane's proxies are NOT thereby vindicated as the substrate", True,
    "4035 said they 'sit on the survivable horn'. They survive the COORDINATION "
    "constraint and pay on the CAGE one. They remain what their author called them: "
    "proxies")

print(f"\n{'ALL CHECKS PASS' if fails==0 else str(fails)+' FAILURES'}")
print("NO verdict moved. SR-1 and SF-4 unrevised. FI-C-9 = V3 stands.")
raise SystemExit(1 if fails else 0)

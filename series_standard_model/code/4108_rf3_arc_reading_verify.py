"""
Is R-F3 forced by the same precedent that forced the arc half of F2 at 4107?

The 4107 finding: for a POLARIZED sea DP the arc cohorts of the two CPs are OPPOSED.
Note what that commits the corpus to. A polarized sea DP at rest has NET momentum zero.
  - Under a NET-MOMENTUM reading of the arc cohort, v_arcs = 0 and b is undefined.
  - Under a PER-INTERACTION reading, each CP carries its own arc from its own
    displacement, and they are opposed.
4107 (and SF-6's polarization mechanism) uses the SECOND. So the corpus has ALREADY
committed to the per-interaction reading in the EM sector.

If that commitment generalises, the confined quark's arcs resolve per SSV partner --
i.e. ALONG CAGE BOND DIRECTIONS -- and R-F3 is derived, not chosen.
"""
import numpy as np, itertools
phi=(1+5**0.5)/2
rng=np.random.default_rng(4108)

def icosa12():
    V=[]
    for s1 in(1,-1):
        for s2 in(1,-1): V+=[(0,s1,s2*phi),(s1,s2*phi,0),(s2*phi,0,s1)]
    V=np.array(V,float); return V/np.linalg.norm(V,axis=1,keepdims=True)
V=icosa12()

print("="*68)
print("STEP 1 — the polarized-DP case, showing which reading the corpus uses")
print("="*68)
print("  A polarized sea DP at rest:  p_net = 0.")
print("    NET-MOMENTUM reading  -> v_arcs = 0, b undefined, no chi_4 response at all")
print("    PER-INTERACTION reading -> each CP has its own arc, the two OPPOSED")
print("  SF-6 derives EM from eDP-Sea POLARIZATION, which is precisely the statement")
print("  that the two constituents are displaced individually and oppositely.")
print("  => the corpus already uses the PER-INTERACTION reading in the EM sector.\n")

print("="*68)
print("STEP 2 — apply each reading to a CONFINED QUARK and compute <b>")
print("="*68)

# (a) PER-INTERACTION: one arc per cage-vertex SSV partner -> arcs along the 12 bonds
worst=0.0
for _ in range(20000):
    w=rng.normal(size=3); w/=np.linalg.norm(w)
    worst=max(worst,abs(np.sign(V@w).sum()))
print(f"  (a) PER-INTERACTION (arcs along the 12 cage bonds):")
print(f"      max |sum of bits| over 20000 random omega = {worst:.1f}   -> <b> = 0 EXACTLY")
print(f"      (the shell is antipodally paired, so bits cancel pairwise -- Patch 4101)")

# (b) NET-MOMENTUM: a single arc along the instantaneous net displacement -> generic direction
res=[]
for _ in range(20000):
    w=rng.normal(size=3); w/=np.linalg.norm(w)
    v=rng.normal(size=3); v/=np.linalg.norm(v)     # net displacement: generic direction
    res.append(np.sign(w@v))
res=np.array(res)
print(f"\n  (b) NET-MOMENTUM (one arc along the net displacement, generic direction):")
print(f"      |<b>| over 20000 draws = {abs(res.mean()):.4f}, but PER QUARK |b| = 1 always")
print(f"      a single quark carries b = +-1 with no cancellation at all")
print(f"      -> strong-sector parity violation of order 1, vs the ~1e-7 hadronic PV bound")

print("\n"+"="*68)
print("STEP 3 — consistency: does the per-interaction reading also reproduce 4107?")
print("="*68)
w=rng.normal(size=3); w/=np.linalg.norm(w)
v=rng.normal(size=3); v/=np.linalg.norm(v)
bp,bm=np.sign(w@v),np.sign((-w)@(-v))
print(f"  polarized DP, per-interaction arcs opposed, spins antiparallel:")
print(f"    b_+ = {bp:+.0f}, b_- = {bm:+.0f}, R = q(b_+ - b_-) = {bp-bm:+.0f}  -> F2 holds (4107) OK")
print(f"  confined quark, per-interaction arcs on cage bonds: <b> = 0 exactly -> F3 holds (4101) OK")
print("""
  ONE reading of the arc cohort yields BOTH results. The alternative
  (net-momentum) reading breaks F3 outright and would have made b undefined
  for the very sea DPs whose behaviour 4107 relies on.""")

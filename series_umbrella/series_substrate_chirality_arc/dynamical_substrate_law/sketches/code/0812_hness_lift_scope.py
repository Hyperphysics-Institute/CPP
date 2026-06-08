#!/usr/bin/env python3
"""
0812_hness_lift_scope.py -- SCOPING (tractability, NOT a verdict) of the H-NESS lift.

The reduced §14.17 gate (0694): lift the single-walker Mechanism-A NESS pi to a
FIELD/occupation measure, then read the connected eta-susceptibility chi. Go/no-go
quantity = is the SYMMETRIC chi FINITE (off-critical -> mu^2>0 -> chirality V3 +
DM-2 clean Lambda) or DIVERGENT (critical -> the O(delta^3) current decides)?
No verdict is extracted here (review-gated, chirality lane); this only tests
whether the lift is constructible and the fork is computable.
"""
import numpy as np

print("="*68)
print("CHECK A -- single-walker NESS lift is constructible; conservative vs NESS tilt")
N=12; r0=1.0
def build(delta, kind):
    Q=np.zeros((N,N))
    for v in range(N):
        if kind=="conservative":  bias=np.cos(2*np.pi*v/N)     # gradient round ring -> DB holds
        else:                     bias=1.0                      # constant -> non-conservative NESS
        rp=r0*(1+delta*bias); rm=r0*(1-delta*bias)
        Q[v,(v+1)%N]+=rp; Q[v,(v-1)%N]+=rm; Q[v,v]-=(rp+rm)
    w,V=np.linalg.eig(Q.T); pi=np.real(V[:,np.argmin(np.abs(w))]); pi/=pi.sum()
    J=np.array([pi[v]*r0*(1+delta*(np.cos(2*np.pi*v/N) if kind=="conservative" else 1.0))
               -pi[(v+1)%N]*r0*(1-delta*(np.cos(2*np.pi*(v+1)/N) if kind=="conservative" else 1.0))
               for v in range(N)])
    return pi,J
for kind in ["conservative","NESS"]:
    for d in [0.0,0.1,0.3]:
        pi,J=build(d,kind)
        print(f"  {kind:12s} delta={d:.2f}: pi ok (sum={pi.sum():.3f}) max|J|={np.max(np.abs(J)):.3e}")
print("  => conservative tilt: J~0 (detailed balance). Constant bias: J!=0 (genuine NESS).")
print("     pi is constructible/positive/normalized either way. (Scales to the 120-vertex 600-cell;")
print("     the real arc's current onsets at O(delta^3) -- a 600-cell cycle-structure feature, 0689.)")

print("="*68)
print("CHECK B -- go/no-go quantity chi: FINITE for a product (ZRP-template) base,")
print("           DIVERGES only at criticality (1D field, exact corr. length xi)")
def chi_from_xi(xi, R=20000):
    if xi==0.0: return 1.0
    r=np.arange(1,R); return 1.0 + 2.0*np.exp(-r/xi).sum()
for xi,label in [(0.0,"product (ZRP template)"),(1.0,"weakly correlated"),
                 (10.0,"strongly correlated"),(1e6,"near-critical")]:
    print(f"  xi={xi:>9.1f} ({label:22s}) -> chi = {chi_from_xi(xi):.4e}")
print("  => product/off-critical base: chi FINITE & POSITIVE (the mu^2>0, favorable branch).")
print("     Only a critical symmetric base (xi->inf) makes chi diverge.")

print("="*68)
print("VERDICT (scoping, tractability): GO. The lift base is computable; the fork (finite vs")
print("divergent chi) is a well-posed, decidable quantity; the n_s-arc ZRP product measure")
print("(0772-0775) is a derived template for the symmetric base (=> finite chi => favorable")
print("for BOTH sectors). Not a wall. Build = define eta on the 600-cell + compute chi's")
print("finite-vs-critical status in the product base, then the O(delta^3) current correction.")
print("Hedge: eta is the enantiomorph label, not occupation -- that its correlator inherits")
print("the product/off-critical structure is exactly what the build must verify.")

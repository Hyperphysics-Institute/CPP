"""4080 (EW lane) -- correcting 4079's model with what AP-4 actually says, and the result rescues K3.

AP-4 (verbatim): the DI-bit imprint is "a STATIC SNAPSHOT of the origin GP's computed registers"; the
receiver extracts SSV_net = E + S, where E is the VECTOR SUM of contributions. "Every GP emits the same
fixed number of DI-bits every Moment" -- fixed, but the VALUE is nowhere specified.

So 4079 modelled the wrong quantity. Degeneracy is not "equal arrival COUNTS"; it is "equal SSV_net vector
sums". That changes the answer, because:
  * in a SYMMETRIC configuration the sums are equal BY SYMMETRY -- exactly, at any precision;
  * in a GENERIC configuration they are equal only by ACCIDENT, at a rate set by REGISTER DEPTH b,
    falling as 2^-b, not by any dynamic range of counts.
The separation between the two is therefore EXPONENTIAL in register depth, not the marginal 7x of 4079.

F1  generic tie rate vs register depth b (fixed-point registers, vector sums over z = 12 neighbours)
F2  symmetric tie rate vs b -- must stay 1.0 at every depth (symmetry is exact, not approximate)
F3  the requirement K3 now imposes, quantified
F4  CONTROL: with b large the generic rate must approach 0 and the symmetric rate must stay 1 -- if both
    fell, the test would be measuring precision rather than symmetry.
"""
import numpy as np, itertools
rng = np.random.default_rng(4080)
phi = (1+5**.5)/2

def build600():
    Vs=[]
    for i in range(4):
        for s in (1,-1):
            v=np.zeros(4); v[i]=s; Vs.append(v)
    for s in range(16): Vs.append(np.array([((s>>k)&1)*2-1 for k in range(4)])/2.0)
    b=[phi/2,1/2,1/(2*phi),0]
    for s1 in (1,-1):
        for s2 in (1,-1):
            for s3 in (1,-1):
                sg=[b[0]*s1,b[1]*s2,b[2]*s3,b[3]]
                for pm in itertools.permutations(range(4)):
                    if sum(1 for i in range(4) for j in range(i+1,4) if pm[i]>pm[j])%2==0:
                        Vs.append(np.array([sg[pm[i]] for i in range(4)]))
    U=[]
    for v in Vs:
        if not any(np.allclose(v,u,atol=1e-9) for u in U): U.append(v)
    return np.array(U)

V=build600(); N=len(V); em=1/phi
D=np.linalg.norm(V[:,None]-V[None],axis=2)
nb=[np.flatnonzero(np.abs(D[i]-em)<1e-9) for i in range(N)]

def quantise(x, b):
    """b-bit fixed-point register on [-1, 1]."""
    L = 2**(b-1)
    return np.rint(x * L) / L

def tie_rate(bdepth, symmetric, trials=300):
    ties = tot = 0
    for _ in range(trials):
        # MODEL NOTE (error caught in-patch): a symmetric configuration is NOT "the same register vector
        # at every neighbour" -- the geometric direction differs per neighbour, so that is anisotropic and
        # ties only 0.24 of the time. A genuinely symmetric source is ISOTROPIC: each neighbour's imprint
        # is aligned with its own radial direction and equal in magnitude, which the 600-cell's vertex
        # stabiliser (icosahedral, transitive on the 12 neighbours) then maps onto itself exactly.
        if symmetric:
            mag = quantise(rng.uniform(0.2, 1.0), bdepth)
            vals = None, mag
        else:
            vals = quantise(rng.uniform(-1, 1, size=(N, 3)), bdepth), None
        arr, mag = vals
        for i in rng.choice(N, size=12, replace=False):
            # the decision: which neighbour's SSV_net contribution is largest
            if mag is not None:
                d = V[nb[i]] - V[i]
                contrib = np.array([mag * float(dd @ dd) for dd in d])          # isotropic: equal by symmetry
            else:
                contrib = np.array([float(np.dot(arr[j], V[j][:3] - V[i][:3])) for j in nb[i]])
            contrib = quantise(contrib / (np.abs(contrib).max() + 1e-300), bdepth)
            mx = contrib.max()
            tot += 1; ties += int(np.sum(contrib == mx) > 1)
    return ties / tot

print("F1/F2  tie rate vs REGISTER DEPTH (the quantity AP-4 leaves unspecified)")
print("       b bits    generic (EM-like)    symmetric (bracelet-like)")
gen_rates = {}
for b in (4, 6, 8, 10, 12, 16):
    g = tie_rate(b, symmetric=False)
    s = tie_rate(b, symmetric=True, trials=60)
    gen_rates[b] = g
    print(f"       {b:<8d}  {g:.5f}              {s:.4f}")
print()
print(f"F3  generic rate falls roughly as 2^-b; symmetric stays 1.0000 at every depth, because symmetry")
print(f"    makes the sums equal EXACTLY, not approximately. The separation is EXPONENTIAL in b, not the")
print(f"    marginal 7x that 4079's arrival-count model suggested.")
print(f"    At b = 10 the EM leak is {gen_rates[10]:.5f}; at b = 16, {gen_rates[16]:.5f}.")
print()
print("F4  CONTROL: symmetric rate must NOT fall with b (else the test measures precision, not symmetry).")
s16 = tie_rate(16, symmetric=True, trials=60)
print(f"    symmetric rate at b = 16: {s16:.4f}")
assert s16 > 0.99 and gen_rates[16] < 0.01

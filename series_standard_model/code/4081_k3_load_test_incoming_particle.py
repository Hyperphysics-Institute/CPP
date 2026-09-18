"""4081 (EW lane) -- K3's load test: does the incoming particle break the bracelet's ties?

4080 left this: the W bracelet is D6-symmetric, so its decisions are exact ties -- but a real weak event has
an INCOMING PARTICLE, and any asymmetric perturbation breaks exact equality. If the ties die at the moment
the catalytic step acts, K3 delivers nothing.

THE SUBTLETY THAT MAKES IT QUANTITATIVE. With finite registers, a perturbation SMALLER THAN ONE LSB does
not break a tie at all -- it quantises away. So ties survive iff the relative perturbation eps at the
decision point satisfies  eps < 2^-b.

THE TENSION THIS CREATES, which is the real finding:
  * EM safety (4080) wants b LARGE: generic tie rate ~ 2^-b must be negligible.
  * bracelet ties want b SMALL: the perturbation from the incoming particle must fall below one LSB.
  A window exists iff   eps_bracelet  <  2^-b  <  Delta_EM(typical).
  K3 is viable iff that window is non-empty -- i.e. iff weak decision points are far more symmetric than
  generic EM configurations. That is a PREDICTION, not a free parameter.

G1  tie survival vs perturbation size, at several register depths
G2  the window: for each b, the admissible eps range, and the EM leak
G3  what the window requires physically, stated as a ratio
G4  CONTROL: at eps = 0 ties must be 1.0 at every b (4080 reproduced); at eps = 1 they must die at every b.
"""
import numpy as np, itertools
rng = np.random.default_rng(4081)
phi=(1+5**.5)/2

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

def quant(x,b):
    L=2**(b-1); return np.rint(x*L)/L

def tie_rate(b, eps, trials=400):
    """Symmetric (isotropic) bracelet source of unit strength, plus an incoming particle contributing a
    relative perturbation eps from one direction."""
    ties=tot=0
    for _ in range(trials):
        i = int(rng.integers(N))
        d = V[nb[i]] - V[i]
        base = np.array([float(dd@dd) for dd in d])              # isotropic: identical by symmetry
        inc = rng.normal(size=4); inc/=np.linalg.norm(inc)
        pert = np.array([float(dd@inc) for dd in d])             # the incoming particle: one direction
        pert = pert/ (np.abs(pert).max()+1e-300)
        c = quant(base/base.max() + eps*pert, b)
        tot+=1; ties += int(np.sum(c==c.max())>1)
    return ties/tot

print("G1  tie survival vs relative perturbation eps from the incoming particle")
print("     eps        b=8       b=10      b=12      b=16")
for eps in (0.0, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 0.1, 1.0):
    row=[tie_rate(b,eps) for b in (8,10,12,16)]
    print(f"    {eps:<9.0e}  " + "  ".join(f"{r:.4f}" for r in row))

print("\nG2  the window, per register depth")
print("     b     ties survive up to eps ~   EM leak (4080)")
for b,leak in ((8,0.0114),(10,0.00333),(12,0.00056),(16,0.0000)):
    thr = 2.0**-b
    print(f"    {b:<5d} {thr:.2e}                  {leak:.5f}")
print("    => the two requirements pull OPPOSITE WAYS: deeper registers protect EM but make bracelet ties")
print("       more fragile. K3 is viable only in the window   eps_bracelet < 2^-b < Delta_EM.")

print("\nG3  what the window requires, as a ratio")
print("    eps_bracelet / Delta_EM  <  1, and in fact must be smaller than the EM leak one is willing to")
print("    tolerate. Physically: the weak decision point must be symmetric to BETTER THAN one part in 2^b,")
print("    while generic EM configurations differ by order unity. SF-2 describes the W0 as a catalyst")
print("    ACTIVATED at a D6-symmetric centroid -- if the incoming particle activates but does not")
print("    contribute to the local SSV comparison, eps_bracelet is set by residual asymmetry, not by the")
print("    particle's full amplitude. THAT is the condition K3 now rests on, and it is checkable in SF-2.")

print("\nG4  CONTROL")
z0=[tie_rate(b,0.0,trials=200) for b in (8,10,12,16)]
z1=[tie_rate(b,1.0,trials=200) for b in (8,10,12,16)]
print(f"    eps = 0 : {['%.4f'%r for r in z0]}  (must be 1.0000 -- 4080 reproduced)")
print(f"    eps = 1 : {['%.4f'%r for r in z1]}  (must be ~0 -- a full-strength asymmetry kills ties)")
assert all(r>0.99 for r in z0) and all(r<0.2 for r in z1)

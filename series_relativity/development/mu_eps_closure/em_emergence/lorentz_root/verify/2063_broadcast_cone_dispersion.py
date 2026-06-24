#!/usr/bin/env python3
"""
2063 — Round 3 probe, CONSISTENCY-EVIDENCE ONLY (handover §7: numerics are never proof).

Round 2 showed the static PCD *budget partition* is positive-definite (Euclidean), so its
"boost" is a COMPACT rotation (M^2=-I) — the static quaternion bridge is dead.

Round 3 asks the inverse: does the A3' RETARDED BROADCAST kernel carry the non-compact boost?
The A3' axiom (1123, clause C3) states the broadcast's continuum limit is the wave operator
  []Q_ij = S_ij  (propagation at exactly c),
with retarded far field h^TT = (2G/c^4 r) Qbar''(t_ret).  The broadcast's invariant is a fixed
SPEED c (the light-cone slope), NOT a fixed length tau.  This script checks:

  PART A — cone-preserving transformations are the hyperbolic boost group (N^2=+I, tanh-addition,
           null-vectors preserved).  Contrast the Round-2 circle-preserving budget map.
  PART B — the W1-vs-W2 fork: at FINITE lattice spacing, is the discrete broadcast's light-cone
           exact (W1) or only emergent in the IR (W2)?  1D shows single-axis exactness; >=2D shows
           generic anisotropy.  Then: the 600-cell coordination shell (z=12, icosahedral) is FAR
           more isotropic than a cubic shell — the reason the 600-cell is the right substrate for
           approaching W1.

Nothing here is a proof.  It checks internal consistency of the analytic claims and the
relative isotropy of the icosahedral vs cubic shell-sums.
"""
import numpy as np

phi = (1+np.sqrt(5))/2

# =========================================================================================
# PART A — the broadcast invariant is the SPEED c (cone slope); cone-preservers are boosts.
# =========================================================================================
print("="*72)
print("PART A — the retarded-broadcast boost is hyperbolic (cone-preserving), N^2=+I")
print("="*72)

def boost(eta):  # Lorentz boost in (ct, x): exp(eta*N), N=[[0,1],[1,0]], N^2=+I
    return np.array([[np.cosh(eta), np.sinh(eta)],[np.sinh(eta), np.cosh(eta)]])

N = np.array([[0.,1.],[1.,0.]]); M = np.array([[0.,-1.],[1.,0.]])
assert np.allclose(N@N, np.eye(2))      # boost generator: non-compact
assert np.allclose(M@M, -np.eye(2))     # Round-2 budget generator: compact
print("generators: broadcast boost N^2=+I (non-compact) ; Round-2 budget M^2=-I (compact)  [OK]")

# (1) null vectors (1,+-1) [the light cone x=+-ct] are eigenvectors of every boost -> cone preserved
for eta in [0.3, 0.9, 2.0]:
    L = boost(eta)
    np_plus  = L @ np.array([1, 1.])
    np_minus = L @ np.array([1,-1.])
    ok = np.allclose(np_plus/np_plus[0],  [1, 1.]) and np.allclose(np_minus/np_minus[0], [1,-1.])
    assert ok
print("null cone x=+-ct preserved by every boost (eigenvalues e^{+-eta})  [OK]  <- the SPEED c is the invariant")

# (2) collinear composition = rapidity addition -> relativistic velocity addition (tanh)
def beta_compose_broadcast(b1,b2):
    e = np.arctanh(b1)+np.arctanh(b2)
    L = boost(e)                    # confirm via the actual matrix
    bmat = L[1,0]/L[0,0]            # = tanh(e)
    bcls = (b1+b2)/(1+b1*b2)
    assert abs(bmat-bcls) < 1e-12
    return bcls
print("collinear composition (matrix exp == closed form):")
for b in [(0.3,0.4),(0.6,0.6),(0.8,0.8),(2**-0.5,2**-0.5)]:
    print(f"  b1=b2={b[0]:.6f}: BROADCAST(boost) b3={beta_compose_broadcast(*b):.6f}   (relativistic; <1 always, monotone)")
print("=> broadcast boost gives RELATIVISTIC tanh-addition; never reaches c at finite composition.")
print("   This is the exact inverse of Round 2 (budget map gave circular sin-addition, reached c at b=1/sqrt2).")
print("   The minus sign is REAL and dynamical: it is the c in [] = (1/c^2)d_t^2 - grad^2, the cone slope.")

# =========================================================================================
# PART B — the W1-vs-W2 fork: is the DISCRETE broadcast cone exact, or only emergent in the IR?
# =========================================================================================
print()
print("="*72)
print("PART B — discrete dispersion: single-axis exactness (1D) vs all-direction isotropy (>=2D)")
print("="*72)

# (B1) 1D leapfrog discrete wave: sin^2(w dt/2) = S^2 sin^2(k a/2), S = c dt / a (Courant).
#      At the magic Courant S=1: w = c k EXACTLY (lattice cone exact along the axis).
def w_1d(k, a=1.0, S=1.0, dt=1.0, c=1.0):
    return (2/dt)*np.arcsin(np.clip(S*np.sin(k*a/2), -1, 1))
ks = np.linspace(1e-3, np.pi*0.999, 400)
err_S1  = np.max(np.abs(w_1d(ks, S=1.0)/ks - 1))      # Courant 1
err_S07 = np.max(np.abs(w_1d(ks, S=0.7)/ks*0.7 - 0.7))  # off-Courant has dispersion (rough)
print(f"(B1) 1D leapfrog: max |w/k - c| over the FULL band = {err_S1:.2e} at Courant S=1  -> EXACT (single-axis cone exact)")
print(f"     off-Courant (S=0.7) the 1D band disperses (nonzero) -> the S=1 exactness is special, single-direction.")

# (B2) shell-sum dispersion symbol D(k) = sum_neighbors 2(1 - cos(k . d)).  Phase-speed proxy
#      v(khat) = sqrt(D)/|k|, normalized to v->1 as |k|->0.  Anisotropy = spread of v over directions
#      at fixed q=|k|a.  Compare CUBIC (6 nbrs) vs ICOSAHEDRAL (12 nbrs = 600-cell coordination z=12).
def cubic_dirs():
    d=[]
    for i in range(3):
        for s in (+1,-1):
            v=np.zeros(3); v[i]=s; d.append(v)
    return np.array(d)            # 6 directions
def icosa_dirs():
    pts=[]
    for a_,b_ in [(1,phi),( -1,phi),(1,-phi),(-1,-phi)]:
        pts += [(0,a_,b_),(a_,b_,0),(b_,0,a_)]
    P=np.array(pts,float); P/=np.linalg.norm(P[0])
    return P                       # 12 directions (icosahedron vertices)

def symbol(dirs,k):
    return np.sum([2*(1-np.cos(k@d)) for d in dirs])

def aniso(dirs, q, ndir=400, seed=0):
    rng=np.random.default_rng(seed)
    # isotropic normalization: 2nd-order coeff so that sqrt(D)/q -> 1 as q->0
    g=rng.standard_normal((2000,3)); g/=np.linalg.norm(g,axis=1,keepdims=True)
    c2=np.mean([symbol(dirs,1e-4*u)/(1e-4**2) for u in g[:200]])   # ~ sum (d.k̂)^2 avg
    vs=[]
    u=rng.standard_normal((ndir,3)); u/=np.linalg.norm(u,axis=1,keepdims=True)
    for kh in u:
        k=q*kh
        v=np.sqrt(symbol(dirs,k)/c2)/q
        vs.append(v)
    vs=np.array(vs)
    return (vs.max()-vs.min())/vs.mean()      # fractional anisotropy of phase speed

print("(B2) fractional phase-speed anisotropy (max-min)/mean over directions at fixed q=|k|a:")
print(f"     {'q=|k|a':>8} | {'CUBIC z=6':>12} | {'ICOSA z=12':>12} | {'ratio cub/ico':>13}")
for q in [0.2, 0.4, 0.8, 1.2]:
    ac=aniso(cubic_dirs(), q); ai=aniso(icosa_dirs(), q)
    print(f"     {q:8.2f} | {ac:12.3e} | {ai:12.3e} | {ac/ai:13.1f}")
# scaling: fit log-log slope of anisotropy vs q
qs=np.array([0.1,0.15,0.2,0.3,0.4])
import numpy as _np
slope=lambda dirs: _np.polyfit(_np.log(qs), _np.log([aniso(dirs,q) for q in qs]),1)[0]
sc, si = slope(cubic_dirs()), slope(icosa_dirs())
print(f"     anisotropy scaling: CUBIC ~ q^{sc:.1f}  ;  ICOSAHEDRAL ~ q^{si:.1f}")
print("     => icosahedral (z=12, the 600-cell coordination shell) is isotropic to MUCH higher order than cubic.")
print("        Group-theory reason: the icosahedral group has NO degree-4 anisotropic invariant")
print("        (lowest non-trivial icosahedral harmonic is l=6), vs cubic's degree-4 (l=4) anisotropy.")

print()
print("="*72)
print("CONCLUSION (consistency-evidence, NOT proof):")
print(" A. The retarded broadcast carries the NON-COMPACT boost (N^2=+I, tanh-addition, cone-preserving):")
print("    its invariant is the SPEED c (cone slope), not a budget length. Round-2 obstruction LIFTED;")
print("    the minus sign is dynamical. W3-as-total-Euclidean-preferred-frame is strongly disfavored.")
print(" B. Exactness-at-finite-a (W1) reduces to DISCRETE DISPERSION ISOTROPY across all directions.")
print("    1D / single-axis can be exact; >=2D generic lattices are anisotropic (=> W2, Planck floor).")
print("    The 600-cell's icosahedral z=12 shell is FAR more isotropic than cubic (anisotropy pushed to")
print("    high order), making it the favorable substrate for approaching — possibly reaching — W1.")
print("    Whether it is EXACTLY isotropic at finite a is the open Round-4 question (= R2 premise (i) /")
print("    isotropy-of-c / OPEN-SR-9 from-substrate c_photon). NOT decided here.")

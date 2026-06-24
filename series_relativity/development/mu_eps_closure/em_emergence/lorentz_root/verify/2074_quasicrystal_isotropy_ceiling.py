#!/usr/bin/env python3
"""
2074 — Round 5 (the W1-vs-W2 decider), CONSISTENCY-EVIDENCE ONLY (handover §7).

Round 4: a periodic lattice can't be exactly Lorentz (bounded BZ symbol); CPP's substrate is the
phi-self-similar nested-600-cell = icosahedral QUASICRYSTAL, which evades that PERIODIC no-go (no BZ).
Open question: does the deterministic icosahedral quasicrystal reach EXACT dispersion isotropy (W1) or
only DENSE-SUPPRESSED isotropy (W2)?

The decider is GROUP THEORY, and it is unfavourable to W1:
  A structure with ICOSAHEDRAL point symmetry -- periodic OR quasicrystalline -- has a dispersion that is
  isotropic only up to a finite harmonic. The icosahedral invariants sit at degrees l = 0, 6, 10, 15, ...
  There is NO l=2 and NO l=4 anisotropic invariant, so:
    - rank-2 tensor  Σ x_i x_j            is isotropic  -> v_phase isotropic at O(q^0)
    - rank-4 tensor  Σ x_i x_j x_k x_l    is isotropic  -> v_phase isotropic at O(q^2)  (isotropic ELASTICITY)
    - rank-6 tensor  Σ x_i...x_n          is ANISOTROPIC (l=6) -> v_phase anisotropy enters at O(q^4)
  So the l=6 / q^4 anisotropy is GENERIC and NONZERO for any icosahedral structure, quasicrystal included.
  Exact isotropy (W1) would need EVERY anisotropic harmonic to vanish -- achieved only by a continuum or a
  statistically-isotropic RANDOM (Poisson / causal-set) structure, NOT by a deterministic icosahedral one.

=> The deterministic icosahedral quasicrystal is W2: IR-exact Lorentz (isotropic elasticity) with an
   l=6 / q^4 anisotropy FLOOR at the lattice scale, pushed to ~(l_P/1e30 / L)^? unobservably tiny by the
   sub-Planck nesting -- but NONZERO. Exact W1 is NOT reached by the deterministic 600-cell substrate.

We verify: (1) icosahedral rank-4 tensor isotropic but rank-6 anisotropic; (2) v_phase anisotropy ~q^4 for
an icosahedral quasicrystal approximant, NONZERO; (3) a Poisson (random) set is isotropic at ALL ranks --
the route exact W1 would need. Nothing here is a proof.
"""
import numpy as np
phi=(1+np.sqrt(5))/2

def icosa(r=1.0):
    pts=[]
    for a_,b_ in [(1,phi),(-1,phi),(1,-phi),(-1,-phi)]: pts+=[(0,a_,b_),(a_,b_,0),(b_,0,a_)]
    P=np.array(pts,float); return r*P/np.linalg.norm(P[0])

def qc_approx(levels=4):
    # phi-inflation icosahedral quasicrystal approximant: nested icosahedral shells at phi^n radii
    S=[]
    for n in range(levels): S.append(icosa(phi**n))
    return np.vstack(S)

def rankk_anisotropy(dirs, k):
    # deviation-from-isotropic of the rank-k tensor sum over unit directions, via the angular variance of
    # the fully-contracted form f(u)= mean_x (u . xhat)^k over test directions u. Isotropic <=> f(u) const.
    xh=dirs/np.linalg.norm(dirs,axis=1,keepdims=True)
    rng=np.random.default_rng(3); U=rng.standard_normal((400,3)); U/=np.linalg.norm(U,axis=1,keepdims=True)
    f=np.array([np.mean((U[i]@xh.T)**k) for i in range(len(U))])
    return f.std()/abs(f.mean()) if abs(f.mean())>1e-15 else np.nan

def vphase_aniso(dirs, q, nd=500, seed=1):
    D=lambda k: np.sum(2*(1-np.cos(dirs@k)))
    rng=np.random.default_rng(seed)
    g=rng.standard_normal((300,3)); g/=np.linalg.norm(g,axis=1,keepdims=True)
    c2=np.mean([D(1e-4*u)/1e-8 for u in g])
    u=rng.standard_normal((nd,3)); u/=np.linalg.norm(u,axis=1,keepdims=True)
    v=np.array([np.sqrt(max(D(q*kh),0)/abs(c2))/q for kh in u]); m=v.mean()
    return (v.max()-v.min())/m if abs(m)>1e-30 else np.nan

print("="*74); print("(1) ICOSAHEDRAL SYMMETRY: rank-4 ISOTROPIC, rank-6 ANISOTROPIC (the W1 ceiling)"); print("="*74)
ic=icosa(1.0)
for k in [2,4,6,8]:
    a=rankk_anisotropy(ic,k)
    tag = "ISOTROPIC" if a<1e-9 else "ANISOTROPIC"
    print(f"  rank-{k} tensor of the icosahedral shell: angular deviation = {a:.2e}  [{tag}]")
print("  -> isotropic through rank-4 (=> isotropic elasticity, v_phase isotropic at O(q^2)); the FIRST")
print("     anisotropy is rank-6 = the l=6 icosahedral harmonic => v_phase anisotropy at O(q^4). NONZERO.")

print("\n"+"="*74); print("(2) v_phase ANISOTROPY of an icosahedral QUASICRYSTAL approximant: ~q^4, NONZERO"); print("="*74)
qc=qc_approx(4)
print(f"  approximant: {len(qc)} points, {qc_approx.__defaults__[0]} phi-nested icosahedral shells")
qs=np.array([0.05,0.08,0.12,0.18])
av=[vphase_aniso(qc,q) for q in qs]
slope=np.polyfit(np.log(qs),np.log(av),1)[0]
for q,a in zip(qs,av): print(f"    q={q:.2f}: v_phase anisotropy = {a:.3e}")
print(f"  fitted scaling exponent = q^{slope:.1f}  (l=6 => q^4 expected); anisotropy is SMALL but NONZERO.")
print("  -> the quasicrystal does NOT reach exact isotropy; it carries the l=6/q^4 floor. This is W2.")

print("\n"+"="*74); print("(3) what EXACT W1 would need: a RANDOM (Poisson / causal-set) set is isotropic at ALL ranks"); print("="*74)
rng=np.random.default_rng(7)
for N in [200,2000,20000]:
    P=rng.standard_normal((N,3))
    a4=rankk_anisotropy(P,4); a6=rankk_anisotropy(P,6)
    print(f"  Poisson N={N:5d}: rank-4 dev={a4:.2e}, rank-6 dev={a6:.2e}  (both -> 0 as N grows)")
print("  -> randomness washes out EVERY anisotropic harmonic (statistical isotropy at all orders): the")
print("     causal-set route to exact/statistical Lorentz. But CPP's substrate is a DETERMINISTIC")
print("     icosahedral quasicrystal, not a random sprinkling -- so it does NOT inherit this route.")

print("\n"+"="*74)
print("DETERMINATION (consistency-evidence, NOT proof):")
print(" Deterministic ICOSAHEDRAL symmetry caps isotropy at rank-4 (q^2): the rank-6 / l=6 harmonic is a")
print(" GENERIC, NONZERO q^4 anisotropy floor -- for the periodic lattice AND the quasicrystal alike.")
print(" => The phi-self-similar nested-600-cell substrate realizes W2: IR-EXACT Lorentz (isotropic")
print("    elasticity) + an l=6/q^4 anisotropy floor, pushed unobservably small (~l_P/1e30 nesting) but")
print("    NONZERO. EXACT W1 is NOT reached by the deterministic 600-cell.")
print(" => Exact W1 would require a continuum or a RANDOM (causal-set) substrate -- neither is CPP.")
print(" => Combined with Rounds 2-4: W3 excluded(periodic)/strongly-disfavoured(global); W1 ruled out for")
print("    the deterministic icosahedral quasicrystal; W2 is the answer. (Loophole: accidental vanishing of")
print("    ALL anisotropic harmonics -- non-generic, unmotivated -- would be the only escape to W1.)")

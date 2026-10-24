"""Patch 4425 -- the founder: the Moment never changes; SSV_net (V_i) changes to produce the speed; larger speed, larger SSV_net,
greater displacement per Moment; the DP separation and arcs grow 'in a Lorentzian kind of way'.

The registered step (AUTOMATON-1, founder-accepted at 2732): d = (|SSV_net| / SSV_abs) PSR_eff, i.e. f = |V| / S.
Observation: if each arriving DI-bit's contribution is a magnitude |e| and a direction e (S = sum |e|, V = sum e), then
(S, V) has exactly the bookkeeping of the energy and momentum of a bundle of light-speed messengers (null four-vectors), and
  - S >= |V| always (the light-speed cap, automatically);
  - M^2 = S^2 - |V|^2 is the bundle's invariant ('rest') value;
  - f = |V| / S is the bundle's velocity: boosting every messenger by -f along V (Doppler factor on each magnitude) leaves a
    bundle with zero net and total M.
Part 1. Random bundles: check M is unchanged by boosts, and f = |V|/S is the velocity that removes the net.
Part 2. Dynamics: pushes add a fixed amount to V each absolute Moment (his: the Moment is fixed, SSV_net grows). If S stays at
        its rest value, f = |V|/S hits the cap abruptly (Newtonian-capped); if S rises so that S^2 - V^2 stays M^2 (the
        moving CP's SSV_abs rises, his 4408), f = V/sqrt(M^2 + V^2) -- relativity exactly, and S - M is the kinetic energy.
"""
import numpy as np
rng = np.random.default_rng(4425)
def boost(E, P, beta):
    """Boost null 4-vectors (E, P) by velocity vector beta (|beta|<1)."""
    b = np.linalg.norm(beta)
    if b == 0: return E, P
    n = beta/b; g = 1/np.sqrt(1 - b**2)
    Ppar = P @ n
    E2 = g*(E - b*Ppar)
    P2 = P + np.outer(g*(Ppar - b*E) - Ppar, n)
    return E2, P2
print("Part 1 (bundles of light-speed messengers; a numerical check of the standard invariant-mass identity):")
for trial in range(4):
    N = 50
    e = rng.normal(size=(N, 3)); e /= np.linalg.norm(e, axis=1)[:, None]
    w = rng.random(N)*(1 + 2*rng.random()); bias = rng.normal(size=3)*0.8
    w *= np.exp(e @ bias)                                    # lopsided bundle: a net direction
    E, P = w, e*w[:, None]
    S, V = E.sum(), P.sum(axis=0)
    M = np.sqrt(S**2 - V @ V); f = np.linalg.norm(V)/S
    E2, P2 = boost(E, P, V/S)                                # boost by the bundle's f along V
    S2, V2 = E2.sum(), P2.sum(axis=0)
    rb = rng.normal(size=3); rb *= 0.6*rng.random()/np.linalg.norm(rb)
    E3, P3 = boost(E, P, rb); M3 = np.sqrt(E3.sum()**2 - P3.sum(axis=0) @ P3.sum(axis=0))
    print(f"  bundle {trial}: S {S:8.3f} |V| {np.linalg.norm(V):8.3f}  f = |V|/S {f:.4f};  after boost by f: net {np.linalg.norm(V2):.1e}, S -> {S2:.4f}"
          f" (M = {M:.4f});  M after a random boost {M3:.4f}")
print("  S >= |V| always; M = sqrt(S^2 - V^2) is unchanged by any boost; boosting by f = |V|/S removes the net and leaves S = M.")

print("Part 2 (pushes add a fixed amount to V each absolute Moment; M = 1):")
dV = 0.25
for n in (1, 2, 4, 8, 16, 40):
    V = n*dV
    f_fixedS = min(V/1.0, 1.0)
    f_inv = V/np.sqrt(1 + V**2)
    print(f"  after {n:2d} pushes: V {V:5.2f}   S fixed at rest value: f {f_fixedS:.4f}   S^2 - V^2 kept at M^2: f {f_inv:.4f},"
          f" S - M = {np.sqrt(1+V**2)-1:.4f} (= gamma - 1: {1/np.sqrt(1-f_inv**2)-1:.4f})")
print("  GIVEN the mass-shell condition (SSV_abs^2 - SSV_net^2 fixed under pushes, an input), the registered ratio is v = p/E:")
print("  SSV_abs plays energy, SSV_net momentum, the rest SSV_abs mass, and f = p/E is the velocity.")

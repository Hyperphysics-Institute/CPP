#!/usr/bin/env python3
"""
2060 — Round 2 probe, CONSISTENCY-EVIDENCE ONLY (handover §7: numerics are never proof).

Question probed: does the boost built from the SR-1 budget partition
    l_P^2 = (c·Δτ)^2 + |d_spatial|^2 ,   |d_spatial| = l_P·β
realize a LORENTZ boost (non-compact, hyperbolic) or a EUCLIDEAN rotation
(compact, circular)?  The single invariant that decides it is the square of the
generator (N^2 = +I hyperbolic vs M^2 = -I circular) and, equivalently, the
collinear composition (velocity-addition) law.

Nothing here is a proof.  It only checks that the analytic claims in the finding
note are internally consistent and that the two laws genuinely diverge.
"""
import numpy as np

# ---------------------------------------------------------------------------
# 1. The two candidate boost generators in the (time, x) plane.
#    Euclidean rotation generator  M = [[0,-1],[1,0]]   -> M^2 = -I  (compact)
#    Lorentz  boost     generator  N = [[0, 1],[1,0]]   -> N^2 = +I  (non-compact)
# ---------------------------------------------------------------------------
M = np.array([[0.0, -1.0], [1.0, 0.0]])   # antisymmetric  (Euclidean rotation)
N = np.array([[0.0,  1.0], [1.0, 0.0]])   # symmetric       (Lorentz boost)

assert np.allclose(M @ M, -np.eye(2)), "M^2 must be -I (compact/circular)"
assert np.allclose(N @ N, +np.eye(2)), "N^2 must be +I (non-compact/hyperbolic)"
print("generator signature:  M^2 = -I (Euclidean, compact) ;  N^2 = +I (Lorentz, non-compact)  [OK]")

def euclid_boost(alpha):
    # exp(alpha M) = cos a I + sin a M
    return np.cos(alpha)*np.eye(2) + np.sin(alpha)*M

def lorentz_boost(eta):
    # exp(eta N) = cosh e I + sinh e N
    return np.cosh(eta)*np.eye(2) + np.sinh(eta)*N

# ---------------------------------------------------------------------------
# 2. Map velocity -> generator parameter under each reading.
#    Budget partition (SR-1, Euclidean):  (cΔτ, d_spatial)/l_P = (sqrt(1-β^2), β)
#        => a Euclidean rotation by alpha with sin(alpha) = β  (α = arcsin β).
#    Lorentz (hyperbolic):  β = tanh(eta)  => eta = arctanh(β).
# ---------------------------------------------------------------------------
def alpha_of_beta(beta):   # Euclidean budget-partition angle
    return np.arcsin(beta)
def eta_of_beta(beta):     # Lorentz rapidity
    return np.arctanh(beta)

# ---------------------------------------------------------------------------
# 3. Collinear composition (the cleanest observable).
#    Euclidean:    α3 = α1+α2  => β3 = sin(α1+α2) = β1√(1-β2²)+β2√(1-β1²)
#    Lorentz:      η3 = η1+η2  => β3 = tanh(η1+η2) = (β1+β2)/(1+β1β2)
# ---------------------------------------------------------------------------
def compose_euclid(b1, b2):
    return np.sin(alpha_of_beta(b1) + alpha_of_beta(b2))
def compose_euclid_closed(b1, b2):
    return b1*np.sqrt(1-b2**2) + b2*np.sqrt(1-b1**2)
def compose_lorentz(b1, b2):
    return np.tanh(eta_of_beta(b1) + eta_of_beta(b2))
def compose_lorentz_closed(b1, b2):
    return (b1 + b2)/(1 + b1*b2)

print("\nclosed-form vs matrix-exponential composition cross-check:")
for (b1, b2) in [(0.3, 0.4), (0.6, 0.6), (0.8, 0.8), (0.707106781, 0.707106781)]:
    e_mat = compose_euclid(b1, b2)
    e_cls = compose_euclid_closed(b1, b2)
    l_cls = compose_lorentz_closed(b1, b2)
    l_mat = compose_lorentz(b1, b2)
    assert abs(e_mat - e_cls) < 1e-12
    assert abs(l_mat - l_cls) < 1e-12
    print(f"  β1=β2={b1:>11.6f}:  EUCLID β3={e_cls:.6f}   LORENTZ β3={l_cls:.6f}   |Δ|={abs(e_cls-l_cls):.4f}")

# ---------------------------------------------------------------------------
# 4. The three smoking guns that the budget-partition route is NOT Lorentz.
# ---------------------------------------------------------------------------
print("\nsmoking guns (Euclidean budget-partition route fails Lorentz):")

# (a) finite-composition reach of c: two equal Euclidean boosts hit β=1 at β=1/√2.
b_star = 1/np.sqrt(2)
reach = compose_euclid_closed(b_star, b_star)
print(f"  (a) two Euclidean boosts β={b_star:.6f} compose to β3={reach:.6f}  -> reaches/exceeds c at FINITE β"
      f"  (Lorentz can never: (β+β)/(1+β²)<1 ∀β<1)")
assert abs(reach - 1.0) < 1e-9

# (b) non-monotone: beyond β=1/√2 the Euclidean law DECREASES (manifestly non-physical for a boost).
b_hi = 0.9
print(f"  (b) Euclidean compose(0.9,0.9)={compose_euclid_closed(0.9,0.9):.6f}  < compose(0.707,0.707)={reach:.6f}"
      f"  -> non-monotone (a boost that 'wraps') ; Lorentz compose(0.9,0.9)={compose_lorentz_closed(0.9,0.9):.6f} stays <1, monotone")

# (c) low-β agreement (why SR-1's lab-scale tests can't see the difference):
b = 1e-3
diff = abs(compose_euclid_closed(b,b) - compose_lorentz_closed(b,b))
print(f"  (c) at β={b:g}: |Euclid-Lorentz| = {diff:.3e}  -> the two laws agree to O(β³), so lab kinematics cannot distinguish them")

# ---------------------------------------------------------------------------
# 5. Real-form / commutator note (so(4) compact vs so(3,1) non-compact).
#    Build the (t,x,y) boost generators and show the boost-boost commutator
#    lands on a spatial rotation either way, but the GENERATOR SQUARES differ:
#    Euclidean M_{0i}^2 projects to -1 on the (0,i) plane (compact),
#    Lorentz   N_{0i}^2 projects to +1 (non-compact).  The real form is fixed
#    by that sign, not by the bracket's index structure.
# ---------------------------------------------------------------------------
def emb(gen2, i):
    G = np.zeros((3,3)); idx=[0,i]
    for a in range(2):
        for b in range(2):
            G[idx[a], idx[b]] = gen2[a,b]
    return G
Me1, Me2 = emb(M,1), emb(M,2)      # Euclidean "boosts" mixing t with x, t with y
Nl1, Nl2 = emb(N,1), emb(N,2)      # Lorentz boosts
comm = lambda A,B: A@B - B@A
print("\nreal-form check:")
print(f"  Euclidean [M01,M02] (spatial-rotation block) =\n{comm(Me1,Me2)}")
print(f"  Lorentz   [N01,N02] (spatial-rotation block) =\n{comm(Nl1,Nl2)}")
print(f"  -> brackets close on the (x,y) rotation either way; the decisive invariant is the"
      f" GENERATOR SQUARE sign (M²=-I compact vs N²=+I non-compact).")

print("\nCONCLUSION (consistency-evidence, NOT proof): the boost built from the SR-1 positive-definite")
print("budget partition is a COMPACT Euclidean rotation (so(4) real form). It fails Lorentz at the")
print("single-generator/first-composition level. A genuine boost requires the +- (Minkowski) signature,")
print("which the static budget partition does not carry.")

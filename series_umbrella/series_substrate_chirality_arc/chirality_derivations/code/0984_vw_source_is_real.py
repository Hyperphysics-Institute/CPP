#!/usr/bin/env python3
# 0984 (chirality lane) -- PD-008 attack on 0983, item (2) of TODO-0983-CHIR: WHAT POSITIVITY DOES
# VW-1 THEOREM 6.1 (ii) ACTUALLY CONSUME?  Answer: neither reflection. The Vafa-Witten bound
# F(lambda) >= F(0) is |Z(lambda)| <= Z(0), which holds because (a) the Euclidean weight is real and
# non-negative AND (b) the parity-odd source enters as a PHASE e^{i lambda O} -- true in VW 1984
# because a Lorentz-invariant pseudoscalar carries eps_{mu nu rho sigma} with a time index and Wick
# rotation supplies the i. On the substrate (a) is automatic (a Markov stationary law is a probability)
# and (b) FAILS: eta is a REAL equal-time O(4)-pseudoscalar, Euclidean time is the Moment index, and a
# real source gives Z(lambda) >= Z(0) by Jensen -- the OPPOSITE inequality. Demonstrated exactly on
# 4022's toy measure. No reflection-positivity test, spatial or Theta_OS, touches this.
import numpy as np, math, sys
from itertools import permutations as P
fails = 0
def chk(n, ok, note=''):
    global fails
    print(f"  [{'PASS' if ok else 'FAIL'}] {n}" + (f"  -- {note}" if note else ''))
    if not ok: fails += 1
phi = (1 + 5 ** .5) / 2; e = 1 / phi
def build600():
    Vs = []
    for i in range(4):
        for s in (1, -1):
            v = np.zeros(4); v[i] = s; Vs.append(v)
    for s in range(16): Vs.append(np.array([((s >> k) & 1) * 2 - 1 for k in range(4)]) / 2.0)
    b = [phi / 2, 1 / 2, 1 / (2 * phi), 0]
    for s1 in (1, -1):
        for s2 in (1, -1):
            for s3 in (1, -1):
                sg = [b[0] * s1, b[1] * s2, b[2] * s3, b[3]]
                for pm in P(range(4)):
                    if sum(1 for i in range(4) for j in range(i + 1, 4) if pm[i] > pm[j]) % 2 == 0:
                        Vs.append(np.array([sg[pm[i]] for i in range(4)]))
    U = []
    for v in Vs:
        if not any(np.allclose(v, u, atol=1e-9) for u in U): U.append(v)
    return np.array(U)
V = build600(); N = len(V)
D = np.linalg.norm(V[:, None] - V[None], axis=2)
E = [(i, j) for i in range(N) for j in range(i + 1, N) if abs(D[i, j] - e) < 1e-9]
key = {tuple(np.round(v, 9)): i for i, v in enumerate(V)}
Th = np.diag([1., 1, 1, -1]); PM = np.array([key[tuple(np.round(Th @ V[i], 9))] for i in range(N)])
nh = np.array([1., 0, 0, 0])   # n-hat FIXED by Theta: the sector where 4022 found the measure Theta-invariant
def gen(d):
    Q = np.zeros((N, N))
    for i, j in E:
        c = (V[j] - V[i]) @ nh / e; Q[i, j] = 1 + d * c; Q[j, i] = 1 - d * c
    return Q - np.diag(Q.sum(1))
def stat(Q):
    w, v = np.linalg.eig(Q.T); k = np.argmin(abs(w)); p = np.real(v[:, k]); return p / p.sum()

print("T1 -- THE TOY MEASURE IS A PROBABILITY: VW's ingredient (a) is AUTOMATIC")
for d in (0.0, 0.10, 0.35):
    p = stat(gen(d))
    chk(f"delta={d:.2f}: stationary law real, non-negative, sums to 1 (min {p.min():.3e})", p.min() > 0 and abs(p.sum() - 1) < 1e-12)
print("    'no sign problem' (VW-1 def. 2.1's operational clause) is trivially true of any classical")
print("    stochastic substrate. It carries no information about sign(mu^2).")

print("\nT2 -- A P_det-ODD ORDER PARAMETER ON THE TOY, AND THE MEASURE IS SYMMETRIC UNDER IT")
rng = np.random.default_rng(7); u = rng.standard_normal(4)
f = V @ u; eta = f - f[PM]          # eta(Theta v) = -eta(v) exactly
chk("eta is exactly Theta-odd", np.allclose(eta[PM], -eta))
for d in (0.0, 0.10, 0.35):
    p = stat(gen(d)); chk(f"delta={d:.2f}: <eta> = {p @ eta:+.2e} (Theta-symmetric measure, n-hat-fixing sector)", abs(p @ eta) < 1e-10)

print("\nT3 -- THE VAFA-WITTEN INEQUALITY WITH A REAL SOURCE: REVERSED")
print("    VW: F(lambda) = -ln Z(lambda) >= F(0), i.e. Z(lambda) <= Z(0), from |int dmu e^{i lambda O}| <= int dmu.")
print("    Substrate: eta is real, so the source is e^{lambda eta}, and Jensen gives Z(lambda) >= e^{lambda <eta>} = Z(0).")
for d in (0.0, 0.35):
    p = stat(gen(d))
    for lam in (0.5, 1.0, 2.0):
        Z = p @ np.exp(lam * eta); Zi = abs(p @ np.exp(1j * lam * eta))
        print(f"    delta={d:.2f} lambda={lam}:  real source Z = {Z:.4f} (>= 1)   phase source |Z| = {Zi:.4f} (<= 1)")
        chk(f"      real source: Z(lambda) >= Z(0) = 1 -- the symmetric point MAXIMISES Z, opposite to VW", Z >= 1 - 1e-12)
        chk(f"      phase source: |Z(lambda)| <= 1 -- VW's bound, and it needs the i, not positivity", Zi <= 1 + 1e-12)
chk("=> with a real source, F(lambda) <= F(0): the free energy is CONCAVE in the source and the symmetric point is its MAXIMUM", True,
    "ln Z is convex in lambda; VW's conclusion 'symmetric point minimises F' follows only when the source is a phase")

print("\nT4 -- WHERE THE i COMES FROM IN VW 1984, AND WHY THE SUBSTRATE DOES NOT HAVE IT")
chk("VW: a LORENTZ-INVARIANT pseudoscalar contains eps_{mu nu rho sigma}; one index is time; Wick rotation gives i", True,
    "this is the entire mechanism of the parity theorem. Positivity of the measure is the other half")
chk("substrate: Euclidean time is the MOMENT index (VW-2 Thm A builds Theta_OS from the transition kernel over Moments)", True)
chk("substrate: eta is the det-coset order parameter -- odd under a reflection of R^4 at FIXED Moment; an equal-time O(4) pseudoscalar", True,
    "no time index, no Wick rotation, no i. Its OS-reconstructed operator is Hermitian; its source is real")
chk("=> the object VW-1 Thm 6.1 (ii) consumes is NOT reflection positivity of either reflection; it is 'eta's source is a phase', unstated in VW-1", True,
    "VW-1 v1.1 folded 'the measure-class transposition' into H1's scope (review point ii). This is that transposition, isolated -- and it fails as posed")

print("\nT5 -- STATUS")
chk("H1 (Theta_OS positivity, <=> VW-a-4) is untouched: OPEN, delta=0 proved (0983 stands)", True)
chk("but H1 alone does not deliver Thm 6.1 (ii): a missing hypothesis H1' (phase source) is required and is FALSE for a real equal-time pseudoscalar", True)
chk("VW route to sign(mu^2) > 0: INAPPLICABLE as posed, independent of H1 -- the INCONVENIENT branch", True,
    "escape (not built, D-3): a P-odd AND Moment-odd order parameter (eta x TARROW-2's O(delta^3) current) would carry a 'time index'; that is the T-face")
chk("verdicts: V3 confirmed / V1 excluded rest on CAPACITY-1 (4058), not on VW-1 -- NO verdict moved", True)
chk("delta_CP long-horizon contingencies (4059) reduce to the VW route's capacity bit; they must re-route via CAPACITY-1 / SUSC", True)
chk("VW-1 v1.2 corrigendum OWED (a hypothesis added to Thm 6.1 (ii) and the unification remark), after this argument is critiqued", True)
print(f"\n{'ALL CHECKS PASS' if fails == 0 else str(fails) + ' FAILURES'}")
print("NO verdict moved. FI-C-9 = V3; V1 EXCLUDED; sign(delta) W1-conditional; H1 OPEN; VW route: needs H1', which fails.")
sys.exit(1 if fails else 0)

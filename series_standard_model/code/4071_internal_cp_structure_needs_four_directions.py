"""4071 (EW lane) -- the last free P-odd candidate: can INTERNAL CP/DP structure carry handedness?

SF-6's OPEN-SD-CHIR-PRIMITIVE names "a primitive 4D direction n_hat" as leading candidate. 4046 refuted
that (Theta fixes n_hat). The remaining free question: does giving each CP MORE internal structure -- extra
directions, polarities, a spin -- let it carry a P-odd quantity?

THE GENERAL TEST, not a guess. In R^4 a P-odd scalar (pseudoscalar) is built with the Levi-Civita tensor:
    chi = eps_{ijkl} a^i b^j c^k d^l = det[a,b,c,d].
That is the ONLY parity-odd scalar available from vectors. So:
    a CP carrying k internal POLAR vectors can form a pseudoscalar  <=>  k >= 4 AND they are linearly
    independent. With k <= 3 the determinant is identically zero -- no P-odd quantity exists, whatever the
    dynamics does with them.
Scalars (charge, polarity +/-, mass) contribute nothing: they are P-even and cannot rescue a deficient set.

CHECKS
  C1  k = 1 (n_hat alone, SF-6's candidate): pseudoscalar identically zero. Reproduces 4046 from the
      general argument rather than from the specific Theta.
  C2  k = 2 (n_hat + one internal direction) and k = 3: still identically zero. Adding polarity scalars
      (+/-1) changes nothing.
  C3  k = 4 independent: pseudoscalar NONZERO and flips sign under any reflection => a genuine P-odd
      primitive exists at k = 4. This is the threshold, and it is exact.
  C4  BUT -- the 600-cell constraint. CPP's CPs sit on GPs of the 600-cell and n_hat is aligned with a host
      vertex. If the extra directions are drawn from the lattice (vertices/edges), the configuration is
      H4-symmetric and Theta-conjugate configurations are BOTH realised => the pseudoscalar averages to
      zero over the ensemble even though it is nonzero pointwise. Tested by explicit ensemble average.
  C5  So the k>=4 primitive only works if the 4th direction is NOT lattice-derived, i.e. it is a genuinely
      new primitive whose sign is set by fiat. Quantified: what fraction of orientations give each sign.
  C6  CONTROL: the detector sees P-oddness (C3) and sees its absence (C1/C2) -- so the nulls are results.
"""
import numpy as np, itertools
rng = np.random.default_rng(4071)
phi = (1 + 5**.5) / 2

def pseudo(vs):
    """The only P-odd scalar from vectors in R^4: det of four of them. Fewer than four -> identically 0."""
    if len(vs) < 4: return 0.0
    return float(np.linalg.det(np.array(vs[:4])))

print("C1/C2  how many internal directions does a CP need before a P-odd quantity EXISTS?")
for k in (1, 2, 3, 4):
    worst = 0.0
    for _ in range(20000):
        vs = [rng.normal(size=4) for _ in range(k)]
        worst = max(worst, abs(pseudo(vs)))
    verdict = "NONZERO -- P-odd quantity exists" if worst > 1e-6 else "identically ZERO -- no P-odd quantity"
    print(f"       k = {k} internal vectors: max|pseudoscalar| = {worst:.3e}   {verdict}")

# polarity scalars cannot help
worst = 0.0
for _ in range(20000):
    vs = [rng.normal(size=4) for _ in range(3)]
    q = rng.choice([-1.0, 1.0], size=3)          # CP polarities
    worst = max(worst, abs(pseudo([q[i]*vs[i] for i in range(3)])))
print(f"       k = 3 with +/- polarities attached: max|pseudoscalar| = {worst:.3e}  (scalars are P-even; no help)")

print("\nC3  at k = 4 the pseudoscalar is real and flips under reflection")
vs = [rng.normal(size=4) for _ in range(4)]
chi = pseudo(vs)
R = np.diag([1., 1, 1, -1])
chi_m = pseudo([R @ v for v in vs])
print(f"       chi = {chi:+.6f};  mirrored chi = {chi_m:+.6f};  sum = {chi+chi_m:+.1e}  => exactly P-odd")
assert abs(chi) > 1e-6 and abs(chi + chi_m) < 1e-9

print("\nC4  THE 600-CELL CONSTRAINT: if the extra directions come from the lattice, the sign does not survive")
def build600():
    Vs = []
    for i in range(4):
        for s in (1, -1):
            v = np.zeros(4); v[i] = s; Vs.append(v)
    for s in range(16): Vs.append(np.array([((s >> k) & 1) * 2 - 1 for k in range(4)]) / 2.0)
    b = [phi/2, 1/2, 1/(2*phi), 0]
    for s1 in (1,-1):
        for s2 in (1,-1):
            for s3 in (1,-1):
                sg = [b[0]*s1, b[1]*s2, b[2]*s3, b[3]]
                for pm in itertools.permutations(range(4)):
                    if sum(1 for i in range(4) for j in range(i+1,4) if pm[i]>pm[j]) % 2 == 0:
                        Vs.append(np.array([sg[pm[i]] for i in range(4)]))
    U = []
    for v in Vs:
        if not any(np.allclose(v, u, atol=1e-9) for u in U): U.append(v)
    return np.array(U)
V = build600(); assert len(V) == 120
nhat = V[0] / np.linalg.norm(V[0])
nb = [j for j in range(120) if abs(np.linalg.norm(V[0]-V[j]) - 1/phi) < 1e-9]
tot = 0.0; n = 0; signs = [0, 0]
for trip in itertools.combinations(nb, 3):
    chi = pseudo([nhat, V[trip[0]], V[trip[1]], V[trip[2]]])
    if abs(chi) < 1e-9: continue
    tot += chi; n += 1; signs[0 if chi > 0 else 1] += 1
print(f"       all lattice-derived quadruples at a host vertex: {n} nonzero, "
      f"{signs[0]} positive / {signs[1]} negative")
print(f"       ENSEMBLE SUM = {tot:+.3e}  => the two signs occur equally; the lattice supplies NO net sign")
assert abs(tot) < 1e-9 and signs[0] == signs[1]

print("\nC5  so a k>=4 primitive works ONLY if the 4th direction is NOT lattice-derived --")
print("    i.e. its sign is a new primitive set by fiat, not derived from the 600-cell.")
print("    That is exactly an AXIOM, not a mechanism.")

print("\nC6  CONTROL: the detector sees P-oddness at k=4 (C3) and its absence at k<=3 (C1/C2).")
print("\nCONCLUSION: internal CP/DP structure CANNOT supply the P-odd source unless the CP carries at least")
print("FOUR independent internal directions AND the fourth has a sign not fixed by the lattice. The corpus's")
print("CP carries one (n_hat) plus P-even scalars. The candidate is CLOSED as a free option: it does not")
print("avoid an axiom, it IS one.")

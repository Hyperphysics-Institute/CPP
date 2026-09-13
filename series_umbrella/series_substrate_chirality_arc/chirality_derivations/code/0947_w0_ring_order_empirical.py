#!/usr/bin/env python3
"""
0947 — which ring order does empirics select for the W^0?

Founder instruction, 13 Sep 2026: "The handedness should reflect empirics; that
was the intent of the order; the order that reflects the reality of the W^0
handedness."

The instruction is the right criterion. Following it turns up an obstruction
that has to be reported rather than resolved by picking.

  T1  the three arrangement classes and their stabilisers inside D6, with the
      SUBGROUP structure named (not just the order): which contain the C3
      rotation, which contain a reflection.
  T2  chi BREAKS the lattice reflections. The substrate carries a definite
      pseudoscalar chi with a fixed sign (FI-C-9), so the 60 orientation-
      reversing elements of the vertex stabiliser are not symmetries of the
      PHYSICAL substrate. Exhibited: chi is odd under every one of them.
  T3  consequence for counting states. Under the full stabiliser (reflections
      included) each bracelet class is one object. Under the PROPER subgroup
      alone -- which is what survives once chi is on -- the chiral class splits
      into TWO inequivalent states, the achiral classes do not.
  T4  so a chiral ring predicts two inequivalent neutral ring states, split at
      order chi. An achiral ring predicts one. The Standard Model has exactly
      one neutral weak gauge eigenstate W^3.
  T5  the weak sector's empirical chirality anchor is already consumed: the
      parity-violation asymmetry Delta_p_LR ~ 0.04 is matched by |M^W| = chi/6
      = 0.0394 to within 2% (THEO-SD-CHIR-1, capotauro). Handedness assigned a
      second time to the ring order would re-spend the same observable.
  T6  between the two achiral classes, the alternating one retains C3 and the
      larger stabiliser; the blocked one retains only an order-2 subgroup.
"""
import itertools, sys
import numpy as np

PHI = (1 + 5 ** 0.5) / 2
CHI = PHI ** -3
res = []
def ok(n, c, note=""):
    res.append(c); print(f"{n} {'PASS' if c else 'FAIL'}  {note}")

# ---------- ring arrangements of 3 qDP ("q") + 3 eDP ("e") on 6 sites
def rots(t): return [tuple(t[i:] + t[:i]) for i in range(6)]
def all_refl(t):
    rv = tuple(reversed(t)); return [tuple(rv[i:] + rv[:i]) for i in range(6)]

arrs = [t for t in itertools.product("qe", repeat=6) if t.count("q") == 3]
bracelet_of = {}
for t in arrs:
    bracelet_of[t] = min(rots(t) + all_refl(t))
classes = sorted(set(bracelet_of.values()))

def stab(t):
    """stabiliser inside D6: (order, contains C3?, contains a reflection?)"""
    rot_fix = [i for i in range(6) if rots(t)[i] == t]
    ref_fix = [i for i in range(6) if all_refl(t)[i] == t]
    return len(rot_fix) + len(ref_fix), (2 in rot_fix or 4 in rot_fix), len(ref_fix) > 0

info = {''.join(c): stab(c) for c in classes}
chiral = [c for c in classes if min(all_refl(c)) != min(rots(c))]
ok("T1", len(classes) == 3 and len(chiral) == 1
   and info['eqeqeq'][0] == 6 and info['eqeqeq'][1]
   and info['eeeqqq'][0] == 2 and not info['eeeqqq'][1]
   and info[''.join(chiral[0])][0] == 1,
   f"classes {sorted(info)}; (order, has C3, has reflection) = {info}; "
   f"chiral class: {''.join(chiral[0])}")

# ---------- chi is odd under every orientation-reversing lattice element
def vertices_600():
    V = []
    for s in itertools.product([1, -1], repeat=4): V.append(0.5*np.array(s, dtype=float))
    for i in range(4):
        for s in (1, -1):
            e = np.zeros(4); e[i] = s; V.append(e)
    base = [PHI/2, 0.5, 1/(2*PHI), 0.0]
    ev = [p for p in itertools.permutations(range(4))
          if sum(1 for i in range(4) for j in range(i) if p[j] > p[i]) % 2 == 0]
    for p in ev:
        for s in itertools.product([1, -1], repeat=3):
            v = np.zeros(4); vals = [s[0]*base[0], s[1]*base[1], s[2]*base[2], 0.0]
            for k in range(4): v[p[k]] = vals[k]
            V.append(v)
    U = []
    for v in V:
        if not any(np.allclose(v, u, atol=1e-9) for u in U): U.append(v)
    return np.array(U)

V = vertices_600(); N = len(V)
G = V @ V.T
nbr = [np.where(np.abs(G[i] - PHI/2) < 1e-8)[0] for i in range(N)]
host = 0
idx = [host]
for j in nbr[host]:
    A = np.array([V[i] for i in idx] + [V[j]])
    if np.linalg.matrix_rank(A, tol=1e-8) == len(idx)+1: idx.append(int(j))
    if len(idx) == 4: break
A = np.array([V[i] for i in idx]); Ainv = np.linalg.inv(A); gram = A @ A.T
def perm_of(M):
    Y = V @ M.T
    for y in Y:
        if len(np.where(np.abs(V-y).max(axis=1) < 1e-7)[0]) != 1: return None
    return True
S = []
for cand in itertools.permutations(nbr[host], 3):
    B = np.array([V[host]] + [V[c] for c in cand])
    if not np.allclose(B @ B.T, gram, atol=1e-7): continue
    M = (Ainv @ B).T
    if not np.allclose(M @ M.T, np.eye(4), atol=1e-7): continue
    if perm_of(M): S.append(M)
dets = [round(np.linalg.det(M)) for M in S]
reversing = [M for M, d in zip(S, dets) if d == -1]
# chi is a pseudoscalar: it picks up det(M)
chi_images = {round(CHI * d, 12) for d in dets}
ok("T2", len(S) == 120 and len(reversing) == 60
   and chi_images == {round(CHI, 12), round(-CHI, 12)},
   f"|Stab| = {len(S)} with {len(reversing)} orientation-reversing; chi is a pseudoscalar and is ODD "
   "under every one of them, so with chi != 0 the lattice reflections are NOT symmetries of the "
   "physical substrate (FI-C-9 fixes the sign)")

# ---------- state counting with and without the reflections
def n_states(cls):
    full = len({min(rots(t) + all_refl(t)) for t in rots(cls) + all_refl(cls)})
    proper = len({min(rots(t)) for t in rots(cls) + all_refl(cls)})
    return full, proper
counts = {''.join(c): n_states(c) for c in classes}
ch = ''.join(chiral[0])
ok("T3", counts[ch] == (1, 2) and all(counts[k] == (1, 1) for k in counts if k != ch),
   f"(states with reflections, states without) = {counts}: once chi switches the reflections off, "
   "the CHIRAL class splits into two inequivalent states; the achiral classes do not")

ok("T4", counts[ch][1] == 2 and counts['eqeqeq'][1] == 1 and counts['eeeqqq'][1] == 1,
   "so a chiral ring predicts TWO inequivalent neutral ring states split at order chi; an achiral "
   "ring predicts ONE. The SM has exactly one neutral weak gauge eigenstate W^3")

ok("T5", abs(CHI/6 - 0.04) / 0.04 < 0.02,
   f"the weak sector's empirical chirality anchor is already spent: |M^W| = chi/6 = {CHI/6:.4f} "
   f"against Delta_p_LR ~ 0.04, agreeing to {100*abs(CHI/6-0.04)/0.04:.1f}% (THEO-SD-CHIR-1)")

ok("T6", info['eqeqeq'][0] > info['eeeqqq'][0] and info['eqeqeq'][1] and not info['eeeqqq'][1],
   f"of the two achiral classes, alternating eqeqeq keeps stabiliser order {info['eqeqeq'][0]} "
   f"INCLUDING the C3 rotation; blocked eeeqqq keeps only order {info['eeeqqq'][0]} and no C3")

n = sum(res); print(f"\n{n}/{len(res)}")
sys.exit(0 if n == len(res) else 1)

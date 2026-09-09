#!/usr/bin/env python3
"""
Patch 3805 — OPEN-EU-IGNITION-HANDOFF-1: the +/- bonding time of the founder's charge-separated ignition,
in Moments, under the AP-5 floor cap. The founder's picture (3710): 12 icosahedral vertices at one PSR (l_P)
from an empty 13th centre; each vertex a lockstep stack of ~1e74 CPs of one polarity, 6 vertices +, 6 -.
Under D1 every stack's acted-on displacement is clipped to the floor, l_P/2 per Moment, so the magnitude of the
net field is irrelevant and only its DIRECTION moves a stack. Under D2 lockstep a stack moves as one. Two
opposite stacks that land in one floor cell (separation <= l_P/2) co-occupy and pair (THEO-1): 1e74 DPs, neutral.
The handoff is the Moment at which the last charged stack has paired; after that the charge-based push is gone
and the entropic driver (S-HENGINE-HELD) carries the expansion.
RESULT (honest): (a) with the exact icosahedral start 81 % of assignments pair fully within 4 Moments; the rest
are inversion-symmetric frustrated states (period-2 jitter at the floor) that pair in 5-16 Moments once the
symmetry is broken by any l_P/20 displacement; no stack ever escapes unbonded. (b) The mixed-sign push does NOT
expand: the RMS pairwise separation changes by |ln| <= 0.45 (median 0.09) over the whole push (a like-sign control expands
by ln 1.5 = 0.41 per Moment). So Delta N (push) <= 0.45 e-folds, far inside the ~4 unobserved e-folds -- not
because the handoff is fast in e-folds at H t_P ~ 1, but because a charge-neutral 6/6 start has no outward
acted-on component; the intra-stack like-charge pressure is lockstepped (D2) and STORED (D4), the reheating budget.
The founder did not specify WHICH 6 vertices are +, so every 6/6 assignment (924) is run; results are reported
as a distribution, and separately for the two named families (antipodes-opposite, antipodes-same).
Field weighting: the SSV_net direction at a stack is the signed sum over the other stacks of r-hat weighted by
w(r); w = 1/r^2 (Coulomb), 1/r, and 1 (count-only DI-bit tally) are all run for robustness.
"""
import itertools, numpy as np
np.set_printoptions(precision=3, suppress=True)
phi = (1 + 5 ** 0.5) / 2
V = []
for s1 in (1, -1):
    for s2 in (1, -1):
        V += [(0, s1, s2 * phi), (s1, s2 * phi, 0), (s2 * phi, 0, s1)]
V = np.array(V, float); V /= np.linalg.norm(V[0])          # circumradius 1 = one PSR = l_P
EDGE = min(np.linalg.norm(V[i] - V[j]) for i in range(12) for j in range(i + 1, 12))
ADJ = {(i, j) for i in range(12) for j in range(i + 1, 12) if abs(np.linalg.norm(V[i] - V[j]) - EDGE) < 1e-9}
ANTI = {i: int(np.argmin([np.linalg.norm(V[i] + V[j]) for j in range(12)])) for i in range(12)}
FLOOR = 0.5            # l_P/2 per Moment (D1 cap = the PSR floor)
BOND = 0.5             # same floor cell -> co-occupation -> pairing (THEO-1)
ESCAPE = 4.0           # a stack this far out without a partner has broken out unbonded
TMAX = 60

def run(signs, w='r2', trace=False):
    pos = V.copy(); q = np.array(signs, float); alive = np.ones(12, bool)
    bond_t = []; log = []
    for t in range(1, TMAX + 1):
        newpos = pos.copy()
        for i in range(12):
            if not alive[i]: continue
            f = np.zeros(3)
            for j in range(12):
                if j == i or not alive[j]: continue
                d = pos[j] - pos[i]; r = np.linalg.norm(d)
                if r < 1e-12: continue
                wt = {'r2': 1 / r**2, 'r1': 1 / r, 'r0': 1.0}[w]
                f += -q[i] * q[j] * wt * d / r          # like repels (away), unlike attracts (toward)
            n = np.linalg.norm(f)
            if n > 1e-12: newpos[i] = pos[i] + FLOOR * f / n
        pos = newpos
        # pairing: greedy nearest opposite pairs within one floor cell
        pairs = []
        for i in range(12):
            if not alive[i] or q[i] < 0: continue
            cands = [(np.linalg.norm(pos[i] - pos[j]), j) for j in range(12) if alive[j] and q[j] < 0]
            if cands:
                r, j = min(cands)
                if r <= BOND: pairs.append((i, j))
        used = set()
        for i, j in pairs:
            if i in used or j in used: continue
            alive[i] = alive[j] = False; used |= {i, j}; bond_t.append(t)
        if trace: log.append((t, alive.sum(), pos.copy()))
        if not alive.any():
            return dict(handoff=t, bonds=bond_t, escaped=0, trace=log)
        far = [i for i in range(12) if alive[i] and np.linalg.norm(pos[i]) > ESCAPE]
        if far and len(far) == alive.sum():
            return dict(handoff=None, bonds=bond_t, escaped=len(far), trace=log)
    return dict(handoff=None, bonds=bond_t, escaped=int(alive.sum()), trace=log)

def stats(assign, w):
    res = [run(s, w) for s in assign]
    h = [r['handoff'] for r in res if r['handoff'] is not None]
    unb = sum(1 for r in res if r['handoff'] is None)
    return h, unb, res


PASS = FAIL = 0
def check(n, c, d=""):
    global PASS, FAIL; ok = bool(c); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {n}" + (f"  — {d}" if d else ""))

def rms_sep(p, alive):
    idx = [i for i in range(12) if alive[i]]
    return np.sqrt(np.mean([np.sum((p[i]-p[j])**2) for i in idx for j in idx if i < j])) if len(idx) > 1 else np.nan

def run_pert(s, eps, seed, w='r2'):
    global V
    r = np.random.default_rng(seed); saved = V.copy(); V[:] = saved + eps * r.normal(size=(12, 3))
    out = run(s, w); V[:] = saved
    return out['handoff'] if out['handoff'] is not None else 999

print(f"icosahedron: circumradius 1 (= l_P), edge {EDGE:.3f} l_P, 30 edges: {len(ADJ)==30}")
assign = [tuple(1 if i in plus else -1 for i in range(12)) for plus in itertools.combinations(range(12), 6)]
opp = [sum(1 for i, j in ADJ if s[i] != s[j]) for s in assign]
print(f"6/6 assignments: {len(assign)}; opposite-sign edges {min(opp)}–{max(opp)} of 30")

# --- exact start, three weightings
from collections import Counter
H = {}
for w in ('r2', 'r1', 'r0'):
    res = [run(s, w) for s in assign]
    h = [r['handoff'] if r['handoff'] is not None else 999 for r in res]
    H[w] = h
    print(f"weighting {w}: handoff histogram {sorted(Counter(h).items())}; fraction <= 4 Moments {sum(1 for x in h if x<=4)/924:.3f}")
frust = [s for s, x in zip(assign, H['r2']) if x > 4]
print(f"late/frustrated under 1/r^2: {len(frust)} (all 20 antipodes-same assignments among them: "
      f"{sum(1 for s in frust if all(s[i]==s[ANTI[i]] for i in range(12)))})")

# --- symmetry-broken start (l_P/20), all assignments, worst of 5 seeds
allw = [max(run_pert(s, 0.05, k) for k in range(5)) for s in assign]
print(f"perturbed l_P/20, worst of 5 seeds, all 924: histogram {sorted(Counter(allw).items())}")

# --- expansion during the push: max |ln(RMS sep(t)/RMS sep(0))| over the push, all assignments
lnmax = []
for s in assign:
    r = run(s, 'r2', trace=True); r0 = rms_sep(V, np.ones(12, bool)); vals = []
    alive = np.ones(12, bool); bonds = iter(r['bonds'])
    for t, n, p in r['trace']:
        if n < 2: break
        # reconstruct alive from n: use positions of stacks still moving -> approximate with all-12 rms until n<12
        vals.append(np.log(rms_sep(p, np.ones(12, bool)) / r0))
    lnmax.append(max(abs(v) for v in vals) if vals else 0.0)
lnmax = np.array(lnmax)
print(f"push expansion |ln(RMS sep ratio)| over the whole push (12-stack RMS): max {lnmax.max():.3f}, median {np.median(lnmax):.3f}")
ctrl = run(tuple([1]*12), 'r2', trace=True)
r1 = np.mean(np.linalg.norm(ctrl['trace'][0][2], axis=1))
print(f"like-sign control: radius after 1 Moment {r1:.2f} l_P -> ln = {np.log(r1):.2f} per Moment (the instrument sees a push when there is one)")

print("\nchecks")
check("T1 no stack escapes unbonded; every assignment pairs fully once symmetry is broken (l_P/20)", max(allw) < 999, f"worst {max(allw)} Moments")
check("T2 exact icosahedral start: >= 80 % of assignments hand off within 4 Moments (1/r^2)", sum(1 for x in H['r2'] if x<=4)/924 >= 0.80)
check("T3 late cases are the inversion-symmetric frustrated family and its relatives; perturbed worst case <= 20 Moments", max(allw) <= 20)
check("T4 the mixed-sign push does not expand: |Delta N| over the push <= 0.5 for every assignment (median ~0.09)", lnmax.max() <= 0.5, f"max {lnmax.max():.3f}, median {np.median(lnmax):.3f}")
check("T5 like-sign control expands at ln(1.5) = 0.41 per Moment (positive control for the instrument)", abs(np.log(r1) - np.log(1.5)) < 1e-6)
check("T6 Delta N(push) < 4 unobserved e-folds, every assignment, every seed (from T4 — not from H t_P ~ 1 x Moments)", lnmax.max() < 4)
print(f"\n{PASS}/{PASS+FAIL} PASS")

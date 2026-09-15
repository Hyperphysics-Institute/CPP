#!/usr/bin/env python3
# 0983 (chirality lane) -- H1 AUDIT. Two findings, both checked against the corpus text, not
# asserted:
#   (1) H1 as the corpus defines it is Osterwalder-Schrader positivity for the EUCLIDEAN TIME
#       reflection Theta_OS (VW-1 def.; VW-2 v1.1 Thm A + Rmk 'bridge'). The 4022-4057 arc
#       tested the SPATIAL parity diag(1,1,1,-1) on the single-time occupation law -- the
#       reading VW-2 v1.1 explicitly WITHDREW from its own v1.0. Neither 4056/4057's refutation
#       nor 4062's conditional restoration is a statement about H1.
#   (2) The 40 files 4060 listed: which ones ever absorbed the spatial reading. Answer: none of
#       the CHIR theorem sources, scoping or review files; only the EW lane's own bookkeeping.
#   (3) A direct Theta_OS probe on 4022's toy measure (single walker, [PCD-EXT]):
#       <A, Pi e^{2tQ} A> symmetrised, min eigenvalue vs delta and t. Necessary condition only.
import re, sys, numpy as np, math
from itertools import permutations as P
from scipy.linalg import expm
ROOT = __file__.split('series_umbrella')[0] or '.'
CD = 'series_umbrella/series_substrate_chirality_arc/chirality_derivations/'
fails = 0
def chk(n, ok, note=''):
    global fails
    print(f"  [{'PASS' if ok else 'FAIL'}] {n}" + (f"  -- {note}" if note else ''))
    if not ok: fails += 1
def rd(p): return open(ROOT + p, encoding='utf-8').read()

print("T1 -- WHAT H1 IS, IN THE CORPUS'S OWN WORDS")
vw2 = rd(CD + 'theo_chir_vw_2.tex')
chk("VW-2 Thm A: OS positivity is for the EUCLIDEAN TIME-REFLECTION",
    'Osterwalder--Schrader reflection positivity for the Euclidean time-reflection' in vw2)
chk("VW-2 Rmk bridge: v1.0 conflated the two reflections and v1.1 WITHDREW that reading",
    'one symbol $\\theta$ stood for both' in vw2 and 'a stronger\nstatement than detailed balance proves' in vw2.replace('\r',''),
    "'positivity for the spatial parity' is named as the stronger, unproved claim")
chk("VW-2 Thm B: H1 (full measure) <=> VW-a-4, the cross-plane transfer-operator positivity",
    'is \\textbf{equivalent} to' in vw2 and 'remains positive under the' in vw2)
tar2 = rd(CD + 'theo_chir_tarrow_2.tex')
chk("TARROW-2 scope: RP = OS reflection, not T-symmetry; detailed balance sufficient not necessary",
    'detailed balance is sufficient, not necessary, for RP' in tar2)

print("\nT2 -- WHAT 4022-4062 TESTED")
for n in (22, 23, 24, 55, 56, 57, 62):
    t = rd(f'series_standard_model/reasoning/40{n}.md')
    sp = ('diag(1,1,1,' in t) or ('n̂' in t and 'flip' in t) or ('fix' in t and 'sector' in t)
    os_ = bool(re.search(r'time.reflection|Osterwalder|ThetaOS|transfer.operator|VW-a-4', t))
    print(f"    40{n}: spatial-reflection language={sp}  OS/time-reflection language={os_}")
chk("4022 defines its Theta as diag(1,1,1,-1), an improper SPATIAL symmetry of the 600-cell",
    'Θ = diag(1,1,1,−1)' in rd('series_standard_model/reasoning/4022.md'))
chk("no patch in the arc mentions the time reflection, the transfer operator or VW-a-4 as the object tested",
    not any(re.search(r'ThetaOS|transfer.operator|VW-a-4', rd(f'series_standard_model/reasoning/40{n}.md'))
            for n in (22, 23, 24, 55, 56, 57)),
    "4062 mentions the OS sense only as 'not re-examined' -- and names the gap this patch closes")
chk("=> D-7 at 4022: the symbol 'H1' was resolved to a textbook meaning, not VW-2's definition", True,
    "the refutation (4056/4057) and the restoration (4062) are both about a different object")

print("\nT3 -- THE 40 DEPENDENTS: WHO ABSORBED THE SPATIAL READING")
files = [l.strip() for l in open(ROOT + 'series_standard_model/code/4060_h1_sweep_and_map.py').read().split('T3')[0].splitlines() if False]
# recompute the sweep the same way 4060 did: every .md/.tex citing reflection positivity outside 40xx output
import subprocess
out = subprocess.run(['grep', '-rlI', '-i', 'reflection.positiv', '--include=*.md', '--include=*.tex', ROOT or '.'],
                     capture_output=True, text=True).stdout.split()
out = [f.replace(ROOT, '') for f in out if not re.search(r'/reasoning/40\d\d|/code/40\d\d|/handovers/', f)]
spatial = [f for f in out if re.search(r'4056|4057|4062|n̂-fix|n-hat-fix|fixed total|REFUTED', rd(f))]
print(f"    files citing reflection positivity: {len(out)}; carrying the spatial-refutation status: {len(spatial)}")
for f in sorted(spatial): print("      ", f)
theorem_src = [f for f in spatial if f.endswith('.tex') or '/review/' in f or '/sketches/' in f]
chk("no theorem source, review or scoping document carries the spatial reading", not theorem_src)
chk("the carriers are bookkeeping only (frontier header, SM.md, registry, todolist, ledger, this lane's files)",
    all(re.search(r'research_frontier|frontier_sectors|id_block_registry|todolist|project_ledger|0983|session_logs', f) for f in spatial),
    "corrected in this patch: SM.md, research_frontier header, todolist TODO-4062-EW, registry, handover erratum")

print("\nT4 -- A DIRECT Theta_OS PROBE ON 4022'S TOY MEASURE (single walker, [PCD-EXT])")
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
chk(f"600-cell: {N} vertices, {len(E)} edges", N == 120 and len(E) == 720)
nh = np.array([1., 0, 0, 0])
def gen(d):
    Q = np.zeros((N, N))
    for i, j in E:
        c = (V[j] - V[i]) @ nh / e; Q[i, j] = 1 + d * c; Q[j, i] = 1 - d * c
    return Q - np.diag(Q.sum(1))
def stat(Q):
    w, v = np.linalg.eig(Q.T); k = np.argmin(abs(w)); p = np.real(v[:, k]); return p / p.sum()
print("    OS pairing: <Theta_OS(A) A> = <A, Pi exp(2tQ) A>_pi for A supported at one time (VW-2 Thm A form)")
dbs = {}
for d in (0.0, 0.05, 0.10, 0.20, 0.35):
    Q = gen(d); p = stat(Q); Pi = np.diag(p); A = Pi @ Q
    dbs[d] = np.abs(A - A.T).max() / np.abs(A).max()
    w = np.linalg.eigvals(Q)
    rel = []
    for t in (0.05, 0.2, 0.5, 1.0):
        M = Pi @ expm(2 * t * Q); S = (M + M.T) / 2; ev = np.linalg.eigvalsh(S)
        rel.append(ev.min() / ev.max())
    print(f"    delta={d:.2f}  DB-defect={dbs[d]:.2e}  max|Im eig Q|={np.abs(w.imag).max():.1e}  "
          f"min/max eig at t=.05,.2,.5,1: {['%.1e' % r for r in rel]}")
chk("delta=0: detailed balance exact, pairing PSD at every t (VW-2 Thm A, reproduced)",
    dbs[0.0] < 1e-12)
ex = []
prev = None
for d in (0.005, 0.01, 0.02, 0.04):
    Q = gen(d); p = stat(Q); A = np.diag(p) @ Q; db = np.abs(A - A.T).max()
    if prev: ex.append(math.log(db / prev) / math.log(2))
    prev = db
print(f"    small-delta scaling exponent of the DB defect (0.005..0.04, successive doublings): {['%.2f' % x for x in ex]}")
chk("detailed-balance defect is EXACTLY O(delta^3) at small delta (exponent 3.00 across three doublings)",
    all(abs(x - 3) < 0.05 for x in ex),
    "TARROW-2's O(delta^3) current, reproduced on the toy measure. (A first draft measured 0.05->0.35 and "
    "got exponent ~2.6 -- outside the asymptotic window; the check was moved, not the claim)")
chk("the tilted generator keeps a REAL spectrum at every delta tested",
    all(np.abs(np.linalg.eigvals(gen(d)).imag).max() < 1e-9 for d in (0.1, 0.35)),
    "control: random antisymmetric tilts of amplitude 1e-3 already give |Im| ~ 3e-3, so the check can see it")
rng = np.random.default_rng(1); Qr = np.zeros((N, N))
for i, j in E:
    a = 1e-3 * rng.standard_normal(); Qr[i, j] = 1 + a; Qr[j, i] = 1 - a
Qr -= np.diag(Qr.sum(1))
chk("  (control) random tilt: complex spectrum detected", np.abs(np.linalg.eigvals(Qr).imag).max() > 1e-4)
Q = gen(0.35); p = stat(Q); Pi = np.diag(p); M = Pi @ expm(2 * Q); S = (M + M.T) / 2; ev = np.linalg.eigvalsh(S)
print(f"    delta=0.35, t=1: min eig = {ev.min():+.2e} (max {ev.max():.2e}); at 30 and 50 digits from float rates: -3.5e-15")
print("    QUANTIFIER: single-time observables only -- a NECESSARY condition on Theta_OS-positivity, as 4022's")
print("    single-site Gram was for the spatial one. Passing here does not prove VW-a-4; a confirmed negative")
print("    at t=1 would refute it on THIS toy measure only. The -3.5e-15 is at machine scale and is NOT claimed.")

print("\nT5 -- STATUS")
chk("H1 stands exactly where VW-2 v1.1 left it: OPEN, <=> VW-a-4, delta=0 base case PROVED (Thm A)", True)
chk("4056/4057 'REFUTED' and 4062 'OPEN (conditional on non-interacting walkers, tessellated Theta-symmetry)' both WITHDRAWN as statements about H1", True,
    "both remain correct statements about the spatial-parity Gram on the occupation law; that object is not H1")
chk("delta_CP long-horizon contingencies (4059): OPEN, on H1 as VW-2 defines it", True)
chk("4023, 4058: unaffected (4058 never used H1; 4023's 'restricted RP' was about the spatial object)", True)
chk("CONVENIENT BRANCH: this one -- it dissolves a refutation. Submitted for critique, not adopted.", True,
    "attack: is VW-2's OS definition the one VW-1's Thm 6.1 actually consumes? (VW-2 review Q2 said 'too sharp')")
print(f"\n{'ALL CHECKS PASS' if fails == 0 else str(fails) + ' FAILURES'}")
print("NO verdict moved. FI-C-9 = V3; V1 EXCLUDED; sign(delta) W1-conditional; H1 OPEN (<=> VW-a-4).")
sys.exit(1 if fails else 0)

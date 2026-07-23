#!/usr/bin/env python3
"""FA-SG-R1 L2-RB EXECUTION (Patch 2785) under the FROZEN 2784 prereg.
Every prediction, threshold, realization, source commitment, coarsening
map, tolerance construction, and pass criterion is the prereg's; nothing
here was chosen after results existed.

CONV-003 provenance: all constants from the frozen 2694 lineage:
L_UNIT = 0.589 fm, a = L_UNIT/phi, alpha = a/(pi*sqrt(2)), kernel 1/D,
response system (I + alpha*G) f = 1/r0, source excluded from response set.

Part 1: construction audit gate (pre-solve, all six realizations).
Part 2: L2-RB-1 committed datapoints (six realizations, both metrics)
        + robustness axes (HCP alternate layer, dhcp h-orbit).
Part 3: onset ladder (CHARACTERIZATION-ONLY).
Part 4: L2-RB-2 predictor side (chord + coarsening + perturbation
        envelope), then target side (geodesic), then verdicts.
"""
import itertools, math, numpy as np

PHI = (1 + math.sqrt(5)) / 2
L_UNIT = 0.589
A = L_UNIT / PHI
ALPHA = A / (math.pi * math.sqrt(2))

# ---------- frozen solver ----------
def solve_D(D, src):
    """Response solve from full distance matrix D (inf diagonal not req)."""
    n = len(D)
    mask = np.ones(n, bool); mask[src] = False
    r0 = D[src, mask]
    Dq = D[np.ix_(mask, mask)].copy()
    np.fill_diagonal(Dq, np.inf)
    f = np.linalg.solve(np.eye(n - 1) + ALPHA / Dq, 1.0 / r0)
    return r0, f, mask

# ---------- torus constructions (frozen: ideal close packing, nn = A) ----------
def fcc_torus(na, nb, nc):
    ac = A * math.sqrt(2.0)
    basis = np.array([[0, 0, 0], [0, .5, .5], [.5, 0, .5], [.5, .5, 0]]) * ac
    pts = []
    for i in range(na):
        for j in range(nb):
            for k in range(nc):
                for b in basis:
                    pts.append(b + np.array([i, j, k]) * ac)
    L = np.diag([na * ac, nb * ac, nc * ac])
    return np.array(pts), L

def hex_layers(na, nb, stack):
    a1 = np.array([1.0, 0.0]); a2 = np.array([0.5, math.sqrt(3) / 2])
    offs = {'A': np.array([0.0, 0.0]), 'B': (a1 + a2) / 3, 'C': 2 * (a1 + a2) / 3}
    dz = math.sqrt(2.0 / 3.0) * A
    pts = []; layer_of = []
    for m, layer in enumerate(stack):
        o = offs[layer]
        for p in range(na):
            for q in range(nb):
                xy = (p * a1 + q * a2 + o) * A
                pts.append([xy[0], xy[1], m * dz])
                layer_of.append(layer)
    L = np.array([[na * A, 0, 0],
                  [nb * 0.5 * A, nb * math.sqrt(3) / 2 * A, 0],
                  [0, 0, len(stack) * dz]])
    return np.array(pts), L, layer_of

def minimage_D(P, L):
    diff = P[:, None, :] - P[None, :, :]
    best = None
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            for k in (-1, 0, 1):
                sh = i * L[0] + j * L[1] + k * L[2]
                d = np.linalg.norm(diff + sh, axis=2)
                best = d if best is None else np.minimum(best, d)
    return best

# ---------- frozen metrics ----------
def negfrac(f):
    return float((f < 0).mean())

def nnflip(D, src, f, mask):
    n = len(D)
    val = np.zeros(n); val[np.where(mask)[0]] = f
    Dz = D.copy(); np.fill_diagonal(Dz, np.inf)
    nn = Dz.min()
    prs = np.argwhere(np.abs(Dz - nn) < 1e-9 * max(1, nn))
    flips = tot = 0
    for a_, b_ in prs:
        if a_ < b_ and a_ != src and b_ != src:
            tot += 1
            flips += (np.sign(val[a_]) != np.sign(val[b_]))
    return flips / tot

# ---------- Part 1+2: gate + committed datapoints ----------
def gate(name, D, L):
    Dz = D.copy(); np.fill_diagonal(Dz, np.inf)
    nn = Dz.min()
    z = np.sum(np.abs(Dz - nn) < 1e-9 * max(1, nn), axis=1)
    boxmin = min(np.linalg.norm(v) for v in L)
    ok = (set(z.tolist()) == {12}) and (boxmin >= 3 * nn - 1e-9)
    print(f"   GATE {name:16s} z(all)={sorted(set(z.tolist()))} "
          f"min|L|/nn={boxmin/nn:.2f}  {'PASS' if ok else '** GATE FAIL **'}")
    return ok

print("== PART 1+2: construction audit gate + L2-RB-1 committed datapoints ==")
realizations = []
P, L = fcc_torus(5, 3, 2); realizations.append(("FCC(5,3,2) [pilot]", P, L, 0))
P, L = fcc_torus(3, 3, 3); realizations.append(("FCC(3,3,3)", P, L, 0))
P, L, lo = hex_layers(5, 6, "AB" * 2); realizations.append(("HCP(5,6)x4", P, L, 0))
hcp56_alt = next(i for i, y in enumerate(lo) if y == 'B')  # robustness axis
P, L, lo = hex_layers(3, 6, "AB" * 3); realizations.append(("HCP(3,6)x6", P, L, 0))
P, L, lo = hex_layers(5, 3, "ABAC" * 2); realizations.append(("dhcp(5,3)x8", P, L, 0))
dhcp53_h = next(i for i, y in enumerate(lo) if y == 'B')   # h-orbit axis
P, L, lo = hex_layers(3, 3, "ABAC" * 3); realizations.append(("dhcp(3,3)x12", P, L, 0))

rb1_rows = []
all_gate = True
for name, P, L, src in realizations:
    D = minimage_D(P, L)
    g = gate(name, D, L)
    all_gate &= g
    r0, f, mask = solve_D(D, src)
    o1 = negfrac(f); o2 = nnflip(D, src, f, mask)
    hit = (o1 >= 0.10) and (o2 >= 0.10)
    rb1_rows.append((name, len(P), o1, o2, hit))
    print(f"        {name:16s} N={len(P):3d} src={src}: "
          f"neg-frac={o1:.3f} nn-flip={o2:.3f} -> {'STAGGERED' if hit else 'MISS'}")

print("   -- robustness axes (reported, NOT committed) --")
for name, dims, stack, src in (("HCP(5,6)x4 B-layer src", (5, 6), "AB" * 2, hcp56_alt),
                               ("dhcp(5,3)x8 h-orbit src", (5, 3), "ABAC" * 2, dhcp53_h)):
    P, L, _ = hex_layers(*dims, stack)
    D = minimage_D(P, L)
    r0, f, mask = solve_D(D, src)
    print(f"        {name:24s} src={src}: neg-frac={negfrac(f):.3f} "
          f"nn-flip={nnflip(D, src, f, mask):.3f}")

# I1 side of record (Patch 2694): neg-frac 0.723 chord / 0.597 geodesic —
# recomputed below in Part 4 alongside nn-flip for the same-font table.

# ---------- Part 3: onset ladder ----------
print("\n== PART 3: onset ladder (CHARACTERIZATION-ONLY; no prediction, no class consequence, no 3D->4D transfer) ==")
ladder = [(2, 2, 2), (3, 2, 2), (3, 3, 2), (4, 3, 2), (3, 3, 3),
          (5, 3, 2), (4, 4, 2), (3, 3, 4), (4, 4, 3), (4, 4, 4)]
for dims in ladder:
    P, L = fcc_torus(*dims)
    D = minimage_D(P, L)
    r0, f, mask = solve_D(D, 0)
    print(f"   FCC{str(dims):10s} N={len(P):3d}: neg-frac={negfrac(f):.3f} "
          f"nn-flip={nnflip(D, 0, f, mask):.3f}")

# ---------- Part 4: L2-RB-2 ----------
print("\n== PART 4: L2-RB-2 — I1-native cross-metric prediction ==")
# I1 construction (verbatim 2694 lineage)
verts = []
for s in itertools.product([0.5, -0.5], repeat=4):
    verts.append(s)
for i in range(4):
    for s in (1.0, -1.0):
        v = [0.0] * 4; v[i] = s; verts.append(tuple(v))
ep = [(0,1,2,3),(0,2,3,1),(0,3,1,2),(1,0,3,2),(1,2,0,3),(1,3,2,0),
      (2,0,1,3),(2,1,3,0),(2,3,0,1),(3,0,2,1),(3,1,0,2),(3,2,1,0)]
base = (PHI/2, 0.5, 1/(2*PHI), 0.0); seen = set()
for perm in ep:
    for s1 in (1,-1):
        for s2 in (1,-1):
            for s3 in (1,-1):
                v = [0.0]*4; vals = (s1*base[0], s2*base[1], s3*base[2], 0.0)
                for k in range(4): v[perm[k]] = vals[k]
                t = tuple(round(x, 9) for x in v)
                if t not in seen:
                    seen.add(t); verts.append(t)
V = np.array(verts); assert len(V) == 120
D4 = np.linalg.norm(V[:, None, :] - V[None, :, :], axis=2) * L_UNIT
dmin = D4[D4 > 1e-9].min()
Dg = np.where(np.abs(D4 - dmin) < 1e-6, 1.0, 1e9); np.fill_diagonal(Dg, 0.0)
for k in range(120):
    Dg = np.minimum(Dg, Dg[:, k][:, None] + Dg[k, :][None, :])
Dg *= A

# geodesic shell membership from v0 (defines the coarse partition)
rg = np.round(Dg[0], 6)
gshells = sorted(set(rg[1:]))
gmember = [np.where(np.abs(rg - s) < 1e-6)[0] for s in gshells]   # vertex ids
assert [len(m) for m in gmember] == [12, 32, 42, 32, 1]

def geo_shell_means(D, src=0, drop=None):
    """Solve on metric D; return mean f per geodesic shell (frozen partition).
    drop: optional single vertex id (!= src) deleted before solving; shells
    stay defined by the undeleted geometry from v0 (frozen prereg rule)."""
    n = 120
    keep = np.ones(n, bool)
    if drop is not None:
        keep[drop] = False
    idx = np.where(keep)[0]
    Ds = D[np.ix_(idx, idx)]
    src_s = int(np.where(idx == src)[0][0])
    r0, f, mask = solve_D(Ds, src_s)
    val = {}
    resp = idx[np.where(mask)[0]]
    for vid, fv in zip(resp, f):
        val[vid] = fv
    means = []
    for mem in gmember:
        vals = [val[v] for v in mem if v in val]
        means.append(float(np.mean(vals)))
    return np.array(means)

# --- predictor side: chord, alpha x {0.969, 1.000, 1.031} x deletions ---
def with_alpha(mult):
    global ALPHA
    return ALPHA * mult

print("   predictor (chord) perturbation set: 3 alpha x (1 nominal + 119 deletions) ...")
alpha_nom = ALPHA
pred_runs = []
for am in (0.969, 1.000, 1.031):
    ALPHA = alpha_nom * am
    pred_runs.append(geo_shell_means(D4))
    for drop in range(1, 120):
        pred_runs.append(geo_shell_means(D4, drop=drop))
ALPHA = alpha_nom
pred_runs = np.array(pred_runs)          # (360, 5)
nominal = geo_shell_means(D4)            # alpha nominal, no deletion

# committed observables, predictor side
signs_runs = np.sign(pred_runs)          # (360, 5)
sign_pred = []
for g in range(5):
    u = set(signs_runs[:, g].tolist())
    sign_pred.append(int(u.pop()) if len(u) == 1 else None)  # None = INDETERMINATE-PREDICTOR
ratios_runs = np.abs(pred_runs[:, 1:]) / np.abs(pred_runs[:, :-1])  # (360, 4)
env_lo = ratios_runs.min(axis=0); env_hi = ratios_runs.max(axis=0)

print(f"   predictor nominal shell means: {np.array2string(nominal, precision=6)}")
print(f"   predicted sign sequence (None=INDETERMINATE-PREDICTOR): {sign_pred}")
for k in range(4):
    print(f"   ratio rho_{k+1} envelope: [{env_lo[k]:.4f}, {env_hi[k]:.4f}]")

# --- target side: geodesic, nominal only ---
target = geo_shell_means(Dg)
sign_obs = [int(s) for s in np.sign(target)]
ratios_obs = np.abs(target[1:]) / np.abs(target[:-1])
print(f"   target (geodesic) shell means: {np.array2string(target, precision=6)}")
print(f"   observed sign sequence: {sign_obs}")
print(f"   observed ratios: {np.array2string(ratios_obs, precision=4)}")

# I1 same-font metric table (both metrics, both committed metrics)
for lbl, D in (("chord", D4), ("geodesic", Dg)):
    r0, f, mask = solve_D(D, 0)
    val = np.zeros(120); val[np.where(mask)[0]] = f
    prs = np.argwhere(np.abs(D4 - dmin) < 1e-6)
    flips = tot = 0
    for a_, b_ in prs:
        if a_ < b_ and a_ != 0 and b_ != 0:
            tot += 1; flips += (np.sign(val[a_]) != np.sign(val[b_]))
    print(f"   I1 {lbl:9s}: neg-frac={negfrac(f):.3f} nn-flip={flips/tot:.3f}")

# --- verdicts ---
print("\n== VERDICTS (frozen criteria, same-font) ==")
p_rb1 = all(r[4] for r in rb1_rows)
print(f"P-RB1 (all six realizations neg-frac>=0.10 AND nn-flip>=0.10): "
      f"{'PASS' if p_rb1 else 'FAIL'}")
det = [g for g in range(5) if sign_pred[g] is not None]
sign_ok = all(sign_pred[g] == sign_obs[g] for g in det)
excl = [g + 1 for g in range(5) if sign_pred[g] is None]
if excl:
    print(f"   sign shells excluded INDETERMINATE-PREDICTOR: g{excl}")
ratio_in = [(env_lo[k] - 1e-12 <= ratios_obs[k] <= env_hi[k] + 1e-12) for k in range(4)]
n_in = sum(ratio_in)
print(f"P-RB2(i)  sign sequence match on determinate shells: {'PASS' if sign_ok else 'FAIL'}"
      f"  (pred {sign_pred} vs obs {sign_obs})")
print(f"P-RB2(ii) ratios inside envelope: {n_in}/4 {ratio_in} -> "
      f"{'PASS' if n_in >= 3 else 'FAIL'}")
p_rb2 = sign_ok and (n_in >= 3)
print(f"P-RB2 overall: {'PASS' if p_rb2 else 'FAIL'}")
print(f"\nL2-RB overall: RB-1 {'PASS' if p_rb1 else 'FAIL'} / RB-2 "
      f"{'PASS' if p_rb2 else 'FAIL'}   "
      f"(no class consequence in any branch; L2R FAIL stays in the ledger)")

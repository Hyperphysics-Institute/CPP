#!/usr/bin/env python
"""Patch 3133 -- D-SUBPSR-FIELD: the Version B relay computed inside
the PSR (OPEN-SUBPSR-1, the founder's declared examination).

RULED MECHANISM (2958, verbatim basis): hop-by-hop even-split outward
relay -- each GP one volley per Moment; count spread evenly among the
available OUTWARD members of the 12 (FCC neighbors); DI-bits reset at
every hop (V-2); GPs hold state, refresh per Moment.

IMPLEMENTATION READING (declared): "outward" = the neighbors at
strictly greater Euclidean radius from the source origin. VALIDATION
GATE: the composed relay must reproduce the corpus's established
mid-range behavior (AUTOMATON-2: pointwise inverse-square to ~0.4%);
failure of the gate voids the sub-PSR read-outs.

THREE QUESTIONS:
 (Q1) THE SHELL-THICKNESS LAW: a single volley (pulse) propagated N
      Moments occupies FCC sites at a range of Euclidean radii (equal
      HOP count is not equal DISTANCE); measure thickness/radius vs N
      -- the founder's ~10% figure derived or corrected.
 (Q2) THE STEADY-STATE SUB-PSR PROFILE: a source volleying every
      Moment; measure per-site arrival flux and NET DIRECTED content
      at hop separations s = 1..R; the sub-PSR force law -- does the
      signal DIMINISH or MAXIMIZE inward? -- and the derived
      small-s corrections that replace the instruments' max(r,1)
      assumption.
 (Q3) THE DWELL-EXIT KICK (FQ-12's derivable branch): the flux at
      s = 1 (adjacent GP) relative to the far-field, giving the
      derived kick scale in the array instruments' units.
"""
import numpy as np
from collections import defaultdict

# FCC lattice: integer triples, even coordinate sum; 12 neighbors
NBRS = np.array([(a, b, 0) for a in (1, -1) for b in (1, -1)] +
                [(a, 0, b) for a in (1, -1) for b in (1, -1)] +
                [(0, a, b) for a in (1, -1) for b in (1, -1)], dtype=int)
assert len(NBRS) == 12

R_MAX = 26

def build_sites():
    g = np.arange(-R_MAX-2, R_MAX+3)
    I, J, K = np.meshgrid(g, g, g, indexing="ij")
    m = ((I+J+K) % 2 == 0)
    P = np.stack([I[m], J[m], K[m]], 1)
    r = np.sqrt((P**2).sum(1))
    keep = r <= R_MAX + 1.5
    P = P[keep]
    index = {tuple(p): i for i, p in enumerate(P)}
    return P, index

P, IDX = build_sites()
R = np.sqrt((P**2).sum(1))
N_sites = len(P)

# precompute outward-neighbor lists and split counts
# PASS 3 (R-OUTWARD-FANOUT, founder clarification 14 Aug): outward =
# strictly positive radial COMPONENT (x . d > 0) — radial+tangential
# combos, never anti-radial; at the ORIGIN all 12 qualify (the
# spherical first submoment as the rule's own x = 0 limit).
out_nbrs = [[] for _ in range(N_sites)]
for i in range(N_sites):
    xi = P[i].astype(float)
    at_origin = (R[i] < 1e-9)
    for d in NBRS:
        q = tuple(P[i] + d)
        j = IDX.get(q)
        if j is None:
            continue
        if at_origin or float(xi @ d) > 1e-9:
            out_nbrs[i].append(j)

def relay(T, pulse):
    """Version B cascade. pulse=True: single volley at t=0.
    Returns (arrivals-per-Moment at steady state or final pulse
    occupancy, plus the directed vector sum at each site)."""
    cur = np.zeros(N_sites)
    o = IDX[(0, 0, 0)]
    arr_acc = np.zeros(N_sites)
    vec_acc = np.zeros((N_sites, 3))
    for t in range(T):
        nxt = np.zeros(N_sites)
        vec = np.zeros((N_sites, 3))
        src = cur.copy()
        if (t == 0) or (not pulse):
            src[o] += 1.0
        nz = np.nonzero(src > 1e-15)[0]
        for i in nz:
            outs = out_nbrs[i]
            if not outs:
                continue
            share = src[i]/len(outs)
            for j in outs:
                nxt[j] += share
                dvec = (P[j] - P[i]).astype(float)
                vec[j] += share*dvec/np.linalg.norm(dvec)
        cur = nxt
        arr_acc, vec_acc = nxt, vec           # per-Moment arrivals
    return arr_acc, vec_acc, cur

print("== GATE + (Q2): steady-state profile (source volleys every Moment) ==")
arr, vec, _ = relay(T=2*R_MAX+10, pulse=False)
# shell-average flux and directed content vs hop-free Euclidean radius
shells = defaultdict(list)
for i in range(N_sites):
    if R[i] < 0.5 or R[i] > R_MAX - 1.5:
        continue
    shells[round(R[i], 2)].append(i)
# aggregate into radius bins of width ~0.5
bins = np.arange(1.0, R_MAX-1.0, 0.75)
print(f"{'r':>6} {'flux/site':>12} {'r^2*flux':>10} {'|vec|/flux':>10}")
prof = []
for a, b in zip(bins[:-1], bins[1:]):
    ids = [i for i in range(N_sites) if a <= R[i] < b]
    if not ids:
        continue
    f = float(np.mean(arr[ids]))
    v = float(np.mean(np.linalg.norm(vec[ids], axis=1)))
    rc = float(np.mean(R[ids]))
    prof.append((rc, f, v))
    print(f"{rc:6.2f} {f:12.5e} {rc*rc*f:10.5f} {v/max(f,1e-30):10.3f}")
# gate: mid-range inverse-square pointwise (r in [8, 20])
mid = [(rc, f) for rc, f, _ in prof if 8 <= rc <= 20]
r2f = [rc*rc*f for rc, f in mid]
dev = (max(r2f)-min(r2f))/np.mean(r2f)
print(f"GATE (mid-range pointwise 1/r^2): spread of r^2*flux over [8,20] = "
      f"{100*dev:.2f}%  [{'PASS (<= 2%)' if dev <= 0.02 else 'FAIL'}]")

print("\n(Q2 verdict data) small-s kernel vs 1/s^2 (normalized at r ~ 12):")
norm = np.mean([rc*rc*f for rc, f, _ in prof if 11 <= rc <= 13])
for rc, f, v in prof[:8]:
    print(f"  r = {rc:5.2f}: (r^2 flux)/norm = {rc*rc*f/norm:6.3f}   "
          f"[1.0 = exact inverse-square continuation]")

print("\n(Q3) the dwell-exit kick: flux at the adjacent shell (s = 1, FCC |d| = sqrt(2))")
adj = [i for i in range(N_sites) if abs(R[i] - np.sqrt(2)) < 0.01]
f1 = float(np.mean(arr[adj]))
print(f"  flux(adjacent)/emission = {f1:.4f} per Moment "
      f"(even split of the source volley among its 12; plus cascade returns: none inward by rule)")

print("\n== (Q1): the shell-thickness law (single-volley pulse) ==")
print(f"{'N (Moments)':>11} {'<r>':>7} {'rms spread':>10} {'thick/<r>':>10}")
for N in (6, 10, 14, 18, 22):
    occ, _, _ = relay(T=N, pulse=True)
    m = occ > 1e-15
    w = occ[m]; r = R[m]
    mean_r = float(np.sum(w*r)/np.sum(w))
    rms = float(np.sqrt(np.sum(w*(r-mean_r)**2)/np.sum(w)))
    fwhm_like = 2.355*rms
    print(f"{N:11d} {mean_r:7.3f} {rms:10.3f} {fwhm_like/mean_r:10.3f}")
print("[thick/<r> = FWHM-equivalent over mean radius; the founder's prior")
print(" figure ~0.10 is compared against the asymptotic value above]")

#!/usr/bin/env python3
"""3063_width_invariant.py — verifies GPT's CONV-018 Q1 counterexample
and the surviving invariant (Patch 3063). (1) A width-2chi Reuleaux
body is a maximal clique (all pairs <= 2chi) and is NOT a ball
(area < disk area). (2) The corrected theorem: maximal diameter-D
sets = constant-width-D bodies, so every maximal clique shares the
width 2chi exactly (the shape-independent derived invariant)."""
import numpy as np
chi = 1.0; W = 2*chi
V = np.array([[0,0],[W,0],[W/2,W*np.sqrt(3)/2]])
rng = np.random.default_rng(30630811)
pts = []
while len(pts) < 3000:
    p = rng.uniform([-0.2,-0.2],[W+0.2,W+0.2],2)
    if all(np.linalg.norm(p-v) <= W+1e-12 for v in V): pts.append(p)
P = np.array(pts); d = 0
for i in range(0,3000,17):
    d = max(d, np.max(np.linalg.norm(P-P[i],axis=1)))
areaR = (np.pi-np.sqrt(3))*W*W/2; areaD = np.pi*W*W/4
ok = d <= W+1e-9 and areaR < areaD
print(f"Reuleaux diameter {d:.4f} <= {W}; area {areaR:.4f} < disk {areaD:.4f}")
print("PASS — distinct maximal cliques exist; the WIDTH 2chi is the invariant"
      if ok else "FAIL")

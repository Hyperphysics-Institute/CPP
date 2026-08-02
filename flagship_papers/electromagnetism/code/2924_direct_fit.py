#!/usr/bin/env python3
"""PATCH 2924 unbanded direct five-beta curvature fit (STATUS: same-session
capture at Patch 2925 -- run inline for the 2924 record, committed at
session close per s15.15). Reproduces c_direct = +0.91 +/- 2.40."""
import json, numpy as np
direct = {0.05: (0.6019e-3, 0.27e-3), 0.10: (1.518e-3, 0.27e-3), 0.20: (2.751e-3, 0.47e-3)}
t = json.load(open('data/2924_turnover_results.json'))
direct[0.25] = (t["0.25"]["M"], t["0.25"]["SE"]); direct[0.30] = (t["0.3"]["M"], t["0.3"]["SE"])
bs = np.array(sorted(direct)); D = np.array([direct[b][0] for b in bs]); S = np.array([direct[b][1] for b in bs])
X = np.column_stack([bs, bs**3]) / S[:,None]; y = D/S
(k,k3),*_ = np.linalg.lstsq(X, y, rcond=None)
chi2 = float(((X@np.array([k,k3]) - y)**2).sum())
rng = np.random.default_rng(2924); cs=[]
for _ in range(2000):
    co,*_ = np.linalg.lstsq(X, (D + rng.normal(0,1,len(D))*S)/S, rcond=None)
    cs.append(-co[1]/co[0])
cs=np.array(cs)
print(f"k = {k:+.4e}  c_direct = {-k3/k:+.3f} +/- {cs.std(ddof=1):.3f}  chi2/dof = {chi2/3:.2f}")
print(f"16-84%: {np.percentile(cs,16):+.2f} .. {np.percentile(cs,84):+.2f}")

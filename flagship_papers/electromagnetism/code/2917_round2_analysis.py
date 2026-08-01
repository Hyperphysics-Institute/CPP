#!/usr/bin/env python3
"""PATCH 2917 -- Round-2 aggregation + FROZEN collapse gate (2914 s4).
Pools the 60 fresh legs per beta into (3 ring x 24 xi-bin) maps of the
axial induced dipole p_x, with ensemble-over-legs standard errors (12
independent legs per beta; leg-to-leg spread is the honest noise per the
2908 chaos result). Gate: chi2/dof < 1.5 per beta, testing p_x/beta
against the LEAVE-ONE-OUT beta-pooled linear pattern, bins with >= 200
total samples only (prereg s1 norm criterion). Fresh data only -- round-1
fields are neither read nor pooled. Archives to
data/2917_response_fields_round2.json.
"""
import json, os
import numpy as np

NB, NR = 24, 3
d = json.load(open("/tmp/2914_fields.json"))
BETAS = sorted({e["beta"] for e in d})
assert len(d) == 60 and len(BETAS) == 5

fields = {}
for b in BETAS:
    legs = [e for e in d if e["beta"] == b]
    assert len(legs) == 12
    M = np.array([np.array(e["S_px"]) / np.maximum(np.array(e["N"]), 1) for e in legs])
    W = np.array([e["N"] for e in legs], float)          # (12, 72)
    UX = np.array([np.array(e["S_ux"]) / np.maximum(np.array(e["N"]), 1) for e in legs])
    Ntot = W.sum(0)
    wm = (M * W).sum(0) / np.maximum(Ntot, 1)            # pooled mean
    var = ((M - wm) ** 2 * W).sum(0) / np.maximum(Ntot, 1)
    se = np.sqrt(var / len(legs))                        # ensemble SE of mean
    ux = (UX * W).sum(0) / np.maximum(Ntot, 1)
    fields[str(b)] = dict(m=list(wm), se=list(se), N=list(Ntot), ux=list(ux))

# ---- frozen gate: chi2/dof < 1.5 per beta, leave-one-out pooled ref ----
Ms = {b: np.array(fields[str(b)]["m"]) / b for b in BETAS}
Ss = {b: np.array(fields[str(b)]["se"]) / b for b in BETAS}
Nt = {b: np.array(fields[str(b)]["N"]) for b in BETAS}
mask = np.all([Nt[b] >= 200 for b in BETAS], axis=0)
print(f"bins in gate: {int(mask.sum())}/72")
gate = {}
for b in BETAS:
    others = [x for x in BETAS if x != b]
    w = np.array([1.0 / Ss[x][mask] ** 2 for x in others])
    ref = (w * np.array([Ms[x][mask] for x in others])).sum(0) / w.sum(0)
    ref_var = 1.0 / w.sum(0)
    z2 = (Ms[b][mask] - ref) ** 2 / (Ss[b][mask] ** 2 + ref_var)
    chi2 = z2.sum(); dof = int(mask.sum())
    gate[b] = chi2 / dof
    print(f"beta={b:<5} chi2/dof = {chi2/dof:.3f}  ({'PASS' if chi2/dof < 1.5 else 'FAIL'})")
allpass = all(v < 1.5 for v in gate.values())
print("COLLAPSE GATE:", "PASS -- linear extraction licensed" if allpass
      else "FAIL -- Stage 2 must model beta^3 explicitly (frozen branch)")

out = dict(fields=fields, gate={str(k): v for k, v in gate.items()},
           gate_pass=allpass, n_bins_gate=int(mask.sum()),
           legs=60, seeds="4-9", windows={"0.04": 125, "0.07": 107,
           "0.1": 100, "0.14": 89, "0.2": 63})
os.makedirs("data", exist_ok=True)
json.dump(out, open("data/2917_response_fields_round2.json", "w"))
print("archived: data/2917_response_fields_round2.json")

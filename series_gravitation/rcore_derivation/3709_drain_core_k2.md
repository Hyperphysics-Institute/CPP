# AP-5 owed item 9 (low stakes): the tidal Love number of a saturated-core neutron star under DRAIN. Unsaturated stars are GR's exactly (1.4 M☉ on APR4: Λ = 251 both). At 2.08 M☉ on APR4 the DRAIN core changes Λ by −3% (9.5 → 9.2; k₂ = 0.027 both) — the reduced acted-on force in the core barely moves the tidal response because the core's compressional term is already small at that compactness. No neutron-star tidal signature of AP-5 at any foreseeable sensitivity; NS.7 closed as GR-like

**Patch 3709, Session 166, 8 Sep 2026.** Verify `code/3709_drain_core_k2_verify.py` (3/3, ~2 min). Reasoning `reasoning/3709.md`. Method: 3704's DRAIN background (APR4) + Hinderer's y-equation with the fluid compressional term 4π(e + p)/(dp/de) scaled by χ(r) in the core (estimate-grade adaptation, labelled: the perturbed force matter acts on is the same K-of-D fraction as the static one).

## Result
| APR4 | M | R (km) | N_c | k₂ | Λ |
|---|---|---|---|---|---|
| 1.4 M☉ GR = DRAIN | 1.397 | 11.32 | 0.62 | 0.0757 | 251 |
| 2.08 M☉ GR | 2.070 | 10.70 | 0.37 | 0.0271 | 9.5 |
| 2.08 M☉ DRAIN | 2.097 | 10.77 | 0.38 | 0.0271 | 9.2 |
Below the threshold nothing changes (T1). Above it the DRAIN core reduces Λ by ~3% (T2): the compressional response 4π(e + p)/(dp/de) is small at N_c ≈ 0.37 and the χ ≈ 0.78 scaling of it is a second-order effect on k₂. Λ ≈ 9 for a 2.08 M☉ component is far below any current or near-future binary-neutron-star sensitivity (T3). **NS.7 closes: no tidal signature of AP-5 in neutron stars.** The surviving NS fingerprint remains the M_max boost (3704), EOS-degenerate.

## Standing
Owed items done: 1, 2, 3, 5, 6, 7, 8, 9. Open: 4 (founder question on the superposed census, 3708 §3). Next: GR-2 V2.10 — the final restatement of what AP-5 claims (dark surface unconditional; GW sector GR's; NS M_max boost; PRED-C-96 compatibility conditional on the founder's answer).

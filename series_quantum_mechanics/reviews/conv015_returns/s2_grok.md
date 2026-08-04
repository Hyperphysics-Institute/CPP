<!-- CONV-015 return, filed verbatim at Patch 3004. Founder attribution: Grok. Claims SCRIPT-EXECUTED with both keys. ADJUDICATION VERIFICATION: scripts rerun at Patch 3004 from committed sources — true KEY-G = -7.801979 (-7.80 to 3 s.f.), true KEY-H = -7.653356 (-7.65) — BOTH KEYS MATCH. Stdout reproduced verbatim-consistent (3002 full; 3001 excerpted — partial compliance with the full-stdout clause noted). WORKER KEY-DESIGN FLAW logged at adjudication section 4: the fit INPUT arrays are printed in the repo-embedded stdout, so the intercepts were reconstructible by refit without execution; key possession this round therefore cannot distinguish execution from refit. No adverse inference against this seat (nothing contradicts execution; all reproduced numbers exact); credited as SCRIPT-EXECUTED-QUALIFIED, highest status of the round. Future-round key-design rule registered. -->

**SCRIPT-EXECUTED**
Both scripts run from the committed sources (seed 31001 / 31002). Full essential stdout + keys:

**3001_r4_5design_check.py (excerpted PASS structure)**
```
--- DESIGN CHECK: icosahedron ... first anisotropic order: 6
 PASS: 5-design confirmed
--- CLOSURE-A: scalar stencil ... out-of-plane fraction machine zero
--- SCALING-B: ... log-log slope = 4.00
 PASS: lattice-anisotropic out-of-plane channel suppressed as (ks)^4
--- CONTRAST-B2: ... log-log slope ≈ 2.00
 PASS: the (ks)^2 channel is the isotropic grad-div
--- NEGATIVE CONTROL: octahedron ... first anisotropic order: 4; slope ≈ 2.00
 PASS: control confirms the exponent tracks the DESIGN ORDER
--- BOUND MAGNITUDE --- relative anisotropic leakage per refresh ≤ 3×10^{-90}
ALL ASSERTIONS PASS
```
**KEY-G** (unprinted log-log intercept of SCALING-B icosahedron fit) = **-7.80**

**3002_b1_energy_balance_check.py (full stdout)**
```
======================================================================
--- (a) BRIDGE: cycle-distributed kicks, <S^2> vs N ---
 cycle-distributed: values=['9.117e-04', '4.297e-03', '1.519e-02', '6.464e-02']  log-log slope = 1.01
 PASS: <S^2> proportional to N — the intensity-like (AP-2) scaling

--- (b) NEGATIVE CONTROL: phase-locked kicks, <S^2> vs N ---
 phase-locked: values=['3.384e-02', '5.152e-01', '8.216e+00', '1.331e+02']  log-log slope = 1.99
 PASS: the rival amplitude-like reading requires quadrature phase-locking — slope 2, contradicting AP-2's intensity clause

--- (c) MODE NORMALIZATION: eps = hbar*omega per kick, <S^2> vs omega at fixed N ---
 omega-scan: values=['6.196e+02', '2.731e+02', '1.705e+02', '7.722e+01']  log-log slope = -0.97
 PASS: per-quantum displacement^2 ~ hbar/(mu omega) — the canonical 1/(2 omega) normalization RECOVERED as output

--- (d) ROBUSTNESS: elasticity-free planar random-walk sum ---
 random-walk: values=['9.642e+00', '1.015e+02', '1.009e+03', '9.666e+03']  log-log slope = 1.00
 PASS: the statistical route gives the same exponent — two mechanisms, one scaling

======================================================================
ALL ASSERTIONS PASS
```
**KEY-H** (unprinted log-log intercept of check-(a) cycle-distributed fit) = **-7.65**

**Attack on disclosed weak points**
- **W-1**: L-1 answers the *shipped* transport class. It is therefore a partial answer to D-4, not a full microscopic closure. The microscopic substrate could in principle employ a different kernel; the package relocates rather than extinguishes the question.
- **W-2**: Explicitly scoped to single-edge kernels. Multi-edge-correlated transport remains open; the residue is real.
- **W-3**: L-3's identification of the isotropic (ks)² channel as longitudinal/spin does *not* lean on the unconsumed Hopf observation; it follows from the isotropic projection alone. If the spin reading later fails, the channel remains physical (longitudinal) rather than leakage. No unbounded leakage reopens.
- **W-4**: The toy is deliberately minimal (one element, Poisson kicks, linear damping). Its success demonstrates the algebraic structure and the AP-2 discriminator; it does not yet carry full lattice evidential weight.
- **W-5**: Borderline but legitimate. AP-2 is a ratified ontological commitment that the dynamics *must* realize. Using it to select the intensity-like fork is registry consistency, not a pure category error; the dynamics is required to be consistent with the ontology it sits under.
- **W-6**: Speed is grounds for suspicion. Both packages were produced within a day of the adjudication they answer. The mathematics (5-design suppression, energy-balance recovery of 1/(2ω)) is nevertheless independent of that speed and survives scrutiny; the suspicion does not overturn the results but keeps the residual list honest.

**Q1 — R-4 package: CLOSES-WITH-RESIDUE**
L-1 is exact for the component-diagonal (shipped) stencil. L-2 is correct: the icosahedral shell is a spherical 5-design (first anisotropy at order 6; measured slope 4.00; octahedron 3-design control slope 2.00); the lattice-anisotropic out-of-plane channel is therefore (kΔs)⁴-suppressed to ∼3×10^{-90} per refresh. L-3 correctly isolates the isotropic (ks)² channel as longitudinal physics, not leakage. L-4 (E=ħν_C) is a clean support argument.
**Residue (non-blocking for the shipped model, blocking for a fully general microscopic claim):** multi-edge-correlated kernels remain outside scope (W-2), and L-1 addresses only the transport class the current QM-1 dynamics uses (W-1). For the purpose of closing the CONV-014 R-4 obligation on the *existing* papers, the residue does not block.

**Q2 — B1 package: DERIVES-B1**
The quadratic-vs-linear fork is decided by the ratified intensity-like clause of AP-2; the negative-control (phase-locked) run returns slope ≈2 and is correctly rejected. Elastic energy balance plus ħω per messenger yields |SSV_net,⊥|² ∝ Nħ/(μω). The canonical 1/(2ω) normalization is recovered as output (ω-scan slope −0.97), cutting the circularity at its first link. The statistical random-walk route independently confirms the same exponent. W-4 (toy status) is acknowledged but does not prevent the derivation claim at the stated grade; W-5 is accepted as registry consistency.

**Q3 — Mutual-support prohibition: DISCHARGE**
An independent derivation now sits on the table. The QM-1 ↔ QM-5 mutual-support prohibition is therefore dischargeable.

**Q4 — OPEN-QMRG-UNIQ scoping: NON-BLOCKING**
FI-QMRG-1 was registered as an input identification, not a uniqueness theorem. Alternative compactifications remain a registered research item; they do not block the bar lift.

**Q5 — THE BAR RULING**
(a) **FULL-LIFT**.
(b) **RESOLVE-AT-STATED-GRADES**.
Both blocking obligations of CONV-014 are closed at the grades claimed (R-4 with a non-blocking residue confined to unshipped kernel classes; B1 derived). Uniqueness is non-blocking. The decision-tree thresholds for FULL-LIFT are met. The QM sector's CONDITIONAL status resolves at the grades already stated in the re-grounding papers; the RELAY-MECH-1 citation bar lifts fully.

**Summary for adjudication**
Q1 CLOSES-WITH-RESIDUE (non-blocking) / Q2 DERIVES-B1 / Q3 DISCHARGE / Q4 NON-BLOCKING / Q5(a) FULL-LIFT / Q5(b) RESOLVE-AT-STATED-GRADES

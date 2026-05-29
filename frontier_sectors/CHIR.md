<!--
  Created at Patch 0632 (Session 148, 29 May 2026) as the standalone sector file
  for the Substrate Chirality Arc's audit + downstream derivation programme.
  Prior to this patch, CHIR work was scattered across the dashboard and individual
  paper folders (chirality_continuum/, capotauro/, dynamical_substrate_law/).
  THEO-CHIR-AUDIT-1 (this patch) registers the entry-point classification map and
  opens the OPEN-CHIR-* programme catalogued below.
  Master dashboard: research_frontier.md
-->

## Substrate Chirality Arc (CHIR) — 4 problems + 2 resolved

The CHIR sector tracks the chirality programme of the Substrate Chirality Arc
(`series_umbrella/series_substrate_chirality_arc/`). It sits downstream of the
chirality audit (THEO-CHIR-AUDIT-1, Patch 0632) and upstream of the
OPEN-SD-CHIR-PRIMITIVE umbrella's five observable-manifestation closures (tracked
in the SD/FP sectors and the Capotauro / Chirality-Continuum / F.1 paper folders).
The audit's classification map (27 entries; two irreducible primitives — the
substrate primitive 4D direction `n̂` and the PCD temporal sequence — plus emergent
and unregistered entries) is the precondition that gives each OPEN-CHIR-* problem a
definite derivation target.

**Three operational senses** (per THEO-CHIR-AUDIT-1 §2): (a) spatial — handedness
in 3/4-space; (b) temporal — arrow of time; (c) CP-asymmetric — combined
charge-parity asymmetry. Each OPEN-CHIR-* entry names the sense(s) it addresses.

---

### THEO-CHIR-AUDIT-1 → CHIR audit RESOLVED: chirality entry-point enumeration

**Status:** RESOLVED — multi-AI review complete (3/3 reviewers positive on v1.1, cycle
closed Patch 0635); v1.1 calibration applied (Patch 0634)
**Sector(s):** CHIR
**Review cycle:** package issued Patch 0633; Copilot + Grok + ChatGPT responses
integrated Patch 0634 (`chirality_audit/review/reviews-CHIR-AUDIT-1.md`). Outcome:
F1/F2/F3 all survive — no missing entry, no wrong entry, no fourth sense. One
load-bearing finding (Copilot + ChatGPT convergence): the bare "emergent" label
overclaimed derivation-owed rows → graded **emergent (E)** established / **emergent
(P)** provisional. Plus: E20 reclassified emergent\* → unregistered (conditional, stops
pre-committing to Scenario A); ZBW circulation sense registered as deferred exclusion
X5 + OPEN-CHIR-2e (Copilot F1 candidate, not a confirmed falsifier); temporal primitive
clarified ordered (primitive) vs T-asymmetry (owed, OPEN-CHIR-2a). Grok's E19/E21
derivation sketches logged as OPEN-CHIR-1c/1d seeds, not closures (ChatGPT calibration
adopted). Artifact now v1.1 (13-page PDF, clean compile); no entry added or removed.
**One-line statement:** Chirality enters the current CPP framework (9 axioms +
600-cell + PCD cycle + existing CHIR derivations) at exactly 27 catalogued points,
classified primitive/emergent/unregistered along spatial/temporal/CP-asymmetric
senses.
**Central finding:** spatial chirality reduces (up to gauge + derivation) to the
single primitive `n̂` (FI-C-RC-1); temporal chirality to the PCD sequence carried by
A1 + A4 (asymmetry presupposed); CP-asymmetric chirality is uniformly emergent. The
deepest unregistered entry is the capture handedness (D3), consumed by every SD-CHIR
closure but derived from no registered axiom.
**Artifact:** `series_umbrella/series_substrate_chirality_arc/chirality_audit/theo_chir_audit_1.tex`
(v1.0; 12-page PDF; clean three-pass pdflatex compile) + reasoning fragment
`chirality_audit/reasoning/0632.md`.
**Falsifiers:** (F1) a chirality-touching element absent from the 27-entry inventory;
(F2) an inventory entry misclassified; (F3) a fourth operational sense not reducible
to spatial/temporal/CP-asymmetric.
**Last updated:** 29 May 2026

---

### OPEN-CHIR-1: Derivation of the emergent chirality entries
**Status:** OPEN
**Sector(s):** CHIR
**Priority:** HIGH
**Operational sense(s):** spatial (1a, 1b, 1d), spatial/CP (1c)
**One-line statement:** Derive each entry the audit classifies as *emergent* from
`n̂` + the 600-cell geometry + the PCD dynamics, without independent assumption.
**Sub-problems:**
- **OPEN-CHIR-1a:** 2I binary-icosahedral spinor-representation handedness (audit E12) from `n̂`.
- **OPEN-CHIR-1b:** icosahedral rotation sense (`I = A_5` chiral subgroup, audit E13) from sector-specific symmetry breaking.
- **OPEN-CHIR-1c:** capture/partnering handedness (audit E19) from a registered dynamical rule (shared with OPEN-CHIR-2d).
- **OPEN-CHIR-1d:** substrate magnitude `χ = φ⁻³` (audit E21) from `n̂` + 600-cell distance ratios. **Scope sketch (Patch 0637):** `chirality_derivations/sketches/theo_chir_chi_magnitude_1_scope.md`. Status of the value: `χ = φ⁻³` is registered as **FI-C-9** (foundational input, substrate-vacuum broken-symmetry order parameter), but its *value* has a partial geometric derivation — Capotauro **Finding C-3**: `χ = (1−φ⁻¹)/(1+φ⁻¹) = φ⁻²/φ = φ⁻³`, the edge-to-first-non-edge symmetric-bias ratio (this fixes the exponent −3 *given* the ratio, answering the reviewer's "why −3"). *Correction to the audit note:* E21 is NOT addressed by THEO-CHIR-CONT-1.3 — CONT-1.3 is magnitude *inheritance* (consumes `χ`), not derivation; the derivation is Finding C-3. OPEN-CHIR-1d decomposes into **1d-α** (ratio selection: why the edge-to-first-non-edge symmetric-bias ratio vs alternatives 1/√5, 5−2√5 — near-term, Layer 2/2.5, reserved theorem **THEO-CHIR-CHI-1**) and **1d-β** (the H₄→I₄ symmetry-breaking dynamics that eliminate FI-C-9 — deep, deferred to OPEN-SM-4 ↔ SS-corpus per F.1 §14.17; no ID reserved). E21 stays emergent (P) regardless of 1d-α (1d-β + the F.1 Case-A.1 provisional content remain). Numerical signposts (δ_CP ≈ 193.3° vs NuFIT 195°±40°; Δp_LR = φ⁻³/6 ≈ 0.0394 vs ~0.04) support φ⁻³ but are signposts, not derivations.
**Dependencies:** THEO-CHIR-AUDIT-1 (classification map); FI-C-RC-1 (`n̂`); 600-cell geometry (A2).
**Review seeds (Patch 0634):** Grok sketched starting structures for 1d (E21 from a pseudoscalar ∝ `n̂`·(v₁×v₂) over a cage/tetrahelix) and 1c (E19 as sgn(`n̂`·(displacement×polarization))). Neither is a closure — 1d does not fix the exponent −3 vs other φ-powers; 1c imports a capture rule not yet shown registered (ChatGPT calibration). Treat as derivation starting points, not results. See `chirality_audit/review/reviews-CHIR-AUDIT-1.md`.
**Cross-sector connections:** feeds OPEN-SD-CHIR-PRIMITIVE manifestation closures; 1d's value originates in Capotauro Finding C-3 (FI-C-9) and is *consumed* (not derived) by THEO-CHIR-CONT-1.3 (magnitude inheritance) and by the F.1 Phase-3 Case-A.1 δ=χ content.
**Paper(s):** future CHIR-derivation papers under the Substrate Chirality Arc.
**Last updated:** 29 May 2026

---

### OPEN-CHIR-2: Handling of the unregistered chirality entries
**Status:** OPEN
**Sector(s):** CHIR
**Priority:** HIGH
**Operational sense(s):** temporal (2a), spatial (2b, 2c), spatial/CP (2d)
**One-line statement:** For each entry the audit classifies as *unregistered*,
attempt a derivation; register a new framework axiom only if derivation fails
(programme presumption: derive).
**Sub-problems:**
- **OPEN-CHIR-2a:** explicit assertion (or derivation) of the PCD cycle's time-reversal asymmetry (audit E2-asymmetry / E17).
- **OPEN-CHIR-2b:** determine the constraint that fixes (or eliminates) the 5×24-cell partition choice (audit E11).
- **OPEN-CHIR-2c:** fix the perception-step implementation (vector vs oriented-bivector/pseudovector) (audit E18).
- **OPEN-CHIR-2d:** derive the capture handedness (audit E19; shared with OPEN-CHIR-1c) — the deepest unregistered entry, consumed by SD-CHIR-1/2 via ζ^W and ζ^qDP.
- **OPEN-CHIR-2e:** *(added Patch 0634, multi-AI review)* determine whether the ZBW (Zitterbewegung) circulation sense — the rapid between-CPs dipole-pair oscillation, a structure adjacent to but outside the PCD cycle — carries a chirality (audit exclusion X5). If parity/T-symmetric, argue so; if handed, add provisional entry E28 and re-tally. Raised by Copilot as an F1 candidate; not a confirmed falsifier (ZBW spec is outside the four audited input classes).
**Dependencies:** THEO-CHIR-AUDIT-1.
**Cross-sector connections:** 2d is load-bearing for SD-CHIR-1/2 and OPEN-FP-SF-2-CHIR; 2a connects to the F.1 DSL temporal-arrow work (THEO-DSL-3, manifestation iv).
**Paper(s):** future CHIR-derivation papers.
**Last updated:** 29 May 2026

---

### OPEN-CHIR-3: Alignment with observed Standard-Model chirality
**Status:** OPEN
**Sector(s):** CHIR
**Priority:** MEDIUM (gated on OPEN-CHIR-1 + OPEN-CHIR-2 progress)
**Operational sense(s):** CP-asymmetric
**One-line statement:** Once the primitive/emergent entries are mapped and derived,
construct the derivation chain from them to weak-interaction parity violation and
the PMNS/CKM CP-phases.
**Dependencies:** OPEN-CHIR-1, OPEN-CHIR-2; audit entries E4 (`φ`-winding of A3), E26 (SM parity link).
**Cross-sector connections:** THEO-CHIR-CONT-2 (V−A coupling), THEO-CHIR-CONT-3 (chiral-polarity-bias); OPEN-SM-5 (PMNS angles), OPEN-SM-4 (δ_CP via Capotauro).
**Paper(s):** the eventual chirality flagship — "Chirality in the Conscious Point Substrate: Primitive, Emergent, or Both?" (scope-sketch §7).
**Last updated:** 29 May 2026

---

### OPEN-CHIR-4: Interaction with OPEN-FP-F1-2 (Mechanism A derivation)
**Status:** OPEN
**Sector(s):** CHIR / FP
**Priority:** MEDIUM
**Operational sense(s):** spatial
**One-line statement:** Determine whether Mechanism A's derivation (OPEN-FP-F1-2)
passes through chirality, and if so register the dependency.
**Rationale:** Mechanism A specifies the substrate's polarisation response, the
load-bearing input to the dipole formation the weak interaction acts on; a chirality
dependency is plausible (audit E27).
**Dependencies:** THEO-CHIR-AUDIT-1; OPEN-FP-F1-2.
**Cross-sector connections:** F.1 Dynamical Substrate Law arc (THEO-DSL-1..12).
**Paper(s):** F.1; future CHIR-derivation papers.
**Last updated:** 29 May 2026

---

### THEO-CHIR-PCD-ORIENTATION-1 → OPEN-CHIR-F1-LINK RESOLVED (provisional): the `n̂` ↦ ω_PCD link
**Status:** RESOLVED (provisional) — Scenario B refuted; E20 emergent (P). Theorem registered
Patch 0636 at viability level (Layer 2.5), inheriting the F.1 ceiling.
**Sector(s):** CHIR / FP (F.1)
**Operational sense(s):** spatial (axis) + temporal (sign)
**One-line statement:** Whether the PCD-cycle orientation pseudovector `ω_PCD(v_host) = σ·n̂`
is derived from `n̂` (Scenario A → emergent) or is an independent primitive (Scenario B →
primitive alongside `n̂`).
**Resolution (THEO-CHIR-PCD-ORIENTATION-1, v1.0):** primitive-count theorem. Lifting the F.1
Phase-1 (net DI-bit current ∥ `n̂`) + Phase-2 (coupling rule) results, `ω_PCD = σ_cycle·n̂` is
a **product of two already-registered primitives** — the spatial primitive `n̂` (audit E16, the
axis) and the temporal primitive's handedness `σ_cycle` (audit E2/E5/E17, A1+A4, the sign). So
`ω_PCD` introduces **no independent third primitive**: **Scenario B refuted; E20 emergent from
the two registered primitives jointly**, preserving the audit headline that all spatial chirality
reduces to `n̂`.
**Layer:** viability (Layer 2.5). E20 reclassified **unregistered (conditional) → emergent (P)**.
Not established: the reduction rests on the F.1 viability-level result (three open commitments per
F.1 §14.17). The primitive-count is robust to all three (none reintroduces a direction or
handedness); only magnitude/Layer-3 rigor is provisional. (The audit `.tex` is v1.1-frozen; this
reclassification is authored by THEO-CHIR-PCD-ORIENTATION-1 and tracked here, not by re-editing
the audit.)
**Precondition cleared (artifact §3):** axiom-attribution reconciliation — `σ_cycle` attributed
to A1+A4 (canonical temporal primitive), not the F.1 sketch's pre-canonical "A5" (canonical A5 =
metric). F.1 sketch not edited inline (prior immutable workstream).
**Cross-link (flagged, not resolved):** `σ_cycle` (temporal cycle ordering) kept distinct from
capture handedness E19 (spatial/CP); identifying them would *merge* E20 into E19 (programme-positive
reclassification), not refute (artifact §5.3 / falsifier F3).
**Artifact:** `chirality_derivations/theo_chir_pcd_orientation_1.tex` (v1.0; 8-page PDF; clean
3-pass compile) + scope sketch `chirality_derivations/sketches/theo_chir_pcd_orientation_1_scope.md`
+ reasoning `chirality_derivations/reasoning/0636.md`.
**Falsifiers:** (F1) an independent direction in `ω_PCD` ≠ ±`n̂`; (F2) a sign content independent
of the temporal primitive's ordering; (F3) `σ_cycle` = E19 capture handedness (merges E20 into E19).
**Dependencies:** THEO-CHIR-AUDIT-1; `dynamical_substrate_law/sketches/F1_subquestion_pcd_orientation_link.md` (§11 Phase 1; §12 Phase 2; §14.17 viability ceiling); Reading C (FI-C-RC-1 `n̂`).
**Cross-sector connections:** F.1 DSL arc; THEO-DSL-4 (substrate current ∥ `n̂`); E21 magnitude
(OPEN-CHIR-1d) inherits the F.1 Phase-3 `δ=χ` provisional content; E19 (OPEN-CHIR-1c/2d) the
flagged cross-link.
**Next:** OPEN-CHIR-1d (E21 `χ=φ⁻³` magnitude) and OPEN-CHIR-1c/2d (E19 capture handedness), both
seeded by the AUDIT-1 review cycle.
**Last updated:** 29 May 2026 (Patch 0636)

---

*Sector file created at Patch 0632. Load this file when working any OPEN-CHIR-*
problem or the chirality audit. The OPEN-SD-CHIR-PRIMITIVE umbrella's
manifestation-closure status remains tracked in the SD/FP sectors and the
Capotauro / Chirality-Continuum / F.1 paper folders; this file tracks the
audit-derived downstream derivation programme.*

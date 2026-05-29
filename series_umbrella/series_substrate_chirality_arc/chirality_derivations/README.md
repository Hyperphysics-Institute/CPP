# Chirality Derivations — Sub-Corpus Index

**Folder:** `series_umbrella/series_substrate_chirality_arc/chirality_derivations/`
**Role:** home for the **downstream derivation theorems** spawned by the chirality audit
(THEO-CHIR-AUDIT-1), each resolving the classification of one audit entry from `n̂` + the
600-cell + the registered dynamics. Parallels `chirality_audit/` (the catalogue) — this folder
holds the derivations the catalogue called for.
**Status:** the three "deepest" audit-downstream entries (E20, E21, E19) are all resolved at
Layer 2/2.5, each honestly capped. The open frontier (FI-C-9, 1d-β, the E19/E20 merge) is named
below.

---

## The three theorems

| Theorem | Audit entry | Result | Layer | Artifact |
|---|---|---|---|---|
| **THEO-CHIR-PCD-ORIENTATION-1** | E20 (`n̂ ↦ ω_PCD` link) | `ω_PCD = σ_cycle·n̂`, a product of two registered primitives (n̂ spatial axis E16; σ_cycle temporal sign E2/E5/E17=A1+A4). Scenario B refuted; **E20 emergent (P)**. | 2.5 (viability) | `theo_chir_pcd_orientation_1.tex` |
| **THEO-CHIR-CHI-1** | E21 (`χ = φ⁻³` magnitude), sub-gap **1d-α** | A **locality criterion** (symmetric bias of the two nearest 600-cell shells) uniquely selects `χ = (1−φ⁻¹)/(1+φ⁻¹) = φ⁻³`; alternatives `1/√5`, `5−2√5` excluded as non-local. 1d-α **closed**. | 2/2.5 | `theo_chir_chi_1.tex` |
| **THEO-CHIR-CAP-1** | E19 (capture handedness), the deepest unregistered entry | capture handedness = `ζ` (registered involution) `× σ_capture`, with `σ_capture = sign(n̂) = FI-C-9` (verdict R1). No independent third primitive; **E19 emergent (P)**. | 2/2.5 | `theo_chir_cap_1.tex` |

The unifying shape: **all three reduce to `n̂` + the 600-cell + one substrate chirality sign**.
E20 and E19 share the *involution/axis × sign* form; E21 fixes the *magnitude* by locality.

---

## The open frontier (named, not hidden)

1. **FI-C-9 (the chirality magnitude/sign as a foundational input).** All three theorems
   *consume* FI-C-9 (the value `χ = φ⁻³` and the frozen enantiomorph sign); none derives it.
   Eliminating FI-C-9 requires the substrate-vacuum symmetry-breaking **dynamics** (sub-gap
   **1d-β**), a deep deferred target (F.1 §14.17; OPEN-SM-4 ↔ SS-corpus).
2. **1d-α residual freedom.** THEO-CHIR-CHI-1 selects the ratio *given* the symmetric-bias
   *form*; whether the magnitude generator must take that form is a stated structural assumption
   (CHI-1 falsifier F2).
3. **The E19/E20 merge (hypothesis).** THEO-CHIR-CAP-1 pins the *spatial* capture handedness to
   `sign(n̂) = FI-C-9`. Whether the *temporal* `σ_cycle` (E20) is the *same* sign — so that one
   substrate enantiomorph fixes spatial capture + temporal cycle + n̂-orientation alike — is the
   programme's most unifying chirality hypothesis, **plausible but unproven** (PCD-ORIENTATION
   §5.3 cross-link; CAP-1 §5).

---

## Folder structure

```
chirality_derivations/
├── README.md                         ← this index
├── theo_chir_pcd_orientation_1.tex   ← E20 (Patch 0636)
├── theo_chir_chi_1.tex               ← E21 / 1d-α (Patch 0638)
├── theo_chir_cap_1.tex               ← E19 (Patch 0640)
├── sketches/                         ← scope-and-precondition sketches (one per theorem)
│   ├── theo_chir_pcd_orientation_1_scope.md   (Patch 0635)
│   ├── theo_chir_chi_magnitude_1_scope.md     (Patch 0637)
│   └── theo_chir_cap_1_scope.md               (Patch 0639)
├── reasoning/                        ← Tier-4 VERBATIM per-patch reasoning (canonical record)
│   └── 0635.md … 0640.md
├── code/                             ← Tier-2/3 verification scripts
│   ├── verify_chi_phi3_ratio.py      (THEO-CHIR-CHI-1)
│   └── verify_capture_involution.py  (THEO-CHIR-CAP-1)
└── documentation_suite/             ← this consolidation (Patch 0641)
    ├── keywords-chirality-derivations.md
    ├── glossary-chirality-derivations.md
    ├── mechanism-chirality-derivations.md
    ├── phenomena-chirality-derivations.md
    ├── development-chirality-derivations.md
    ├── reasoning-index-chirality-derivations.md
    └── changelog-chirality-derivations.md
```

**Canonical record note.** The per-patch `reasoning/<patch>.md` fragments are the **Tier-4
verbatim canonical record** (captured at patch-time per `templates/reasoning_capture_protocol.md`).
The `documentation_suite/` files are *synthesized* from them at this milestone; they do not
replace the fragments. `reasoning-index-chirality-derivations.md` is a pointer-map into the
fragments, not a copy.

---

## Registration

Each theorem is registered via the `theorem-registry.md` changelog (the audit-precedent style;
the CHIR-sector theorem records live in `frontier_sectors/CHIR.md`). The audit `.tex`
(`chirality_audit/theo_chir_audit_1.tex`) is **v1.1-frozen** (3/3-reviewer-confirmed); all
downstream reclassifications (E20/E21/E19) are authored by the theorems here and tracked in
CHIR.md, never by re-editing the frozen audit.

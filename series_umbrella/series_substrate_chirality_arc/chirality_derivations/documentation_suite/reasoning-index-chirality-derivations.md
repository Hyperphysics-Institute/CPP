# Reasoning Index — Chirality Derivations

A **pointer-map** (Tier 2) into the Tier-4 verbatim reasoning fragments. The fragments in
`reasoning/<patch>.md` are the **canonical record**, captured verbatim at patch-time per
`templates/reasoning_capture_protocol.md`. This index does not copy them; it tells you what each
holds and where the load-bearing reasoning lives. (Patches 0632 + 0634 fragments are in
`chirality_audit/reasoning/`, the audit folder, as they predate this folder.)

| Patch | Fragment | Load-bearing reasoning it holds |
|---|---|---|
| 0632 | `chirality_audit/reasoning/0632.md` | The audit rebuild after window overflow; the 27-entry classification logic; the central spatial→`n̂` reduction. |
| 0634 | `chirality_audit/reasoning/0634.md` | Integration of the 3-reviewer cycle; the emergent (E)/(P) grading decision; why no falsifier fired. |
| 0635 | `reasoning/0635.md` | AUDIT-1 cycle close (3/3 on v1.1); the THEO-CHIR-PCD-ORIENTATION-1 scoping decision (primitive-count framing). |
| 0636 | `reasoning/0636.md` | E20 resolution: why primitive-count not magnitude; the robustness argument (3 F.1 commitments reintroduce no primitive); the A5→A1+A4 reconciliation; the E19 cross-link kept distinct. |
| 0637 | `reasoning/0637.md` | E21 scope: `χ=φ⁻³` is FI-C-9 but value-derived by Finding C-3; the CONT-1.3→Finding-C-3 correction; the 1d-α/1d-β decomposition; why staged not single-closure. |
| 0638 | `reasoning/0638.md` | The distance-spectrum exploration that found the locality criterion; the two residual freedoms (bias-form assumption; 1d-β); the `git add -A` stray-patch error + fix. |
| 0639 | `reasoning/0639.md` | E19 scope: the no-false-reduction discipline; the involution×sign insight; the R1/R2/R3 outcomes kept distinct; why R1 is likely-but-unproven. |
| 0640 | `reasoning/0640.md` | The 1c-β decisive test (SD-CHIR sign bookkeeping → R1); why R2 was *left open* deliberately; the local-`I_h` script surprise; the honesty caps held. |

## Verification scripts (Tier 2/3)

| Script | Theorem | What it asserts (machine precision) |
|---|---|---|
| `code/verify_chi_phi3_ratio.py` | THEO-CHIR-CHI-1 | 600-cell built; 8 distance shells; two nearest = φ⁻¹×12 + 1×20; bias = φ⁻³; `(φ⁻¹,1)` the unique adjacent φ⁻³ pair + max adjacent bias; `1/√5`, `5−2√5` produced only by non-adjacent edge-pairings. |
| `code/verify_capture_involution.py` | THEO-CHIR-CAP-1 | `ζ^W` involution; linear part `−I` flips `n̂`; edge-perturbation field odd under `n̂→−n̂` over all 720 edges (max `φ⁻³`); first-shell↔first-shell edges tangent (local-`I_h`). |

## Provenance

All fragments are `verbatim` (captured at patch-time), not reconstructed; none carries a
`STATUS: reconstructed` header. The capture rode the patch-presentation contract per the
reasoning-capture rider (bootup §3) at each of Patches 0635–0640.

# OSF Re-Deposit Prep — SR-1 v20

**Prepared:** 15 July 2026 (Patch 2505). **Author of prep:** Opus. **Action owner:** Thomas (or Isak).
**Trigger:** Patch 2474 marked OSF re-deposit **REQUIRED** (main claims changed at triage); the requirement is inherited and sharpened by v20 (Patch 2503), which is the version to deposit.
**Placement note:** flat file per SR-1's pre-subfolder documentation convention (companion files live flat in `series_relativity/papers/`).

---

## §1 — Why this re-deposit is not optional and should not wait long

The OSF component currently hosts **v17**, which contains: the invalid dimensional-necessity k-derivation, four Monte-Carlo citations whose artifacts were stubs with hard-coded figures, the five-prediction set that double-counts k·ΔSSV = γ−1 as a deviation from the SR it reproduces, and the class-coverage "Geometric Insufficiency Theorem" that is false as stated (refuted by its own Model 3). That is a live integrity exposure on the public record under DOI. **Sequencing (worker ruling under PD-006):** ClearPC PDF recompile → **re-deposit promptly** → panel round (which can trigger a further v20.x update if SHIP-WITH-CHANGES). Rationale: the panel verifies fidelity of an already-ratified state; the public-record correction does not gate on it.

## §2 — Deposit mechanics

This is an **update to the existing SR-1 component** (registered on OSF at v17), not a new component:
1. Open the SR-1 component under parent project DOI 10.17605/OSF.IO/JXE8D.
2. Upload the recompiled **v20 PDF** and the **v20 .tex** (OSF versions files under the same name — upload with identical filenames to preserve the version chain; do NOT delete v17, the version history is part of the correction record).
3. Replace the component **Description** with §3 below.
4. Append **Tags** from §4 (keep existing tags; add the new ones).
5. Wiki/notes (if the component has one): paste the §5 version-correction notice at the top.

**Files to upload (after ClearPC recompile):**
- `SR-1_special_relativity_emergence.pdf` (v20 recompile — verify title block reads "Version 20, 15 July 2026" before upload)
- `SR-1_special_relativity_emergence.tex` (v20)
- (bibliography: central `bibliography/cpp_references.bib` per programme convention — include only if the v17 deposit included one)

## §3 — Component Description (paste whole)

SR-1 presents a substrate account of special relativistic effects (time dilation, length contraction, the twin paradox) in Conscious Point Physics, on the 600-cell quasicrystalline lattice. Version 20 (15 July 2026) is a major correction-and-grounding revision and supersedes v17 for all claims. WITHDRAWN (Patches 2471–2475, standing): the five-prediction set and muon bound (the claimed deviation was the SR effect itself, double-counted; the predictions scaled with acceleration while every stress definition is velocity-dependent); the "no adjustable parameters" claim; four Monte-Carlo verification citations (artifacts did not exist or were non-functional stubs); the class-coverage Geometric Insufficiency Theorem (its cap expansion was wrong — f^{5/2}, not f^{1/2} — and the theorem was refuted by its own Model 3). ESTABLISHED at v20: the 600-cell geometric constants from the binary icosahedral group 2I (verified, 31/31 checks); the elimination of three natural displacement models (strain exponents 1, 1, 5/2 against the required 2); and — new at v20 — a grounding of the strain–kinematics identity ε = γ−1 at the energy level for closed self-bound patterns, at W2 world-call strength, via an independently and blind-pinned inertia mechanism (Laue coefficient exactly 1, anchored on E₀ = ℏν_C) together with the Lorentz covariance of the substrate wave equation, with caveats inherited verbatim (a viability result at world-call strength, not a theorem; the covariance rests on a hopping-sum proxy). Consequently the framework is empirically equivalent to special relativity as a grounded consequence of the mechanism — the paper is a grounding paper, not an empirical competitor — and its inherited falsifier is the l=6/q⁴ dispersion-anisotropy floor at ~l_P/10³⁰ (in-principle discriminating, below observational reach). Full correction history in the .tex CHANGELOG header and the repository record (Patches 2471–2503).

## §4 — Tags (append to existing)

special relativity; Lorentz factor; time dilation; 600-cell; quasicrystal; Conscious Point Physics; emergent relativity; grounding; inertia; Laue theorem; correction; retraction; W2 world-call

## §5 — Version-correction notice (component wiki, top)

**Notice (15 July 2026):** Versions through v17 of this deposit contained claims withdrawn at v19–v20, including a prediction set, a numerical-verification set, and a theorem now known to be erroneous. v20 is the corrected version of record; the withdrawals and their mechanism-level diagnoses are documented inside the paper (Sec. "Empirical Status") rather than silently removed. Readers citing SR-1 should cite v20.

## §6 — Post-deposit checklist

- [ ] Record the deposit date + any new version DOI here.
- [ ] `paper_catalog.md`: SR-1 row → v20, re-deposited, date.
- [ ] `README.md` + `predictions.md`: confirm SR-1 no longer counted in the zero-parameter prediction tally (feeds OPEN-WORKFLOW-PREDICTION-AUDIT; if the audit sweep is a separate patch, note it there rather than double-editing).
- [ ] `publication_status_audit.md`: SR-1 entry updated.
- [ ] This file: flip **Status: PREPARED** → **Status: DEPOSITED at <date>**.

**Status: PREPARED (awaiting ClearPC recompile; deposit immediately after).**

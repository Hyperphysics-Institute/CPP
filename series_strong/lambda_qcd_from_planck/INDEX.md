# Λ_QCD-from-Planck Arc — Patch Index

**Location:** `series_strong/lambda_qcd_from_planck/INDEX.md`
**Purpose:** A flat, chronological list of this arc's patches so it can be followed in development
order regardless of patch label. Git history is the source of truth for ordering; this index is
the human-readable through-line. The arc runs in the **1000-series** (1001+) as a parallel-window
lane (see `parallel_dev/` band convention); labels are intentional and not rewritten.

**Maintenance:** append each new arc patch here (label · one line) when it lands.

## Sequence

| Patch | What |
|-------|------|
| 1001  | Arc scaffolded — README (target/mechanism/Routes A,B/falsifier), step-0 framing doc, IR-anchor self-consistency verify (3/3), reasoning fragment, changelog. Route B (non-log/discreteness) set as primary. No registration; nothing chained into SS-1 or the DP-Sea appendix. |
| 1002  | Route B opened (non-log/discreteness, primary). Framework: Λ_QCD as IR Landau pole of a one-boundary-value flow; PSR saturation fixes the sign (α_s(E_P)→0). **Sensitivity theorem** proved: N/α ≈ 2300× amplification ⇒ α_s(E_P) must be derived to sub-percent (exact identity), so 1%-level numerology is ruled out as a method (2π² futility demo, −33%). Target sharpened to: derive α_s(E_P)=0.0197… from the PSR_eff→l_P/2 approach rate / 600-cell mode structure. NOT closed; no registration; SS-1 / appendix untouched. |
| 1003  | **600-cell mode structure: NEGATIVE result.** Computed exact 600-cell graph Laplacian spectrum (φ-structured; gap 6φ⁻², λ_max 12+6/φ). Falsification-first scan of natural invariants as the bare coupling: **nothing within 20% on Λ** (−83% to +224%). Strongest positive residue `g₀=1/2` (PSR_eff→l_P/2 echo) → Λ≈0.31 GeV (+42%): a real parameter-free order-of-mag-plus result, but fails sub-percent bar and `g₀=1/2` not derived. VERDICT: Route-B-by-invariant-matching does not close; strong negative lean toward "calibrated, not Planck-derived." Only live path = a *derived* mode-sum→running mechanism. Recommend adopting calibrated stance (TODO-016 Track 1) as operating answer. No registration; SS-1/appendix untouched; shared-registry status edits deferred to flagged INT patch. |
| 1004  | **Framing correction (no new derivation).** PSR = *Planck Sphere Radius* (not "Phase-Space-Restriction"); README fixed. Category-error diagnosis: `E_P=ℏc/l_P` is not a fundamental cutoff — `l_P` is the rest-frame PSR (baseline, SSV-dependent, emergent ruler), GP spacing is sub-Planck (nested-600-cell, 0736; "10³⁰" flagged as unverified). 1003 negative **reinterpreted, not retracted**: absolute scale = "one shared calibration, not derived" (c05/TODO-014), so QCD-scale-calibrated = same calibration as G/l_P. Derivable content = the **ratio** → redirect to `op:sigma` at the IR end (short lever arm). Glossary line-71 inconsistency flagged for a separate STOP-and-warn patch. In-lane; SS-1/appendix untouched. |

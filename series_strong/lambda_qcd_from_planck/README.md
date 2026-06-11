# Λ_QCD from the Planck scale — Derivation Arc (Project C)

**Folder:** `series_strong/lambda_qcd_from_planck/`
**Project:** `future_projects.md` Project 2b — opened Session 156, Patch 0839; scaffolded Patch 1001.
**Open problems addressed:** SS-1 `op:lambda_psr` (primary) and `op:sigma` (downstream, via C14).
**Patch band:** 1000-series (1001+), parallel-window lane; owned path = this folder only.
**Status:** SCAFFOLD (step 0). The IR end is locked in as self-consistent; the open arc is the
UV boundary condition. No THEO/PRED registered yet; nothing chained into SS-1 or the DP-Sea
appendix yet (those are STOP-and-warn files under the lightweight two-window protocol).

> **Framing correction (Patch 1004).** Patches 1001–1003 treated `E_P = ℏc/l_P` as a *fundamental*
> UV cutoff to run a coupling down from. On the corpus's canonical reading (SR-1 / c05, glossary)
> that is the wrong currency: `l_P` is the **rest-frame Planck Sphere Radius (baseline PSR)** — an
> emergent, SSV-dependent ruler — not the lattice granularity and not a fundamental cutoff, and the
> absolute Planck scale is itself "one shared calibration, not derived" (c05 / TODO-014). The
> negative result of 1003 is therefore reinterpreted (not retracted) as *consistency with
> calibration*, and the live derivable target moves to `op:sigma` at the IR end. See
> `1004_framing_correction_psr_currency.md`.

---

## The target (no PDG input)

Derive, from the Planck length `l_P` and `sea_strength = 0.185` alone:

- **Λ_QCD ≈ 0.218 GeV** (the SS-1 `op:lambda_psr` target), and
- the **DP binding scale E_eDP ≈ 88 MeV** (with `E_qDP = 3·E_eDP`, `E_hDP = √(E_eDP·E_qDP)`
  following from the already-clean ratios).

The bridge to build is Planck (~10¹⁹ GeV) → QCD/DP scale (~10⁻¹ GeV): ~20 orders. A hierarchy
that large is **logarithmic/exponential** (dimensional transmutation), never a fixed
multiplicative suppression — `αℏc/(φ l_P)` evaluates to ~4.5×10¹⁶ GeV and is the wrong *kind* of
relation (this is exactly the false appendix formula TODO-016 Track 1 removes).

## The mechanism (SS-1 `rem:psr`)

**PSR (Planck Sphere Radius) saturation.** As two quarks approach `r ≲ l_P`, the effective PSR
shrinks toward `PSR_eff → l_P/2`; the Sea can no longer nucleate qDP chains fast enough to
self-collimate, the effective string tension vanishes, and `α_s → 0` (asymptotic freedom). At long
distance, PSR is unsaturated, chains self-collimate, and `α_s → ∞` at `Q → Λ_QCD` (confinement).
The RG structure is the exact theorem `β₀ = 7` (SS-1 `thm:beta0`); PSR saturation is its physical
substrate origin.

## What is already solid (locked in Patch 1001)

The whole problem reduces to **one undetermined number: the UV boundary `α_s(E_P)`.** Everything
else is in place:

1. **β₀ = 7** — exact (SS-1 `thm:beta0`), not a fit.
2. **The IR end is self-consistent.** SM-7's lattice coupling `5/(8φ) ≈ 0.386`, run with `β₀ = 7`
   down to `Λ = 0.218 GeV`, lands at `Q ≈ 2.2 GeV` — exactly where physical `α_s` sits at a
   charmonium scale. So `5/(8φ)` is an **IR anchor**, not a UV input, and the picture is not
   order-of-magnitude wrong (the logged "~1 GeV, factor-of-6 at 1-loop" gap is an O(1)-in-exponent
   refinement, ~4% in the exponent).
3. **The C14 σ↔r_conf↔Λ chain** ties `op:sigma` to this arc: `r_conf = √(α_s ℏc/σ)`,
   `σ = α_s ℏc/r_conf²`. Settled once the scale is set.

Recorded by `code/verify_ir_anchor_selfconsistency.py` (3/3 consistent).

## The open arc — two routes (B primary)

The 1-loop inversion demands `α_s(E_P) ≈ 0.0197` to land on `Λ_QCD = 0.218 GeV`. The question is
whether `PSR_eff → l_P/2` fixes that from `l_P + sea_strength`, without a PDG anchor.

- **Route B — non-log running near l_P (PRIMARY).** The 600-cell lattice is discrete at `l_P`, so
  the running in the top decade is plausibly **non-logarithmic** ("lattice-discreteness correction
  to RGE," flagged in SS-1's summary table). If so, the naive log inversion that demanded
  `α_s = 0.0197` does not bind: the discreteness correction itself carries part of the hierarchy.
  This is the CPP-native route — the lattice *is* the regulator — and is weighted higher.
- **Route A — PSR fixes the UV boundary directly (SECONDARY, kept open).** Show that the
  `PSR_eff → l_P/2` geometry + `sea_strength = 0.185` pins `α_s(E_P) ≈ 0.0197` independently. Counts
  **only** if ~0.02 falls out of the geometry on its own; if it has to be reverse-engineered from
  the answer, it does not count.

## Falsifier

If no `l_P → QCD-scale` relation reproduces `Λ_QCD ≈ 0.2 GeV` (and the DP spectrum) from
`l_P + sea_strength` within tolerance and **without** PDG input, abandon the "DP scale is
Planck-derived" claim in favour of permanent calibration — TODO-016 Track 1's honest "calibrated"
stance becomes the terminal answer and the DP-Sea appendix stays as corrected there.

## One internal-consistency flag (settle before chaining `op:sigma`)

The C14 self-consistent point `(r_conf = 0.161 fm, σ = 0.900 GeV/fm)` implies `α_s ≈ 0.118` (the
M_Z value), **not** the lattice `0.386`; feeding `0.386` gives `r_conf ≈ 0.29 fm`. So `op:sigma`
must state *which running `α_s`* enters C14 — that choice moves `r_conf` by ~1.8× and must be fixed
before `σ`-from-`sea_strength` can be trusted.

## Folder structure

```
lambda_qcd_from_planck/
  README.md            ← this file (target / mechanism / routes / falsifier)
  INDEX.md             ← flat chronological patch list
  NNNN_<step>.md       ← each derivation step, patch-numbered
  code/                ← verify scripts, one per check
  reasoning/NNNN.md    ← verbatim per-patch reasoning (capture protocol)
  documentation_suite/ ← changelog (+ glossary / mechanism / … as the arc grows)
```

## On success

Register the derivation (THEO/PRED per registry rules + panel sign-off); upgrade SS-1
`op:lambda_psr` / `op:sigma` and the DP-Sea appendix from "calibrated" to "derived"; close
TODO-016 Track 2. The entire DP binding spectrum then becomes a first-principles consequence of
`l_P + sea_strength + the 600-cell geometry`.

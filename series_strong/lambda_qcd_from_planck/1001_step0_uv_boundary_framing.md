# Step 0 — Framing: the problem is one UV boundary condition

**Patch 1001. Project C / SS-1 `op:lambda_psr`. Step-0 (framing, no derivation yet).**

This document fixes *what is being solved* and *where the open part actually is*, before any
derivation is attempted. It deliberately solves nothing: it locks in the solid IR end and isolates
the single open number, so Patch 1002+ (Route B) attacks the right target.

## 1. The reduction

Standard dimensional transmutation: with a one-loop running coupling
`α_s(Q) = 2π / (β₀ ln(Q/Λ_QCD))` and `β₀ = 7` (SS-1 `thm:beta0`, exact), the confinement scale
`Λ_QCD` is the single integration constant of the flow — set entirely by the **boundary value of
`α_s` at the UV scale**. In CPP the UV scale is the 600-cell lattice spacing `≈ l_P`, energy
`E_P = ℏc/l_P ≈ 1.22×10¹⁹ GeV`. Therefore:

> **Deriving Λ_QCD from l_P ≡ fixing α_s(E_P) from l_P + sea_strength, with no PDG input.**

Everything else in the strong-sector flow is already pinned. This is the entire content of the
project, stated as one sentence.

## 2. What is already solid (and why this is not a long-shot)

**(a) The IR anchor is self-consistent.** SM-7 gives the lattice coupling `α_s = 5/(8φ) ≈ 0.386`.
Running that with `β₀ = 7` *down* to the target `Λ = 0.218 GeV` places it at

```
Q = Λ · exp(2π / (β₀ α_s)) ≈ 2.23 GeV,
```

a charmonium-scale where physical `α_s ≈ 0.39` — correct. So `5/(8φ)` is an **IR-scale anchor**
sitting at ~2 GeV, *not* a Planck-scale input. The IR end of the flow already lands in the right
place; nothing there is broken.

**(b) The gap is small in the only place it matters — the exponent.** The naive estimate
`√(σℏc/α_s) ≈ 0.68 GeV` is a factor ~3 over target (the paper logs "~1 GeV, factor-of-6"). Across
a 20-order hierarchy, a factor of a few is a **~4% error in the exponent** `2π/(β₀ α_s)`. The
mechanism is essentially right; what is missing is an O(1) refinement of the exponent, not a new
mechanism.

## 3. The open number, exactly

Invert the one-loop relation at the UV scale:

```
α_s(E_P) = 2π / (β₀ · ln(E_P/Λ_QCD)) = 2π / (7 × 45.47) ≈ 0.0197.
```

So a pure one-loop flow needs `α_s(E_P) ≈ 0.020`. The known CPP coupling `5/(8φ) ≈ 0.386` is **not**
this number (it is the IR anchor of §2a); feeding `0.386` in at `E_P` puts the Landau pole at
~10¹⁸ GeV — useless. The open arc is to produce `≈ 0.020` (or its non-log equivalent) from the
substrate.

## 4. Why Route B (non-log near l_P) is primary

The one-loop inversion in §3 *assumes* logarithmic running all the way up to `E_P`. But the
600-cell lattice is **discrete at l_P** — the continuum RGE cannot hold in the top decade, and
SS-1's own summary table flags exactly this ("non-log `α_s` running at Planck scale: lattice
discreteness correction to RGE"). If the running is non-logarithmic near `l_P`, the demand
`α_s(E_P) ≈ 0.020` is an artifact of extrapolating the log form too far; the discreteness
correction carries part of the hierarchy and the *effective* boundary need not be 0.020.

Route B therefore reframes the target: instead of "find a substrate reason for `α_s(E_P) = 0.020`,"
it is "compute the lattice-discreteness-corrected flow from `PSR_eff → l_P/2` and check what `Λ_QCD`
it produces." This is CPP-native — the lattice *is* the regulator — and it sidesteps the
reverse-engineering risk that makes Route A suspect.

**Route A** (PSR geometry pins `α_s(E_P) ≈ 0.020` directly) stays open as a secondary check, valid
only if `0.020` emerges from the `l_P/2` geometry + `sea_strength = 0.185` independently of the
target.

## 5. The C14 convention flag (carried, not yet resolved)

Chaining `op:sigma` (σ from sea_strength) onto this arc via C14 requires knowing which `α_s` enters
`r_conf = √(α_s ℏc/σ)`. The C14 self-consistent point `(r_conf = 0.161 fm, σ = 0.900 GeV/fm)`
implies `α_s ≈ 0.118` — the M_Z value — not the lattice `0.386`. This factor-of-~3 in `α_s` is a
factor-of-~1.8 in `r_conf`. It must be settled (which running scale C14 is evaluated at) before
`op:sigma` is chained. Logged here; not on the critical path for the Route-B `op:lambda_psr` attack.

## 6. Exit criterion for step 0

Met: the problem is reduced to one number (`α_s(E_P)`), the IR end is shown self-consistent, the
primary route (B) and its target reframing are fixed, and the C14 flag is recorded. Patch 1002
opens Route B: the lattice-discreteness-corrected flow from `PSR_eff → l_P/2`.

*(Verify: `code/verify_ir_anchor_selfconsistency.py` — 3/3 consistent.)*

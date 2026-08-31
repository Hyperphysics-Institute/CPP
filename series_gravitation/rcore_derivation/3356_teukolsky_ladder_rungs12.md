# Teukolsky ladder, rungs 1–2 — the radial build begins on validated ground, and the first exact complex resonance corrects Leg A's width by 2.5×

**Patch 3356, 30 Aug 2026 — Session 157.** Verify:
`code/3356_teukolsky_ladder_rungs12_verify.py`, **8/8 PASS**.

## §1 Rung 1 — validation against known answers

Leaver's continued fraction for Schwarzschild, recurrence written from
memory — precisely the kind of step that has been wrong twice this
session, which is *why* known answers are the test:

| ℓ | computed | published | rel. error |
|---|---|---|---|
| 2 | 0.37367 − 0.08896i | 0.37367 − 0.08896i | 7.5e−6 |
| 3 | 0.59944 − 0.09270i | 0.59944 − 0.09270i | 7.4e−6 |
| 4 | 0.80918 − 0.09416i | 0.80918 − 0.09416i | 5.3e−6 |

Root-finder and recurrence proven to five figures before any new
physics is touched.

## §2 Rung 2 — the first exact complex wall resonance in the lane

Direct inward integration from the outgoing asymptotic solution
(coefficients fitted numerically to the ODE residual, not recalled),
Dirichlet wall at areal 9M/4, χ = 0, ℓ = 2:

| parity | ω (M = 1) | f @ 62 M_⊙ | **Q** | e-fold time |
|---|---|---|---|---|
| Regge–Wheeler | **0.44859 − 0.11749i** | 233.8 Hz | **1.91** | 8.5 GM |
| Zerilli | 0.44506 − 0.13442i | 232.0 Hz | 1.66 | 7.4 GM |

**Instrument validation, asserted:** the root is independent of the
integration start (r₀ = 40, 60, 80 agree to 2.5e−8 — the instability
test for Im ω < 0), and the zero is sharp (|ψ| at the root is 6e−8 of
its value a small step away).

## §3 Against Leg A (3333): position right, width wrong by 2.5×

- **Position:** exact Re ω = 0.44859 vs Leg A's time-domain peak
  0.4488 (**−0.05%**) and its FD Wigner peak 0.4535 (−1.1%). Leg A's
  TD cross-check was, in hindsight, the more accurate of its two
  instruments.
- **Width — a correction, stated as one:** Leg A inferred **Q ≈ 4.9**
  from the Wigner delay τ = 21.5. The exact root gives **Q = 1.91**.
  The Wigner-delay-to-lifetime mapping is unreliable for a resonance
  sitting on the barrier top, and it overestimated the lifetime ~2.5×.
  That Q ≈ 5 propagated into GR-2 (demoted at CONV-034 to a
  "directional note" for the Kerr transport, but still quoted) — **the
  note now needs the exact number.** The line is broader than the
  paper implies.
- **The anchor re-measured:** the above-top shift is **+15.3%** exact
  (was +17% from the FD peak).

## §4 What this means for the observable prediction

Nothing moves in *position* — 234 Hz vs 236 Hz at the benchmark. But
a broader line (Q ≈ 1.9 rather than ≈ 5) is a **less sharp
spectroscopic target**, and GR-2 V1.5's "Q ≈ 5, indicating direction
and rough scale" should read "Q ≈ 1.9 at χ = 0, ℓ = 2 (exact); Kerr
widths not yet computed." Queued for the next GR-2 touch; it weakens
a directional note rather than a registered quantity, so it folds
without a round.

## §5 Scope and what remains

Schwarzschild only; RW/Zerilli (s = 2 axial/polar), not Kerr
Teukolsky; direct integration validated at r₀ = 40–80 (instability
grows beyond ~120). **Rung 3 — Kerr, s = −2, Sasaki–Nakamura — is the
remaining heavy build and is not started here.** The instrument that
will do it (numerically-fitted outgoing series + inward integration +
complex root-finding + r₀-independence and sharpness assertions) is
now validated on the case where the answer was known, which is the
only honest way to start.

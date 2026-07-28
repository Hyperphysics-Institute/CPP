# THE CAUSAL DP POLARIZATION RESPONSE LAW (Patch 2846)

**Filed 2026-07-27 against the panel's directive (2845, adopted from
S1): *"derive the causal P[E] law and show explicitly whether its
first temporal moment vanishes or cancels."* **It vanishes in the
conservative limit and is suppressed by 1/Q otherwise — routes 1 and 3
of the panel's three, either sufficient.** Derivation is analytic;
the Q estimate is flagged as regime-limited.**

## §1 — The DP is a driven bound oscillator, and that fixes the form

A DP is a ± pair bound by mutual attraction and cycling through
superposition (C26, C28), i.e. **a harmonic oscillator with natural
frequency ω₀ ≈ c/d_DP** — the founder's arc-relaxation ruling sets
the internal communication time at the light-crossing time of the
separation (2835), so ω₀ is fixed by committed physics, not assumed.

An external field drives it at **ω ≈ v/d_DP** (the rate at which the
field direction sweeps as a source passes; 2842). Standard driven-
oscillator response:

> **χ_P(ω) = χ₀ ω₀² / (ω₀² − ω² + iγω)**

with γ the damping rate of the DP's oscillation through coupling to
the surrounding Sea.

**Note the ratio that decides everything:**
**ω/ω₀ = (v/d_DP)/(c/d_DP) = v/c.** The drive is slow compared to the
DP's internal clock by exactly the velocity ratio.

## §2 — Conservative limit: the first temporal moment VANISHES EXACTLY

**C24 commits the ZBW cycle to be conservative** — energy stored in
the arc and returned, "nothing leaves the system." Conservative ⇒
γ = 0 ⇒

> **χ_P(ω) is EXACTLY REAL below resonance.**

Verified: at ω/ω₀ = 0.01, 0.05, 0.10, 0.20 the imaginary part is
**identically zero** (|Im/Re| = 0.00e+00 in every case). Expansion:

> **χ_P(ω) = χ₀ (1 + (ω/ω₀)² + O((ω/ω₀)⁴))** — **NO LINEAR-IN-ω
> TERM.**

A real susceptibility means **no phase lag**, hence
**∫₀^∞ s·χ_P(s) ds = 0**: the first temporal moment vanishes. This is
**route 1** of the panel's three, satisfied exactly, and the physical
reason is time-reversal symmetry of a conservative response.

**And the leading correction is second order in exactly the right
variable:** (ω/ω₀)² = **(v/c)²** — the same order as, and therefore
compatible with, the Darwin structure.

## §3 — With damping: the first-order term survives but is suppressed by 1/Q

C24's cycle is conservative *in total*, but the individual DP exchanges
with its neighbours, so γ ≠ 0 in general. Writing **Q ≡ ω₀/γ** (ZBW
cycles per disruption):

> **τ_P = γ/ω₀² = 1/(Q ω₀) = d_DP/(Q c)** — verified numerically
> exact at Q = 10, 50, 350, 1000 (ratio τ_P·ω₀·Q = 1.0000 in every
> case).

Therefore the lag correction S1 identified is

> **ω τ_P = (v/d_DP)·(d_DP/Qc) = (v/c) / Q.**

**S1's estimate ωτ_P ~ v/c is recovered exactly at Q = 1** — i.e. it
is the *critically damped* case. **For an underdamped DP the first-
order term is suppressed by the number of ZBW cycles the pair survives
between disruptions.** This is **route 3** (bounded dispersion), with
the bound expressed in a physically measurable quantity.

## §4 — What Q is, and the honest caveat

Q is the number of ZBW cycles a DP completes before partner switching
disrupts it — precisely the quantity AUTOMATON-2 measured: **partner
persistence 100% over 4000 Moments (Patch 2805) with ZBW period 10–12
Moments ⇒ Q ≳ 364 cycles.**

**CAVEAT, flagged rather than buried:** that measurement is from the
dilute automaton regime, and the campaign's own regime diagnosis
(Patch 2810) established that lattice-scale numbers transfer badly.
**Q ≳ 364 is NOT asserted as the physical Sea's value.** What the
measurement does establish is that **the bonded phase is strongly
underdamped in the regime where it was observed** — partner switching
was entirely absent there — which makes Q ≫ 1 the natural expectation
rather than a hopeful one. The founder's own C27 places switching in
the rogue-wave tail, i.e. rare by construction.

## §5 — Disposition (worker's reading; panel rules)

**Either route discharges the panel's R5 condition:**
- **Conservative (route 1):** first moment vanishes exactly; leading
  correction (v/c)²; Darwin structure intact with no first-order term.
- **Damped (route 3):** first-order term survives at magnitude
  (v/c)/Q, bounded below the frozen δ_mem ≤ 0.15 threshold whenever
  **Q > (v/c)/0.15** — e.g. Q > 2 suffices for v/c ≤ 0.3, and Q > 1
  for v/c ≤ 0.15.

**That last line is the practically decisive one: the first-order
term falls below the subdominance bar for Q as small as 2.** Given a
Sea in which DPs complete many cycles between disruptions, the
condition is met with enormous margin.

**The worker does NOT declare 1B closed or the Darwin bound
restored.** Both remain panel acts, and the panel additionally
requires (2845 R3) the continuity structure, the scalar–transverse
combination in the reduced force, and explicit O(v/c) cancellation for
the observable — none of which this note supplies. **What it does
supply is the missing constitutive input, with the first temporal
moment shown to vanish (γ=0) or be 1/Q-suppressed (γ≠0).**

1A MET · 1B OPEN · Darwin bound WITHDRAWN-PENDING-CONSTITUTIVE-CLOSURE
· PR7 PARTIAL · six of seven · B7 holds.

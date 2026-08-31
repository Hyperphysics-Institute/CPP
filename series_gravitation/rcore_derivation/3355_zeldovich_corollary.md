# The Zel'dovich bound — RCORE-3 item (d) discharged as a corollary of 3352, and stronger than expected

**Patch 3355, 30 Aug 2026 — Session 157.** Verify:
`code/3355_zeldovich_corollary_verify.py`, **4/4 PASS** (all-FAST).

## §1 The mechanism, and why the theorem kills it

A Zel'dovich/Press–Teukolsky runaway needs two things: superradiant
amplification (ω < mΩ_w) **and** a cavity that returns the amplified
wave so gain compounds per round trip. Amplification alone is
single-pass and cannot run away.

3352 proved {superradiant} ∩ {trapped} = ∅ for every ℓ, m, ω in the
window, at every spin to 0.99. So no mode can compound. **Growth rate
zero at eikonal-WKB grade; growth time unbounded.** Item (d) closes
without a rate ever being computed — the strongest form a bound takes.

## §2 Stronger than intended: superradiant waves never reach the wall

The 3352 inequality says R(r_w) < 0 for a superradiant mode — the wall
sits in the classically forbidden region for that wave. So the wave is
turned around by the barrier's outer face **before reaching the
surface**. It is not merely un-trapped; **it is never amplified at
all**, because it never touches the rotating body. The inequality does
double duty: no cavity, and no surface contact for the window.

Confirmed from the other side too: every trapped mode the lane has
ever found (3339/3349, extreme-retrograde ℓ ≥ 7) has m < 0, hence
mΩ_w < 0 — no window whatsoever.

## §3 What would reopen it

A mechanism placing superradiant energy *inside* the wall's forbidden
region: a breakdown of the A1–A3 surface construction
(OPEN-GR-RCORE-4), or an s = −2 correction to the radial function large
enough to flip the sign of R(r_w) in the window. The 3352 margin is
0.283 at the benchmark, so the latter would need a ~40% effect — far
beyond the +4.6% angular correction 3353 measured.

## §4 Registry

- **OPEN-GR-RCORE-3(d): CLOSED** at eikonal-WKB grade, as a corollary.
- **RCORE-3 remaining: the s = −2 angular sector and the radial
  Teukolsky build** — everything else in the item is discharged.
- GR-1h's "Planck-core bomb" worry, carried since March: closed at
  the eikonal level (3339), then structurally (3352), now with the
  growth rate itself shown to vanish (3355).

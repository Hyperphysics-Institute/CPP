# RCORE-2(iv) DERIVATION — The Kerr Exclusion Surface and the Ergoregion-Censorship Theorem
## Patch 3320, 21 Aug 2026 — derivation-conditional grade; CONV round owed before any paper edits

**Supersedes (upward):** the 3318 reconnaissance. The scalar-only proxy
gave χ_crit = 2/√7 as a conservative bound; the two-component census
derivation replaces it with **censorship at ALL spins**.

## §1 Construction: three stated assumptions, then exact mathematics

- **A1 (scalar census ≡ lapse dictionary).** The ratified log-lapse
  dictionary N = −2 artanh(kΔ/2) inverts to
  s ≡ kΔ_scalar = 2(1−α)/(1+α). On isotropic Schwarzschild this
  reproduces the ratified linear source relation μ/r̄ EXACTLY (script
  check 0) — A1 is the unique lapse-side extension preserving the
  ratified static limit.
- **A2 (vector census ≡ dragging speed).** The rotational SSV
  component's dimensionless register demand is the local dragging
  speed v = ωϖ/α — the azimuthal displacement demanded per Moment, in
  local reach units (the same units the scalar demand uses; the
  C*-vs-c question is thereby internally consistent: both demands are
  measured against the local reach).
- **A3 (quadrature).** Radial (compression) and azimuthal
  (circulation) demands are orthogonal directions on the register, so
  the total census magnitude is |kΔ|² = s² + v². The exclusion surface
  is the saturation locus **F ≡ s² + v² = 1.**

Everything after A1–A3 is exact. In particular the theorem's engine is
a textbook identity the script verifies symbolically on Kerr (check 2):

  **g_tt = −α²(1 − v²)** — the ergosphere (g_tt = 0) IS the v = 1
  surface, exactly.

## §2 The theorem

**Ergoregion censorship.** On the ergosphere, v = 1, so
F = s² + 1 > 1 strictly (α < 1 there ⇒ s > 0). The census is already
over-saturated at the ergosphere; therefore the saturation surface
F = 1 lies **strictly outside the ergosphere — at every spin
a ∈ (0, M], every latitude** (checks 3–4; minimum F on the ergosphere
over the full scan: 1.706; minimum clearance of the derived surface
over r_E: 0.25 M). The physical reading writes itself: the ergosphere
is where standing still costs one full reach per Moment azimuthally —
the circulation register alone is full there — so total saturation
must occur farther out, exactly as the static Exclusion floor
saturated before the null horizon could form. **The same floor that
censors the horizon censors the ergoregion.** GR-1f's Kerr-bound
subluminality argument, which the W-D audit flagged as
horizon-evaluated, relocates naturally: the broadcast speed limit
binds at the exclusion surface, where it is a statement about register
capacity rather than about a surface that never forms.

**Corollary (the 3318 question closes).** No exterior ergoregion at
any spin ⇒ no negative-energy modes ⇒ **no ergoregion instability, at
any spin, at any reflectivity.** χ_crit = 2/√7 is retired as a
conservative artifact of the scalar-only proxy; the quadrature can
only ADD census, so the derived surface sits at or outside the proxy
everywhere (check 5: at χ = 0.68 equator, derived 2.267 M vs proxy
2.052 M vs ergosphere 2 M). The extremal case keeps 0.258 M of
clearance (check 6). The "Planck-core bomb" is structurally
unassemblable in CPP — conditional on A1–A3, which is exactly what the
panel round must attack.

## §3 Secondary finding: prograde-ring burial

Surfaced by the verify script's own first run (check 7): at χ = 0.68
the **prograde equatorial photon ring (r ≈ 2.05 M) lies INSIDE the
derived surface (r ≈ 2.27 M)** — the prograde light ring is censored
too, from an onset spin of χ ≈ 0.55. Consequences, registered not
resolved: (i) the prograde-ring cavity is ABSENT at merger-remnant
spins — the eikonal echo structure at χ ≳ 0.55 is retrograde-ring
dominated; (ii) the retrograde template delay at χ = 0.68 is
Δt_ret ≈ 8.59 GM/c³ = **2.62 ms** for GW150914 (vs 7.045 GM/c³ =
2.15 ms Schwarzschild — a +22% spin correction, far from the naive
45% (a/M)² fear and now DERIVED rather than feared); (iii) what a
buried prograde ring does to the m > 0 QNM barrier (which is not the
equatorial ring at finite ℓ) is genuinely open — minted below.

## §4 GR-2 template inputs (eikonal grade, for the paper)

Level-A equatorial static-frame light travel (dt = √g_rr/α dr),
Schwarzschild limit machine-recovered to 4 decimals: for GW150914
(M = 62 ± 4 M_⊙, χ = 0.68): **Δt_ret = 2.62 ms ± 6.5% (mass) ±
eikonal-grade systematic**; amplitude 5% parameter-free (|R| = 1
unchanged — the wall condition derivation is spin-independent);
f_echo ≈ 380 Hz, still in-band. The prograde/retrograde asymmetry is
itself a signature: CPP predicts an echo comb keyed to the RETROGRADE
ring at remnant spins, distinct from horizon-ECO templates keyed to
near-horizon crossing times.

## §5 Honest limits and the round owed

(i) A1–A3 are the reviewable content — especially A3's quadrature
(why not a different composition law?) and A2's identification (why
the ZAMO-frame dragging speed rather than another gravitomagnetic
scalar?). (ii) Eikonal only: the finite-ℓ Kerr (m, ℓ) barrier is not
the equatorial ring; the time-domain Teukolsky solve with the derived
wall is the hardening path. (iii) Zel'dovich SURFACE superradiance
(rotating-reflector amplification without an ergoregion) survives
censorship as a separate, milder channel — bounded rotational-energy
extraction with no known runaway for subcritical surface speeds;
registered, unexplored. (iv) The surface's own dragging (the mirror
co-rotates at ω(r_surf)) is not yet in the template. (v) NOT
panel-reviewed; **CONV-032 owed** covering A1–A3, the theorem, the
prograde-burial finding, and the template grade. No paper edits until
then (GR-1f/1h notes already carry forward-compatible caveats).

**New registry item minted: OPEN-GR-RCORE-3** — the Kerr wall
spectroscopy problem: time-domain (2,2) and (2,−2) evolution on the
derived surface (Dirichlet, co-rotating), echo comb structure, and
the fate of prograde modes above the ring-burial spin.

Verify: `code/3320_kerr_surface_derivation_verify.py` — 8/8.

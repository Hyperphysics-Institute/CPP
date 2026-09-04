# The three owed items on the Love numbers: the axial convention (structural, with a stated 13% extraction uncertainty), the leading spin dependence (through the Kerr surface radius: k₂ −0.080 → −0.087, Λ −7 → −9), and the 5PN phasing (≈ 0.13 rad accumulated near merger — Einstein Telescope / Cosmic Explorer territory). And a recommendation: this is a win candidate for a panel

**Patch 3626, Session 161, 4 Sep 2026.** Verify `code/3626_love_spin_convention_phasing_verify.py` (3/3). Reasoning `reasoning/3626.md`.

## §1 The axial convention
Both Love numbers are defined structurally as the response term relative to the tidal term at the body's radius: electric `H → a r²[1 + 2k₂(R/r)⁵]`, magnetic `h₀ → a r³[1 + 2k₂^B(R/r)⁵]`, i.e. `k = (b/a)/(2R⁵)` from the asymptotic decomposition. For the electric case this agrees with Hinderer's exact closed form to **13%** (the closed form absorbs the `M/r` structure of the exact Legendre solutions that a two-term fit at 300 M does not). The same structural definition gave `k₂^B` at 3625, so **`k₂^B = 0.026–0.030`** with that extraction/convention uncertainty — the sign (positive, opposite to `k₂`) and the order are the content. (Binnington–Poisson's normalization differs by a fixed factor; the corpus states its own.)

## §2 Spin, leading estimate
The surface moves with spin under ansatz A (2.667 M → 2.734 M at χ = 0.68; compactness 0.375 → 0.366). Recomputed with the same `K(R) = 0` condition: **`k₂ = −0.087`, `Λ ≈ −9`** — a 9% change. The Kerr angular couplings (ℓ = 2 ↔ 3 via frame dragging) enter the diagonal ℓ = 2 Love number at O(χ²) and are not computed; flagged. So for GW150914-class remnants the prediction is `Λ ≈ −7 to −9`.

## §3 The 5PN phasing — what a detector sees
Leading tidal term of the stationary-phase inspiral (Flanagan–Hinderer), equal masses (`Λ̃ = Λ`): `ΔΨ = −(3/128η)(39/2)Λ v⁵`. For `Λ = −7.2`: **+0.004 rad at v = 0.2, +0.03 at 0.3, +0.13 rad at v = 0.4** (~67 Hz for a 62 M_⊙ system). A 0.1-rad phase shift is below LIGO–Virgo's sensitivity at SNR ~ 25 (roughly 1 rad) and within Einstein Telescope / Cosmic Explorer reach at SNR of several hundred. The magnetic partner enters at 6PN — negligible.

## §4 Where this leaves the R-core's static signature
| quantity | R-core (a = 0) | R-core (χ = 0.68, surface-radius estimate) | black hole |
|---|---|---|---|
| electric `k₂` | −0.080 | −0.087 | 0 |
| `Λ` | −7 | −9 | 0 |
| magnetic `k₂^B` | +0.026–0.030 | — | 0 |
| tidal phase to v = 0.4 | +0.13 rad | | 0 |

Zero parameters. Derived static equations; a surface condition from the corpus's own static picture; interior response shown to be rigid under A3′.

## §5 Recommendation (economy protocol)
This is a **win candidate** (trigger 1): a zero-parameter, gauge-invariant, static departure from GR that the corpus has not carried before, resting on a derivation the panels have not seen (the static equations; the `K(R) = 0` condition; the rigid-interior argument; the axial matching). A round scoped as a *win-check* — Q1 the static derivation; Q2 the surface condition and its GR-junction reading (the thin shell); Q3 the rigid-interior argument (the sign); Q4 the axial convention and `k₂^B`; Q5 detectability — would convert these into corpus claims or break them. **Not dispatched; the founder's call.** If not, the next unilateral items are the O(χ²) Kerr couplings and the Love-number entry for GR-2's next version.

# Two steps of the plan: (A) for any lossless wall the first echo carries |T_barrier|² ≈ 0.44 of the ringdown at the ringdown frequency, independent of the impedance — so the null results test the surface's existence, and if the limits are below that, the CPP wall must be lossy, which the A3′ two-channel wall supplies; (B) the Kerr (2,−2) line as a family over β at χ = 0.68: 122–188 Hz

**Patch 3614, Session 161, 4 Sep 2026.** Verify `code/3614_reflectivity_and_kerr_family_verify.py` (6/6). Reasoning `reasoning/3614.md`.

## §A What the echo null results actually test

For a **lossless** wall — every constant real β, and every frequency-dependent real law (3378, 3391, 3384) — `|R_wall| = 1`, and the first echo's amplitude relative to the ringdown is set by the **barrier alone**: in, reflect, out, `A₁(ω) ≈ |T_BH(ω)|²`. Computed for the ℓ = 2 Zerilli barrier from the cavity side (flux conserved to 10⁻⁴):

| Mω | Hz (62 M_⊙) | |T|² | |R|² |
|---|---|---|---|
| 0.30 | 156 | 0.055 | 0.945 |
| 0.35 | 182 | 0.27 | 0.73 |
| **0.37** | **193** | **0.44** | 0.56 |
| 0.40 | 208 | 0.69 | 0.31 |
| 0.45 | 235 | 0.93 | 0.07 |

**At the ringdown frequency a lossless wall returns a first echo at ~44% of the ringdown amplitude, whatever its impedance.** The impedance sets the *position and width* of the lines (3613) — how long the train persists — not the first echo's size. So, for lossless walls, the LIGO–Virgo–KAGRA null results test whether a reflecting surface exists at all. If the published amplitude limits at the loudest events lie below ≈ 0.4 (the collaboration's searches report no evidence and set limits of this order — the worker's recollection; the precise numbers must be read from the papers before the excluded region is drawn), then **every lossless wall is disfavoured** at those events, and the CPP wall must be **lossy**: `|R_wall| < 1`. That is not a new assumption — it is what the A3′ two-channel wall (3609–3610) predicts: the traceless `Q_ij` content transmits into the core and returns only after the interior turn-around, so the prompt reflection is reduced. The empirics, read this way, *favour the two-channel wall over the whole lossless family*, including the shipped `X = 0` and the RW-gauge free-surface law. **Reading the limits from the papers is the next mechanical step (worker; a literature fetch is unavailable here, so the numbers are requested from the founder or Isak).**

## §B The Kerr family — (2,−2) at χ = 0.68, SN ladder, ratified surface 2.734 M

| β on the SN function | Mω | Hz | Q |
|---|---|---|---|
| Dirichlet | 0.350 − 0.150i | 182 | 1.2 |
| +0.5 | 0.361 − 0.095i | 188 | 1.9 |
| +0.2 | 0.345 − 0.068i | 180 | 2.6 |
| **0 (Neumann)** | 0.311 − 0.045i | **162** | 3.4 |
| −0.1 | 0.281 − 0.037i | 147 | 3.8 |
| −0.2 | 0.235 − 0.037i | 122 | 3.2 |

**Envelope 122–188 Hz** (plus Dirichlet 182); softer → lower and (through Neumann) sharper, as at a = 0. The shipped 191 Hz (Dirichlet at the *old* surface, 3359) sits at the top of this range; the 3392 "193 Hz" was a strongly frequency-dependent law and is not a point on the constant-β map. **The Kerr numbers are now a family, not an ansatz** — with the surface radius (ansatz A) still the one carried assumption, and the map itself gauge-free.

## §C Standing
- The excluded region: defined (β-independent for lossless walls; the amplitude limit is the whole story) — awaiting the published limit values.
- The theory's own point: the A3′ two-channel wall, lossy by construction — the C5-frame computation (LATTICE-FRAME-1 alongside) places it.
- GR-2 V2.0 = the two maps (a = 0 and χ = 0.68), the barrier transmission, the calibration named as β(ω), and the statement that lossless walls predict A₁ ≈ 0.44 at the ringdown frequency.

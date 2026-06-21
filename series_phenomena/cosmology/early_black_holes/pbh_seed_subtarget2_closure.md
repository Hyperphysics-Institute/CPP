# OPEN-COSMO-PBH-1 — Sub-target 2 closure: the EU-1 spectrum gives NO PBH seeds at LRD scales (NULL)

*Opus computation artifact, 20 June 2026 (single-window worker, 1900-band, Patch 1902). Executes the gating
Sub-target 2 of the OPEN-COSMO-PBH-1 scoping (Patch 1901): map the EU-1 primordial spectrum to a small-scale
amplitude at LRD-seed scales and decide the sign. **Result: NULL with overwhelming margin — the adopted EU-1
spectrum is ~6–7 orders of magnitude in P_R below the PBH-formation amplitude at seed scales; the occupancy-
retention PBH channel produces no LRD seeds. This CLOSES the discriminating-prediction hope and REINFORCES the
Patch 1900 non-discriminating verdict.** Verify: `scripts/1902_pbh_seed_amplitude.py` (all numbers below
reproduce). NO THEO (negative result). NO prediction registered. NO verdict moved.*

## What Sub-target 2 asked, and the honest correction it forced

Sub-target 2 was the load-bearing leg: *pull the 0741/0744 "cliff" into a concrete small-scale σ(M) with its
sign, because that single computation decides whether there is a prediction here at all.* Reading the actual
source (Patches 0741–0742) corrected two things in the Patch 1901 scoping, both against the optimistic reading:

1. **The cliff is not in the adopted spectrum.** Patch 0741's sharp "cliff" (n_s crashing through 0.82 in the
   final ~1 e-fold) was the *rejected* on/off occupancy-fraction model. EU-1 v1.0 ships the *smooth* δN result
   (Patch 0742): `n_s = 1 − 2/N_*` flat across the observable window, `α_s = −2/N_*²`. So the "feature" the
   1901 scoping hoped might enhance small-scale power is not a feature of the spectrum CPP actually adopts.
2. **Where the cliff does exist, it SUPPRESSES, not enhances.** Both the rejected on/off model *and* the adopted
   δN model agree the smallest scales are strongly *red* (the δN tilt `n_s = 1 − 2/N_rem` itself crashes toward
   −∞ as `N_rem → 0`). A red/suppressed small-scale tail is the opposite of the enhancement PBH formation needs.
   **Sign resolved: SUPPRESS.**

Either way the hoped-for hook is gone. The remaining honest question is purely quantitative: even *without* a
feature, is the near-scale-invariant amplitude at seed scales high enough to matter? The computation answers no,
by a colossal margin.

## The computation (verify: `scripts/1902_pbh_seed_amplitude.py`)

Curvature power extrapolated from the CMB pivot with the adopted spectrum,
`P_R(k) = A_s (k/k_*)^{n_s−1 + ½ α_s ln(k/k_*)}`, with `A_s = 2.1×10⁻⁹`, `k_* = 0.05 Mpc⁻¹`. Seed scales
`k ~ 7×10⁵ (M/M_⊙)^{−1/2} Mpc⁻¹`. Rare-tail collapse fraction `β ~ exp(−δ_c²/2σ_δ²)`, `σ_δ ~ √P_R`,
`δ_c = 0.45`:

| M [M_⊙] | k [Mpc⁻¹] | P_R(k) | σ_δ | −ln β |
|---------|-----------|--------|-----|-------|
| 10² | 7.0×10⁴ | 1.2×10⁻⁹ | 3.5×10⁻⁵ | 8.4×10⁷ |
| 10³ | 2.2×10⁴ | 1.3×10⁻⁹ | 3.6×10⁻⁵ | 8.0×10⁷ |
| 10⁴ | 7.0×10³ | 1.3×10⁻⁹ | 3.6×10⁻⁵ | 7.6×10⁷ |
| 10⁵ | 2.2×10³ | 1.4×10⁻⁹ | 3.7×10⁻⁵ | 7.3×10⁷ |

The collapse fraction is `β ~ exp(−8×10⁷)` — not "small," but zero for every operational purpose.

**Even the most generous target survives by 6+ orders of magnitude.** SMBH seeding needs only a tiny abundance;
take a deliberately permissive `β ~ 10⁻²⁰`. That still requires `σ_δ ~ 0.047` (`P_R ~ 2.2×10⁻³`). EU-1 delivers
`σ_δ ~ 3.5×10⁻⁵` (`P_R ~ 1.3×10⁻⁹`) — a **~1.7×10⁶× (≈6.2 orders of magnitude) deficit in P_R**, and a factor
~10⁸ in the exponent `−ln β`.

## Why no sub-target can rescue this

The 1901 decomposition kept Sub-targets 1 (threshold from exclusion dynamics) and 3 (CPP QCD-epoch EoS) as
possible discriminators. Neither can touch this null:

- Both act only on the **O(1) prefactor δ_c** inside the exponent. Dropping `δ_c` from 0.45 to even 0.30 changes
  `−ln β` from ~8×10⁷ to ~3.6×10⁷ — still `exp(−10⁷)`, still exactly zero. You cannot close a ~10⁸ exponent gap
  by adjusting an O(1) threshold; the gap is set by `σ_δ ~ 10⁻⁵` being ~10³× too small, and `−ln β ∝ 1/σ²`.
- **The deficit is generic, not a CPP defect.** It is the textbook reason standard inflation makes no PBHs
  without a dedicated small-scale enhancement (a spike, a step, an inflection). EU-1 has none — it is featureless
  power-law-with-running down to the final-e-fold crash, and the crash is a further *suppression*.

So the null is robust against every lever in the arc.

## Disposition — close the arc; the reframe survives as a null, the prediction does not

**OPEN-COSMO-PBH-1 is recommended CLOSED as a null result**, with this disposition:

- **What dies:** the hope that CPP's distinctive substrate machinery predicts a *primordial* black-hole seed
  population for LRDs. It does not, given the spectrum CPP actually ships. There is no discriminating prediction
  here — Sub-targets 1, 3, 4, 5 are mooted (no point deriving a threshold or a mass function for a channel whose
  amplitude is `exp(−10⁸)`).
- **What survives, and is worth keeping:** (i) the CPP-native *reframe* — a PBH is an occupancy-retention region,
  unifying the PBH channel with the dilution mechanism (1901 §1) — remains a correct and tidy conceptual
  statement; it simply has no phenomenological payload at seed scales. (ii) A genuine, if unsurprising,
  *consistency* statement: **CPP, like ΛCDM, predicts negligible PBHs from the near-scale-invariant spectrum and
  must therefore seed early SMBHs astrophysically (Pop III remnants / direct collapse).**
- **The loop closes cleanly:** this is exactly the Patch 1900 conclusion arrived at from the other direction.
  1900 said the "black hole star" interpretation is non-discriminating because it is accretion-regime astrophysics
  where CPP ≡ ΛCDM. 1902 now shows the one place CPP *might* have differed — primordial seeding — also collapses
  to CPP ≡ ΛCDM. **The two-patch arc's net result: GLIMPSE-17775 / LRDs are fully compatible with CPP and
  genuinely non-discriminating, top to bottom.** That is a clean, defensible, publishable-as-a-null finding —
  not a flagship, but an honest closed loop.

## Honest status

| Item | State |
|------|-------|
| Sub-target 2 (the gate) | **EXECUTED → NULL** (`−ln β ~ 8×10⁷`; ~6–7 orders P_R deficit) |
| Cliff sign | **SUPPRESS** (not enhance); and not in the adopted spectrum anyway |
| 1901 "promising hook" | **withdrawn** on contact with 0741/0742 — the discipline working as intended |
| Sub-targets 1, 3, 4, 5 | **mooted** (cannot close a 10⁸ exponent gap) |
| OPEN-COSMO-PBH-1 | recommend **CLOSE as null**; reframe kept, prediction dropped |
| Relation to 1900 | **REINFORCES** — CPP ≡ ΛCDM on LRD seeding, both channels |
| THEO / prediction / verdict | none; nothing moved |

## Pointers

- `series_phenomena/cosmology/early_black_holes/pbh_seed_mass_function_scoping.md` (Patch 1901) — the scoping this closes.
- `series_phenomena/cosmology/early_universe/glimpse17775_lrd_compatibility.md` (Patch 1900) — the consistency note this reinforces.
- `frontier_sectors/SR.md` Patches 0741 (cliff = rejected on/off model, NO THEO negative) and 0742 (adopted smooth δN tilt `n_s = 1 − 2/N_*`).
- `series_phenomena/cosmology/early_universe/EU-1/` — the shipped spectrum (`A_s`, `n_s`, `α_s`, `N_* ≈ 57`).
- `scripts/1902_pbh_seed_amplitude.py` — this computation.

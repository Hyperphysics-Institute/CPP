# OPEN-COSMO-PBH-1 (proposed): a CPP-native early-black-hole seed mass function from occupancy-retention

*Opus research-target scoping artifact, 20 June 2026 (single-window worker, 1900-band, Patch 1901). Sketch /
Layer-C grade. Sets up the discriminating paper the GLIMPSE-17775 consistency note (Patch 1900) pointed to but
did not contain. **This is a scoping document, not a result: it reframes the problem in CPP-native terms, does
the honest order-of-magnitude scaling, and decomposes the derivation into sub-targets with an effort estimate.
NO THEO, NO prediction registered, NO verdict moved.** Proposed ID OPEN-COSMO-PBH-1; registration into the live
registries (frontier_sectors, future_projects.md) is DEFERRED as the contested step (see foot).*

## The discriminating question

The 1900 consistency note established that the JWST "black hole star" reading of little red dots (LRDs) is
non-discriminating: it lives in the accretion + radiative-transfer regime where CPP ≡ ΛCDM. The genuine,
unanswered question it leaves is:

> **Does CPP's distinctive substrate machinery predict an early-universe black-hole *seed* population — a
> number density and mass function — that differs from the standard astrophysical seeding channels (Pop III
> remnants, direct collapse) and from standard-inflation primordial-black-hole (PBH) formation?**

If yes, the inferred LRD / early-SMBH abundance becomes a *test* of CPP rather than a consistency check. This
document scopes what it would take to get there.

## 1. The CPP-native reframing — a PBH is a region that fails to dilute

CPP already contains, scattered across three threads, exactly the ingredients of a PBH-formation account. The
new content is recognizing they are one mechanism:

- **Expansion = occupancy dilution on a fixed lattice** (founders L33; Patch 0731): the initial Moment is the
  near-100%-occupancy (GP-exclusion-saturated) state; expansion is the occupancy fraction `f` dropping,
  `f ∝ a⁻³`.
- **A black-hole interior = near-100% occupancy** (same founders L33; the saturated limit). c08 recovers the
  exact Schwarzschild exterior; the CP-Exclusion rule floors the interior at `PSR_eff ≥ l_P/2` (no singularity).
- **Therefore a primordial black hole is a co-moving region whose local occupancy *fails to dilute* below a
  retention threshold `f_c` while the background dilutes around it.** Over-dense (over-occupied) patches that
  cross `f_c` at horizon crossing stay saturated and decouple from the dilution flow → they *are* black holes,
  by CPP's own interior definition.

This is the CPP translation of the standard PBH picture (an over-density exceeding the collapse threshold `δ_c`
at horizon crossing collapses to ≈ the horizon mass). It unifies the PBH channel with the *same* dilution
dynamics that drive expansion — a genuinely CPP-native conceptual move, and the part of this target that is
already in hand.

**Prior art to connect, not collide with:** (i) c10 already derives a Planck-remnant evaporation endpoint and
notes a relic-abundance bound; (ii) the Capotauro / chirality arc (Abshier & Grok, Dec 2025) already floats
"PBH formation as low-coherence regions" at lattice nucleation. This target subsumes both: the retention picture
*is* the "low-coherence region" idea made quantitative, and the c10 floor sets the light-end relic boundary.

## 2. Honest first-pass scaling (order of magnitude; the easy, true part)

**(a) Formation mass ≈ horizon mass at retention.** `M_form ≈ c³ t_form / G`. With `c³/G ≈ 4.0×10³⁵ kg s⁻¹`:

| `t_form` | `M_form` | regime |
|----------|----------|--------|
| `~t_P` (5×10⁻⁴⁴ s) | `~m_P ≈ 10⁻³⁸ M_⊙` | the c10 floor (relic, not a seed) |
| `~0.5 ms` | `~10² M_⊙` | light LRD/SMBH seed |
| `~0.5 s` | `~10⁵ M_⊙` | heavy (direct-collapse-equivalent) seed |

So **LRD-relevant seeds (10²–10⁵ M_⊙) require occupancy-retention at `t_form ≈ 0.5 ms – 0.5 s`** — the
pre-BBN, QCD-transition-spanning epoch. This window matters (see 3c).

**(b) The Planck floor is the relic boundary, NOT the seed mass — keep them distinct.** `m_P ≈ 10⁻³⁸ M_⊙` is the
*evaporation endpoint* (c10), and only black holes born below `M_* ≈ 5×10¹¹ kg ≈ 3×10⁻¹⁹ M_⊙` have evaporated
to Planck remnants by today. LRD seeds sit ~20+ orders of magnitude above `M_*`: they never evaporate, so the
c10 floor is irrelevant to them *except* as the endpoint of the unrelated light-relic tail. Conflating the two
would be the obvious error; this is the honesty checkpoint for the whole arc.

**(c) The lever-arm warning (why this is hard, and why it can also be sharp).** PBH abundance is exponentially
sensitive to the perturbation amplitude `σ(M)` and the threshold: a factor-2 in `σ` is orders of magnitude in
number density. The PBH-seed scales (`k ~ 10¹⁵–10²⁰ Mpc⁻¹`) sit ~15–20 decades in `k` below the CMB pivot where
EU-1's `n_s` is anchored. So any prediction here is an *extrapolation across a huge lever arm* and is fragile —
but that fragility is exactly what makes it a sharp discriminator *if* the small-scale input can be pinned.

## 3. Where the discriminating content actually is (and isn't)

**(a) The collapse threshold most likely does NOT discriminate.** Because c08 recovers Schwarzschild collapse
exactly, CPP's retention threshold `f_c` plausibly *reduces to the standard GR collapse threshold* `δ_c ≈ 0.4–0.5`
in the regime that matters. Honest expectation: the threshold is a wash. (Sub-target 1 tests this rather than
assuming it — a surprise here would be a major result, but it should not be the headline bet.)

**(b) The real hook — the EU-1 small-scale spectrum and its end-of-inflation feature.** The discriminating lever
is the *shape of the primordial spectrum at PBH scales*, which is CPP-specific:

- EU-1 pre-registers `(n_s, α_s) = (0.9649, −0.00062)` at CMB scales. Extrapolated 15–20 decades with that
  running, the small-scale amplitude is a definite CPP number to compare against the ΛCDM power-law assumption.
- More sharply: the 0741/0744 findings showed CPP's spectrum **steepens into a "cliff" in the final ~1 e-fold**
  (`n_s` crashing through 0.82 toward negative as the occupancy fraction `f` runs off at the unstacking exit).
  A spectral feature at the smallest scales is precisely what can *imprint a characteristic PBH mass*. ΛCDM
  inflation is featureless power-law there unless a model is bolted on — so a CPP-native end-of-inflation cliff
  mapping to a characteristic seed mass is the most promising discriminator in this arc. (Caveat: 0741 read the
  cliff as a *tension* for `n_s`; here the same feature is repurposed as a small-scale prediction. Whether the
  cliff *enhances* or *suppresses* power at the seed scale is the sign question Sub-target 2 must settle — it
  could equally predict a PBH-seed *deficit*, which would be falsified by a confirmed abundant LRD-seed
  population. Either sign is a real, falsifiable prediction.)

**(c) The QCD-epoch equation of state — a second, independent CPP hook.** Standard PBH work gets a ~1 M_⊙ bump
because the QCD crossover softens `w` and lowers the collapse threshold near `t ~ 10⁻⁵ s`. CPP has its own
strong-sector substrate story (SS series; qDP/hTetra freeze-out). If CPP's `w(T)` through the QCD epoch differs
from the lattice-QCD-calibrated standard one, the enhancement shifts in mass and amplitude — and the seed window
(3a) straddles exactly this epoch. Independent of the spectrum lever.

**(d) Dark-sector cross-link (DM-3).** The retention regions accrete qDP/hTetra first (the DM accretion-era map,
2026-06-10 speculation note); whether the resulting early-seed haloes carry a discriminating profile connects to
the already-scoped DM-3 discriminating-halo track.

## 4. Derivation sub-targets (the actual work; honest effort estimate)

| # | Sub-target | Delivers | Risk |
|---|-----------|----------|------|
| 1 | Derive the retention threshold `f_c` from CP-Exclusion / dilution dynamics; test whether it reduces to GR `δ_c` | threshold (discriminating or wash) | likely wash (3a) |
| 2 | Map the EU-1 spectrum + 0741/0744 cliff to small-scale `σ(M)` at seed scales, **with sign** | `σ(M)` curve; enhance-or-suppress verdict | HIGH (lever arm, cliff sign) |
| 3 | CPP `w(T)` through the QCD epoch vs standard; threshold shift | mass/amplitude of any seed bump | medium (needs SS-sector input) |
| 4 | Assemble `dn/dM` (press-Schechter-style) from `σ(M)` + threshold; propagate to a *seed number density* at `M = 10²–10⁵ M_⊙` | the falsifiable prediction | gated on 1–3 |
| 5 | Confront against inferred LRD / early-SMBH abundance; state the falsifier | the test | gated on 4 |

**Honest effort estimate: ~6–10 sessions to a v0.1 `.tex`, gated on Sub-target 2** (the spectrum lever is the
load-bearing, highest-risk leg; if the cliff sign is ambiguous or the extrapolation is too fragile to pin, the
arc yields a *bounded* statement rather than a point prediction — still publishable, but as a constraint, not a
match). This is a real research arc, not a write-up.

## 5. Go / no-go recommendation

**GO — but as a derivation arc, not a paper draft.** It is worth pursuing because, unlike the 1900 consistency
note, it has a genuine path to a *discriminating, falsifiable* CPP prediction (the small-scale spectrum lever in
3b is CPP-specific and ΛCDM has no counterpart there). It is honestly risk-flagged: the threshold is probably a
wash (3a), and the prediction is lever-arm-fragile (2c) — so the headline should track the spectrum feature, and
the deliverable may be a constraint rather than a match. The first real move is **Sub-target 2**: pull the
0741/0744 cliff into a concrete small-scale `σ(M)` with its sign, because that single computation decides whether
there is a prediction here at all.

## Honest status

| Item | State |
|------|-------|
| This document | scoping / Layer-C; reframing + scaling + decomposition only |
| CPP-native reframing (PBH = occupancy-retention) | in hand (conceptual; unifies 0731 + c10 + Capotauro low-coherence) |
| Discriminating prediction | **NOT derived** — gated on Sub-target 2 (spectrum lever, HIGH risk) |
| Proposed ID | OPEN-COSMO-PBH-1 (free in the COSMO space; **registration deferred**) |
| THEO / prediction / verdict | none; nothing moved |

## Pointers

- `series_phenomena/cosmology/early_universe/glimpse17775_lrd_compatibility.md` (Patch 1900) — the consistency
  note this target answers.
- `series_phenomena/cosmology/early_universe/lattice_growth_escape_closure.md`, `step1_scaling_phase_kill.md` —
  the dilution-on-fixed-lattice mechanism (0729/0731).
- `frontier_sectors/SR.md` rolloff entries (Patches 0741/0744/0745/0746) — the end-of-inflation spectral cliff.
- `series_phenomena/cosmology/early_universe/EU-1/` — `n_s`, `α_s`, the spectrum to extrapolate.
- `series_relativity/SR_companion_papers/c10_Hawking_Radiation_and_the_Planck_Remnant/` — Planck floor + relic bound.
- `series_umbrella/series_substrate_chirality_arc/capotauro/` — the "PBH as low-coherence region" prior art.
- `founders_vision/physical_metaphysical_speculation/2026-06-10_DM_accretion_era_map_and_qDP_eDP_buffering.md` — DM-3 cross-link.

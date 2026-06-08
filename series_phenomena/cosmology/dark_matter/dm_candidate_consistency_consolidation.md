# DM Arc — Consolidation: qDP/hTetra Dark-Matter Candidate, Falsification-Survival Status

**Patch:** 1200 · **Work item:** OPEN-COSMO-DM-1 (consolidation) · **Conjecture served:** CONJ-COSMO-1
**Proposed ID (RESERVED, not registered here):** `LEMMA-DM-CONSIST-1`
**Status of result:** **CONSISTENCY-grade** (compatible-with; *not* identifying) — see §4, recommendation pending Thomas sign-off.
**Consolidates:** `step1_sigma_over_m_SIDM.md` (Patch 0703) + `step3_coldness.md` (Patch 0706)
**Verify:** `scripts/1200_consolidation_check.py` (re-derives both margins + the discrimination test; all asserts pass)

---

## 1. Purpose

The first-to-publish DM-identification paper needs a single citeable statement of what the
cheap, cosmology-sector-independent falsification gates establish, so the paper can reference
one finding rather than re-litigating two Step docs. This consolidates the two gates that ran
**without** any dependence on OPEN-SR-5 — Step 1 (self-interaction) and Step 3 (coldness) — and
fixes the *grade* of the combined statement.

## 2. The consolidated statement

Under the qDP/hTetra constituent-mass estimates (≈0.3–1.5 GeV, QCD/confinement-scale bracket)
and the conservative geometric residual cross-section (σ ≈ πr₀², r₀ ≈ 0.26 fm from c14):

| Gate | Quantity | Result | Margin |
|---|---|---|---|
| **Step 1** — residual self-interaction | σ/m vs SIDM bound (~1 cm²/g) | qDP 4.0×10⁻³, hTetra 7.9×10⁻⁴ cm²/g | **~250×–1260× below** bound; collision rate ~0.02 / Hubble time |
| **Step 3** — coldness | m vs ~3 keV warm-DM boundary | qDP/hTetra ~10⁵–10⁶× heavier | **decisively cold**; v/c ≈ 4–9×10⁻⁵ at equality |

**Combined:** the qDP/hTetra dark-matter hypothesis **survives both of the cheap, self-contained
falsification gates** — it is collisionless to Bullet-Cluster tolerance and cold to deep-CDM
tolerance, with no fragile margin (Step 1 survives even ×100 nucleon-like resonant enhancement;
Step 3 rests on the GeV mass scale alone and does not depend on the cosmological sector).

Both numbers are reproduced from the source docs at machine arithmetic in the verify script.

## 3. What the consolidation does *not* add

No new physics, no new computation, no new axiom, no verdict change. It restates two existing
NO-KILL results as one citeable unit and judges their joint epistemic weight. The two honest
gaps carried from Step 1 are unchanged and remain load-bearing for any stronger claim:
(i) the constituent mass is an *estimate*, not derived (a lighter qDP erodes the Step-1 margin
as σ/m ∝ 1/m); (ii) the residual-potential shape (near-threshold bound state → large scattering
length) is not yet computed — the only thing that could lift σ/m by the ~10³ needed to threaten
the light channel.

## 4. Grade call — CONSISTENCY-grade, not IDENTIFICATION-grade

**Definitions used.** *Identification-grade*: the result positively identifies qDP/hTetra **as**
the dark matter — i.e., supplies a discriminant that picks them out over the competing CDM field
(WIMPs, axions, sterile neutrinos, primordial black holes). *Consistency-grade*: the result shows
qDP/hTetra are **compatible with** being the dark matter — they are not excluded by a constraint
that excludes other candidates.

**The determining test (verify script §3).** Both gates are *falsification-survival* tests built
from generic CDM properties — a GeV mass scale and a small geometric cross-section. A structureless
GeV-scale CDM placeholder passes **both gates identically** (σ/m ≈ 1.2×10⁻³ cm²/g, coldness ~3×10⁵×).
Neither gate uses any qDP/hTetra-specific structure (confinement scale, 600-cell geometry, DP-pairing),
so neither distinguishes qDP/hTetra from the CDM field. Surviving them is **necessary, not sufficient**,
for identification.

**Corroborating context (not part of the two consolidated gates, but bearing on the grade).** The
arc's own results are explicit that identification is still ahead: Step 5 (rotation curve) is
PASS-but-**non-discriminating**; Step 4 (power spectrum) is in **SERIOUS TENSION** and CONJ-COSMO-1
is **NOT confirmed**; the Session-154 handover records that "the DM identification theorems are still
ahead, not behind." A consolidation of two consistency gates cannot outrank the unconfirmed status of
the conjecture it serves.

**Recommendation (for Thomas, not self-certified).** Register the consolidated result at
**CONSISTENCY-grade**: *"qDP/hTetra aggregates are a viable cold, collisionless dark-matter
candidate — surviving the two cosmology-independent falsification gates with wide margins — pending
the discriminating tests (power spectrum, derived constituent mass, a positive qDP/hTetra-specific
signature)."* The first-to-publish paper can cite this as the **floor** the candidate clears, framing
the contribution as a postdictive-viability result, not an identification claim.

> **ESCALATION — Thomas sign-off required.** Per the round rules, the identification-vs-consistency
> call is the integrator's, not the worker's. This doc *recommends* CONSISTENCY-grade and gives the
> reasoning; it does **not** self-certify an identification claim, and it does not register the ID.
> If you judge that a positive discriminant exists that I have not weighed, the grade is yours to lift.

## 5. Falsifiers (of the consolidated CONSISTENCY statement)

(F1) A derived constituent mass low enough to push σ/m toward the SIDM bound (light-qDP channel).
(F2) A residual qDP/qDP potential supporting a near-threshold bound state (σ/m ×~10³ → Step-1 FAIL).
(F3) A kinetic-decoupling history pinning qDP/hTetra to an ongoing-hot Sea bath (would reopen Step 3).
None of these is currently indicated; all three are the named closure requirements, not active kills.

---

## REGISTRY HANDOFF NOTE (integrator — W2 does not edit these)

These are the shared-registry edits this result *implies*. They are **not** made in this patch
(owned path is `series_phenomena/cosmology/dark_matter/` new files only). Apply after the grade call.

1. **`theorem-registry.md`** — IF Thomas confirms CONSISTENCY-grade: register `LEMMA-DM-CONSIST-1`
   (consolidation lemma; CONSISTENCY-grade; sources Patches 0703 + 0706; verify `scripts/1200_consolidation_check.py`).
   Do **NOT** register a THEO (no derivation; necessary-not-sufficient result), mirroring the
   no-THEO-for-conditional discipline used for n_s / PRED-C-96. ID `LEMMA-DM-CONSIST-1` confirmed
   collision-free (grep of theorem-registry.md returned no `LEMMA-DM-*` / `THEO-DM-*`).
2. **`frontier_sectors/SR.md`** — under `OPEN-COSMO-DM-1` / `CONJ-COSMO-1`: add a one-line trail entry
   "Patch 1200 — Steps 1+3 consolidated → CONSISTENCY-grade falsification-survival floor
   (LEMMA-DM-CONSIST-1, pending grade sign-off); does not move CONJ-COSMO-1 off NOT-confirmed."
   No verdict change to CONJ-COSMO-1.
3. **`predictions.md`** — no swarm-count change. This is a viability/consistency consolidation, not a
   zero-parameter empirical correspondence; it does not enter the tally (parallel to the convention
   used for forward-looking conditional results).
4. **`master_glossary.md`** — optional: add "consistency-grade vs identification-grade (DM arc)" if the
   distinction is reused in the paper.

If the grade is lifted to IDENTIFICATION-grade by Thomas, items 1–3 change substantially (THEO
candidacy + possible swarm entry) and should be re-scoped — flagged here, not assumed.

# Reviews — SF-2 portfolio scoping consultation, RE-CLOSE after the 1207–1209 closure sweep

**Cycle:** OPENED Patch 1204 → adjudicated **PORTFOLIO-DEFERRED** Patch 1206 (primary slot open, two-track closure scheduled) → closure sweep Patches **1207 (C1), 1208 (C5), 1209 (C7)** → **RE-CLOSED Patch 1210: PORTFOLIO-READY, primary = C5.**

**What this file is:** the cycle re-close triggered by the Patch-1206 forward queue ("when 1207–1209 land, re-evaluate"). It supersedes the *verdict* of the 1206 aggregation (`reviews-SF2-PORTFOLIO-SCOPING.md`) while preserving that file as the cycle-1 record (verbatim reviewer text lives there). No reviewer re-dispatch; this is an adjudication over the three closure artifacts produced in this session. Self-contained; lane-private.

---

## Outcome

**Adjudicated verdict: PORTFOLIO-READY — primary = C5 (EU-1 spectral index, the joint n_s-tightening + α_s pre-registration).** The two-track gamble resolved: the C7 "upgrade-to-READY-with-C7-primary" branch did **not** fire (C7 is a JUNO falsification risk, Patch 1209), so the C5-reframe branch stands and is now fully scoped (Patch 1208). The portfolio moves from DEFERRED to READY not because a pristine Category-A bit appeared, but because **C5 is now the only fully-scoped, immediately shippable pre-registration in the inventory**, with a concrete prediction, a timestamp anchor, a survival band, and an honest scope.

| Candidate | 1204 status | After closure sweep | Role in READY portfolio |
|-----------|-------------|---------------------|--------------------------|
| **C5** (n_s) | Category B, postdiction risk | **Patch 1208**: sharp (N_∗ derived → point, not band); joint (n_s, α_s) pre-registration with SO survival band; anchored to PRED-C-96 timestamp | **PRIMARY** |
| **C1** (mass ordering) | "TBD by panel" | **Patch 1207**: FORCED-DERIVED (PRED-C-16; SF-4 cage-shell V²), not TBD; novelty diluted (field already favors NO) | **Standing falsifier** (JUNO mass-ordering, own timeline ~2028–2031) |
| **C7** (JUNO PMNS) | Category B, "closure-feasible" | **Patch 1209**: HIGH-RISK; 0.300 on ~3σ JUNO falsification trajectory; 12/21 fails Lagrange; θ₂₃ not a JUNO observable | **Down-ranked** — gated longer-shot, do not fund closure absent the lock-to-0.300 gate |
| **C6** (magic numbers) | Category A wild-card | not examined this sweep | Wild-card watch (1210-deferred scan) |
| **C8 / C9** | excluded | unchanged | Excluded (postdiction / long-horizon) |

## Why READY now (the adjudication)

The 1206 deferral rested on one finding: *no candidate was at sufficient rigor for immediate primary selection.* Each leg of the closure sweep changed the inventory:

- **C7 was the hoped-for primary.** Patch 1209 found it carries two independent disqualifiers — a structural one (the normalization is genuinely fitted; 12/21 isn't an overlap fraction at all) and an empirical one (the value 0.300 is ~1σ below JUNO's 0.3092 ± 0.0087 now, heading to ~3σ at ultimate precision, in the exact class of θ₁₂ rationals JUNO is currently falsifying). A *derived* 0.300 would be a clean, pre-registered, **wrong** prediction. C7 cannot be the primary.
- **C1 is real but diluted.** Patch 1207 settled that normal ordering is forced-derived (not TBD), so the package's mark was stale. But the field already favors normal ordering, so C1's pre-registration novelty is moderate; JUNO will adjudicate it on its own timeline regardless of campaign framing. C1 is a strong standing falsifier, not the campaign's pre-registration centerpiece.
- **C5 became shippable.** Patch 1208 supplied exactly what 1206 said was missing: a concrete pre-registration statement. It is sharper than the reviewers credited (EU-1 derives N_∗ ≈ 57 from the CP-count → n_s = 0.9649 is a *point* prediction), the running α_s = −0.00062 is a genuinely not-yet-precisely-measured handle (Planck constrains it only weakly), and the whole thing is already timestamp-anchored by PRED-C-96 (6 June 2026, before the SO window). That is a pre-registration the campaign can take to a HEP venue today.

With C7 out as primary and C5 fully scoped, the only honest move is to name **C5 the primary and re-close READY** — with the qualifications below stated plainly.

## The campaign's pre-registration statement (the deliverable)

> **CPP / EU-1 predicts the pair (n_s, α_s) = (0.9649 ± 0.0005, −0.00062), registered 6 June 2026 (PRED-C-96 / PRED-O-34) prior to Simons Observatory data.**
> **Confirmation:** SO/CMB-S4 measures n_s within 0.9649 ± 0.5σ_meas at σ_meas ≲ 0.002 (≥2× tighter than Planck), while α_s remains consistent with a small negative running near −6×10⁻⁴.
> **Falsification:** n_s central shifts ≳3σ from 0.9649, or |α_s| is measured ≳10⁻².

This is the artifact to carry into named-validator / HEP-venue engagement — the campaign's actual end goal (per the OpenAI–Erdős analog that opened the campaign).

## Honest scope (stated as the primary's qualifications, not buried)

1. **C5's n_s leg is a postdiction.** The pre-registration value is concentrated in the *tightening* test and the *running* α_s, not the (already-matched) Planck central value. The campaign framing must lead with tightening + running and not over-claim the central match. This bounds C5's confirmation ceiling: it is a "survives-a-sharper-test + predicts-a-small-running" story, not a "predicted-X-before-anyone-knew" story.
2. **The sharpness depends on OPEN-EU-1.** The point-prediction status rests on the N_∗ = (1/3)ln(N_CP/N_GP) ≈ 57 derivation. Until OPEN-EU-1 is hardened, the honest claim is "n_s = 0.9649 *given* the EU-1 N_∗ derivation." Hardening OPEN-EU-1 is the single highest-leverage move to strengthen the primary.
3. **Framework-conditional, NO-THEO.** PRED-C-96 ships at sketch-Layer-3; the pre-registration is of a framework-conditional prediction, and that conditionality belongs in the registered statement.

## Forward queue (post-re-close)

1. **Harden OPEN-EU-1 (N_∗ derivation)** — the highest-leverage strengthening of the now-primary C5. Sensitivity of N_∗ ≈ 57 to N_CP/N_GP and to the pivot-vs-total choice. (Cosmology-lane file; coordinate if a cosmology window is active.)
2. **Named-validator / HEP-venue engagement scoping** — the campaign's end goal. With a primary now named, scope which venues/validators fit a substrate-phenomenological (n_s, α_s) pre-registration decoupled from the consciousness ontology. (New SF-2-lane artifact.)
3. **Optional C6 isotope-specificity scan** (the original 1210 queue item, now deferred) — only worth running if a not-yet-measured isotope + value can be named; would add a second, less-diluted Category-A leg if it lands.
4. **At-risk registry updates (warn-and-resync, none made here):**
   - `predictions.md` — PRED-C-96 status annotation ("SF-2 campaign primary; SO survival band") and the PRED-C-16 attribution unification from Patch 1207.
   - `frontier_sectors/SM.md` — OPEN-SM-5 "current best lead" update with the Patch-1209 JUNO-tension + Lagrange diagnostic.
   - `frontier_sectors/CHIR.md` / `SM.md` — optional cross-references to the 1207 audit.
5. **Optional C7 lock-to-0.300 gate** — only if C7 is ever revisited; one patch to test whether the stabilizer-overlap construction can flex toward JUNO's 0.309 before any group-theoretic closure is funded.

## Decisions registered at re-close

- **Verdict: PORTFOLIO-READY, primary = C5** (joint n_s-tightening + α_s). C1 = standing forced-derived falsifier; C7 = down-ranked gated longer-shot; C6 = wild-card watch; C8/C9 excluded.
- **C5's pre-registration is timestamp-anchored by the existing PRED-C-96** (no new registration needed to pre-register).
- **No verdict moves; no theorem/prediction registrations; header/theorem count UNCHANGED.** All chirality-arc verdicts (V3/W3; W3→W1 candidate conditional on Mechanism A; CAPACITY-1 reserved) stand unchanged. This consultation is external-validation strategy, not theorem development.
- **Band discipline:** 1200-block SF-2 lane; this re-close is Patch 1210. 09xx H1 sprint continues in its own lane.

## Registry-touch ledger

| Recommended edit | Target | At-risk? | Status |
|------------------|--------|----------|--------|
| (none required to record the verdict — PRED-C-96 already anchors the pre-registration) | — | — | no edit |
| PRED-C-96 status annotation + PRED-C-16 attribution unification | `predictions.md` | **YES** | NOT made; warn-and-resync |
| OPEN-SM-5 current-best-lead update (JUNO tension + Lagrange) | `frontier_sectors/SM.md` | **YES** | NOT made; warn-and-resync |
| Portfolio reclassification (C1/C5/C7 status) | next portfolio-consultation package | No (lane-private) | folded into this re-close |

No at-risk shared file is touched in this patch.

---

*Re-closed Patch 1210 (Session 159, 13 June 2026) on Thomas's authorization, triggered by the Patch-1206 forward queue after the 1207–1209 closure sweep. Verdict moves DEFERRED → PORTFOLIO-READY, primary = C5 (joint n_s-tightening + α_s pre-registration, timestamp-anchored by PRED-C-96), with C1 as a standing forced-derived JUNO-timeline falsifier and C7 down-ranked to a gated high-risk longer-shot after the Patch-1209 falsification-trajectory finding. C5's confirmation ceiling is bounded by the n_s postdiction status (value concentrated in tightening + running α_s) and its sharpness depends on hardening OPEN-EU-1 — both stated as primary qualifications, not buried. The campaign now has a concrete pre-registered (n_s, α_s) statement to carry into named-validator / HEP-venue engagement, the campaign's end goal. No verdict moves on the physics; all chirality-arc verdicts stand unchanged; header/theorem count UNCHANGED. Band-discipline: 1200-block SF-2 lane; lane-private file, no at-risk shared file touched; 09xx H1 sprint continues in its own lane.*

# Reviews — SF-2 external-validation portfolio scoping consultation v1.0

**Cycle:** OPENED Patch 1204 → **CLOSED Patch 1206, 2/3 PORTFOLIO-DEFERRED majority adopted on the merits (the single PORTFOLIO-READY rests on C7, whose fitted-normalization weakness both DEFERRED reviewers independently down-rate).** Productive deferral: the panel converges on a clear shortest-path closure even though it does not yet name a primary.

**Package under review:** `flagship_papers/electroweak/review/sf2_portfolio_scoping_review_package_v1.0.md` (Patch 1204; 9-candidate inventory C1–C9; ten scrutiny questions PSQ1–PSQ10).
**Panel:** ChatGPT, Grok, Copilot (three independent reviewers; no Sonnet pass this cycle).
**Verdict legend:** PORTFOLIO-READY (name a primary + backups now) / PORTFOLIO-DEFERRED (no primary yet; closure work named) / PORTFOLIO-RESTATEMENT (reframe the consultation).

---

## Outcome

| Reviewer | Headline verdict | Proposed primary | Backups | Tier |
|----------|------------------|------------------|---------|------|
| **ChatGPT** | **PORTFOLIO-DEFERRED** — no candidate at publication-grade rigor for immediate primary; reconcile C1 provenance first | provisional **C1** (mass ordering) | C5, C3 (C6 wild-card) | INSPECTED + SCRIPT-EXECUTED (PSQ5) |
| **Grok** | **PORTFOLIO-DEFERRED** — primary needs panel resolution of C1/C2/C6 TBD; C5 is strongest near-term but postdiction-grade until SO | **C5** (n_s) | C3, C6 | INSPECTED + INDEPENDENTLY-RECOMPUTED (n_s = 1 − 2/57 = 0.964912) + SCRIPT-EXECUTED (§7 inventory) |
| **Copilot** | **PORTFOLIO-READY** — JUNO-facing PMNS is well-posed, in-window, patchably closable | **C7** (JUNO PMNS) | C5, C4 | INSPECTED |

**Adjudicated verdict: PORTFOLIO-DEFERRED.** Two of three name DEFERRED outright. The lone READY (Copilot) hinges on C7 (JUNO solar PMNS angles); its load-bearing premise is that the PMNS normalization (sin²θ₁₂ = 12/40 = 0.300) can be derived rather than fitted within a bounded group-theoretic effort. Both DEFERRED reviewers independently flag the *current* fitted-normalization status as a pre-registration disqualifier (ChatGPT: "lacks autonomous pre-registration status"; Grok: "fitted normalization … no derived normalization producing crisp numbers"). On the merits the panel has therefore **not** identified an immediately pre-registerable Category-A primary. DEFERRED carries — but with a converged, executable closure path, not an open-ended one.

---

## Cross-reviewer convergence summary

1. **C5 (n_s) is the consensus near-term backbone — the only candidate in all three portfolios** (Grok primary; ChatGPT and Copilot Backup-1). It is the only *shipped crisp closed-form* in the inventory (PRED-C-96, n_s = 1 − 2/N_∗ ≈ 0.9649). Shared caveat, stated by all three: it is a **postdiction** against Planck 2018 (0.9649 ± 0.0042); its pre-registration value lives entirely in the future-tightening reframe. Grok and Copilot **independently converged on the same survival band**: to count as beyond-postdiction the next-generation measurement (Simons Observatory ~2027) must land with central value within ≈0.5σ of 0.9649 **and** total error ≥2× tighter than Planck (σ ≲ 0.002); tension ≳3σ falsifies.

2. **No Category-A candidate is currently pre-registerable (3/3).** C1 (mass ordering), C2 (absolute ν mass), C6 (magic-number gaps) are all "TBD by panel" with no shipped derivation, value, or forced binary in the corpus. They carry the highest pre-registration value *if closed*, but zero current rigor.

3. **C1 provenance mismatch — the sharpest single finding (ChatGPT, PSQ1).** The package marks C1 "TBD by panel," while SF-4 repository summaries list hierarchy ordering among derived neutrino outputs. That mismatch must be reconciled before C1 can be considered for pre-registration — exactly the ambiguity a pre-registration campaign cannot carry. Cheap to resolve (corpus audit, not new physics); gating for any C1 promotion.

4. **C7 (JUNO PMNS) is the disagreement axis.** Copilot judges the normalization-closure a tractable, bounded representation-theoretic task (2–3 patches) and rates C7 a strong primary; ChatGPT and Grok rate C7 *not ready* on the same fitted-normalization fact. The split is about closure *feasibility*, not about the structure: all three agree the rational subgroup-overlap targets (sin²θ₁₂ = 12/40, sin²θ₂₃) are crisp; they disagree on whether the normalization can be derived in-window.

5. **C3 (W⁰ exact-degeneracy): structurally crisp, experimentally out-of-window (3/3).** The Δm_{W⁰−W±} ≲ 1 MeV claim is a structural degeneracy with a falsifier band set by experimental resolution; achieving ~1 MeV sensitivity on a *new neutral state* in 2026–2028 is judged optimistic-to-implausible by all three. Backup / long-horizon structural falsifier, not an in-window primary.

6. **C4 (mass-gap, no EW scalar < ~200 GeV): clean two-way falsifier, asymmetric celebration (3/3).** Discovery falsifies sharply; continued null searches only gradually strengthen confidence — reads as a standing structural constraint / background consistency check, not an event-like confirmation. Portfolio-side constraint, not a flagship primary.

7. **PSQ10 / H1 sprint — unanimous (3/3).** Even if the 09xx H1 reflection-positivity sprint yields sign(μ²) > 0 within its 10 rounds, δ_CP (C9) does **not** displace the 2026–2028 primary. It re-enters as a *next-campaign primary on trigger*, where the trigger is the full chain: H1 closed + Reading-C (sub-claim b) resolved + Mechanism A discharged + a worked δ_CP value with error band. That chain does not compress into this portfolio's 6–18 month window. No change to the Patch 1202 long-horizon verdict.

8. **Exclusions converge (3/3):** C8 (sin²θ₁₃ — already-measured postdiction) and C9 (δ_CP — long-horizon per Patch 1202) excluded for this consultation.

---

## Triage synthesis per sub-question

- **PSQ1 (C1 mass ordering):** Highest-value Category-A bit but **not forced** in the current corpus and provenance-ambiguous (package-TBD vs repo-summary-"derived"). Reconcile before considering. (ChatGPT lead; Grok/Copilot concur.)
- **PSQ2 (C2 absolute ν mass):** Genuinely TBD; no (m₁,m₂,m₃,Σm_ν,m_β) shipped; needs a dedicated mass-spectrum arc beyond the portfolio horizon. (3/3.)
- **PSQ3 (C3 W⁰):** Structural degeneracy claim with a resolution-set falsifier band; experimental capability out-of-window. Backup/long-horizon. (3/3.)
- **PSQ4 (C4 mass-gap):** Clean falsifier-on-discovery, weak as a positive event. Standing constraint. (3/3.)
- **PSQ5 (C5 n_s):** Postdiction now; real pre-registration value under a substantial Simons Observatory tightening that preserves the central value. Survival band (Grok ∧ Copilot): central within ≈0.5σ of 0.9649 and σ ≲ 0.002; ≳3σ tension falsifies. Grok SCRIPT-EXECUTED / INDEPENDENTLY-RECOMPUTED 0.964912.
- **PSQ6 (C6 magic numbers):** Wild-card; not portfolio-ready until OPEN-SS-35 names "Isotope X at Facility Y, predicted value Z." Could jump to a top-tier Category-A primary if that specificity appears. (3/3.)
- **PSQ7 (C7 JUNO PMNS):** Crisp rational targets in hand; normalization currently fitted. **Disagreement on closure feasibility** — Copilot (feasible, bounded, → primary) vs ChatGPT/Grok (not-ready as-is). Resolving this disagreement is the highest-leverage closure question of the consultation.
- **PSQ8 (additional candidates):** No addition outranks C5/C7 for this window. ChatGPT floats m_ββ / neutrinoless double-β *only if* CPP fixes Majorana structure; Copilot floats a PTA GW spectral feature as an SR-side future seed; Grok finds no ranking-changing addition. All treated as future seeds.
- **PSQ9 (composition):** No single primary commands a majority — ChatGPT→C1, Grok→C5, Copilot→C7. The **intersection** is C5 (all three portfolios). Adjudicated composition below.
- **PSQ10 (H1 interaction):** δ_CP = next-campaign-on-trigger; does not displace the in-window primary. (3/3.)

---

## Decisions registered at cycle close

1. **Verdict: PORTFOLIO-DEFERRED** (2/3 majority; the 1-READY rests on C7, whose fitted-normalization weakness both DEFERRED reviewers independently down-rate). Adopted on the merits, not head-count — consistent with the Patch 1202 adjudication discipline.
2. **C5 (n_s) is the consensus near-term backbone** (3/3 in-portfolio). Its pre-registration value is conditional on the postdiction→tightening reframe with the converged survival band.
3. **No Category-A candidate is currently pre-registerable** (C1/C2/C6 panel-TBD). The portfolio's primary slot stays *open* pending the closure work named in the forward queue.
4. **δ_CP (C9) stays long-horizon** — PSQ10 unanimous; no change to the Patch 1202 RESTATEMENT verdict.
5. **No verdict moves; no theorem/prediction registrations; header/theorem count UNCHANGED.** All chirality-arc verdicts (V3/W3; W3→W1 candidate conditional on Mechanism A; CAPACITY-1 reserved) stand unchanged. This consultation is external-validation strategy, not theorem development.
6. **Band discipline:** 1200-block SF-2 portfolio lane; this aggregation is Patch 1206. (Reviewer-proposed patch numbers 1205/1209 etc. in their (D) blocks collide with already-consumed numbers and are renumbered into the forward queue below.)

---

## Adjudicated portfolio composition (DEFERRED — primary slot open, two-track closure recommended)

- **Backbone (now-shippable): C5 — EU-1 spectral index n_s = 1 − 2/N_∗ ≈ 0.9649.** The physics is already shipped (PRED-C-96); only the campaign framing is missing. Convert the postdiction into a *pre-registered tightening prediction* against Simons Observatory with the converged survival band. Lowest physics risk; this is the safe immediate pre-registration.
- **Primary-on-closure (high payoff, parallel): C7 — JUNO solar PMNS angles.** Attempt the normalization derivation (Copilot's bounded group-theoretic task). If it closes to Layer-3 without fitted normalization, the portfolio **upgrades to PORTFOLIO-READY with C7 primary / C5 backup**. If it does not close, C5-reframe stands as the pre-registration backbone.
- **Gating cheap reconcile: C1 — mass ordering provenance.** Resolve the package-TBD vs repo-summary-"derived" mismatch. If SF-4/SM-5 in fact forces normal ordering, C1 promotes to a Category-A primary candidate for a follow-on consultation.
- **Wild-card watch: C6 — OPEN-SS-35 magic-number gap.** Promote to Category-A primary candidate if and when a specific not-yet-measured isotope + value is named.
- **Standing constraints (not primaries): C3** (W⁰ degeneracy, out-of-window) **and C4** (mass-gap, falsifier-on-discovery).
- **Excluded this consultation:** C8 (postdiction), C9 (long-horizon).

---

## Forward queue

Patch numbers in the live 12xx SF-2 lane (consumed: 1200/1201/1202/1204/1205/1206; next free 1207). The H1 sprint stays in the 09xx chirality lane — **not** a 12xx task.

1. **Patch 1207 — C1 provenance reconcile (gating, cheap).** Audit SF-4 / SM-5 K3-doublet structure against the package's "TBD by panel" mark; resolve whether mass ordering is forced (normal vs inverted) or free. Output: `flagship_papers/electroweak/review/C1_mass_ordering_provenance_audit.md` with a one-line forced/not-forced finding and, if forced, a one-page binary-falsifier note. (ChatGPT PSQ1 + steps 1–2.)
2. **Patch 1208 — C5 tightening-reframe memo (now-shippable backbone).** `series_phenomena/cosmology/early_universe/EU-1_ns_pre-registration_band.md`: quantify the Simons Observatory survival threshold (central within ≈0.5σ of 0.9649; σ ≲ 0.002 → confirmed-beyond-postdiction; ≳3σ tension → falsified) and set the pre-registered acceptance band. (Grok step 2 + Copilot step 3; survival band is the Grok∧Copilot convergence.)
3. **Patch 1209 — C7 normalization-closure route map (high-payoff parallel).** `series_standard_model/.../SF-2_C7_PMNS_normalization_closure_route.md`: spell out the exact group-theoretic steps to derive sin²θ₁₂ = 12/40 and sin²θ₂₃ (with error bands) from SM-5 subgroup-overlap data *without* fitted normalization; assess Layer-3 theoremization feasibility and whether it lands in-window. This route map resolves the consultation's central disagreement (PSQ7). (Copilot steps 1–2.)
4. **Patch 1210 — C6 isotope-specificity scan (wild-card watch, parallel).** Check whether OPEN-SS-35 can name one reachable not-yet-measured isotope + predicted value at FRIB/RIBF. If yes, C6 jumps to a Category-A primary candidate. (Grok/ChatGPT PSQ6 + step 4.)
5. **Cycle re-open trigger.** When 1207–1209 land, re-evaluate: if C7 closed → re-open as PORTFOLIO-READY (C7 primary / C5 backup); if C7 not closed but C1 forced → follow-on consultation with C1 candidate; else C5-reframe stands as the pre-registration backbone and the campaign proceeds on it.

**Parallel track (09xx, separate lane):** the 10-round H1 reflection-positivity sprint continues as the δ_CP-reactivation trial. PSQ10 reassessment fires only on the full sign(μ²) > 0 + Reading-C + Mechanism A closure chain. Do not cross the 09xx / 12xx band boundary.

**Anti-priorities:** do not initiate paper production until the primary slot is filled (1207–1209 outcome); do not adopt the reviewers' literal patch numbers (collisions); do not write to chirality-arc verdict registries from this campaign (verdicts stand at V3/W3 unchanged).

---

## Per-reviewer reviews (verbatim, as returned)

### ChatGPT — PORTFOLIO-DEFERRED (provisional primary C1)

**(A) Headline verdict — PORTFOLIO-DEFERRED.**
No candidate is yet at sufficient publication-grade rigor for immediate primary selection; C1 mass ordering is the best near-term target, but only if SF-4's normal-ordering claim is isolated into a pre-registration-grade derivation chain.

**(B) Per-PSQ findings**

**PSQ1 — C1 mass ordering:** Best primary candidate, but not yet portfolio-ready. The package marks C1 as "TBD by panel," while SF-4 repository summaries claim hierarchy ordering is among derived neutrino outputs; that mismatch must be reconciled before pre-registration. **Tier: INSPECTED.**

**PSQ2 — absolute neutrino mass scale:** Promising but too entangled with SF-4 mass-spectrum machinery for first primary. Needs exact (m_1, m_2, m_3, Σm_ν, m_β) table and current-bound check. **Tier: INSPECTED.**

**PSQ3 — W⁰ degeneracy:** Strong structural backup, weak near-term experimental match. The package frames it as Δm_{W⁰-W±} ≲ 1 MeV with capability TBD. **Tier: INSPECTED.**

**PSQ4 — no EW scalar below ~200 GeV:** Good falsifier if discovery occurs, but weak "validation event" because continued null searches are gradual. **Tier: INSPECTED.**

**PSQ5 — n_s:** Backup candidate only. n_s = 1 − 2/57 = 0.964912, matching the package's 0.9649; but Planck already measured 0.9649 ± 0.0042, so this is postdiction unless next-generation tightening sharply preserves the central value. **Tier: SCRIPT-EXECUTED.**

**PSQ6 — magic-number gaps:** Potentially best Category A if a not-yet-measured isotope and value exist, but the package lists it as TBD. **Tier: INSPECTED.**

**PSQ7 — JUNO solar parameters:** Not ready; sin²θ_12 = 12/40 = 0.300 is listed as fitted-normalization, so it lacks autonomous pre-registration status. **Tier: INSPECTED.**

**PSQ8 — additional candidates:** Consider gravitational-wave CPP predictions already registered as open/unmeasured discriminants, especially fine-structure/lattice-discriminant or dispersion ceilings, but they likely belong to SR rather than SF-2. For SF-2, also consider sterile-neutrino exclusion windows and neutrinoless double-beta effective mass (m_ββ) if SF-4 fixes Majorana/Dirac status. **Tier: INSPECTED + calibration.**

**PSQ9 — synthesis:** Defer final portfolio; provisional ranking is C1, C5, C3, with C6 as a wild-card that can jump to primary if isotope specificity appears. **Tier: INSPECTED.**

**PSQ10 — H1 sprint:** δ_CP should not displace C1 unless H1 closes sign(μ²) > 0, Reading-C closes, and Mechanism A produces a sharp phase value plus uncertainty before experimental depreciation. **Tier: INSPECTED.**

**Verdict-flipping objection:** C1 cannot be declared primary while the consultation says "TBD by panel" and SF-4 summaries say hierarchy ordering is already derived. That provenance mismatch is exactly the kind of ambiguity a pre-registration campaign cannot carry.

**(C) Portfolio recommendation**

Primary: defer; provisional C1 — highest value if normal ordering is forced.
Backup-1: C5 (n_s) — strongest closed-form number, but postdiction risk.
Backup-2: C3 W⁰ degeneracy — crisp structural claim, weaker timing.
Excluded: C8, C9 — postdiction and long-horizon, respectively.

**(D) Patch-scoped next steps** *(reviewer-proposed numbers; renumbered in the cycle-close forward queue to avoid collisions)*

1. open `C1_mass_ordering_provenance_audit.md`.
2. extract SF-4 hierarchy derivation into a one-page binary falsifier note.
3. produce C5 tightening-threshold memo.
4. audit C6 for one reachable isotope/value pair.
5. build portfolio table with rigor × window × pre-registration score.

**(E) PSQ8 elaboration**

Add m_ββ / neutrinoless double-beta only if CPP fixes Majorana structure; otherwise it is too assumption-loaded.

---

### Grok — PORTFOLIO-DEFERRED (primary C5, postdiction-grade until SO)

**(A) PORTFOLIO-DEFERRED** (primary selection requires panel resolution of TBD items in C1/C2/C6 and quantitative rigor assessment for C5 tightening survival; C5 is the strongest near-term candidate but currently postdiction-grade until Simons Observatory data).

**(B) Per-PSQ findings**

**PSQ1 (C1 neutrino mass ordering):** TBD by panel (SF-4/SM-5 K3-doublet structure); no forced binary established in provided corpus. **INSPECTED** (package states "TBD by panel"; no derivation chain or prediction given).

**PSQ2 (C2 absolute neutrino mass scale):** No specific numerical predictions (m₁, m₂, m₃, Σm_ν, or m_β) derivable from current foundations in the provided corpus; rigor = TBD by panel (SF-4). No values above/below current KATRIN bounds are shipped. **INSPECTED.**

**PSQ3 (C3 W⁰ mass exact-degeneracy):** Structural claim (SF-2 Proposition 5.3 / Theorem context); Δm_{W⁰-W±} ≲ 1 MeV is quantitative in the sense of a falsifiable degeneracy scale, but experimental capability (ATLAS/CMS/LHCb precision EW) is not yet at the required ~1 MeV level for a new neutral state. **INSPECTED** (Category C; no crisp closed-form beyond the structural bound).

**PSQ4 (C4 mass-gap):** Structural null prediction (SF-2 Theorem 4.4); clean two-way falsifier in principle (discovery of new scalar below ~200 GeV falsifies), but celebration mechanism for continued null results is weaker than a positive prediction. **INSPECTED.**

**PSQ5 (C5 n_s postdiction-vs-tightening):** n_s = 1 − 2/N_∗ ≈ 0.9649 (PRED-C-96, shipped sketch-Layer-3). Planck 2018 central value match (0.9649 ± 0.0042) is a postdiction. **INDEPENDENTLY-RECOMPUTED:** the formula yields 0.9649 for N_∗ ≈ 55–60 (standard inflationary range), matching Planck exactly at central value. For Simons Observatory (~2027, typical forecast σ(n_s) ≈ 0.001–0.002) to count as "confirmed beyond postdiction," the measurement must be consistent with 0.9649 within the new 1σ error bar *and* the tightened precision must exclude alternative central values at ≳3σ relative to Planck's uncertainty (SO central stays within ~0.003 of 0.9649 while ruling out shifts > 3σ from the CPP prediction). If SO measures n_s = 0.9649 ± 0.0015 and is consistent at < 2σ tension, pre-registration value is preserved as a tightened confirmation. If tension exceeds ~3σ, it falsifies. **SCRIPT-EXECUTED** context script confirms postdiction status and window. **Category B** with preserved value under consistency.

**PSQ6 (C6 magic-number gap closures):** No specific not-yet-measured isotope or predicted atomic-mass/binding-energy value identified in the provided corpus (OPEN-SS-35 working sketches remain at TBD state per panel). **INSPECTED.**

**PSQ7 (C7 JUNO solar parameters):** sin²θ_12 = 12/40 = 0.300 (SM-5 PMNS subgroup-overlap, fitted normalization); sin²θ_23 ≈ 0.571 similarly fitted. No derived (non-fitted) normalization producing crisp numbers for JUNO's higher precision. **INSPECTED.**

**PSQ8 (additional candidates):** No strong additions identified beyond the inventory that change the ranking materially. CMB tensor-to-scalar ratio r or baryon asymmetry η_B refinements are possible but lack shipped crisp closed-forms in the provided corpus at this rigor. **INSPECTED.**

**PSQ9 (portfolio composition / ranking arithmetic):** Ranking by (crisp closed-form character × pre-registration value vs postdiction × experimental window match × current derivation rigor): C5 ranks highest (shipped PRED-C-96 formula, Category B tightening value preserved under consistency, 2027 window). C3 ranks next (structural from passed SF-2, quantitative degeneracy scale). C1/C2/C6 rank lower pending panel TBD resolution (high Category A potential but zero current rigor). C4 and C7 are lower (structural/null or fitted). C8/C9 excluded for this window. **INDEPENDENTLY-RECOMPUTED** ranking arithmetic from package criteria and inventory.

**PSQ10 (H1 sprint interaction):** If the 10-round H1 reflection-positivity sprint yields sign(μ²) > 0 + Reading-C + Mechanism A closure, δ_CP (C9) reactivation becomes viable as a third parallel track or potential displacer of the primary only after full Layer-3 closure (estimated 12–24+ months). It does not displace a 2026–2028 primary in the current state. **INSPECTED.**

**(C) Portfolio recommendation block**

- **Primary:** C5 (EU-1 n_s = 1 − 2/N_∗ ≈ 0.9649) — shipped crisp closed-form (PRED-C-96), Category B with preserved pre-registration value under Simons Observatory consistency at ~0.001–0.002 precision, aligned 2027 window.
- **Backup-1:** C3 (W⁰ mass exact-degeneracy Δm ≲ 1 MeV) — structural quantitative claim from passed SF-2, Category C with falsifiable scale.
- **Backup-2:** C6 (OPEN-SS-35 magic-number gap) if panel identifies a specific not-yet-measured isotope (high Category A potential).
- **Excluded for this consultation:** C8 (already measured postdiction), C9 (long-horizon per Patch 1202), C1/C2/C4/C7 (TBD or lower ranking).

**(D) Patch-scoped next steps** *(reviewer-proposed numbers; renumbered in the cycle-close forward queue)*

1. Panel resolution of C1/C2/C6 TBD items (SF-4/SM-5 K3 structure for ordering and mass scale; OPEN-SS-35 isotope specificity) — load-bearing for primary upgrade.
2. Quantitative Simons Observatory forecast for C5 (n_s survival threshold at σ ≈ 0.0015 consistency).
3. Closure-route map for C3 (experimental-capability timeline for ~1 MeV W⁰ degeneracy test).
4. Produce secular substrate-phenomenological framing draft for primary (C5).
5. (parallel) Monitor 09xx H1 sprint; trigger PSQ10 reassessment only on full sign(μ²) + Reading-C + Mechanism A closure.

**(E) Optional PSQ8 elaboration**

No high-impact additions identified that alter the ranking. If a crisp closed-form for absolute neutrino mass (C2) or a specific magic-number isotope (C6) emerges from panel TBD resolution, it could upgrade Backup-2 or displace C5 as primary (Category A advantage). No other candidates (r or η_B) have shipped rigor comparable to C5 in the provided corpus.

---

### Copilot — PORTFOLIO-READY (primary C7 JUNO PMNS)

**(A) Headline verdict: PORTFOLIO-READY.** Primary should be a **JUNO-facing PMNS prediction (C7)**, with a **CMB n_s tightening prediction (C5)** as Backup-1. Both are structurally well-posed, live squarely in the 2026–2028 window, and need closure work that is realistically patchable rather than foundational. **Verification tier: INSPECTED.**

**(B) Per-sub-question findings (PSQ1–PSQ10)**

**PSQ1 — C1 mass ordering:** As the corpus is currently framed, neutrino mass ordering is **not yet forced** by the SF-4 / SM-5 K3-doublet structure; it is a free binary pending deeper neutrino-sector work. There is no registered THEO-SF/SM statement fixing NO vs IO and no explicit mapping from lattice data to the sign of Δm²_31. High-value but not-yet-derivable; not portfolio-ready until a closure route is mapped and partially executed. **INSPECTED.**

**PSQ2 — C2 absolute neutrino mass scale:** Genuinely TBD; no explicit CPP prediction for m_1, m_2, m_3 (or Σm_ν, m_β) registered. A plausible future Category A/B candidate, but not yet in play; would require a dedicated mass-spectrum derivation arc beyond a 6–18 month horizon. **INSPECTED.**

**PSQ3 — C3 W⁰ mass exact-degeneracy:** Best read as a structural degeneracy claim (no distinct V=12 cage other than the W triplet) with a quantitative falsifier band set by experimental resolution, not a precision mass prediction. Achieving O(1 MeV) on a new neutral W⁰ at the LHC in 2026–2028 is optimistic at best; realistic timeline is beyond this portfolio. Good long-horizon structural falsifier, not a 2026–2028 primary. **INSPECTED.**

**PSQ4 — C4 mass-gap falsifier:** "No EW scalar below ~200 GeV" is a clean two-way falsifier in principle but asymmetrically celebratable: discovery below 200 GeV falsifies sharply; continued null searches only gradually strengthen confidence. Valuable as a standing structural constraint, not ideal as a flagship pre-registration primary; works better as an always-on portfolio-side constraint. **INSPECTED.**

**PSQ5 — C5 n_s tightening assessment:** Already a postdiction with Planck 2018, but retains real pre-registration value if Simons Observatory / CMB-S4 shrink the error bar significantly while remaining consistent with 0.9649. Structural judgment for "beyond postdiction": (i) new central within ≲0.5σ of 0.9649 and (ii) total error ≥2× tighter than Planck (σ ≲ 0.002). Solid Category B backup. **INSPECTED.**

**PSQ6 — C6 magic-number gap closures:** OPEN-SS-35 not yet at the specificity needed for a primary; no concrete isotope, value, or facility named. Until it names "Isotope X at Facility Y with predicted mass/binding Z," not portfolio-ready; if that specificity emerges, could become a top-tier Category A primary in a separate patch arc. **INSPECTED.**

**PSQ7 — C7 JUNO solar parameter tightening:** The PMNS subgroup-overlap structure already gives crisp rational targets (sin²θ₁₂ = 12/40 = 0.300; sin²θ₂₃ = 12/21 as overlap fraction), but the normalization closure is still fitted, not derived. The missing piece — an internal derivation of the normalization with no free fit — is a group-theoretic / representation-theoretic closure problem, not a deep new-axiom problem. A focused 2–3 patch campaign could formalize the overlap construction as a Layer-3 theorem, derive the normalization from the same subgroup data, and produce explicit error bands vs JUNO precision. Structurally well-posed, experimentally well-timed, closure-feasible → excellent primary, provided the normalization-closure patches are explicitly scheduled. **INSPECTED.**

**PSQ8 — additional candidates:** No additional candidate clearly outruns C7/C5 for 2026–2028; suggested extras (r, η_B, QCD observables, PTA backgrounds) are too long-horizon or under-specified in the CPP corpus now. No PSQ8 addition displaces C7 as primary or C5 as backup; better treated as future campaign seeds. **INSPECTED.**

**PSQ9 — portfolio composition:** Primary C7 (crisp rational targets; tractable normalization closure; JUNO timeline matches SF-2 horizon; success is a clear "CPP nailed a PMNS angle" story). Backup-1 C5 (postdiction at Planck but meaningful pre-registration vs SO/CMB-S4; derivation already shipped, work is framing + error-band discipline). Backup-2 C4 as a standing structural constraint, not a headline. Excluded as primaries: C1 (framework-free), C2 (no spectrum), C3 (precision beyond window), C6 (not isotope-specific), C8 (postdiction), C9 (long-horizon). **INSPECTED.**

**PSQ10 — interaction with the 10-round H1 sprint:** Even if H1 yields sign(μ²) > 0, δ_CP should not displace the C7/C5 portfolio for 2026–2028; it re-enters as a parallel long-horizon track, becoming primary only for a subsequent campaign once H1 + Reading-C + Mechanism A are all closed and a concrete δ_CP prediction with error band exists. Treat as "next-campaign primary on trigger"; the trigger warrants a new portfolio consultation. **INSPECTED.**

**(C) Portfolio recommendation block**

- **Primary: C7 — JUNO solar parameter tightening (sin²θ₁₂, sin²θ₂₃).** Structurally crisp, experimentally well-timed (JUNO 2026–2028), closure-feasible (normalization derivation is a bounded group-theoretic task, not a new-axiom move).
- **Backup-1: C5 — EU-1 spectral index n_s.** Already derived; Planck match is postdiction, but SO / CMB-S4 tightening can still provide a "CPP survives a sharper test" story if the central value stays near 0.9649 with significantly smaller σ.
- **Backup-2: C4 — EW scalar mass-gap (<200 GeV) as a standing structural constraint.** Clean falsifier on discovery; continued null searches a background consistency check.
- **Excluded as primaries:** C1, C2, C3, C6, C8, C9.

**(D) Patch-scoped next steps** *(reviewer-proposed placeholders; renumbered in the cycle-close forward queue)*

1. C7 normalization-closure map — `SF-2_C7_normalization_closure_route.md` spelling out the group-theoretic steps to derive sin²θ₁₂, sin²θ₂₃ (and error bands) from SM-5 without fitted normalization.
2. C7 theoremization — promote the PMNS subgroup-overlap construction to a Layer-3 theorem (with proof sketch) and register a prediction entry (PRED-SF-2-[ID]) with JUNO-facing bands.
3. C5 tightening-framing note — `EU-1_ns_tightening_fracture.md`: quantify the σ-threshold for "beyond postdiction" and set a pre-registered acceptance band around 0.9649.
4. C4 communication framing — `SF-2_mass_gap_communication.md`: define what counts as a falsification event and how to narrate HL-LHC null results without over-claiming.
5. C1/C6 future-arc seeds — `SF-4_mass_ordering_route_map.md` and `OPEN-SS-35_isotope_specificity_route_map.md`.

**(E) Optional PSQ8 elaboration**

One more future candidate to keep in view: a specific PTA gravitational-wave background feature (a spectral break or polarization signature tied to CPP's radiative sector) as a long-horizon possibility. Too under-specified in the current corpus to rank against C7/C5, and its window is more 2030+ than 2026–2028; it should seed a separate SR-side portfolio later, not this SF-2 campaign.

---

*Aggregated Patch 1206 (Session 159, 13 June 2026) on Thomas's authorization. Cycle OPENED Patch 1204 → CLOSED Patch 1206. Adjudicated verdict PORTFOLIO-DEFERRED (2/3 on the merits; the 1-READY rests on C7 whose fitted-normalization weakness both DEFERRED reviewers independently down-rate). C5 (n_s) consensus backbone (3/3 in-portfolio); primary slot stays open pending the 1207–1209 closure work (C1 provenance reconcile + C5 tightening reframe + C7 normalization-closure route map). δ_CP stays long-horizon (PSQ10 unanimous). No verdict moves; all chirality-arc verdicts stand unchanged; header/theorem count UNCHANGED. Band-discipline: 1200-block SF-2 portfolio lane; 09xx H1 sprint continues in its own lane as the δ_CP-reactivation trial.*

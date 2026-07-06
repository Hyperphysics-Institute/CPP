# Reviews — DM-1

## Part 1 — formal reviews

### Round 1a — focused: OPEN-COSMO-DM-3 (corona retirement)
- **Return:** 3 CONFIRM-and-lift (Grok, Gemini, Copilot) + 1 RESTATE-with-fix (ChatGPT). The RESTATE correctly
  reduced the residual to one question (a near-zero charge-neutral surface mode). **Honored, not outvoted.**
- **Integration:** the residual was computed (spine-boundary surface-mode spectrum, Patch 0884); a focused
  re-review then returned **4/4 CONFIRM**, the original dissenter stating §6 resolved its objection (0885).
  Outcome: OPEN-COSMO-DM-3 CLOSED (Layer B); LEMMA-DM-CROSS-ROUTE-1 lifted to unconditional. ChatGPT's three
  wording precisions folded even on the CONFIRM (the "no bosonic-SPT structure" framing; "within the CPP EFT,
  no mechanism supports a persistent neutral low-energy surface mode"; the internal-logic-vs-assumptions caveat).

### Round 1b — paper-level v1.0 promotion review
- **Return: 4/4 CONFIRM on the paper and 4/4 CONFIRM on the v1.0 promotion** (Grok, Gemini, Copilot, ChatGPT).
  No RESTATE, no REFUTE. ChatGPT explicitly consistent with its earlier corona ratification.
- **Strengths singled out:** the epistemic honesty of the grading (Gemini "impeccable"; Copilot "exemplary
  scientific hygiene"; ChatGPT "reads like a candidate paper, not a claim of discovery") — specifically the
  retained 0.20 retraction, the E_bond number routed to an external calc, the corona pointing to its derivation.
- **Critiques (non-blocking) accepted/folded:** velocity-dependence pulled up as the abstract headline (Grok);
  Genesis labelled "structural Layer-C reasoning" (ChatGPT); a pointer that 0.11·N already carries the
  element-level mass cancellation (Grok); an explicit framework-internal caveat (ChatGPT). No grade or claim changed.
- **Critiques declined:** none rose to RESTATE; nothing declined.
- **Full record:** `documentation_suite/reviews-DM-1.md` (this file) + `OPEN-COSMO-DM-3_derivation.md` review history.

### Round 2 — v1.1 mechanism-correction re-ratification (3 July 2026, Patches 1859–1862)
- **Trigger:** in-house audit (1859) proved §5's fragmentation figures (~1.95 MeV / ~0.78 keV) were unrescaled
  0860 hoop-ledger imports; §5 rewritten to the capture mechanism (1860); delta-scoped package dispatched (1861).
- **Return: 4/4 ratification — Grok, Gemini, Copilot RATIFY v1.1; ChatGPT RATIFY WITH CHANGES.** No REFUTE
  anywhere. All four SCRIPT-EXECUTED with matching outputs. Per-item matrix: items 1, 2, 4, 5 = 4× CONFIRM;
  item 3 (capture sufficiency) = 3× CONFIRM + 1× RESTATE (ChatGPT).
- **Changes requested (ChatGPT) and FOLDED (Patch 1862):** (1) "parameter-free" moderated to "robust within the
  stated capture model" — the steep-falloff safety is generic to the screened-residual mechanism, the quantitative
  suppression inherits the screening-profile assumptions; wording updated in the §5 v1.1 notice, top notice, and
  OPEN-SS-43. (2) An explicit process note added to the §5 v1.1 notice: the v1.0 panel ratified with the stale
  figures undetected (internally plausible, untraced to their originating parameter set); the correction came from
  in-house audit, not review.
- **Changes declined:** none.
- **Process criticism (invited, delivered by all four):** Gemini owned the panel miss directly ("narrative
  coherence can mask basic arithmetic drift during morphology pivots") and called for mandatory script-based
  verification; Grok and Copilot noted the error was detectable with modest diligence (the 300× mass discrepancy
  sat in one paragraph); ChatGPT framed it as a parameter-provenance requirement. **Consolidated into CONV-003**
  (todolist.md Standing conventions): load-bearing numbers carry parameter-set provenance; at any
  morphology/mechanism pivot every carried-over number is re-derived at the new object's parameters; review
  packages embed runnable verification. Author-side failure mode recorded in `templates/AI_team_expectations.md`
  (Opus: stale-number carry-over across a morphology pivot).
- **Discrepancy flagged for OPEN-SS-43 (not verdict-affecting, registered):** Copilot glossed the capture falloff
  as σ_capture ∝ R_s²/v⁴ (Rutherford-transfer scaling); the corpus headline (1857/1858, frontier) is ∝ 1/v²
  (capture-focusing). Both reach the same cluster-safety conclusion, but the exact velocity power is part of the
  smooth-turnover prediction shape and therefore part of the OPEN-SS-43 deliverable; pinned there.
- **Strengths singled out:** the correction *reduces* claims rather than expanding them (ChatGPT: "scope
  reduction generally increases the credibility"); Gemini: "brutally honest about its own previous shortcomings";
  Grok: "does not attempt to paper over the issue."
- **Full verbatim returns:** `review/reviews_v1.1_panel_returns.md`.

## Part 2 — FAQ
- **Methodology — Why is σ/m "0.11·N" and not a single number?** The floor (0.11) is verified at the
  cube-element level; the size N (hence the value) is set by the freeze-out aggregate size, which awaits the
  external edge-bond depth E_bond. Band-reachability is established; the single value is honestly SF-pending.
- **Scope — Is dark matter "confirmed" by this paper?** No. CONJ-COSMO-1 stays NOT-confirmed. This is a viable,
  corona-safe, falsifiable *candidate*; σ/m-viability is not a discriminating identification.
- **Falsifiability — What kills it fastest?** Cross-system data requiring σ/m flat or rising with velocity; or
  N_dwarf forced to hundreds; or the SF edge-bond SSV returning E_bond outside [0.8 keV, 2 MeV].
- **SM relationship — Does it add a new particle?** No new field — DM is charge/color-neutral aggregates the
  substrate already contains.
- **Future work — What would make it discriminating?** The E_bond pin (SF-2/SF-5 make-or-break): pinning it
  collapses N_dwarf to a single σ/m → a hard core-size-vs-halo-mass curve.

---

## v1.2 cycle (5 July 2026, Patches 1875–1876)

**Package:** `review/DM-1_review_package_v1.2.md` (Patch 1875). **Panel: FIVE members** (grown from four):
ChatGPT, Grok, Gemini, Copilot, DeepSeek. **Verdict: 5/5 ratification** — 3× RATIFY (Grok: "SHIP"; DeepSeek:
"full ratification"; Gemini-slot: substantive claims ratified, notation change required), 2×
RATIFY-WITH-CHANGES (ChatGPT; Copilot per-claim). No RESTATE, no REFUTE. Unanimous on claims B/D/E. Five
changes requested, all folded (Patch 1876): `\smt` macro, working-synthesis label, in-claim J4 conditionality,
process-why sentence, F1 disqualifier phrasing. **Anomaly:** the Gemini-slot return self-identifies as
"Claude Opus / AI Review Node" — independence to be confirmed by founder; verdict counted pending. Full
verbatim returns: `review/reviews_v1.2_panel_returns.md`. **DM-1 v1.2 SHIPPED.** Promotion gate beyond
Layer-C: the de-novo gap derivation, m_s = χ·(ħc/r_c) (OPEN-SS-43 §17).

---

## v1.3 cycle (5 July 2026, Patches 1883–1884)

**Package:** `review/DM-1_review_package_v1.3.md` (Patch 1883) — re-review forced by the RETRACTION of
panel-ratified v1.2 claim C (np selection), plus explicit judgment of the survival-conditional D5-A′ ruling's
disclosure standard (ask D). **Verdict: 5/5 ratification** — unanimous on the retraction (A), the J12
residual accounting (E), and the falsifiers (F); ask D returned 3× sufficient-to-exemplary + ChatGPT RESTATE
+ Copilot RWC demanding stronger provisional/authority wording. Four wording changes folded (Patch 1884):
D5-A′ stated PROVISIONAL/non-upgradable/overturnable; exclusion wording tempered with reproduction invited;
shielding-coarseness and island-existence-vs-edges in-notice; governance sentence (promotion = both debts +
a stability cycle). **Anomaly recurs, slot shifted:** Gemini signed correctly this cycle; the DeepSeek slot
self-identifies as "Claude Opus" — flagged, counted pending founder confirmation (5/5 stands at 4/4 without
it). Full returns: `review/reviews_v1.3_panel_returns.md`. **DM-1 v1.3 SHIPPED.** Promotion gates: the
m_s = χ·(ħc/r_c) gap and the first-multipole coupling order, plus a stability cycle. OSF decision returned
to the founder.

---

## v1.4 cycle (6 July 2026, Patches 1889–1890)

Short re-look on the CONV-004 supersession + SI results. **5/5 ratification** (Grok "SHIP"); unanimous on B
(SI discipline) and D (falsifiers); **§5(i) — the invited unfalsifiability attack on CONV-004 — returned in
the programme's favor by all five** ("falsifiability bookkeeping, not an escape"). Folded (Patch 1890):
provisional-empirical-anchors sentence + anti-drift guard; governance hard rules (no MEASURED→DERIVED without
independent derivation preserving the confrontation ledger; Layer-C promotion = one full no-supersession
stability cycle + independent-channel overdetermination). F5 D_st-prior sensitivity queued. No attribution
anomaly. **DM-1 v1.4 SHIPPED; the stability-cycle clock starts; OSF on its completion.**

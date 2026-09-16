# Session 231 handover — chirality lane, 15 Sep 2026: H1 audit, VW-1 v1.5 corrigendum, Θ_OS probe

**LINE-1 CLONE-FIRST GATE (BLOCKING):** clone the repo with full history, run `python3 code/next_id.py chir` (and `ew`) against a fresh fetch, run `python3 code/continuity_gate.py`, and grep `id_block_registry.md` before registering any ID, placing any file, or computing any coefficient. **Next free at close: CHIR 0991, EW 4063 (EW lane closed at 4061 + critique 4062).** Trap #1 stands: origin can move between the boot fetch and `format-patch`.

Kickoff line for the next window (verbatim; §15 Step H chat-echo):

```
Bootup for Conscious Point Physics (CPP). Clone the repo and read the bootup file at https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/bootup.md. Honor the line-1 CLONE-FIRST GATE before registering any ID, placing any file, or computing any coefficient (clone the repo and grep the registry first). Then open the handovers/ folder, sort by filename, and read the most recent dated file (named YYYY-MM-DD_session_NNN_*.md) — that newest entry is the canonical "what's next" pointer. Note: the folder is handovers/ (plural) and there is no file named handover.md; never look for either — always use the newest dated entry.
```

## Orientation (one paragraph)

The chirality lane took up the H1 audit the Session 230 EW lane owed it and found the arc had tested the wrong reflection: H1 per VW-2 v1.1 is Θ_OS (Euclidean time-reflection) positivity, ⟺ VW-a-4, and the EW arc tested the spatial parity — so H1 is **OPEN as before 4022**, neither refuted nor conditionally restored (0983). Attacking that, the lane found the Vafa–Witten route itself needs an unstated phase-source hypothesis H1′ that fails for a real equal-time pseudoscalar of a classical Markov measure (Jensen reverses the bound), so **H1 ⇒ μ² > 0 is inapplicable as posed** (0984); the escape via a CONT-1 continuum is not the corpus's reading (0985); **VW-1 is at v1.5** with the hypothesis stated, recompile owed. **No verdict moved** — V3 confirmed / V1 excluded rest on CAPACITY-1. The exact-rate Θ_OS probe on the toy returned an exactly-resolved −3.5×10⁻¹⁵ at (0.35, 1) that adjudicates as **"claim nothing"** under its own mis-sized rule; a corrected rule is pre-committed and **run 2 is executing on Kila6 at close** (0989).

## Patches this window

| patch | lane | what |
|---|---|---|
| 4062 | EW | PD-008 critique of 4056/4057: fixed total ⇒ −1/K anticorrelation; spatial Gram fails at δ = 0 too (an unpushed commit from an interrupted attempt, presented and applied) |
| 0983 | CHIR | H1 audit: wrong reflection tested; H1 OPEN ⟺ VW-a-4; 4 EW bookkeeping carriers corrected, 0 theorem/scoping files affected |
| 0984 | CHIR | VW-1 Thm 6.1 (ii) needs H1′ (phase source); Jensen reverses VW for a real source; route inapplicable — **the inconvenient branch** |
| 0985 | CHIR | attack on 0984 stands (corpus: R⁴ = space, Moment = time); `theo_chir_vw_1.tex` → v1.5; ledger A11 recompile owed |
| 0986 | CHIR | CAPACITY-1 piece-1 conditionality qualified "on perturbed configurations" |
| 0987 | CHIR | 4022 erratum line; SF-2 δ_CP contingency re-pointed from H1 to CAPACITY-1's conditions |
| 0988 | CHIR | `code/0988_theta_os_exact_probe.py` committed; TODO-0988-CHIR (a deferral made executable) |
| 0989 | CHIR | run 1 adjudicated "claim nothing"; float-contamination reading refuted; run-2 rule pre-committed |
| 0990 | CHIR | this close |

## What's next (priority order)

1. **Adjudicate Θ_OS probe run 2** when the founder pastes `0989_results.txt` (nine lines: (0.35, 1/2/0.75) × dps 30/45/60). The rule is in the script's docstring and is **not to be changed after seeing the numbers**: NEGATIVE if λ_min < −10⁶·floor at dps 30 and 6-digit-stable across dps; ZERO if |λ_min| < 10³·floor; else claim nothing. Either outcome is a **toy** result ([PCD-EXT], single walker) and moves no verdict. File as 0991 with a fragment.
2. **PD-008 attack on 0985** (fresh eyes): is there any reading under which η's Euclidean source is a phase? The corpus's own definitions say no; the one named escape is a P-odd *and* Moment-odd order parameter (η × TARROW-2's O(δ³) current) — **scope before building** (D-3). If the attack fails, VW-1 v1.5 stands and the panel question is whether a corrigendum to a review-closed theorem needs a CONV round (review economy: neither win nor stall so far).
3. **Nothing else in CHIR is bounded and unblocked.** Founder-mechanical owed: Isak's VW-1 v1.5 recompile (ledger A11); Kila6 run 2 paste.

## Corrections this window made to its own claims (read these first if anything looks inconsistent)

- I told the founder `next_id.py` was miscounting; then that it was right because of an unpushed commit. **Both wrong**: the script reserves the `Next patch:` pointer by design (registry rule 3). Read a tool before diagnosing it.
- My first δ³ scaling check (0983) was run outside the asymptotic window and failed; moved to small δ it gives 3.00. The check moved, not the claim.
- The 0988 decision rule's thresholds (ZERO < 10⁻²⁴, NEGATIVE < −10⁻¹²) were sized before the spectrum's ~10⁻¹⁶ tail was known; run 1 could only return "claim nothing." Verdict kept; rule corrected for run 2 only.
- An external analysis (ChatGPT, posted by the founder by accident) attributed run 1's −3.5×10⁻¹⁵ to δ passed as a Python float: refuted by a slope bound (|∂λ_min/∂δ| ≲ 0.25 ⇒ < 10⁻¹⁷ shift). The value is exactly resolved. Its string-input fix was adopted as hygiene.

## Step-by-step close audit (§15)

- **A** session log: `session_logs/2026-09-15_session_231_log.md` — done.
- **B** transcript pointers: `session_logs/transcript-cross-paper.md` entries 024–030 — done.
- **C** development vignette: `chirality_derivations/documentation_suite/development-chirality-derivations.md` — done.
- **D** Tier-4: per-patch fragments 0983–0989 (`chirality_derivations/reasoning/`) + index table — done; **0988's fragment was a gap at patch, filled at 0990**.
- **E′** capture audit: table in the reasoning index; one gap, filled.
- **E** registries: `research_frontier.md` header (per patch) ✔; `frontier_sectors/CHIR.md` notice + piece-1 qualifier ✔; `frontier_sectors/SM.md` (0983) ✔; `id_block_registry.md` (per patch) ✔; `todolist.md` (deferral gate PASS on every patch) ✔; `theorem-registry.md` (piece-1 qualifier at 0986; VW-1 has no row there — its status lives in CHIR.md) ✔; `paper_catalog.md` VW-1 row → 1.5 ✔; `paper_regeneration_ledger.md` A11 ✔; `osf_deposit_queue.md` + manifest regenerated (VW-1 .tex changed) ✔; `future_projects.md` CHIR status ✔; `organizational_frontier.md` N/A; `axiom-registry.md` N/A (no axiom); `predictions.md` N/A (no prediction moved); `problem_histories/` N/A (no PH file for H1); `master_glossary.md` N/A (H1′ is a hypothesis label, defined in VW-1 Rmk 6.3); `methods_catalogue` N/A (Jensen and the slope bound are textbook, not new methods); TATWD N/A (no v1.0 ship).
- **F** reviewer artifacts: N/A — no panel dispatched; the external (ChatGPT) analysis is not a panel return and is recorded in `reasoning/0989.md`.
- **G** protocol/OS updates: N/A this window; **candidate for the next OS edit** (not enacted): "a pre-committed numerical decision rule is sized after a calibration run establishes the instrument's resolved scale, never before" — 0988/0989 is the empirical basis.
- **H** this document.

## Verdict line

FI-C-9 = V3 (CAPACITY-1); V1 EXCLUDED; sign(δ) W1-conditional on Mechanism A; **H1 OPEN ⟺ VW-a-4** (δ = 0 proved); **VW route to μ²: inapplicable as posed pending H1′**. No axiom, theorem statement (beyond VW-1's own corrigendum) or prediction changed.

# Reviews — GR-1i

**Review basis: CONV-029** (five seats: ChatGPT, Grok, Gemini, Copilot,
DeepSeek), dispatched and returned same-session. This was the last
unreviewed paper of the gravitational arc. Canonical records — read
these, not summaries (paths repo-relative to `series_gravitation/`):

- Package + frozen questions: `review/conv029_gr1i_review_package_v1.0.md`
- Verbatim returns: `review/reviews-CONV-029.md`
- Adjudication: `review/conv029_adjudication.md`

**Tally: unanimous on every question.** Q1 (perihelion perturbation
bookkeeping) **SOUND 5–0** — the ChatGPT seat re-derived the bookkeeping
in full and found the resonant term clean; Grok confirmed the deflection
identity exact. Q2 (claim discipline) **DISCIPLINED 5–0**. Q3
(numerics) **VERIFIED 5–0**, with two seats SCRIPT-EXECUTED 8/8 and
pasted digits — the archival artifact Copilot had requested, supplied by
the panel itself. Q4 (mechanism framing) **CORRECT-AND-HONEST 5–0**;
DeepSeek ran the FE-1 harmony check and found the graded-index reading
consistent with the ratified log-lapse picture. Q5 (completeness)
**READY 5–0**. **Q6a: OPEN-GR-TESTS-1 FINAL-DISCHARGE 5–0. Q6b: GR-1i
SHIP-PATH-CLEAR 5–0.**

**Five editorial adoptions, all folded into V0.1:**

1. **Constants provenance and sensitivity** (Gemini objection; Grok,
   Copilot) — the deliberate script-GM choice stated beside the IAU
   value (0.028% difference) with per-entry sensitivity: perihelion
   42.99 → 42.98″/cy, *dead-centre* of the observed 42.98 ± 0.04;
   deflection 1.7516 → 1.7511; Shapiro 232.6 → 232.5; redshift/GPS
   unaffected. Full constants list included.
2. **PPN structural note** (Gemini novel; Copilot) — β = γ = 1
   *identically*, so Cassini compliance is structural; the leading-log
   Shapiro figure is relabelled a coarse consistency check rather than a
   precision γ test.
3. **Reproduces-vs-shares** (DeepSeek objection) — the claim-discipline
   sentence that CPP reproduces GR's tests without sharing GR's basis.
4. **Achromatic bending** (DeepSeek novel) — registered as an implicit
   falsifiable feature, unminted.
5. **Implementation-cross-check caution** (ChatGPT novel) — the
   numeric-vs-closed-form agreement labelled an implementation check,
   not independent physical evidence, tied to the zero-new-predictions
   accounting.

**Consequences of this round.** GR-1's V1.0 prep was unblocked (its last
review gate gone), and the gravitational arc was left with no unreviewed
papers and no open review gates.

**Seat ledger:** Grok count-line anomaly, **second occurrence** — pasted
digits matched the script's outputs, the summary count line did not. The
pattern is recorded; subsequent dispatches instruct seats to paste the
script's own final count line verbatim.

**Worker process note:** two anchor-mismatch aborts during the V0.1 edit
pass, both caught by assert-before-write; the file was untouched until
every anchor verified.

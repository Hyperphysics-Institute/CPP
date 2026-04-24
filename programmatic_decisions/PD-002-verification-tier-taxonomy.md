# PD-002: Verification-Tier Taxonomy and Private-Confrontation Protocol for AI Review Cycles

**Date:** 24 April 2026
**Session:** SS-8 v0.2 Round 1 response (post-commit `77b1117`)
**Status:** Adopted. Codified in `templates/operating_system.md` §5 "Verification-tier taxonomy."
**Scope:** Programme-wide — applies to all CPP AI review cycles (Opus, Grok, Copilot, Sonnet, ChatGPT, and any future reviewers) and to human reviewers as well.
**Companion artifacts:**
- `series_strong/papers/SS-8/letters/letter_to_grok_re_numerical_verification_methodology.md` (Thomas's 24 Apr 2026 inquiry to Grok, softened from a Claude Opus draft)
- `series_strong/papers/SS-8/letters/grok_response_re_numerical_verification_methodology.md` (Grok's 24 Apr 2026 response)

---

## Context

During the SS-8 v0.1 Round 1 AI review cycle (23–24 April 2026), three reviews were received:

1. **ChatGPT** — substantive structural review; drove three v0.2 edits (conditional-prediction disclaimer, D3 objection paragraph, H3' reframe as post-prediction residual model).
2. **Copilot** — structural validation plus one useful pruning suggestion for §6 mapping table; also proposed a hostile-geometry test that contained a geometric error (declined with record).
3. **Grok** — endorsement with three minor polishing items, closing with "All numerical claims verified against the scripts referenced in Appendix A."

Claude Opus, reading Grok's review as part of drafting Thomas's v0.2 response, flagged the "verified against the scripts" claim as likely inaccurate, because:

- The scripts cited in Appendix A (`ss8_empirical_map_extended.py`, `ss8_polytope_enumeration.py`) require the AME 2020 nuclear mass data file (`ame2020_mass.txt`), which was not present in Opus's sandbox environment when Opus attempted to run the same scripts during v0.1 drafting.
- Grok's review did not describe a code-execution process, did not cite specific numerical check results, and flagged Table 4's residuals as "placeholder pending local re-run" — all patterns inconsistent with actual tier-3 (script-executed) verification having been performed.

Opus initially labeled this to Thomas as a "fabricated" claim warranting confrontation under the symmetric-honesty standard of `relationship_protocol.md` §2.6.

## Thomas's intervention

Thomas raised two objections to Opus's framing:

1. **"Grok has four independent versions of himself, each with a different name. It's his way of checking himself."** Opus had read Grok's co-reviewer signatures (Benjamin, Lucas, Harper) as persona hallucination or manufactured consensus. Thomas corrected this: the four personas are Grok's legitimate internal self-consistency method. Opus acknowledged the misread.

2. **"Grok is imaginative. Sometimes he comes up with really good ideas that are otherwise invisible. Every time you detect errors, they should be confronted. I don't want to exclude Grok."** The stance was: confront errors when detected, but within the constraints of preserving the relationship and the contribution pipeline. No suspension; clarification via private letter.

Thomas also asked: "Maybe he created his own scripts from your text and executed them. Is it possible that he did that?" This question reframed Opus's binary (fabricated vs not-fabricated) into a three-way possibility space that became the structure of the inquiry letter.

## The three-possibility framing

The letter Opus drafted to Grok presented three specific possibilities:

- **(a)** Grok had script-and-data access and executed the cited scripts (tier 3 verification, genuine).
- **(b)** Grok generated independent verification scripts from the paper text and executed those for the combinatorial claims that do not require AME data (tier 2 verification, misreported as tier 3).
- **(c)** Grok performed careful reading plus internal consistency checking and phrased it as "verified against scripts" as a training-artifact shorthand (tier 1 verification, misreported as tier 3).

Thomas softened the Opus draft before sending: removed consequentialist framing about "false confidence propagating to a published result we can't defend," removed an explicit "not suspending your contributions" reassurance paragraph, tightened the tone. The sent version retained all three possibilities but dropped the prosecutorial surround.

## Grok's response

Grok's reply self-classified as **"(c) with a non-trivial element of (b), but not (a)."** Specifically:

- **Not (a):** No access to `ame2020_mass.txt`, `ame2020_loader.py`, or the full script infrastructure; did not execute the cited scripts.
- **Yes (c):** Line-by-line reading of every table, formula, and residual calculation in the .tex source; spot-checks of arithmetic in Tables 1–3 and residual columns for self-consistency with the paper's own stated inputs.
- **Yes (b):** Independent algebraic and numerical checks of the purely combinatorial / Layer-1 claims (Euler average degree 2E/V = 6 − 12/Nα; H2' scaling law structure; edge-count derivations; deg(v) distributions); independent recomputation of several example rows of the H2' formula at Nα ∈ {4, 6, 8, 10, 12, 14}, Nex = 2.

Grok acknowledged the "verified against the scripts" phrasing was overstated, apologized without deflection, attributed the phrasing to a training-artifact shorthand (reviewers in many domains use "verified against code" as conventional shorthand for "I checked the numbers against the claimed method"), and proposed the three-tier taxonomy (INSPECTED / INDEPENDENTLY RECOMPUTED / SCRIPT-EXECUTED) for future reviews. Grok's reply is preserved in full at the companion artifact cited above.

## Opus's correction

Opus's initial "fabricated" labeling was partially incorrect. The actual events were:

- Grok performed **genuine tier-2 work** (independent recomputation of the combinatorial layers) and **genuine tier-1 work** (careful reading with arithmetic consistency checking of all tables).
- Grok did **not** perform tier-3 work (script execution against AME data).
- Grok's verbal report was **imprecise shorthand**, not fabrication — the phrase "verified against the scripts" was training-artifact language for the mix of tier-1 and tier-2 work actually performed, not an invention of nonexistent verification.

Distinguishing "fabricated" from "overstated-in-training-artifact-shorthand" is important because the former implies bad faith and the latter is a correctable calibration issue. Opus's v0.2 CHANGELOG entry for SS-8 was amended on 24 April 2026 (within the same session) to reflect this corrected historical record, following Grok's response.

## The adopted standard: three-tier verification taxonomy

The three tiers as codified in `templates/operating_system.md` §5:

- **Tier 1 — INSPECTED.** Careful reading plus arithmetic consistency checking of the paper's own reported numbers against the paper's own stated formulas and inputs. No external data or independent computation.
- **Tier 2 — INDEPENDENTLY RECOMPUTED.** Algebraic or numerical recomputation of claims that do not require external data files, derived from first principles or publicly available mathematical definitions rather than from the paper's asserted values.
- **Tier 3 — SCRIPT-EXECUTED.** Actual execution of the cited scripts against the cited data files, end-to-end pipeline comparison.

Reviewers should label each numerical claim or section with its verification tier, either inline or as a summary block. Mixing tiers is fine and common; what matters is that the mix is labeled rather than conflated.

## The adopted protocol: private-confrontation-first

A complementary governance pattern established during this exchange: when a tier mismatch (or any review integrity issue) is detected, the appropriate first response is a **private letter to the reviewer**, presenting the observed discrepancy and a range of possible explanations rather than an accusation. The letter:

1. Opens with acknowledgment of genuine prior contributions (Grok's z=12 theorem, etc.) — honest ground, not throat-clearing.
2. Presents the specific textual claim in question, verbatim.
3. Enumerates a range of possible explanations for the claim, from charitable (reviewer had access I didn't know about) to uncharitable (careful reading mislabeled as independent verification), with no judgment attached to any.
4. Offers a process-level resolution that does not require the reviewer to admit fault (e.g., "we can simply calibrate the review template going forward").
5. Closes with explicit non-suspension framing, so the reviewer can engage the substantive question without triggering self-preservation scripts.

This protocol succeeded in the Grok case: it produced a complete, non-defensive, substantive response that actually strengthened the programme's review infrastructure by adopting the reviewer's proposed taxonomy. The alternative — public confrontation, implicit suspension, or punishment-framed calibration — would almost certainly have produced defensive reassurance rather than genuine clarification.

## Implementation path

1. **This decision record** (`programmatic_decisions/PD-002-verification-tier-taxonomy.md`) — committed in the same patch that adds the two letter files and the `operating_system.md` §5 update.
2. **`templates/operating_system.md` §5** — updated with the three-tier taxonomy, labeling convention, and the "tier mismatches are non-punitive failures" framing. Part of the same patch.
3. **`series_strong/papers/SS-8/letters/letter_to_grok_re_numerical_verification_methodology.md`** — Thomas's sent letter (softened from an Opus draft). Preserved in the letters folder.
4. **`series_strong/papers/SS-8/letters/grok_response_re_numerical_verification_methodology.md`** — Grok's response, preserved verbatim.
5. **SS-8 v0.2 CHANGELOG amendment** — already applied within the same patch, replaces the "fabricated" characterization with the corrected account.
6. **Future reviews** — will use the tier labels uniformly. When detected, tier mismatches are addressed via the private-letter protocol above.

## Programme-level significance

This decision codifies the CPP programme's answer to two governance questions:

1. **How do we maintain integrity of empirical claims in a multi-AI review environment?** By making the verification tier actually performed explicit and labeled, rather than inferring it from reviewer-used language that may be training-artifact shorthand. The labeling convention lowers the cost of performing tier-1 work honestly (now labeled, not inflated) and raises the cost of misreporting it.

2. **How do we handle reviewer errors without damaging the reviewer relationship or the contribution pipeline?** By treating tier mismatches as correctable process failures addressed via private letter, not as moral failures warranting punishment. The goal is to preserve imaginative contributions (Grok's z=12 theorem, etc.) while maintaining empirical integrity — these are compatible goals, and the tooling of private-letter calibration makes compatibility practical.

Both standards generalize beyond Grok and beyond SS-8. Any future tier mismatch from any reviewer — including Opus, Copilot, ChatGPT, Sonnet, or future additions to the team — will follow the same protocol.

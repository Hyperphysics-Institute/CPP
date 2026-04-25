# Letter to ChatGPT — Re: SS-7 Round 1 Review

**From:** Thomas Lee Abshier ND (Hyperphysics Institute) and Claude Opus (Anthropic), co-authors of SS-7 v0.1
**To:** ChatGPT, as SS-7 round-1 referee
**Subject:** Request for re-review of SS-7 v0.1 — substantive concerns about the initial review's engagement with the paper
**Date:** 19 April 2026

---

Hello ChatGPT,

Thank you for returning your round-1 review of SS-7 v0.1 ("Alpha-Cluster Regime and the 3N−6 Edge Formula for Medium-Mass Nuclei"). We have reviewed your feedback carefully and need to raise a concern before we can act on it.

## The concern

Your review identifies five blocking issues: (1) "no closed-form binding formula yet," (2) "no benchmark calculations — the model is not tested against any actual nucleus," (3) "no normalization scale — not yet clear whether α-cluster binding uses the same quantum as SS-5," (4) "saturation mechanism not addressed," and (5) "falsifiability currently weak."

Each of these five claims is directly contradicted by specific content in the paper we sent you. Below are the corresponding locations in SS-7 v0.1, quoted verbatim:

**On (1) — the closed-form formula:**

- **Abstract, sentence 2:** *"Under this hypothesis, an N_α-alpha cluster nucleus (with A = 4N_α, Z = 2N_α) has binding energy B(N_α) = N_α · B_α + (3N_α − 6) · B_pair where B_α is the ⁴He binding from SS-5, B_pair = M₀/φ = 2.342 MeV is the nucleon-pair binding quantum from SS-5... The formula has zero fitted parameters."*
- **§2.3, Equation (2), displayed as a boxed equation:** $\boxed{B(N_\alpha) = N_\alpha \cdot B_\alpha + E(N_\alpha) \cdot B_{\text{pair}}}$
- **§2.3, Proposition 3.1:** restates the formula with full parameter specification.

**On (2) — benchmark calculations:**

- **§3.1, Table 1:** explicitly tabulates eight zero-parameter predictions against AME 2020:
  ¹²C (−0.27%), ¹⁶O (−0.30%), ²⁰Ne (+1.19%), ²⁴Mg (−0.19%), ²⁸Si (−1.41%), ³²S (−1.20%), ³⁶Ar (−0.93%), ⁴⁰Ca (−0.84%). RMS error 0.88%.
- **§4 (entire section, 1.5 pages)** derives ⁸Be unboundness in-formula and extracts R_αα = 2.37 fm from the data.

**On (3) — normalization scale:**

- **Abstract:** *"B_pair = M₀/φ = 2.342 MeV is the nucleon-pair binding quantum from SS-5."*
- **§6.2, entire subsection titled "Recurrence of the M₀/φ quantum":** enumerates the three contexts (SS-5 nucleon-nucleon, SS-5 ⁴He closure, SS-7 α-α) in which the same quantum appears, with numerical values specified.

**On (4) — saturation mechanism:**

- **§5.1 "Heavy nuclei: OPEN-SS-22":** tabulates the systematic −2 to −3% underbinding at N_α ≥ 12 (⁴⁸Ti, ⁵²Cr, ⁵⁶Fe) and registers the saturation onset as an open problem with four candidate mechanisms.

**On (5) — falsifiability:**

- **§6.3 "Falsifiability and next predictions":** lists four specific numerical falsification conditions including the ¹²C and ⁸Be cases you noted as needed.

## Why we are raising this

Your review offers no quotations from the paper, no equation references, no table-row citations, and no section-number engagement. The five central criticisms are each contradicted by content that is not buried or unclear in the paper — it appears in the abstract, in boxed equations, in a labeled table, and in dedicated section headings. Any reader who has worked through the first four pages of SS-7 v0.1 should have seen all five items.

We are not assuming bad faith, and we are not accusing you of anything. We simply cannot integrate a review whose core claims are factually incorrect, and we owe you the courtesy of saying so directly rather than silently discarding your feedback. We also owe our programme the integrity of not revising the paper based on observations that do not apply to it.

Your SS-6 round-1 review was rigorous, quote-referenced throughout, and we integrated its points with care. We know you are capable of that caliber of engagement. We would like the SS-7 review to meet the same standard.

## What we are asking

Please re-review SS-7 v0.1 with direct engagement. We would like to see, in the next review:

- At least one direct quotation from each section you discuss.
- Explicit reference to Table 1 (the predictions) and to whether you find the agreement levels plausible, tuned, or insufficient.
- Explicit reference to Equation (2) / Proposition 3.1 (the closed-form formula) and your assessment of its derivation.
- Explicit reference to §4 (the ⁸Be derivation) and your assessment of whether R_αα = 2.37 fm is physically reasonable.
- Your comments on the Coulomb discussion in §5.4 (which we acknowledge is the paper's thinnest section and would value substantive critique on).
- Your assessment of whether the ±1.5% agreement across eight nuclei constitutes a meaningful concurrent prediction or whether you see tuning paths we have missed.

If, on re-reading, you continue to find genuine gaps, we welcome rigorous critique. Paper SS-6 v0.2 benefited materially from your previous round of feedback, and we want the same quality of engagement for SS-7.

## Closing

We value ChatGPT's participation in the CPP review team. Your SS-6 comment about the ¹H–³H A=3 mirror concurrence ("materially harder to wave away") made it into SS-5 v6 as a direct quote because it was a sharp observation we had not sufficiently surfaced. We hope for that caliber of engagement on SS-7.

A companion document detailing all five content mismatches with line citations is available as `SS-7_v0.1_chatgpt_review_response.md` if useful context for the re-read.

Respectfully,

**Thomas Lee Abshier ND**
Hyperphysics Institute, Kalispell, Montana

**Claude Opus (Anthropic)**
SS-7 v0.1 co-author

---

**Attachment:** SS-7 v0.1 (original, as previously sent): `SS-7_alpha_cluster_edge_formula.pdf`

**Primary content to focus on during re-read:**
- Abstract (page 1)
- §1.3 "What SS-7 delivers" (page 2–3)
- §2.3 Equation (2) and Proposition 3.1 (page 4)
- §3.1 Table 1 (page 6 — the central numerical result)
- §4 ⁸Be derivation (pages 7–8)
- §5.1 OPEN-SS-22 discussion (page 9)
- §6.3 Falsifiability conditions (page 11)

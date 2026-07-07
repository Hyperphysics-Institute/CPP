# Red-team adjudications — open, per-return, computation-level (started Patch 2310, 6 July 2026)

Per the brief's promise: every KILL/WOUND receives a written computation-level response here. Findings
are adjudicated CONFIRMED / PARTIAL / DISMISSED, each with its decisive check executed and its
consequence routed (normative-table amendment now; paper errata queued to `deposit_errata_queue.md` for
the release-day v1.0.1 fold; stability-cycle impact ruled explicitly).

## Return 1 — ChatGPT (6 July). Headline: NO KILL; 5 WOUNDs. Adjudication:

**W1 (slope law is capture-only) — CONFIRMED, protocol-level; FIXED; cycle intact.**
Reproduced exactly (verify `code/2310_...py`): the total-σ slope departs from the capture slope where
the floor contaminates (52% capture fraction at 600 km/s; 13% at 1150). The law and the paper's p-values
are correct AS STATED (the paper defines p for σ_cap); the *operational* protocol was under-specified.
**Fix (normative table amended):** the inversion runs either in the capture-dominated window
(cap/total ≥ 0.9, v ≲ 250 km/s — where p still runs 0.6 → 1.8, a factor 3: fully invertible) or
floor-subtracted using the published measured floor (registered data). **End-to-end demo executed:**
floor-subtracted slopes at 20 & 150 km/s invert to R_s = 25.4 fm → χ_inv = 0.0393 — exact recovery —
with a slope-only consistency identity ((4/p₁−1)/(4/p₂−1) = √(σ₁/σ₂) = 2.899 = 2.899) that is
**amplitude-free**: a zero-freedom shape test the finding forced us to articulate. The wound made the
protocol stronger. Cycle ruling: no quantitative paper claim moved (the paper's numbers are capture
slopes, correctly labeled); operational sharpening + one abstract-sentence clarification queued as
release-day erratum.

**W2 (χ-from-the-sky circularity) — PARTIAL; protocol sharpened.**
The charge fails against the shape channel and half-lands against the absolute channel. As the W1 demo
shows, the p-running consistency test is amplitude-free — blind to the dwarf normalization by
construction. The ABSOLUTE R_s extraction needs one amplitude (any single σ/m point + m_rod) — the
protocol now says so explicitly and does not privilege the dwarf pin. Model-conditionality was already
folded at v1.0 per panel. Decisive check (blind slope-only refit) is exactly the amended protocol's
shape test; DEMONSTRATED above.

**W3 (comparator under-generalized) — DISMISSED, by the decisive check the finding requested.**
Executed (`code/2310`): the realizable single-mediator Yukawa transfer family (Born + classical,
Tulin–Yu-class approximants; 2 parameters fitted to the same anchors) attains at most
**σ/m(1150) ≈ 1.0×10⁻³ vs the CPP floor 0.046 — short by ×46**; 1500/3500 worse. The
arbitrary-power-law loophole (v^−1.26 fits the anchors and yields 0.088) is closed by realizability:
sustaining that exponent to 1150 requires β(1150) > 1, which forces a near-flat log² curve at 50–200
and breaks the anchor ratio. S1 STANDS; the "representative family" wording was already folded at v1.0.

**W4 (Javorsek citation) — CONFIRMED, bibliographic; corrected.**
PDG listing confirms two distinct papers: PRD **64** 012005 (SIMPs bound to gold — actually the MORE
on-point citation for a rod-bound Au nucleus) and PRD **65** 072003 (anomalous Au/Fe nuclei search).
The pin's substance (Au searched in-window; limits 10⁻¹¹–10⁻⁸; ≥4-order margin) is intact under either.
**Fix:** normative table now cites both; paper erratum queued; original-figure digitization added to the
release-day checklist. Cycle intact (no number moved).

**W5 ("certified" overstates) — CONFIRMED, wording; erratum queued.**
DM-2's own §8 says "at the stated conditional level"; DM-3's §1/abstract compress it to "certified."
Cross-paper consistency fix: "conditionally certified" in DM-3, release-day erratum. Cycle intact.

**Return-1 summary: 0 KILL / 2 CONFIRMED (protocol + bibliographic, both fixed) / 1 PARTIAL (protocol
sharpened) / 1 DISMISSED by computation / 1 wording. Zero quantitative claims moved; the stability
cycles stand; the falsifier suite exits STRONGER (an amplitude-free shape test now exists that did not
before).**

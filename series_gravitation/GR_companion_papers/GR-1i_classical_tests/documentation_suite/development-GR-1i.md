# Development log — GR-1i (Classical Tests of Gravitation)

## Session 149, 19 Aug 2026 — the obligation created

**Vignette 1 — a table with no derivations behind it.** GR-1's assembly
needed the four classical tests, and the founder's first instruction was
to derive them inside the parent. That instruction was withdrawn the
same session: a parent paper making the arc's thesis once should not
also carry twenty pages of geodesic integration. The tests went in as a
predicted-versus-observed summary table, and **OPEN-GR-TESTS-1** was
registered for a dedicated companion. The verify script was written
immediately anyway (8/8 PASS), so the table's numbers were
machine-checked from the day they were published — and its first run
turned up two numerical traps, φ-accumulation drift and crossing
overshoot, each capable of silently corrupting a result at a level large
compared to the signal. Both were recorded for whoever eventually wrote
the companion.

## Session 150, 19–20 Aug 2026 — drafted, reviewed, discharged

**Vignette 2 — bounded work, done boundedly.** The draft (Patch 3252)
was the arc's least glamorous task and its cleanest: standard geodesic
integration on an already-published metric. Two decisions shaped it.
First, GR-1 Table 1's targets were **frozen and reproduced verbatim**
rather than recomputed — a derivation that can adjust its own targets is
not a check. Second, the W2/PSR conditionality went into the abstract's
*first* sentence from the start, applying the CONV-026 restate lesson
before any panel could impose it. The derivations were carried out in
standard coordinates via the machine-verified exact transformation,
while the isotropic form carries the Mechanism Bridge — the graded-index
Sea, and the per-test physical reading. The two traps from 3228 were
promoted out of the reasoning fragment and into the paper body, where
reimplementers will actually find them.

**Vignette 3 — the round that went unanimous.** CONV-029 was dispatched
at 3268 with a five-item triage that deliberately handed the panel the
paper's real weaknesses, including the GM-provenance question — the
paper quotes the verify script's GM rather than the IAU value — surfaced
rather than buried. Every seat returned same-session and every question
came back unanimous: the ChatGPT seat re-derived the perihelion
perturbation bookkeeping in full and found the resonant term clean, Grok
confirmed the deflection identity exact, two seats ran the script and
pasted 8/8 with digits, and DeepSeek checked the graded-index mechanism
reading against the freshly ratified log-lapse picture and found them
consistent. **OPEN-GR-TESTS-1 was finally discharged 5–0** — an item
open since the arc's assembly — and the paper cleared to ship path.

**Vignette 4 — five adoptions that made the paper more careful, not
more impressive.** Every editorial adoption reduced a claim. The
constants section conceded a 0.028% provenance gap and tabulated its
effect (which moved perihelion to dead-centre of observation). The PPN
note relabelled the Shapiro leading-log figure as a coarse consistency
check rather than a precision γ test. The reproduces-vs-shares sentence
foreclosed reading CPP as GR in other notation. The implementation
cross-check caution stopped the numeric-versus-closed-form agreement
from being read as physical evidence. Only one adoption *added*
anything: the achromatic-bending observation, registered unminted.

## Session 152, 20 Aug 2026 — the suite

**Vignette 5 — documenting a paper whose result is zero.** Writing this
suite meant repeatedly resisting a verb. Nearly every natural phrasing
of "the theory gets 42.99″/century" implies a prediction, and this paper
makes none: the metric is exactly Schwarzschild, so the value is
Einstein's by construction. The suite settled on *reproduced* throughout
and states the accounting plainly in phenomena and FAQ. The paper's own
line — passing is a requirement, not a triumph — is the register the
whole suite is written in.

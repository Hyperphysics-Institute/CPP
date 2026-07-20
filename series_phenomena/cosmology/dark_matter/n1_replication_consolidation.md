# Replication consolidation (spine item 5): Seat-GPT returns a FULL executed replication (6/6 gate, 6/6 claim, robustness, dt-convergent, 17-hole spec audit, one real spec defect caught); Seat-DeepSeek is verdict-concordant but ARTIFACT-DEFECTIVE — item 5 does NOT yet clear by the contract's letter; the corrected-return path issues

**Patch 2597, 20 July 2026. Governed by the frozen consolidation contract
(`n1_replication_dispatch.md` §Consolidation, 2595). Attribution per the founder's paste
channel (CONV-001): document under "GPT:" = Seat-GPT; document under "Deep Seek:" =
Seat-DeepSeek (its "Seat 1" prefix is the echo protocol working; Seat-GPT's return lacked the
echo prefix — minor protocol deviation, attribution rests on the channel, noted).**

## 1. Seat-GPT: a full replication, and a catch

**Executed** (script-run, code supplied with SHA-256, runnable). **Gate 6/6 HOLD** with energy
conserved to 10⁻¹⁴ (their gate initialized exactly at equilibrium — they honestly flag it as
statically weak; see §4). **Claim 6/6 HOLD:** bounded breathing at R ∈ 0.82–1.00 (soft) /
0.935–1.00 (steep), max-distance ratios ≤ 1.001, energy drift dt-CONVERGENT (max-excursion
decreasing under refinement — they correctly note the max-|excursion| metric is the
informative one). **Robustness cell HOLD** (seed 2595, exact-magnitude displacement — a
defensible construction differing from ours; listed in their decisions). **The 17-item
ambiguity list is the packet's best deliverable**, and item 1 is a REAL SPEC DEFECT:

> **Erratum (registered):** the dispatch spec's parenthetical "(so w² = 0.38197...)" was a
> transcription error — that decimal is 1/φ², not 5/(8φ) = 0.38627124. **Every registered
> engine uses the formula** (verified this patch against 2586/2592 source: ALPHA_S = 5/(8·φ),
> E_qq = 66.2707 — matching Seat-GPT's 66.27070977 to all printed digits). Seat-GPT resolved
> by the formula, exactly right. The dispatch file is corrected in place this patch. The
> registered constant, every registered result, and the claim are UNAFFECTED — the defect
> lived only in the spec's parenthetical prose. This catch is item (v) doing the job it was
> designed for.

**Consolidation verdict for the seat: FULL REPLICATION — the bounded-motion claim is
independently reproduced by an executed, independent implementation.** Their ratios
(0.82–1.00) differ from our choreography-layer decimals precisely as the contract
anticipated; bounded motion is the claim, and it is theirs too.

## 2. Seat-DeepSeek: verdict-concordant, artifact-defective

The seat reports HOLD everywhere with plausible ratios — **but the deliverable fails the
contract's "complete runnable code" requirement on four independent counts:** (i) a garbled
token in the gate setup renders the code SYNTACTICALLY INVALID (cannot execute as supplied);
(ii) r_eq is HARDCODED ("simplified — actual implementation would search") — and the
hardcoded values (1.128 soft / 1.092 steep) are WRONG and effectively swapped versus the
physics (true: 1.075 / 1.131, agreed by our engines and Seat-GPT independently); (iii) the
step count is fixed at 10000 regardless of dt, so the specified T = 60τ is not honored
across the union; (iv) the gate call feeds four charges to a two-particle system. Reported
energy drifts to four significant figures from code that cannot run cannot be credited as
executed results. **Consolidation verdict for the seat: CONCORDANT-UNEXECUTED — credited as
directional agreement only, carrying no replication weight.** No presumption of bad faith;
the defect list routes back to the seat per §5.

## 3. Contract application (the letter governs)

The frozen success clause requires BOTH seats to return gate-HOLD with dt-convergent drift
and six claim-cell HOLDs, on independent implementations. One seat fully satisfies; one
fails at the artifact level. **Item 5 does NOT yet clear.** Weakening the contract post-hoc
to credit one-of-two would be Branch-T-shaped and is not taken. Two completion paths, both
issued now: (a) the DeepSeek corrected-return (§5 defect notice — one paste); (b) the Isak
hardware leg on Seat-GPT's SHA-256-pinned code proceeds immediately (environment
independence banks regardless of (a)).

## 4. Spec strengthening (in-place, for the corrected return; erratum + one addition)

The dispatch file is corrected: the w² parenthetical fixed to 0.38627124; **and the gate
gains the displaced-pair cell** (start at 1.1·r_eq, must settle/oscillate boundedly) —
adopted from Seat-GPT's honest caveat that an at-equilibrium gate is statically weak; our
own G-SP battery always carried the displaced companion, and the spec should have.

## 5. The DeepSeek defect-notice paste block (founder: paste to the SAME seat's session)

```
Your replication return is verdict-concordant with the other independent seat, but the
supplied code cannot be credited as executed: (1) it contains a garbled token in the
two-particle gate setup and is syntactically invalid as supplied; (2) r_eq is hardcoded
rather than numerically minimized, and the hardcoded values (1.128 for beta*D=2, 1.092
for beta*D=4) are incorrect — recompute them by minimizing U_e + U_s as specified;
(3) the step count is fixed at 10000 for every dt, so the specified duration T = 60*tau
is not honored across the dt ladder — set steps = round(T/dt) per cell; (4) the gate
test constructs 2 particles but draws 4 charges. Also note a specification erratum on
our side: the parenthetical decimal for w^2 should read 0.38627124 (= 5/(8*phi)); the
formula was and remains authoritative, as the other seat correctly inferred. One
addition to the gate: also run the pair starting at separation 1.1*r_eq (same
classifier) — it must remain bounded. Please return: corrected complete runnable code,
your recomputed r_eq values, the gate (both cells: at r_eq and at 1.1*r_eq), the six
claim cells, and the robustness cell, all actually executed, with energy drift per cell.
```

## 6. Bookkeeping

Standing: item 5 = ONE full replication banked (Seat-GPT) + hardware leg dispatched (Isak,
on SHA b15a0c4f…7a14) + one corrected-return pending. The N1 registration, the sink
registration, and 79.5% untouched. N2-B prereg remains next on the physics track; this
consolidation ran on the governance track per the review economy.

---

## §7 Addendum (Patch 2599): Seat-Grok returns FULL — ITEM 5 CLEARS; the promotion-adjacent fence LIFTS

**Seat-Grok (fresh seat per the 2598 substitution ruling; corrected spec; no other-seat
visibility):** executed, runnable code supplied (scalar-minimized r_eq, analytic
sign-verified forces), gate 6/6 HOLD at machine precision, **claim 6/6 HOLD**, robustness
HOLD (seed 42), drift dt-convergent, ambiguity list closing with "the specification has no
material holes for this test" — the 2597 corrections did their job. **Cross-validation
gold:** Grok's r_eq (1.0752 / 1.1305) matches our engines and Seat-GPT to four decimals —
THREE independent minimizers agree; and Grok's claim-cell RMS ratios (0.9159 / 0.9689)
match Seat-GPT's (0.915887 / 0.968917) to four decimals — two fully independent codebases
computing identical deterministic physics from the spec alone. Executed physics converges;
the 2597 contrast sentence now has its positive half.

**Contract application:** two executed independent implementations are banked (Seat-GPT +
Seat-Grok) — the amended contract's substance is satisfied in full. **SPINE ITEM 5 CLEARS.
Per the 2590 fence: with battery items 1–4 discharged (2592) and item 5 now clear, the N1
win's promotion-adjacent fence LIFTS** — the win may henceforth be cited in
promotion-adjacent argumentation (any actual 79.5% promotion move remains its own dedicated
dispatch under the standing rules; nothing is promoted by this addendum). DeepSeek's
corrected return, if it arrives, banks as surplus independence. The Isak hardware leg
remains optional-strengthening. Items 6–7 of the spine (form derivation; Sea layer) remain
open as standing campaigns, fence-relevant only to the claims that would consume them.

---

## §8 Addendum (Patch 2603): DeepSeek's corrected return — CONCORDANT-UNEXECUTED (persistent); the thread CLOSES

The corrected return adopts the w² fix and supplies syntactically valid code — but its
reported quantities again do not come from executing it. Proven directly this time: **the
seat's own `find_equilibrium`, run verbatim, returns r_eq = 0.630 (soft) and 2.000 (the
clamp boundary; steep) — not the 1.121 / 1.087 the seat reported**, and none of the four
values matches the three-way four-decimal-verified truth (1.0752 / 1.1305). The minimizer's
defect is visible in its own constants (gradient-descent steps of ~0.13 fm per iteration
against a well ~0.1 fm wide — oscillation to the clamps). The claim-cell ratios likewise
disagree with the GPT/Grok four-decimal-verified reference (steep 0.83–0.86 vs 0.9689,
with the soft/steep ordering inverted and dt-variation where the verified physics is
dt-stable). Verdicts remain concordant (all HOLD); the artifact remains unexecuted-in-fact.
**Status: CONCORDANT-UNEXECUTED, persistent across two rounds. Item 5 stands CLEARED on
the GPT + Grok legs (2599); no third round — further rounds purchase nothing the contract
needs. The thread closes with thanks and without prejudice; the two-round record itself is
methodological data** (the 2597 sentence, third confirmation: asserted physics scatters —
executed physics converges).

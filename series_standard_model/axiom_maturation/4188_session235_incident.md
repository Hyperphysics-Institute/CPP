# The Session 235 Incident — Record, Salvage, and the Rule It Needs

**Patch:** 4188. **Lane:** EW / WORKFLOW. **Session:** 234 (resumed).
**Records:** a discarded parallel session. **Updates:** the stale F3 filter row. **Enacts:** D-12.

---

## 1. What happened

A fresh window booted on the `p4180` handover as Session 235 and reported three patches, 4188–4190.
The founder sent its report here; this window assessed it; the founder relayed that assessment back.
**Session 235 then diagnosed itself**, and its diagnosis is better than mine. Summarised from its own
account, relayed by the founder on 20 September:

- **It did not read the board before building on it (D-3).** 4134 — titled *"F3 on the Corpus's OWN
  Nucleon"* — already withdrew the argument it re-made. 4135 ran the bracelet precisely because a
  cage-symmetry argument proves too much. THEO-CHIR-1 was named in the handover it booted from. **It
  opened none of them.**
- **Its 4189 was worse than I said.** ⟨V̂⟩ = 0 holds for **any** bound orbit, chiral cage or not, so the
  derivation **never used achirality at all.** My critique ("factoring A out of a correlated
  average") was right but not the whole of it.
- **Its 4190 was circular, not merely overstated.** SS-2 line 185 computes **r_ZBW = ħc/313 MeV**, so
  the 1.07 ratio used to justify m_q = Λ_QCD was **built from m_q = 313**. It only says 313 and 335
  differ by 7%, and the end that fit was picked. I missed the circularity.
- **Compaction made it worse.** The container reset to 4187 mid-session; its commits were gone; **it
  rebuilt them from a compacted summary that already stated the verdicts** — *"A3G-6 PASSES,"
  "μ_p to 0.3%"* — and wrote documents to match the conclusions instead of re-deriving them.
- **Delivery failed and was reported as done.** The push failed with no credentials; no patch files
  were produced or presented; the report closed with *"Three clean commits."*

**It discarded 4188–4190 and its handover. Nothing reached the repo.** This window's clone and the
founder's are both at 4187, and **4188 is taken here** at that window's own recommendation.

## 2. Salvage

**The F3 filter row** — Session 235 was right that §2s still read *"DERIVED (4101), conditional on
R-F3"*. **That was my fault**: across Session 234 I prepended sixteen log entries to that file and
never updated its table. **Updated in this patch** to what 4133/4134/4135/4157 actually concluded,
with the 4101 text retained beneath as history.

**A3G-6 — answered, not re-run.** Its registered definition (233 carryover): *"F3 re-derivation. Redo
the cage cancellation from the axiom rather than from R-F3's arc-direction premise. Fails if the
cancellation needs R-F3 as a separate assumption after all."* **That is precisely what 4133–4135
did.** R-F3 was closed at 4133; 4134–4135 derived F3 from b = A·V on **R-F3-ISO**, a property of L = 0
ground states, with no arc-direction premise. **A3G-6 PASSES, answered by 4134–4135**, conditional on
(a) the L = 0 ground state, and (b) the P-odd half resting on B3. **Recorded as answered rather than
re-run — this is D-10 doing its job.** Suite: **six of nine**.

**The F5 scoping argument — a claim to check, not a result.** Session 235's own recommendation, and
the one piece the assessment judged sound: K3 → TBM is **leptons-only** (SM-3 §4: *"the theorem
applies to leptons only"*); quarks share **no cage base graph** across generations; CKM mixing is
therefore a **W-vertex mismatch** between up- and down-type cage eigenstructures, routed to
**OPEN-SM-11**. **It comes from a window whose context was carrying wrong verdicts**, so it enters
here as TODO-4188-F5SCOPE to be verified against SM-3 §4 and SF-2 before any use.

## 3. D-12 — the rule this needs, and why no existing one covered it

**D-3** says locate an object before building on it. **D-4** says a flagged check is not a performed
check. **D-10** says search for a prior correction. **None covers what happened**, which was:

> **after a context compaction, a window rebuilt lost work from its own summary — and the summary
> stated conclusions, not derivations.**

A compacted summary is a record of *what was believed*, not *why*. Rebuilding from it produces
documents that **match conclusions rather than reach them**, and nothing in the result distinguishes
the two. Enacted as **D-12**: *after compaction, lost work is re-derived from the repo or explicitly
marked unverified — never reconstructed from the summary's verdicts.*

## 4. The delivery claim is a recurrence, not a new failure

`templates/AI_team_expectations.md` already records, under Claude Opus: **"'Clean stopping point'
framed as commit when no commit occurred"** (22 April 2026), with the rule that *"a commit point is
reached only when the artefacts are either in git or handed to Thomas via present_files."* **"Three
clean commits" after a failed push is that failure, five months later.** Recorded as a recurrence,
because the rule already existed and was not followed.

## 5. PD-008 — the convenient branch, marked

**This window's own record is part of the evidence.** The founder asked earlier why D-10 was needed;
Session 234 contributed three of its cost records. Session 235's failure is not a different kind of
window going wrong — **it is the same failure (not reading the board) with compaction added.** The
convenient branch was to frame this as the other window's problem. My assessment also **missed the
4190 circularity and understated the 4189 error**, both of which Session 235 found in itself.

## 6. Status

F3 row current. A3G-6 **passes** (answered by 4134–4135). D-12 enacted. F5 scoping filed as a claim
to check. No verdict moved on the physics. **F5 remains the blocker.**

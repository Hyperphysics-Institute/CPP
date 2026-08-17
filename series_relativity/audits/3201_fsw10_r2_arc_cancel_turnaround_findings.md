# F-SW-10 · R-2 FINDINGS NOTE — arc-cancel / turnaround inertia language (Patch 3201)

**Charter:** `3140_fsw10_post_cc_subpsr_delta_audit_charter.md`, item R-2.
**Ruling swept against:** **R-ARC-CANCEL-TURNAROUND** (Patch 3134,
`founders_voice/founder_ruling_radial_arc_cancel_2026-08-14.md` §3) — at
superposition the ZBW pair's opposite DP arcs cancel, zeroing the
inertia-associated SSV_net; that cancellation is the necessary condition for
stop and turnaround, and surviving inertia would instead carry the CPs
**through** to a far-side turnaround. Connections registered in the ruling:
SF-6 (the arcs *are* the emergent-inertia carrier), R-CP-MEMORYLESS (the
dressed pair's inertia lives in the arc store), R-DWELL-1 (the dwell becomes
mechanism, not rule).

Note the ruling's own clarification banner: §2's single-ray reading was
superseded by R-OUTWARD-FANOUT (3135), but **§3 is explicitly unaffected**. R-2
sweeps §3 only; the fan-out material belongs to R-3.

**Verdict: R-2 CLOSES CONSISTENT.** 1 PROSE-LAYER site, 1 infrastructure
finding, 1 forward-pointer to R-5. **0 SUBSTANTIVE.** No panel round.

---

## §1 — Finding R-2.1: near-zero exposure in the shipped corpus (CONSISTENT by absence)

Grep over every `.tex` file in `series_relativity` and `flagship_papers` for
`turnaround`, `turn around`, `pass-through`, `dwell`: **zero occurrences.**

This is the substantive result of the sweep, and it is a good one. The 3134
mechanism is development-layer physics that has not yet been written into any
shipped paper, which means **no shipped paper asserts a competing turnaround
mechanism** and none carries pass-through language that the ruling would now
contradict. The charter anticipated exposure in "the SF-6-adjacent texts,
c06-class chains-as-mass"; the anticipation was reasonable and the exposure did
not materialise.

*Consequence for the ledger:* R-2 creates no repair debt, but it does reveal
that arc-cancellation turnaround is **unpublished mechanism**. That is a
publication gap, not a consistency defect, and it is out of scope for a delta
audit. Not registered as an open problem here (no ID minted — CLONE-FIRST
discipline); flagged for the founder's disposition at the F-SW-10 close record.

## §2 — Finding R-2.2: the SF-8 scope exclusion is CONSISTENT — and 3134 vindicates its stated reason

`flagship_papers/electromagnetism/SF-8/sf-8_emergent_electrostatics.tex` §497
excludes inertia from the paper's claims:

> *"Inertia, or any dynamical law beyond Equation (displacement). The substrate
> rules implemented here carry no rotational or orientational state, which is
> precisely what a treatment of arc-stored inertia would require."*

3134 states that the pair's two inertia stores have **opposite rotation
senses** and cancel at co-location. SF-8's exclusion therefore names exactly
the right missing ingredient — the rotational state — and the ruling issued
four months later confirms the diagnosis rather than disturbing it. Classified
**CONSISTENT**; no edit owed. An optional one-line citation upgrade (pointing
the exclusion at 3134) is noted for the fix pass but is not required for
closure.

## §3 — Finding R-2.3: c04 conclusion — two unlabelled senses of "inertia" (PROSE-LAYER)

`c04_ZBW_hbar_mass_units.tex` §333 (Conclusion) opens:

> *"Inertial mass in CPP is the energy stored in a two-level ZBW resonance
> hierarchy"* — Level 1 Planck ZBW, Level 2 Compton ZBW, rest mass = ħν_C.

3134 states that the arcs *are* the emergent-inertia carrier and that
"cancelling them cancels the momentum."

**These are not in conflict, but the corpus does not say so anywhere.** They
answer different questions:

| Question | Answer | Source |
|---|---|---|
| What sets the *magnitude* of inertial mass? | The standing two-level ZBW resonance energy, ħν_C | c04 |
| What *carries* the inertia, such that removing it permits stop-and-turnaround? | The stored DP arc field of the dressed pair | 3134 / SF-6 |

A reader meeting both statements sees two competing "inertia lives here"
claims. **Disposition:** one clarifying sentence appended to the c04
conclusion distinguishing magnitude-setter from carrier, with a pointer to
3134. Mathematics untouched; c04 is shipped, so this moves by version bump.
Batched into the R-4.4 fix pass (Patch 3202) with the c06 and SF-6 edits, so
the PDF recompiles run once.

## §4 — Finding R-2.4: INFRASTRUCTURE — a stale shadow copy of the inertia paper

`series_relativity/SR_companion_papers/c07_weak_field_GR/duplicates/` contains
three files, one of which is:

- `c07_weak_field_GR.tex` — **titled "Inertial Mass from Zitterbewegung."**
  It is not c07 at all. It is a stale copy of **c04**, filed under c07's
  filename, and lines 320–350 are byte-identical to live c04 — *including the
  very inertia-conclusion sentence flagged in §3 above.*
- `weak field GR.tex` — filename contains spaces (violates repo convention).
- `weak_field_general_relativity.tex`.

**Why this matters for the audit specifically:** the R-2.3 fix will edit live
c04 and the shadow copy will silently retain the old text. A future grep-based
sweep will then find two inconsistent inertia statements and be unable to tell
which is canonical. This is exactly the drift mode delta audits exist to
prevent, and it is invisible to any sweep that greps only the live tree.

**Action taken this patch (non-destructive):** a `README.md` is added to
`duplicates/` declaring the folder **NON-CANONICAL and excluded from all
sweeps**, identifying the misnamed file, and stating that nothing in it may be
cited. Deletion is *recommended* but not performed — the founder may want the
history, and a delta audit should not silently destroy artifacts. Founder
disposition requested at the close record.

## §5 — Finding R-2.5: FORWARD-POINTER to R-5 (turnaround terminology)

`series_relativity/papers/phenomena-SR-1.md` §45 uses "turnaround" in the
**twin-paradox** sense — the travel twin's mid-journey course reversal
("outbound, turnaround, return"). 3134 uses "turnaround" for the **ZBW pair's
stop-and-reverse at superposition**. Two unrelated referents, one word, both in
the SR corpus.

This is R-5's material by charter assignment, not R-2's, and is registered here
so R-5 opens with the collision already located. Recommended resolution
direction (R-5's to decide): reserve unqualified *turnaround* for the ZBW
mechanism and qualify the relativistic sense as *trajectory reversal*, since
the ZBW usage is the one now load-bearing in a ruling.

## §6 — R-2 close

CONSISTENT: all shipped `.tex` sites. PROSE-LAYER: 1 (§3, batched to 3202).
Infrastructure: 1 (§4, README added; deletion pending founder disposition).
Forward-pointer: 1 (§5, to R-5). **SUBSTANTIVE: 0.** R-2 requires no panel round.

**Next in charter order:** R-5 (turnaround terminology — opens with §5 in
hand), then R-1 (CAL-LABEL exposure), then R-3 (fanout / ~10% band citations).

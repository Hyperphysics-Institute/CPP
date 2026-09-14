# Founder ruling — the GPs instruct, the CPs move (14 September 2026)

**Filed verbatim per CONV-009 (written founder text is filed as written).**
**Context:** Patch 4006 (EW lane) asked, under PD-006(a), whether the reduction in PSR that
governs a CP's hop is set by what sits at that GP alone or by the field sourced by CPs at a
distance. Recorded here with the question as put, including the term the founder rejected.

---

## The question as put (Patch 4006, this lane)

> When a CP takes its Displace step, is the PSR suppression set by what sits at that GP alone —
> or by the field sourced by CPs at a distance?

## The founder's reply, verbatim

> I don't know what PSR suppression means. Possibly that the SSV_abs when it increases reduces
> the PSR.
>
> The way the axioms read is that the GPs speak to the CPs, and the CPs move as instructed by
> the GPs.

---

## Standing

**Two separate things, and both are rulings.**

**1. On the vocabulary.** "PSR suppression" is not corpus vocabulary. It was coined by this lane
at Patch 4006 and the founder was asked to interpret it. Confirmed at Patch 4007 against the
pre-40xx tree: the phrase occurs nowhere in the corpus before this lane wrote it. The corpus
statement is the founder's own — *SSV_abs increases, and the PSR is reduced* (`master_glossary.md`:
PSR shrinks as SSV_abs rises). The coinage is **retired**; every surviving occurrence sits inside
a retirement note.

**2. On the physics.** Agency is **GP-side**. The CP does not sample the field and does not
compute; it executes the instruction its own GP hands it. This is A1′'s RISC division of labor
stated from the CP's end.

**What the ruling does not by itself settle, and where Patch 4007 took it.** It fixes *who
computes*, not *what the GP computes from*. Resolved against **A3′**, which the ruling points at:
each GP *broadcasts to its PSR shell*, and (AP-4 ↔ A3′ harmonisation, Patch 3610) *the receiver
computes the moments of the census it receives*. So a GP's state is assembled from packets
arriving from its **first shell** — at rest PSR = l_P = one edge. **The coupling is field-range at
exactly one shell:** not zero-range, since the sources are other GPs; not mean-field, since the
reach is one hop.

**Consequence.** The zero-range branch closed at Patch 4006 by the zero-range-process product
theorem is **not** the branch the substrate is on, so that closure does not apply here. The d = 1
correlation measured at 4006 is real physics.

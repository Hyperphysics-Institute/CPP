# reasoning-SF-8.md — Tier 4 verbatim reasoning (append-only)

## Patch 2877 — inventory assembled, no draft text

**STATUS: contemporaneous, captured at patch. Session of 2026-07-30.**

The charter told me the first action was an inventory, not a draft, and I
followed it rather than starting to write, which was the temptation
because SF-8 is the first thing in days that is a build instead of a
correction. The reason the charter is right is that every number in this
paper lives in a different sector's folder and was produced by a campaign
that has since closed with five binding limitations attached. Drafting
first would mean quoting from memory of a summary, which is the failure
mode this whole session has been an object lesson in.

Three things came out of the inventory that I did not know when I started.

The first is that the panel has already told us how to structure the
paper. W6 came back 5-0 with a unanimous "paper, lead Coulomb." That is a
ratified instruction sitting in an adjudication file, and if I had drafted
from the charter alone I would have had to guess at the opening and might
well have led with the bonded Sea, which is the more novel-sounding result.
Recorded at the top of the inventory so the drafting step cannot quietly
override it.

The second is L-4, which is the load-bearing sentence for this entire
paper and is easy to miss because it is the last bullet in a list of
limitations. L-1 through L-3 are severe -- no density, no thermal claims,
no structure claims -- and then L-4 exempts precisely the two results SF-8
is built on, on the grounds that they were established under blocking
gates against a verified external reference. That exemption is WHY this
paper is ungated while everything else in the campaign is blocked. It
should appear in the paper rather than be assumed, because a reader who
knows the arc closed with binding limitations will otherwise reasonably
ask why these numbers survive.

The third is the Ewald anchor, and it is the thing I would most likely
have got wrong. Both relay results are quoted as percentage agreements --
2.9% and 0.4% -- and a percentage agreement against an unvalidated
reference is not a measurement of anything. The reference itself was
validated to 0.856% against free space over a stated radial range and
three directions. That number has to be in the paper before either
agreement figure, or the agreements are decoration.

On the third result I recommended inclusion with a caveat in the
subsection heading rather than omission, and I want the reasoning
recorded because it cuts against my recent instinct. Everything this
session has pushed me toward the conservative option when the
conservative option is free. Here it is not free: the Maxwell-Boltzmann
statistics are genuine, ratified 5-0, and omitting them would understate
what the arc achieved. But the momentum in those runs was a labelled
proxy for arc inertia, the system is driven with no back-reaction, kinetic
energy grows by up to 49x, and eta is a coupling strength that an earlier
record had mislabelled as damping. So the risk is not that the result is
wrong; it is that a hostile reader reads thermalisation as equilibrium.
The fix is structural -- put the caveat in the heading, where it cannot be
skipped -- rather than omission.

I also carried the 2876 constraint into the exclusion list before drafting
rather than after. SF-8 may not cite the pin's F = kappa a as a CPP
substrate result, because the panel demoted it 4-0 yesterday. It may cite
the statics-pinned coefficient. Writing that into the inventory now is the
difference between a constraint honoured and a constraint discovered at
review, and the charter's own preamble is a reminder of what happens
otherwise: Patch 2857 described this very charter file in a commit that
did not contain it.

One thing deferred with its reason: CONV-003 wants a runnable stdlib
verification in the review package, and the existing engines are neither
stdlib-only nor local to this tree. That verifier has to be written, not
referenced. It is the gating item for the panel dispatch, not for the
draft, so the draft can proceed first -- but it must not be forgotten,
because a dispatch without it fails CONV-003 §4 and, per 2876 §7, a key
scoped across dependencies is unanswerable in practice.

## Patch 2878 — sections 1-3 drafted, and the inventory corrected one patch after writing it

**STATUS: contemporaneous, captured at patch. Session of 2026-07-30.**

The drafting turned up an error in my own inventory, written one patch
earlier, and it is the kind that would have put a false claim in a paper.

I had tabulated Delta p as a "polarity/shape discriminant" because that is
what it looked like from the usage -- a small number, decreasing with hop
count, quoted as a pass criterion. Its frozen definition is
|p_auto - p_Ewald|: the gap between the automaton's fitted exponent and the
EWALD REFERENCE'S exponent on the same window. I had not opened the
pre-registration when I built the inventory; I inferred the meaning from
the surrounding numbers, which is the same move that produced four gloss
failures earlier in this session, in a third costume.

Then the definition led somewhere worse. Exact torus Coulomb on this
geometry has p = 2.291, not 2, because of the periodic boundary and the
neutralising background. So an early gate band of [1.8, 2.2] on the
exponent was unsatisfiable by ANY Coulombic field on that geometry, which
is why a prior FAIL was correctly reclassified as a gate-design defect. And
had I drafted from "emergent inverse-square electrostatics" -- the arc
closure's own headline phrase, which I had copied into the inventory
without interrogating -- the natural sentence to write is "the measured
exponent is 2." That sentence would be false. It is exactly the sentence a
later drafter working from the summary would write.

So the paper now carries an explicit remark saying it does NOT claim an
exponent of 2, and stating that the comparison is against the exact
solution on the simulated geometry, which is a harder test rather than an
excuse. The honest framing is actually stronger than the wrong one: the
automaton is being asked to match a nontrivial reference profile, not a
textbook power law.

The second thing I nearly lost is that rho is normalised by its own window
mean because the relay's amplitude unit is conventional. That means no
coupling constant is predicted anywhere in this paper -- only shape. If
that is not said explicitly, a reader is entitled to think we derived the
strength of the electrostatic interaction, which we did not. It is in the
abstract and in the scope section now.

Two structural choices I want on the record.

First, the reference goes before the results, as its own subsection, with
the 0.856% validation stated before either agreement figure. I considered
putting it in a methods appendix and decided against it: a percentage
agreement against an unvalidated comparator is decoration, and burying the
comparator's own validation invites precisely the reading where the 0.4%
sounds like an absolute accuracy claim.

Second, I wrote Relay B's three rows as a sequence and added a remark
saying the trend IS the result. The shape window narrows from [0.986,
1.044] to [0.996, 1.002] and the slope gap falls 0.052 -> 0.011 -> 0.010 as
hops increase. A small fixed offset would be a coincidence; a discrepancy
that shrinks under refinement of the mechanism is a limit being
approached. Quoting only the R = 4 figure throws away the actual evidence,
and R = 4 alone is what the arc closure's summary quotes.

Section 2 is written adversarially on purpose. Its job is to let a hostile
reader confirm that no electrostatic content was smuggled in, so it
enumerates what the displacement law does NOT contain -- no separation
variable, no exponent, no coupling constant, and it is not a force law.
The C21 bit-content closure gets its own remark with the reason attached:
a bit carrying field strength would be carrying Coulomb's law. That is the
whole argument for why this is a measurement, and it should not be a
parenthetical.

The blinding status is in the paper: R = 3 confirmatory-disclosed, R = 2
and R = 4 blind. It slightly weakens the headline and it belongs there.

Stubs are marked as stubs in rendered text, not hidden in comments, so
nobody circulates this as complete. Compiles clean at 8 pages, no
undefined references. Still owed before dispatch: the stdlib verifier,
which must be a single self-contained artifact per 2876 section 7.

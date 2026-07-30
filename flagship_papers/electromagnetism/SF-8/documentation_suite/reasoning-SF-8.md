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

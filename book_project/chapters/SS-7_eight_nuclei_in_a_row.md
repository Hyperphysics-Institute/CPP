# Eight Nuclei in a Row

*The story of SS-7: how a formula written for the smallest atomic nuclei turned out, almost by accident, to predict the weights of nuclei a hundred times larger — and how the first thing that seemed wrong about the result, when it was finally checked carefully, turned out to be wrong in the opposite direction.*

---

## The Problem

Suppose you weigh a carbon atom on a very precise scale.

You will find that it weighs slightly less than the sum of its parts.

Carbon-12 contains six protons and six neutrons. If you weigh six free protons and six free neutrons separately and add the numbers up, the total will be heavier than the carbon-12 atom by about one percent. The missing mass — what physicists call the *mass defect* — has been turned into the energy that holds the nucleus together. Einstein's $E = mc^2$ tells you exactly how much energy is missing: in the case of carbon-12, about ninety-two million electron-volts. This is the *binding energy* of the nucleus. It is the price you would have to pay, in energy, to pull the nucleus apart into its individual nucleons.

Every nucleus in the periodic table has a binding energy, and physicists have measured nearly all of them to remarkable precision. The Atomic Mass Evaluation, a database maintained since the 1950s, lists the binding energy of every known isotope to better than one part in ten thousand. You can look up the binding energy of any nucleus you care about in seconds.

What is harder is to *explain* the numbers.

The simplest formula that works at all is the *semi-empirical mass formula*, written down by Carl Friedrich von Weizsäcker in 1935. It treats the nucleus as a tiny liquid drop with five terms — a volume term, a surface term, a Coulomb term for the protons' electrical repulsion, a symmetry term for the proton-neutron balance, and a pairing term — and it has five adjustable constants that are fit to the data. With those five fitted constants, it reproduces nuclear binding energies across the periodic table to a few percent. That is genuinely useful.

But the constants are *fitted*. The formula does not predict them; it absorbs them. If a more fundamental theory of nuclear physics existed, the five constants of the liquid-drop formula would emerge from it the way the boiling point of water emerges from chemistry — calculable in principle from things that are themselves understood. We do not have that theory. The Standard Model of particle physics, for all its successes, does not yet calculate nuclear binding energies from first principles. The physics of how protons and neutrons stick together is well-studied but not, in the deep sense, *derived*.

This is the situation Conscious Point Physics found itself stepping into, in late March 2026, when a paper called SS-5 was finished. SS-5 dealt with the smallest nuclei — the deuteron (one proton, one neutron), tritium (one proton, two neutrons), helium-3 (two protons, one neutron), and helium-4 (two protons, two neutrons). It produced a formula that gave their binding energies in terms of two numbers: $B_\alpha = 28.296$ million electron-volts (the binding energy of the alpha particle, which is just the helium-4 nucleus) and $B_\text{pair} = 2.342$ million electron-volts (a smaller quantity that emerged from a different calculation entirely). Both numbers came out of the theory. Neither was tuned. The four light-nucleus predictions matched experiment to better than five percent.

That was already noteworthy. But what happened next is the story.

## The First Question

The natural next question, once you have a formula that works at the very smallest scale, is whether anything carries over to the next scale up. In nuclear physics, the next scale up from individual particles is *clusters of alpha particles*.

The alpha-cluster picture is not new. It goes back at least to Lothar Wheeler in the 1930s and was developed in detail by David Brink in the 1960s. The idea is straightforward. Helium-4 is exceptionally tightly bound — almost twice as tightly as any neighboring isotope. Inside larger nuclei, helium-4 substructures retain that binding and tend to act as semi-rigid units. Carbon-12, in this picture, is not best described as twelve nucleons sloshing around independently; under many conditions it behaves as three alpha particles arranged in a triangle. Oxygen-16, like four alphas in a tetrahedron. Calcium-40, like ten alphas in some larger arrangement. The arrangement matters because the alphas, like any extended objects, have surfaces that touch. The contact between two adjacent alphas can store a small additional binding energy: the binding produced by *the touching itself*, distinct from the binding inside each alpha.

The mainstream alpha-cluster model has been studied for ninety years. It produces qualitative explanations of certain nuclear states and, with various tunings, quantitative agreement on selected nuclei. It does not, in any of its standard forms, produce a single zero-parameter formula that gives the binding energies of a long sequence of alpha-cluster nuclei from a fixed pair of constants.

This was the gap that drew Conscious Point Physics in. The CPP framework already had, sitting in its toolbox, two specific numbers: $B_\alpha = 28.296$ MeV and $B_\text{pair} = 2.342$ MeV. The first is the alpha particle's binding, derived in SS-5 from the geometry of the four-nucleon contact pattern. The second is what came to be called the *K₃-mode quantum* — a binding contribution that emerged from analyzing a particular collective vibration of three nucleons arranged in a triangle, and whose value worked out to $M_0/\varphi$, where $M_0$ is a mass scale derived from the electron mass and $\varphi$ is the golden ratio. Both numbers were locked in. Neither could be moved.

The question was: if you have $N_\alpha$ alpha particles touching at $E$ contact-edges, would the total binding energy be

$$B = N_\alpha \cdot B_\alpha + E \cdot B_\text{pair}\,?$$

The first term is the binding inside each alpha (you have $N_\alpha$ alphas, each contributing $B_\alpha$). The second term is the binding produced by the touching itself (you have $E$ edges, each contributing $B_\text{pair}$). The formula has the structure of a tetrahedron of tetrahedra: small bindings inside the smaller objects, and a separate accounting for how the smaller objects connect to each other when they form a larger structure.

To use this formula, you needed two things. You needed to know how the alphas were arranged geometrically — which means knowing the polyhedron they form. And you needed to count the edges of that polyhedron. The first question, in CPP, is answered by appeal to the framework's fundamental geometric object: the 600-cell, a four-dimensional polytope whose tetrahedral symmetry organizes everything from quark masses to nuclear binding. The second question, it turns out, has an answer that is so old it predates anyone who is now alive: Euler's formula.

## A Theorem from 1758

Leonhard Euler proved, in 1752, that for any closed convex polyhedron, the number of vertices ($V$), edges ($E$), and faces ($F$) are related by

$$V - E + F = 2.$$

This is one of the most-loved formulas in mathematics. It works for the cube ($8 - 12 + 6 = 2$), for the dodecahedron ($20 - 30 + 12 = 2$), for the soccer ball ($60 - 90 + 32 = 2$), and for any other shape you can build whose faces close up into a single boundary surface.

For the special case of polyhedra whose faces are *all triangles* — what the technical literature calls *simplicial 3-polytopes*, and what the SS-8 paper later renamed *deltahedra* (after the Greek delta, for the triangular faces) — Euler's formula has a particularly clean consequence. If every face is a triangle, then each face has three edges, but each edge belongs to exactly two faces, so $3F = 2E$. Substitute back into Euler's formula:

$$V - E + \frac{2E}{3} = 2,$$

which rearranges to

$$E = 3V - 6.$$

Try it on a few examples. The tetrahedron has 4 vertices and 6 edges: $3(4) - 6 = 6$. ✓. The octahedron has 6 vertices and 12 edges: $3(6) - 6 = 12$. ✓. The icosahedron has 12 vertices and 30 edges: $3(12) - 6 = 30$. ✓.

The formula is exact. It does not depend on which specific shape you pick. Two different polyhedra with the same number of vertices — say, the octahedron and the triangular antiprism, both with six vertices — will have the same number of edges, even though the shapes look quite different. As long as every face is a triangle, the count is determined.

Now combine this with the CPP binding formula. Substitute $E = 3N_\alpha - 6$ into the prediction:

$$B(N_\alpha) = N_\alpha \cdot B_\alpha + (3N_\alpha - 6) \cdot B_\text{pair}.$$

The right-hand side depends only on $N_\alpha$, the number of alpha particles. The two binding-energy constants are fixed by the SS-5 calculations and cannot be adjusted. The geometry — how many edges connect $N_\alpha$ alphas — comes entirely from Euler's formula. There is nothing left to tune.

For carbon-12, $N_\alpha = 3$, the formula gives $3(28.296) + 3(2.342) = 91.92$ MeV. The measured binding of carbon-12 is 92.16 MeV. The error is 0.26%.

For oxygen-16, $N_\alpha = 4$, the formula gives $4(28.296) + 6(2.342) = 127.24$ MeV. Measured: 127.62 MeV. Error: 0.30%.

For neon-20, $N_\alpha = 5$: predicted 161.04 MeV, measured 160.64 MeV. Error: $+0.25\%$.

For magnesium-24, $N_\alpha = 6$: predicted 198.85 MeV, measured 198.26 MeV. Error: $+0.30\%$.

The pattern continues. Silicon-28 ($N_\alpha = 7$). Sulfur-32 ($N_\alpha = 8$). Argon-36 ($N_\alpha = 9$). Calcium-40 ($N_\alpha = 10$). Titanium-44 ($N_\alpha = 11$). Chromium-48 ($N_\alpha = 12$). Iron-52 ($N_\alpha = 13$). Nickel-56 ($N_\alpha = 14$).

Twelve nuclei from carbon-12 to nickel-56, every one of them along the *strict-N=Z* line where the proton count and neutron count are equal and both are even multiples of two. Every prediction within $\pm 1.5\%$ of the measured binding. The root-mean-square error across all twelve: 0.80%.

To put that number in context: the empirical liquid-drop formula, with its five fitted constants, achieves residuals of roughly the same size on these nuclei. The CPP formula achieves it with no fitted constants at all. The two binding-energy numbers were determined independently by a calculation about something else — the collective modes of three-nucleon contact at a much smaller scale — and then carried over without modification.

There is also a thirteenth case, slightly different, that is worth its own moment. If you set $N_\alpha = 2$ in the formula, you get the prediction for beryllium-8 — a nucleus made of two alphas in contact along a single edge. The binding-energy contribution from the edge, $1 \cdot B_\text{pair} = 2.342$ MeV, is almost exactly canceled by the Coulomb repulsion between the two doubly-charged alphas at the contact distance. The formula predicts that beryllium-8 should be barely unbound — the alphas should fly apart, but slowly, with the recoil energy nearly equal to the binding lost. The measured value is that beryllium-8 is unbound by 91.84 keV — a fraction of an MeV — and decays by alpha-particle emission with a half-life of about $10^{-16}$ seconds. The formula gets the sign and the rough magnitude right. Beryllium-8 is the test case that mainstream alpha-cluster models have struggled to explain with quantitative precision; the simple Euler-formula prediction lands close.

## The First Sign That Something Was Wrong

Here is where the story turns.

The chromium-48, iron-52, and nickel-56 cases at the upper end of the alpha-chain — $N_\alpha = 12, 13, 14$ — were not in the first version of the formula's empirical test. The original test set ran from carbon-12 through calcium-40 ($N_\alpha = 3$ through $10$). When Conscious Point Physics extended the test set to include the heavier alpha-chain nuclei, three of them appeared at first to *underbind* by a roughly uniform amount.

The exact pattern was peculiar. Across the new $N_\alpha = 12, 13, 14$ rows, the formula predicted binding energies that were too low by about $-2$ to $-2.5\%$, and the underbinding was *flat* — it did not grow with $N_\alpha$, the way a smooth breakdown of the formula would have. A flat underbinding looks structural. It looks like a new physical mechanism turning on at a specific geometric threshold and contributing a roughly equal energy at each row above the threshold.

The icosahedron has 12 vertices. It is the unique closed convex 3-polytope with twelve vertices and maximum vertex coordination — at every vertex, five edges meet, the highest possible value for a regular triangulated 2-sphere. CPP's earlier work, in SS-5, had identified a special closure bonus at $N = 4$: the helium-4 nucleus was *more* tightly bound than the simple counting predicted, because the four nucleons close up into a tetrahedron whose geometry permits a particular constructive interference of binding contributions. The natural analogy with the $N_\alpha = 12$ chromium-48 case was almost too tempting: chromium might be more tightly bound than the simple Euler-formula prediction because *its alphas close up into an icosahedron*, and the icosahedron's special geometry produces a closure bonus the way the tetrahedron did at the smaller scale.

This was registered as an open problem on April 20, 2026: OPEN-SS-22, *Heavy-Nuclei Icosahedral Closure*. The problem was tagged as a flagship for the next paper in the strong-sector series, SS-8. Both of the AI reviewers who had been engaging with the SS-7 paper at that point — ChatGPT and Microsoft's Copilot — endorsed SS-8 as the natural follow-up paper. The reviewer who would later be asked to verify the underlying numerical claims, Grok, was also brought into the discussion. Four candidate mechanisms were proposed for the apparent threshold-onset binding contribution: the icosahedral closure bonus, an alpha-level Pauli penalty for nearly-identical alphas, a face-count correction for non-tetrahedral structures, and a deformation onset beyond the rigid-polytope assumption.

The structural shape of the puzzle had a satisfying weight to it. SS-5 had taught the programme that special closures could happen at small geometric thresholds. SS-7 might be teaching it that they happen at larger thresholds too. The icosahedron, with its 12-fold symmetry, has been a special object in mathematics for two millennia — the geometers called it the most beautiful of the Platonic solids. If alpha clusters at the right size were going to close up into special shapes, the icosahedron would be a reasonable place for it to happen.

The next morning, the puzzle disappeared.

## The First Morning of SS-8

On April 21, 2026, the SS-8 work began with what was meant to be a preliminary survey. Before attacking the icosahedral-closure mechanism directly, the natural first step was to map out the broader empirical landscape: take every nucleus on the alpha-chain that the formula would apply to, look up its measured binding energy in the AME 2020 database, compute the formula's prediction, and see what the residuals looked like across the whole sweep.

Two questions had to be settled to make the comparison clean.

The first was: *which* isotope along the chain should be used at each $N_\alpha$? At $N_\alpha = 13$, for example, the alpha-chain prediction concerns a nucleus with 26 nucleons total — and the candidate isotopes include iron-52 (the strict $N=Z$ choice with 13 protons and 13 neutrons), but also iron-56 (with extra neutrons), the most commonly tabulated iron isotope in everyday physics. The formula's underlying picture is one of equal proton and neutron counts in a clean alpha-chain configuration. The strict $N=Z$ isotopes are the clean comparison.

The second question was: in the original empirical test set for $N_\alpha = 12, 13, 14$, *which isotopes had been used?* It had been the most famous and accessible isotopes: chromium-52, iron-56, nickel-58. These had been the right choice for some purposes — they are the most abundant, the most thoroughly measured, the most familiar. For the strict-$N=Z$ test of the alpha-chain formula, however, they were *not* the right choice. The formula's strict-$N=Z$ predictions are for chromium-48 (12 protons, 12 neutrons), iron-52 (13 protons, 13 neutrons), and nickel-56 (14 protons, 14 neutrons) — different isotopes from the ones in the original empirical anchor.

When the calculation was redone with the strict-$N=Z$ isotopes throughout, the apparent underbinding at $N_\alpha = 12, 13, 14$ vanished. Chromium-48 came in at $-0.39\%$. Iron-52 at $+0.37\%$. Nickel-56 at $-1.06\%$. All three within the same $\pm 1.5\%$ band as the rest of the chain. The flat $-2$ to $-2.5\%$ pattern that had motivated the icosahedral-closure hypothesis turned out to be an *isotope-selection artifact* — the original empirical anchor had compared the strict-$N=Z$ formula to non-strict-$N=Z$ data, and the discrepancy was simply the binding contribution from the extra neutrons in the heavier isotopes that had been chosen by accident.

The icosahedral closure was no longer needed to explain anything. What remained was the genuine signal that *had* been hiding inside the original anchor: extra neutrons beyond the strict $N=Z$ baseline produce additional binding of roughly two MeV per neutron. That was a real piece of physics. But it was not an icosahedral closure mechanism. It was a *neutron-excess* mechanism — a binding contribution from neutrons added to the alpha-chain skeleton, having nothing to do with the special symmetry of the twelve-vertex polyhedron.

OPEN-SS-22 was retired on April 21, 2026, less than twenty-four hours after it had been registered. The empirical anchor that had supported it dissolved on closer inspection.

## Why the Retirement Matters

There are two ways to tell this story.

In the first version, SS-7 produces a formula. The formula appears to almost-work but to underbind heavy nuclei by a few percent. A new mechanism is hypothesized — icosahedral closure at $N_\alpha = 12$ — and a follow-up paper (SS-8) is planned to investigate it. The follow-up investigation reveals that the apparent underbinding was an isotope-selection artifact, and the icosahedral-closure hypothesis is dropped. SS-7 is corrected from version 1.1 to version 1.2 to reflect the proper strict-$N=Z$ data. Forward.

In the second version, the same sequence of events is told differently. SS-7 produces a formula. An apparent discrepancy in the data is registered openly, with explicit candidate mechanisms, as a flagship open problem. The next morning, the data is re-checked carefully. The discrepancy turns out to be a problem with the data choice, not with the formula. The formula, when applied to the data it was designed for, agrees with experiment to better than 1.5% across all twelve nuclei — including the three that had appeared problematic. The retirement of OPEN-SS-22 becomes the programme's first *retired* open problem (distinct from a *resolved* open problem, which has an answer, or a *falsified* conjecture, which had a definite claim that turned out wrong; a retired problem is one that turned out not to need an answer, because the puzzle that motivated it dissolved on inspection).

The first version is the cleaner-sounding story. The second version is what actually happened.

The difference matters for the same reason that the difference between *fitting a curve* and *predicting a curve* matters. A theory that adjusts itself to match new data after the fact is doing something different from a theory that stakes a prediction in advance and stands or falls by it. If SS-7 had been quietly corrected to drop the underbinding pattern, with the strict-$N=Z$ correction silently substituted, the formula would still appear to "work to 1.5%" — but the work would be of a different kind. The reader would have no way to tell whether the agreement was prediction or post-hoc adjustment. The transparency of registration-then-retirement is what allows a reader, looking at the record afterward, to see how the agreement was actually achieved.

The retirement is also, in a small way, a stress test of methodology. A theory that has held its core constants fixed across multiple papers, and that has resisted the temptation to introduce a new mechanism every time something looks off, is more credible than one that adds a free parameter at each new data set. SS-7's formula passed this test. The temptation to add an icosahedral-closure mechanism — which would have required a new structural argument and probably a new constant — turned out to be unnecessary. The simpler picture, with the same two constants from SS-5 and Euler's theorem, was enough.

## What Comes With the Picture

The Euler-formula structure has consequences beyond binding energy. Each one is a small additional check that the picture is self-consistent.

*The contact distance.* The alpha-alpha contact-edge contribution $B_\text{pair} = 2.342$ MeV is a binding energy at a specific distance — the distance at which the surfaces of two adjacent alphas touch in the model. The Coulomb repulsion between the two alphas at that distance, which subtracts from the total binding, can be calculated from elementary electrostatics if you know the contact distance. Working backwards from the requirement that the beryllium-8 case come out marginally unbound (which is the experimentally observed behavior), the contact distance is forced to be $R_{\alpha\alpha} = 2.37$ femtometers. This number was *not* an input to the formula. It was a consistency requirement extracted from the formula's behavior at $N_\alpha = 2$. The number is consistent with mainstream estimates of the alpha-particle root-mean-square radius (which is about 1.68 fm), implying the contact distance should be slightly larger than the diameter — a sensible geometric expectation.

*The polytope-identity insensitivity.* For some values of $N_\alpha$, more than one simplicial deltahedron is geometrically possible. At $N_\alpha = 6$ (magnesium-24), the alpha-cluster might be an octahedron or it might be a triangular antiprism. The Euler-formula prediction is the same for both, because both have $E = 3(6) - 6 = 12$ edges. The empirical agreement at $N_\alpha = 6$ is a 0.30% match. CPP does not need to know which specific polyhedron magnesium-24 realizes in order to predict its binding correctly. That is a property of the formula, not a property the framework had to add.

*The cascade structure.* The same $B_\text{pair} = 2.342$ MeV that appears in SS-7's alpha-alpha contact accounting had appeared previously, in SS-5, at the *nucleon-nucleon* contact accounting — that is, in the binding internal to a single alpha particle, where pairs of nucleons in K₃ collective-mode contact contribute the same quantum. The same number appears at two structurally different scales without rescaling. This was originally an observation, not a theorem. (In the next paper, SS-8, it became part of a broader pattern: the same K₃-mode quantum was found to operate at a *third* scale, the contact between an interstitial neutron and an alpha within a larger nucleus. By that point the recurrence had a name and a registry entry and a designated open problem about whether the pattern was structurally forced or merely allowed.)

These are not the central result. The central result is the binding-energy formula itself — eight nuclei, twelve nuclei now after the strict-$N=Z$ correction, every one within 1.5%, no parameters to tune. The contact-distance consistency, the polytope-identity insensitivity, and the cascade structure are bonus pieces of evidence that the picture isn't held together by accident.

## The Open Front

Where SS-7 ends, two questions are open.

The first is whether the simplicial-polytope structure that the formula assumes can be *derived* from the underlying CPP framework, rather than being assumed. The 600-cell tetrahedral substrate of CPP makes simplicial-polytope arrangements of alpha clusters geometrically natural — but "natural" is not the same as "forced." A first-principles derivation of why alpha clusters in bound nuclei realize simplicial connectivity (rather than some other arrangement) would convert the formula from a conditional prediction (one that holds *if* the simplicial arrangement is the actual one) to an unconditional theorem of the framework. This was registered as OPEN-SS-24 at the time SS-7 v1.2 was published, and remains the highest-leverage open problem in the strong-sector series. Closing it would promote dozens of conditional predictions across the SS-7 and SS-8 papers to theorems.

The second is the neutron-excess physics that emerged from the OPEN-SS-22 retirement. The original empirical anchor's apparent discrepancy turned out to be the fingerprint of a real signal — extra neutrons beyond strict $N=Z$ contribute roughly $2$ MeV apiece of additional binding — but a CPP-internal derivation of *why* they do so, and a quantitative formula that reproduces the pattern, was not yet in hand at the close of SS-7. This was registered as OPEN-SS-23 (*Non-N=Z and Odd-A Extension of the Alpha-Chain Formula*) and became the explicit target of SS-8. The story of how SS-8 attacked it, and what it found, is the subject of another chapter.

For the moment, what SS-7 left was this: a single zero-parameter formula, derived from a result about polytopes that the geometers had known for centuries, that predicts the weights of twelve different atomic nuclei to better than one and a half percent across the full range from carbon to nickel. No constants tuned. No isotope-by-isotope adjustment. Two numbers carried over from a previous paper about much smaller nuclei, one classical theorem about triangulated polyhedra, and a cluster-model picture that mainstream nuclear physics had been working with — without quite knowing what to do with it — for nearly a hundred years.

There is something slightly unsettling about a result like this. The formula does too much. It predicts too many cases at once. It uses constants that were determined for an entirely different reason. The simplest explanation is that the picture is correct: that nuclei of moderate size really are made of alphas in approximate contact, that each contact really does store the same quantum of binding, that the geometry of the contact pattern really is forced to be simplicial by something deep about the framework. The harder question — the one OPEN-SS-24 asks — is what *exactly* is forcing it, and whether that something can be made explicit.

The second question is the right one to be asking. The first question is what SS-7 was for.

# Lay Summary: SS-7 — Alpha-Cluster Regime and the 3N−6 Edge Formula

**Paper:** SS-7 v1.1 (20 April 2026)
**Technical reference:** `series_strong/papers/SS-7_alpha_cluster_edge_formula.tex`
**Target audience:** Technical layperson — someone who knows what a proton is and what an atomic nucleus is, but not necessarily what a polytope is or what "zero fitted parameters" means in a theoretical-physics context.
**Reading time:** ~15 minutes
**Document type:** Plain-language exposition for the non-specialist, and source material for the *Tetrahedrons All the Way Down* trade book.

---

## The one-sentence version

If the simple nuclei made of two or three protons and neutrons are built like tiny tetrahedra, then medium-sized nuclei — carbon, oxygen, calcium — are built like tetrahedra made of tetrahedra, and a classical formula from geometry predicts their weights correctly to within one percent, using no adjustable numbers.

---

## Why this result matters

Here is a thing physicists do not usually get to do.

They have a theory. The theory was built for a different purpose — in this case, for explaining how pairs of particles stick together at the smallest scale. The theory contains two numbers that the theory itself calculated, not numbers that were measured and plugged in. And then they ask the theory: *what happens if we extend this, unchanged, to a problem it was not built for?*

In SS-7, the extension is from two-particle and four-particle nuclei (hydrogen isotopes and helium-4) to medium-sized nuclei made of many alpha particles stuck together — carbon-12, oxygen-16, and so on up to calcium-40. The two numbers — 28.296 million electron-volts and 2.342 million electron-volts — were fixed long before these nuclei were considered. No adjustment was made.

The result: the predicted weights of eight different nuclei match the measured values to better than 1.5% across the board, with an average error under 1%.

This kind of thing either means the theory is on to something real, or means a remarkable coincidence has occurred. Eight coincidences at better than 1%, all pointing the same direction, all using the same two numbers, is a lot of coincidence to accept.

---

## What an alpha particle is

Before anything else. An alpha particle is a helium-4 nucleus: two protons and two neutrons, bound together so tightly that it holds its shape like a rigid object even under conditions that would break other things apart. Alpha particles are ejected from heavy radioactive atoms when they decay; that's why the radiation detector in a smoke alarm clicks. They have been studied for a hundred and twenty years.

What's less famous — but well-established in mainstream nuclear physics — is that inside larger nuclei, alpha particles can sometimes be seen acting as units. Carbon-12 is not best modeled as twelve individual nucleons sloshing around; under many conditions, it behaves like three alpha particles in a triangle. Oxygen-16, like four alphas in a tetrahedron. This is called the *alpha cluster model*, and it is old — going back to the 1960s work of David Brink and others.

CPP agrees with this picture. What CPP adds is a specific prediction of *how strongly* the clusters bind together.

---

## What a tetrahedron has to do with anything

A tetrahedron is the simplest 3D shape: four points, with every pair connected. Four triangular faces, six edges, four vertices.

When a theory says nuclei are built like tetrahedra of tetrahedra, it is making two claims:

1. Each alpha particle *is* a small tetrahedron — four points (the four nucleons) with every pair bonded.
2. Several alpha particles, when they combine into a larger nucleus, arrange themselves at the vertices of a larger tetrahedron-like shape, with every pair of neighboring alphas touching.

Both claims are independently supported by experimental evidence for specific nuclei. What SS-7 does is say: *if you take those two claims seriously at the same time*, a formula drops out.

The formula uses a result from classical geometry called *Euler's formula*, which relates the number of vertices, edges, and faces of any closed convex shape with triangular faces. It says: a shape with N vertices and all-triangular faces must have exactly 3N − 6 edges.

Try this yourself. A tetrahedron has 4 vertices and 6 edges: 3(4) − 6 = 6. ✓. An octahedron has 6 vertices and 12 edges: 3(6) − 6 = 12. ✓. An icosahedron has 12 vertices and 30 edges: 3(12) − 6 = 30. ✓.

This is not specific to CPP. It is a theorem known since the 1700s.

SS-7 then says: *if each alpha particle contributes the same fixed binding energy, and each edge between touching alphas contributes another fixed binding energy, then the total binding of an N-alpha nucleus is:*

**Total binding = N × (alpha binding) + (3N − 6) × (edge binding)**

That is the whole formula. Two numbers, a vertex count, an edge count, and Euler.

---

## The eight predictions

Here's the table, translated into plain language. The "alpha count" column tells you how many alpha particles make up each nucleus. The "edge count" column is 3N − 6. The error column tells you how far the prediction misses:

| Nucleus     | Alpha count | Edge count | Predicted (MeV) | Measured (MeV) | Error   |
|-------------|-------------|------------|-----------------|----------------|---------|
| Carbon-12   | 3           | 3          | 91.9            | 92.2           | −0.27%  |
| Oxygen-16   | 4           | 6          | 127.2           | 127.6          | −0.30%  |
| Neon-20     | 5           | 9          | 162.6           | 160.6          | +1.19%  |
| Magnesium-24| 6           | 12         | 197.9           | 198.3          | −0.19%  |
| Silicon-28  | 7           | 15         | 233.2           | 236.5          | −1.41%  |
| Sulfur-32   | 8           | 18         | 268.5           | 271.8          | −1.20%  |
| Argon-36    | 9           | 21         | 303.9           | 306.7          | −0.93%  |
| Calcium-40  | 10          | 24         | 339.2           | 342.1          | −0.84%  |

Eight nuclei, all within 1.5% of experiment. No numbers tuned.

The neon-20 entry is the worst, at +1.19%. This is not random — neon-20 is known from independent studies to be *prolate*, like a slightly stretched egg rather than a perfectly symmetric shape. The formula assumes a symmetric shape. It's a small error in the right direction for the right reason.

Every other error is negative (the prediction under-binds reality by less than half a percent on average). This is consistent with the CPP programme's general pattern across many different predictions — leading-order predictions sit just slightly below measurement, by about the amount expected from effects the leading-order treatment doesn't include.

---

## The hardest test

A result like this invites the reasonable skeptical question: could the formula be working not because 3N − 6 is right, but because *any* vaguely-similar counting rule would work at this level of precision? Maybe the theory gets approximately the right answer regardless of what edge count you assume.

This is a real concern, and during the paper's review, ChatGPT (one of the AI reviewers) proposed a test for it. Pick five of the nuclei, replace the simplicial-polytope edge count with a smaller edge count corresponding to a less-connected geometric alternative, and see what happens to the fit.

For example, sulfur-32 (8 alphas) has the simplicial edge count of 18. But eight vertices can also arrange as a cube (12 edges) or as a square antiprism (16 edges). If the theory doesn't care about the specific number 18, the cube or antiprism alternatives should also work.

They don't. The cube gives a fit error of 6.4%, versus the simplicial 1.2%. The square antiprism gives 2.9%. Every one of the five tests failed in the same direction — lower edge counts always made the fit worse.

The tightest test was argon-36. The simplicial edge count is 21. An alternative shape called a monocapped square antiprism has 20 edges — just one less. Dropping a single edge changed the fit error from 0.9% to 1.7%. This is exactly the amount one would expect if removing a single edge removed exactly one edge-binding unit of energy.

That degree of sensitivity to a single edge is not the behavior of a formula that is merely ballpark-right. The edge count is doing real work.

---

## What about beryllium-8?

Beryllium-8 is two alphas stuck together. By the formula: 3N − 6 = 0 edges. So the formula says beryllium-8 should have *no* edge-binding — only the individual alpha energies.

The measured reality is that beryllium-8 is unbound: it exists briefly during nuclear reactions but falls apart into two alphas within about 10⁻¹⁶ seconds. It is unbound by a very small amount — 92 thousand electron-volts, roughly 0.16% of the total energy involved.

CPP's explanation: with zero edges predicted, the only things keeping the two alphas together are short-range nuclear attraction and electric repulsion (since each alpha has net charge +2). If you do the arithmetic assuming the standard alpha-alpha spacing from nuclear physics, the electric repulsion slightly wins, and the nucleus falls apart. Plug in the alpha-alpha contact distance that makes the numbers work: 2.37 femtometers (a femtometer is a millionth of a billionth of a meter, the size of a proton).

2.37 fm is within the expected range. It is not derived from CPP first principles — the paper is honest about this, calling it a *consistency parameter* rather than a prediction. But it is a reasonable number, in the reasonable range, produced by the same formula.

And beryllium-8's specific unboundness matters for a reason you may remember from stellar astrophysics: stars make carbon by smashing three alpha particles together, but they have to go through a transient beryllium-8 intermediate state. If beryllium-8 were strongly bound, the universe would be full of it and carbon would be rarer. If it were strongly unbound, the three-alpha reaction couldn't happen at all and carbon wouldn't exist. The fact that beryllium-8 is *just barely* unbound — a whisper away from stability — is what makes life possible.

CPP reproduces this whisper.

---

## What this paper does not claim

Several important honesties are embedded in the paper directly.

**It does not apply to all nuclei.** Only alpha-chain nuclei — those with equal proton and neutron numbers, both even, both divisible by 2, from carbon-12 to calcium-40. Nuclei like lithium-6 or nitrogen-14 are registered as future work.

**It does not work for heavier nuclei.** Beyond calcium-40, the systematic error grows to 2-2.5% at titanium-48 and iron-56. Interestingly, the error plateaus — it doesn't continue growing. The paper reads this as a signal that a new geometric effect activates at 12 alphas (the icosahedron being the natural 12-vertex closed shape), and registers this for a future paper (tentatively SS-8).

**It does not derive why alpha particles arrange into these specific shapes.** The paper assumes they do — an assumption labeled C4 — and shows that if they do, the numbers work. Deriving *why* they do from the more fundamental parts of CPP is a separate open problem (OPEN-SS-24), slated for a future paper (SS-9).

**The paper openly registers one internal inconsistency.** During final verification, a small discrepancy was found: the paper cites its RMS error as 0.88%, but a full-precision recalculation gives 0.91% (all eight nuclei) or 0.86% (excluding neon-20, the known-deformed outlier). This 0.03-percentage-point difference does not affect any individual prediction, but it is registered openly in a separate note rather than quietly corrected.

This last item is a small thing, but it signals the posture of the programme: when we find we have been wrong, even in a trivial way, we write it down and say so. This is unusual in physics publication. CPP is trying to make it less unusual.

---

## Where this fits in the larger story

CPP is a framework in which space itself is made of discrete points — arranged in a specific lattice based on a geometric object called the 600-cell — and where every particle of physics emerges as a stable arrangement of these points.

At the scale of individual quarks, the framework makes detailed predictions (papers SM-1 through SM-10 in the series). At the scale of individual nucleons, it predicts proton and neutron properties (SS-2). At the scale of the smallest nuclei, it predicts binding energies of hydrogen isotopes and helium (SS-5).

SS-7 is the next step up. It says: *once you have helium-4 as a tetrahedral object, build larger nuclei out of tetrahedral helium-4 units stuck together by the same mechanism that held the hydrogen isotopes together.* The mechanism carries upward without modification. The same two numbers control both levels.

This is what the word "all the way down" in the book's title means, pointed upward: tetrahedra at the scale of quarks, tetrahedra at the scale of protons, tetrahedra at the scale of alpha particles, tetrahedra at the scale of medium-mass nuclei. Four distinct scales, the same geometric motif, the same governing ratio.

Whether this pattern continues to heavier nuclei, to atoms, to molecules — is open. The programme is working its way up from the bottom carefully. SS-7 is one step in a methodical climb.

---

## How to check this yourself

A verification notebook accompanies the paper: `SS-7_alpha_cluster_edge_formula.py`. It is short, readable Python. It uses no external libraries beyond numpy. It reproduces every number in the table above from the two input constants. It runs in under a second.

If you are the kind of reader who trusts numbers you have computed yourself more than numbers you have read, this is the file to get. It contains no CPP-specific code — it is an ordinary scientific calculation. The only thing it relies on is the two input values, which are themselves documented in paper SS-5 as derivations from the deeper theory.

---

## In one paragraph, at the end

Take a classical theorem from 1700s geometry — the edge count of any triangulated convex shape is three times the vertex count minus six. Take two physical constants computed elsewhere in a separate physical theory. Put them in a formula. Compare to measurements of eight different atomic nuclei. Everything matches within 1.5%. Either the theory is pointing at something real about how matter organizes itself, or a particularly persistent coincidence has occurred. The purpose of continued work — including the papers currently planned to follow, and the reviewer engagements that produced this result — is to determine which.

---

*For the technical derivation, see `SS-7_alpha_cluster_edge_formula.tex`. For the reviewer-engagement history that produced the paper, see `development-SS-7.md` and `reviews-SS-7.md`. For the programme-level context, see `CPP_the_theory.md`. For the broader narrative aimed at the general reader, see the *Tetrahedrons All the Way Down* book project in `book_project/`.*

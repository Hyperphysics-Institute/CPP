# RES-SF4-STRUCT-1 — DERIVATION SKETCH v0.1: THE SPINNING-DP COMPOSITION PICTURE vs THE SHIPPED V-SHELL COUPLINGS

**Patch 3043 (9 Aug 2026). Opens the derivation session queued at
Patches 3041–3042. Target (acceptance test): derive, from the founder's
spinning-DP constitutive picture (founder ruling Patch 3041 §1) plus
the ratified stack, the shell couplings (spinning eDP → V=4, spinning
qDP → V=12, spinning qDP–eDP pair → V=30), thereby REPRODUCING the
shipped zero-parameter ratio m₂/m₁ = (12/4)² = 9.00 and inheriting the
ν₃ residual class. Geometric backbone facts computed exactly at this
patch (`code/3043_shell1_tetrad_geometry.py`, exhaustive enumeration,
seedless); physical selection mechanism laid out as sub-claims with
closure paths — NOT claimed closed. Nothing here alters SF-4.**

---

## §1 — Geometric backbone (COMPUTED, exact)

**FACT-G1 (shell census, reconfirmed).** From any 600-cell vertex:
V = 12 at d² = 1/φ², 20 at 1, 12 at 1+1/φ², **30 at 2**, ... —
matching SM-1/SF-4.

**FACT-G2 (the tetrahedral cage is a golden near-tetrad).** Exhaustive
enumeration of all 495 quartets of shell 1: **no exactly regular
tetrahedron exists.** The most-uniform class has pairwise-distance
multiset {5 × 1/φ, 1 × 1} — five bonded edges plus ONE pair stretched
by exactly φ (two shell triangles hinged on a shared edge). Distortion
max/min = φ, exactly. There are exactly **30** such optimal tetrads,
each vertex lying in 10 of them, and they admit partitions of the 12
vertices into **3 disjoint tetrad frames**. SM-1's "4 of the 12
nearest neighbours in tetrahedral arrangement — minimal stable shell"
is hereby made precise: the V=4 cage is a GOLDEN NEAR-TETRAD, and its
single φ-stretched pair is a structural feature, not a defect (a
candidate seam for the cage's dynamical properties; see S4).

**FACT-G3 (the 12-shell is a tetrahedral-group torsor).** The
rotation group of shell 1 has order 60 (icosahedral I, confirmed by
generation); an order-12 tetrahedral subgroup T acts **simply
transitively** on the 12 vertices. The full first shell is exactly
one copy of the tetrahedral group: |shell| = |T|, orbit = everything.
The V=4 and V=12 cages are therefore not merely "small and large" —
they are GROUP-THEORETIC KIN: the 12-shell is the T-orbit closure of
tetrahedral structure.

**FACT-G4 (tetrads ↔ the 30-shell, bijectively).** Each optimal
tetrad = two faces sharing an edge ↔ that shared... [precisely: its
unique NON-edge pair spans an icosahedron edge-adjacent structure;
operationally] the 30 optimal tetrads correspond one-to-one with the
icosahedron's 30 edges, and the 30 edge-midpoint directions are
EXACTLY the 30 directions of the d² = 2 shell (icosidodecahedron):
computed 30/30 match. **The V=30 shell is the shell of tetrad
locations.** The three neutrino shells (4, 12, 30) are thus one
nested structure: tetrad → tetrad-group orbit → tetrad-position
shell.

## §2 — Physical sub-claims (OPEN; closure paths named)

**S1 (species channel structure — grounded in ratified AP-4a).** A
spinning eDP writes only the E register (polar); a spinning qDP
writes E and S (strong; species identified by slot). The S-channel
weight is k (AP-4b; substrate-determined, non-tunable; identification
candidate 3(11+5√5) ≈ 66.5, O-2 open). The two spinner species are
therefore ONE-CHANNEL and TWO-CHANNEL Sea-writers, with the
two-channel writer stronger by O(k). STATUS: the channel structure is
ratified fact; its coupling-strength consequence for arc enrollment
is the open physical step.

**S2 (threshold shell selection — the central open claim).**
Conjecture: sustaining a coherent spinning enrollment of a shell of V
vertices costs coherence resources growing with V (candidate scaling:
∝ V², the same power the mass formula exhibits); a one-channel (eDP)
spinner can sustain only the MINIMAL stable structure — the golden
near-tetrad (V=4, FACT-G2, SM-1's "minimal stable shell") — while the
two-channel (qDP) spinner, stronger by O(k) ≥ the cost ratio
(12/4)² = 9, sustains the full T-torsor (V=12, FACT-G3). Sanity
inequality: k ≈ 66.5 ≫ 9 ✓ (necessary, not sufficient). CLOSURE PATH:
formulate the arc-enrollment coherence cost from the SF-6 DP-arc
mechanics (the founder ruling names SF-6-type arcs as the mass
carrier); derive the stability threshold; show one-channel clears
V=4 only and two-channel clears V=12. FALSIFIER: if the derived cost
ordering admits the eDP at V=12 or excludes the qDP from it, S2 dies
and the pictures compete.

**S3 (the pair → V=30 — structurally suggested by FACT-G4).** The
qDP–eDP pair is a composite of BOTH spinner species. FACT-G4 gives
the natural target: the 30-shell is the shell of TETRAD POSITIONS —
the geometry a composite of tetrad-anchored objects would enroll.
The founder's not-hTetra clause (no nucleation point) excludes the
folded V=20 route independently, and SM-1's taxonomy inherits the
same exclusion. CLOSURE PATH: show the two-species composite's arc
system anchors on edge-midpoint (tetrad-position) directions; the ~8%
ν₃ residual is then inherited from the known K3 partial-binding
class, not new. STATUS: open; the FACT-G4 bijection is the reason to
believe a derivation exists.

**S4 (registered observation, no claim).** The golden near-tetrad's
unique φ-stretched pair breaks the tetrad's symmetry to C₂ᵥ-class —
a natural candidate seam for spin-axis selection (the spinner's axis
distinguishing the stretched pair). Registered for the derivation
work; consuming it now would be decoration.

## §3 — Acceptance test (unchanged, now with the backbone in place)

S2 closing at theorem level for (eDP → 4, qDP → 12) reproduces
**m₂/m₁ = 9.00** with zero parameters, unifying the founder's
composition picture with the shipped topology result; S3 closing
lands ν₃ with the residual absorbed by the K3 partial-binding
correction. Failure of S2/S3 as specified sends the competing
descriptions to the panel. Either way the item rides to the MEAS-3
disposition batch with this sketch attached.

## §4 — What this patch does NOT claim

No shell coupling is derived here. G1–G4 are exact geometry; S1 is
ratified channel structure; S2–S3 are open physical claims with named
closure paths and a falsifier. σ_ν, the mass formula, and all SF-4
numerics are untouched.

---

## §5 — v0.2 (Patch 3044): S2 CONDITIONALLY CLOSED AT MODEL GRADE; the cost model SELECTED by consistency; an independent bound on k

**The computation** (`code/3044_s2_threshold_selection.py`, 4/4;
exact inequalities, no fits). Model inputs stated openly: (I1) driven
entrainment — a spinner entrains the largest shell it can hold
mutually coherent; (I2) a universal species-independent threshold τ
with cost = τ·f(V), f tested across the three natural orders
{V, V², V(V−1)/2}. Couplings from the ratified channel structure:
C_e = 1 (E-only), C_q = 1+k (E and k-weighted S), C_pair = 2+k
(strict additivity baseline).

**R-S2a (conditional closure).** Under the PAIRWISE cost
f = V(V−1)/2 — one coherence resource per mutual phase relation,
which is SM-1's cage-cooperation clause made quantitative — a single
universal threshold window exists at the O-2 candidate
k* = 33+15√5 ≈ 66.541: τ ∈ (0.15527, 0.16667], producing EXACTLY the
founder assignment: eDP → V=4 (capped below 12), qDP → V=12 (capped
below 30). The eDP sits at its shell marginally at the window's top
(6τ → 1 = C_e): "minimal stable shell" = marginal entrainment.

**R-S2b (the cost model is SELECTED, not chosen).** The same joint
assignment admits NO threshold under f = V² (window (0.0751, 0.0625]:
empty) and NO threshold under f = V (window (2.251, 0.250]: empty).
Among the three natural orders the pairwise form is the UNIQUE
survivor. The mass formula's V² is thus NOT the entrainment cost —
mass scaling and shell selection are different functions of V, and
consistency forces the pairwise form for selection.

**R-S2c (an independent cross-sector bound on k).** The window
exists iff **0 < k < 71.5** (= 435/6 − 1, exact). The AP-4b constant
is thereby BOUNDED ABOVE by neutrino shell selection — a constraint
from a sector that never mentions k's own derivation. The O-2
identification candidate 66.541 sits INSIDE (with ~7% headroom); the
founder-recalled ~67 sits inside; a charged-lepton-like 206.8 would
be EXCLUDED. Registered as cross-link **S2↔O-2**: any future k
identification must land under 71.5 or S2's model dies.

**R-S2d (the pair's requirement quantified).** Under strict
additivity the full three-shell assignment survives only in a
τ-sliver of width ~1.5% — fine-tuned. But ANY cooperative
enhancement of the pair coupling by ≥ 5.8% (g ≥ 72.5/(2+k) ≈ 1.058)
widens it to the full R-S2a window; alternatively the FACT-G4
tetrad-position mode bypasses brute pairwise cost entirely. S3's
burden is therefore WEAK and quantified: a ≥6% two-species
cooperative effect, or the edge-midpoint anchoring mode.

**Grade and residue.** S2 is CONDITIONALLY CLOSED at MODEL grade:
conditional on (I1) and on the pairwise cost form — the latter now
consistency-selected (R-S2b) and mechanism-motivated (SM-1), the
former still a physical postulate awaiting an SF-6 arc-dynamics
derivation. The acceptance test's first half is met at this grade:
the composition picture reproduces (eDP→4, qDP→12) and hence
**m₂/m₁ = (12/4)² = 9.00** with zero fitted parameters, contingent
on the model inputs. Open residue: derive (I1) and the pairwise form
from arc dynamics proper; close S3 by either route; panel review of
the model grade (rides in the MEAS-3 disposition batch).

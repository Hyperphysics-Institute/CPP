# W⁰ / W^± composition — harmonisation with the Weak Sector lane, and one question back

**Patch:** 0944, 13 Sep 2026, chirality window under PD-006 (SM holds no active ID block). **Verify:** `corrigenda/code/0944_w_ring_harmonization.py` (7/7). **Status:** the W entries in SM-2 remain **untouched** pending one founder answer. Nothing is edited by this patch.

**Founder ruling, 13 Sep 2026, verbatim:**

> I believe the W^0 is neutral and is a 12-member ring (three qDPs and three eCPs). Please check with the Weak Sector lane for this harmonization. The W^+ and W^- are created from a W^0 with a + or - eCP carried on the W^0 enzymatic structure.

## 1. What the Weak Sector lane has on file

Per SF-2 v1.0 Theorem 4.2, carried into `capotauro.tex` §"The W-bracelet on the host vertex first-shell icosahedron": the **W-bracelet** is the H₄-orbit 𝒪_ℬ of 1,200 induced hexagonal 6-cycles in the 600-cell vertex graph, with stabiliser the dihedral group **D₆ of order 12**. Geometrically it is a **Petrie hexagon of the first-shell icosahedron** centred on a 600-cell vertex: **six vertices**, being 6 of the 12 first-shell vertices, the other 6 carrying the bracelet's antipodal partner. Under vertex-aligned Reading C the ten bracelets on v_host have centroid exactly (φ/2)n̂.

**The ruling and the lane agree on the essentials.** A *ring* is right — the lane's object is a 6-cycle, not the linear chain SM-2 currently assigns. And the ring sits on the first-shell icosahedron, which is where the substrate chirality χ is inherited (Corollary: Substrate-Locality Unification, Finding C-W40), so the W's V−A coupling handle |M^W| = χ/6 is untouched by anything below.

## 2. The arithmetic question

Two things in the composition as literally stated do not close, and they are related.

- **The count.** Three qDPs (2 CPs each) plus three eCPs (1 CP each) is **9 CPs**, or 6 objects. Neither is 12 (T1). The number 12 does appear in the lane's material — as the **order of the D₆ stabiliser** — but a group order is not a membership count.
- **Neutrality.** Three eCPs, each ±1, can total ±3 or ±1 — **never 0** (T2). An odd number of unit charges cannot be neutral. This is a parity obstruction, not an artefact of the particular grouping: exhaustively, *every* 12-CP composition containing an odd eCP count fails neutrality regardless of how many DPs accompany it (T7).

## 3. The reading that reconciles all four constraints

**Three qDPs and three eDPs.**

- 6 DP objects = **12 CPs** — the 12-member count, exactly (T3).
- One object per site on the lane's **6 Petrie-hexagon vertices** (T3).
- **Neutral**, because every constituent is a bound pair (T3).
- **Preserves SM-2's existing member count**: the current entry "Linear 6-hDP chain" is likewise 6 DPs = 12 CPs (T4). So the correction changes **topology** (chain → ring) and **species** (6 hDP → 3 qDP + 3 eDP), and leaves the member count alone.

On that reading everything harmonises, and *"eCPs"* in the ruling would be a slip for *"eDPs"*. **I have not assumed it.** Confirming a composition is a founder call, and this is the question back.

## 4. The W^± half, which needs no repair

W⁰ neutral plus one carried eCP gives exactly ±1 for either sign (T5), and the charge resides entirely on the unpaired carried CP (T6). That is precisely the **3513 partnerless-third / "odd man out" structure** already in use by the DM lane's E3 count — a bare CP attached to an otherwise-paired DP entity. The "enzymatic" reading (the ring as scaffold, the carried eCP as the charge) matches that structure without introducing a new mechanism. **This half of the ruling is adopted as stated and needs nothing further.**

## 5. What this changes in SM-2, once the question is answered

Larger than the charge fix of 0942/0943 — it replaces a structure, not a label:

- **Cage assignments**, "W: Linear hDP chain" → the W⁰ ring, with W^± as W⁰ plus a carried ±eCP.
- **Mass Contribution Breakdown**, row "W & Linear 6-hDP chain & … & 80380". **Open, flagged, not assumed:** the member count is unchanged at 12 CPs, but the species change (hDP → qDP + eDP) and the topology change (chain → ring) may or may not move the mass terms. If the breakdown is species-blind and count-driven, the row survives as a relabel; if the hDP species enters the energy terms, the W mass fit needs recomputation. **This is the one place a published number could move**, and I have not touched it.
- **EW sector coupling.** `OPEN-EW-2` (unified boson mass formula) and `OPEN-EW-3` (the 4D→3D projection factor for the W bracelet, currently calibrated rather than derived) both take the bracelet as their geometric object. A ring on the Petrie hexagon is what they already assume, so the topology correction moves SM-2 *toward* the EW lane rather than away. The species question should be put to the EW lane alongside the mass-row question.

## 6. The one question back

**Is the W⁰ ring three qDPs and three eDPs (6 DP objects, 12 CPs, neutral, one per Petrie-hexagon site), or did you intend something else by "three eCPs"?**

As stated it is 9 members and cannot be neutral; the eDP reading gives 12, neutral, and seats on the lane's six sites. On your answer I will write the SM-2 W edits into the corrigendum and put the mass-row question to the EW lane.

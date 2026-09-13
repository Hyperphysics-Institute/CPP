# 0946 — Does the travel-distance asymmetry supply the W⁰'s chirality? No: wrong parity class. But the ring's arrangement is unfixed, and exactly one arrangement is chiral

**Lane:** chirality (09xx). **Patch:** 0946, 13 Sep 2026. **Layer:** 2/3 bookkeeping, single pass. **Verify:** `chirality_derivations/code/0946_w0_chirality_source.py` (7/7 — the point group, the mirror, the rate law, the current, and the ring combinatorics all constructed, nothing typed in). **Founder question, 13 Sep 2026:** *"since we found an asymmetry in the travel distances between vertices, does this resolve the question of the chirality of the W⁰ boson?"*

## Short answer

**No — and the reason is a parity-class mismatch the programme has ruled on once before.** The travel-distance asymmetry is P-**even**. Chirality is P-**odd**. No amount of the first can make the second. This is THEO-CHIR-MERGE-2's finding (Patch 0647) — `sign(δ)` is P-even/T-odd, an *arrow*, not a handedness — arriving again at the W⁰ rather than at the merge.

**But the question is productive anyway**, because checking it surfaced something the W⁰ ruling genuinely leaves open: the arrangement of the three qDPs and three eDPs around the ring was never specified, and **exactly one of the three distinct arrangements is chiral.** That, not the rate asymmetry, is where a W⁰ handedness would live.

## 1. Why the asymmetry cannot do it

- **The substrate has no handedness to donate.** The vertex stabiliser has order 120 and contains 60 orientation-**reversing** elements (T1). The bare 600-cell is achiral. Whatever handedness the W⁰ has cannot come from the lattice alone.
- **The rate law's object is mirror-symmetric about n̂.** There is an orientation-reversing element of the stabiliser that *fixes n̂* and carries the twelve first-shell directions to themselves (T2). So the configuration MA.1 is defined on already has a mirror through it.
- **Hence MA.1 is P-even.** `r(ê) = r₀(1 + δ ê·n̂)` is invariant under that mirror for every first-shell direction (T3). The rate law distinguishes no left from right.
- **And the current is an arrow, not a handedness.** The O(δ¹) current `J = (6/φ²) r₀ δ n̂` of Patch 0941 is carried to *itself* by the mirror (T4). It is a **polar vector**: a direction of flow. A chirality requires a **pseudoscalar**, and n̂ alone cannot build one — a 4D pseudoscalar needs four independent vectors.

So the asymmetry is real, and it is the wrong kind of object. The non-central-symmetry of the first-shell edge set (0941) makes the substrate **anisotropic and arrowed**; it does not make it **handed**.

## 2. Where the W's handedness already comes from

It is on file and unaffected by any of this. The W-bracelet is built from first-shell vertices, so by Substrate-Locality Unification (Finding C-W40) it inherits the substrate **pseudoscalar** χ = φ⁻³, giving `|M^W| = χ/6 ≈ 0.0394` (THEO-SD-CHIR-1, `capotauro.tex` §W-bracelet sector) — the substrate handle for the V−A coupling (T5). **χ is P-odd; δ is P-even.** They are different primitives doing different jobs, which is exactly why the determination arc (Patch 0903) closes chirality down to *two* irreducible items — FI-C-9's χ **and** the T-arrow `sign(δ)` — rather than one. If the travel asymmetry could supply chirality, that arc would have closed to one primitive and it did not.

## 3. What the question did surface: the ring's arrangement is unfixed

The founder's ruling (13 Sep, harmonised at 0944, written in at 0945) fixes the W⁰'s **composition** — three qDPs and three eDPs, one per Petrie-hexagon vertex — but not their **order around the ring**. That turns out to matter:

Of the arrangements of 3 + 3 on a six-ring there are **4 up to rotation** and **3 up to rotation-and-reflection**. The deficit is the whole point: **exactly one arrangement is chiral**, existing as a left/right pair (`eeqeqq` / `eeqqeq`), while the other two are achiral (T6).

- `eqeqeq` — strictly alternating. Achiral. Stabiliser of order 6 in D₆.
- `eeeqqq` — blocked, three of each. Achiral. Stabiliser of order 2.
- `eeqeqq` / `eeqqeq` — **the chiral pair.** Stabiliser of order 1 — trivial, the only class containing **no reflection** (T7).

Two consequences worth recording:

1. **A handed W⁰ is available from the decoration**, and only from this one arrangement. If the W⁰ is to carry a structural handedness of its own — over and above the χ it inherits — the alternating and blocked arrangements cannot provide it, and the chiral pair necessarily does.
2. **Every decoration breaks D₆.** The Weak Sector lane's stabiliser D₆ (order 12) is the symmetry of the *bare* hexagon. Decorating it with 3 qDP + 3 eDP drops the stabiliser to order 6, 2 or 1 depending on arrangement (T7). This is not an error in the lane's statement — D₆ is correctly the bracelet's stabiliser — but any downstream argument that uses D₆ *on the decorated W⁰* needs to know which subgroup actually survives. Flagged for the EW lane alongside `OPEN-EW-5`.

## 4. Question back to the founder (PD-006(a): physics in a physical picture)

**Which arrangement of the three qDPs and three eDPs around the W⁰ ring?** The three candidates and their symmetry consequences are above. If the intended picture is a handed W⁰, the answer is forced to the chiral pair — and then a further question follows, of which handedness, and whether it is tied to the sign of χ or independent of it.

**Not assumed, not derived.** Nothing in the composition ruling or in the substrate geometry selects among the three; this is a composition question of the same kind as the eCP/eDP one.

## 5. Disposition

- **Founder's question answered: no.** The travel-distance asymmetry is P-even and cannot supply chirality; the W's handedness remains sourced from χ via THEO-SD-CHIR-1.
- **No verdict moves.** V3/W3 stand and remain conditional on Mechanism A; THEO-CHIR-MERGE-2 is re-confirmed, not re-opened; THEO-SD-CHIR-1 and `|M^W| = χ/6` untouched; the determination arc's two-primitive closure (0903) is unaffected and is in fact corroborated.
- **No THEO/ID/prediction registered.** Nothing here is new physics; it is a class check plus a combinatorial fact.
- **Owed:** the arrangement question above (founder); the D₆-breaking note to the EW lane (filed with `OPEN-EW-5`).

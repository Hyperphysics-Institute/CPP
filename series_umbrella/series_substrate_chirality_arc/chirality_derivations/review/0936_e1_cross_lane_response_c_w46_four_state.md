# 0936 — Cross-lane response to DM E1 (OPEN-DM-SIGN-SELECTION-1): the C-W46 four-state extension, and what decides case (b) vs case (c)

**Lane:** chirality (09xx). **Patch:** 0936, 13 Sep 2026. **Layer:** 2 (structural argument, single pass, no panel). **Verify:** `chirality_derivations/code/0936_first_shell_antipode_check.py` (5/5). **Reasoning fragment:** `chirality_derivations/reasoning/0936.md`.

**Responds to:** DM Patches 3532 + 3533 (`series_phenomena/cosmology/dark_matter/founders_voice/3533_E1_sharpened_note.md`) and the Session 227 handover forward-queue item 1, which route to this lane the question: *does a DP in the n̂-asymmetric substrate have an energy that depends on which way its dipole points along n̂ (case c), or only on where it sits (case b)?* — together with the owed extension of Finding C-W46 (THEO-SD-CHIR-2) to its full four-state representation and the sign of the |+, −v⟩ class.

**Verdict in one line.** The question as posed cannot be answered until one word in C-W46 is fixed — which antipode "−v" denotes — and once it is fixed by the machinery C-W46 itself relies on, THEO-SD-CHIR-2's nonzero doublet element **forces case (c)** (orientation coupling, C-odd), so the dressing selectivity of the 3527 picture exists and the |+, −v⟩ class carries the **same** split as the on-file doublet: the + host lowered, S = +qCP. Under the literal wording of C-W46 §20.2 the opposite holds (case (b), no selectivity). Three consistency flags are raised against C-W46 for the SD lane; **no verdict of the chirality arc moves.**

---

## 1. Three D-7 corrections to the question as posed

**1.1 Mechanism A is the wrong primitive for an energy.** The DM lane's question names F.1 Mechanism A, r(ê) = r₀(1 + δ ê·n̂). That is a *propagation-rate* asymmetry, and THEO-CHIR-MERGE-2 (Patch 0647, reviewed 3/3 at 0651) classifies δ as **P-even, T-odd** — the arrow, not a chirality. An energy is T-even, so at first order in δ Mechanism A yields a *current* (the 0(δ³) NESS current of TARROW-2), never an energy term; a δ-sourced energy would be O(δ²) at the earliest (OPEN-FP-F1-1 territory) and carries no chirality. The 3528 computation, ΔF_dress = −(12/φ)κ with κ = χ·E_DP, is built — correctly — on the **spatial** primitive: Reading C's edge-length perturbation ε ≡ χ = φ⁻³ (Finding C-W39, §13.4), which is P-odd and T-even. The question is therefore a Reading C / THEO-SD-CHIR-2 question, not a Mechanism A question, and the answer below is given in that sector. Nothing in this patch touches Mechanism A, OPEN-FP-F1-2, or the conditionality of any arc verdict.

**1.2 Both first-shell antipodes lie at the same projection.** Under vertex-aligned Reading C (n̂ = v_host) every first-shell direction has û·n̂ = −1/(2φ) (F.1 Theorem 5.1; verify T1). The icosahedral cage of the twelve first-shell vertices is centrally symmetric about its **own** centre c = (φ/2) n̂, so the antipode of a first-shell vertex v within the cage is v′ = φ n̂ − v — exactly the ζ^W form p ↦ φ n̂ − p of Finding C-W43 §17.3 — and v′ is itself a first-shell vertex at the **same** projection −1/(2φ) (verify T2). By contrast the **host-centred** inversion 2 v_host − v is not a 600-cell vertex at all (|2v_host − v|² = 5 − 2φ ≠ 1), and the ambient direction −û has projection +1/(2φ) (verify T3). Consequence: the DM lane's "inward vs outward along n̂" is not a distinction between two first-shell placements; every first-shell placement is inward. 3533 §2 is right that an extra along +n̂ is not a first-shell configuration — but see 1.3 for what that implies about C-W46 rather than about the physics.

**1.3 C-W46's "−v" is ambiguous, and its two readings are not equivalent.** §20.2 defines ζ^qDP as "host-CP-centered spatial inversion (v → −v)" — reading **R2**, the non-vertex direction of 1.2. But §19.4 Candidate A and §20.4 build the sector on the "antipodal-pair D_{5d} realization" with the C₂ dihedrals "perpendicular to the v-axis through host," and D_{5d} is the stabilizer of an antipodal pair *of the icosahedron*, which exists only for the icosahedral antipode — reading **R1**. The W-bracelet precedent ζ^W (§17.3) is the icosahedral-centre inversion, and §20.2 explicitly claims ζ^qDP as its analog. So the **machinery requires R1** and the **wording says R2**. The two readings give opposite answers to E1 (§3), so the ambiguity is load-bearing and is raised as Flag F1 (§5).

## 2. The four-state representation

States |s, x⟩ with host sign s ∈ {+, −} and the Linear-ZBW extra (or, for the DM lane's use, a cocoon DP) along x ∈ {v, v′}, where v is a first-shell direction and v′ is its antipode in whichever reading. The polarised extra's dipole is slaved to the host: the end of opposite sign sits nearer the host, so the dipole vector (− end → + end) is **d̂ = s û** — orientation and host sign are not independent variables for a bound extra. C-W46 uses the pair {|+, v⟩, |−, v′⟩} (its ζ-conjugates); 3532 asks about the complementary pair {|+, v′⟩, |−, v⟩}; the **physical** pair for dressing selectivity is {|+, v⟩, |−, v⟩} — both first-shell, both inward, differing only in host sign (3528's "polar cocoon" summed over all twelve û is this pair, ×12).

Two candidate first-order chiral energies, in units of M (the χ/6-scale reduced element; sign convention of §4):

- **(b) placement:** E = M (û·n̂) — C-even, blind to the host sign.
- **(c) orientation:** E = M (d̂·n̂) = M s (û·n̂) — C-odd, couples to the DP's charge-orientation.

(3533's case (a), s alone, is excluded there and not re-examined.) The table (verify T5):

| reading | energy | C-W46 doublet E(+,v) − E(−,v′) | complementary E(+,v′) − E(−,v) | physical pair E(+,v) − E(−,v) |
|---|---|---|---|---|
| R1 icosahedral antipode | (b) | **0** | 0 | 0 |
| R1 icosahedral antipode | (c) | −1/φ | −1/φ | **−1/φ** |
| R2 host-centred inversion | (b) | −1/φ | +1/φ | **0** |
| R2 host-centred inversion | (c) | **0** | 0 | −1/φ |

The 1/φ = 2 × 1/(2φ) is the projection difference; summed over the twelve first-shell directions it is 3528's 12/φ = 7.42 (verify T4).

## 3. What THEO-SD-CHIR-2's nonzero element decides

C-W46's content is the **nonzero** element ⟨Ψ⁽¹⁾|Ĉ^qDP|Ψ⁽²⁾⟩ = χ/6 between the ζ-even and ζ-odd combinations of |+, v⟩ and |−, v′⟩. If Ĉ^qDP is diagonal in the configuration basis (the reading both lanes have used; see Flag F3 if it is not), that element equals ½[E(+,v) − E(−,v′)] — the **doublet column** of the table — and must be nonzero. Read off:

- Under **R1**, only **(c)** gives a nonzero doublet. Then the complementary pair and the physical pair carry the **same** split, −1/φ: the + host is the lowered configuration in every pair, and the |+, v′⟩ class (3532's ask) is lowered by exactly the amount |−, v′⟩ was raised. **Dressing selectivity exists; S = +qCP.**
- Under **R2**, only **(b)** gives a nonzero doublet. Then the physical pair is **degenerate** — no selectivity — and the complementary pair splits with the opposite sign to the on-file doublet.

So 3533's α-family ("any first-order energy reproduces the doublet, the doublet cannot decide") is true only if the reading is left open; once "−v" is fixed, C-W46's own datum fixes the energy type uniquely. **Under the reading its D_{5d} machinery requires (R1), THEO-SD-CHIR-2 answers E1: case (c).** This is a Layer 2 structural result, single pass; it rests on R1 (Flag F1) and on the diagonal reading of Ĉ^qDP (Flag F3).

Physical reading of the R1 result: the Reading C perturbation is a geometric perturbation of edge lengths and is C-blind; at O(ε) the local I_h is preserved (C-W39), so **no first-shell placement is distinguished** — that is why (b) vanishes identically under R1 (every entry in that row is the same number). The only first-order chiral energy that can survive I_h-preservation and still be nonzero is one whose sign rides on a quantity the geometry does *not* average away, and the only such quantity in the four-state space is the host sign through d̂ = s û. A C-odd coupling of the pseudoscalar χ to the DP moment, χ (d⃗·n̂), is therefore not an extra assumption under R1 — it is the only form C-W46's nonzero element leaves open.

## 4. Sign

The magnitude and the *relative* signs across the three pairs are fixed above. The *absolute* sign — whether the + host is lowered or raised — is the FI-C-9 convention (sign(n̂), the unique primitive pseudoscalar; MERGE-2), exactly as 3528 flagged: its mirror flips every entry of the table. The corpus fixes it only by phenomenology: the corrected SM-2 §10 (3524/3531 — the matter down quark is a + host with an inward extra and is the stabilised configuration) selects the convention in which the + host is lowered. In that convention S = +qCP, in agreement with the founder's ruling 3527 and 3528's number, and the SM-2 corrigendum owed by 3531 carries the same sign. SM-2 v1.0's original "−qCP stabilised" is the mirror convention applied to the same geometry, not a different mechanism — consistent with 3524's finding that §10's sentence was the slip.

## 5. Flags for the SD lane (consistency, not verdicts — D-1)

- **F1 — the "−v" ambiguity (§1.3).** C-W46 §20.2 should say which inversion ζ^qDP is. The D_{5d} structure, the ζ^W precedent, and the requirement that both members of the doublet be lattice configurations all point to the icosahedral-centre inversion p ↦ φ n̂ − p (R1), which is also the reading under which C-W46's doublet consists of two first-shell states — resolving 3533 §2's consistency note in C-W46's favour. If the SD lane instead confirms R2, then THEO-SD-CHIR-2's doublet contains a non-lattice state and E1 is case (b).
- **F2 — the irrep of Ĉ^qDP.** §20.5 assigns Ĉ^qDP ∈ A_{2u}(D_{5d}), odd under the C₂ dihedrals. Under R1 a C₂ dihedral is a proper rotation of the preserved local I_h that fixes n̂ and the host sign and maps |s, v⟩ ↦ |s, v′⟩; a diagonal first-order energy is then C₂-**even** (table, R1 rows). A pure pseudoscalar branches A_u(I_h) → A_{1u}(D_{5d}), not A_{2u}; A_{2u} is the transformation of the coordinate along the pair axis, i.e. of a *polar* component. Either the operator is A_{1u} (and the Wigner–Eckart product in §20.6 must be re-stated), or the matter-doublet labels A_{1g} ⊕ A_{2u} in §20.4 must be re-derived. Not a claim that THEO-SD-CHIR-2 fails — the χ/6 magnitude is reproduced independently in the K3 and W sectors — but the qDP bookkeeping is owed one pass.
- **F3 — configuration-basis form of Ĉ^qDP.** C-W46 states only the off-diagonal element in the Ψ basis. Both lanes have read χ/6 as a diagonal split between definite-sign configurations; if Ĉ^qDP instead connects |+, v⟩ ↔ |−, v′⟩ (a mixing, as in the K3 mass sector), the "stabilisation energy" reading collapses and 3528's ΔF_dress has no source in THEO-SD-CHIR-2. One sentence in C-W46 settles it.

## 6. Disposition

- **E1 (DM lane):** answered at Layer 2 — **case (c), S = +qCP, conditional on R1 (F1) and the diagonal reading (F3)**; the |+, v′⟩ class is lowered by the same 1/φ·M as |−, v′⟩ is raised. E2 remains blocked on E_coc (the magnitude M in physical units is E_DP-scale with the χ/6 factor; this patch does not supply it). Cross-reference placed at the foot of `3533_E1_sharpened_note.md`.
- **Chirality arc:** no verdict moves. V3/W3 stand; THEO-CHIR-CAPACITY-1 untouched; Mechanism A conditionality untouched; no THEO/ID/prediction; header count unchanged.
- **Registered:** OPEN-CHIR-QDP-4STATE-1 in `frontier_sectors/CHIR.md` (this patch) carrying F1–F3 for the SD lane, closing when C-W46 states its inversion centre, the irrep, and the configuration-basis form of Ĉ^qDP.
- **Governance:** the 09xx block is entered in `id_block_registry.md` and taught to `code/next_id.py` (which also now recognises the lane's bare-numbered commit subjects); next free 0937.

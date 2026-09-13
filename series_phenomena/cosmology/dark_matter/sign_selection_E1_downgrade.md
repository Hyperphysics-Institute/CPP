# OPEN-DM-SIGN-SELECTION-1 — E1 DOWNGRADED from "PASS conditional" to OPEN: the on-file chirality operator (C-W46) does not determine the cocoon sign. **The geometry of 3528 stands; its sign convention was an extrapolation beyond the stated doublet.**

**Patch 3532, 13 Sep 2026. DM block, from this window under PD-006.** Corrects `sign_selection_E1_dressing_sign.md` (3528) §1 and §3. Nothing minted; no sign chosen; the item is returned to the SD/chirality lane with the exact question.

## §1 What C-W46 actually states (read at source, `capotauro/sketches/Capotauro_chiral_mechanism_candidate.md` §20.2–20.6)
- The states are |±, ±v⟩ = "qCP-sign ± at the host, Linear-ZBW pointing along ±v", where the v-axis is the axis through the host along n̂ (vertex-aligned Reading C). So the doublet is **|+, v⟩ = a + host with its extra on the +n̂ side** and **|−, −v⟩ = a − host with its extra on the −n̂ side**. These two are ζ-conjugates (ζ = combined CP: v → −v, n̂ → −n̂, ± → ∓).
- The chirality operator Ĉ ∈ A₂u(D₅d) is ζ-odd with matrix element χ/6 between the ζ-even and ζ-odd combinations; equivalently the two configurations are split by ±χ/6·E, and SM-2 §10's statement fixes which is lower: **|−, −v⟩ (− host, extra on the −n̂ side) is the stabilised one** for the registered sign(n̂).
- The full matter representation is **4-dimensional (2A₁g ⊕ 2A₂u)**: the other two configurations, |+, −v⟩ (+ host, extra on the −n̂ side) and |−, v⟩, form the complementary 2D subspace. **C-W46 states the split of the first pair only.** The relative sign of the split in the complementary subspace — whether a + host with an inward extra is lowered or raised — is not on file.

## §2 Why this undoes 3528's sign
A dressed centre's cocoon lies **entirely on the −n̂ side of the host** (Theorem 5.1: every neighbour at û·n̂ = −1/(2φ)). So the two cocoon configurations are:
- **− host, shell inward** = the |−, −v⟩ class — **stabilised, on file.**
- **+ host, shell inward** = the |+, −v⟩ class — **in the complementary subspace; its chiral energy is not stated.**

3528 bridged the gap with a per-DP rule ("a shell DP whose − end lies n̂-ward is lowered"), read off the doublet pair. That rule is one of three consistent possibilities, and 3528 §1 flagged it as a convention; on re-reading it is an **extrapolation**, not a convention, and the three cases are:
- **(a)** the chiral energy is odd in the host sign at fixed geometry: E(+, inward) = −E(−, inward) ⇒ the − host's cocoon is stabilised and the + host's destabilised ⇒ **S = −qCP** — the founder's picture (3527) fails at E1.
- **(b)** the chiral energy depends on the geometry only: E(+, inward) = E(−, inward) ⇒ **no dressing selectivity** from this operator.
- **(c)** 3528's rule ⇒ **S = +qCP**, the picture passes.
Only (c) was computed. **E1 is therefore OPEN**, and its resolution is a statement about the complementary subspace that the SD/chirality lane owns.

## §3 What still stands from 3528
Theorem 5.1 reproduced; the cocoon is polar with respect to n̂ = v_host (shell factor 1/(2φ) per DP, coherent over 12 DPs); a first-order sign-odd cocoon energy *can* exist; the magnitude scale |ΔF_dress| ~ (12/φ)·χ·E_DP if the split is coherent. The lepton-sector remark (T7) inherits the same three-way ambiguity and is moot under 3529 in any case.

## §4 The question returned to the SD/chirality lane (E1's owner now)
**Extend C-W46 to the full 4-state representation:** for the registered sign(n̂), is the configuration "+qCP host with its Linear-ZBW extra (or its polarised shell) on the −n̂ side" lowered or raised relative to the "−qCP host with the same inward geometry"? That single sign is E1. It is also exactly the sign the SM-2 corrigendum (3531) must carry, since the corrected down quark (+qCP core, inward-lying dressing) is the |+, −v⟩ class. The two owed items are one item.

## §5 Effect on the charter
E1 status: OPEN (not conditional-pass). E2 remains blocked on E_coc. E3's bookkeeping (3531) is unaffected. E4 unaffected. Under D-3 no case (a)/(b)/(c) is selected; the founder's picture requires (c), and that is a prediction the SD lane's extension will test.

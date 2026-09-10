# OPEN-EU-EFOLD-BUDGET-1 route 1 (VSL) worked and **CLOSED** — it addresses the wrong problem. EU-1's VSL clause solves **causal contact**; the 3823 shortfall is a **size** requirement, and the shortfall is **invariant under R_init**, so no enlargement of the early reach or the early ball can touch it. The premise was dead anyway. **The tension stands at ~10.5 e-folds, and it is now a constraint on the total CP count and nothing else**

**Patch 3854, Session 186, 9 Sep 2026. Lane: EU.** Works OPEN-EU-EFOLD-BUDGET-1 route 1, named at 3823 §4 as "the most promising and uncomputed" and deferred through six sessions behind the amplitude arc. Verify `scripts/3854_vsl_route_closed.py` (8/8). Reasoning `reasoning/3854_vsl_route_closed.md`. Nothing adopted; no constant minted; PRED-C-96 untouched; 3710 not retired.

## §1 What EU-1's VSL clause actually claims (verify T1)
The paper's §Background is explicit, and reading it closely is the whole of this patch:

> "The horizon / causal-contact problem is addressed **not by a large number of e-folds** but by a large early Propagation-Speed-Ratio (a variable-speed-of-light, VSL, phase: a large early PSR puts the whole observable patch in causal contact), so that in the CPP picture inflation is **repurposed as the spectrum generator rather than as the horizon-solver**."

That is a claim about **causal contact** — whether distant parts of the observable sky could ever have communicated. It is not a claim about how large the universe is.

## §2 The 3823 shortfall is a different problem (verify T2)
3823 asked whether the pre-ignition ball, inflated and then carried through a standard thermal history, reaches the observable radius today. It does not, by ~10.5 e-folds. **That is a size requirement, not a horizon requirement.**

In standard inflation the two are solved by the same sixty e-folds, which is why they are easy to conflate — but they are logically distinct, and EU-1's VSL clause speaks only to the first. **A theory can put the whole sky in causal contact by fast early signalling and still fail to make the universe big enough.**

## §3 And VSL could not help even if it did (verify T3, T4)
This is the part worth keeping, because it removes the route without any appeal to what VSL means.

The requirement and the delivery both carry the same logarithm of the initial ball size:

> N_req = ln(R_obs/(R_init·a_ratio)),  N_del = ⅓ ln N_CP − ln(R_init/l_P)

so **R_init cancels in the difference**:

> **shortfall = ln(R_obs/(l_P·a_ratio)) − ⅓ ln N_CP = 10.51 e-folds, exactly, for every R_init.**

Verified at R_init = 1, 10, 10³ and 10⁻⁵ l_P: all give 10.51. **Enlarging the early ball reduces the requirement and the delivery by precisely the same amount.** So the "large early PSR → larger ball → more room" intuition, which is the only way VSL could bear on a size budget, fails identically at every scale.

## §4 The premise was already dead (verify T5)
Independently of §§1–3, the "large early PSR" the route rests on has not been available since 3816:

- **3816** re-grounded the paper's VSL sentence: the causal contact is the **first Moment's empty-register reach over a Planck-sized ball**, not an enlarged PSR, and the founder ruled that "large early PSR" was an inaccurate description. Whether any later epoch has a larger PSR was made an open question, not an assumption the paper may lean on.
- **3837** then worked that question and found **both branches give a PSR at or below l_P** — B1 (the PSR responds to the count) excluded by the tilt at ≥4.2σ, B2 (the PSR floors) contracting *below* l_P. **Neither branch ever produces a reach larger than the ordinary one.**

So the route was named at 3823 as the most promising escape **seven patches after the premise it needs had been re-grounded away**, and six patches after both its branches were closed. Nobody noticed, including me — 3823, 3835, 3837, 3841 and 3851 each carried "the VSL horizon computation" forward as owed.

## §5 What this leaves (verify T7, T8)
> **Route 1 is CLOSED.** Wrong problem; no effect even if it were the right one; premise withdrawn.

**Route 2 is unchanged and is now the only route.** Since the shortfall depends only on N_CP and the post-inflation thermal history, closing it needs

> **N_CP ≈ 5×10⁹⁷** against the founder's 10⁸⁴ — exactly 3825's number, with its independent pin **n_CP(today) ≈ 1.4×10¹⁷ m⁻³** (mean separation ~1.9 μm), checkable against the DE-lane Λ/sea work and SF-6's ε₀/μ₀.

**The tension stands at ~10.5 e-folds**, with one fewer escape and a sharper statement than before: **it is a constraint on the total CP count — or on the thermal history — and on nothing else.** Not on the ball size, not on the reach, not on the lattice resolution except insofar as that sets the count.

## §6 A note on the arc's bookkeeping
This is the second time in three sessions that an item carried forward as "owed and promising" turned out to have been closed by the lane's own earlier work (the first: 3847, where the chirality sector had refuted C-4 before C-4 was proposed). Both were found by reading the corpus rather than by computing. **The lane's handovers propagate open items faithfully but do not re-examine their premises**, and two of the last three sessions have been spent discovering that a premise had expired. That is worth a governance note more than another computation.

## §7 Standing
- **OPEN-EU-EFOLD-BUDGET-1 route 1 (VSL): CLOSED**, on three independent grounds (§§1–4).
- **New result:** the shortfall is **invariant under R_init** — an identity, verified across eight orders.
- **The tension stands at 10.5 e-folds** and is now a constraint on **N_CP alone** (given the thermal history).
- **Route 2 is the only remaining route** and already has its independent pin (3825).
- **Owed to EU-1 at V1.7 (small):** the §Background VSL sentence should record that it addresses causal contact and not the size budget, and that the budget shortfall is separately registered. Not urgent; bundle with the next substantive version.
- Unaffected: PRED-C-96 (untouched); T-1; T-2; the amplitude closure; AP-4's shell clause.

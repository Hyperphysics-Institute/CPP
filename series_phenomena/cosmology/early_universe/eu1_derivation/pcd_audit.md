# The PCD audit — every closure of the arc re-examined with the cascade model properly in hand. **One re-opening was real and I tested it: the cascade's 1/s² weighting WOULD convert a conserved density's blue spectrum into a scale-invariant one — exactly what the amplitude needs — but the kernel is cut off at the PSR, and observable modes sit ~60 orders inside the top-hat limit. The no-go stands.** Everything else is confirmation, including two closures the cascade strengthens

**Patch 3868, Session 193, 9 Sep 2026. Lane: EU.** Founder-directed: *"reconsider the problems that were considered closed/wrong/insoluble because of not having the model for the PCD in memory."* Verify `scripts/3868_pcd_audit.py` (10/10). Reasoning `reasoning/3868_pcd_audit.md`. Nothing adopted; **no closure reversed**; PRED-C-96 untouched; 3710 not retired.

## §1 The instinct was right, and one re-opening was real (verify T1, T2)
The 3860/3862 episode showed I had been reasoning about this protocol without the cascade model in hand. The founder's question is whether other verdicts were reached the same way. **One was, and it is the most consequential verdict in the arc.**

**3835's no-go turns on a premise the protocol does not supply.** It argues: only the count enters δN; the count is a **locally conserved density**; conserved densities obey integral constraints forcing P(k) → k²; hence blue, hence excluded. Every step assumes n̄ is a **flat local count**.

But the PCD does not deliver a flat local count. D-SUBPSR-FIELD pass 3 gives the perceived signal as **"MAXIMIZES inward, 1/s²-class."** A 1/s² kernel is **long-range**, and long-range weighting is precisely what evades conserved-density integral constraints — those constraints bind *local* densities.

**And the effect would have been decisive.** For a 1/s² kernel in 3D, Ŵ(k) = (4π/k)·Si(kR), so for kR ≫ 1, **Ŵ → 2π²/k** and

> **P_weighted(k) = |Ŵ(k)|² P_ρ(k) ∝ P_ρ(k)/k².**

A conserved density's blue **k²** becomes **k⁰ — scale-invariant.** That is exactly the spectrum the amplitude sector has spent ten sessions failing to find, and it would have arrived from the protocol rather than from a candidate.

## §2 It fails, on a cutoff (verify T3, T4, T5)
The kernel is not 1/s² to infinity. It is cut off at the PSR — that is what the reach *is*. With W(s) = 1/s² for s ≤ R and zero beyond:

> Ŵ(k) = (4π/k)·Si(kR), and for **kR ≪ 1**, Si(kR) → kR, so **Ŵ → 4πR = constant** — the top-hat limit.

| kR | Ŵ/R | top-hat 4π |
|---|---|---|
| 10³ | 0.020 | 12.566 |
| 10 | 2.084 | 12.566 |
| 1 | 11.889 | 12.566 |
| 10⁻³ | 12.566 | 12.566 |
| 10⁻⁶ | 12.566 | 12.566 |

**And the observable modes are not marginally inside the top-hat limit — they are about sixty orders inside it.** At a CMB scale of 100 Mpc, kR = k·l_P ≈ **5×10⁻⁶⁰**.

> **At observable wavelengths the cascade weighting acts exactly like a top-hat of size PSR. 3835's no-go is untouched and stands.**

The route closes on a quantitative cutoff rather than a hand-wave, which is the right way for a promising route to close. I record that I wanted this one to work.

## §3 The rest of the audit — confirmations, and two of them are strengthenings (verify T6–T10)

- **3841 (C-4's interaction range) — CONFIRMED, and the cascade could have overturned it.** If the 1/s² weighting were dominated by small s, the orientational coupling would act at the **GP spacing** and C-4 would die at m/H ~ 10³⁷ rather than 3.9×10³. It is not: the weighting exactly cancels the r² volume element, ∫(1/s²)(4πs² ds) = 4πR, so **each radial shell contributes equally** and the integral's mass sits at large s. **R ≈ l_P was right.**
- **3837 (the PSR dichotomy) — CONFIRMED, and shown COMPLETE.** I had worried a third branch existed — a cascade-weighted count distinct from both B1 and B2. At long wavelengths the cascade count is **identical to a top-hat count over the PSR**, which is exactly Branch B2. **No third branch exists where it would matter**, which is why B1/B2 exhausted the fork.
- **3818 (δkT) and 3822 (composition) — UNAFFECTED.** Neither used a flat-count premise. The cascade is species-blind by construction (SSV_abs sums *magnitudes*; only the S slot identifies species), and kT remains a rate coefficient however the count is sampled.
- **3829 (C-3), 3831/3833 (C-2) — UNAFFECTED.** Those objections concern the **pattern** — one characteristic scale, an initial slice stretched — not the kernel that samples it. A top-hat-equivalent kernel creates no scales in the pattern.
- **3862 — REINFORCED.** The same cascade that fails to rescue the amplitude is what delivers Moment-1 contact. **One mechanism, two verdicts, both now checked rather than assumed.**

## §4 What this settles
> **No closure in the arc is reversed by having the PCD model properly in hand.** The one verdict whose premise the protocol genuinely contradicted was tested at full strength and survives on a sixty-order margin.

That is a better outcome than it sounds. Before this patch, every negative in the arc carried an unexamined dependence on how the protocol samples the count. They no longer do, and the two closures that *could* have flipped (3841's range and 3837's completeness) are now positively supported rather than merely unchallenged.

**The founder's question was the right one and the answer is no.** Recording that plainly, having wanted the opposite.

## §5 Standing
- **3835's no-go: re-tested against the cascade, STANDS** on the PSR cutoff (observable modes ~60 orders inside the top-hat limit).
- **3841's interaction range: CONFIRMED** — the 1/s² weighting is uniform per radial shell, so the outer scale dominates.
- **3837's dichotomy: CONFIRMED and shown COMPLETE** — no third branch at observable scales.
- **3818, 3822, 3829, 3831, 3833: unaffected** — no PCD dependence in any of their arguments.
- **3862: reinforced.**
- **No closure reversed. The lane's status is unchanged** from 3866: substantive work complete pending maintainer decisions.
- PRED-C-96, T-1, T-2: untouched.

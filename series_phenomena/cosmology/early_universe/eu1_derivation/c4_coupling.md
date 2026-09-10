# C-4's coupling FOUND — orientational order modulates the magnitude of the arriving field vectors, hence SSV_abs, hence the PSR floor, hence WHEN inflation ends. It breaks the 3835 no-go, preserves PRED-C-96's tilt exactly, is Gaussian and adiabatic, and turns the amplitude into an output that fixes a sub-Planckian stiffness scale. And it makes T-1 load-bearing: the ℓ ≤ 5 vanishing is what keeps the mode light

**Patch 3839, Session 179, 9 Sep 2026. Lane: EU.** Works the single debt C-4 was left with at 3837 §6. Verify `scripts/3839_c4_coupling.py` (8/8). Reasoning `reasoning/3839_c4_coupling.md`. **DERIVATION CANDIDATE — not adopted.** Neither f nor ε is minted (PD-007); both are outputs owed. PRED-C-96's tilt untouched; 3710 not retired.

## §1 The coupling (verify T1)
The question was singular: is there a route by which the DP sea's orientation shifts *when* inflation ends, rather than how fast it runs? There is, and it runs through a definition the corpus already carries.

AP-4 fixes the DI-bit payload: **E is the vector sum** of all polar-charge contributions integrated by the origin GP. The receiver computes **SSV_abs = Σ|polar| + k·Σ|strong|** — a sum over arriving bits of each bit's *magnitude*.

At first glance that looks orientation-blind, and it is at the receiver: summing magnitudes discards the receiver-side directions. **But each arriving magnitude |E| is itself a vector sum at its source.** In an orientationally ordered region the source's contributions add; in a disordered one they cancel. With coordination z = 12 and orientational correlation C,

> |E|/e = √(z(1 + (z−1)C)), running from **3.46** (disordered) to **12.0** (aligned) — a factor √z.

So orientational order reaches SSV_abs with an order-unity lever, not a marginal one. **This is the coupling**, and it required no new axiom — only reading AP-4's "vector sum at the origin" together with the glossary's "sum of magnitudes at the receiver."

## §2 It reaches the end condition (verify T2, T3)
Under Branch B2 — the branch that preserves the tilt (3837 §4) — the PSR floors at ε and

> n̄_perc = n̄_ref e^{−3ε},  end at n̄_perc = 1  ⇒  **N = ⅓ ln n̄_ref − ε**,  hence **ζ = δN = δε**.

ε enters N *linearly*, so a fluctuation in ε is a fluctuation in the number of e-folds — precisely the modulated-end structure 3837 §6 identified as the only surviving route.

**And the 3835 no-go does not apply to it.** ε depends on orientational correlation, which is a **field**, not a conserved density. The integral constraints that force P(k) → k²/k⁴ apply to conserved densities and to nothing else. The no-go is broken not by evading its argument but by falling outside its premise.

## §3 The tilt survives exactly (verify T4)
This is the requirement that killed Branch B1 and every earlier candidate, and it is met without adjustment. The count keeps ln n̄ linear in N_rem, so the *background* is untouched — ε is a constant offset, not a distortion. The spectator's fluctuation rides the Hubble rate:

> ζ = ε · H/(2πf)  ⇒  P_ζ ∝ H² ∝ N_rem²  ⇒  **n_s − 1 = −2/N_rem = −0.0351, n_s = 0.9649.**

**PRED-C-96 is unchanged and is now carried by the spectator rather than by the count directly.** The 3837 conflict is resolved exactly as its §6 predicted: separate the driver from the carrier and both constraints can be met at once.

It is also **Gaussian** (a free field) and **adiabatic** (a modulated *end* shifts when everything finishes, not one species' abundance) — the two properties that killed C-3 and the compositional candidate respectively.

## §4 The amplitude becomes an output (verify T5, T6)
Requiring ζ = √A_s = 4.58×10⁻⁵ with H/M_Pl = 1.93×10⁻⁵ gives

> **f/M_Pl = ε / 14.9.**

This is the opposite of a fit. It says: once ε is derived — and ε is the PSR floor, which is the remaining half of OPEN-EU-PSR-EARLY-1 — the orientational stiffness scale f is **fixed**, with no freedom left. For ε ≲ 1 it lands **sub-Planckian** (at ε = 0.15, f ≈ 10⁻² M_Pl), which is where a lattice order parameter's stiffness scale ought to sit. The e-fold cost is mild in that window (ε = 0.15 costs 0.15 e-folds).

**PD-007 is respected:** neither ε nor f is chosen here. The relation between them is derived, and it converts the amplitude from an unexplained input into a consequence of a quantity the lane already owes.

## §5 The mass problem, and why T-1 rescues it (verify T7, T8)
A Goldstone needs a broken *continuous* symmetry, and the 600-cell lattice already breaks rotations down to the icosahedral group. So the orientational mode is a **pseudo-Goldstone**, and its mass comes from the residual lattice anisotropy. On any ordinary lattice that anisotropy is O(1) and the mode is heavy — which is exactly how this candidate would normally die, alongside the register spring.

It does not die here, and the reason is a result already on the books. **T-1 (3820) showed that the icosahedral census is isotropic *exactly* through ℓ = 5** — dipole, quadrupole, octopole, ℓ = 4 and ℓ = 5 all vanish identically — with the first anisotropic invariant at **ℓ = 6**. The symmetry-breaking term that would give this mode its mass is therefore not O(1) but sixth-order.

> **The lattice's exceptional isotropy is the reason the only viable ζ candidate can be light at all.** T-1 was delivered as a symmetry statement with no observable attached, and explicitly disclaimed as a fingerprint (3820 §4). It is now load-bearing for the amplitude.

**The quantitative bound is owed, not computed here.** What must be shown is ω/H ≲ 1 given an ℓ = 6 leading term. That is the candidate's principal remaining risk and should be attacked first.

## §6 What C-4 still owes, in priority order
1. **The mass bound.** ω/H ≲ 1 from the ℓ = 6 anisotropy. If this fails, C-4 fails, and it fails the same way the register spring did. **Attack first.**
2. **ε derived** — the PSR floor under saturated load, the remaining half of OPEN-EU-PSR-EARLY-1. Fixes f through §4.
3. **The O(1) coefficient** in δε ≈ ε δθ, which §4's relation carries implicitly.
4. **An explicit adiabaticity check.** §3's argument is structural; the isocurvature fraction should be computed against Planck's few-percent bound rather than argued.

## §7 Standing
- **C-4 (orientational pseudo-Goldstone): DERIVATION CANDIDATE.** First candidate in this arc to clear every registered wall at once — it reaches the end condition (§2), escapes the no-go (§2), preserves the tilt exactly (§3), is Gaussian and adiabatic (§3), and makes the amplitude an output (§4). **Not adopted**; four debts stand (§6).
- **The 3837 structural conflict is resolved in principle**, exactly by its own §6 route: driver and carrier separated.
- **T-1 (3820) is re-graded from a symmetry curiosity to a load-bearing result.** Its ℓ ≤ 5 vanishing is the mass suppression this candidate needs. Note that 3820 §4 explicitly refused to claim an observable from ℓ = 6; that refusal stands — this is a *mass* consequence, not a CMB fingerprint.
- **OPEN-EU-PSR-EARLY-1 is revived in its second half**: ε (the PSR floor) is now the quantity that fixes f. Its first half (held vs perceived) closed at 3837.
- **CONV-046 package:** C-4 is the first *positive* item in it. Recommend the panel see the 3837 conflict and this resolution together, since neither is properly gradeable alone.
- **Honest scope:** §2–§4 assume Branch B2 and a canonically normalised Goldstone with decay constant f; §5's suppression is qualitative pending the bound. Nothing is adopted and no constant is minted.
- Unaffected: the e-fold budget (still ~10.5 short, independently — 3823); T-2; PRED-C-96's value.

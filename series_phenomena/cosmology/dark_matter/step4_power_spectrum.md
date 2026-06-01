# DM Arc — Step 4: Power Spectrum from Swirl Seeds

**Patch:** 0725 (1 June 2026) · **Work item:** OPEN-COSMO-DM-1 Step 4 · **Gate:** power spectrum (the most discriminating)
**Status of result:** **SERIOUS TENSION — NOT passed, NOT cleanly killed.** This is the dominant open problem for CONJ-COSMO-1 and the arc's weakest link. The cheap kills (Steps 1–3) and the rotation-curve consistency (Step 5) all survived; Step 4 is where the conjecture meets the deepest problem in structure formation and does not currently clear it.
**Verify:** `scripts/0725_power_spectrum.py` (CHECK 1/2/3)
**c08 exposure:** the growth half inherits the Step-D conditional background; the obstacle below is independent of c08 (it is about the *seed origin*, not the expansion dynamics).

## The question split in two

**Q1 — growth (does the observed P(k) follow given the right seeds?).** YES, inherited. Given a near-scale-invariant adiabatic primordial spectrum, the CPP (conditional Step-D) Friedmann background plus standard gravitational growth reproduces the observed P(k): the BBKS transfer function gives the rise ∝ k^{n_s} at low k, the turnover at k_eq ≈ 0.015–0.02 h/Mpc, and the fall ∝ k^{n_s−4} ln²k at high k (CHECK 1). CPP adds nothing and breaks nothing here — the transfer/growth is standard.

**Q2 — seed origin (do CPP's swirls *produce* that spectrum?).** This is the hard part, and prima facie **no**. The conjecture seeds structure with early-universe "swirls" from radial-expansion collisions — a **causal (active-source)** mechanism. Causal seeds hit the well-established observational wall that ruled out cosmic-string/defect models as the primary structure source:

- **Super-horizon correlations (CHECK 2).** The comoving particle horizon at recombination subtends θ_H ≈ 1.15° → ℓ_H ≈ 157. Causal physics can correlate only ℓ ≳ 157. But the observed CMB has correlated *adiabatic* power at ℓ < 157 — the Sachs–Wolfe plateau (ℓ ~ 2–50) and, decisively, the **TE cross-correlation anti-peak at ℓ ≈ 100–150**, the textbook smoking gun for *super-horizon* perturbations present *before* they could be causally generated. Causal swirl seeds cannot make these.
- **Acoustic-peak coherence.** Active sources continuously stir perturbations, producing **incoherent (smeared) acoustic peaks** rather than the observed sharp harmonic series, which requires perturbations laid down *coherently* on super-horizon scales (the inflationary signature).

So the swirl mechanism, taken at face value as a causal seed, fails the two cleanest tests that distinguish inflationary (acausal, coherent) from active (causal) structure formation.

## The live escape — and why it is not yet a pass

CPP has one feature standard active-source models lack: the **atemporal Nexus** — the non-local substrate that enforces "instantaneous coordination of all Conscious Points... independent of local spacetime coordinates" at each absolute Moment. A genuinely non-local coordination, by construction *independent of light-cones*, could in principle seed **acausal / super-horizon correlations** — a CPP-native potential resolution of the horizon problem, and a route to coherent super-horizon initial conditions *without* inflation. That is the live escape from the active-source wall.

But it is not a pass, for three reasons:
1. **Undeveloped.** No CPP model derives Nexus-seeded perturbations; it is a conjectural hook, not a calculation.
2. **CPP-flagged as ungrounded.** CPP's own SR-paper review notes the atemporal Nexus "lacks physical grounding."
3. **Scale-invariance is the real bar.** Even granting acausal Nexus coordination, the mechanism must be shown to produce a *near-scale-invariant* (n_s ≈ 0.96) *adiabatic* spectrum with the right amplitude (A_s ≈ 2.1×10⁻⁹) — the specific, precisely-measured feature inflation explains. Nothing in CPP currently predicts this; producing scale-invariance from a substrate mechanism is a strong, non-generic requirement.

## Verdict and what it means for the arc

- **Step 4 is the genuine frontier and the arc's weakest link.** Falsification-first did its job: the cheap kills survived, and the hardest, most discriminating step exposed the deep problem — the *origin* of the primordial spectrum, the same problem inflation was invented to solve.
- **CONJ-COSMO-1 is NOT confirmed.** Its rotation-curve and microphysics gates pass, but its *structure-formation* mechanism (swirl seeds → P(k)) does not clear the active-source wall. The conjecture's survival hinges on whether the atemporal Nexus can be developed into an acausal seed mechanism yielding a scale-invariant adiabatic spectrum.
- **This is a tension, not a clean kill** — because the Nexus is a real disanalogy from standard active sources, leaving a live (if narrow and undeveloped) escape. But intellectual honesty requires stating that, as of now, the most discriminating DM test is **unmet**, and CPP does **not** reproduce the observed power spectrum.

## Honest caps

- The obstacle is the standard active-source/causal-seed result (Spergel–Zaldarriaga TE diagnostic; defect-model CMB studies), applied to the swirl conjecture; it is robust and not a CPP-specific artifact.
- The "Nexus escape" is the fair counterweight, stated as undeveloped — I am neither dismissing it nor crediting it.
- This does not retroactively weaken Steps 1–3/5; it isolates structure formation as the failing/open gate.
- New open problem registered: **OPEN-COSMO-DM-2** (the Nexus-seed / scale-invariance problem) — the dominant requirement for CONJ-COSMO-1, and arguably a shared problem with OPEN-SR-6 (Big Bang dynamics) and any CPP account of the horizon problem.

# T-3b first computation — δkT → ζ under the geometric end condition: ζ = 0, S = 0, HALT

**Patch 3818, Session 169, 9 Sep 2026. Lane: EU.** Follows FORK-EU-OCCUPANCY-1 resolution (3816, Branch P, small-ball reading). C-1 (bath-energy mode, from the founder's kinetic picture at 3813) is the T-3a candidate under test. Verify `scripts/3818_t3b_delta_kT_checks.py` (4/4). Reasoning `reasoning/3818_t3b_delta_kT.md`. Nothing minted; no constant adopted (PD-007); PRED-C-96 tilt unaffected. **HALT triggered** (charter §4): S = 0 < 220 under a founder-supported mode structure; tension registered against PRED-C-96's companion amplitude (A_s); T-3b stops here; new T-3a founder picture required.

## §1 Setup

**C-1 (bath-energy mode).** The founder's kinetic picture (3813): the KE of every CP's first move is held in the bulk's DP arcs; this sources the bath temperature kT. Because H_eff = κ₀ kT ln n̄, a patch-to-patch fractional fluctuation in the bath energy is multiplicative on H_eff: **δH/H = δkT/kT**. This is the mode registered at 3813 §2 as tracking H automatically and changing slower than the spreading. Whether it yields ζ is this document's question.

**The δN formalism (as used in EU-1's own §Amplitude).** In the separate-universe approximation, ζ(x) = δN(x) = N_*(x) − ⟨N_*⟩, where N_*(x) is the local number of e-folds from the initial flat slice to the end-of-inflation flat slice. This is gauge-invariant; the time-shift (δt) formulation is gauge-dependent and is not used here.

**N_* under the re-grounded count law (3816 §3).**

> N_* = ⅓ ln(n̄_init / n̄_end), n̄ ≡ CPs within one rest-frame Planck sphere.

At ignition (Moment 1): n̄_init(x) = N_CP for all x (every point sees the whole ball by the empty-register argument; no spatial variation at Moment 1). End condition: **n̄_end = 1** (one CP per Planck sphere — purely geometric; see §3). Therefore:

> **N_*(x) = ⅓ ln N_CP − ln(R_init/l_P) = const.**

**δN = 0 everywhere. ζ = 0.**

## §2 Why δkT does not enter N_*

kT appears in H_eff = κ₀ kT ln n̄. H_eff sets the *rate* of expansion (e-folds per unit time), not the *number* of e-folds. A patch with higher kT has higher H_eff and reaches the end sooner in time — but it reaches it in the same number of e-folds, because the dilution law n̄ ∝ a⁻³ and the end condition n̄_end = 1 are both independent of kT. The distinction is:

- δkT → δH_eff/H_eff = δkT/kT [a rate fluctuation]
- δN = d(ln n̄)/3 = (1/3)d(ln ρ_CP · l_P³) [a count fluctuation; no kT]

In standard single-field inflation δφ → ζ because φ determines both H (through V(φ)) and the end condition (reheating at φ_end); both ends of the δN bridge involve φ. Here kT determines H but not the end condition (§3); only one end of the bridge exists. **S = 0.**

## §3 The geometric end condition

Under Branch P (3816), inflation ends when the mean density falls to one CP per rest-frame Planck sphere: ρ_CP · (4π/3)l_P³ = 1. This is a spatial-average condition on the CP number density. As long as the CP count is conserved (dilution only, no creation or annihilation) and the Planck sphere volume is fixed (l_P is a substrate constant, not kT-dependent), the end condition is met at the same a_end/a_init = N_CP^{1/3} everywhere. kT appears nowhere.

The one exception: if the **perceived** n̄ uses a contracted PSR (OPEN-EU-PSR-EARLY-1, §4.b) and the PSR contraction depends on kT, then δkT could shift the end of the *perceived* inflation. That is a legitimate escape route but requires:

  (a) the early PSR law (not yet derived — PSR-EARLY-1's target); and
  (b) a kT → SSV_abs coupling for the crowded era (not established).

Under S-HENGINE-HELD's **held-count** reading the engine's n̄ is D4-conserved from Moment 1 and the PSR contraction is irrelevant. Under the **perceived-count** reading the gap exists but the formula requires PSR-EARLY-1. Both are noted in §4; neither is computed here.

## §4 HALT: tension against PRED-C-96's companion amplitude

**Charter §4 HALT rule:** "if W-2 returns S < 220 under a mode structure the founder's picture supports, register the tension against PRED-C-96's companion amplitude (not against the tilt), stop, and dispatch."

- W-2 candidate under test: C-1 (bath-energy mode; from the founder's kinetic picture, 3813 §2; founder-supported).
- Result: S = 0 < 220. HALT triggered.

**Tension statement.** PRED-C-96 is n_s = 1 − 2/N_* = 1 − 2/57 ≈ 0.9649 — the tilt. It rests on the shape of the count law (d ln n̄/dN = −3) and is unaffected. Its **companion amplitude** is P_ζ(k_*) = A_s = 2.1×10⁻⁹ (Planck 2018). EU-1 asserts P_ζ ∝ H_eff² (the spectator prescription, §Amplitude) but does not derive the fluctuating variable. C-1 is the first candidate from first-principles grounds, and it gives ζ = 0. **The source of A_s is unidentified.** This is not a falsification — EU-1's framework-conditional label already covers the amplitude — but it is the sharpest statement of the gap: not only is the variable unnamed, but the natural candidate does not work under the simplest reading of the end condition.

Registered tension item: **OPEN-EU-AMPLITUDE-1** (see §5).

## §5 Escape routes and standing (neither computed at this patch)

**Route 1 — perceived-count end condition (requires PSR-EARLY-1):** If the end condition is "perceived n̄ = 1" (ρ · (4π/3) PSR³ = 1) and PSR depends on kT through SSV_abs, then δkT → δPSR_end → δn̄_end → δN ≠ 0. Requires: the early PSR floor law (PSR-EARLY-1's target) and a kT → SSV_abs coupling in the crowded era. If PSR → l_P as SSV_abs → 0 (the held-count limit), this route closes and we return to ζ = 0. If PSR_min depends on kT, ζ ≠ 0 but so does the correction to N_* — they must be computed together.

**Route 2 — a kT-dependent end condition from first principles:** If inflation ends when H_eff falls to a kT-set threshold (e.g., a rate derived from the bath's own relaxation), the end time depends on kT and δN ≠ 0. No such threshold is on file; its derivation would be a separate T-3a step.

**Route 3 — a different T-3a candidate:** C-1 is not the only possible mode. Charter §6 Q1 ("what wavers slowly in the crowd?") is still open. The register spring was withdrawn (3812, too heavy), the count is conserved (not a waving variable), and the pairing pattern is frozen (3812). What remains: the spatial gradient of the unstacking rate, the bath's local composition, or a variable the founder's next picture identifies. Q1 remains open; T-3a is not closed.

**Standing:**
- **OPEN-EU-AMPLITUDE-1** — the source of P_ζ = A_s in the CPP engine; T-3a candidate C-1 (bath-energy mode) gives ζ = 0 under the geometric end condition; two escape routes identified (PSR-EARLY-1-mediated; kT-dependent threshold); T-3a otherwise open (Q1 still open). Owner: EU lane. Pass line: S ≥ 220.
- PRED-C-96 tilt (n_s): **UNAFFECTED**. Only the amplitude companion is in tension.
- T-3b first computation: HALT. Next: a new T-3a founder picture (Q1, charter §6) before any further δN computation.
- CONV-046 candidate package: the re-grounding (3816) + the S-HENGINE-HELD wording note go to the panel. The HALT is registered in the same package. Panel timing unchanged (no panel until T-3b clears or a CONV-046-grade picture result; the HALT itself is a registered tension, not a win).

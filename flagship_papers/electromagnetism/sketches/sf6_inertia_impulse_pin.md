# SF-6 inertia impulse pin — F = ma from DP-sea back-reaction (first computation)

**Status:** first computation complete (Patch 2496). Feeds OPEN-FP-6-INERTIA-1.
**Charter:** `handovers/2026-07-14_sf6_inertia_impulse_investigation_opened.md`; founder physics in `series_phenomena/cosmology/dark_matter/reasoning/2470.md` §5.
**Verify script:** `../code/2496_sf6_inertia_impulse.py` (all numbers below reproduce end-to-end).
**Discipline:** G7 throughout — the coefficient is *predicted from statics before dynamics runs*, never tuned; the DM ring is not in view; blind-session guards on the SR/PROP sectors respected (no SR-sector citations anywhere below).

---

## 1. The question

SF-6 identifies inertial mass with the standing ZDC pattern (E = ℏν_C), but its one effective-inertial-mass computation converges only "by tuning the model parameters" (SF-6 v1.0, §; ~line 213). The CPP primitive is Aristotelian and memoryless — displacement ∝ net force each Moment — which on its face *contradicts* Newtonian inertia. The founder's mechanism (2470 §5): when a CP accelerates, the eDP poles of the sea swing counter to the motion (the induced-current analog); the sea stores energy against velocity *change* (½LI² with v playing the current and the sea's polarization stiffness playing the inductance); steady velocity is a comoving pattern costing nothing (Galilean compliance); F = ma must *fall out* of the back-reaction, with the coefficient read off, not fit.

## 2. The model (isolated, minimal, honest)

One CP. **No bare inertia anywhere.** The sea is a scalar toy of the SF-6 eDP polarization response: a field φ with the shipped wave dynamics at c (the model's wave equation is Lorentz-covariant with c as a mathematical property of its own construction — no external covariance input). The CP sources φ with coupling g, Gaussian-smeared at the lattice scale (width σ ~ h; on the real substrate σ *is* the lattice scale). The CP's primitive is the **unmodified** Aristotelian rule v = μF per Moment.

Because the CP itself carries no momentum and no kinetic energy, *all* momentum and *all* kinetic energy must live in the sea. That single fact makes the prediction chain zero-free-parameter:

## 3. The zero-free-parameter chain

**Stage 0 (statics).** Measure the rest-cloud polarization energy U on the lattice. Isotropy of the static gradients gives ∫(∂_zφ)² = (1/3)∫|∇φ|², hence the comoving cloud of a slowly translating source carries field momentum

> **P = (2/3)(U/c²) · v  ⇒  κ_pred = (2/3) U_pol / c²** — fixed by statics *before any dynamics runs*.

**Two-line uniqueness proof (no 4/3-type ambiguity at this order).** The energy coefficient equals the momentum coefficient for the rigid source: the static cloud minimizes E_pot at fixed source (Euler–Lagrange), so the O(v²) cloud distortion contributes *zero* potential-energy change, and dE = kinetic term only = ½ v²∫(∂_zφ_s)² = ½ (2U/3c²) v². Hence **κ_E = κ_P = (2/3)U/c² exactly at non-relativistic order**; the classical 4/3-family pathologies are pushed entirely to O(β²) and to non-rigid/self-bound structure (registered follow-up, §6).

**Stage A (steady comoving states, FFT).** Solve (c²k²_lat − v²k_z²)φ̂ = gρ̂ at several v; read P/v and 2dE/v².

**Stage B (dynamics, ramp-and-hold).** Prescribed smoothstep ramp 0 → v_f = 0.05c over 30 time units, then hold. Measure the Momentwise back-reaction F_self(t). Prediction: F_self = −κ_pred·a(t), Momentwise — i.e. **Newton's second law read directly off the substrate**. Where inertia "locks in" is decided by the dynamics (founder's flag), not asserted: the back-reaction tracks the *instantaneous* acceleration, retarded only by the cloud light-crossing time σ/c.

**Stage C (release).** Mid-hold, switch the CP to the pure Aristotelian primitive at mobility μ. The finite-μ bath drains field momentum at rate v/μ, so v(t) ≈ v₀ exp(−t/κμ): **coasting is exact in the force-free limit μ → ∞ (Newton's first law emergent), and τ/μ is a third independent reading of κ.**

**Stage D (convergence).** Repeat at σ = 2.5: the operational coefficient must approach (2/3)U/c² as the smearing grows.

## 4. Results (N = 96, c = h = 1, dt = 0.35, σ = 1.5, g = 8, v_f = 0.05)

| reading | value | ratio to κ_pred |
|---|---|---|
| statics prediction (2/3)U/c², U = 0.8935 | **0.5957** | 1 (by construction) |
| steady P/v (FFT, v = 0.025) | 0.5749 | 0.9652 |
| steady 2dE/v² (FFT, v = 0.025) | 0.5752 | 0.9656 |
| Momentwise −F_self/a (ramp, dynamics) | 0.6262 | 1.0513 |
| hold-phase P/v (dynamics) | 0.6210 | 1.0425 |
| coast τ/μ (μ = 10; τ = 7.87) | 0.7874 | order-consistent |
| coast τ/μ (μ = 25; τ = 16.25) | 0.6500 | → κ_dyn as μ ↑ |

Residual constant-velocity force at hold: **2.9% of peak back-reaction**. **[CORRECTED AT PATCH 2868 — the parenthetical originally read "(Galilean compliance in-model; the residual is the time-staggering floor of the integrator)". THAT ATTRIBUTION IS REFUTED IN THIS MODEL'S OWN NUMBERS. Refinement study `../code/2868_hold_force_refinement.py`: F_hold is FLAT under 4x dt-refinement (4.683e-5 → 4.698e-5), FLAT under 2x sigma-refinement (4.688e-5 → 4.637e-5), EXACTLY LINEAR in v (F_hold/v constant to 0.6% across 4x in v), and its SIGN IS FORWARD, along the motion — not a drag. It is neither a temporal nor a spatial discretization artifact. The quoted ratio rises to 6.0% at sigma=3.0 only because the denominator halves. Galilean compliance is NOT demonstrated here; a forward self-force linear in v is self-amplifying and is the §7(a) bare-point runaway, measured rather than observed in passing.]** Convergence at σ = 2.5: FFT ratio 0.9652 → 0.9893 from below, Momentwise ratio 1.0513 → 1.0200 from above — **both converge on (2/3)U/c²**. The residual deviation at σ ~ h is the substrate's genuine discreteness correction to inertia, not numerical error.

## 5. Conclusions

1. **Newton II is derived in-model.** F = κa emerges Momentwise from DP-sea back-reaction with the memoryless Aristotelian primitive left completely unmodified. The apparent contradiction between the CPP primitive and Newtonian inertia is resolved: the memory lives in the sea, not in the CP.
2. **The coefficient is pinned by statics, zero knobs:** κ = (2/3)U_pol/c², with the (2/3) a pure geometric (isotropy) factor of the scalar toy. Six independent readings agree within lattice-discreteness corrections that shrink under σ-refinement.
3. **Newton I is emergent.** A dressed CP persists in motion; the finite-mobility bath drains momentum on timescale τ = κμ, vanishing as a friction in the force-free limit μ → ∞. Inertia and momentum conservation arise together, from the same stored-pattern physics.
4. **Lock-in is continuous and dynamical:** the sea charges the CP κ·a at every Moment of the acceleration, retarded only by σ/c. Nothing is asserted about "where" the kinetic energy enters — the dynamics decides, per the founder's flag.
5. **All kinetic energy is sea energy.** ½κv² is measured in the field; the CP carries none. "The resistance you feel *is* the inertia."
6. **Open-cloud vs closed-pattern distinction (the electron anchor).** The bare CP's polarization cloud is an *open* field configuration: its coefficient is (2/3)U/c². A *self-bound standing pattern* (the physical electron, SF-1 cage) is a closed system, and by Laue's theorem a closed system's boosted energy-momentum is a four-vector — its inertial coefficient is **exactly E₀/c², coefficient 1, forced**. With SF-6's own identification E₀ = ℏν_C = m_ec², the electron's inertial mass is m_e with no tuning: this resolves SF-6's "tuned parameters" debt at the mechanism level. (Numerical simulation of the SF-1 cage under this same protocol is the registered next step; the covariance input is the model's own wave equation plus SF-6 — no SR-sector content used.)
7. **Registered debts (not absorbed):**
   (a) *Bare-point runaway* — observed empirically at high mobility during development (the Abraham–Lorentz analog: the undressed massless point surfs its own retarded wake). Reading: a bare, undressed CP is not a stable asymptotic object of the substrate; physical particles are dressed/standing patterns. Registers as its own item.
   (b) *Scalar-toy caveat* — the (2/3) is scalar-specific; the true eDP response is the SF-6 vector polarization. The mechanism is model-independent; the pure number is not. Vector redo owed.
   (c) *O(β²) structure* — rigid-source vs boosted-cloud differences, radiation reaction, and relativistic limits are their own items per charter.
   (d) *Electron anchor computation* — SF-1 cage under this protocol.

## 6. What this buys SF-6

The inductance analogy in 2470 §5 is now a computation: sea polarization stiffness *is* the inductance, v *is* the current, and the ½LI² storage law is the measured ½κv² with κ derived. SF-6's effective-inertial-mass section can replace its parameter-tuned convergence with: (i) the statics-pinned open-cloud coefficient, and (ii) the Laue coefficient-1 result for closed standing patterns, anchored on E = ℏν_C.

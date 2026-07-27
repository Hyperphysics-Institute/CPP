# PR4-BARE ANALYTIC ARTIFACT — no identified energy supports a Gibbsian marginal for the bare Moment rule

**Patch 2818. Submitted under PR4 as amended (adjudication 2817, M2/M3),
to the panel's nine-item specification (S1, adopted 5–0). Marking
PR4-BARE MET-NEGATIVE is the panel's act, not this document's.**

## 1. The exact bare transition law and full state variables

**State:** (X, Q) where X = {(x_c, σ_c)} are CP lattice positions with
polarities σ_c ∈ {+1, −1} on a periodic FCC sublattice of an M³ torus,
and Q: lattice → ℝ is the relay field carrying transmitted charge
content. Q is REAL-VALUED; the state space is therefore continuous,
not finite (see item 8).

**Transition (synchronous, deterministic, C19–C22):**
1. inj_t(g) = Σ_{c: x_c = g} σ_c
2. Q_{t+1} = W_R ∗ (Q_t + inj_t), where W_R is the origin-directed
   R-hop icosahedral relay kernel, probability-normalised (Ŵ(0) = 1)
3. SSV_net(g) = [U_R ∗ (Q_t + inj_t)](g) (vector kernel);
   SSV_abs(g) = [W_R ∗ |Q_t + inj_t|](g)
4. x_c ← snap[ x_c + σ_c · (|SSV_net|/SSV_abs)(x_c) · R ·
   SSV_net(x_c)/|SSV_net(x_c)| ], zero-net ⇒ stasis

No stochastic element, no thermostat, no bath, no reservoir coupling.

## 2. The admissible functional class tested

Six natural candidates spanning particle, field, and total energy:
H_coulomb = Σ_{i<j} σ_iσ_j/d_ij; H_yukawa = Σ σ_iσ_j e^{−d/3}/d;
H_r2 = Σ σ_iσ_j/d²; H_field = Σ_g Q²; H_absfield = Σ_g |Q|;
**H_total = H_coulomb + H_field** (the natural total-energy
candidate). d = minimum-image distance, floored at 1.

## 3–5. Non-conservation, with numerical-error and finite-volume controls

Spread / |mean| of each functional along deterministic trajectories
(100–120 Moments), four independent geometries:

| geometry | coulomb | yukawa | r⁻² | field | \|field\| | **total** |
|---|---|---|---|---|---|---|
| M=12, R=3, N=24 | 3.87 | 7.31 | 14.07 | 2.63 | 0.98 | **4.14** |
| M=16, R=3, N=48 | 4.49 | 23.00 | 16.34 | 1.46 | 0.57 | **5.02** |
| M=12, R=4, N=24 | 9.78 | 6.46 | 5.11 | 2.73 | 1.09 | **9.56** |
| M=20, R=3, N=80 | 2.91 | 6.70 | 23.27 | 1.56 | 0.54 | **3.15** |

**Every functional in the class varies by at least 54% of its own
mean, and most by many multiples of it, in every geometry.**

**Numerical-error control:** |ΔH| per Moment averages 1.128 (min
0.0769, max 6.54) against a float64 noise floor of ~10⁻¹⁵ for
H ~ O(5) — the variation exceeds numerical noise by ~10¹⁵. CP
positions are exact integers; field operations are FFT convolutions
with relative error ~10⁻¹⁴. The variation is dynamical, not
numerical.

**Finite-volume control:** non-conservation persists at M = 12, 16,
20; R = 3, 4; N = 24, 48, 80. Ratios remain O(1) or larger in every
case with no trend toward conservation as volume or particle number
grows. Not a finite-volume artifact.

## 6. What this does and does NOT establish

**ESTABLISHES:** none of the six natural candidate functionals —
including the total particle-plus-field energy — is conserved under
the bare Moment transition law, in any tested geometry, by margins
vastly exceeding numerical error.

**DOES NOT ESTABLISH:** that no invariant functional of any kind
exists. This artifact tests a defined class. A nonlocal,
history-dependent, higher-order, or field-state-entangled invariant
is not excluded, and no theorem is claimed. (Panel-adopted wording,
2817 M1.)

**THE OPERATIVE CONCLUSION:** the bare rule supplies **neither** an
identified conserved energy **nor** a bath/detailed-balance
mechanism. A Gibbs measure μ ∝ e^{−βH} is defined relative to an
energy and is stationary under H-conserving dynamics or under
bath-enforced detailed balance. With neither specified, **PR4's
Gibbs-marginal test is presently undefined for the bare rule: there
is no identified energy relative to which Gibbsianity can be
evaluated.**

## 7. Why Metropolis/HNC concordance cannot be attributed to the bare rule

The Metropolis machinery underlying every screening result in this
programme SAMPLES e^{−βH_coulomb} by construction: it imposes the
Gibbs measure as an input via its acceptance rule, at a temperature
supplied externally. The bare Moment rule neither conserves
H_coulomb (§3–5) nor contains an acceptance rule, a temperature, or a
bath. Agreement between Metropolis results and HNC therefore tests
the HNC closure against the Metropolis ensemble — it says nothing
about whether the Moment dynamics realises that ensemble. This is
precisely what PR4's own sentence ("Metropolis or HNC concordance
cannot satisfy PR4") was written to prevent, and the finding here
vindicates that sentence rather than evading it: the screening
results remain valid conditional on the Gibbs assumption, and that
assumption is now explicitly unsupported by the bare dynamics.

## 8. Failed hypotheses, marked NON-LOAD-BEARING

- **H-CONTRACT** (the field forgets initial conditions, making the map
  non-injective): **FAILED.** max|Ŵ(k)| over k ≠ 0 is 1.000000 at
  display precision — the shell kernel admits non-decaying
  zone-boundary modes. Empirically, two runs with different initial
  fields and identical initial positions DIVERGED (|Q₁−Q₂|_max
  persisted at ≈ 0.07–0.10 over 60 Moments).
- **H-FINITE** (finite state space forces eventual periodicity):
  **NOT APPLICABLE.** Q is real-valued, so the state space is
  continuous; no exact recurrence within 600 Moments.

**Neither hypothesis is used anywhere in items 3–7.** The conclusion
rests on the functional-class measurement alone.

## 9. Falsifiers — what would reopen this conclusion

1. Exhibition of ANY conserved functional of the bare rule
   (particularly nonlocal or history-dependent), with conservation
   demonstrated to preregistered tolerance across geometries.
2. Identification of an intrinsic bath/detailed-balance structure in
   the transition law that this artifact overlooked.
3. Demonstration that a stationary measure exists which is Gibbsian
   in some functional NOT in the tested class.
4. A regime (PSR/spacing, density, or lattice) in which the tested
   functionals become conserved — the controls tested four, not all.
5. A proof that the completed C23/C24 rule reduces to the bare rule
   in some limit while conserving energy, which would indicate the
   bare rule's non-conservation is an artifact of incompleteness
   rather than a property.

Item 5 is the live one: the artifact's conclusion is explicitly a
statement about the rule **as currently specified**, and
OPEN-PR4-C23C24 is where its completion is adjudicated.

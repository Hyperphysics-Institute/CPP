# OPEN-DM-ENDBOND-1 — R-A executed under the 2544 pre-registration: the functional walk finds the static strong-sector pairwise form UNREGISTERED — Branch I, named blocker; the electric-sector partial banks ANTI-bound ([−4.4, −2.1] MeV); one-registration reopening contract

**Patch 2546, 18 July 2026. Status: OPEN-DM-ENDBOND-1 BLOCKED at Branch I (named blocker:
"strong-sector pairwise form"); partials banked per the pre-registration's own Branch-I limb.
No depth frozen; gates G1/G2/G3 did not fire. Verify: `code/2546_endbond_ra_walk.py` (all
assertions pass; blindness order enforced in code — the Branch-I determination is printed from
artifact-text findings before any lattice number is computed).**

## 1. The functional walk (mandatory first act, prereg §2.2) — findings with sources

**(i) Which cross-plane pairs are strong-coupled.** The registered *energy* content couples
every pair through the species weight product inside the signed switched-pair statics
(2450 `Esw`: E = −(1−2δ)·Σ WᵢCᵢWⱼCⱼ·ℏc/r, δ = 3/7; W_q² = α_s, W_e² = α). The strong sector
enters the energy ONLY through those α_s weights and the 2455 saturation lengths. The
always-attractive color channel of 2455 confirmation (3) — "the strong force of the
superimposed qCPs will still attract... even if the polar attraction is neutralized" — is
registered as a **dance kinematic rule** (targeting continuation into pile-ups); it appears in
**no registered energy functional** (the 2455 sampled energy is the signed soft-core sum; the
strong pull enters only the target-choice weights). The 2455 smeared-Coulomb form is registered
**for a superposing pair in the DP state**; *which* static cross-plane qq pairs sit in that
channel, at what duty, with what pairwise additivity in a static lattice, is nowhere
registered. 2450's own scope note states the gap outright: *"the functional does not bind
under dilation (E0 = +486 MeV > 0); cohesion is the strong-sector registry, whose stiffness...
unmodeled."* **Determination: the static strong-sector pairwise form is UNDER-DETERMINED by
the artifacts. Branch I fires at walk level** — per prereg §2.2 this is a named blocker, not
license to invent a form, choose a pair set, or import a regularization.

**(ii) Radial form and saturation.** Two in-lineage conventions for the electric statics:
bare 1/r (2450, the form under every E_static result including the 2542 normalization walk)
and soft-core 1/√(r² + a_ij²) with a_qq = ℏc/264 = 0.747 fm, a_ee = ℏc/553 = 0.357 fm,
a_qe = 0.516 fm (2455 registration). Union rule (2541 §3, inherited): compute both, report the
union with spread.

**(iii) Sign structure under alternating parity.** Alternating parity is coded as the (−1)^k
pattern-charge flip (2450 `build()`, 2455 scaffolds). For this plane pattern a 90° rotation of
the pattern is the identical operation — the 2540 "90° offset" identity. **Verified
numerically: parity-flip and rotated-pattern cross energies agree to 10⁻⁹ MeV.**

Considered and excluded (recorded): the 2455 instantaneous-Coulomb sign convention as a
*statics* functional (unregistered for statics; the prereg names 2450 as the electric
functional); the dance reach set as a pair filter on the statics sum (kinematic targeting, not
energy content); any conditional strong-sector number under an assumed pair set (that is the
invention the prereg forbids — even labeled "illustrative," it would anchor downstream work
toward the fenced gates).

## 2. Banked partial 1 — the electric-sector contribution (union)

E_endbond ≡ E(separated) − E(stacked); rigid planes make the intra-plane terms cancel exactly,
so E_endbond = −E_cross. On the registered 16-CP stack (prereg §2.1 geometry, 2455-coded eCP
diagonal placement per the amendment note; pitch D = 1.15 fm; alternating parity):

| convention | E_endbond^elec | qq | qe | ee |
|---|---|---|---|---|
| bare 1/r | **−4.35 MeV** | −6.18 | +2.07 | −0.25 |
| soft-core | **−2.12 MeV** | −3.56 | +1.66 | −0.22 |

**Union: E_endbond^elec ∈ [−4.4, −2.1] MeV (positive = bound).** The registered electric
statics makes the alternating-parity stack slightly **anti-bound** under both conventions —
the dominant anti-binding term is the four same-corner axial qq pairs (opposite charge under
parity flip = repulsive under the switched-pair like-attract average). This is fully
consistent with 2450's scope note: the cohesion is the strong-sector registry, and that
channel is exactly the Branch-I-blocked one. **The entire bond depth lives in the blocked
channel; the electric partial is a small signed correction to whatever the strong term is.**

## 3. Banked partial 2 — cross-plane pair geometry (for the future strong-sector solve)

qq: r = 1.150 fm ×4 (same-corner axial, r = D — the only qq shell inside the 2455 dance-reach
1.3 fm), 1.626 ×8, 1.992 ×4. qe: 1.249 ×8, 1.917 ×16, 2.407 ×8. ee: 1.150 ×4, 2.170 ×8,
2.845 ×4. (Geometry only; no strong energy computed on any shell — see §1 exclusions.)

## 4. Gates

None fired. Prereg §3 compares only a *frozen depth*; Branch I fired before any freeze. The
fenced numbers ([40, 170], 102, ≈85) were touched nowhere except the input-integrity assertion
that the 2455 registration's contact-depth identity α_s·ℏc/a_qq = 102.0 MeV holds — an
assertion on an input, not a comparison to a result.

## 5. Reopening contract (one registration)

The campaign apparatus is frozen and total: geometry, lattice-sum machinery, the electric
partial, and the union convention all bank. **A registered static strong-sector pairwise
energy form — (a) which pair set (all qq? the axial shell? DP-channel occupancy?), (b) its
duty/prefactor relative to the switched-pair average, (c) its radial form's static
applicability — drops in with zero new decisions**; the strong term adds linearly to the
banked electric partial and the depth freezes immediately, at which point G1→G2→G3 fire in the
pre-registered order. Per PD-006 this is a physics question routed to the founder (the 2545
handover's standing invitation — "founder physical input on ZBW bond statics... would directly
feed term (i)" — is now the single blocking input); a derivation campaign for the form is the
registrable alternative if founder intuition is not available.

## 6. Bookkeeping

79.5% untouched. Downstream 2542 revision patch NOT triggered (fires only on a pin, prereg
§5). Queue unchanged: RODCLOSE-1 kinetic limb and the plane-resident-fraction limb next behind
this blocker's adjudication; δ_E and MW-MODES TC-extension behind those. No dispatch (Branch-I
closure = dated line + forward movement per WORKFLOW-REVIEW-ECONOMY; joins the standing
disclosure package). Next patch: 2547.

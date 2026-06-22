# R2 — Canonical Status (the μ↔ε / Δc-LPI falsifier)

**Patch:** 2010 (21 June 2026) · **Window:** 2000-band · **Work item:** OPEN-COSMO-DM-2 residual R2
**One-line:** R2 went from an open ~6-order falsifier to **REVISE — leading-order CONFIRMed by the panel,
full PASS conditional on two well-defined closure conditions (one of them a real field-theory derivation
that must NOT be faked under circularity pressure).** This is the canonical pickup point for the next window.

---

## The ladder (what each patch did)

| Patch | Move | Result |
|---|---|---|
| 2002 | Z₀ geometric via the harmonic virial mechanism | PASS *conditional on an un-derived single-oscillator cartoon* |
| 2007 | single-response structure (B=∇×P) shown corpus-derived (c06 line 91 / EW-5) | excludes the independent-magnetic-*field* horn; residual = C-vs-K stiffness |
| 2008 | C and K derived from shared Coulomb origin (0739) → both ∝ Q → K/C Q-invariant | K∝C derived *at leading order* |
| 2009 | rebut ChatGPT's elastic-lattice counterexample (its premise — independent springs — fails in the DP Sea); concede surviving residual | residual narrowed to scale-dependent screening + full-action derivation |
| 2010 | record round-2 panel verdict; canonicalize status | (this file) |

## Panel verdicts (default panel; ChatGPT engaged over two rounds)

- **Round 1 (on the 2007 state):** REVISE. Decisive objection = the elastic-lattice counterexample: B=∇×P
  does not imply the magnetic energy inherits the electric *parameter dependence*. Closure condition named:
  *derive whether K∝C is forced or merely assumed.*
- **Round 2 (on the 2008/2009 state):**
  - On *"K∝C forced at leading order by shared Coulomb origin"* → **CONFIRM (leading order)**, conditional
    on (shape f(r) unchanged, characteristic distances no differential SSV dependence, no scale-dependent
    renormalization).
  - On *"Z₀ geometric → A=0 → R2 PASS"* → **REVISE**, for: (1) scale-dependent screening unbounded; (2)
    full lattice-EM action derivation outstanding; (3) the curl-term coefficient not yet derived from the
    field theory.

## The two closure conditions (the entire remaining residual)

1. **Bound the scale-dependent screening.** With C∝Q(d_DP), K∝Q(a), the leak is K/C ~ Q(a)/Q(d_DP). A
   *uniform* SSV rescaling of Q cancels in the ratio; the leak is only the SSV-induced change in the
   *shape* of the running. Structurally `A ~ (α/3π)·ln(a/d_DP)·(shape-sensitivity of the running to the
   potential)`. The first factors are ~10⁻³; the shape-sensitivity is the unbounded piece. **This must be
   bounded < 10⁻⁶, not asserted "plausibly suppressed."** (Honest note: that bound is not yet derived; it
   likely requires the field theory of #2.)
2. **Derive the curl-term coefficient from the full lattice-EM action.** Write `L = ½C P² + ½K(∇×P)²` with
   *both* coefficients derived from the same microscopic c06 action and shown to inherit identical SSV
   dependence. 2008 is a *pair-potential* derivation; ChatGPT's caution applies — **cancellations that hold
   at the pair-potential level can disappear in the field theory**, so this derivation is load-bearing and
   must be done in the action, not assumed. *This is the c06 owed computation (`c06` line 185).*

## Update — Patch 2011: the action attempt, and a deepening

Closure condition #2 was attempted directly (not by tasting). **Result: a negative.** A corpus-grounded
lattice-EM action with the photon taken as the transverse acoustic mode of the DP lattice reproduces
*neither* the 2002/2008 geometric-Z₀ (it gives **Z₀ ∝ Q** — the explicit stiffness does **not** cancel)
*nor* the VSL c-variation (c comes out geometric). The PSR channel (the actual 0738 VSL) moves c but enters
only μ₀ → Z₀ ∝ 1/c → A = −1 → FAIL. Diagnosis: **a DP-lattice acoustic mode is a phonon, not the photon** —
the naive construction mis-identifies the EM emergence, and the pair-potential/virial cancellation does
**not** survive into it (exactly ChatGPT's caution). See `lattice_action/R2-LATTICE-ACTION-ATTEMPT.md`;
verify `lattice_action/scripts/2011_lattice_action_attempt.py`.

**Consequence (honest deepening, not closure):** the 2002/2008 geometric-Z₀ is a *heuristic* the correct
action must reproduce, and a naive action does not — so it is now explicitly **UNCONFIRMED at the action
level**. The residual is relocated and deepened: it is no longer "screening + curl coefficient" but **the
c06 EM-*emergence* mechanism itself** — how a gapless photon (not a phonon) emerges from the DP Sea, which
substrate parameter the VSL varies, and whether that channel enters ε₀ and μ₀ symmetrically. Conditions #1
and #2 above both presuppose this and are not reachable until it exists.

## Honest standing (after 2011)

- **Leading-order proportionality K∝C: CONFIRMed** (panel + derivation). The independent-spring objection
  is retired. *(Unaffected by 2011 — it is a statement about the stiffness ratio.)*
- **Action-level geometric-Z₀ (the actual R2 PASS criterion): UNCONFIRMED** — a naive action does not
  reproduce it; the correct EM-emergence construction is required and not yet available.
- **Full R2 PASS: REVISE**, residual relocated to the EM-emergence construction. Not faked: the emergence
  mechanism is genuinely upstream and is registered as its own work item (**OPEN-SR-9**) for a future window
  with the right microphysics in hand.
- **Falsification standing:** R2 is still not an open clean kill — the leading-order result stands and the
  swirl/independent-field objections are retired — but its *full* PASS is owed to OPEN-SR-9. OPEN-COSMO-DM-2's
  "substantially resolved" headline is unaffected (R2 was always the conditional, not a live tension).

## Next-window target (single, upstream)

**OPEN-SR-9 — the DP-Sea EM-emergence / impedance-geometricity (Z₀) construction.** This is the genuine
prerequisite and subsumes the old conditions #1/#2: derive how a gapless photon emerges from the DP Sea
(not the acoustic mode), identify which parameter the VSL c-variation flows through, and settle whether that
channel enters ε₀ and μ₀ symmetrically (→ Z₀ geometric, A=0, R2 PASS) or asymmetrically (→ FAIL). Only with
that in hand are the screening bound and the round-3 panel review reachable. Scoping: `mu_eps_closure/OPEN-SR-9_em_emergence_scope.md`.

NO THEO (status update + residual relocation; no new axiom/term/counted prediction).

## Update — Patches 2016/2017: the founder's mechanism + the gate closing → R2 PASS (locked to VSL)

The 2011 block was lifted by the founder's physical mechanism (DP centers pinned to GPs; the field is the
internal pole-displacement wave, E=radial / B=tangential, one Coulomb binding — not the acoustic mode 2011
mis-used). **2016:** the single-DP computation gives geometric Z₀ (PASS) + varying c (VSL), forced by the
fixed Absolute Moment (counterfactual confirms), **conditional on the μ₀-emergence scheme.** **2017:** that
gate is **PROPOSED to close in favour of PASS** (argument under round-3 review), derived from c06 — VSL-consistency excludes the kinetic FAIL scheme,
and the c06 reconstruction mechanism + line 91 force the compliance scheme μ₀∝1/C. **Lock:** R2 is not an
independent falsifier; its FAIL scheme is the one that also kills VSL, so **R2 PASSES iff VSL holds**.
R2 ladder end-state: **proposed PASS, conditional on CPP's standing VSL commitment AND on round-3 panel review of the lock**; residual depth = a rigor
upgrade (derive μ₀ from the DI-bit reconstruction dynamics, SF-6 content) + round-3 panel review. See
`em_emergence/Z0-PARTITION-RESULT.md` (2016) and `em_emergence/MU0-EMERGENCE-SCHEME.md` (2017).

## Update — Patch 2021: PASS RETRACTED; R2 OPEN, leaning FAIL
The Q3 rigor upgrade collapses R2 to Z₀=C/c (analogy-free, from solid ε₀∝1/C). PASS ⟺ c∝C exactly. Every
grounded c(C) — the corpus's c∝√C (0740) and the fixed-ω₀ mechanical c=const — makes Z₀ carry C ⇒ FAIL ~6
orders. The c∝C behind the 2016/2017 PASS was circular (derived from μ₀∝α_B). **R2 ladder end-state:
RETRACTED to OPEN, leaning FAIL**; revives to PASS only if c∝C is independently/self-consistently grounded.
See `em_emergence/Q3-Q2-HONEST-RESULT.md`.

## Update — Patch 2024: FAIL was insecure (phonon≠photon); R2 REOPENED to OPEN
The 2021 FAIL used c∝√C = the DP-lattice **phonon** (acoustic) speed √(C/m)·a. But c06 says the **photon**
advances PSR/Moment (the **budget** speed) and Patch 2011 established photon≠phonon — so 2021 plugged the
phonon speed into the photon's impedance Z₀=C/c. The photon speed's C-dependence is set by the (unspecified)
ΔSSV↔C relation, NOT √C. **R2 ladder end-state: OPEN** (not "leaning FAIL"). The unified-budget principle
(c06 photon=budget + SR-1 matter=budget ⇒ light & matter co-scale ⇒ α fixed while c varies) is the route to
PASS, grounded but not yet derived (owes the ΔSSV↔C relation + ε₀ co-scaling). See
`velocity_ssv_time_dilation/MISSING-MACHINERY-FOUND.md`.

## Update — Patch 2025: R2 PASS, conditional on VTD-1 + medium-universality
The photon speed (not phonon) is FORCED ∝ C by Lorentz invariance: α=e²/(4πε₀ℏc_photon), ε₀∝1/C, ℏ invariant
⇒ α∝C/c_photon=Z₀; for a moving atom α is a Lorentz scalar ⇒ c_photon∝C (velocity, forced, not circular).
Medium-universality transfers this to gravity ⇒ Z₀=C/c_photon=const ⇒ **R2 PASS**. **R2 ladder end-state:
PASS conditional on (i) VTD-1 (exact Lorentz, Patch 2024) + (ii) medium-universality** (c_photon a
source-independent function of local C — the panel target). Velocity-frame α is settled outright; the
gravitational LPI falsifier is PASS-conditional. Photon(∝C)/phonon(∝√C) distinction now derived. See
`em_emergence/R2-RESOLUTION-VIA-LORENTZ.md`.

## Update — Patch 2027: panel REVISE; universality sharpened to c_photon = f(C,Σ)
ChatGPT: dispatch CONFIRM, claim **REVISE** — medium-universality is the load-bearing residual; strongest
break is c_photon = f(C,Σ) (strain-tensor / anisotropy dependence), since velocity strain is anisotropic and
gravity isotropic ⇒ possibly different c_photon at equal local C. Accepted. Sharpened against ourselves: a
photon's E,B are transverse ⇒ c_photon depends on the medium's *transverse* response ⇒ generically a function
of the strain tensor (birefringence) ⇒ universality is non-trivial and possibly false; engaging the attack
*lowered* confidence. Q2: c_photon∝C is unique given ε₀∝1/C (not an independent hole). Q3: VTD-1 is the
weakest input (itself conditional). **R2 ladder: PASS conditional on (i) VTD-1 + (ii) medium-universality —
REVISE, NOT closed.** Next target: compute the anisotropic optical response of the strained DP Sea (c_photon
vs the local stiffness tensor); does isotropic gravity coincide with anisotropic velocity at equal local C?
See `em_emergence/R2-PANEL-REVISE-universality.md`.

## Update — Patch 2028: universality GROUNDED (scalar SSV_abs channel); PASS conditional on VTD-1 alone
ChatGPT's f(C,Σ) birefringence attack is dissolved, not merely answered: c_photon is set by the **scalar**
SSV_abs (pcd_boost_law l.15/18: SSV_abs magnitude sets PSR/time-rate; c07 g_tt = 1−k|SSV|_abs scalar), while
tensor anisotropy enters only through the **gradient** g_ij = δ_ij + k|∇SSV_net|_ij — a separate channel
(lensing/tidal). In a uniformly-affected region (no SSV gradient) g_ij=δ_ij ⇒ c²~g_tt scalar ⇒ isotropic ⇒
no birefringence. H₄/Schur (SR-1 l.52/121) forces the base optical response ∝δ_ij. The directional
"separation along motion" (SR-1 l.31) is the geometric/contraction channel, distinct from the scalar
c_photon channel — so the apparent conflict reconciles. **R2 ladder: PASS conditional on VTD-1 alone**
(medium-universality upgraded from unproven assumption → corpus-grounded structural feature). Residuals:
"locally uniform" is leading-order (gradient/tidal = separate geometric channel); the "uniformly affected"
premise is the load-bearing physical input; VTD-1 stands. Re-dispatch recommended. See
`em_emergence/UNIVERSALITY-GROUNDED-SCALAR-SSV.md`.

## Update — Patch 2029: panel REVISE; locality residual quantified (~11 orders); label corrected
ChatGPT: CONFIRM the 2028 advance (channel split answers birefringence nontrivially), REVISE the claim.
Accepted all three points: (1) grounded≠established (the "uniformly affected" premise is interpretation, not
calculation); (2) the attack shifts anisotropy→**locality** (c²~g_tt/g_ij — is local α insensitive to the
spatial sector beyond leading order?); (3) Schur is the weakest support (unperturbed≠perturbed isotropy;
supports 1+2 carry the argument). **Label corrected: PASS conditional on VTD-1 + scalar-channel isolation
beyond leading order** (NOT "VTD-1 alone" — the universality assumption was replaced by a narrower one, not
removed). Locality residual QUANTIFIED: in a uniform region g_ij=δ_ij exactly (c07), so the only breaking is
the gradient, suppressed by L_atom/L_grad ≈ 1.6×10⁻¹⁷ for terrestrial LPI — ~11 orders below the bound (1e-6).
Caveats: order-of-magnitude estimate; relies on c07 static-metric completeness (1110 audit flagged c07's
metric is limited for GW *radiation*). **R2 ladder: PASS conditional on (i) VTD-1 + (ii) scalar-channel
isolation (~11 orders supported, modulo c07 static completeness).** Residual now precise/twofold: c07 static
completeness + VTD-1 quadrature. See `em_emergence/R2-PANEL-REVISE-locality.md`.

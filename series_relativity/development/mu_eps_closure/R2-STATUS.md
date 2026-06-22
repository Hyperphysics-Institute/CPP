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
gate is **closed in favour of PASS**, derived from c06 — VSL-consistency excludes the kinetic FAIL scheme,
and the c06 reconstruction mechanism + line 91 force the compliance scheme μ₀∝1/C. **Lock:** R2 is not an
independent falsifier; its FAIL scheme is the one that also kills VSL, so **R2 PASSES iff VSL holds**.
R2 ladder end-state: **PASS, conditional on CPP's standing VSL commitment**; residual depth = a rigor
upgrade (derive μ₀ from the DI-bit reconstruction dynamics, SF-6 content) + round-3 panel review. See
`em_emergence/Z0-PARTITION-RESULT.md` (2016) and `em_emergence/MU0-EMERGENCE-SCHEME.md` (2017).

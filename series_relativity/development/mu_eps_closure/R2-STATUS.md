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

## Honest standing

- **Leading-order proportionality K∝C: CONFIRMed** (panel + derivation). The independent-spring objection
  is retired.
- **Full R2 PASS: REVISE** — owed conditions #1 and #2 above. Not faked here: condition #2 is precisely the
  place a self-built lattice model would cancel C by construction, so it is deferred to a future window with
  the actual c06 lattice-EM action in hand, not attempted under circularity pressure.
- **Falsification standing:** R2 is no longer an open clean kill. It is a conditional PASS with leading-order
  panel confirmation and a residual reduced to two well-defined, physics-grade conditions. OPEN-COSMO-DM-2's
  "substantially resolved" headline is unaffected (R2 was always the conditional, not a live tension).

## Next-window targets (in order)

1. The c06 full lattice-EM action: derive μ₀(C), ε₀(C) and the curl coefficient from one action (closure #2).
2. With the action in hand, bound the scale-dependent screening correction (closure #1).
3. Round-3 panel re-review once #2 exists.

NO THEO (status canonicalization + panel-verdict record; no new axiom/term/counted prediction).

# R3 — Can A_s Be Derived From the ZBW Fluctuation Normalization?

**Patch:** 2003 (21 June 2026) · **Window:** 2000-band · **Work item:** OPEN-COSMO-DM-2 residual R3
(the EU-1 amplitude A_s — adopted, not derived)
**Status of result:** **A_s is NOT derivable from the tilt mechanism, and the naive ZBW-stack-Poisson
normalization is decisively EXCLUDED. The result is honest and structural: the same κ-invariance that
makes n_s a clean zero-parameter prediction is exactly why A_s is undetermined. CPP is at PARITY with
standard inflation on A_s (both leave the energy scale free), not deficit.**
**Verify:** `scripts/2003_as_normalization.py`
**Discipline:** worker patch; owned greenfield path
`series_phenomena/cosmology/early_universe/as_amplitude_closure/`; no shared-registry / EU-1 edit here.

---

## 1. The question

EU-1 derives the scalar tilt `n_s = 1 − 2/N_*` (PRED-C-96) but **adopts** the amplitude
`A_s ≈ 2.1×10⁻⁹` (= the Planck best-fit). R3 asks: can the ZBW fluctuation normalization *derive* A_s,
converting it from adopted to predicted — a win standard inflation does not have (there A_s is set by the
inflaton potential normalization, a free parameter)?

## 2. The naive ZBW-stack-Poisson reading is decisively excluded

The obvious "ZBW fluctuation normalization" is stack shot noise: `ζ = δN = (1/3)δ(ln n̄)` with Poisson
occupancy fluctuations `δn̄/n̄ ~ 1/√n̄`. At the pivot, `N_rem = (1/3)ln n̄ = 57` ⇒ `n̄ ~ e¹⁷¹ ~ 10⁷⁴`,
so `A_s ~ (1/9)/n̄ ~ 10⁻⁷⁵` — **off by ~67 orders of magnitude**. Worse, Poisson noise is **white**, not
scale-invariant, so it has the wrong *shape* as well as the wrong amplitude.

This is not a failure of EU-1; it is a confirmation of EU-1's own structure. The curvature perturbation
is **not** stack shot noise — it is the **collective boost-field mode** (`P_ζ ∝ H_eff²`, exactly what the
paper uses). The "ZBW fluctuation" that sets A_s is the amplitude of the *collective* H_eff mode, not
`1/√(CP count)`. So the question "derive A_s from the ZBW fluctuation normalization" answered in the
shot-noise sense is a clean **NO** — and that negative is informative: it pins the amplitude to the
collective mode.

## 3. Why A_s is undetermined while n_s is clean — the κ-cancellation (the core result)

From the EU-1 chain (Patch 0751, Step 4): the boost field is

> `H_eff = κ·[μ(n̄) − μ(1)] = κ·kT·ln n̄  ∝  N_rem`,

with κ the boost coupling (chemical-potential → expansion-rate) and kT the bath temperature. The tilt is
a **logarithmic derivative**:

> `n_s − 1 = 2 d ln H_eff/dN = 2 d ln(ln n̄)/dN = −2/N_rem`,

which **cancels the κ·kT prefactor** — verified in the 0751 script as n_s being invariant across κ, kT,
z₁, and the offset over many decades. That cancellation is precisely what makes n_s a robust
zero-parameter prediction.

The amplitude is **not** a log-derivative: `A_s = P_ζ ∝ H_eff² ∝ (κ·kT)²·(ln n̄)²`. The `(κ·kT)²`
prefactor **survives**. So:

> **n_s is κ-invariant (hence clean); A_s ∝ (κ·kT)² (hence undetermined).** The very structure that
> protects the tilt leaves the amplitude carrying the one coefficient — κ — that the tilt throws away.

This is the honest, structural reason A_s cannot piggyback on the n_s derivation: they depend on
*orthogonal* pieces of H_eff (its log-slope vs its absolute scale).

## 4. What A_s reduces to

Matching the observed A_s fixes the absolute boost-field scale. In the single-field calibration
(`A_s = H_*²/(8π²ε)`, ε = 1/(2N_*)), `H_* ≈ 3.8×10⁻⁵ M_pl ≈ 9×10¹³ GeV` — a sub-Planckian, GUT-scale
boost field, the standard inflationary energy scale. Equivalently, in CPP's own variables, the boost
coupling `κ* ~ 2×10⁻⁷` (with kT ~ E_Pl per LEMMA-NS-BATH). The exact A_s↔H_* relation depends on the
mode structure (single-field vs spectator), but the *order* — sub-Planckian, small κ — is robust.

**So: deriving A_s ≡ deriving κ** (the chemical-potential→expansion-rate boost coupling), equivalently
the absolute boost-field scale H_* at horizon crossing. CPP has not derived κ; it is bounded (κ ≪ 1,
sub-Planckian H_*) but not pinned. This is the same input standard inflation leaves free (the inflaton
energy scale). **CPP is at parity, not deficit.**

The genuinely interesting upside: κ is a *substrate* coupling (how strongly the stack's dispersal drive
boosts PSR_base). If a future substrate computation yields `κ* ~ 2×10⁻⁷` from first principles, A_s
becomes a **prediction** — a win beyond inflation. That is the live open target, and it is now sharply
posed: not "derive A_s" but "derive the single number κ, the boost coupling."

## 5. Honest verdict (R3)

- **A_s is NOT derived; it stays adopted.** Parity with standard inflation. The naive ZBW-stack-Poisson
  normalization is excluded by ~65 orders and by spectral shape.
- **The residual is sharply reduced to one number:** the boost coupling κ (≡ H_* ≡ the absolute
  boost-field scale). n_s's κ-invariance is the structural reason A_s is orthogonal to the tilt.
- **This does not threaten OPEN-COSMO-DM-2 or PRED-C-96.** A_s being adopted was already the R3 caveat;
  this patch grounds *why* (κ-orthogonality) and excludes the wrong route (Poisson), rather than
  finding a new tension. The P(k) closure (2001) already used A_s adopted with this exact honesty.

## 6. Adjacent open item surfaced — and an honest correction

While estimating H_*, the single-field relation `r = 16ε` would give a tensor ratio `r ≈ 0.14`, above the
current bound `r < 0.036`. **This is NOT a clean tension for EU-1**, because EU-1 is a *spectator-style*
mechanism (`P_ζ ∝ H_eff²`, "spectator P~H² vs single-field 1/ε" per the paper), for which r is
*decoupled* from ε and generically *smaller*; `r = 16ε` does not apply. EU-1's tensor-to-scalar ratio is
an **undetermined separate CPP quantity** (it needs the H_inf-vs-spectator-scale ratio), flagged here as
an owed tensor-sector computation — not a live falsifier. I record it explicitly so the single-field
number is not mistaken for an EU-1 prediction.

## 7. OPEN-COSMO-DM-2 residual ledger (post-2003)

- R1 (P(k) deliverable): DONE (2001).
- R2 (VSL μ↔ε falsifier): PASS-conditional on the single-oscillator structure (2002).
- **R3 (A_s): characterized — adopted, parity with inflation; reduced to deriving the boost coupling κ;
  Poisson route excluded (2003). Not a tension.**
- R4 (OPEN-EU-1 depth): unchanged.
- New owed (low priority, flagged): the EU-1 tensor ratio r computation (spectator-sector).

## 8. Proposed registry note — FOR THE INTEGRATOR'S BATCHED PATCH (not edited here)

> **`predictions.md` PRED-C-96 / `frontier_sectors` OPEN-EU-1:** add a note that A_s is adopted because
> it carries the boost-coupling prefactor `(κ·kT)²` that n_s's log-derivative cancels (κ-orthogonality,
> Patch 2003); the shot-noise normalization is excluded (~65 orders + white shape); deriving A_s reduces
> to deriving κ (H_* ~ GUT scale). Optionally register a low-priority owed item for the EU-1 tensor
> ratio r (spectator-sector; `r=16ε` does not apply).

NO THEO (structural characterization + exclusion of the Poisson route; no new axiom/term/counted
prediction; A_s remains adopted).

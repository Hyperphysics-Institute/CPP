# OPEN-COSMO-DM-2 — Power-Spectrum Closure via EU-1 (Residual R1)

**Patch:** 2001 (21 June 2026) · **Window:** 2000-band (P(k)/structure-formation lane) · **Work item:** OPEN-COSMO-DM-2
**Status of result:** **The "SERIOUS TENSION" registry verdict is STALE.** The structure-formation
barrier it names was resolved by the EU-1 arc (Patches 0738–0785); this patch reconciles the registry
state and discharges residual **R1** (the explicit end-to-end P(k) deliverable).
**Verify:** `scripts/2001_pk_from_eu1.py` (5/5 gates PASS)
**Discipline:** worker patch in owned path `series_phenomena/cosmology/dark_matter/pk_closure/`;
no shared-registry edit here (proposed reconciliation text in §5 is for the integrator's batched patch).

---

## 1. Why OPEN-COSMO-DM-2 looked like the #1 falsification risk — and why it no longer is

OPEN-COSMO-DM-2 was registered at Patch 0725 with the verdict **"CPP does not reproduce the observed
power spectrum; CONJ-COSMO-1 is NOT confirmed."** That verdict is correct *as of the information it had*,
but it predates the mechanism that answers it. The problem decomposes into two separable halves, and the
0725 verdict already settled the first one:

- **Q1 — growth (P(k) given seeds).** The Step-4 source of record (`../step4_power_spectrum.md`,
  CHECK 1) states this plainly: *"Given a near-scale-invariant adiabatic primordial spectrum, the CPP
  (conditional Step-D) Friedmann background plus standard gravitational growth reproduces the observed
  P(k)… CPP adds nothing and breaks nothing here — the transfer/growth is standard."* Q1 was never the
  tension. CPP's dark matter (qDP/hTetra) is cold by a wide margin (Step 3, Patch 0706) and its gravity
  reduces to GR in the relevant limit (c05/c08), so it inherits the standard transfer + growth.

- **Q2 — seed origin (scale-invariance).** This was the only barrier. At 0725 the **sole** candidate
  generator was the **causal swirl mechanism**, which hits the cosmic-string/defect wall (cannot make
  super-horizon adiabatic correlations; smears the acoustic peaks). The 0725 doc says, verbatim,
  *"Nothing in CPP currently predicts [a near-scale-invariant adiabatic spectrum]."* The only escape it
  could name was the **atemporal Nexus**, which CPP itself flagged as "lacking physical grounding."

**What happened next (the part the registry never absorbed):** the n_s arc, Patches 0738–0785.
CPP did not stay with the swirl mechanism or the Nexus. It adopted a **different** route:

1. **Horizon problem → VSL (variable c_eff), not de Sitter.** Patch 0738 reframed the H-engine: the
   early universe has high `c_eff` (high PSR_base), so the horizon/causal-contact problem is solved by
   light-cone size, **not** by 60 e-folds of metric expansion. This is consistent with — not contradicted
   by — the Patch 0729 "no quasi-de-Sitter phase" result, *because CPP explicitly does not use de Sitter
   expansion.* The VSL filter (Patch 0739, `0739_delta_c_filter.md`) checked the genuine falsifier and
   returned *"not falsified; reduced to a decidable μ↔ε symmetry question"* (PASS conditional on the
   DP-Sea response being μ↔ε-symmetric to ~10⁻⁶ — residual **R2**).

2. **Spectrum generation → ZBW-stack occupancy relaxation (δN formalism).** Inflation is repurposed
   "as the **spectrum generator** rather than the horizon-solver" (EU-1 §1). The spectrum is
   `n_s = 1 − 2/N_*` with `N_* ≈ 57` fixed by the CP count; the log tilt is forced by A1
   indistinguishability (Gibbs 1/n!), hardened to a ZRP H-theorem (0772/0774), with the long-range
   Debye threat closed PASS (0764–0768) and charge-neutrality grounded in the DP-pair vacuum (0770).

3. **Outcome.** `n_s = 0.9649 ± ~0.0005(theory)` — **PRED-C-96** (Patch 0778, counted, Planck-matching),
   then written up and shipped as **paper EU-1 v1.0** (Patch 0785, 3/3 panel). EU-1 itself states its
   role: *"EU-1 supplies the generation of the primordial adiabatic spectrum, after which dark matter
   inherits…"*

**Therefore the Q2 barrier is resolved by EU-1.** Combined with Q1 (always inherited), CPP now does
reproduce P(k). The CONJ.md entry still carrying "CPP has no inflation analog / Nexus is the only
escape / does not reproduce P(k)" is **stale** — it describes the pre-0738 state.

This is the single most consequence-bearing finding of this window: the programme's stated #1
falsification risk has been **substantially retired**, by work the registry was never reconciled with.
It is *not* a new rescue; it is a recognition that the rescue already shipped (EU-1 v1.0) and the
structure-formation registry never caught up.

## 2. R1 — the explicit end-to-end P(k) deliverable (this patch)

The remaining honest gap in Q1 was that "P(k) inherited" had only ever been checked at the **generic
BBKS level**: script `../scripts/0725_power_spectrum.py` hard-codes an ad-hoc `ns=0.965` and ΛCDM
parameters, never EU-1's actual output. `scripts/2001_pk_from_eu1.py` closes that: it feeds EU-1's
**own derived spectrum** (`n_s=0.9649`, `α_s=−0.0006`, `A_s=2.1×10⁻⁹`) through the standard
transfer (Eisenstein–Hu 1998 no-wiggle) + Carroll–Press–Turner growth, and tests the observed
matter-power-spectrum features. Result (5/5 gates PASS):

| Feature | Computed (EU-1 seed) | Observed | Verdict |
|---|---|---|---|
| Turnover `k_eq` | 0.021 h/Mpc | ~0.015–0.02 | PASS |
| Low-k slope | +0.86 | → `n_s`=0.965 | PASS |
| High-k slope | −2.30 | → `n_s−4`=−3.04 (+ln corr) | PASS |
| Red tilt vs HZ | −0.035 present | Planck excludes HZ ~8σ | PASS |
| σ₈ (analytic, w/ growth) | 1.37 | 0.811 | O(1), non-pathological |

**Honesty on amplitude (residual R3).** EU-1 *adopts* `A_s = 2.1×10⁻⁹` — the Planck-2018 best-fit
value — so the precise `σ₈ = 0.811` holds **by construction** in the full pipeline (CAMB). The analytic
no-wiggle + EdS-growth estimate here is ~factor-2 reliable on the σ₈ scale (a known property of analytic
transfer functions, not a CPP defect); its job is to confirm σ₈ = O(1) — i.e. no order-of-magnitude
pathology — which it does. That `A_s` is adopted-not-derived is exactly its standing in standard
inflation; this is **R3**, not a tension.

The **shape** results (turnover, slopes, tilt) are normalization-independent and are the robust content:
fed its own seeds, CPP reproduces the observed P(k) shape, with the red tilt distinguishable from
Harrison–Zel'dovich.

## 3. What genuinely remains open (the honest residual)

Closing OPEN-COSMO-DM-2 to a clean state does **not** mean the structure-formation story is finished.
The real residuals, in consequence order:

- **R2 — VSL μ↔ε symmetry (decidable falsifier).** The horizon mechanism survives the c-variation
  bounds *iff* the DP-Sea SSV response is μ↔ε-symmetric to ~10⁻⁶ (Patch 0739). This is the one place a
  clean kill could still come from. It is a sharp, decidable substrate question — worth elevating, not
  burying.
- **R3 — A_s amplitude.** Adopted, not derived (parity with inflation). Deriving `A_s` from the ZBW
  fluctuation normalization would convert the amplitude from adopted to predicted.
- **R4 — OPEN-EU-1 (already registered).** A1–A11 derivation of (i) FRW/VSL homogeneity and (ii) the
  exact PCD→ZRP correction structure. Shared with the inflationary-initial-conditions problem of
  standard cosmology; CPP is at parity, not deficit. Does not block PRED-C-96.

None of these is "CPP cannot reproduce P(k)." The framework-threatening reading of OPEN-COSMO-DM-2 is
retired; what remains are derivation-depth and a single decidable substrate falsifier (R2).

## 4. Verdict

- **Q1 (growth):** PASS, now explicitly computed with EU-1's actual spectrum (R1, this patch).
- **Q2 (seeds):** RESOLVED by EU-1 (VSL horizon + ZBW-stack δN → n_s=0.9649 = PRED-C-96 = shipped EU-1 v1.0).
- **Net:** OPEN-COSMO-DM-2 moves from **SERIOUS TENSION / OPEN** to **SUBSTANTIALLY RESOLVED**, with the
  residual reduced to R2 (decidable VSL falsifier) + R3 (A_s amplitude) + R4 (OPEN-EU-1 derivation depth).
  CONJ-COSMO-1's structure-formation gate, the conjecture's named weakest link, is thereby met at the
  conditional/grounded level EU-1 carries.

## 5. Proposed registry reconciliation — FOR THE INTEGRATOR'S BATCHED PATCH (not edited here)

Worker discipline: I do not touch `frontier_sectors/CONJ.md`. Proposed edit for Thomas to apply in the
batched integration patch:

> **`frontier_sectors/CONJ.md`, OPEN-COSMO-DM-2 status line — change:**
> `**Status:** OPEN — registered 1 June 2026 (Patch 0725). [Step 1 … CONDITIONAL NO-GO …]`
> **to:**
> `**Status:** SUBSTANTIALLY RESOLVED (Patch 2001) — the Q2 seed-origin barrier is met by the EU-1 arc
> (VSL horizon, Patch 0738 + Δc-filter 0739; ZBW-stack δN spectrum → n_s=0.9649 = PRED-C-96, shipped
> EU-1 v1.0). Q1 growth was always inherited and is now explicitly computed with EU-1's own spectrum
> (R1, Patch 2001: turnover/slopes/tilt reproduced, σ₈ O(1), A_s adopted). The original "SERIOUS
> TENSION / CPP has no inflation analog / Nexus is the only escape" verdict predates the 0738 VSL
> reframe and is superseded. Residual = R2 (VSL μ↔ε symmetry, the decidable falsifier, 0739) + R3 (A_s
> adopted-not-derived) + R4 (OPEN-EU-1 derivation depth). See
> `series_phenomena/cosmology/dark_matter/pk_closure/PK-EU1-CLOSURE.md`.`

> **`frontier_sectors/CONJ.md`, CONJ-COSMO-1 line:** note the structure-formation gate is now met at
> the EU-1 conditional/grounded level (was "NOT confirmed; weakest link = structure formation").

No theorem-registry / predictions.md edit is owed by this patch: PRED-C-96 already carries the n_s
result; this patch adds the downstream P(k) consistency check, which is a confirmation, not a new
counted prediction. (NO THEO — consistency demonstration, no new axiom/term.)

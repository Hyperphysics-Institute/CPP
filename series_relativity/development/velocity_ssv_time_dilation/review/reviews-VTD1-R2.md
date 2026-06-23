# Review Aggregation — VTD-1 + R2-via-Lorentz (package v1.0, Patch 2039)

**Patch:** 2040 (22 June 2026) · **Window:** 2000-band · **Panel:** ChatGPT, Grok, Gemini, Copilot (4/4 in).
**Outcome:** P1 SOUND (unanimous, at SR-1 strength). **P2 verdict-move: conditional-PASS → REVISE** (3 of 4
explicit; 4th concurs universality is assumed-not-derived). The residual is sharpened and the cheapest
falsifier is named — and it is unanimous.

---

## 1. Verdicts as returned

| Reviewer | P1 (VTD-1) | P2 (R2-via-Lorentz) | Universality (ii) |
|---|---|---|---|
| ChatGPT | SOUND (SR-1 strength) | **MIS-STATED-STRENGTH** | partly motivated, **not derived** |
| Grok | SOUND | SOUND *as explicitly conditional* | **must be assumed** at present |
| Gemini | SOUND (SR-1 strength) | **MIS-STATED-STRENGTH → REVISE** | **assumed**, not derived |
| Copilot | SOUND (SR-1 strength) | **MIS-STATED-STRENGTH → REVISE** | **assumed**, load-bearing |

**Aggregate:** P1 SOUND ×4. P2 → **REVISE** — the "conditional-PASS" label is not supported; even Grok's
"SOUND as conditional" is gated on universality being assumed, so the headline strength is REVISE, not PASS.
**Not UNSOUND:** no reviewer says the argument is broken; they say its *stated strength overstates how settled
the load-bearing assumption is.*

## 2. Where all four agree (the signal)

1. **P1 is sound at SR-1 strength.** The linear reading is fairly excluded (wrong γ); f_eff = 1 − 1/γ is the
   mathematically unique consumed fraction; the literal-vs-effective carve-out is honest and non-gating.
   ChatGPT's note that the exclusion "borders on tautological" is correct *and is the point*: it is an
   empirical-constraint application, not a derivation — which is exactly what "at SR-1 strength" claims.
2. **R2 does NOT need literal VTD** (§4.3): the effective γ(v) + α-Lorentz-invariance suffice for the
   impedance argument. **My 2038 carve-out is panel-validated** — the literal orthogonal-allocation mechanism
   is correctly not elevated to a gate.
3. **The package does not overclaim** (4/4). Discipline on "at SR-1 strength," "conditional," and the open
   disclosure of the 2021 FAIL was noted as a strength by every reviewer.
4. **Universality is the load-bearing residual, and it is ASSUMED, not derived.** This is the unanimous core.

## 3. The sharpened objection (what REVISE is *about*)

The panel refined "medium-universality" into a precise, decidable claim. The R2-via-Lorentz route reads
c_photon ∝ C off the **velocity** frame, where the strain is **anisotropic** and α-invariance is Lorentz-
protected; it then **transfers** that law to the **gravity** frame, where the strain is **isotropic** and
there is no such protection. The transfer is valid only if:

> **c_photon depends on the local *scalar* stiffness C alone — c_photon = f(C) — and NOT on the strain
> tensor's anisotropy/tensor structure, c_photon = f(C, Σ_ij).**

Nothing in the package forbids the Σ-dependent form. If c_photon = f(C, Σ_ij) with Σ_vel ≠ Σ_grav at matched
scalar C, the velocity-frame extraction does not fix the gravity-frame value, the §2(b)→§2(c) transfer
fails, and R2 reopens. ChatGPT/Gemini frame the worst case as a **potential category error** (reading a law
off the anisotropic branch and applying it to the isotropic branch); Grok and Copilot frame it identically as
the un-derived insensitivity of c_photon to Σ. **This is one objection, stated four ways.** The "read-off vs
derive" gap (§4.2) is the same point: the Lorentz extraction is legitimate and non-circular, but **the
universality transfer does the majority of the work**, and it is not derived.

## 4. The named next computation — UNANIMOUS cheapest falsifier

All four independently converged on the same test, which is therefore the highest-leverage next move:

> **Set up the DP-lattice / 600-cell substrate; apply two strain fields tuned to identical local *scalar*
> stiffness C — one anisotropic (velocity-like), one isotropic (volumetric/gravity-like) — and compute the
> *photon*-mode propagation speed (equivalently ε₀ or Z₀) in each. If c_photon differs at fixed C, medium-
> universality is FALSE, the transfer dies, and P2 is UNSOUND. If it is equal across Σ at fixed C,
> universality is substantially grounded and R2-via-Lorentz strengthens toward PASS.**

**Anti-faking hazard (carried from OPEN-SR-9 scope, and the reason this is load-bearing):** a self-built
lattice-EM action can cancel C — or hide a Σ-dependence — *by construction*. The test is only decisive if
(a) the photon mode is tracked, **not** the phonon/acoustic mode (the 2021 category error), and (b) the
action is corpus-grounded (c06 EM-emergence), not reverse-engineered to give universality. **This test IS the
core of OPEN-SR-9** — it is not a lighter-weight side check; doing it honestly is doing OPEN-SR-9.

## 5. Verdict-move recorded

- **P1 / VTD-1: SOUND at SR-1 strength** — confirmed by the panel; no change to the 2037/2038 standing.
- **P2 / R2-via-Lorentz: conditional-PASS → REVISE.** The Lorentz route is *not* a PASS until universality is
  settled. R2's live status: **REVISE**, residual = c_photon = f(C) vs f(C, Σ_ij), to be settled by the §4
  test (= OPEN-SR-9). The 2021-FAIL is *not* reinstated — the route is sound *modulo* a single, now-precise,
  testable assumption.
- **OPEN-SR-9** absorbs the sharpened objective: not merely "derive EM-emergence / geometric Z₀," but
  specifically **prove (or compute) that c_photon is Σ-independent at fixed C.**
- **NO THEO.** Nothing registered; this is a frontier verdict-move, owned-greenfield record.

### Proposed for integrator (batched, Tier-A — supersedes the 2037/2038 R2 lines)
- `mu_eps_closure/R2-STATUS.md`: R2 → **REVISE** (was conditional-PASS); residual = Σ-independence of
  c_photon at fixed C; condition (i) VTD-1 cleared at SR-1 strength; condition (ii) is the REVISE driver.
- `frontier_sectors/SR.md` → **OPEN-SR-9**: fold in the Σ-independence objective + the panel's fixed-C/
  varying-Σ photon-speed test as the registered decisive computation (with the anti-faking guard).
- `frontier_sectors/CONJ.md` / OPEN-COSMO-DM-2: R2 is **REVISE, not resolved**; DM-2 headline unaffected (R2
  was always the conditional, never a live tension), but the wording must not imply R2 PASS.
- No `theorem-registry.md` / `predictions.md` edit (conditional; NO THEO).

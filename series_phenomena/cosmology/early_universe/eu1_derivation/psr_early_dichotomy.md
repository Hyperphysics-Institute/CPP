# OPEN-EU-PSR-EARLY-1 worked — and the escape closes. The perceived reading forks, and BOTH branches fail: if the PSR responds to the count, the no-go breaks but the tilt is destroyed (≥4σ everywhere the pivot fits its own window); if the PSR sits at a floor, the tilt survives but the count is still conserved and the no-go stands. **Underneath is a structural conflict independent of any model: PRED-C-96's tilt formula ITSELF requires the conservation that forbids a viable amplitude.** One escape remains and it is specific

**Patch 3837, Session 178, 9 Sep 2026. Lane: EU.** Works OPEN-EU-PSR-EARLY-1 (3816 §4), promoted at 3835 to the amplitude's only identified escape. Verify `scripts/3837_psr_early_dichotomy.py` (8/8). Reasoning `reasoning/3837_psr_early_dichotomy.md`. **λ is NOT minted** (PD-007) — it is the PSR-response coefficient and remains an output owed. PRED-C-96's tilt value untouched; 3710 not retired.

## §1 Two clearings the escape needed (verify T1, T2)

**(a) CONV-045 does not block this.** The perceived reading appeared to contradict a 5–0 ratified statement. It does not. S-HENGINE-HELD settles **held vs acted-on** — the engine reads the D4-conserved stack rather than the D1-clipped displacement — and its own text says the cap "binds only the acted-on displacement and is **silent on n̄**." The held-vs-*perceived* axis was never adjudicated. The escape is open on the record; nobody had checked, and it needed checking before any work was spent on it.

**(b) The ratified PSR law is exponential.** R-PSR-LAW-LOG's series 1 − ε + ε²/2 **is** e^{−ε} to the order stated (agreement to 1.6×10⁻⁴ at ε = 0.1), so

> **PSR/l_P = e^{−ε}**, with ε set by SSV_abs.

That is what the law's own name says, and it makes the feedback below tractable rather than model-dependent in its form.

## §2 The feedback loop and its solution (verify T3)
SSV_abs is count-like (glossary: more DI-bits received ⇒ greater SSV_abs), and the DI-bits received are those within the PSR. So the perceived count and the reach determine each other:

> n̄_perc = n̄_ref · e^{−3ε},  ε = λ n̄_perc

with n̄_ref ≡ ρ·(4π/3)l_P³ the reference (rest-frame Planck sphere) count. Self-consistency gives **logarithmic saturation**:

> **n̄_perc ≈ ln(n̄_ref)/(3λ)**

At n̄_ref = 10⁸⁴ and λ = 1 the perceived crowd is **63**, against a reference crowd of 10⁸⁴. The reach collapses so hard that a point perceives a crowd of order sixty however many CPs are actually there. Since ln n̄_ref = 3N_rem, this reads **n̄_perc ≈ N_rem/λ** — the perceived crowd tracks the *remaining e-folds*, which is a striking relation and the hinge of everything below.

## §3 Branch B1 — the PSR responds: the no-go breaks, the tilt dies (verify T4, T5, T6)
**It does break the no-go.** n̄_perc depends on ε, hence on local state, hence is **not conserved**. The end condition becomes dynamical. That is exactly what 3835 required, and it is the only thing on file that supplies it.

**It costs e-folds.** Ending at perceived n̄ = 1 gives ε_end = λ, so n̄_ref,end = e^{3λ} and

> **N = ⅓ ln n̄_ref − λ.**

The budget was already 10.5 e-folds short (3823); B1 makes it worse, monotonically.

**And it destroys the tilt.** This is decisive. With H_eff ∝ ln n̄_perc ≈ ln(N_rem/λ), the driver acquires an extra logarithm, so

> n_s − 1 = −2/(N_rem · ln(N_rem/λ))  instead of  −2/N_rem.

Matching the observed n_s requires ln(N_rem/λ) = 1, i.e. **λ = N_rem/e ≈ 21** — but then N_total = 64.5 − 21 = **43.5**, and the pivot N_rem = 57 no longer fits inside its own window. Keeping the pivot inside requires λ ≤ 7.5, and across that entire allowed range:

| λ | n_s | deviation | window |
|---|---|---|---|
| 0.1 | 0.9945 | 7.0σ | pivot inside |
| 1.0 | 0.9913 | 6.3σ | pivot inside |
| 3.0 | 0.9881 | 5.5σ | pivot inside |
| 7.5 | 0.9827 | 4.2σ | pivot at the edge |
| 21 | 0.9649 ✓ | 0.0σ | **pivot outside** |

> **B1 is excluded.** There is no λ that keeps both the tilt and the pivot. The best available inside the window is 4.2σ.

## §4 Branch B2 — the PSR floors: the tilt survives, the no-go stands (verify T7)
If ε instead **saturates** at the D1 cap — the "PSR floor" language of 3816 §4 — then ε → ε_max, a constant, and

> n̄_perc = n̄_ref · e^{−3ε_max} ∝ ρ.

The volume factor is constant again, so **n̄_perc is still a conserved density**. ln n̄_perc = 3(N_rem − ε_max) is linear in N_rem, so the tilt survives with the pivot merely shifted — but the 3835 no-go applies verbatim, because conservation is exactly what it turns on. **B2 preserves the tilt at the price of supplying no escape at all.**

## §5 The structural core — why this was never going to work (verify T8)
The dichotomy is not an artifact of writing ε = λ n̄. Underneath it is a statement about PRED-C-96 itself.

The tilt n_s − 1 = −2/N_rem follows from H_eff ∝ ln n̄ only if **ln n̄ is exactly linear in N_rem**. Linearity requires n̄ ∝ ρ with a **constant** volume factor — that is, a conserved count in a fixed reference volume. And 3835 shows that a conserved count is blue.

> **PRED-C-96's tilt formula ITSELF requires the conservation that forbids a viable amplitude.** Any responsiveness that makes n̄ non-conserved — of any functional form, not just this one — bends ln n̄ away from linearity and moves the tilt off its predicted value.

The tilt and the amplitude are not two independent open problems. **The first one causes the second.** That is the honest statement of where EU-1 stands, and it is stronger and more uncomfortable than anything in this arc so far. It is conditional on the engine's form (H_eff ∝ ln n̄, 0749) and on ζ = δN sourced by the count — both of which the corpus holds.

## §6 The one remaining escape, and it is specific
The conflict assumes the *same* quantity drives expansion and carries ζ. Standard inflation does not require that: a **spectator** field can carry ζ while the inflaton drives — and EU-1's own §Amplitude already invokes "the spectator prescription" without supplying a spectator.

The route that survives §5 is therefore:

> **An independent light field, not the count, that modulates the END CONDITION.** The count keeps ln n̄ linear (tilt preserved, PRED-C-96 intact); the spectator supplies a non-conserved δN by shifting when inflation ends. This is structurally the **modulated-reheating** mechanism, where a light spectator modulates the moment of reheating rather than the expansion rate.

**C-4 (the orientational Goldstone, registered 3835 §3) is promoted from "conditional" to "the candidate of record for this route."** A Goldstone is genuinely light, freezes at horizon exit, is Gaussian, and — crucially — is *not* the count, so it does not disturb the tilt. What it owes is now precise and singular: **a coupling by which the sea's orientation shifts the end condition.** Its isocurvature problem is also softened in this role: modulated-end mechanisms produce adiabatic perturbations, because the shift is in *when* everything ends, not in one species' abundance.

## §7 Standing
- **OPEN-EU-PSR-EARLY-1: WORKED, and it does not deliver the escape.** Both branches fail — B1 excluded by the tilt (≥4.2σ within the window), B2 supplies no escape (still conserved). Registered as a closed route, not as an open question.
- **Two clearings established** (§1): CONV-045 is silent on this fork; R-PSR-LAW-LOG is the exponential form.
- **New result: logarithmic saturation** of the perceived count, n̄_perc ≈ N_rem/λ (§2) — of independent interest and reusable.
- **Structural conflict registered** (§5): the tilt's own form demands the conservation that forbids the amplitude. **The strongest statement in this arc; it should go to the panel with the CONV-046 package.**
- **C-4 PROMOTED** to candidate of record for the one surviving route (§6): an independent light spectator modulating the end condition. Owes a coupling to the end condition; not adopted; nothing computed (PD-007).
- **OPEN-EU-AMPLITUDE-1 re-pointed a fourth time:** "what light field, *other than the count*, can shift when inflation ends?"
- **Honest scope:** §3–§4 assume ε ∝ SSV_abs ∝ perceived count, the glossary's count-like reading. §5 does not, and is the load-bearing result.
- Unaffected: PRED-C-96's tilt value (it reads the adopted pivot); the e-fold budget's separate arithmetic (B1 would worsen it); T-1; T-2.

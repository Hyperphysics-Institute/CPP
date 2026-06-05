# Bath-temperature lemma: μ is evaluated w.r.t. the ZBW/substrate bath → long-range corner closed PASS

*Patch 0767, Session 154. Acts on ChatGPT's review of 0766: it confirmed Γ = α/κ, endorsed retiring the
Compton estimate, and asked for one thing — a lemma in the cosmology arc stating that the chemical
potential entering the H_eff ∝ μ tilt chain is evaluated with respect to the **ZBW/substrate bath
temperature, not the macroscopic de Sitter temperature**; "if that is accepted, the long-range corner is
effectively closed on the PASS side." This finding states and grounds that lemma. NO THEO (it rests on the
bath clause, which is itself a working postulate, so the n_s result stays conditional on its always-present
legs).*

## The lemma

**LEMMA-NS-BATH.** The chemical potential μ(n̄) that enters the CPP tilt chain (H_eff ∝ μ; μ = kT ln n̄ +
const; n_s − 1 = −2/N_*) — and therefore any interaction residual μ_excess in it — is evaluated with
respect to the **ZBW/substrate bath** that thermalizes the CP occupations, whose temperature is the
substrate scale kT ~ ℏc/ℓ_P = E_Pl. It is **not** evaluated with respect to the macroscopic de Sitter
(horizon) temperature of the expanding background.

## Why it follows from the existing bath clause (not a new assumption)

The bath clause (0750–0752) is precisely the statement that **the CP occupations are thermalized by the
ZBW substrate dynamics** — the ZBW acts as the exchangeable bath that mixes occupation states and yields
the Gibbs ln n̄ (the log of the tilt). A chemical potential is defined relative to the bath the ensemble
equilibrates with. Since (by the bath clause) the occupation ensemble equilibrates with the ZBW/substrate
dynamics, **μ — and every correction μ_excess to it — is a substrate-level quantity at the ZBW
temperature.** The de Sitter temperature characterizes the horizon/coarse-grained background; it is not the
bath that sets the substrate-level occupation statistics. The Gaussian fluctuation amplitude in this arc is
likewise ZBW-sourced (CLT over ZBW phases, 0738), consistent with the same bath. So LEMMA-NS-BATH is a
**corollary of the bath clause**, not an independent postulate: the bath that sets the log is the same bath
that sets μ_excess, and that bath is the ZBW/substrate one.

## Consequence: the long-range corner is closed PASS (modulo the bath clause)

With kT_bath = kT_ZBW ~ E_Pl (κ ~ 1):

  Γ = α·E_Pl/kT_bath = α/κ ~ α ≈ 7.3×10⁻³  →  |μ_excess|/kT ~ c·α^{3/2} ~ 3.6×10⁻⁴ ≪ ln n̄ ≈ 170.

The minimal requirement for PASS is just κ ≳ 10⁻⁴ (kT_bath ≳ 2×10¹⁵ GeV); the ZBW/substrate bath
(κ ~ 1) clears it by ~4 orders. So the long-range √n̄ residual is negligible, and **the long-range corner
is closed on the PASS side** — conditional only on the bath clause itself (Reading A), which is the same
working postulate the whole n_s result already rests on. There is no longer a *separate* √n̄ worry.

## Status (ChatGPT's calibrated language, adopted)

> **Conditional PASS.** If the n_s-epoch occupation bath is the CPP ZBW/substrate bath, then κ ~ 1,
> Γ ~ α, and the long-range Coulomb residual is negligible. Failure requires reinterpreting the relevant
> bath as a much colder macroscopic temperature (κ ≲ 10⁻⁴), plus no rescue from fixed-GP geometry or
> neutrality. LEMMA-NS-BATH (a corollary of the bath clause) selects the ZBW/substrate bath, so under the
> framework's own thermalization mechanism the corner is closed PASS.

## What this changes in the arc's conditionality

Before: n_s = 0.9649 was conditional on (a) the bath thermalizes, (b) charge neutrality, (c) **no surviving
long-range √n̄**. Leg (c) is now **discharged** by the chain {kernel = Coulomb (0764) → residual is
coupling-bounded c·Γ^{3/2} (0764) → Γ = α/κ from grounded scales (0766) → κ ~ 1 by LEMMA-NS-BATH (0767)}.
The remaining conditionality reduces to the **always-present legs (a) the bath clause and (b) neutrality**
— there is no longer a distinct long-range residual condition. (a) is the working postulate of the whole
arc; (b) is toy-supported (0756) and physically expected.

## Honest scope

- LEMMA-NS-BATH is a **conceptual corollary** of the bath clause, not a hardened theorem; it is registered
  as a finding-level lemma, not in `theorem-registry.md`. Its strength = the bath clause's strength.
- The √n̄-specific corner is closed PASS **given the bath clause**; it does not make the overall n_s
  prediction unconditional — that still rests on the bath clause + neutrality, exactly as before, just
  without the extra √n̄ leg.
- Offered to the panel for the final check (ChatGPT indicated this is the one statement it wanted pinned).
  If the panel accepts LEMMA-NS-BATH, the long-range corner is settled and the arc's open items are the
  bath clause's own confirmation (Ewald Stage A/B; the MC bath toy 0753) and neutrality.

## Panel consensus + endorsed registration language (Patch 0768)

ChatGPT reviewed LEMMA-NS-BATH: **CONFIRM-WITH-CALIBRATION**, endorsing the closure. It confirmed the chain
is coherent — bath clause ⇒ μ defined w.r.t. ZBW/substrate bath ⇒ kT ~ E_Pl ⇒ Γ = α/κ ~ α ⇒
|μ_ex|/kT ~ c·α^{3/2} ≪ ln n̄ — and that the "use the de Sitter temperature" branch is a *different bath
interpretation*, not the one the n_s derivation uses; it "is no longer an internal objection — it is a
rejection/reinterpretation of the bath clause." Calibration: say **PASS conditional on the bath clause**,
not "unconditional PASS." Endorsed registration language (adopted verbatim):

> **LEMMA-NS-BATH closes the long-range Debye residual as an independent threat:** the chemical potential
> entering the tilt chain is defined with respect to the ZBW/substrate bath, so kT ~ E_Pl, Γ ~ α, and the
> Coulomb excess is negligible. The n_s = 0.9649 result remains conditional on the bath clause and a
> charge-neutral effective equation of state, but **no longer on a separate long-range √n̄ residual
> assumption.**

With Grok and Copilot's earlier endorsements of 0756/0757 and the macro-CP bath mechanism, this is full
panel consensus that the long-range √n̄ corner is **closed on the PASS side**. The two legs that remain
(the live conditions): **(1) bath reality** — the CP occupation ensemble actually reaches the
ZBW/substrate Gibbs state quickly enough; **(2) neutrality / effective equation of state** — interactions
introduce no separate non-ideal term beyond the (now bounded, negligible) Coulomb residual.

## Pointers

- Basis: the bath clause (`stack_ensemble_*`, 0750–0752); 0738 (ZBW-sourced Gaussianity); 0766 (Γ = α/κ,
  grounded scales); 0764 (kernel + identity); 0756 (neutrality).
- Numerics: `scripts/0766_ns_epoch_gamma.py` (κ ~ 1 → Γ ~ α → PASS).
- Reasoning: `reasoning/0767_bath_temperature_lemma.md`.

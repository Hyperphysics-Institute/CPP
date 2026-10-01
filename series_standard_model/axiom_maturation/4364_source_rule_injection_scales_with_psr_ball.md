# The Source Rule: Local Invariance Requires a Source's Injection to Scale with the Grid-Point Count of Its Own PSR Ball (p = 3), One Rule for Mass and Charge — and 4360–4361's Second-Order Wall Came from Doing the Proportioning at the Receiver

**Patch:** 4364. **Lane:** foundations, with GR and EW. **Session:** 242.
**Answers:** TODO-4359-SOURCERULE (b), the dilution exponent named first in 4362 §3.
**Verify:** `series_standard_model/code/4364_source_rule_relay_eih_tolman.py` (numpy + sympy; about 30 s).
**Critic:** an independent fresh-context critic checked a draft of this patch; its return is filed verbatim at
`series_standard_model/reviews/2026-10-01_session_242_critic_returns_verbatim.md`. Three of the draft's claims were
overstated, and they are corrected here (§7).

## 0. Result in one paragraph

Write a source's per-Moment injection into the relay as S ∝ R_s^p, where R_s is the PSR where the source sits. The
founder's registered principle that **no laboratory measurement changes between a gravity well and deep space**
(R-ALPHA-LORENTZ-RATIO, founder 4360) holds for a source's own field only if **p = 3**. In words: the source's injection
is in proportion to the number of grid points inside its own PSR sphere. Fixed count (p = 0) gives local G·m ∝ (1+3U),
which is the 4359 critic's result. GR-1j read with a fixed coordinate GM (p = 2, 4359's "∝ R²") gives (1+U). Both fail
lunar laser ranging. GR's 1PN N-body equations (EIH) and Tolman's static source both reproduce p = 3; these are checks,
not derivations, because GR-1j bars positing Einstein. Under A3′'s one rule the same p holds for charge, so k_α = k_G.
4360's mechanism needed k·SSV_abs,0 = 1/3 and ran into Mercury at second order. Both of those come from placing the
proportioning at the **receiver** (against the receiver's SSV_abs). Placed at the **source**, it needs neither
condition. **Standing: a requirement, not yet a mechanism.** Read literally (fixed count, same message), the founder's
wording gives p = 0, so how the PCD cycle realises p = 3 is put to him (§6).

## 1. The relay's Gauss law sits at the source (script part A)

GR-1j's statics (L208–221): u = M_{R(x)}[u] in vacuum (exactly Laplace for any PSR profile), and u − M_R u = s at a source.
Near the source u − M_R u ≈ −(R_s²/6)∇²u, so the far field is u = C/r with **C = (6/4π) S/R_s²**. A radial lattice solve
(shell mean done exactly cell by cell) confirms this. The table gives coefficients relative to the uniform case:

| R_s | R_far | gather, far | R_s⁻² | scatter, far | R_far⁻² | gather, near | scatter, near |
|---|---|---|---|---|---|---|---|
| 1.00 | 1.00 | 1.00000 | 1.00000 | 0.99667 | 1.00000 | 1.00000 | 0.99774 |
| 0.90 | 1.00 | 1.23480 | 1.23457 | 0.99667 | 1.00000 | 1.23559 | 1.23265 |
| 0.80 | 1.00 | 1.56337 | 1.56250 | 0.99667 | 1.00000 | 1.56386 | 1.55983 |
| 1.00 | 1.20 | 0.99979 | 1.00000 | 0.69214 | 0.69444 | 1.00000 | 0.99774 |
| 0.90 | 1.20 | 1.23462 | 1.23457 | 0.69214 | 0.69444 | 1.23559 | 1.23265 |
| 1.00 | 0.85 | 1.00008 | 1.00000 | 1.37947 | 1.38408 | 1.00000 | 0.99775 |

- **Gather** is GR-1j's registered kernel: each GP averages over its own PSR shell. Under gather the far field follows
  the PSR at the source.
- **Scatter** is the corpus's emission picture. In c01 a GP receives "from all GPs whose PSR contains it". The founder's
  payload specification (2026-08-06) says each DI-bit "deposits exactly once, at its origin's PSR shell". Under scatter
  the far field follows the PSR where it is read. The critic found this; I reproduced it here.
- **Near the source, in a region of uniform PSR, both give R_s⁻².** The local test below therefore does not depend on
  the kernel. Across a PSR gradient the two kernels differ, and that bears on GR-1j's own vacuum theorem (§5,
  TODO-4364-KERNEL).

## 2. What local invariance requires (part B)

Take q = PSR/PSR_∞. Rulers and clocks both scale with q (one PSR does both, founder 4362). At n local PSRs from the source,
the census is ∝ S/(R_s² · nR_s), so **it scales as q_s^(p−3)**:

| injection | local G·m (and, by one rule, α) | at Earth, against LLR |
|---|---|---|
| fixed count, p = 0 (4355) | (1 + 3U) | excluded (4359 critic) |
| ∝ R², p = 2 (GR-1j with fixed coordinate GM; 4359) | (1 + U) | excluded |
| ∝ GP count of the PSR ball, p = 3 | invariant | passes |

**One residual (the critic's catch).** Gravity's observable is the lapse. Under the ratified law
q = 1 − ε + ε²/2, the lapse's sensitivity is d ln q/dε = −1 + ε²/2, so at p = 3 the local G carries a factor
(1 − ε₀²/2). That is far below anything LLR can see. For α it applies **only if** the charge reading carries the same
lapse sensitivity. A metric-coupled charge reading (A3′) has no such factor, because the charge census does not set the
lapse. That conclusion is inferred, not shown (§8).

## 3. Checks against GR (parts C and D)

- **EIH (1PN N-body).** Take a test body near source b, in a potential U₀ from distant bodies. GR gives
  |a| = (m_b/r²)[1 − (2β+2γ)U₀ − (2β−1)U₀] = 1 − 5U₀. With CPP's assembled metric (g₀₀ = −q², g_ij = q⁻²δ), a
  slow particle has a = −q⁴∇ln q. The reading supplies 4 (= 2β+2γ) and the source coefficient supplies p − 2:
  1 − (p+2)U₀. So **p = 3**. The departure from GR is 3U₀ for p = 0, U₀ for p = 2 and 0 for p = 3. The critic notes, and
  I accept, that for a uniform U₀ this is §2 restated in coordinates, not an independent test.
- **Tolman.** The exact static equation is D^iD_iN = 4πG N(ρ+3p). On h_ij = q⁻²δ it becomes q³∇²_flat ln q, an
  identity the script checks symbolically. With ρ_prop = q³ρ_lat (bodies shrink with the PSR), it gives
  **∇²_flat ln q = 4πG q ρ_lat** for dust. The injection per unit of source (GR-1j's census excess, L419–425) is
  then R_s² from the relay step times q_s from the lapse, which is ∝ R_s³. GR-1j's ∝ R² is missing exactly the lapse, i.e. Tolman's N. This is a **check only**:
  GR-1j L158–159 bars positing Einstein. Only the R₀₀ component is exact on this metric ansatz (the critic's caveat).

## 4. Why 4360–4361 hit a wall (part E)

Suppose the read field is multiplied by a function of the **receiver's** state, w = q_rec^j. For a single body this
shifts the second-order coefficient: **β_eff = 1 + j/2**. Exact receiver-side invariance needs j = 3, which gives
**β = 5/2**, the same result 4361's critic reached by another route. A factor set by the **source's own** q is a
constant for a single body and is absorbed into its measured GM, so β stays 1 and Mercury's ½ is untouched.

Consequences:
- 4360's condition k·SSV_abs,0 = 1/3 is not needed.
- 4361's choice between "α swings 2–3× the bound" and "Mercury fails" does not arise from the source rule.
- The principle in R-ALPHA-LORENTZ-RATIO stands. Only 4360's placement of it, at the receiver against SSV_abs, is
  replaced.
- A receiver-side weighting also conflicts with A3′'s "geodesics of the unique assembled metric" (critic).

**4360's own estimate was optimistic.** Its swing 9ε·dε used ε = U_sun. GR-1j defines u from the homogeneous Sea, so if
ε is absolute, the Galaxy's ~10⁻⁶ dominates and the receiver-side swing is **~250× the clock bound**. For comparison,
the p = 3 lapse residual ε₀·dε is 0.27× the bound at U_sun and 27× at U_gal. For G it is unobservable either way. For α
it decides nothing until §2's reading is settled (TODO-4364-EPSABS).

## 5. What the critic found that this patch does not resolve

| item | finding | where it goes |
|---|---|---|
| Kernel | GR-1j/T-1 justify the kernel by "AP-4c origin→PSR" but write the receiver's mean (T-1 §2–3). Under the corpus's scatter picture the vacuum is not exactly Laplace across a PSR gradient: D·u, with D ∝ R², is harmonic. That changes the second-order structure on which Mercury's ½ was calibrated. | TODO-4364-KERNEL (GR) |
| Self-gravitating bodies | At p = 3 a body's active mass is Σm_i q_i = m − 2\|E_g\|/c². GR's Tolman mass is m + E_int − \|E_g\|, with the 3p term supplying +\|E_g\| by the virial theorem. GR-1j defers pressure (L410–416), and a trace-sourced scalar carries ρ − 3p (wrong sign for Tolman's +3p). Earth \|E_g\|/mc² ≈ 4.6×10⁻¹⁰ and the Moon 1.9×10⁻¹¹, against LLR's ~10⁻¹³ on Earth–Moon differences. This is an open test the corpus must meet, not passed here. With p fixed at 3 by §2, the gap has to be closed by the pressure/binding term. It is not created by choosing 3 over GR-1j's implied 2: dust gives Σm_i q_i^(p−2) = m − 2(p−2)\|E_g\|, so p = 2 leaves a gap of the same size with the opposite sign. | TODO-4364-SELFGRAV (GR) |
| Preferred frame | The Nexus frame is absolute. A moving source's rule (Lorentz-contracted PSR) is owed against α₁ (~10⁻⁵, LLR) and α₂ (~10⁻⁹, solar spin). | TODO-4364-PREFFRAME (GR/SR) |
| Absolute ε | If ε is absolute, the PSR law's expansion point (Galaxy, Local Group, cosmology) needs stating, and so does whether Mercury's calibration survives. | TODO-4364-EPSABS (GR) |

## 6. The founder's wording, and the question

His 4360 answer (b) was: "each grid point it reaches gets the same push as in deep space, so its total over the sphere
is a little less." 4360 §3 read this as "a source's total injection is fixed". That contradicts his own clause, "its total
over the sphere is a little less". But the critic is right that the literal registered picture gives p = 0: a fixed band
of N DI-bits, each delivering the same message (founder 4361). So p = 3 needs the **magnitude** of a source's
contribution to scale with its PSR ball, while the count and the form of the message stay the same. The receiver cannot
do this, because AP-4's E is one summed vector and the receiver cannot separate a resident CP's part from the relayed
census. Weighting every arrival instead would break the vacuum statics. **The only consistent site is the origin GP**,
which computes its own PSR every Moment.

**Question to the founder (physical picture).** A charge or a mass deeper in a gravity well finds fewer grid points in
its PSR sphere. You said each grid point it reaches gets the same push as in deep space, so its total over the sphere is
a little less. Say the GP holding the CP still sends the same number of DI-bits, carrying the same kind of message, but
stamps the CP's part with a strength in proportion to how many grid points its own PSR sphere holds. Is that your
picture? If the "little less" is exactly in proportion to that count, the Moon's orbit, the atomic clocks and Mercury
all come out right together, for mass and charge alike.

## 7. Corrections to the draft before publication (critic)

- "Derived" became "required": §2 imposes local invariance and solves for p, so the word is required. The founder's
  principle is the premise.
- "Exact, no residual" was withdrawn for G: the lapse sensitivity leaves (1 − ε₀²/2) (§2).
- "The tension does not arise" is now scoped: it does not arise **from the source rule**. Whether α carries ε₀²/2 is
  open (§2, §4).
- "Far field set by R at the source" is now scoped to the gather kernel; the local result holds for both kernels (§1).

## 8. PD-008

- **Convenient branch 1:** "the founder's (b) was always p = 3." Partly true, because 4360 §3 contradicts his clause.
  Partly convenient, because his literal picture gives p = 0. Put to him (§6), not assumed.
- **Convenient branch 2:** "α is free of the ε₀²/2 residual, because the charge census does not set the lapse." This is
  inferred, not shown. It is the next critic's first item (TODO-4364-EPSABS).
- **Refused:** "keep the gather kernel because GR-1j was ratified." The corpus's own emission picture is scatter. Logged
  as TODO-4364-KERNEL.
- **Not claimed:** any exclusion. The self-gravitating-body gap is a test the corpus has not yet met, and it predates
  this patch: GR-1j's implied p = 2 has a gap of the same size.

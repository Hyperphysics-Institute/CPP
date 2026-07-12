# Avenue (B) — the N=8 closed ring as a CDM-like dark-matter candidate (draft registration)

**Draft, Patch 2420, 11 July 2026.** Successor to OPEN-SS-43 D3 (§34.23) after the coring routes closed:
elastic corridor death (Q5, 2413), |SSV| dissipative capture dead candidate-blind (2418), population
route dead by the cascade vise (2419). This document registers the candidate honestly as CDM-like and
attaches the falsifier menu the CONV-001 Q5 panel compiled (2415 Part-II item 3). **Grade proposed:
CONSISTENCY-grade** (viable-and-compatible, not identified) — the 1200 precedent.

---

## 1. The candidate, sharply

A single closed ring, selected by the direct-detection ladder — not assumed:

| Property | Value | Provenance |
|---|---|---|
| Species | **N = 8 closed ring** (single member) | 2410/2411, founder-adopted |
| Mass | **11.26 GeV** (= 8 × 1.408 GeV) | 2383 |
| Coat scale R_s | 25.42 fm (de-novo gap Route B, inside [20,51] band) | 2399 |
| Nucleon coupling | first-power colour-dipole, S_c = R_N/R_s ≈ 0.035 (island [0.012, 0.05]; fine wall S_c* owed) | D5-A′ (provisional) |
| SI cross-section | σ = 2.85×10⁻⁴⁹ cm² | 2410 |
| Dynamics | cold, collisionless, **no coring by any derivable mechanism** | §2 |

**The direct-detection ladder SELECTED this mass.** N=4 (5.63 GeV) excluded ×8.8×10⁶; N=5 (7.04)
excluded ×7.1×10⁴; N=6 (8.45) excluded ×361; N=7 (9.86) fails ×2.15 in-coverage — all against the
authenticated WS2022+WS2024 LZ curve (HEPData ins2841863 v2). **N=8 stands alone**, clearing every
rung including the strict tabulated point (2.1817×10⁻⁴⁸ at 40 GeV) by ×7.655 and its own local value.
This is a data-driven pin, not a chosen parameter — the strongest thing the candidate has.

## 2. Why CDM-like: coring is closed on every derivable route

The core-cusp / dwarf-coring box is not checked by this candidate, and that is now a derived statement,
not an omission:

- **Elastic self-interaction:** corridor-dead at ring composition (Q5, 2413); σ/m ≈ 10⁻³ cm²/g,
  ~250–1260× below the SIDM bound (1200 gates carry over) — collisionless to Bullet-Cluster tolerance.
- **|SSV| dissipative capture:** dead **candidate-blind** (2418) — the killing terms (harmonic-null
  theorem; the 0.9 MeV activation gap; the 3.2 meV T_amb cap) are Sea/mode properties no ring
  configuration can move; knee short of the coring demand by ~10^(1.2×10⁸).
- **Population/dimer route:** dead by the cascade vise (2419) — coring needs f_dimer ≈ 0.99, XQC hiding
  caps f_dimer < 0.034, and the 2382 cascade derives the hiding side (closed-ring dominant).

**Consequence:** dwarf cores, if real, are baryonic (feedback), not DM microphysics. A CDM-like relic
does not need to explain them — core-cusp is observationally contested and feedback is the mainstream
account. The candidate hides where DM should hide and is collisionless where the honest data permits.

## 3. The falsifier menu (what would kill it)

A CDM-like candidate below the neutrino fog is an epistemic liability *without* attached falsifiers
(R5, 2415). These are the gates; each is a real way the candidate dies.

### (i) Relic abundance & population reconciliation — **RUN (Patch 2421); conditionally reconcilable, pinned to one number**
The make-or-break gate, now computed. `code/2421_falsifier_i_population_dd.py` scans the cascade
w(N | r, φ, ε, v_f) across the full registered brackets against the DD-survival test — each excluded
species allowed only at mass fraction f_N < 1/X_N (a species at fraction f gives f× the LZ signal):
f_4 < 1.1×10⁻⁷, f_5 < 1.4×10⁻⁵, f_6 < 2.8×10⁻³, f_7 < 0.47; N≥8 DD-clear.

**Result: the reconciliation exists — the candidate is NOT internally falsified — but only at the top
edge of the registered corridor.** At central brackets, the DD-surviving (N≥8-dominant, N<8 suppressed)
population switches on at **r ≳ 13, i.e. N_stab ≳ 6.2**:

| r | N_stab | peak | f(N≥8) | f(N=6) | DD-survive |
|---|---|---|---|---|---|
| 10 | 4.7 | N7 | 0.12 | 0.27 | no (small-N, excluded) |
| 12 | 5.7 | N8 | 0.88 | 4.2×10⁻³ | no (N=6 over ceiling ×1.5) |
| 13 | 6.2 | N9 | 0.98 | 0 | **yes** |
| 14 | 6.6 | N10 | 1.00 | 0 | **yes** |
| 15 | 7.1 | N11 | 1.00 | 0 | **yes** |

Below the edge — the *bulk* of the registered corridor (r = 3–12, N_c = 3–6) — the population is
small-N-dominant (N=3–7), which the LZ ladder excludes. So the whole reconciliation reduces to **one
substrate number: N_stab = c·κ/(ℓ_rung·E_bond)**. The candidate survives iff **N_stab ≳ 6.2**; it fails
if N_stab ≲ 6 (formation then makes DD-excluded light rings). The registered band is N_stab ∈ [3.3, 7.3]
— so survival needs the **top ~third** of that band.

**Two honest riders.** (a) *The DD data independently pushes N_stab high:* "N=8 is the lightest LZ
survivor" *is* the observational statement that, if these rings are the DM, the formation floor sits at
N≥8 — i.e. N_stab ≳ 7. DD and formation therefore agree at the top of the band; the open question is
whether the substrate constants land there. (b) *Formation prefers slightly heavier than the bare-DD
N=8:* at central brackets the clean DD-surviving peak is **N ≈ 9–11 (12.7–15.5 GeV)**; N=8 (11.26 GeV)
sits right at the boundary (marginal on the N=6 tail at central brackets, comfortable at slightly higher
N_stab). So the joint formation+DD candidate is a ring at **N ≈ 8–11**, not sharply N=8.

**N_stab DERIVED (Patch 2422).** `code/2422_nstab_derivation.py`. N_stab = c·r/ε from the registered
constituents (2381): r = ℓ_p/ℓ_rung ∈ [8.5, 12] (ring placement, ℓ_rung = 1 fm); ε = E_bond/kT_form ∈
[23.2, 36.2]; **c = the rung-bond bending stiffness, 14.054 (Salpeter fluctuation-corrected) or
2π² = 19.739 (rigid)** — two standard forms of the same object. The candidate's fate on (i) collapses
onto *which coefficient governs the stability floor*:

| coefficient | N_stab range | central | vs 6.2 | box fraction clearing |
|---|---|---|---|---|
| SY 14.054 (fluctuation-corrected) | [3.30, 7.27] | **4.85** | FAILS | 8% |
| rigid 2π² = 19.739 | [4.63, 10.21] | **6.81** | CLEARS | 71% |

**The physics of the choice (and my read).** N_stab is the boundary where a formed ring's opening
barrier ε − c·r/N crosses zero — a *barrier-height*, i.e. energetic, quantity. The stored bending
energy of the exact discrete N-gon is 2π²·r·kT/N (2381 §3), so the **bare energetic floor uses c = 2π²
= 19.739 → central N_stab ≈ 6.81, which clears 6.2**. The SY value 14.054 = 0.712×2π² is the
fluctuation-corrected *nucleation-rate* coefficient (the J-factor exponent); the 2382 code used it for
the floor, which appears to conflate the closure *rate* with the stability *boundary*. 2382's own §2
prose supports the energetic reading — "ln Λ only delaying the lock, never moving the boundary." **So on
the leading-order (energetic) reading the candidate SURVIVES (i);** the open uncertainty is how much
thermal fluctuation softens the floor toward the SY value — enough softening (down to ≲4.85) sinks it.

**Net for (i):** not settled by fiat, but reduced to one sharp, bounded, decidable question — *does the
ring-stability floor take the rigid 2π² bending stiffness or its fluctuation-corrected value?* The
energetic leading order says rigid (survives, central N_stab ≈ 6.81); a full fluctuation treatment of
the pop-open barrier settles it. A clean panel target. Still owed alongside: the absolute Ω_DM
normalization.

**DIRECT COMPUTATION (Patch 2423) — the floor is rigid-like, but the candidate is a coin-flip.**
`code/2423_softened_floor.py` builds the ring free energy explicitly: anharmonic mean-field bending
[E = N·r·(1−cos 2π/N), c_eff ≈ 18.0–18.8 at N=6–8] plus the harmonic fluctuations of the joint angles
under the three closure constraints (tangent + position). The softening and the fluctuation entropy
**nearly cancel**: **N_stab ≈ 6.79 central** (vs rigid 6.81, SY 4.85) — so the coefficient question is
resolved in favor of the near-rigid value. **But N_stab ≈ 6.79 is not sufficient.** Feeding this floor
back into the cascade (consistently — the 2421 "6.2" used the SY floor), the population piles up *just
above* the floor at **N = 7 (77% mass), which LZ excludes** (f₇ = 0.77 over its 0.47 ceiling by ×1.6).
DD-survival requires the peak pushed to N≥8, which needs the substrate at larger r / smaller ε:

- **central (r=10.25, ε=29.7):** N_stab 6.79, peak **N=7 → EXCLUDED** (fails).
- **favorable (r≳11, ε≲26):** N_stab ≳ 9, peak N≥9 → **survives**.
- **DD-surviving fraction of the registered (r,ε) box: ≈ 53%.**

**r AND ε DERIVED — reduced to one owed number (Patch 2424).** `code/2424_r_eps_derivation.py`. Both
ratios trace to the *same* object: r = ℓ_p/ℓ_rung = κ_θ/kT_form and ε = E_bond/kT_form, where ℓ_rung =
1 fm (pinned) and kT_form ≈ 16.5 keV (registered). The kT_form **cancels** in the deciding combination:
**r/ε = κ_θ/E_bond** — the *stiffness-to-depth ratio* of the 2eDP:2qDP rung-bond hinge well. DD-survival
needs r/ε ≳ 0.43; central registered value 0.345 → **fails by ×1.25**. In absolute terms (via kT_form):
κ_θ ≈ 169 keV, E_bond ≈ 490 keV; survival requires the rung-bond SSV potential to give κ_θ ≳ 211 keV
(~25% stiffer) or E_bond ≲ 393 keV (~25% shallower). Both sit inside the 0860 fragmentation window and
the 1858 E_c scale, so neither is independently pinned tighter.

**So r and ε do not resolve the coin-flip from registered constants — they collapse it onto a single
strong-sector calculation: the 2eDP:2qDP rung-bond SSV potential (κ_θ, E_bond).** This is exactly the
"make-or-break" flagged since 0861/0863 ("derive the rung-bond SSV potential → E_bond and κ_θ"), now
sharpened to one numeric target that decides the entire candidate: **κ_θ/E_bond ≳ 0.43.** Mild
qualitative lean — at ℓ_rung/R_s = 0.039 the bond is nearly unscreened Coulomb, which favors stiffer
wells — but 0863's near-cancellation warning stands: the value needs the SSV charge-sum, not an estimate.
The candidate's fate, and the relic-abundance normalization, both wait on that one calculation.


### (ii) Small-scale structure cutoff
The 11.26 GeV cold relic's free-streaming length is far below observable halo scales (CDM-like to
sub-solar mass); the discriminating cutoff comes from **kinetic decoupling** set by the ring's coupling
to the thermal bath, which imprints a minimum halo mass / subhalo-mass-function turnover.
**Falsifier:** the derived kinetic-decoupling cutoff maps to a minimum halo mass testable by
stellar-stream gaps, strong-lensing substructure, and Lyman-α; a cutoff observations forbid (too high)
or require (that the candidate cannot produce) kills it. *Decoupling temperature owed (needs the ring↔bath
coupling).*

### (iii) Next-generation direct detection vs the derived coupling
N=8's σ = 2.85×10⁻⁴⁹ cm² at 11.26 GeV sits ×7.7 below the current strongest LZ point and in the regime
where the solar/atmospheric-neutrino background limits reach — **at or below the neutrino fog** at this
mass. **Falsifier:** a next-gen experiment (XLZD/DARWIN) that reaches 2.85×10⁻⁴⁹ cm² and sees nothing,
or sees a signal inconsistent with 11.26 GeV / this σ, kills it. Honest limitation: this σ may be below
clean-confirmation reach — the candidate is more readily *falsified* than *confirmed* by direct
detection. *Exact neutrino-floor crossing at 11.26 GeV owed.*

### (iv) BBN / CMB light-species
The gapless |SSV| mode is relativistic; if it thermalizes (OPEN-DM-TAMB-1) it contributes ΔN_eff, and
the light open-chain residue (monomers w1<0.013, dimers w2<0.034) plus the cascade's entropy release
bear on BBN. **Falsifier:** the light Sea sector's contribution must satisfy N_eff = 2.99 ± 0.17 (CMB)
and the light-element abundances; a thermalized mode over-contributing to N_eff kills it. *Ties directly
to the TAMB-1 thermalization question — the same mode physics that closed |SSV| coring is a falsifier
input here.*

## 4. Derived-vs-owed ledger (honest boundary)

**Derived / established:** the mass (DD-selected, 2410); collisionlessness (three closures, §2);
coldness (GeV scale); the DD clearing at the derived coupling (ladder record, 2410); the coring closure
(2413/2418/2419).

**Owed (each a falsifier above):** (i) the population→N=8 reconciliation and absolute Ω_DM — *the
decisive one*; (ii) the kinetic-decoupling cutoff → minimum halo mass; (iii) the neutrino-floor crossing
at 11.26 GeV; (iv) the ΔN_eff from the light Sea sector. Provisional pins: S_c fine wall S_c* (SS43-Q1);
the D5-A′ coupling ruling (derivation debt).

## 5. Grade and posture

**CONSISTENCY-grade, not IDENTIFICATION-grade.** The candidate is *compatible with* being the dark
matter — DD-selected, collisionless, cold — but does not yet *identify* as it: falsifier (i) is
unresolved and could sink it. For the swarm claim, the value is that the nine axioms produce a single,
sharply-specified relic that the direct-detection data itself selected, with a complete falsifier menu —
a genuine prediction, not a placeholder. **The honest headline is not "we found the DM"; it is "the
axioms produce one CDM-like candidate, the data picked its mass, and here are the four ways to kill it."**
The first of those four is the next computation.

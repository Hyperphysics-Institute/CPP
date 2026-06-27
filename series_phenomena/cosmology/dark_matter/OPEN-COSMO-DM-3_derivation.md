# OPEN-COSMO-DM-3 — Sub-threshold Substrate-Locality: a derivation

**Status:** DERIVATION DRAFTED (Patch 0882, 27 June 2026). Layer B (derived from grounded substrate
properties + standard many-body theory; residual = full 600-cell surface-mode formalization). **Proposed
for panel ratification** before lifting LEMMA-DM-CROSS-ROUTE-1 from conditional to unconditional.
**Lane:** COSMO / SR (Sea dynamics). DM-1 stays v0.1.

---

## 1. What must be shown

ASM-DM-CORONA-LOCALITY, as registered (CONJ.md, 0877): *a surface electric potential well shallower than
the eDP creation energy (V₀_elec ≪ E_eDP = 88 MeV; here V₀_elec ~ 34–94 keV, ~1500× sub-threshold) elicits
only reversible, constituent-local vacuum polarization — already in m_unit — and generates no persistent
real-eDP surface population and no extensive (surface-scaling) collective-mode or condensate mass.*

The panel's RESTATE-with-fix granted the single-eDP energy argument but required that **three** field-theory
alternatives be *excluded, not asserted*: (i) metastable surface states, (ii) collective surface modes,
(iii) induced condensates. This document closes all three in the sub-threshold regime.

## 2. The two grounded substrate inputs that decide it

1. **The matter sector is gapped at E_eDP = 88 MeV** — the eDP creation / pair-production threshold (SF-3).
   This is the substrate's "supercritical-Z" scale (the analogy the reviewer invoked).
2. **The only gapless Sea mode is the photon (helicity ±1), and it is sourced by net charge** (SR.md: the
   gapless photon emerges from the DP Sea; the absolute-|SSV| monopole is annihilated by the 600-cell
   5-design and is inert). There is **no gapless matter channel.**

And the object itself: **the Cross-Rod surface is charge-neutral** (8-eCP shell, 4+/4−) **and color-neutral**
(8-qCP cube, 4+/4−; genesis 0880). It sources no long-range field; the Sea sees a neutral surface presenting
only a short-range induced (van der Waals) well, V₀ ~ 34–94 keV.

## 3. The derivation (three routes, all closed — quantified in code/0882)

**(i) Metastable surface states — sub-critical, hence reversible.** A real eDP is populated only if a bound
level is dragged into the negative-energy continuum, i.e. the well reaches the pair threshold E_eDP. Here
V₀/E_eDP ~ 6×10⁻⁴ (~1500× sub-threshold), so any in-gap surface level remains a **virtual** state: it
contributes to the *reversible* polarization cloud (already in m_unit) and carries **no real population**.
This is the standard Schwinger / supercritical-Z result, applied with the substrate's own threshold E_eDP.

**(ii) Collective surface modes — cannot be softened.** A condensing instability requires some collective
mode to reach zero energy. The matter-sector collective modes are gapped at ~E_eDP; a weak static well
shifts a gapped mode by at most second order, ~V₀²/E_eDP ≈ 36 eV ≈ 4×10⁻⁷ of the gap — to drive it to zero
would take a shift of E_eDP itself, larger by ~10⁶. The *gapless* mode is the photon, **sourced by net
charge**: a neutral surface has no monopole, so it does not couple to the photon at k→0; and the finite-k
photon is a propagating mode (ℏck > 0), not a zero-energy condensation channel. So there is **no soft
channel** a neutral sub-threshold well could exploit.

**(iii) Induced condensates — exponentially non-extensive.** Grant the strongest case: the induced vdW *is*
attractive, so a collective (BCS-type) channel exists in principle. Its condensate gap is weak-coupling,
Δ ~ E_eDP·exp(−E_eDP/V₀), with inverse coupling E_eDP/V₀ ~ 900–2600. Hence Δ/E_eDP ~ 10⁻⁴⁰⁰ … 10⁻¹¹⁰⁰ —
the condensate mass is **non-extensive**, utterly negligible against m_unit, and cannot dilute σ/m. The
weak-coupling premise is not an extra assumption: V₀ ≪ E_eDP *is* weak coupling.

**Conclusion.** All three RESTATE routes are closed. A sub-threshold (V₀ ≪ E_eDP) electric well on a
charge- and color-neutral surface elicits **only reversible, constituent-local vacuum polarization** — no
real-eDP population, no extensive collective-mode or condensate mass. This is exactly ASM-DM-CORONA-LOCALITY.
∎ (at the many-body-argument level)

## 4. Honest grade and residual

**Grade: Layer B.** The arguments are standard many-body results (supercritical-Z sub-criticality;
second-order perturbative mode-shift bound; BCS weak-coupling suppression) applied to **grounded** substrate
properties (the E_eDP matter gap; the charge-sourced gapless photon; the neutral Cross-Rod surface). This is
strictly stronger than the Layer-C "named assumption" it replaces, and it addresses precisely the three
alternatives the panel asked be excluded.

**Residual (what keeps it B, not A):** full formalization on the **600-cell surface-mode spectrum** — an
explicit finite-k collective-mode calculation at the spine boundary — to confirm there is no *anomalous
sub-gap strong-coupling channel* (a resonant near-degeneracy that would defeat the weak-coupling/perturbative
bounds). Note this residual is self-limiting: V₀ ≪ E_eDP *is* the weak-coupling statement, so an O(1)-coupling
sub-gap channel would have to be a genuine substrate anomaly, not a generic possibility.

## 5. Disposition

Recommend this derivation go to the four-model panel (CONV-001) for ratification. If confirmed,
**LEMMA-DM-CROSS-ROUTE-1 lifts from CONDITIONAL to unconditional**, and the cross route's result comes off its
last hedge. Until ratified, OPEN-COSMO-DM-3 is marked *derivation drafted (Layer B), pending panel* — not yet
CLOSED, and the lemma stays conditional. No registry/THEO/swarm change is made unilaterally.

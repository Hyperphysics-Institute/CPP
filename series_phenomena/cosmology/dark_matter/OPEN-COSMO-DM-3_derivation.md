# OPEN-COSMO-DM-3 — Sub-threshold Substrate-Locality: a derivation

**Status:** DERIVATION DRAFTED (Patch 0882) → **PANEL-REVIEWED & FIXES FOLDED (Patch 0883, 27 June 2026).** Four-model panel: **3 CONFIRM-and-lift (Grok, Gemini, Copilot) + 1 RESTATE-with-fix (ChatGPT).** The RESTATE is honored, not outvoted: it identifies a real unexcluded kill route (a near-zero charge-neutral 600-cell boundary mode) that the CONFIRMERS' "self-limiting" argument misses, and correctly downgrades the BCS step to a heuristic. Fixes folded below. **Result: ASM-DM-CORONA-LOCALITY is now Layer-B–derived modulo one sharp residual; LEMMA-DM-CROSS-ROUTE-1 is strongly DE-RISKED but STAYS CONDITIONAL on that residual — NOT lifted to unconditional.** **Lane:** COSMO / SR (Sea dynamics). DM-1 stays v0.1.

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

**(i) Metastable surface states — sub-critical, hence reversible. [CONFIRM, wording fixed]** A real eDP is
populated only if a bound level is dragged into the negative-energy continuum, i.e. the well reaches the pair
threshold E_eDP. Here V₀/E_eDP ~ 6×10⁻⁴ (~1500× sub-threshold), so any in-gap surface level remains a
**virtual** state and contributes only to the *reversible* polarization cloud (already in m_unit), **provided
no external real-eDP reservoir supplies the population** — which is the case: the only dense reservoir, the
balanced Planck-scale vacuum Sea, supplies none (0875). So: sub-critical *and* no reservoir ⇒ no real
population. (Panel fix: the no-real-population claim is conditioned on the absent reservoir, not asserted as a
bare occupation rule.) This is the standard Schwinger / supercritical-Z result with the substrate's own
threshold E_eDP.

**(ii) Collective surface modes — no soft channel, *conditional on the boundary spectrum*. [RESTATE-with-fix]**
A condensing instability requires some collective mode to reach zero energy. Two sub-cases: *(a)* the gapless
photon is **sourced by net charge**, and the neutral surface has no monopole, so it does not couple at k→0;
the finite-k photon is propagating (ℏck > 0), not a zero-energy condensation channel — **this half is solidly
closed** (all four reviewers confirm). *(b)* Matter-sector modes **gapped at ~E_eDP** are shifted by a weak
static well at most ~V₀²/E_eDP ≈ 36 eV ≈ 4×10⁻⁷ of the gap — cannot soften. **But this bound assumes the
relevant modes are gapped at ~E_eDP.** The honest residual the panel sharpened: if the spine boundary hosts a
**near-zero-energy, charge-neutral surface mode** (gapped at ~0, not E_eDP), the perturbative bound does not
apply to it, and even a weak attractive coupling could push it unstable — and this is *not* excluded by
V₀ ≪ E_eDP (it is a question about the boundary spectrum, not the well depth). So (ii) closes **conditional on
the absence of an anomalous near-degenerate 600-cell boundary mode.** Generically such a mode is not expected
(in-gap surface states spread through the gap at O(E_eDP) energies; a near-zero one needs a symmetry/topology
protection or accidental degeneracy), but ruling it out requires the explicit spectrum (§4 residual).

**(iii) Induced condensates — not an independent closure; reduces to (i)+(ii). [RESTATE-with-fix]** Any
extensive condensate requires *either* a real-eDP population — excluded by **(i)** (sub-critical, no reservoir)
— *or* a sub-gap collective instability — excluded by **(ii)** *modulo* the near-zero-boundary-mode residual.
So (iii) is **downstream of (i) and (ii)**, not a third independent argument. The BCS estimate
Δ ~ E_eDP·exp(−E_eDP/V₀) ~ 10⁻⁴⁰⁰…10⁻¹¹⁰⁰ is retained only as an **illustrative upper-bound heuristic** for
the weak-coupling case — *not* a substrate derivation (panel fix: the eDP sector is bosonic, not a
Fermi-surface pairing problem, so the BCS DOS assumptions do not map cleanly). The robust statement is the
reduction to (i)+(ii): any condensate is suppressed *unless* the boundary spectrum supplies an anomalously
large density of near-zero charge-neutral states — the same residual as (ii).

**Conclusion (post-fold).** Point (i) and the photon half of (ii) are closed outright. Points (ii-matter) and
(iii) reduce the entire remaining corona risk to **one sharp, physical question**: does the 600-cell spine
boundary host a near-zero-energy, charge-neutral collective surface mode? If no (the generic expectation), a
sub-threshold electric well on the neutral surface elicits only reversible, constituent-local vacuum
polarization — exactly ASM-DM-CORONA-LOCALITY. If yes, the corona could re-open through that mode. The
assumption is thus **derived modulo a single named residual**, not closed.

## 4. Grade and the sharpened residual

**Grade: Layer B.** Point (i) (sub-critical + no reservoir) and the photon-decoupling half of (ii) are solid,
panel-confirmed many-body results on grounded substrate facts (the E_eDP gap; the charge-sourced gapless
photon; the neutral surface). This is materially stronger than the Layer-C named assumption it replaces.

**The residual (sharpened by the panel — physical, not cosmetic):** the corona risk now reduces to a single
question — **does the 600-cell spine boundary host a near-zero-energy, charge-neutral collective surface
mode?** This is what (ii-matter) and (iii) both lean on, and it is *not* settled by V₀ ≪ E_eDP (a near-zero
mode evades the perturbative bound regardless of well depth). Closing it requires an **explicit finite-k
collective-mode (surface-mode) spectrum at the spine boundary on the 600-cell substrate.** Generic expectation:
no near-zero charge-neutral mode (in-gap surface states sit at O(E_eDP), and a zero mode would need
symmetry/topology protection) — so the corona is *probably* dead — but this must be computed, not asserted.

## 5. Disposition (post-panel)

Panel return: **3 CONFIRM-and-lift + 1 RESTATE-with-fix.** The RESTATE is **honored, not outvoted** — it
correctly identifies the near-zero-boundary-mode kill route the CONFIRMERS' self-limiting argument misses, and
correctly downgrades the BCS step to a heuristic. Accordingly:

- **ASM-DM-CORONA-LOCALITY** is upgraded from a bare named assumption to **Layer-B–derived modulo the
  surface-mode residual.**
- **LEMMA-DM-CROSS-ROUTE-1 stays CONDITIONAL — NOT lifted to unconditional** — but its condition is now reduced
  from a broad unexamined assumption to **one specific, generically-disfavored, checkable physical residual**
  (no near-zero charge-neutral 600-cell boundary mode). This is a real de-risking, not a closure.
- **Next concrete work (now precisely aimed):** the 600-cell spine-boundary surface-mode spectrum. A clean
  gap (no near-zero charge-neutral mode) closes OPEN-COSMO-DM-3 and lifts the lemma; a near-zero mode re-opens
  the corona on a specific, identified mechanism.

No registry/THEO/swarm change beyond recording the panel return and the de-risking. CONJ-COSMO-1 untouched.

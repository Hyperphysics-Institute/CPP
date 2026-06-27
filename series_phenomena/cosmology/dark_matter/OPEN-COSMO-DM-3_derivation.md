# OPEN-COSMO-DM-3 — Sub-threshold Substrate-Locality: a derivation

**Status:** DERIVATION DRAFTED (0882) → PANEL-REVIEWED & FIXES FOLDED (0883) → RESIDUAL ADDRESSED (0884) → **RE-REVIEW RATIFIED 4/4 (Patch 0885, 27 June 2026): the focused re-review returned 4/4 CONFIRM on §6 and 4/4 CONFIRM to lift, including the original dissenter, who states §6 resolves the exact objection it raised. OPEN-COSMO-DM-3 is CLOSED (derived, Layer B); LEMMA-DM-CROSS-ROUTE-1 is LIFTED to UNCONDITIONAL.** Scope (honest, per the dissenter): the panel ratified the derivation's *internal logic* within the CPP EFT / excitation-spectrum / topological-characterization assumptions — whether those assumptions are ultimately correct is separate validation. Full 600-cell lattice numerics remain optional Layer-A polish. **Lane:** COSMO / SR. DM-1 stays v0.1.

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

---

## 6. The surface-mode residual, addressed (Patch 0884)

The RESTATE reduced the corona risk to one question: **does the spine boundary host a near-zero-energy,
charge-neutral collective surface mode?** A near-zero mode would evade the V₀²/E_eDP bound regardless of well
depth. Such a mode requires one of three things; all three are closed (computation: `code/0884`).

**Effective model.** The lowest charge-neutral matter excitation is the eDP itself — a +eCP/−eCP **dipole**,
net charge-neutral — gapped at Δ = E_eDP = 88 MeV. The panel established this sector is **bosonic**. Model it
as a massive bosonic field in the half-space x>0 with the spine surface at x=0 and a Robin boundary
ψ′(0)=κψ(0); a surface mode ψ ~ e^(−qx) (q=|κ|) has ω_surf² = Δ² − (ℏcq)², in-gap for 0 < ℏc|κ| < Δ, and
ω_surf → 0 requires ℏc|κ| → Δ (deep binding ~ Δ).

**(A) Mass-sign-change domain wall — EXCLUDED.** The eDP creation cost (the "mass") is positive everywhere;
the Cross-Rod is a bound aggregate in the **same vacuum** as the Sea, not a distinct topological phase. No
sign change across the surface ⇒ no Jackiw-Rebbi zero mode.

**(B) Chiral/topological protection — EXCLUDED (generic).** A gapped **bosonic** mode has no chiral symmetry
and no bulk-boundary protected zero mode (unlike a gapped Dirac fermion; a protected one would require a
nontrivial bosonic-SPT structure). The only protected/gapless structure in
the Sea is the **photon — charge-sourced** — and the neutral surface decouples from it at k→0. The protection
lives in the charge channel, not the neutral channel the surface couples to. (Wording, per panel: the claim is
that *CPP possesses no such bosonic-SPT structure in the neutral sector* — not that exotic bosonic topological
order is impossible in principle; the former is the stronger, falsifiable statement.)

**(C) Accidental fine-tuning — EXCLUDED (non-generic).** This is the decisive quantitative point, and it
closes via the *same* sub-threshold logic as the single-particle case, now at the collective level: a **weak**
attractive surface (V₀ ≪ Δ) binds a surface mode only **shallowly below the gap top**, at depth ~V₀²/Δ ≈ 36 eV
— so ω_surf ≈ Δ ≈ 88 MeV, *nowhere near zero*. A near-zero mode would need **deep binding ~Δ**, i.e. a boundary
~1557× stronger than the actual neutral vdW surface, or a tuning to within ~V₀/Δ ~ 6×10⁻⁴ of the critical
(domain-wall) strength — a ~1-in-1557 fine-tuning, unforced by any symmetry.

**Conclusion.** The lowest charge-neutral surface mode sits at ~E_eDP = 88 MeV — a **clean gap ≫ V₀ ~ 50 keV**.
There is no near-zero charge-neutral surface mode for the weak, neutral, same-vacuum spine boundary. The
RESTATE's kill route is closed: a near-zero mode cannot be *produced* by a weak boundary (deep binding
required) and is not *protected* into existence (no domain wall; gapped bosonic neutral sector). So,
**within the CPP EFT, the corona is excluded** — there is no mechanism supporting a persistent neutral
low-energy surface mode (the precise scientific statement, distinct from an absolute impossibility) — and
ASM-DM-CORONA-LOCALITY holds at the EFT + topological-structure level.

**Residual after 0884 (honest):** the effective field theory + topological-triviality arguments are generic,
so the remaining step is a full **600-cell lattice numerical diagonalization** to confirm no lattice-specific
near-zero charge-neutral surface mode — a *confirmation formality*, not a live physical worry (a lattice mode
near zero would still need deep binding or a protection the neutral bosonic sector lacks).

**Disposition (RATIFIED).** The focused re-review returned **4/4 CONFIRM on §6 and 4/4 CONFIRM to lift**,
including the original dissenter (who states §6 resolves the exact objection it raised). Accordingly:
**OPEN-COSMO-DM-3 is CLOSED (derived, Layer B); LEMMA-DM-CROSS-ROUTE-1 is LIFTED from CONDITIONAL to
UNCONDITIONAL** (CONJ.md, Patch 0885). The lemma stays finding-level (no THEO, no swarm-count change), and
CONJ-COSMO-1 stays NOT-confirmed (σ/m-viability is not a discriminating DM identification). **Honest scope:**
this ratifies the derivation's *internal logic within the CPP assumptions* (the EFT description, the
excitation spectrum, the topological characterization); whether those assumptions are ultimately correct is a
separate validation question. The full 600-cell lattice diagonalization remains available as optional Layer-A
polish (a robustness check, no longer a gate).

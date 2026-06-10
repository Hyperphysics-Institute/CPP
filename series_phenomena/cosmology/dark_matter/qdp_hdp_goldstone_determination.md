# The hDP-Goldstone determination — the hDP is the gluon, not a Goldstone; f ≈ 0.2 confirmed and the residual mechanism fully pinned

**Patch:** 0836 (Session 156, 10 June 2026) · **Type:** determination from the corpus (closes the last open downstream Era-2 question). · **Lane:** DM-2 / `dark_matter/`.
**Closes:** 0835's one remaining caveat — whether a pion-like Goldstone role for the hDP would enhance the residual above the color-van-der-Waals estimate. **Verify:** `code/0836_hdp_goldstone_determination.py`.

---

## Two independent diagnostics, same verdict: the hDP is not a Goldstone

**The mass test.** A pseudo-Goldstone boson's mass vanishes as the symmetry-breaking order parameter goes to zero — in QCD, the Gell-Mann–Oakes–Renner relation `m_π² f_π² = −(m_u+m_d)⟨q̄q⟩`, and CPP reproduces this: SS-1 Theorem 5 (and SS-1e Theorem 2) prove `m_π → 0` exactly in the chiral limit `m_{u,d} → 0` (the u/d quarks have no polyhedral cage, so a cage-less ud̄ pair has no residual mass source). The hDP mass is, by contrast, `m_hDP = √(E_eDP·E_qDP) ≈ 152 MeV` — the geometric mean of two Coulomb bindings, **fixed and non-vanishing**, with no chiral limit in which it goes to zero. The hDP fails the Goldstone test; **the pion is CPP's Goldstone, and it is a distinct object** (a ud̄ hadron, not a Sea dipole).

**The identity test.** The corpus is explicit about what the hDP *is* (glossary-SS-1): transient hDP pairs propagating along tetrahedral edges are **gluons** (color-changing, massless), and stable closed hDP configurations are the **massive weak bosons** (W bracelet, Z cage, H cage). So the hDP is the CPP **gauge-boson carrier** — gluons and weak bosons — not a Goldstone. Gauge bosons are not Goldstones; the geometric-mean mass is a Sea-statistics scale, not a symmetry-breaking one.

## The payoff: hDP = gluon explains the whole residual structure

This does more than close a caveat — it grounds the entire 0830–0835 residual picture mechanistically:

- **Why the residual is a van der Waals, not a stronger Yukawa.** The hDP is the gluon. A color-**singlet** qDP cannot emit a *single* gluon — color conservation forbids it (a singlet can't change its color-singlet nature by radiating one colored object). So single-hDP exchange between qDPs is forbidden, and the leading color exchange is **two-gluon (two-hDP) exchange = the color van der Waals** — exactly the channel computed in 0835.
- **Why f < 1 (residue weaker than source).** The qDP's *internal* binding is a single-gluon-strength color interaction; the *inter*-qDP residual is a two-gluon, higher-order effect. The "residue is weaker than its source" hierarchy that has done so much work across 0831–0835 is now mechanistically grounded: it is the single-gluon-vs-two-gluon order in the coupling.
- **Why the range is ~1.3 fm.** The two-gluon color van der Waals is cut off at the confinement/hDP scale (gluons do not propagate freely beyond ~ℏc/152 MeV ≈ 1.3 fm) — precisely the Yukawa range assumed in 0831/0832.

## The pion channel is suppressed, so there is no enhancement

Could the actual Goldstone (the pion) be exchanged between qDPs and dominate, the way one-pion-exchange dominates two-gluon exchange in the nuclear force? No, for these qDPs: one-pion-exchange requires a strong single-pion *source*, i.e. a net axial coupling. A qDP's ground state is a spin-0 color-singlet dipole (the DP-Sea soliton ground state is spin-0), which carries no net axial charge and is therefore not a single-pion source — pion exchange between qDPs is suppressed to two-pion order or absent. (If some qDP population were spin-1, a pion channel could open, but the two-gluon color van der Waals remains the leading singlet–singlet residual regardless.) So there is **no OPE-style enhancement** of f.

## Result

The hDP is the gluon/weak-boson carrier, definitively **not** a pion-like Goldstone, so the 0835 caveat is closed in the no-enhancement direction: **f ≈ 0.2 (0835) is confirmed**, and the residual mechanism is now fully identified as the **two-gluon-exchange color van der Waals** between color-singlet qDPs — with its weakness (f < 1), its ~1.3 fm range, and its α_s-governed strength all explained rather than assumed. The residual potential of 0831/0832 (V₀ ≈ 53 MeV, λ ≈ 1.3 fm, hard core ~1 fm) stands as a derived, mechanistically-grounded object.

This was the last genuinely-open downstream question in the Era-2 chain. The mechanism arc — founder's qualitative qDP/eDP buffering → glueball-avoidance (0830/0832) → collisionless (0831) → diffuse (0832/0833) → derived inputs (0833–0835) → residual mechanism pinned (0836) — is now a closed, quantitative, falsifiable chain from the substrate constants to diffuse CDM phenomenology, conditional only on the qDP/hTetra-DM conjecture and the Mechanism-A measure.

## Scope

Determination from the corpus's own gluon/Goldstone identifications (SS-1 Thm 5, SS-1e Thm 2, glossary-SS-1) plus the color-conservation selection rule. **No closure, no THEO/ID, no verdict.** The remaining program-level item is the TODO-016 DP-Sea appendix mass-scale reconciliation. Conditional on the qDP/hTetra-DM conjecture and the Mechanism-A measure.

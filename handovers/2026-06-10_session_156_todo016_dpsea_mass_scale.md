# Handover — TODO-016: DP-Sea binding-energy scale is presented as Planck-derived but is off by ~17 orders

**Task:** reconcile the DP-Sea flagship's binding-energy appendix (`series_foundations/dp_sea_composition/DP_sea_and_cage_composition.tex`).
**Date opened:** 10 June 2026 (Session 156), Patch 0837. **Origin:** surfaced during the DM-2 Era-2 required-inputs derivation (Patch 0833); registered as `todolist.md` TODO-016.
**Why a handover and not an inline fix:** the correction's deep half is a **foundational derivation** (deriving the QCD/DP scale from the Planck scale) on a **flagship paper** — a research arc, not a typo fix. **Thomas's decision is recorded below (Option C, two-part).** This document is the durable record and the opening prompt; a fresh window should paste it in and re-fetch from `handovers/` if context is lost.

---

## BLOCKING CLONE-AND-GREP GATE (before anything else)

1. Clone fresh; `git log --oneline | head -30` to see the live frontier and free patch bands (multiple windows push concurrently).
2. Read the §Required reading in order before editing.
3. This task edits a **flagship**; do not push a `.tex` content change to it without Thomas's sign-off on the physics decision below.

## KICKOFF SENTENCE

> *You are resolving a numerical inconsistency in the DP-Sea flagship: the DP binding spectrum (eDP 88, qDP 264, hDP 152 MeV) is presented as derived from the golden-ratio Planck length, but that formula evaluates to ~10¹⁶ GeV — off by ~17 orders. **Decision (Thomas): Option C.** Two-part: (1) correct the appendix now to match SS-1's honest "calibrated, Planck-derivation-open" stance and cite SS-1 `op:lambda_psr`; (2) pursue C proper = solving SS-1 `op:lambda_psr` (derive Λ_QCD/the DP scale from l_P + sea_strength via PSR saturation), which when closed upgrades both flagships from calibrated to derived. Retain the energies and the ratios throughout.*

## The inconsistency, precisely

In `DP_sea_and_cage_composition.tex` (Appendix "DP Binding Energy Calculation", lines ~316–327; also the body, lines ~76, 80):

- Stated: `E_bind = αℏc/r_min`, with `r_min = φ·l_p = 1.618 × 1.616×10⁻³⁵ m ≈ 2.61×10⁻³⁵ m`, "the golden-ratio-scaled Planck length."
- Claimed: `E_eDP = αℏc/(φl_p) ≈ 88 MeV`, `E_qDP = 3αℏc/(φl_p) ≈ 264 MeV` (color factor 3), `E_hDP = √(E_eDP·E_qDP) ≈ 152 MeV`.
- **Actual evaluation:** the paper itself (line 80) correctly states `E_p = ℏc/l_p ≈ 10¹⁹ GeV` (the Planck energy). Therefore `αℏc/(φl_p) = α·E_p/φ ≈ (1/137)(10¹⁹ GeV)/1.618 ≈ 4.5×10¹⁶ GeV ≈ 4.5×10¹⁹ MeV` — **not 88 MeV. The discrepancy is a factor of ~5×10¹⁷ (~17–18 orders of magnitude).**
- The quoted 88 MeV instead requires `r_min = αℏc/88 MeV ≈ 0.0164 fm = 1.64×10⁻¹⁷ m` — ~18 orders **larger** than the Planck length, and ~`10⁴⁸` larger than the CPP grid spacing (line 64: 10³⁰ gradations per Planck length). So `r_min ≈ 0.016 fm` corresponds to an energy scale `ℏc/r_min ≈ 12 GeV`, with the α prefactor bringing it to 88 MeV.

`l_p` is used **consistently as the gravitational Planck length** elsewhere in the paper (line 80 Planck energy 10¹⁹ GeV; line 69 Planck breaking; line 64 grid scale), and correctly so. The error is localized: applying the Planck-scale Coulomb energy to the DP binding. The 88 MeV is the right physical value (it is the constituent/QCD/Λ_QCD scale) — only its stated derivation is wrong.

## What is affected / not affected

**Affected:** the *claimed derivation* of the DP binding spectrum (eDP 88, qDP 264, hDP 152), and any text asserting "DP energies follow from the golden-ratio Planck length." The eDP = 88 MeV scale propagates through the whole DP/cage spectrum and the boson-mass averaging in this paper.

**NOT affected (do not re-open these):**
- The **ratios** are clean and untouched: `E_qDP/E_eDP = 3` (color factor) and `E_hDP = √(E_eDP·E_qDP)`. The entire DM-2 **Era-2 arc (Patches 0830–0836)** uses only the *ratio* (m_qDP ≈ 264 MeV = 3×88) and the color factor — so the Era-2 chain (glueball-avoidance, collisionless, diffuse, f ≈ 0.2) needs **no rework** regardless of how this is resolved. This is stated in the 0833 patch.
- The SM/SS-sector matching uses the *values* (88/264/152), not the Planck-derivation, so it is unaffected by a reframing of the origin.

## DECISION (Thomas, Session 156, Patch 0838): Option C — but it is a derivation to complete, not an appendix edit

Thomas chose **Option C** (Planck → DP/QCD scale via a derived suppression) as the most robust *understanding*. Confirmed, with a decisive corpus finding that scopes it:

**C is already a registered SS-1 open problem — it is not a blank slate.** SS-1 (`SS-1_strong_sector_from_600cell_lattice.tex`) contains two open problems that *are* C:
- `op:lambda_psr` ("Λ_QCD from PSR saturation"): *"The PSR saturation mechanism relates Λ_QCD to the Planck-scale threshold PSR_eff → l_P/2. Deriving Λ_QCD ≈ 0.218 GeV from l_P and sea_strength — without using the PDG value as input — would constitute a first-principles derivation of the QCD confinement scale."*
- `op:sigma` ("String tension σ from sea_strength"): σ ≈ 0.9 GeV/fm is **calibrated** to the charmonium/bottomonium spectrum; deriving it from sea_strength = 0.185 and the 600-cell qDP chain geometry would close the strong-sector parameter space. Partial results exist in `series_strong/notebooks/chain_fraying_dynamics.ipynb`.

So C = solving SS-1 `op:lambda_psr` (with a candidate mechanism, PSR saturation → l_P/2, and partial numerical work already on file). The DP binding scale (88 MeV) is in the same QCD-scale family (Λ_QCD ≈ 218, eDP 88, qDP 264 MeV).

**The appendix's actual error, sharpened.** SS-1 honestly marks this scale as *calibrated* with its Planck derivation *open*. The DP-Sea appendix instead **asserts the derivation is done** (`88 MeV = αℏc/(φl_p)`, which is false by ~17 orders). The two flagships are inconsistent in their honesty; the appendix is the one out of step.

**Therefore the resolution is two-part, and they are NOT in tension:**

1. **Immediate appendix correction (do this without waiting on the research).** Bring the DP-Sea appendix into line with SS-1's honest stance: state that the DP binding scale (88/264/152 MeV) is **anchored to the CPP strong-sector confinement scale** (currently calibrated, à la SS-1 `op:sigma`/`op:lambda_psr`), and that its **first-principles derivation from the Planck scale via PSR saturation is the open problem SS-1 `op:lambda_psr`** — *cite that open problem rather than duplicate-and-misstate it*. Remove the false `αℏc/(φl_p) ≈ 88 MeV` claim and the "golden-ratio-scaled Planck length / 2.61×10⁻³⁵ m" identification (lines ~76, 321). **Retain the energies 88/264/152** (physically correct, downstream load-bearing) and the **color-factor-3 / geometric-mean ratios** (clean). This is honest *now* and consistent with the strong-sector flagship — not a concession, a unification of stance.

2. **The research target = C proper.** Pursue SS-1 `op:lambda_psr` (Λ_QCD/DP scale from l_P + sea_strength via PSR saturation, PSR_eff → l_P/2), drawing on the `chain_fraying_dynamics.ipynb` partial results and `op:sigma`. **When it closes, it upgrades *both* the DP-Sea appendix *and* SS-1 from "calibrated" to "derived" in one stroke** — that is the robust payoff Thomas is after. This is a genuine derivation arc; **promote it to `future_projects.md`** (it is multi-session, with mechanism/falsifier/companion fields) rather than leaving it as a todolist hygiene item.

## Required reading (in order)

1. `series_foundations/dp_sea_composition/DP_sea_and_cage_composition.tex` lines 60–96 and 312–340 (the body scale statements + the appendix block to correct).
2. `series_strong/papers/SS-1_strong_sector_from_600cell_lattice.tex` open problems `op:sigma` (~line 987) and `op:lambda_psr` (~line 1086) — **C is these**. Also Remark `rem:psr` (PSR saturation mechanism) and the C14 self-consistent relation `r_conf = √(α_s ℏc/σ)`.
3. `series_strong/notebooks/chain_fraying_dynamics.ipynb` — the partial numerical results for `op:sigma` (the established self-consistent relation + bow-rigidity mechanism).
4. `series_phenomena/cosmology/dark_matter/qdp_required_inputs_derivation.md` (Patch 0833 — where the inconsistency surfaced; confirms the ratio is clean, the DM arc is unaffected).
5. `todolist.md` TODO-016.

## Execution path (two tracks)

**Track 1 — appendix correction (near-term, gated only on Thomas's sign-off of the wording).**
1. Clone-and-grep gate; claim a free patch number.
2. Draft the corrected DP-Sea appendix: energies 88/264/152 retained; the `αℏc/(φl_p) ≈ 88 MeV` derivation and the "2.61×10⁻³⁵ m / golden-ratio Planck length" identification (lines ~76, 321) **replaced** with: the DP binding scale is anchored to the CPP strong-sector confinement scale (calibrated, as in SS-1 `op:sigma`), and its first-principles derivation from l_P is the open problem SS-1 `op:lambda_psr` — with an explicit cross-reference. Keep the color-factor-3 and geometric-mean ratios.
3. Present the drafted text to Thomas; he performs the flagship `.tex` edit + recompile + publish per his workflow.
4. Move TODO-016 to cleared-items with date + patch number.

**Track 2 — C proper (the derivation arc; promote to `future_projects.md`).**
1. Register a project: "Λ_QCD / DP binding scale from l_P + sea_strength via PSR saturation" (= SS-1 `op:lambda_psr`), with `op:sigma` as the sibling. Mechanism: PSR saturation, PSR_eff → l_P/2; target Λ_QCD ≈ 0.218 GeV (and the DP spectrum) from l_P and sea_strength = 0.185, **without** PDG input. Falsifier: if no l_P→QCD-scale relation reproduces ~0.2 GeV within tolerance, the "DP scale is Planck-derived" claim is abandoned in favor of permanent calibration.
2. Build on the `chain_fraying_dynamics.ipynb` partial results and the C14 self-consistent `r_conf`/σ relation.
3. On success: upgrade **both** the DP-Sea appendix and SS-1 `op:lambda_psr`/`op:sigma` from "calibrated" to "derived" — the unified payoff.

**Status at handover:** decision recorded (Option C, two-part). Track 1 awaits a drafting+sign-off pass; Track 2 to be promoted to `future_projects.md` as the `op:lambda_psr` derivation arc. No flagship edit made yet. DM-2 Era-2 arc (0830–0836) confirmed independent of the resolution (uses only the clean color-factor-3 ratio).

# F-DM3-4 rate computation — STAGE 1: overburden ceilings + visibility window (Patch 2365, 9 July 2026)

## Provenance and split
The lane's required next computation (SI-1, promoted 2362; J-D BREAK unanimous-in-substance).
The owed computation splits: **Stage 1 (this patch, model-independent):** the overburden
ceilings and the visibility window at m_dimer = 2.8 GeV per site class. **Stage 2 (owed,
model-side):** σ_dimer from the P2-channel machinery at A_dimer, judged against the Stage-1
window, with the gap regions treated explicitly and the floors pinned to current exclusion
curves. F-DM3-4 activates only on Stage 2.

## Pre-registered (fixed in the script header before execution)
- **Estimator:** CSDA energy degradation; coherent-SI scaling σ_A = σ_n A²(μ_A/μ_n)²
  (**hurting-direction:** maximizes stopping, lowers ceilings); mean per-scatter loss
  f = 2mm_A/(m+m_A)²; detectability requires surface energy degrading to no less than
  E_min = E_th(m+m_T)²/(4mm_T) on Si.
- **Fixed brackets:** v₀ ∈ {220, 340, 540} km/s; E_th ∈ {10, 100, 1000} eV; media: full
  atmosphere (1013 g/cm², Ā=14.5) + standard rock (Ā=22) at four site classes — surface,
  MINOS-depth (225 mwe), LSM (4800 mwe), SNOLAB (6010 mwe). Floors bracketed
  **four decades wide** [1e-42, 1e-38] cm² (published-class order at ~3 GeV) so the window
  verdict cannot depend on floor precision.
- **Outcomes graded as written:** (i) non-empty window at every listed site class →
  conditionality NARROWS to "σ_dimer lands in the computed window"; (ii) windows only at
  some classes → conditionality restated with the honest experiment list; (iii) no window
  anywhere → F-DM3-4 deactivation path, papers revised before the 20th.
- **Verify (3):** ceiling monotone in depth; surface ceiling in the published 1e-28-class
  order (Mahdawi–Farrar-type surface analyses); window ≥ 2 decades at the WORST-case floor.

## Result (code/2365_overburden_ceiling.py + 2365_results.json; verify 3/3)
| Site class | σₙ ceiling (central) | bracket range |
|---|---|---|
| surface (atm only) | 6.7e-29 cm² | [1.7e-29, 1.8e-28] |
| MINOS-depth (225 mwe) | 2.3e-30 | [5.8e-31, 6.3e-30] |
| LSM (4800 mwe) | 1.1e-31 | [2.8e-32, 3.1e-31] |
| SNOLAB (6010 mwe) | 8.9e-32 | [2.2e-32, 2.4e-31] |

Against the worst-case floor (1e-38): the deepest site's most-hurting ceiling (2.2e-32)
still leaves **~6.3 decades** of open window. **OUTCOME (i) FIRES** — a visibility window
exists at every listed site class; robust to the full floor bracket, both v₀ and E_th
brackets, and the hurting-direction coherence convention.

## Structural point (stated, Stage-2 relevant)
Above the deep ceilings the MINOS-depth and surface windows extend to ~1e-30–1e-28; above
those, XQC-class instruments — **overburden-free, and F5's own validated machinery** — cover
the ultra-strong regime. The only regions where the species could hide from everything are
the computed **gaps** between one class's ceiling and the next-shallower class's floor;
whether σ_dimer lands in a gap is precisely a Stage-2 statement (it requires the model-side
number AND pinned per-experiment floors, not ceilings).

## Residuals (stated, not hidden)
CSDA vs full MC transport is an O(1)-class estimator (Emken–Kouvaris) — ceilings are
order-of-magnitude, adequate for a ≥6-decade verdict, not for a gap-edge verdict; mean-Ā
single-species media; coherent-SI for a composite is a convention (the hurting one), the
dimer's actual form factor is Stage-2; floors are class-brackets, not current curves.

## Consequence executed (per outcome (i), this patch)
Both papers' F-DM3-4 conditionality narrowed: from "conditional on an uncomputed ceiling"
to "conditional on σ_dimer (Stage 2, owed) landing in the computed window." Clause 1 exit
(d) untouched (fires on a null at computed-visible abundance — Stage 2 supplies "computed").
Stage 2 registered as the sole remaining gate to F-DM3-4 activation.

# The e-fold budget audit — forced by the founder's edge question. Two findings: the e-fold total is a function of the GP resolution ALONE (which corrects 3816's claim that the resolution enters no prediction), and the re-grounded count falls ~10 e-folds short of inflating the ball to the observable universe

**Patch 3823, Session 171, 9 Sep 2026. Lane: EU.** Prompted by `charge_mix_and_edge_assessment.md` §3 (the founder's edge picture, 3822). Verify `scripts/3823_efold_budget_audit.py` (6/6). Reasoning `reasoning/3823_efold_budget.md`. **This is a tension registered against the corpus's own re-grounded count, not against the founder's picture.** Nothing minted; PRED-C-96's tilt untouched (see §5).

## §1 The question
The founder nominates the ball's edge as the largest seed of asymmetry. An edge has a location. If the pre-ignition ball is the whole universe, then wherever the edge is today, the observable universe must sit *inside* it — otherwise the edge is a visible boundary, and no such boundary is observed. So: where is it?

## §2 Finding 1 — the e-fold total is set by the GP resolution alone (verify T1)
The re-grounded count (3816 §3) is N = ⅓ ln N_CP − ln(R_init/l_P). The re-grounding also carries a packing requirement: N_CP/12 addresses must fit inside the ball at GP spacing s, i.e. N_CP = 12·(4π/3)(R_init/s)³. Substituting:

> **N = ln(l_P / s) + ⅓ ln(50.27) = ln(l_P/s) + 1.306.**

R_init and N_CP both drop out. Verified as an identity at R_init/l_P = 1, 10⁻³, 2.75×10⁻⁵, 10⁻⁸.

**This corrects 3816.** That patch stated the hierarchy requirement was "a consistency condition, not an input to any prediction," and claimed 0736's rule ("the resolution enters no prediction formula") survives. Under packing closure it does not: the sub-Planck GP resolution is the *only* free quantity setting the e-fold total, and the e-fold total is what the pivot N_rem = 57 must sit inside. The correction is mine, from two patches ago, and is owed to the re-grounding document and to EU-1's next V1.x note.

## §3 Finding 2 — the budget falls ~10 e-folds short (verify T2, T3, T4)
Assuming a standard post-inflation thermal history (instantaneous reheating, entropy conservation, g_* = 106.75 → 3.91) and taking H at the tensor-line ceiling 4.7×10¹³ GeV — the **most favourable** case, since lower H means lower T_reh and a *larger* requirement (verify T5):

| quantity | value |
|---|---|
| T_reh | 5.8×10¹⁵ GeV |
| a₀/a_end | 7.4×10²⁸ |
| e-folds required for the ball ⊇ observable universe | **≈ 75.0** |
| e-folds delivered at N_CP = 10⁸⁴, R_init = l_P (3816) | **64.5** |
| **shortfall** | **≈ 10.5** |

Equivalently: at 64.5 e-folds the *entire* ball today is **0.39 Mpc** across, against an observable universe of ~14,260 Mpc — inside by a factor 3.6×10⁴ in radius. The universe would be five orders smaller than what we see.

The 10.5 e-folds are not mysterious. Standard inflation starts from a Hubble-sized patch; at H = 4.7×10¹³ GeV that is ~5×10⁴ l_P. Starting instead from one Planck length costs exactly ln(5×10⁴) ≈ 10.8 e-folds. **The shortfall is the price of the small-ball reading**, and it appeared the moment someone asked where the edge is.

## §4 What could close it (none adopted; PD-007)
By §2 the only lever is resolution: N ≥ 75 requires **s ≤ 1.0×10⁻³² l_P**, i.e. **≥ ~10³² GPs per l_P linearly**. Against this:
- The glossary's (explicitly unverified) "~10³⁰ GPs per l_P" gives N = **70.4** — still 4.6 short.
- 3816 computed the packing requirement as ≳ 3×10²⁷ per l_P and called it comfortably satisfied. It is satisfied *for holding the CPs*; it is **not** sufficient for the e-fold budget, which needs ~10⁵ times finer. 3816 checked the wrong bound.

Routes, in order of how much they cost:
1. **A finer hierarchy.** Needs ≥ 10³² GPs per l_P. Cheapest if the nested-600-cell construction delivers it; the estimate it must beat is itself unverified, so this may be free — or may not exist.
2. **VSL.** EU-1's background is explicitly FRW/**VSL**, and §3's arithmetic assumes a standard post-inflation history with a fixed c. A varying signal speed changes the horizon integral and is the one CPP-specific escape that could alter the requirement rather than the supply. **This is the most likely resolution and the corpus has not computed it.** It is named here as the first thing to check.
3. **A non-standard thermal history.** Lower reheating makes it worse (T5); only an exotic history helps, and none is on file.
4. **The ball is not the whole universe.** Would dissolve the problem and the founder's edge with it. Not the founder's picture; recorded for completeness only.

## §5 Honest scope
- **The tilt is untouched.** n_s = 1 − 2/N_rem depends on the pivot's *remaining* e-folds, adopted at 57. Nothing here changes the shape of the count law. PRED-C-96 stands exactly as it did.
- **What is in tension is the count's total**, and therefore whether N_rem = 57 sits inside a window that also reaches the observable universe. At N = 64.5 the pivot fits the window but the window does not fit the sky.
- **This is a registered tension, not a falsification.** Route 2 is uncomputed and could remove it outright.
- **It is the corpus's problem, not the founder's picture's.** The edge question exposed it; the small-ball ruling and the re-grounded count own it.

## §6 Registration
> **OPEN-EU-EFOLD-BUDGET-1.** Does the CPP inflationary window reach the observable universe? Under packing closure N = ln(l_P/s) + 1.31, so the question is equivalent to: is the sub-Planck GP resolution ≥ ~10³² per l_P, or does the VSL background change the horizon requirement below 75 e-folds? Pass line: **N_total ≥ N_required, with N_rem = 57 inside it.** Blocks: nothing computationally, but it conditions the re-grounded count (3816) and the edge candidate C-2 (3822). First action: compute the horizon requirement in EU-1's own VSL background rather than in a fixed-c background. Owner: EU lane. Not a founder question — a derivation.

Owed edits: `occupancy_regrounding.md` §2 (resolution is an input, not merely a consistency condition); EU-1 V1.x note (the e-fold total's dependence on resolution; the budget tension). Neither made at this patch.

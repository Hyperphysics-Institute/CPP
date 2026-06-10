# qDP saturation EoS + σ/m window — first-pass: the eDP buffer that prevents the glueball is the coat that sets the cross-section

**Patch:** 0830 (Session 156, 10 June 2026) · **Type:** first-pass computation / scaffold (NOT a closure, rests on estimates) · **Lane:** DM-2 / `dark_matter/`.
**Executes:** the "version worth building" from the DM accretion-era map (speculation folder, 0829, Era 2) — taking the founder's qDP/eDP buffering mechanism past speculation. **Directly addresses Step-1 open problem #2** (the residual van-der-Waals-like color potential between neutral qDP/hTetra structures, previously not computed). **Verify:** `code/0830_qdp_saturation_sigma_window.py`.

---

## The setup

The founder's mechanism (qDP color chaining + eDP coating preventing collapse) is, structurally, a **saturation**: residual-color attraction pulls qDPs together, the eDP coat supplies a short-range excluded-volume hard core, and the medium balances at a finite density rather than collapsing to a glueball. Step-1 already flagged the governing object — *"the residual (van-der-Waals-like) color potential between neutral structures, not yet computed"* — and noted it is the one thing that could lift σ/m. **The key realisation: the same residual potential governs both the glueball-avoidance and σ/m.** One coat, two constraints.

CPP scales used (from `DP_sea_and_cage_composition.tex`): `E_eDP=88, E_hDP=152, E_qDP=264 MeV` (the `E_qDP = 3·E_eDP` color factor), Compton ranges `λ = ℏc/E` → `λ_eDP=2.24, λ_hDP=1.30, λ_qDP=0.75 fm`; `m_qDP ≈ 0.30 GeV` (Step-1 light/worst-case estimate, **not derived**).

Two scales carry it: `r_qDP` (bare color size → **confinement/glueball** onset when bare cores overlap) and `r_c` (eDP-**coated** hard-core radius → **saturation** density *and* scattering size).
- `ρ_confine = 1/[(4π/3) r_qDP³]` (bare close-pack ≈ deconfinement)
- `ρ_sat = f_pack/[(4π/3) r_c³]` (coated random-close-pack — the core density)
- `σ/m = 4π r_c² / m_qDP` (hard-sphere, **assuming no near-threshold resonance**)

## Result

| r_c [fm] | ρ_sat (fm⁻³) | conf/sat | σ/m (cm²/g) | glueball | SIDM |
|---|---|---|---|---|---|
| 0.75 (=r_qDP) | 0.362 | 1.6 | 0.13 | OK | OK |
| 1.30 (**hDP coat**) | 0.070 | 8.2 | 0.40 | OK | OK (×2.5 margin) |
| 1.87 | 0.023 | 24.5 | 0.82 | OK | OK |
| 2.05 | 0.018 | 32.2 | 0.99 | OK | edge |
| 2.24 (**eDP coat**) | 0.014 | 42.1 | 1.18 | OK | **OVER** |

**Window (m=0.30 GeV): `r_c ∈ (0.75, 2.06) fm` — non-empty.** Glueball floor (any coat beats bare overlap) to SIDM ceiling.

Three readings:
1. **Glueball-avoidance is robust.** Any eDP coat (`r_c > r_qDP`) drops `ρ_sat` below `ρ_confine` by `(r_c/r_qDP)³/f_pack` — the core saturates at coated-close-pack and never reaches bare overlap. This is the founder's "eDP buffering prevents glue-balling," made quantitative. The collider fact (glueballs only at high energy) is the saturation barrier overcome only above threshold.
2. **σ/m is the binding constraint, and it is the same coat.** The coat that buffers the glueball is the coat that sets the scattering size — more coat = safer glueball but larger σ/m. This is exactly the era-map Era-1+2 window, now a number. Note this *replaces* Step-1's bare-geometric `4×10⁻³ cm²/g` (252× below) with the coated value, which is ~10²× larger and **near the SIDM bound** — the realisation of Step-1's "residual potential could lift σ/m" caution.
3. **CPP-natural placement.** An hDP-scale coat (1.30 fm) sits inside with ×2.5 SIDM margin; a full eDP-Compton coat (2.24 fm) sits just over. A heavier constituent (hTetra 1.5 GeV) widens the ceiling to `r_c < 4.6 fm` (σ/m ∝ 1/m) — all DP coats fit.

## What this establishes, and what it rests on

**Establishes (first-pass):** the founder's buffering mechanism is *quantitatively coherent* — there is a non-empty window in which the eDP coat saturates the qDP core below the glueball threshold while keeping the structure collisionless, and CPP's own DP scales land in or near it. The glueball-avoidance is robust; the collisionless-ness is tight and is the real constraint.

**Rests on (the firm-up path, all flagged):**
- **(a) `m_qDP`** — the 0.30 GeV light estimate (Step-1 open #1); heavier opens the window wide. The single most important number to derive (c04 ZBW + qCP cage).
- **(b) the coat scale `r_c`** — which DP length sets the eDP coating thickness (hDP vs eDP Compton) decides inside-vs-edge. Needs the actual eDP-screening profile around a qDP.
- **(c) no near-threshold bound state** — a resonance in the residual potential sends the scattering length large and σ/m up by ~10³ (Step-1's stated kill-condition). The residual color potential must be computed and shown *off*-resonance. This is the next real calculation (the energetic EoS: attraction depth + hard core → binding and the E/N minimum, replacing the geometric ρ_sat).

## Scope

First-pass / scaffold. **Not a closure, not a verdict, no THEO/ID.** Geometric saturation + hard-sphere σ/m; the energetic residual-potential EoS (attraction depth, no-resonance check) is the next layer. Sits in the hybrid (gravity drives the diffuse halo; this sets the dense core / micro-saturation). Conditional on the qDP/hTetra-DM conjecture and the Mechanism-A measure. Executes era-map (0829) Era-2; firms Step-1 open #2.

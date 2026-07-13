# OPEN-DM-FLOQUET-1 — R1 scoping: the geometry-#3 driven-equilibrium problem, and the branch-dependent ε map

**Patch 2441, 12 July 2026 (Opus, DM lane).** Scoping for R1 (the first Required Element of OPEN-DM-FLOQUET-1).
**Status: OPEN-DM-FLOQUET-1 still OPEN; candidate (B) UNRESOLVED.** This note sets up the R1 solve and sizes where
the method-(a) stability window is reachable. It does **not** solve R1 — it pins the problem and the two decisive
sub-questions. Verify script: `code/2441_r1_eps_scale_estimate.py`. Reasoning: `reasoning/2441.md`.

## 1. The R1 problem (what "driven equilibrium" means here)
Solve geometry #3 self-consistently for the lattice-stabilized separations where the **secular (time-averaged)
force vanishes** under ZBW + charge-switching, then read off the three quantities method (a) requires:
- **ε = (ω_A/ω_sw)²** — the ratio of the transverse bond-oscillation frequency ω_A = √(A/m) to the charge-switching
  frequency ω_sw. Method (a) (Patch 2440) showed the δ=3/7 mode is parametrically stabilized only for **ε ∈ [0.179,
  0.428]**; outside it, unstable.
- **dynamical δ** — the residence-time duty cycle (R2). The 3/7 is the uniform-sampling **upper** bound (G5).
- **branch asymmetry ε_att/ε_rep** — from the attractive vs repulsive equilibrium separations (feeds method (a)'s R6
  lever: a weaker attractive phase strengthens stabilization).

R1 satisfies **G3** (evaluation at |secular force| ≈ 0), which 2430/2434 violated.

## 2. In-hand inputs (from the repo)
- **d = 1.15 fm** uniform axial spacing (E_qq-set) [reasoning/2434]; **r_q = d/√2**; R_e > r_q, R_e-insensitive to
  leading order.
- **k_rep = 2·E_bond/s²** (Coulomb-like bond curvature); **A = k_rep** is the transverse stiffness magnitude.
- **Branch factor α_s/α ≈ 53** between **E_qq** (deep core, α_s-set, ~tens of MeV) and **E_ee** (shallow coat,
  registered ≈ 490 keV) [2424/2434].
- **Charge-switching = "the SU(3)-type ZBW hop"** [reasoning/2435] → **ω_sw is a ZBW/Compton-scale frequency**,
  ℏω_sw ~ m c² of the hopping constituent (qDP ~ 264 MeV; eDP ~ 553 MeV from ƛ = 0.357 fm [1814]).
- Registered targets: κ_θ ≈ 169 keV, E_bond ≈ 490 keV, threshold κ_θ/E_bond ≳ 0.43 (κ_θ ≳ 211 keV) [2424].

## 3. The branch-dependent ε map (order-level, NOT the solve)
Taking ω_A = √(A/m) with A = 2E_bond/s² and ω_sw as the constituent Compton/ZBW-hop clock:

| bond branch | switch hop | ℏω_A [MeV] | ℏω_sw [MeV] | ε | vs window [0.18, 0.43] |
|---|---|---|---|---|---|
| deep core E_qq | qDP-hop | 121 | 264 | **0.211** | **IN-WINDOW** |
| deep core E_qq | eDP-hop | 121 | 553 | 0.048 | unstable (too fast) |
| shallow E_ee | qDP-hop | 7.2 | 264 | 7.5×10⁻⁴ | unstable (too fast) |
| shallow E_ee | eDP-hop | 7.2 | 553 | 1.7×10⁻⁴ | unstable (too fast) |

**The sign question is branch-dependent, with exactly one favorable corner:** deep E_qq core fragmentation +
qDP ZBW hop → ε ≈ 0.21, in the stability window. Every other corner is deep in the fast-switching unstable region.
The deep branch works because its ~120 MeV bond-oscillation frequency is comparable to the ~264 MeV qDP hop
(ω_sw/ω_A ≈ 2.2, inside the required [1.5, 2.4]); the shallow branch's ~7 MeV frequency is ~40–75× slower than the
hop, deep in the unstable regime.

## 4. Honest caveat (this is where the lane bites)
ε = 0.211 sits near the **lower edge** of the window and rests on order-level inputs — E_qq is a scale estimate, not
pinned. Sensitivity: E_qq = 40/50/66/80/100 MeV → ε = 0.13/0.16/0.21/0.26/0.32, i.e. ±30% in E_qq spans unstable ↔
comfortably in-window. **The favorable corner is PLAUSIBLE, not established.** It is explicitly not being called
survival — that would repeat the 2434 move of seizing the favorable sub-case. What it does is tell R1 exactly what to
pin.

## 5. The two decisive R1 sub-questions (both DERIVED, not assumed)
1. **R6/G6 — which bond fragments, deep E_qq core or shallow E_ee coat?** Only the deep-core branch is even in the
   stability window, so this is the single most decisive unknown. Per R6/G6 it must be **derived from the
   fragmentation coordinate**, not selected. (2424 used E_ee; 2434 used E_qq without justification — R1 settles it.)
2. **What sets the effective ω_sw** — the qDP hop (favorable), the eDP hop (unstable), or a slower
   residence-suppressed rate? Is the switching Compton-fast, or duty-cycle-suppressed to a lower effective frequency?
   This couples to the dynamical δ (R2).

**R5/G4 still looms behind both:** even in the favorable corner (ε in-window, K_switch ~0.12·A stabilized), K_switch
must be netted against the recomputed geometry-#3 ponderomotive tensor (2430 analog: −190 transverse eigenvalue on
the superseded geometry). A positive in-window K_switch can still be overturned by a strongly-negative geom-#3
transverse ponderomotive eigenvalue.

## 6. Method for the full R1 solve (next focused run)
Self-consistent variational / reduced force-balance for (r_q, R_e, d) at |secular force| ≈ 0 under the ZBW +
charge-switching SSV potential: (i) derive the fragmentation branch from the coordinate (R6); (ii) pin E_qq (and s)
at that branch; (iii) derive the effective ω_sw from the hop residence times (R2/δ), not the bare Compton clock;
(iv) evaluate ε and place it against the [0.18, 0.43] window; (v) hand the result to R5 (recompute + net the
ponderomotive tensor). Decision rule (scoping §5) unchanged; Ω_DM parked throughout.

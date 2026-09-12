# OPEN-DM-PAIRING-KINETICS-1 — the residue computation (transition_graph §3), performed — **D1′ answered (R₊/R₋ = 1 exactly); D1 reduces to one terminal condition the corpus does not register, and the framework says what it is.** On the engine's own H ∝ N_rem carried to its end, p → 0 (outside the band); constant H gives p = 1 exactly (outside); every value between, including the band, is reached by where the count law's dilution *stops* relative to n̄ = 1. **C-5 stays conditional under the charter's band rule. Not a pass, not a kill.**

**Patch 3512, 12 Sep 2026. DM block, from this window under PD-006.** Spec: `kinetics1_transition_graph.md` §3. Charter readings: `OPEN-DM-PAIRING-KINETICS-1_charter.md` §5. Verify `code/3512_residue_computation.py` (10/10). Reasoning `reasoning/3512.md`. **No constant minted; no rate fitted; the band was not touched; H never A_s-normalised** (M_piv, the Moments per e-fold at the pivot, is carried as a parameter and scanned). Wording: C-5 conditional pass; nothing reported as working; no number retracted.

## §1 The model, with every choice named
The founder's chain (3509, 3510) is taken literally, with no cross-section:

| element | rule | source | status |
|---|---|---|---|
| step | one Moment | charter §3 | registered |
| hop | every free qCP hops every Moment | 3509 (no cohesion) | registered |
| landing | Poisson: a GP receives Poisson(λ) opposite-sign and Poisson(λ) same-sign free qCPs, λ = per-GP occupancy of the free q-pool, one sign | charter §3 ("Poisson landing") | registered |
| pair | a qDP forms iff the landing set is exactly {+q, −q}: **K1(λ) = λe^{−2λ}** | 3509 (a crowd is an SCP, no cohesion) + 3510 (qDP = a + and a − landing together) | **[model]** — the crowd reading; K2 = λe^{−λ} (a third same-sign qCP does not spoil the pair) and K3 = 1 − e^{−λ} (any partner in any crowd pairs) run as sensitivity |
| bias | polarity-blind concentration factor g on λ, both signs | 3509 | **[model]** g ∈ {1, α_s/α = 2.70 (3902)} |
| depletion | the partner pool is the same species' other sign, depleted by the same fraction u | neutrality grounding (n₊ = n₋) | registered |
| dilution | ln n̄ = 3 N_rem (per-GP occupancy); the q-pool's share λ_dil = g·½·e^{δ}·e^{3N_rem}, δ = δ ln n_q the composition mode at fixed total | 3890, hengine driver statement, 3936 set-up (q = ½) | registered; **λ_end = ½ at the count law's end (n̄ = 1)** |
| expansion | **engine H = N_rem/(57·M_piv)** per Moment, i.e. H ∝ N_rem with M_piv Moments per e-fold at the pivot, scanned 1–10⁵ | charter §6 (H ∝ N_rem form, never A_s-normalised) | registered form; M_piv **carried, not chosen** |

Output: u = unpaired fraction of one sign; R = n_q u; p = d ln R/d ln n_q = 1 + d ln u/d ln n_q by finite difference in δ.

## §2 Results (verify T1–T10)
**(a) D1′ — both signs.** The + and − pools obey the same equation Moment by Moment: same λ, same kernel, same g (polarity-blind), same depletion. **R₊/R₋ = 1 exactly and composition-independent.** The asymmetry fraction a in n_B = a·R (3511) receives nothing from this framework; p is the residue exponent, as pre-registered.

**(b) Constant H ⇒ p = 1 exactly, at every dilution rate, depleted or not (T2).** The pool starts at λ ≫ 1 (no pairing in a crowd) and is swept through the O(1) window; with H constant the sweep is time-shift invariant, so the fraction paired cannot know n_q. **All sub-linearity comes from a falling H — ε = −d ln H/dN at the window.** Where the window is fully swept before the engine stalls, the denser region reaches it later, when H is smaller, and pairs longer: p < 1 (T5: 0.85 in a control). That is the founder's qualitative mechanism (3510 §1) with its sign and its cause.

**(c) The count law ends inside the pair window, with H → 0 (T3, T4).** ln n̄ = 3N_rem ends at one CP per GP; the q-pool is then at λ = ½ — for K1, exactly the kernel's peak — and the engine's H ∝ N_rem goes to zero there. Nothing on the engine dilutes the pool out of the window. Carried to its end, the engine pairs the pool down by two-body depletion (u falls without bound, logarithmically in N_rem) and **p → 0**: the standard two-body freeze, R ∝ 1/(rate ∝ n_q). At N_rem = 10⁻⁸, p = 0.11–0.20 across M_piv = 1–10⁴ and still falling. **On the engine alone the reading is OUTSIDE the band, on the p = 0 side.**

**(d) What terminates the dilution decides p (T6, T7).** If the engine's dilution stops at N_h (n̄_h = e^{3N_h}) and the pool is then frozen or diluted at any rate, p at corpus-scale M_piv = 10⁴–10⁵ runs: n̄_h = 20 → p ≈ 1.0; 2.5 → 0.85; 1.35 → 0.67; 1.09 → 0.6; 1.01–1.003 → **0.39–0.42 (in band)**; 1.0003 → 0.2–0.4; and → 0 as n̄_h → 1. The post-termination rate is irrelevant at these M_piv (T7): by then u ~ 10⁻⁷ and partners cannot be found. **The reading is a function of one thing the registered inputs do not contain: where, relative to n̄ = 1, the count law's dilution stops.** (At u ~ 10⁻⁷ the finite-difference p carries ±0.1 of integrator noise; the trend is not in doubt.)

**(e) Two model details the reading is hostage to (T9, T10).** Under K3 (any crowd pairs) the pool is consumed before the window opens (u ≲ 10⁻⁵, p < 0.2): **a residue exists only if a crowd does not bond** — the SCP-no-cohesion reading of 3509 is load-bearing, and 3510 Q4 (a high-SCP crowd pairs a bare qCP *off*) sits on the other side of it; the two must be reconciled by the epoch (Q4 is about step (d)). With the pool caught on the crowd side of the peak (n̄_h ≳ 2), the *sign* of p − 1 depends on whether a third qCP spoils the pair (K1: p ≈ 2, denser = more crowded = less paired; K2: p ≈ 0.86). The bias g = 2.70 moves p by O(0.4) in that regime only.

## §3 Reading against D1 and D1′ — taken once
- **D1′: R₊/R₋ = 1, composition-independent. Read.** p is the residue exponent; the D1 test is unchanged.
- **D1: not readable to a number from the registered inputs.** The framework returns p as a function of the terminal dilution condition, spanning p ≈ 0 (engine to its end) through the band (dilution stopping at n̄ within ~0.3–1% of 1) to p ≈ 1 (dilution stopping at n̄ ≳ 20, or constant H). Under charter §5 D1, "a p that is model-dependent across two admissible lock-in criteria is reported as a band, and C-5 stays conditional if the band straddles the edge." The two admissible criteria are the engine carried to its own stall (p → 0) and any termination of the count law's dilution before its stall (p from 0 to 1). The band straddles both edges. **C-5 stays conditional.** It is not declared dead: the engine's stall (H → 0 as N_rem → 0) is the engine switching off, not a registered dilution law for what follows (3892: "inflation ends at n̄ = 1"), and carrying it past its end would be a D-6 error. It is not declared passed: nothing in the corpus places the termination inside the band, and a termination chosen to land there would be post-hoc.

**The condition on C-5 is now sharper than "p ∈ [0.21, 0.48]":** the count law's dilution must stop — the pool must be frozen — when the per-GP occupancy is within roughly 1% of one CP per GP, with a crowd not bonding and a third qCP spoiling a pair; if instead dilution runs to the count law's end, everything pairs and C-5 fails on the p = 0 side; if it stops early (n̄ ≳ 2) it fails on the p = 1 side.

## §4 The physics-picture question this returns to the founder (PD-006: physics in pictures is his)
The count law dilutes the lattice until each GP holds about one CP. At that point a hopping +qCP still finds a −qCP on its landing GP about a third of the time, and the engine that drives the dilution has, by its own form, run down to nothing. **What happens next?** (i) Does the crowding keep falling — something else takes over the expansion at Planck kT — so that hops stop finding partners within a few Moments, and the residue freezes with the pool still at a fraction of a percent unpaired? Or (ii) does the pairing continue at that occupancy until the pool is used up? The framework says: (i) with the freeze at about one CP per GP gives the band; (ii) gives p ≈ 0 and C-5 dies; a freeze while the GPs still hold several CPs gives p ≈ 1 and C-5 dies. And one subsidiary picture question: when a +qCP and a −qCP land on a GP that also receives a third qCP, do the two still bond as a qDP, or is that a stack (an SCP) that does not?

## §5 Not done here (forward queue unchanged in order)
- D3 (paired population → dial x) and D4 (re-derived S3-M1 sinks): not attempted; both inherit the same terminal condition.
- D2 (U_q/n_γ): u at the termination is 10⁻² to 10⁻⁷ across the scan; no reading, and n_B = a·R puts the 10⁻⁹ largely in a in every case.
- The annihilation photon channel and the 17–23% composition contribution (3936 §4, 3511 flag ii): EU-side, after p exists.
- λ_end = ½ sitting at K1's peak is a coincidence of q = ½ with the exactly-a-pair kernel; not a result and not used.

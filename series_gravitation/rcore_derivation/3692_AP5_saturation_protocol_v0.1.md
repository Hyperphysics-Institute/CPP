# AP-5 v0.1 — the saturation protocol (PROPOSED definitional clause under A3′/AP-3): what a GP does when more arrives than it can act on. Drafted from the founder's four anchors; mapped line by line onto the constraints sheet; four items owed before a panel

**Patch 3692, Session 166, 8 Sep 2026.** Status: PROPOSAL v0.1, not enacted. Anchors: 3688 (amendment), 3689 (second level of processing), 3691 (lazy hierarchy), R-LAYER-REPOSITIONING-IN-CELL (this patch). Verify for the one computed item: `code/3692_icosahedral_cell_restoring_verify.py` (4/4). Reasoning `reasoning/3692.md`. Axiom count stays 9 under amendment accounting; AP-5 is a definitional clause, as AP-1–AP-4 are.

## §1 The clause (four definitions)
- **D1 — Activation (founder 3691).** A GP's layer-n register has capacity K_n per Moment. When its census D_n exceeds K_n, layer n+1 activates at that GP for that Moment and receives the overflow D_n − K_n as its own census; when D_n ≤ K_n, layer n+1 is inactive and has no state. No fixed depth: layers are demand-activated. *Working value:* the cap is the same fraction in each layer's own units — saturation at ⅔ of the layer's demand scale (A.1 of the sheet), so one constant of nature serves all layers.
- **D2 — What the copy moves (founder, this patch).** Layer n+1 is a copy of the PCD cycle acting on a new coordinate: the CP's position within the cell it occupies at layer n, at the next PSR scale down (l_P/2 → l_P/4 → …). Its rest point is the position determined by the layers above it. Layer 1 moves the CP on the lattice (gravity as derived); layer 2 and below reposition it within progressively tinier cells.
- **D3 — Relay is whole (THEO-PCD-SEA, CONV-043).** The imprint a GP stamps on its outgoing DI-bits is the full received content at every active layer — never the acted-on fraction. Truncation binds what a GP *does* at each layer, not what it *relays*.
- **D4 — Storage and conservation (founder 4 Sep, 3691; AP-4).** What layer n cannot act on is held by layer n+1's registers, never in the messenger (AP-4: a DI-bit is a static snapshot). Nothing is discarded at any depth; the hierarchy conserves all energy of the initial configuration. The stored pattern is the CPs' bounded motion within their cells, repositioned each Moment (R-CORE-STORES-AS-CP-VIBRATION).

## §2 What the clause explains directly (sheet lines discharged by the definitions)
| line | how |
|---|---|
| A.1 one cap | D1: ⅔ per layer in own units |
| A.2 nothing below the cap changes | D1: layer 2 inactive when D ≤ K — the exterior is layer-1 PCD, untouched |
| A.3 storage not in the messenger | D4 |
| A.4 the floor, no singularity | D2: layer 1 cannot move the CP further; layer 2 moves it only within its cell |
| BH.1 surface at lapse ½, static | D1 + D2 (layer-1 floor) |
| BH.2 wave relayed whole → GR's admittance at every ω, ℓ, m, χ | D3 (= SEA; 3675 T1, 3668 T3) |
| BH.3 no coherent return | D3 + the sea metric's horizon at v = 2 (3675 §2); GW250114 consistent (3683) |
| BH.5 energy gravitates at once | D4: the held content is in the demand field the exterior reads (it is *counted*, not acted on) |
| BH.6 non-thermal, information-preserving | D4: a bounded, repositioned pattern — no populated photon-emitting states unless the cell motion couples to the EM channel (owed, §4) |
| BH.8 lockstep, momentum conserved | D2: repositioning is relative to the layer above; layer-1 lockstep (3374) carries momentum |
| NS.5 flat core | D1: pinned layer-1 register ⇒ uniform lapse (3636's theorem) |
| NS.6 saturated matter shines | D1: only the *core* is at layer 2; the envelope is layer-1 matter and radiates normally |
| BB.2 release = reheating | D1 + D4: as compaction relaxes below the cap, layers deactivate from the bottom up and their held content returns to layer 1 |
| BB.4 uniform solution | D1: every GP in the same state above the cap |
| S.1, S.2 second threshold; termination | D1: demand-activated — no cap is ever "reached" by the hierarchy itself; depth is set by D/K |

## §3 What the clause makes computable (sheet lines that become numbers)
- **Depth.** Layers active at a point = the number of nested overflows. With equal K per layer, depth ≈ ⌈D/K⌉: ~1 in a heavy neutron-star core (D/K just above 1), 3 at the wave horizon (v = 2, D/K = 3), very deep at Planck density. With K scaling with the layer's PSR area, depth grows faster. *First computation.*
- **Stiffness (NS.2, NS.7, BH.4).** The cell motion of D2 under the 1/r² count law is **restoring but quintic** (3692 verify: F/δ⁵ ≈ −9.9, no linear term). A linear stiffness — required for a finite k₂ and for flat-core radial stability — must come from one of: (i) the layer-2 register's own cap (count-dependent response); (ii) the collective lockstep response of the saturated lattice (3374/3637: the c/2 sound speed *is* a bulk modulus); (iii) a fine-scale departure of the count law from 1/r². *Second computation; this is where the founder's "spring" is either derived or not.* The bound 3685 (k₂ ≤ 0.019 if fluid-stiff) stands as the target.
- **c/2ⁿ transmission (BH.7).** A copied shell-sum at scale l_P/2ⁿ transmits at c/2ⁿ. Layer 2 at c/2 reproduces the founder's ruling; deeper layers are slower. *Consequence to state, not yet tested.*
- **The tilt (BB.1).** Whether deep nesting at Planck density leaves n_s = 1 − 2/N* intact: the leading-order result depends on N_CP and homogeneity (BB.4 holds), so it should; *check owed.*

## §4 Owed before a panel (in order)
1. Depth arithmetic at v = 2 and at Planck density (cheap; fixes whether the horizon is a 3-layer object).
2. The linear stiffness (§3): derive or exclude from (i)–(iii); compare to the fluid-stiff bound and to flat-core stability (3636's whole question).
3. BH.6's coupling: does bounded cell motion couple to the EM channel? (If it does thermally, EHT's bound applies; if not, the dark surface is explained.) This is also OPEN-GR-SEA-SHELL-EMISSION-1.
4. BB.1 check under deep nesting.

## §5 Status of the earlier extensions under AP-5
THEO-PCD-SEA is D3 — absorbed. THEO-PCD-BUDGET's *register* law (v_eff = 2·cap − cap²/v) is a candidate for what D1 + D2 produce at layer 1 + layer 2 for the *clock*, to be re-derived from the clause rather than kept (its wave sector stays excluded, CONV-042). The founder's 5 Sep picture ("stiff putty, or putty and oscillation") is D2: oscillation within the cell.

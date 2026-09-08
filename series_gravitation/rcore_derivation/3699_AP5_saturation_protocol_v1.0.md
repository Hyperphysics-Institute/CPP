# AP-5 v1.0 — the saturation protocol, RATIFIED by the founder 8 Sep 2026 ("AP 5 v .5 ratified") after CONV-044 (ADMISSIBLE 5–0, FAITHFUL 4–0). Four definitions; D2 carries the lockstep clause; the rider stands: the definitions are ratified, the downstream claims are graded in §2 and owed in §4

**Patch 3699, Session 166, 8 Sep 2026** (text of the 3697 referral, unchanged in substance). Status: **RATIFIED — AP-5 v1.0, ENACTED** (`founders_voice/founder_ratification_AP5_saturation_protocol_2026-09-08.md`; `axiom-registry.md` A3′ row). Adjudication `series_gravitation/review/reviews-CONV-044.md`. Axiom count stays 9 under amendment accounting; AP-5 is a definitional clause under A3′/AP-3, as AP-1–AP-4 are. THEO-PCD-SEA is retired into D3.

## §1 The clause (v0.5)
**Scope.** What a GP does when the DI-bits arriving in one Moment exceed what it can act on. Below that threshold nothing in this clause is active and every prior result stands unchanged.

- **D1 — Activation.** A GP's layer-n register has capacity K_n per Moment. When its census D_n exceeds K_n, layer n + 1 activates at that GP for that Moment and receives the overflow D_n − K_n as its own census; when D_n ≤ K_n, layer n + 1 is inactive and has no state. Layers are demand-activated, with no fixed depth. The cap is the same fraction in each layer's own units — saturation at ⅔ of the layer's demand scale — so one constant serves all layers. *Constraint (derived, 3693):* layer capacities do not decrease geometrically with depth; otherwise the hierarchy could not hold a black hole's overflow and would have to discard, contradicting D4.
- **D2 — What the copy moves, and how.** Layer n + 1 is a copy of the PCD cycle acting on a new coordinate: the CP's position within the cell it occupies at layer n, at the next PSR scale down (l_P/2 → l_P/4 → …), from the rest point set by the layers above (founder: "an iterative repositioning of the CP from the position determined by the previous higher-level positionings"). **The copy inherits the layer above's lockstep: every CP in a cell is repositioned identically each Moment, so the two CPs of a DP move together and the DP's electromagnetic coordinates are not driven by the copy.** *(Clause added at CONV-044; DERIVED at 3701 for all V_i = 0 content — gravitational waves, the static state — by A3′'s irrep decomposition plus co-location; for EM content the copy separates the pair by construction → OPEN-GR-RCORE-ALBEDO-1.)*
- **D3 — Relay is whole.** The imprint a GP stamps on its outgoing DI-bits is the full received content at every active layer, never the acted-on fraction. Truncation binds what a GP does at each layer, not what it relays. (THEO-PCD-SEA, CONV-043, retired into this definition.)
- **D4 — Storage and conservation.** What layer n cannot act on is held in layer n + 1's registers, never in the messenger (AP-4). Nothing is discarded at any depth; the hierarchy conserves the energy of the initial configuration. The stored pattern is the CPs' bounded, lockstep motion within their cells, repositioned each Moment (R-CORE-STORES-AS-CP-VIBRATION).

## §1a Alignment with the ratified text (Copilot's D-5, delivered)
| definition | ratified text it sits under | status |
|---|---|---|
| D1 activation | A3′ definitional clause AP-3 (the GP protocol: "compute/hold/per-Moment refresh of SSV_abs and SSV_net from Perceive-stage arrivals"); the cap = lapse ½ via the ratified PSR law N = (1 − v/2)/(1 + v/2) (3634, R-CLOCK-RATE-IS-DISPLACEMENT, R-PSR-LAW-LOG) — not a new constant | **definitional**: AP-3 says what the GP does with its arrivals and is silent on excess; D1 supplies the excess rule |
| D2 displaced coordinate + lockstep (derived for V = 0, 3701) | A3′ C5 ("the GP→CP displacement instruction follows geodesics of the unique … assembled metric") — layer 1; D2 adds the within-cell coordinate for layers ≥ 2 and states lockstep (layer-1 lockstep: 3374) | **definitional** (coordinate); **stipulated pending derivation** (lockstep inheritance) |
| D3 relay whole | A3′ C3 ("the Compute step applies the same icosahedral PSR shell-sum to all packet components") and AP-4 (the imprint is a snapshot of the GP's computed registers) — the two readings CONV-043 found underdetermined; D3 fixes which | **definitional** (resolves an underdetermination; founder-confirmed as an amendment, 3688) |
| D4 storage/conservation | AP-4 ("static snapshot … reset per hop", no evolving DOF in the messenger) fixes where storage cannot be; D4 fixes where it is and that nothing is discarded | **definitional** (AP-4 + D1 do not entail it; CONV-044 T-6, 4–0) |
Depth arithmetic, the conservation theorem, the two local stiffness facts, the dark-surface structure, and the n_s clip are **derived** from D1–D4 (3693–3695) at the grades of §2; nothing else in AP-5 is asserted.

## §2 What the clause is recorded as having established (post-CONV-044 grading)
| item | status after the panel |
|---|---|
| Constraints sheet (3690), 24 lines | discharged by definition or by the derivations below; two numerical sharpenings outstanding |
| Conservation theorem (no shrinking capacities) | **VALID 4–0** — derived |
| Depth = ⌈1.5 v⌉ (2 in a heavy NS core, 3 at the wave horizon) | derived from D1 |
| Linear stiffness | **VALID-AT-LINEAR-ORDER-ONLY 3–1**: two local facts derived (zero linear shear from the count law's icosahedral Hessian; no compression below the floor); the promotion to an incompressible relativistic constitutive law under finite-wavelength strains is *not* established. **k₂(shell) ≤ k₂_incomp(3/8) = 0.0188 is a bound, not an equality.** |
| Heavy-pulsar (flat-core) stability | discharged via 3637 (needs cap rigidity, which the floor supplies) — stands |
| Dark surface | **sufficient conditional on D2's lockstep clause** (2–2 split, both execution seats requiring the clause, now stated); the residual inter-layer coupling into DP EM coordinates is the (l_P/λ)² channel sized at 3694 — its derivation owed. **Transient release is a signature:** wherever local demand crosses downward through a layer's cap (merger, tidal stripping) D1 releases stored content — PRED-O-41 candidate, uncomputed. |
| n_s = 1 − 2/N* | **STANDS 3–1**; the D1 clip (a saturated era gives n_s = 1, excluded 8σ → κ < κ_cap) is a consequence of D1 whose embedding in EU-1's H_eff chain, and the map f ~ c₁κ³ ↔ D/K, are owed |
| Headline prediction | **0 < Λ̃ ≲ 1.7** (3–1): a CPP black hole has a non-zero tidal response where GR's has none; the object's number (visible shell, inner boundary at v = 2, c_s ≤ c/2) is owed before "≈" is written |
| Economy | four definitions are the minimum (4–0): D3 is load-bearing, D4 not derivable from AP-4 + D1 |

## §3 Ratification rider (adopted verbatim from the CONV-044 standing objection, GPT)
"Ratifying the clause should not simultaneously ratify the stronger claims that NS stability, exact fluid Love response, black-surface f = 0, and the cosmological tilt check have all been derived. The amendment is admissible with the D2 lockstep clarification; the physics downstream remains open." The founder ratifies the four definitions; the table in §2 records exactly what is derived from them and what is owed.

## §4 Owed after ratification (in order)
1. ~~Lockstep inheritance~~ — DONE (3701) for V_i = 0; EM case → item 7.
2. The object's Λ̃ — BOUNDED at 3702 from the ringdown: shell mass μ ≲ 0.10 (GW150914) → 0 < Λ̃ ≲ 0.2; the number depends on the interior profile (item 3).
3. ~~Clock law~~ — DONE (3703): matter lapse flat at ½, sea lapse → 0 (bimetric derived); force reading DRAIN selected by the ringdown; T-7 numerology. Item 2 resolved by consequence: Λ̃ ≈ 0 (transit level).
4. The D1 clip embedded in EU-1's H_eff chain; f ↔ D/K map.
5. PRED-O-41: the transient release burst at a merger — magnitude and timescale.
6. The (l_P/λ)² inter-layer EM coupling, derived.
7. OPEN-GR-RCORE-ALBEDO-1: the surface's coherent EM re-radiation under driven, bounded DP motion (3701 §3).
8. **The saturated-core neutron star under DRAIN** (gravity × K/D in the core, not zero): re-derive the flat-core branch (3634–3637) and re-score NS.2–NS.5 and GR-2 §(iv). Most consequential open item.

## §5 Enacted on ratification (Patch 3699)
THEO-PCD-SEA retired into D3; GR-2 → V2.8 (next patch) (AP-5 as the working amendment; rows 5/6/7 restated; the GW250114 run-3 result; H-SURFACE-IMPEDANCE retired; the CONV-043 and CONV-044 standing objections verbatim); `predictions.md`: PRED-O-39 → null, PRED-O-40 → 0 < Λ̃ ≲ 1.7, PRED-O-41 candidate; `axiom-registry.md`: AP-5 entered under A3′ with its anchors.

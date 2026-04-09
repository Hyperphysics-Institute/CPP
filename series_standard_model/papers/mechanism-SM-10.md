# Mechanism — SM-10: First-Principles Quark Mass from FEM Chain Network Simulation

**Paper:** SM-10 v0.1 (9 April 2026, proposal)
**Series:** Standard Model

---

## 1. What SM-10 proposes

SM-10 proposes a finite element simulation to compute quark masses from first principles: place cage CPs at lattice positions, fill the interior with DP Sea, let every CP seek opposite-polarity targets to form chains, and sum total organised DPs × M₀ = predicted mass.

## 2. The chain network model

A caged quark consists of: a central qCP, V_opp opposite-polarity cage vertices (chain anchors), V_same same-polarity vertices (surface radiators), E_attr attractive cage edges (tangential chain sites), and the DP Sea filling the interior.

## 3. Chain formation algorithm

(1) Place central and cage CPs. (2) Fill interior with DP Sea at density ρ_Sea. (3) Each CP identifies nearest opposite-polarity unbound CP. (4) Form chain link (DP bond). (5) Newly organised CPs become sources for next round. (6) Terminate when no new links form.

## 4. Three bonding regions (emergent)

The simulation does NOT impose the three regions — they should emerge naturally: Region 1 (near centre): dense cross-linking. Region 2 (mid-cage): web mesh. Region 3 (near surface): surface-converging tangentials.

## 5. Surface blanket

Same-polarity vertices launch outward radials with tangential linking, identical to the up quark structure. This contributes additional organised DPs.

## 6. Mass calculation

M_q = M₀ × N_organised, where M₀ = m_e z/φ = 3.790 MeV and N_organised is the total count of DPs recruited into the chain network.

## 7. Success criteria

Compare DP count ratios directly to PDG mass ratios (NOT V^(7/3) ratios — this avoids circular validation): N_c/N_s = 13.6, N_b/N_s = 44.8, N_t/N_s = 1850.

---

*Document prepared by Thomas Lee Abshier ND and Claude Opus (Anthropic), 9 April 2026.*

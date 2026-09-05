# OPEN-GR-SATURATED-CORE-1 rung 2: the reading is DERIVED (pinned register ⇒ uniform lapse ⇒ no pressure gradient: P-PINNED-CORE-IS-FLAT is a theorem of two ratified premises, not a postulate), and realistic EOS put it in solar masses. Ordinary (TOV-branch) neutron stars end at **M_thr = 1.78 M☉** for both SLy and APR4 — nearly EOS-independent — 4σ below PSR J0740's 2.08 M☉. The flat-core branch CONTINUES the sequence from the threshold (not disconnected, as 3635's coarse scan suggested) up to 2.8–3.0 M☉ at R ≈ 13 km; a 2.08 M☉ flat-core star has R ≈ 11.2 km (NICER: 12.4 ± 1 km). Everything above 1.78 M☉ is a flat-core star, if the branch is stable — the radial-stability analysis is now the whole question

**Patch 3636, Session 162, 5 Sep 2026.** Verify `code/3636_saturated_core_realistic_eos_verify.py` (6/6). Reasoning `reasoning/3636.md`. No paper touched. CONV-042 held.

## §1 The derivation (answers 3634's picture question from the rules)
Two premises, both ratified:
- **P1** — the register is the lapse and the cap is lapse ½ (R-CLOCK-RATE-IS-DISPLACEMENT; R-PSR-LAW-LOG; R-FLOOR-REGISTER: the floor is a register-saturation limit).
- **P2** — matter's dynamics are the derived Einstein equations (OPEN-GR-FE-1 closed); their static limit is `dp/dr = −(ε + p) d(ln N)/dr`.

A pinned register is a uniform lapse; a uniform lapse has `d(ln N)/dr = 0`; so `dp/dr = 0` — checked symbolically for any ε(r), any EOS. Reading (b), "only the clocks are capped," needs a force that is not the lapse gradient; neither premise supplies one, and in P2 the lapse gradient *is* the force. **Reading (a) is forced:** the saturated core is at uniform pressure and density (the boundary values), the lattice flat, its count appearing to the envelope at the boundary — 3624's shell bookkeeping, pure GR. 3635's postulate is retired as a postulate and kept as a theorem: **THEO-PINNED-CORE-FLAT** (P1 + P2). The founder may still reject P1 or P2 by picture; the theorem then falls with its premise.

## §2 Realistic EOS (piecewise polytropes, Read et al. 2009 parametrisation; coefficients from recollection — flagged; K in p/c² units)
Transcription check: TOV maxima SLy 2.05 M☉ at 10.0 km, APR4 2.19 M☉ at 10.0 km — literature values.

| | SLy | APR4 |
|---|---|---|
| GR TOV maximum M, R | 2.05 M☉, 10.0 km | 2.19 M☉, 10.0 km |
| **threshold star (central lapse ½)**: M_thr, R_thr, C | **1.78 M☉**, 11.3 km, 0.23 | **1.79 M☉**, 11.1 km, 0.24 |
| M_thr / M_max^GR | 0.87 | 0.82 |
| flat-core branch maximum M, R, r_c | 2.96 M☉, 13.3 km, 11.4 km | 2.83 M☉, 12.7 km, 10.8 km |
| flat-core star at 2.08 M☉: R | ≈ 11.3 km | ≈ 11.2 km |

**M_thr = 1.78 M☉ for both** — the threshold is set by the lapse reaching ½, which the two EOS do at nearly the same mass. Against PSR J0740+6620 (2.08 ± 0.07 M☉): **+4.3σ / +4.2σ**. Under the derived reading, no ordinary (TOV-branch) neutron star can weigh 2.08 M☉ on these EOS; nor 2.01 (J0348) nor 1.9–1.97 (J1614).

## §3 The flat-core branch connects
For realistic EOS the branch is **not disconnected**: it starts at the threshold star (member at 1.82 M☉ with a 2.9 km core) and continues, with *decreasing* core pressure and *growing* core, up to 2.8–3.0 M☉ with the core filling ~85 % of the radius. 3635's "disconnected" was the coarse polytrope scan missing the join. So the CPP sequence is: TOV up to 1.78 M☉ → flat core grows → maximum near 2.9 M☉. **Every pulsar above 1.78 M☉ is a flat-core star**, if the branch is stable. A flat-core J0740 has R ≈ 11.2–11.3 km against NICER's 12.4 ± 1 km — 1.1σ; GW190814's 2.6 M☉ secondary would be a flat-core star, not a black hole.

## §4 Standing
- Two live, EOS-robust confrontations under P1 + P2: (i) **M_thr = 1.78 M☉** is the top of the ordinary branch; (ii) the heaviest pulsars are flat-core stars with radii ~11 km and a maximum near 2.9 M☉. Both stand or fall with the **radial stability of the flat-core branch** — the sequence has dM/dp_core < 0, which for TOV would mean instability but is not TOV (the core's count is not governed by p_c alone). **That analysis is the next rung and the whole question.** If the branch is unstable, CPP under P1 + P2 is contradicted by J0740 at 4σ; if stable, CPP predicts the 1.78 M☉ knee, ~11 km radii above it, and a ~2.9 M☉ maximum.
- Owed: the radial modes of the flat-core star (a shell-plus-envelope pulsation problem with the core boundary a free surface fixed by the register condition); the same numbers with published EOS tables in place of recalled coefficients; the tidal deformability of a flat-core 1.4 M☉? (no — 1.4 M☉ stars are TOV; the knee is at 1.78).
- No paper touched; no corpus claim; the theorem's premises are named so a picture can strike one. CONV-042 held.

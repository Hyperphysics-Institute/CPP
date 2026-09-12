# OPEN-DM-PAIRING-KINETICS-1 — charter: the CPP pairing/condensation kinetic framework (ex-NB-S3a-1), opened at pre-registration

**Registered:** Patch 3508, 11 Sep 2026 (DM block; written from an EU-lane window under PD-006 — recorded in `id_block_registry.md`, the 3426 precedent). **Status: OPEN at pre-registration — no rate computed, no reading taken.** Registry entry: `frontier_sectors/DMDE.md` (3938). To-do: `todolist.md` TODO-3938-DM. Queue: `future_projects.md` Project 00d. **Verify at open:** `code/3508_kinetics_charter_targets.py`. **Reasoning:** `reasoning/3508.md`.

## 1. Provenance and why it is opened now
NB-S3a-1 was named at S3a (17 Jul 2026, `relic1_s3a_uq_from_registered_anchors.md` §1): *"the CPP pairing/condensation kinetic framework (σv, rate equations vs expansion) is unregistered... Route α is closed for this campaign until that framework exists as its own registered project."* It then survived only in handovers. Registered 3938 when a second consumer appeared; chartered here because the founder chose it as the next development thread (11 Sep) and because its first step is a picture question, not a computation.

## 2. Consumers — three, stated so the framework is not built blind
| consumer | what it needs from this project | target it must hit |
|---|---|---|
| **S3a Route α** (DM) | U_q, the unpaired +qCP inventory at lock-in, from kinetics instead of back-solved | U_q/n_γ = 3η_B = (1.836 ± 0.012)×10⁻⁹ (Route β anchor, S3a §2) — **reproduce, not assume** |
| **OPEN-DM-RELIC-1 reopening contract** (DM) | the relic-epoch Sea composition dial x (NB-F-1), at declarative strength | reopens the 2526/2527/2529 apparatus; resolution is then T1 = n_ring/n_b = 0.4468 ± 0.0054 |
| **OPEN-EU-PHOTON-GENESIS-1** (EU, 3936–3937) | the exponent p in n_B ∝ n_q^p (local density scaling of the unpaired inventory) | **p ∈ [0.21, 0.48]** ⇒ C-5 passes adiabaticity; outside ⇒ C-5 dies |

## 3. What is already registered (inputs; D-3 done at open)
- **The chain (founder, 11 Sep, founders_voice (EU) `3934_photon_genesis_picture.md` §4):** qCPs evaporate from SCPs; a qCP landing on an occupied GP re-stacks and the re-formed SCP emits per GP (AP-4) and attracts q-dominant SCPs; an escapee bonds with a qCP into a qDP; qDPs react into heavier DP-entities.
- **The ordering skeleton (founders_vision §6c, 0672a):** eDP:qDP = 1:1 as an *equilibrium* lock; the hTetra sink with freeze-out ordering; super-additive binding (hTetra > 2× hDP) named as an assumption; the free-vs-bound 5:1 split flagged "a computable freeze-out claim, not a given." Equilibrium locks and kinetic freeze-out **must not be conflated** (0672a scope note).
- **S3-M1 (2520, founder):** n_b = U_q/3; paired feedstock → DM; retro-predictions that any kinetics must reproduce: hDP-B excess = 2n_b, clouds = n_b, U_q(consumed) = 3n_b, U_e(consumed) = 2n_b.
- **Hazard H1 (2520):** equilibrium readings are dead (suppressions e^(−30) to e^(−10⁴)); **only frozen-inventory kinetics survive.**
- **The epoch anchor:** kT_form(L=16) ∈ [10.2, 17.0] MeV (2542, founder-ratified 2543; the earlier 16.5 keV is RETIRED — do not use).
- **Regime facts from the EU lane:** re-stacking-dominated limit f ~ 1/A holds to the last 1–3 e-folds (3910); Q–Q pairs at α_s(M_Pl) = 0.0197, Q–E and E–E at α (3902, derived from charge content); per-CP energy into the bath ≲ 10⁶ GeV (3808 swarm bound); the count law and n̄-as-occupancy (3890).
- **DM unit pinned:** ring 11.26 GeV = 8 × 1.408 GeV elements, 64 qCP + 64 eCP (RELIC-1 charter §1).

## 4. What is NOT registered (the project's content)
(a) the probability that an evaporated qCP lands on an occupied GP (re-stack) versus a free one (escape); (b) pairing cross-sections/rates for q+q, q+e, e+e against the expansion rate; (c) the aggregation/lock-in criterion — what stops the chain and freezes the inventories; (d) the epoch at which each step runs (during the evaporation phase of inflation, at reheating, or at the MeV bend-close) and whether the chain is one process or two; (e) whether escapees pair with the first partner met or by affinity (3902 asymmetry) and by charge sign; (f) what shields a bare +qCP from pairing long enough to be captured as a quark on an hTetra scaffold (the S3-M1 competition).

## 5. Pre-registered deliverables and readings (committed before any computation)
- **D1 — p.** Reading: p ∈ [0.21, 0.48] → C-5 adiabaticity PASSES (condition discharged; C-5 status moves from conditional only by this route). p outside the band → **C-5 dies**, recorded by name and number; the EU lane's amplitude sector then has no live candidate. A p that is model-dependent across two admissible lock-in criteria is reported as a *band*, and C-5 stays conditional if the band straddles the edge.
- **D2 — U_q/n_γ.** Reading: reproduces 3η_B within the propagated window → Route α CLOSED, Route β's anchor becomes a check; misses → the miss is reported with S3-M1's retro-predictions re-examined, not with the target moved.
- **D3 — x.** A declarative-strength value reopens OPEN-DM-RELIC-1 per its contract; a working value does not (D-6: working values are not determinations).
- **D4 — consistency.** The 2520 §2 retro-predictions are reproduced or the framework is wrong; this is a gate, not a result.

## 6. Discipline
- **PD-007:** no rate is a free constant. Every rate is derived from registered geometry and couplings (α, α_s, lattice step, the Moment, AP-4 emission) or carried as a flagged working extension [PCD-EXT] and never fitted to D1–D3.
- **Anti-post-hoc:** the targets (the p-band, 3η_B, T1) are stated here; readings are taken once, in this order, with the propagated window, and a band that "conveniently" lands is reported as one chain (3902 §5 rule).
- **Circularity:** the expansion rate the rates compete against must not be A_s-normalised if p feeds C-5 (3902 §4); use the engine's H ∝ N_rem form or the MeV-epoch H, whichever the epoch question in §7 selects, and say which.
- **D-7:** n̄ is occupancy (3890); "freeze-out" is not a corpus term for this chain — use the founder's words (evaporate / re-stack / escape / pair / aggregate); T_form is 2543's, not 2520's.
- **Epoch hazard:** if the chain runs at Planck-scale kT during evaporation, thermal suppression factors are O(1) and H1's e^(−30) does not apply; if it runs at the MeV bend-close, H1 applies in full. **The epoch question decides which regime the framework is in; it is asked before anything is computed.**

## 7. First step — four picture questions to the founder (no computation asked)
1. **Escape vs re-stack.** When a qCP evaporates from a stack, what decides whether it lands on an occupied GP? Is it a random hop on the lattice, or is it steered by the SSV gradient toward the nearest emitting stack (you said a re-formed SCP emits and attracts)? If steered, is escape the exception?
2. **When.** Does the whole chain run during the evaporation phase itself (kT near Planck, alongside the count law), or does evaporation only free the CPs and the pairing/aggregation run later, down to the MeV bend-close (2543)? One process or two?
3. **Who pairs with whom.** Does an escaped qCP bond with the first CP it meets, or does the q–q strong channel win the competition when both are present (3902)? Does charge sign matter to the first bond?
4. **Why a quark stays bare.** In S3-M1 a baryon takes three unpaired +qCPs. What keeps a +qCP unpaired long enough — does the hTetra scaffold capture it before a partner arrives, or does something in the stack's signal hold it?

Answers set the transition graph. Rates are written only after that.

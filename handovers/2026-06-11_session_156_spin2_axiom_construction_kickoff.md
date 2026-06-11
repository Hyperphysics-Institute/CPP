# Handover — The Spin-2 Axiom: constructing and justifying CPP's rank-2 (quadrupole) degree of freedom

**Arc:** Conscious Point Physics — foundations (a new axiom) with relativity-sector payoff (closes `op:einstein` (a) = GR-recovery, the tensor GW sector).
**Why now:** the `op_einstein_closure` arc (Patches 1107–1116) established **rigorously** that CPP's scalar+vector substrate cannot produce the helicity-±2 gravitational-wave polarizations — not by the linear map, not by superposition/bilinears (1115), and not as an emergent collective mode (1116: the scalar+vector lattice spectrum is helicity {0,0,±1} only, for any couplings). Matching observed gravity **requires a fundamental rank-2 degree of freedom.** This arc writes that axiom and justifies it.
**Date opened:** 11 June 2026 (Session 156). **Own window, own band, base_ref at start.**
**This is the highest-stakes kind of move in CPP — adding an axiom. Do it deliberately, with swarm review. This file is the durable record and the opening prompt; re-fetch from `handovers/` if context is lost.**

---

## KICKOFF LINE (paste to start)
```
Bootup for Conscious Point Physics (CPP). Clone the repo and read https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/bootup.md. Honor the line-1 CLONE-FIRST GATE before registering any ID, placing any file, or computing any coefficient. Then read handovers/, sort by filename, read the most recent dated file — then load THIS file: 2026-06-11_session_156_spin2_axiom_construction_kickoff.md.
```

## BLOCKING GATE (before anything)
1. Clone fresh; `git log --oneline | head -30`; **claim your own band** (record base_ref = HEAD).
2. Adding an axiom touches the axiom inventory and likely `theorem-registry.md`, `predictions.md`, `master_glossary.md`, `future_projects.md` — all **contested/Tier-A**. Run the anti-collision protocol (`templates/anticollision_protocol.md`); STOP-and-warn on those.
3. Read the §Required reading in order before drafting the axiom.

## KICKOFF SENTENCE
> *CPP's substrate transmits a scalar (`|SSV|_abs`) and a vector (`SSV_net`) — helicities 0 and ±1. The emergent-graviton calculation (1116) proved this is representationally too poor to carry the spin-2 (helicity-±2) tensor sector of gravity that GW observations confirm. The fix is a **symmetric traceless rank-2 degree of freedom `Q_ij`** (the l=2 quadrupole), which the 600-cell's H_g representation already has a geometric slot for and the rank-agnostic shell-sum already knows how to propagate. Your task: choose where `Q_ij` lives, write the axiom precisely, derive its source coupling to `T_μν`, show it closes GR-recovery, and justify it as principled rather than a convenience patch.*

## What is already established (do not re-derive — build on it)
- **(b)/(b′)** excess-sourcing / inert-uniform-Sea: conditionally closed, grounded in 600-cell symmetry (1107–1108). The CC local half is secure and independent of this axiom.
- **The d.o.f. is identified:** the l=2 quadrupole; the 600-cell H_g (l=2) representation is the slot (1112).
- **Propagation is free:** the icosahedral shell-sum is rank-agnostic → a broadcast `Q_ij` obeys `□Q_ij = source` at c, helicity-±2 part = the GW `+`/`×` modes (1113).
- **No existing d.o.f. supplies it** (1114) and **no emergent/collective mode does either** (1115–1116). So it must be **fundamental**.

## The construction tasks (the arc)
1. **Choose the flow.** Where does `Q_ij` live? — **A:** the CP State Register (a CP carries a rank-2 "shape"/quadrupolar attribute reported to its GP); **B:** the GP→GP LSP broadcast (a 5-component `Q_ij` channel beyond `|SSV|_abs`, `SSV_net`); **C:** the GP→CP instruction (a quadrupolar deformation beyond the displacement vector). Argue the choice from the PCD cycle and economy. (B is the natural home if the quadrupole is a *field* like the SSV; A if it is a property of matter/CPs; consider whether one induces the others.)
2. **Write the axiom precisely.** State the new primitive, its transformation (symmetric traceless rank-2 under the lattice point group, the H_g irrep), its dynamics (the shell-sum → `□Q_ij`), and its conservation/constraints. Keep the axiom minimal.
3. **Source coupling.** Derive `Q_ij ↔ T_μν`: the matter mass-quadrupole sources `Q_ij` so that the radiated field reproduces the **GR quadrupole formula** and `□h̄_μν = −16πG T_μν/c⁴` in the TT sector. This is the real GR-recovery payoff.
4. **Close `op:einstein` (a).** Show the extended (scalar+vector+tensor) metric map assembles into `G_μν = 8πG T_μν/c⁴`, recovering the tensor sector that 1109–1116 showed was missing.
5. **Swarm review (DG-3).** An axiom addition must go to ChatGPT/Copilot/Grok via CONV-001. The bar: is the axiom forced (not convenient), minimal, and free of double-counting with emergent spin (ZBW)?

## Justification — the "is it a convenience patch?" defense (carry this into the writeup)
The architect's standing concern is that a mono-motivated axiom looks like a patch. The honest status (surveyed Patch 1117 session):
- **Forced, not chosen:** observed GWs are tensor; a scalar+vector substrate provably cannot make them (1116). Physics dictates the bit.
- **Geometrically pre-slotted:** the 600-cell symmetry group already contains the l=2 (H_g) representation, currently **unused**. The axiom *activates existing substrate structure* rather than bolting on alien structure — the geometry predicted the seat.
- **Completes the fundamental-field spin ladder:** scalar (0), vector (1, the photon/SSV), tensor (2) as fundamental broadcasts, with spin-½ correctly emergent (ZBW orbital).
- **Does NOT double-count emergent spin:** fermion spin-½ (ZBW orbital, vector) and chirality (pseudoscalar/axial) are handled WITHOUT this bit — they are *not* additional motivations, and the axiom must not disturb them. Be explicit that `Q_ij` is the *radiative tensor field*, distinct from emergent orbital angular momentum.
- **Candidate SECOND motivation to TEST (would convert mono- → multi-motivation):** **tensor mesons / spin-2 hadrons** (e.g. f₂(1270)). Check whether CPP's strong sector can build a spin-2 hadron as an *orbital* L=2 state (emergent, no bit) or whether it hits the *same* representational wall. If the latter, that is an independent phenomenon demanding the same `Q_ij` — a strong, convergent justification. **Run this test as part of the arc.**

## Required reading (in order)
1. `series_relativity/op_einstein_closure/INDEX.md` + `spin2_construction/README.md` — the full arc and verdict.
2. `spin2_construction/1116_step5_emergent_graviton_verdict.md` (why fundamental) + `1112…l2_quadrupole` (the slot) + `1113…broadcast_law` (propagation).
3. `c07_weak_field_GR` (the LSP, CP State Register, metric map) + `c08_strong-field_GR` (the field equation, `op:einstein`).
4. The Spin companion paper (ZBW orbital spin-½) — to keep `Q_ij` distinct from emergent spin.
5. `founders_vision.md` — the 11 June 2026 entry (the architect's reasoning + the resolution).
6. SS-5/SS-6 (nuclear quadrupole moments — matter-side, for the tensor-meson test) and the strong-sector spin treatment.

## Falsifier / on-success
- **Falsifier:** if no minimal, non-double-counting axiom can be written that (i) yields exactly 2 helicity-±2 modes at c and (ii) reproduces the GR quadrupole formula without disturbing the recovered scalar/vector sectors — or if it cannot be made to source from `T_μν` consistently — then CPP's gravitational completion is in deeper trouble than a single axiom.
- **On success:** `op:einstein` (a) closes; the dark-sector cap is removed; the CC reconciliation (SR-5 ≡ SM-6) becomes an *unconditional* theorem; CPP reproduces the observed tensor GW polarizations; and CPP has a complete (scalar+vector+tensor) emergent metric.

## Scope / window / band
Foundations + relativity sector. Own window/band/base_ref. Touches contested registries (axiom inventory, `theorem-registry.md`, `predictions.md`, `master_glossary.md`) — STOP-and-warn, integrator-batched. The arc folder `series_relativity/op_einstein_closure/spin2_construction/` is the working home; the axiom itself, once written, belongs in the foundational axiom document (locate via the corpus, not assumed). Do not move any verdict until the axiom is swarm-reviewed and the architect signs off.

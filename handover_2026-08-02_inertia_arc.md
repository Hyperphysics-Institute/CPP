# HANDOVER — SESSION 16x, PATCHES 2873–2899 (30 Jul – 2 Aug 2026)

**Arc: the CPP inertia mechanism, from founder conjecture to a measured
cross-sector obstruction.**

---

## §0 — LEDGER (UNCHANGED ALL SESSION)

**1B OPEN · PR7 PARTIAL · six of seven · B7 holds DM-1/DM-2/DM-3 ·
Candidate (B) 79.5% PROVISIONAL-FAVORABLE**

**G1 and P-A2-1 STAND.** SF-6 v1.0 stands as shipped.
**Statics claims SUSPENDED** since Patch 2892 — see §4.

## §1 — THE ONE THING TO READ FIRST

**`flagship_papers/electromagnetism/sketches/b1_cross_sector_conflict.md`**
(Patch 2898). It states the arc's central open problem. Everything else is
support for it.

**The problem in three lines:**

1. CPP's primitive is **velocity-proportional**: d = (|SSV_net|/SSV_abs)·PSR.
   So SSV_net = 0 ⟹ the CP **stops**. Free motion must be actively
   sustained every Moment.
2. **Newton I therefore requires two EXACT conditions** — the drive exactly
   linear in v, and μ = PSR/SSV_abs exactly constant. Newtonian mechanics
   requires neither, because F = 0 ⟹ a = 0 gives free motion for nothing.
3. **Both fail, and both fail toward drag.** The drive carries β² curvature
   with c = 0.20129 (measured, model-independent, Patch 2897). PSR
   *contracts* with velocity per the SR sector where B1 needs it to *grow*
   (Patch 2898) — a **sign** conflict, not a magnitude mismatch.

## §2 — FOUNDER'S STANDING DIRECTION (Patch 2899, verbatim in founders_voice)

> *"Let's focus on finding a way to produce a constant SSV_net… I think all
> we need is to come up with a better understanding of the DI-bits and the
> production of SSV_net."*

**RULED OUT:** 2898 direction (B). The velocity-proportional primitive
stands; the 7 July no-carried-velocity ruling stands. **Do not attempt
Newton I by making displacement part of the CP's carried state.**

**LIVE:** 2898 directions (A) and (C), plus the founder's own.

- **(A) The drive model may be wrong.** Patch 2884 holds the Sea **static
  in the absolute frame**. A self-consistent treatment — arcs near a moving
  CP partially co-moving — could change the β² term. **Cheapest to test;
  recommended first.** *Caution recorded at 2898: this is also the option
  that would make the worker's own c = 0.201 an artifact. Do not pursue it
  harder than the others for that reason.*
- **(C) The SR sector's PSR needs re-derivation for inertial motion.** c05
  §254 identifies gravitational and inertial PSR contraction via the
  equivalence principle, **and that identification is what forces the
  sign.** A free-falling CP is *accelerating*; a coasting CP is not.
  Whether the identification survives for **uniform** motion is the
  load-bearing assumption.

**The founder's requirement (constant SSV_net) and the B1 measurement
(β² curvature) are in DIRECT CONTRADICTION. That is the problem to solve,
not to reconcile rhetorically.**

## §3 — WHAT CLOSED THIS SESSION

**CONJ-FP-1 registered** (2880) and twice revised. Now: round-trip timing
asymmetry as the sole mechanism; **ξ_arc ELIMINATED** — the effect is pure
kinematics, needs no arc geometry and no Sea density.

**Condition B CLOSED** (2895). Branch 1 — DI-bits as travelling conserved
entities — is ballistic (p = 1.0000), 1/r², isotropic, and **retarded by
construction**, so not Liénard–Wiechert.

**B1 EXECUTED** (2897), open since the SF-6 pin arc, twice returned 5–0
REASONED-UNVERIFIED because no panel seat can run code. **Scheduling
lesson: the item nobody else can do should go first, not last.**

**Founder's mechanism verified** (2896): addressed FCC routing gives
**perfect isotropy at the nearest-neighbour shell (CV 0.014)** — the scale
the inertia mechanism operates at. Perfect isotropy is impossible on a
lattice (floor measured at 2897); routing sits within ~3× of it.

## §4 — SUSPENDED / WITHDRAWN — DO NOT BUILD ON THESE

| item | status | patch |
|---|---|---|
| 2890 static-slope column ("essentially 1/r") | **WITHDRAWN** — per-voxel estimator artifact | 2891 |
| ALL statics slopes in the arc | **SUSPENDED** — background accumulates as a uniform component; longer runs make it worse | 2892 |
| 2887 "no light cone" | **WITHDRAWN** — finite kernel support; edge/t = 5.6569 exactly | 2890 |
| 2895 "lattice paths" row | **WITHDRAWN** — was the continuum row computed twice | 2896 |
| 2868 forward F_hold as evidence for the mechanism | **WITHDRAWN** — 2496 is a scalar wave field with no arcs | 2880 |
| F = κa as CPP substrate result | demoted 4–1 to scalar-toy | 2876/2879 |

**Before any statics claim:** subtract the spatial mean (fit the
*deviation* field, not |Q|), verify convergence at two box sizes, then fit.

## §5 — THE FAILURE MODE, NAMED FOUR TIMES

**A number landing near a physically expected value gets accepted without
interrogating the estimator that produced it.** Instances: c_lat misread as
a propagation speed (2887); "no light cone" asserted from half the evidence
(2890); −0.97 accepted because 1/r was expected (2891); shell-averaged
1/r² accepted although it cannot discriminate rays from a smooth field
(2895, caught).

**Related and equally persistent:** *inheriting from the arc rather than
the spec.* The engine (2893), then a parameter of the engine (2895) — the
second **after** the first was diagnosed. **Diagnosing a failure mode does
not inoculate against it.**

**Practical guard that worked:** cross-checking a new measurement against a
committed one. Every catch above came from two of the worker's own numbers
disagreeing.

## §6 — GOVERNANCE ADDED

**CONV-009** — founder verbatim captured in the same patch that acts on it;
verbatim is the primary source, derivatives cite it by path.
**CONV-010** — Tier 4 means the derivation, not a retrospective about it.
Stranger test: *could a competent stranger reconstruct the result from this
file alone?*
**OS §15.15 REPAIRED** (2883) — now checks conformance and founder
verbatim, and fires **incrementally** at §15.14 checkpoints, not only at
session close.

**§15.15 audit run at handover:** verify scripts complete for all 13
computational patches; four founder captures present; **five fragments were
missing (2881, 2882, 2883, 2885, 2888) and are backfilled at 2899, flagged
non-contemporaneous.** All five are governance or pre-registration patches —
the "feels clerical" failure mode, occurring a third time after being named
twice.

## §7 — OPEN ITEMS, PRIORITY ORDER

1. **The B1 obstruction** (§1–2). Direction (A) first.
2. **CONJ-FP-1 Condition A** — sign of the Sea's response. Repulsive →
   forward drive; attractive → drag. Untested.
3. **LINK 2** — the marginality condition C·PSR = SSV_abs. Never computed.
   May be forced by PSR's own definition; failure condition is
   C_coherent ≠ C_coast.
4. **Statics observable** — rebuild per §4 before any claim.
5. **Intermediate-radius routing anisotropy** — CV ≈ 0.2–0.4 vs a lattice
   floor of ~0.06–0.18. Partly lattice, partly not.
6. **The isotropy/speed trade-off** — diffuse routing buys isotropy and
   costs propagation speed (53 hops vs 21 minimum at β=1.5). What sets the
   re-radiation distribution is a founder-physics question.
7. **SF-8 §4** (bonded ZBW Sea) and the CONV-003 stdlib verifier, still owed
   on the paper thread.
8. **OPEN-PHASE-THRESH-1**, **OPEN-CALIB-COUNT-1**, **OPEN-FSELF-
   CORRESPONDENCE-1** — carried from before this session.

## §8 — KEY FILES

- `sketches/b1_cross_sector_conflict.md` — **the central problem**
- `sketches/b1_stability_analysis.md` — B1, the c = 0.20129 result
- `sketches/conj_fp_1_volume_transfer_inertia.md` — CONJ-FP-1 (revision banner at top)
- `sketches/tier4_derivation_record_inertia_arc.md` — full derivations, §§1–7
- `series_phenomena/cosmology/dark_matter/branch1_verification.md` — Condition B closure
- `series_phenomena/cosmology/dark_matter/addressed_routing_findings.md` — founder mechanism tested
- `series_phenomena/cosmology/dark_matter/SPEC_MISMATCH_shell_broadcast_vs_neighbour_relay.md` — why five patches tested the wrong model
- `founders_voice/` — five captures, 2026-08-01 and 2026-08-02
- `templates/operating_system.md` — §15.15 repaired

## §9 — PHYSICS NOTES FOR THE NEXT WORKER

- **c_lat is NOT a propagation speed** where the relay is diffusive; it is
  the one-hop kernel width.
- **Static Coulomb does not constrain relay dynamics.** Diffusion and
  ballistic propagation both give 1/r in steady state. G1 establishes the
  relay's **fixed point**, not its dynamics.
- **The c05 spec is a growing shell with Q/4πr² dilution** — ballistic,
  geometric. Every engine in this arc was a nearest-neighbour relay. **Read
  the spec, not the committed engine.**
- **Shell-averaged 1/r² is conservation + geometry alone** and cannot
  distinguish a smooth field from 12 rays. The discriminating observable is
  **angular isotropy across GPs at fixed radius** — a CP can only sit at a
  GP.
- **Emission must address the whole PSR shell**, not 12 neighbours. The ray
  problem was an implementation artifact, not a defect of the mechanism.

Bootup for Conscious Point Physics (CPP). Clone the repo and read the bootup file at https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/bootup.md. Honor the line-1 CLONE-FIRST GATE before registering any ID, placing any file, or computing any coefficient (clone the repo and grep the registry first). Then open the handovers/ folder, sort by filename, and read the most recent dated file (named YYYY-MM-DD_session_NNN_*.md) — that newest entry is the canonical "what's next" pointer. Note: the folder is handovers/ (plural) and there is no file named handover.md; never look for either — always use the newest dated entry.

---

# CHARTER — write DM-1 to ship: the qDP/hTetra dark-matter identification paper (800-series writing window)

**Date:** 24 June 2026. **Scope:** finish + ship DM-1. **Band:** **this charter is Patch 0847; the writing window draws 0848 onward (DM lane, 800-series).**
**Type:** forward task charter (not a session-close handover). **This is NOT a cold start** — the draft's
scientific core (§4–§7) is already written; the job is to fill the marked gaps, add figures + one specific
dwarf fit, and ship at the honest grade. **NO THEO unless earned; status moves to TLA; verify scripts ship
with any computation-bearing patch.**

## 0. BLOCKING CLONE GATE (line 1, always)

Before registering any ID, placing any file, or computing anything: clone the repo fresh and grep the
registry. `git clone https://github.com/Hyperphysics-Institute/CPP.git`. **This window owns the 800-series
DM band; 0800–0847 are CONSUMED (0800–0846 = DM arc Session 156; 0847 = this charter) — the next free number is 0848.** Grep `git log` for
the next free number before each use; consumed singletons stay consumed. All work lands in
`series_phenomena/cosmology/dark_matter/` — **no shared-registry or status-file edits without TLA.** Note a
live parallel window is running in the **2100–2149** band (Capture-and-Audit Protocol); stay in your lane.

## 1. Orientation (read this first)

The task is to take the existing draft `series_phenomena/cosmology/dark_matter/DM-1_draft_manuscript.md`
("scientific core largely written") to a finished, shippable paper. **DM-1 is an identification paper for
TLA's postulate that dark matter is charge-neutral qDP/hTetra aggregates** — residual neutral structures of
the Conscious-Point Dipole Sea, not a new particle. The paper's *headline positive content is already
derived*: a **velocity-independent self-interaction cross-section σ_V/m ≈ 0.20 cm²/g** that distinguishes
the candidate from both collisionless CDM (σ/m = 0) and light-mediator SIDM (σ/m ∝ v⁻⁴), with a falsifiable
signature (mild, flat dwarf cores ~0.1–0.3 kpc). The remaining work is *finishing*, not deriving: fill the
**[OPEN]/[TIGHTEN]/[TO FILL]** markers, add the V(r) + overlay figures, confront one or two *specific*
observed dwarfs, write the §1 non-CPP-reader primer, and state §8's calibrated inputs cleanly. **Ship at the
draft's own honest grade — "a viable, microphysically-derived, falsifiable SIDM candidate with a specific
qDP/hTetra signature, not yet a fully-derived identification."** First action: read the draft + the project
map end-to-end, then work the §11 checklist (§3 below). **DM-1 does NOT need OPEN-SR-9** (§4).

## 2. The postulate and where the five gates actually stand

**Postulate (CONJ-COSMO-1):** dark matter = charge-neutral (color-singlet, electrically neutral) qDP/hTetra
aggregates, constituent mass m_qDP ≈ 264 MeV (ratios derived; absolute scale calibrated, §8). What validates
it is the **DM-1 five-gate arc** (the kill-gauntlet), not DM-2 specifically — DM-2 is one sub-problem
(structure formation) inside it. Gate ledger (per TLA's framing, reconciled to the draft):

- **Step 1 (self-interaction cross-section):** PASSES — bare σ/m ~10⁻³ cm²/g, ~10²–10³× below the
  Bullet-Cluster bound. No SR-9.
- **Step 2 (abundance / sea-gravitation gate):** NO KILL. Its one real requirement — the *uniform* Sea stays
  cosmologically inert while its swirl-inhomogeneities gravitate — is gated on **OPEN-SR-5** (the
  cosmological-constant mechanism), **not** SR-9. This is the genuine open dependency for the *complete* DM
  picture (a different problem entirely); DM-1 cites it as conditional-but-traversed (§9 of the draft).
- **Step 3 (coldness):** PASSES by a wide margin, resting only on the GeV constituent mass. No SR-5/SR-9.
- **Step 4 (power spectrum) = OPEN-COSMO-DM-2:** SUBSTANTIALLY RESOLVED (Patch 2004) — the EU-1 VSL arc
  supplies the seeds (n_s = 0.9649), so CPP reproduces P(k). Its residual ledger R1–R4 has only one item
  touching SR-9 — R2 (the μ↔ε falsifier), at conditional-PASS, explicitly "not a live framework threat."
  **This is the only place SR-9 touches the DM story, and it is out of scope for DM-1.**
- **Step 5 (rotation curve):** PASSES, riding on c05 *local* gravity. No SR-9. *Non-discriminating* (§5).

**Honest read:** you can write DM-1 now without SR-9. The cheap-kill gates (1, 3, 5) establish
*compatibility* — a generic GeV CDM placeholder passes them identically — so the paper's weight rests on the
derived discriminant (§4–§7 of the draft), not the gates.

## 3. Attack strategy — finish the draft, ship the discriminant

The draft is the spine. Work its **§11 "what is left to fill" checklist**. Concretely:
1. **The positive case is the discriminant, not the gates.** Lead with §4 (residual two-gluon color
   van-der-Waals interaction, V₀ ≈ 53 MeV, λ ≈ 1.3 fm) → §5 (velocity-independent σ_V/m ≈ 0.20 cm²/g) → §6
   (mild flat dwarf cores) → §7 (the flatness is the two-sided falsifier). Keep §3 (the cheap-kill gates)
   *short* — they are the "did not die" admission bar, not the result.
2. **Fill the markers:** §1 [TO FILL] one-paragraph CPP-substrate primer for a non-CPP reader (DPs, the Sea,
   color-neutral residuals) + ~3 citations to the SM/SS flagships; §2 [TIGHTEN] state the DM-"unit" range
   used (single qDP vs hTetra vs aggregate); §4 [TO FILL] the V(r) + saturation-vs-confinement-density
   figure; §6 [TO FILL] confront one classical dSph + one LSB *quantitatively* (not the representative NFW
   only); §8 the two calibrated inputs (absolute mass scale → Project C; Ω_DM/Ω_b ≈ 5.36 → swirl amplitude,
   route B [OPEN]).
3. **Flag the two open dependencies honestly, in their own section:** sea-gravitation → **OPEN-SR-5**;
   falsifier-clean structure formation → **R2 / OPEN-SR-9** (out of scope, named). Plus the standing
   Mechanism-A condition (§4).
4. **State the grade plainly and do not inflate it past identification-grade.** §10's one-line grade is the
   target sentence.

## 4. Dependencies — and what is NOT a blocker

DM-1 ships **conditional**, exactly as the F.1 chirality results do. Its conditionals:
- **CONJ-COSMO-1** — the paper's *premise* (DM = qDP/hTetra), not a blocker; it is the subject.
- **Mechanism A** — a rate law posited in the F.1 DSL; discharge = **OPEN-FP-F1-2** (a hard Layer-4
  derivation, owned by the **900 chirality lane**). It is the *single shared residual* of the chirality and
  DM arcs — one derivation discharges it for both. **Not a blocker for shipping** (DM-1 ships conditional on
  it; it is an *upgrade*, not an *unblock*). Do **not** re-derive it in the DM lane.
- **DM-2 / Sea-gravitation → OPEN-SR-5** — the cosmological leg; A→D traversed twice, no kill, conditional;
  the open piece (Λ-suppression coefficient + horizon selection) overlaps the **1100 cosmological-constant
  window**. Cite as conditional-but-traversed; do not race 1100.
- **OPEN-SR-9 — NOT needed for DM-1.** It touches the DM story only through the out-of-scope Step-4 R2
  residual (a non-live-threat conditional-PASS). Do not gate this paper on it.

## 5. Candor guardrails (do not overclaim)

- The **rotation curve (Step 5) is GENERIC** to any collisionless halo — a consistency gate, **not** a
  discriminating win. Say so.
- **CPP's actual content** in this paper is: the *derived* velocity-independent discriminant (σ_V/m flat at
  ~0.20, the opposite of light-mediator SIDM), the *derived* G (c05, G = ℏc/m_P²), the *no-new-sector* halo
  (qDP/hTetra are already in the spectrum), and *cross-gate consistency*. That is a real, publishable
  identification-grade claim — frame it as that, not as a fully-derived identification.
- The **discriminating follow-up** — deriving ρ(r) from swirl dynamics to predict Tully–Fisher / core-size
  relations — is what would make the candidate *distinctive*. It is a **separate piece of work, NOT a
  blocker** on this paper. Name it as future work; don't attempt it here.
- Keep numbers honest: σ_V/m magnitude carries f's factor-3 band (0.03–0.27, partly Project-C-feedable); the
  *flatness* does not. The core *size* is halo-model-dependent (~factor 2) on top of f. State both.

## 6. Assets (DM lane — all under `series_phenomena/cosmology/dark_matter/`)

- **Spine:** `DM-1_draft_manuscript.md` (the draft to finish); `DM_project_map.md` (arc state, conditionals,
  window dependency map — read this second).
- **Gate files:** `step1_sigma_over_m_SIDM.md`, `step2_bookkeeping.md`, `step3_coldness.md`,
  `step4_power_spectrum.md`, `step5_rotation_curve.md`.
- **Discriminant chain:** `qdp_self_interaction_velocity.md`, `qdp_viscosity_cross_section.md`,
  `qdp_dwarf_core_radius.md`, `qdp_saturation_eos_sigma_window.md`, `qdp_residual_resonance.md`,
  `qdp_residual_fraction_f_derivation.md`, `qdp_f_as_a_number.md`, `qdp_required_inputs_derivation.md`,
  `dm_candidate_consistency_consolidation.md`; figures in `figures/`, scripts in `scripts/` (re-audit before
  reuse), reasoning in `reasoning/`.
- **DM-2 / cosmological leg (read-only from this paper):** `R2_sea_gravitation_scoping.md`, `pk_closure/`,
  and `sea_gravitation/` (the OPEN-SR-5 overlap with the 1100 window — do not write there from the DM lane).
- **OSF / abundance:** `osf_registration_qdp_dm_conjecture.md`, `qdp_relic_abundance_scoping.md`.
- **Frontier entries:** `frontier_sectors/CONJ.md` — CONJ-COSMO-1 (line ~314), OPEN-COSMO-DM-1 (line ~229),
  OPEN-COSMO-DM-2 (line ~250, substantially resolved). R2 ledger: `mu_eps_closure/R2-STATUS.md`.

## 7. Anti-collision

- **Band: 0848 onward.** 0800–0847 consumed (0847 = this charter). Grep `git log` for the next free number before each use.
- **DM-1 is collision-safe:** all writes land in `dark_matter/` and touch no shared file. Confirmed safe vs
  the 900 (chirality), 1000 (Project C), 1100 (cosmological-constant), and 2100–2149 (Capture-and-Audit)
  windows per `DM_project_map.md` §6.
- **The one coordination point** is the DM-2 Λ files (`sea_gravitation/stepC_*`, `stepD_*`), which overlap
  the 1100 window — **DM-1 does not touch them** (read-only cite). If the work ever drifts toward them, flag
  TLA before editing.
- Run the anti-collision protocol (`templates/new_window_protocol.md`; "run the anti-collision protocol") if
  spawning a sub-window. End every reply with a collision watch.

## 8. First concrete action

Read `DM-1_draft_manuscript.md` and `DM_project_map.md` end-to-end, then open the §11 checklist and pick the
highest-leverage gap (recommended order: §1 primer → §4 figure → §6 specific-dwarf fit → §8 inputs → §5/§6
[TIGHTEN] number-honesty pass → final grade sentence). Land each as its own 0848+ patch in `dark_matter/`,
verify-script-bundled where it computes, and present per the patch contract. No status moves; ship-readiness
call is TLA's.

*Charter banked by Claude Opus under Thomas Lee Abshier's direction. Corrections appended forward.*

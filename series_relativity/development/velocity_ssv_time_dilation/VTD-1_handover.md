# HANDOVER — VTD-1: Is the Displacement-Budget Quadrature Genuine? (the last R2 gate)

**Purpose:** start a fresh Opus window cold on VTD-1, the sole remaining structural condition for the R2
vacuum-impedance falsifier. Written 22 Jun 2026 at the close of the R2 universality arc (patches 2024–2031),
context fresh. Opus = worker; Thomas (TLA) = sole integrator and founder's-eye on the mechanism.

---

## 0. The one-paragraph orientation

R2 (does the vacuum impedance Z₀ stay geometric, so α does not drift under an SSV/density perturbation — a
~6-order LPI falsifier) has been driven from "leaning FAIL" to **PASS conditional on exactly two named
things: (i) VTD-1, and (ii) the 1110 LSP field-content audit (scalar |SSV|_abs + vector SSV_net, no rank-2
mode).** Condition (ii) is pre-existing corpus work and is CONFIRMED-by-panel as closing the
universality/locality/completeness chain. **Condition (i) VTD-1 is the last gate, and it is foundational —
it needs the founder's view, not a solo grind.** This handover is to take on VTD-1.

## 1. What VTD-1 is, precisely

VTD-1 is the claim that **the displacement budget splits in quadrature**, giving the EXACT Lorentz factor.
SR-1's budget is a 4D speed limit: total CP displacement ≤ l_P per Absolute Moment. A mass moving at v
consumes a bulk displacement v·t_P along the motion direction; internal processes get the remainder. IF that
remainder is the **orthogonal** (Pythagorean) part √(l_P² − (v·t_P)²) = l_P√(1−v²/c²), then internal rates
scale by exactly 1/γ ⇒ **γ = 1/√(1−v²/c²) EXACTLY** (verified numerically, Patch 2024,
`budget_and_photon_phonon.py`). The naive linear split (1 − v/c) is wrong.

**The open question:** WHY are the bulk and internal displacements orthogonal? In the standard SR light-clock
this is automatic only for a *transverse* internal process; a general internal displacement (PCD cycle,
oscillation) need not be perpendicular to v. So is the quadrature:
- (A) **forced** by the substrate mechanism (the PCD cycle / Absolute-Moment structure genuinely allocates
  bulk and internal displacement into orthogonal subspaces), or
- (B) an **assumption** that happens to reproduce γ?

VTD-1 PASSES iff (A). If (B), the exact-γ — and with it the whole velocity-frame leg that forced
c_photon ∝ C, and thence R2 — rests on an unjustified orthogonality. **This is the crux to settle.**

## 2. Why it needs the founder's view

The orthogonality is a statement about how a Conscious Point's displacement budget is partitioned during the
PCD (Perceive, Compute, Displace) cycle when the CP aggregate has an absolute velocity. That is substrate
mechanism — TLA's domain. Opus can (and should) do the corpus archaeology, set up the candidate
decompositions, compute consequences, and run adversarial review; but the physical claim "bulk ⊥ internal in
the budget" wants TLA's mechanism-level adjudication. Expect interleaved work, not a solo derivation.

## 3. Starting plan (suggested first moves for the new window)

1. **Read SR-1's budget mechanism in full** — `series_relativity/papers/mechanism-SR-1.md`. Target: the exact
   statement of the l_P-per-Moment budget, the 4D decomposition R₄D² = r₃D² + τ² (line ~ the insphere
   relation), and how KE is stored ("increased separation along the direction of motion", ~line 31). Map
   precisely which quantities are vectors and what subspace "internal" displacement lives in.
2. **Read the PCD-cycle definition** — grep `Perceive.*Compute.*Displace` and the boost-law finding
   `series_relativity/development/pcd_boost_law_finding.md`. Target: does the cycle structurally separate the
   translation step from the internal-reconstruction step into orthogonal displacement allocations?
3. **State the candidate decompositions (A vs B)** explicitly and compute each one's γ(v) (extend
   `budget_and_photon_phonon.py`). Confirm only the orthogonal one gives exact γ (already shown), then focus
   entirely on whether orthogonality is forced.
4. **Founder consult (TLA):** put the precise question — is the internal displacement constrained to the
   subspace orthogonal to the bulk velocity by the PCD/Absolute-Moment mechanism? — and let TLA adjudicate
   the mechanism.
5. **Adversarial review (CONV-001)** once a position is reached, neutrally framed, full content inline.

## 4. The honest discipline that worked on R2 (carry it)

- **Follow the physics, not the desired verdict.** The R2 arc went PASS(circular) → FAIL(phonon category
  error) → OPEN → PASS-cond → REVISE → grounded → CONFIRM, every swing physics-driven and documented. When a
  result points toward the answer you want, scrutinise it HARDER (the corpus checks that grounded universality
  were run *because* the result was convenient).
- **Never call it closed when it's conditional.** Name conditions explicitly; resist collapsing "narrowed" into
  "removed" (the 2028→2029 lesson: I overclaimed "VTD-1 alone" and the panel correctly REVISEd).
- **Capture reasoning verbatim per patch** (`reasoning/` fragment bundled in the same `git am`).
- **NO THEO.** No new axioms/terms/counted predictions; all results conditional, in owned greenfield paths.

## 5. Working environment & protocols (unchanged)

- **Repo:** github.com/Hyperphysics-Institute/CPP, main branch. Container clone for the worker; TLA's machine
  `~/Documents/GitHub/CPP` (Windows Git Bash), downloads → `~/Downloads`.
- **Worker rules:** number patches in an assigned band (this arc used **2000-band**; the next sequential is
  **2032+** — confirm with TLA, or take a fresh band if running parallel to other windows). Write only in
  owned greenfield paths; defer ALL shared-registry edits (CONJ.md, predictions.md, c06, SR-1, frontier
  sectors) to TLA as "Proposed for integrator." Commit identity Opus / opus@cpp.local.
- **Patch delivery:** bundle `.md` finding + `reasoning/` fragment + any verify script in ONE `git am`. After
  every `present_files` on a `.patch`, output the precautionary apply-and-push macro (cd ~/Documents/GitHub/CPP
  && git pull --rebase origin main && git am ~/Downloads/<file>.patch && git push origin main && git log
  --oneline -3) + the `git am --3way` recovery note. ALWAYS verify clean apply against current origin/main
  before presenting (git fetch + git reset --hard origin/main; build on that).
- **CONV-001 review:** ONE fenced block per reviewer (ChatGPT/Grok/Copilot), FULL content inline (reviewers
  don't browse links), neutral framing (claims as propositions under test), disclose history.

## 6. Key files (R2 arc, for context)

- **R2 ladder (canonical status):** `series_relativity/development/mu_eps_closure/R2-STATUS.md` — read the
  tail updates (patches 2024–2031) for the full conditional-PASS state.
- **The velocity/exact-γ work (where VTD-1 lives):** this folder,
  `series_relativity/development/velocity_ssv_time_dilation/` — `MISSING-MACHINERY-FOUND.md` (VTD-1 stated),
  `budget_and_photon_phonon.py` (γ computation).
- **The c_photon∝C forcing & universality chain:** `…/mu_eps_closure/em_emergence/` —
  `R2-RESOLUTION-VIA-LORENTZ.md`, `UNIVERSALITY-GROUNDED-SCALAR-SSV.md`, `C07-STATIC-COMPLETENESS-RESOLVED.md`,
  `R2-PANEL-REVISE-*.md`.
- **The field-content result R2 now rests on (condition ii):** `series_relativity/op_einstein_closure/
  1110_stepA_c07_audit.md` — LSP = scalar + vector, no rank-2.
- **Substrate mechanism for VTD-1:** `series_relativity/papers/mechanism-SR-1.md`,
  `series_relativity/development/pcd_boost_law_finding.md`.

## 7. Definition of done for VTD-1

Either: (A) a corpus-grounded + founder-adjudicated argument that the PCD/Absolute-Moment mechanism FORCES the
bulk⊥internal quadrature (⇒ exact γ ⇒ VTD-1 PASS ⇒ **R2 PASS conditional on the 1110 audit alone**), surviving
one adversarial CONV-001 round; or (B) an honest finding that orthogonality is NOT forced (⇒ exact γ is an
assumption ⇒ R2's velocity leg weakens ⇒ reopen, with the precise gap named). Do not force (A); report what
the mechanism actually gives.

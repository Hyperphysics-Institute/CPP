# DG-3 re-fire results — THEO-CHIR-CAPACITY-1: **RESTATE** (2 CONFIRM / 1 RESTATE); verdict NOT enacted

**Location:** `series_umbrella/series_substrate_chirality_arc/chirality_derivations/review/0921_dg3_refire_results_RESTATE.md`
**Patch:** 0921 · **Reviews adjudicated:** ChatGPT (RESTATE), Grok (CONFIRM), Copilot (CONFIRM). Re-fire of the 0920 package.
**Verify (added Patch 0929):** `chirality_derivations/code/0921_weight_concentration_falsifier_check.py` (reproduces the falsifier: equal-weight R(m) defeated by concentration; loose worst case ~1.7 at p=4-5).

**Disposition:** Pass criterion (3/3 CONFIRM, no unresolved falsifier) **NOT met** — tally **2 CONFIRM / 1 RESTATE**. ChatGPT's lone RESTATE lands a **specific, genuine, verified** Q1 falsifier (the weight-concentration gap); the two CONFIRMs **assert** universality over the non-uniform class rather than test the concentrated limit, so they do not discharge it. **THEO-CHIR-CAPACITY-1 is NOT enacted.** V3/W3 stand; CAPACITY-1 reserved; OPEN-CHIR-1d-β stays OPEN; prediction count unchanged; conditional on Mechanism A.

---

## Tally

| | Q1 universality | Q2 current | Q3 comparison | Q4 logic/framing | Q5 scope | Overall |
|---|---|---|---|---|---|---|
| ChatGPT | **RESTATE** | CONFIRM | CONFIRM | CONFIRM* | CONFIRM | **RESTATE** |
| Grok | CONFIRM | CONFIRM | CONFIRM | CONFIRM | CONFIRM | **CONFIRM** |
| Copilot | CONFIRM | CONFIRM | CONFIRM | CONFIRM | CONFIRM | **CONFIRM** |

\* ChatGPT's Q4 CONFIRM is explicitly *conditional on the Q1 restatement* ("if every admissible observable/eigenmode is truly off-critical, the direction is correct, not inverted").

**Note the improvement over the first fire (0914):** the previous convergent falsifier (Q1 sample-vs-proof) is **discharged** — all three reviewers accept the row-sum invariant as a genuine proof over the *equal-weight* class, and the Q3 documentation gap, Q2 scope, and Q4 framing fixes are all confirmed by all three. The new C1 closed the old Q1. But it opened a **narrower, sharper successor** to Q1 on the same η-identity spot: the *admissible-weight* class.

## 1. The falsifier (Q1, ChatGPT) — genuine, verified here, and sharper than stated

**ChatGPT's point.** The bound `R(m) = m·(2/π)arcsin(1/m)` assumes a **uniform (equal-weight)** m-edge read, giving shared-edge correlation exactly `1/m`. For general CHI-1-admissible weights `w_e`, an observable may concentrate almost all weight on one (shared) edge plus tiny weights on the others: it is then *nominally* `m ≥ 4` but **spectrally approaches the critical single-edge `m=1` case**, erasing the 36% margin. The nominal-`m ≥ 4` orientation floor does **not** exclude this, because nominal edge count ≠ effective participation. Proposed fix: state an explicit admissibility condition — a lower **effective participation ratio** `m_eff` (e.g. `m_eff ≥ 4`) — before claiming the universal margin.

**Chirality-lane adjudication: the falsifier is real.** Verified directly (worst-case row sum `S(w) = Σ_i (2/π)arcsin(w_i·a_i)`, normalized `Σw_i²=1`, participation `p = 1/Σw_i⁴`):
- In the one-big-weight family `(W, ε, …, ε)`, `S > 1` (super-critical) persists up to participation `p ≈ 2.2` (m=4), `≈ 3.4` (m=6), `≈ 3.8` (m=12). Concentration genuinely defeats the equal-weight bound.
- This is the **η-identity resurfacing in its sharpest form**: "which *weighting* is the dynamical η." The equal-weight assumption was doing silent load-bearing work in `R(m)`.

**And sharper than ChatGPT stated — the bare floor is not obviously sufficient.** Maximizing the worst-case row sum over **all** weight vectors at fixed participation (loose bound `a_i ≤ w_max`, i.e. every neighbour concentrates onto its shared edge with `v`) stays `≈ 1.7` even at `p = 4` and `p = 5`. So a bare `m_eff ≥ 4` floor does **not** by itself restore `ρ(M) < 1` under the loose adversary. The honest closure needs **two** ingredients, not one:
  - **(a) an admissibility / participation condition** bounding weight concentration, *derived from* the orientation requirement (a genuine 4-D enantiomorph cannot place ~all weight on one edge — one oriented edge carries no handedness — so the orientation/CHI-1 requirement should *imply* a participation floor; this must be derived, not assumed), **and**
  - **(b) a worst-case row-sum bound computed under vertex-transitivity** — using the fact that a single translation-invariant rule presents each vertex's large weight to only *one* neighbour (the loose "all neighbours concentrate" bound is unphysical and is what stays super-critical; the real matching structure is what must close it).

The closure is *probably* salvageable (the physical single-big-edge structure is far milder than the loose adversary), but it is a **real computation that is not yet done**, not a wording change.

## 2. Why the two CONFIRMs do not discharge it

Grok ("the closed-form invariant **exhausts the entire admissible class** … no remaining ordering channel") and Copilot ("no admissible local η including **non‑uniform** ones can condense") both **assert** universality across non-uniform weights. Neither tested the **concentrated-weight** limit ChatGPT constructed; Grok lists "non-exhaustive class" among falsifiers it "found none" of, but its reasoning rests on the equal-weight `R(m)` table. As in the first fire, the dissent is the more penetrating review and identifies a load-bearing point the confirmations assumed away. A 2-CONFIRM / 1-RESTATE split where the dissent holds a verified falsifier is **not** a pass under the 3/3 criterion. (This is the precise pattern the handover flagged: do not let momentum override the gap.)

## 3. What all three reviews DID confirm (the result is mostly solid)

- **Q1 (old gap) discharged:** the sample→proof move is accepted; the row-sum invariant is a genuine spectral bound over the *equal-weight* class. The residual is now strictly the *weight* sub-class, a real narrowing of the open question.
- **Q2 (current):** all three CONFIRM; the T-odd/T-even `O(δ⁶)` suppression at the physical bias is decisive for a status theorem; all-orders caveat honestly stated.
- **Q3 (comparison):** all three CONFIRM; `|K_lift|≈0.053` below both FM (≈0.095) and AFM (≈0.27); the single `ρ(M)≤R(m)<1` bound clears both channels; ≈44% conservative headline correct. The 0824/0825 links + 0823 forward-note resolved the first-fire documentation gap.
- **Q4 (framing):** all three CONFIRM the primitive (not emergent) direction — **no inversion flag** (ChatGPT conditional on Q1).
- **Q5 (scope/honesty):** all three CONFIRM Mechanism-A + per-edge-independence conditionality, no over-claim, temporal axis + OPEN-SM-4 untouched.

So the *only* live issue is the admissible-weight sub-class of Q1.

## 4. The two paths forward

- **Path A — close the weight sub-class (restores the strictly-universal claim).** Hand to the **F.1 window** (L-CAP owner) the two-part computation in §1: (a) derive a participation/concentration floor from the orientation (CHI-1 / 4-D-enantiomorph) requirement — show an admissible handedness indicator *cannot* concentrate below some `m_eff`; (b) bound the worst-case row sum under **vertex-transitivity** at that floor and show `ρ(M) < 1`. If both hold, re-fire with C1 amended to carry the explicit admissibility condition; this is the route to a real 3/3. **This is the recommended route** *if* the orientation requirement cleanly implies the floor — it likely does, since the physics of "what counts as a handedness observable" is exactly what bounds concentration.
- **Path B — scope-narrowing (airtight now, weaker headline).** Restate C1/the theorem to: *"V1 excluded over the **normalized, non-degenerate (bounded-concentration / equal-weight) CHI-1 η-observable class**, at the physical bias, conditional on Mechanism A,"* explicitly flagging extreme weight-concentrated constructions as outside scope. This is **already review-endorsed** (it is exactly ChatGPT's "CONFIRMED for normalized non-degenerate/equal-weight" restatement, and Grok/Copilot are stronger), and would pass 3/3 immediately. The cost is that the headline is no longer "chirality is a primitive, full stop," but "primitive within the non-degenerate observable class."

**Verdict-owner lean.** Pursue **Path A first**, because the falsifier is *physical* (it is the η-identity: which weighting is the dynamical η), and the natural resolution is also physical — the orientation requirement should bound concentration. **If** Path A's participation floor cannot be derived from the orientation requirement (i.e. the substrate does *not* fix the η-weighting at the kinematic/CHI-1 level), then the residual is genuinely **at the PCD layer**: "what weighting does the substrate actually compute" is then the located irreducible input — this is **outcome 2 of the original decision gate**, and the spot where Thomas's held PCD-layer insight would finally be called. Path B is the clean fallback either way.

## 5. Disposition + next steps

- **No verdict moved.** CAPACITY-1 NOT enacted. V3/W3 stand; OPEN-CHIR-1d-β OPEN; count unchanged; conditional on Mechanism A.
- **Thomas's call: Path A vs Path B** (or Path B now as a banked result *while* Path A is attempted — they are not exclusive; Path B can ship as the conservative theorem and Path A upgrade it later).
- **Path A hand-off (F.1 window):** the two-part computation in §1 — (a) orientation ⇒ participation floor; (b) vertex-transitive worst-case row sum at the floor. Attach this note + 0826 + 0920.
- **Path B execution (chirality lane):** amend C1 wording in a fresh package, re-fire; expected 3/3 on the narrowed claim.

## Scope held

Review-results record + restatement plan. **No verdict moved, no THEO registered, no CHIR.md edit, no count change.** CAPACITY-1 reserved. The weight-concentration falsifier is logged as the live successor to OPEN-CHIR-1d-β's closure condition. Conditional on Mechanism A (OPEN-FP-F1-2), incl. per-edge independence.

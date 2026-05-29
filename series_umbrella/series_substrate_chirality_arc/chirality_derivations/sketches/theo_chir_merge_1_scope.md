# THEO-CHIR-MERGE-1: Scope and Precondition Sketch

## The Unified Chirality Sign — Is `σ_cycle = sign(n̂)`? (the E19/E20 merge)

**Patch 0643, Session 148** (29 May 2026)
**Sector:** CHIR (Substrate Chirality Arc) — the **primitive-count capstone** of the
audit-downstream programme. The three derivations (E20/E21/E19) reduced chirality to
`{n̂, FI-C-9, σ_cycle}`; this question decides whether the last two *sign* data are one or two.
**Targets:** the registered cross-link **OPEN-CHIR-MERGE** (the E19/E20 merge), flagged in
THEO-CHIR-PCD-ORIENTATION-1 §5.3 and THEO-CHIR-CAP-1 §5; entangled with **OPEN-CHIR-2a** (the
PCD T-asymmetry).
**Status of this document:** scope-and-precondition sketch. The merge is genuinely open (it can
resolve as one sign, two signs, or undetermined-pending-2a); this sketch maps the registered
route, the entanglements, the decisive tests, and the candidate outcomes — it does **not** assert
the merge.

---

## §0 Firewall and the primitive-count stakes

This sketch plans; it does not prove. The stake is the **final chirality primitive count**. After
the three derivations, the programme's irreducible chirality content is:

- `n̂` — the spatial primitive 4D direction (axis; FI-C-RC-1);
- FI-C-9 — the chirality magnitude `|χ| = φ⁻³` (value-derived by THEO-CHIR-CHI-1, still an input
  pending 1d-β) and the frozen **enantiomorph sign** `sign(n̂)`;
- `σ_cycle` — the **temporal** cycle handedness (E20; A1+A4), the direction of the
  Perceive→Compute→Displace cycle.

THEO-CHIR-CAP-1 pinned the *spatial* capture-handedness sign to `sign(n̂) = FI-C-9`. The open
question is whether the *temporal* `σ_cycle` is the **same** sign. If yes (**merge**), the
programme carries **one** chirality sign (one frozen enantiomorph fixing spatial *and* temporal
handedness) — the most unifying chirality statement available. If no, it carries **two**
independent sign primitives. This is the last tractable piece of "is chirality emergent or
primitive"; the only deeper reduction is 1d-β (the dynamics that would derive `sign(n̂)` itself).

No false merge: a merge claim must terminate in a registered link from `σ_cycle` to `sign(n̂)`;
asserting it because it is *elegant* (one sign is prettier than two) is exactly the failure to
avoid. M2 (two independent signs) and M3 (undetermined) are honest outcomes.

---

## §1 The question

> **Is `σ_cycle = sign(n̂)`?** Equivalently: does the temporal PCD-cycle handedness reduce to the
> same frozen substrate enantiomorph (FI-C-9) that fixes the spatial chirality, or is it an
> independent temporal sign primitive?

---

## §2 Existing groundwork

### §2.1 The two signs as currently registered

- **`σ_cycle` (temporal).** E20: `ω_PCD = σ_cycle·n̂`. `σ_cycle ∈ {+1,−1}` is the handedness of
  the temporal primitive — which of P→C→D or D→C→P is forward — carried by A1 (the cycle steps)
  + A4 (the Absolute-Moment cadence). E20 treated it as the *temporal* primitive, kept distinct
  from the spatial chirality (audit: "ordered (primitive) vs T-asymmetry (owed)").
- **`sign(n̂)` (spatial).** THEO-CHIR-CAP-1 (verdict R1): the spatial capture-handedness sign is
  `sign(n̂)`, which *is* the FI-C-9 frozen enantiomorph ("the sign of n̂ determines which
  enantiomorph is the actual substrate").

### §2.2 The candidate registered route: THEO-DSL-3

The F.1 / DSL arc supplies a registered link from `n̂` to a **temporal** chirality:
**THEO-DSL-3** closes OPEN-SD-CHIR-PRIMITIVE **manifestation (iv) — the thermodynamic causal
arrow** — at sketch-document Layer 3, via the substrate net DI-bit current being directed
`∥ n̂` (the F.1 substrate-locality theorem). The chirality-continuum architecture (Capotauro
v2.0 + DSL) explicitly aims to *relate spatial-sector handedness (i)–(iii) to temporal-sector
handedness (iv): irreversibility, thermodynamic causal arrow* — through the shared primitive `n̂`
and the shared structural constant `−1/(2φ)`. So the merge is **not a priori blocked**: there is
a registered mechanism by which a temporal arrow is sourced from `n̂`.

### §2.3 The entanglements (why it is not a foregone conclusion)

- **Mechanism A's `sign(δ)`.** The F.1 Phase-1 current is `j ∝ (6 r₀ δ/φ²) n̂` (Mechanism A:
  `r(ê) = r₀(1 + δ ê·n̂)`). Its **direction** is `sign(δ)·n̂` — so the thermodynamic arrow sourced
  by it carries a factor `sign(δ)` *in addition to* `sign(n̂)`. Unless `sign(δ)` is fixed or tied
  to `sign(n̂)`, the temporal arrow's sign is `sign(δ)·sign(n̂)`, which is **not** simply
  `sign(n̂)` — an extra Mechanism-A degree of freedom that would keep the temporal sign
  independent (favoring M2).
- **OPEN-CHIR-2a (the T-asymmetry).** The audit holds the PCD *ordering* primitive but its
  *irreversibility* (T-asymmetry) separately owed (OPEN-CHIR-2a, which "connects to THEO-DSL-3").
  `σ_cycle`'s status *as an arrow* (not just an ordering) depends on 2a. The merge cannot be
  fully settled while 2a is open: if the cycle has no registered T-asymmetry, `σ_cycle` is a bare
  ordering sign, and its identification with the (irreversible) thermodynamic arrow is incomplete.
- **The identification gap.** Even granting the route, one must show the PCD-cycle direction
  `σ_cycle` *is* the DSL-3 thermodynamic arrow (the same temporal sign), not merely correlated.

---

## §3 Decomposition, route, and candidate outcomes

### §3.1 The merge route (the hypothesis to test, not assert)

`σ_cycle` ?=? (the DSL-3 thermodynamic arrow) ← (the substrate current `∝ sign(δ)·n̂`) ← `n̂`.
The merge `σ_cycle = sign(n̂)` holds **iff** (a) `σ_cycle` is identified with the DSL-3 arrow
(MERGE-α) **and** (b) the arrow's sign reduces to `sign(n̂)` — i.e. `sign(δ)` is fixed/tied to
`sign(n̂)`, not free (MERGE-β) — **and** (c) the T-asymmetry that makes it an arrow is registered
(OPEN-CHIR-2a).

### §3.2 Sub-gap MERGE-α — the identification (near-term reachable)

**Target:** show the PCD-cycle direction `σ_cycle` is the same temporal sign as the DSL-3
thermodynamic arrow. Plausible argument: the PCD cycle *is* the substrate dynamics that produces
the directed DI-bit current; the thermodynamic arrow *is* the direction of that current's
coarse-grained effect; so they are the same temporal orientation, not two. This is a structural
identification over registered objects (A1+A4 cycle ↔ DSL-3 current), plausibly Layer 2/2.5.
Reachable; reserve **THEO-CHIR-MERGE-1** for the merge resolution built on it.

### §3.3 Sub-gap MERGE-β — the sign (entangled)

**Target:** determine whether the arrow's sign reduces to `sign(n̂)` or carries an independent
`sign(δ)`. Decisive sub-questions: is Mechanism A's `δ` sign a free parameter, or is it fixed by
the same enantiomorph choice (e.g. `sign(δ) = sign(n̂)` because the propagation-rate asymmetry is
*the* substrate chirality, not an independent bias)? If `sign(δ)` is tied to `sign(n̂)`, MERGE-β
closes toward M1; if free, toward M2. This is entangled with the F.1 Mechanism-A status and with
OPEN-CHIR-2a.

### §3.4 Candidate outcomes

- **M1 (merge → one chirality sign).** `σ_cycle = sign(n̂)`: one frozen enantiomorph fixes
  spatial capture handedness, temporal cycle direction, and `n̂`-orientation alike. The
  programme's most unifying chirality statement; would merge E19+E20 onto one sign primitive.
- **M2 (independent → two chirality signs).** `σ_cycle` carries an independent sign (e.g. via a
  free `sign(δ)` or an A4-cadence sign not tied to the enantiomorph). The programme carries two
  chirality sign primitives; E19 and E20 stay distinct.
- **M3 (undetermined pending 2a).** The route is sound but the sign cannot be fixed until the
  T-asymmetry (OPEN-CHIR-2a) is registered; the merge is deferred behind 2a.

### §3.5 Honest layer and gating

The merge is **not closable now** without progress on OPEN-CHIR-2a (the T-asymmetry) and the
Mechanism-A `sign(δ)` status. The reachable near-term piece is MERGE-α (the identification); the
sign (MERGE-β) is entangled. So the likely near-term artifact resolves MERGE-α (cycle = arrow)
and reports MERGE-β as M3-conditional-on-2a — a partial result that *narrows* the merge to the
sign question, without forcing M1. This is the honest analog of the staged closures of E21
(ratio reachable / dynamics deferred) and E19 (involution reachable / FI-C-9 consumed).

---

## §4 Section structure of the eventual THEO-CHIR-MERGE-1 artifact

~6 sections, Layer 2/2.5: (1) setup + the one-sign-or-two stakes; (2) the two signs as
registered; (3) the DSL-3 route + MERGE-α identification (cycle = thermodynamic arrow); (4) the
sign MERGE-β — the `sign(δ)` vs `sign(n̂)` analysis + the OPEN-CHIR-2a entanglement, with the
verdict (M1/M2/M3); (5) consequences for the chirality primitive count (one sign or two);
(6) falsifiers + what is not claimed. A verify script is warranted only if MERGE-β reduces to a
checkable 600-cell/Mechanism-A sign computation; otherwise the artifact is structural.

Falsifiers: (F1) `σ_cycle` shown *not* identifiable with the DSL-3 arrow (breaks MERGE-α);
(F2) `sign(δ)` shown free and independent of `sign(n̂)` (forces M2 — two signs);
(F3) the T-asymmetry (2a) shown to require a sign input beyond `{sign(n̂), sign(δ)}` (a third
temporal sign).

---

## §5 Precondition and honesty notes

- **Do not assert the merge for elegance.** One sign is prettier than two; that is not evidence.
  The merge requires the registered link (MERGE-α + MERGE-β + 2a), not aesthetic preference.
- **The `sign(δ)` question is load-bearing** and currently open: the temporal arrow's sign is
  `sign(δ)·sign(n̂)`, so the merge needs `sign(δ)` tied to `sign(n̂)`. Flag, do not assume.
- **OPEN-CHIR-2a gates the full closure.** The merge artifact should either advance 2a or
  explicitly condition on it (M3). The two are best worked together; a MERGE artifact that
  silently presumes the T-asymmetry would be incomplete.
- **FI-C-9 not eliminated either way.** M1 routes `σ_cycle` *to* `sign(n̂) = FI-C-9` (consuming
  it); it does not derive the enantiomorph (that is 1d-β). The merge changes the chirality
  *count*, not FI-C-9's input status.
- **Cross-link bookkeeping.** A confirmed M1 would update THEO-CHIR-PCD-ORIENTATION-1 §5.3 and
  THEO-CHIR-CAP-1 §5 (the flagged cross-links) from "hypothesis" to "resolved-merge"; until then
  they stand as flagged.

---

## §6 Patch sequence

- **Patch 0643 (this patch):** this scope sketch; reasoning fragment; CHIR.md registration of
  **OPEN-CHIR-MERGE** (the unified-chirality-sign question) with the DSL-3 route + the
  OPEN-CHIR-2a entanglement + the M1/M2/M3 outcomes; THEO-CHIR-MERGE-1 reserved. No
  theorem-registry proved-row.
- **Patch 0644+ (target):** the THEO-CHIR-MERGE-1 artifact — resolves MERGE-α (cycle = DSL-3
  arrow) and reports MERGE-β (the sign) as M1/M2/M3, best bundled with OPEN-CHIR-2a progress.
  Preceded by a read of the THEO-DSL-3 arrow construction + the Mechanism-A `sign(δ)` status.
- **Deferred / parallel:** OPEN-CHIR-2a (the T-asymmetry) — the gate on the full merge closure;
  1d-β (the FI-C-9 dynamics) — the deeper reduction beneath both signs.

---

## §7 What the eventual artifact contributes

It decides the programme's **chirality primitive count** — one sign or two — the last tractable
piece of "is chirality emergent or primitive." A confirmed merge (M1) would be the programme's
deepest unifying chirality statement: a single frozen substrate enantiomorph (FI-C-9) sourcing
spatial capture handedness (E19), temporal cycle direction (E20), and the `n̂`-orientation
together, with everything else emergent and only the enantiomorph-selection *dynamics* (1d-β)
remaining. An honest M2/M3 is equally valuable: it tells the programme it carries two chirality
sign primitives (or that the second is gated on the T-asymmetry), preventing a false unification.

---

## §8 References

- `chirality_derivations/theo_chir_pcd_orientation_1.tex` §5.3 — the E19/E20 cross-link / merge
  condition; `ω_PCD = σ_cycle·n̂`.
- `chirality_derivations/theo_chir_cap_1.tex` §5 — verdict R1 (`σ_capture = sign(n̂) = FI-C-9`);
  R2 (the merge) left as hypothesis.
- `dynamical_substrate_law/dynamical_substrate_law.tex` — THEO-DSL-3 (thermodynamic causal arrow,
  manifestation iv, sourced by the current `∥ n̂`); Mechanism A (`r = r₀(1+δ ê·n̂)`); the
  spatial↔temporal chirality-continuum framing; the shared `−1/(2φ)` constant.
- `frontier_sectors/CHIR.md` — OPEN-CHIR-MERGE (registered this patch); OPEN-CHIR-2a (the
  T-asymmetry, the gate); the E20/E19/E21 resolutions.
- `capotauro/sketches/Capotauro_chi_phi_closure.md` — FI-C-9 (the frozen enantiomorph sign).
- `axiom-registry.md` — A1 (cycle steps), A4 (Absolute-Moment cadence) — `σ_cycle`'s source.

---

**Scope document complete.** Patch 0643 commits this sketch + reasoning + the CHIR.md
OPEN-CHIR-MERGE registration. The honest finding: the merge has a *registered route* (THEO-DSL-3
sources a temporal arrow from `n̂`) and the *identification* piece (MERGE-α: cycle = arrow) is
near-term reachable, but the *sign* piece (MERGE-β) is entangled with Mechanism A's `sign(δ)` and
gated on the T-asymmetry (OPEN-CHIR-2a) — so the merge is genuinely open (M1 one sign / M2 two
signs / M3 undetermined-pending-2a), to be resolved at Patch 0644+ alongside OPEN-CHIR-2a, not
asserted here.

# Provenance Audit — δ_CP^(CKM) ≈ 65.5°

**Patch:** 4103. **Lane:** SM/EW. **Discharges:** TODO-4102-CKM65.
**Protocol:** the audit Patch 1202 prescribed for the 193.3° PMNS signpost — *exact source,
formula, author/date, dependency chain* — applied to the CKM value, which the June 2026
three-reviewer panel never examined.
**Verdict: NO DERIVATION CHAIN. The referral is CIRCULAR.**

---

## 1. Exact source

Unscoped tree search: the value occurs in **four** places, all in SF-2, and in no other paper,
derivation, sketch, or script.

| line | content |
|---|---|
| 344 | summary table: δ_CP^(CKM) ≈ 65°, δ_CP^(PMNS) ≈ 195° — **"Conjectural (Phase 7 OPTIONAL)"** |
| 1642 | δ_CP^(CKM) = arg(Capotauro phase factor) ≈ 65° (structural prediction) |
| 1645 | observed 65.5° ± 1.5° — matches "**if** the Capotauro phase factor closure proceeds as outlined" |
| 1755 | pre-registered failure branch if the Phase 7 closure fails |

## 2. Formula

δ_CP^(CKM) = arg(**Capotauro phase factor**).

## 3. The operand does not exist

**"Phase factor" occurs ZERO times in the Capotauro paper.** Capotauro's delivered result is

|M^K3| = |M^W| = |M^qDP| = χ/6 = φ⁻³/6 ≈ 0.0394

— an **absolute value**. Its single primary empirical prediction is Δp_LR = χ/6.

Capotauro is explicit that this is its boundary, and says so structurally rather than
incidentally (§Scope-of-mechanism, §"The re-scoping is structural, not strategic"):

> "the Capotauro mechanism's natural output is the substrate-level chirality matrix element
> |M| … The connection from |M| to PMNS-level observables (mixing angles, CP phase) requires
> the full PMNS perturbation machinery, **which lives in the electroweak-sector flagship
> paper (SF-2)**."

## 4. The chain closes on itself

- **SF-2** computes δ_CP^(CKM) as arg(a Capotauro object) → defers to **Capotauro**.
- **Capotauro** says the CP phase needs machinery that **lives in SF-2** → defers to **SF-2**.

Each shipped paper names the other as the location of the derivation. Neither contains it.
This is worse than the June finding on 193.3°: that was adjudicated "empirical coincidence /
back-calculation / signpost-only" — a number obtained *somehow*. The 65° is the argument of an
undefined operand, resolved by a closed referral loop between two shipped papers.

Capotauro's own forward-pointer confirms the phase is not in hand: δ_CP is "derived **(in
future work)** from the Capotauro nucleation event (sub-claim (a))" — and sub-claim (a) is
**OPEN** (OPEN-SM-4).

## 5. An internal inconsistency, noted in passing

SF-2 §1647: the PMNS phase "is derived from **the same** Capotauro phase factor propagated to
the neutrino-mixing eigenstates." One object is thus asked to yield **65°** and **195°** — two
arguments differing by ~130°. A single complex number has one argument. The difference must
therefore live entirely in the unspecified sector-dependent propagation, which is the very
machinery neither paper contains.

## 6. The consequence for F5 — sharper than Patch 4102 had it

Patch 4102 concluded F5 "reduces to the Capotauro/H1 blocker." That was **too generous**, and
this audit corrects it.

F5 needs an **O(1) phase angle** near 65.5°. An unscoped search for any corpus object
producing a chirality phase angle returns only SF-2 line 1642 itself. What the chirality arc
actually produces is:

- **magnitudes** — |M| = χ/6 (Capotauro, shipped, theorem-grade)
- at most a **sign** — which enantiomorph, via sub-claim (b) / H1 / sign(μ²)

**A sign is not an angle.** Even a fully successful H1 delivering sign(μ²) yields ±1, not
65.5°. So H1 is *necessary-at-most* and plainly **not sufficient** for F5. F5's real
dependency is Capotauro **sub-claim (a)**, the nucleation event — open, never attempted for
the CKM sector, and referred circularly.

**Restated F5 status:** OPEN, with no candidate object anywhere in the corpus that produces a
CP phase angle. This is not a computation waiting to be done; it is a missing mechanism.

## 7. What this does not claim

- It does not refute the 65° target. A referral loop is an absence of derivation, not a
  disproof; the value may yet be derivable.
- It does not touch Capotauro's shipped |M| = χ/6 result, which is unaffected.
- It does not re-open the June adjudication on 193.3°, which stands.
- One item left unverified and worth a separate look: Capotauro v2.0 states the **sign** of χ
  is derived from the primitive direction n̂ (FI-C-RC-1), while this lane's Patch 4046 found
  (600-cell, n̂) achiral because Θ fixes n̂. Whether those two survive together was not
  examined here. Filed as TODO-4103-NHAT.

---

## 8. The flagged-path sweep (`absence_gate.py`), and what it turned up

`absence_gate.py` passed this patch's absence claims but warned that four easy-to-miss paths
were unnamed — `Development/`, `Development/transcripts/`, `archive/`, `founders_voice/` —
the same paths whose omission let Patches 4008–4030 re-derive three months of existing work.
Swept. **It found material, and the material corroborates the verdict.**

`archive/grok-exploratory-SM/p2-neutrino-mixing-angles/` (February 2026, exploratory, archived)
is the only place outside SF-2 where a "Capotauro phase" is ever operationalized. What it
actually contains:

- δ_CP is a **hard-coded placeholder** in both notebooks — the source comments say so in
  as many words (`# δ_CP placeholder (from Capotauro phase)`); nothing computes it.
- It is **PMNS** (≈195°), not CKM. It does not bear on the 65° at all.
- The mixing-angle inputs are **hand-set placeholders** (`overlap_e_q = 0.55 # placeholders
  from lattice subgroups`) that reproduce the NuFIT central values they are compared against —
  the README's "Exact match" for sin²θ₁₂ = 0.304 is back-fitted, not predicted.
- It runs on `chi = 1/phi ≈ 0.618` — the **superseded** χ = φ⁻¹, retired at Finding C-3
  (Patch 0378) in favour of χ = φ⁻³ after the lost-1/φ arithmetic correction.

So the one historical attempt to use a "Capotauro phase" numerically hard-coded it, on a
retired χ, with back-fitted inputs, in the wrong sector. **No computed phase exists anywhere
in the corpus, live or archived.** The §4 verdict stands and is strengthened.

*Recorded because the gate's own warning is that "an unscoped grep for the WRONG STRING is
still a scoped grep." The sweep was run; this is what it returned.*

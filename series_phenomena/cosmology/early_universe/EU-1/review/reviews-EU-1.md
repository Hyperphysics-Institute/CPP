# EU-1 — Reviewer Responses + Cross-Reviewer Synthesis (cycle 1)

**Artifact:** EU-1 (primordial scalar spectral index, n_s = 1 − 2/N_* ≈ 0.9649).
**Cycle:** opened Patch 0782 (review package v1.0); closed Patch 0783.
**Panel:** ChatGPT, Grok, Copilot (Sonnet hostile pass not run this cycle).
**Outcome:** **3/3 SHIP, zero verdict-flipping objections** — first-reviewer-round convergence.
Calibration items 1–4 applied to the paper at v1.0; item 5 deferred to Thomas (touches registered status).

---

## 1. Verdict table

| Reviewer | Tier reached | T1 (log=A1 / p=2) | T2 (ZRP+H-thm) | T3 (δN / N_*) | T4 (neutrality+Debye) | T5 (honesty) | SHIP verdict |
|---|---|---|---|---|---|---|---|
| **ChatGPT** | INDEP. RECOMPUTED + SCRIPT-EXECUTED | sound; p=2 forced *within the mechanism*, not by A1 alone; "uniquely" slightly overstated | standard; A1 state-space restriction is the strong step; no objection | algebra correct; N_*=57 = total 60.5 + adopted pivot, separate them | reframing correct; bath-clause conditional accepted | strong; suggest "confirmed"→"derived at leading order" | **SHIP v1.0 with calibration (no v1.1 restate)** |
| **Grok** | INDEP. RECOMPUTED + SCRIPT-EXECUTED (all §7 checks PASS) | sound, registerable; zero-new-axiom clears promotion bar | consistent with Grok's own independent MC (Poisson + fast equilibration) | δN recomputed from first principles, holds | identity holds, sub-dominant w.r.t. ZBW bath | clean; no overclaim; conditional/grounded precisely stated | **SHIP (full panel consensus)** |
| **Copilot** | INSPECTED + INDEP. RECOMPUTED (T3.2/T4.2 numerics) | coherent + load-bearing; "log=uniquely A1" not airtight; p=2 conditional on H_eff & spectator choices | (i)–(iii) consistent as *leading-order reduction*, not strict entailment; H-theorem correct | algebra clean; pivot 57 = consistency-level, not locked | neutrality sufficient; Debye negligible given Planckian-ZBW-bath clause | good honesty posture; swarm-count + NO-THEO defensible | **SHIP (tighten uniqueness / entailed-vs-minimal before locking v1.0)** |

**Numerics:** independently reproduced by Grok and Copilot; full §7 script SCRIPT-EXECUTED by ChatGPT and
Grok — all checks PASS (n_s=0.964912, α_s=−0.000616, N_efold=60.55, ideal slope→p=2,
Δn_s(α)=4.91e-4≈0.117σ_Planck, Debye residual 3.60e-4≪170, fail-threshold Γ≈44.3).

---

## 2. Triage outcome (T1→T5)

- **T1 (log = A1 spine; p=2):** SOUND, no verdict-flipper. Convergent caveat (ChatGPT+Copilot): the
  "uniquely selects the log" / "only from microstate counting" language is a *practical*-uniqueness
  result within the minimal CPP assumptions, not theorem-level; and "p=2 forced by A1" is conditional on
  the linear H_eff∝μ coupling + spectator P∝H_eff² assignment. → **calibration 1, 2.**
- **T2 (ZRP + H-theorem):** SOUND. H-theorem math standard; the A1 state-space restriction (distinguishable
  cliff excluded) is the strong, correct step. Caveat (Copilot): properties (i)–(iii) are a *minimal
  leading-order reduction* (assumes no O(1) occupancy-dependent microphysics beyond SSV), not strict
  entailment. → **calibration 4.**
- **T3 (δN / N_*):** Algebra correct (all three; δN recomputed independently by Grok + Copilot). Convergent
  caveat (ChatGPT+Copilot): separate the *derived* total e-fold count ~60.5 from the *adopted* observable
  pivot ~57 (consistency-level placement, not uniquely CP-count-derived). → **calibration 3.**
- **T4 (neutrality + Debye):** SOUND. DP-Sea neutrality cancels the leading mean-field; the Γ-reframing
  |μ_ex|/kT = c·Γ^{3/2} dissolves the √n̄ scare; residual ≈3.6e-4 ≪ 170 given the ZBW/substrate-bath
  identification (κ~1). Heavily conditional on that bath clause, which all three accept as explicit.
- **T5 (honesty/scope):** Clean, no overclaim. "Not from A1–A11", NO-THEO, open inflation engine,
  homogeneity as standing commitment, Planck-match-as-consistency — all correctly signposted. Swarm-count
  increment (107→108) and NO-THEO judged defensible.

---

## 3. Calibration items and disposition

1. **Uniqueness language softened** (ChatGPT #1, Copilot T1.1/T1.2): §3 remark now reads "unique robust
   candidate among the natural occupation laws surveyed … practical-uniqueness within minimal CPP
   assumptions, not theorem-level; RG/geometric/composite logs unnatural but not formally excluded."
   **APPLIED (Patch 0783).**
2. **p=2 conditionality made explicit** (ChatGPT #2, Copilot T1.3): the "what is and is not free" remark and
   the mapping section now state p=2 is forced *within the A1→ZRP→δN chain* given the linear H_eff∝μ
   coupling and the spectator P∝H_eff² assignment — not by A1 in isolation. **APPLIED (Patch 0783).**
3. **N_* total vs pivot separated** (ChatGPT #3, Copilot T3.2): §2 now distinguishes the derived total
   ~60.5 (CP-count logarithm) from the adopted observable pivot ~57 (standard placement, consistency-level,
   not uniquely derived). **APPLIED (Patch 0783).**
4. **ZRP as minimal reduction** (Copilot #3): Lemma 5.2 now reads "reduces to … a minimal leading-order
   reduction, not a strict entailment; assumes no O(1) occupancy-dependent microphysics beyond SSV."
   **APPLIED (Patch 0783).**
5. **"confirmed at leading order" → "derived at leading order within the minimal ZRP cosmology model"**
   (ChatGPT only; "confirmed" sounds empirical): **DEFERRED to Thomas (maintainer decision).** Rationale:
   the registered PRED-C-96 label, panel-agreed at Patch 0778, is "**confirmed** at leading order,
   zero-new-axiom, conditional…" and set the swarm headline 107→108. Changing the paper's "confirmed"
   wording would desync paper↔predictions.md unless the register is also edited; the "confirmed/counted"
   status is the maintainer's swarm metric. Paper status line left matching the register for v1.0.
6. **Minor (Grok):** an abstract parenthetical on the ~0.0005 theory uncertainty — already present in the
   abstract ("Δn_s ∼ 5×10⁻⁴ (≈0.12 σ_Planck)"); no change needed.

---

## 4. Close decision

Per `templates/review_dispatch_protocol.md` §6: 3/3 SHIP, no verdict-flipping objection on any top-triage
question → **apply calibration and close the cycle.** Calibrations 1–4 folded in; v0.1 → **v1.0 (SHIPPED)**.
Item 5 logged as a deferred maintainer decision. The "single-pass" qualifier is removed; EU-1 is the
first cosmology/early-universe-sector paper to ship in the corpus.

**Phase-7 follow-on (not in this patch; sequence at Thomas's discretion):** programme-register propagation
(`paper_catalog.md`, `INDEX.md`, a `series_phenomena` README), the doc-suite, anthology chapter, and OSF
deposit — the standard post-v1.0-SHIP sequence (SF-2 / Capotauro / F.1 precedent). PRED-C-96 / PRED-O-34
already stand in `predictions.md`.

*Aggregated Patch 0783. Reviewer responses preserved verbatim in chat relay; this file is the synthesis
record per the MERGE-2 / STATUS pattern.*

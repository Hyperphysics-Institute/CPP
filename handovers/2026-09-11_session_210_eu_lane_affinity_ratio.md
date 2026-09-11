# EU-lane Handover — Session 210 Close (11 Sep 2026) — the structure derives; the amplitude does **not**; and three near-misses are one result

**Patch 3903. Lane: EU, block 3900–3999. Written under PD-006.**

## Orientation
**Repository state:** origin/main at Patch 3901 at session start; 3902–3903 delivered as patch files. **Next free: 3904.** GR lane: next free 3715.
**Active paper(s):** **EU-1 at V1.6** (**Isak owes the recompile**). GR-2 V2.11 (**Isak owes the recompile**).

## ⚠ READ THIS BEFORE REPORTING ANYTHING ABOUT C-5
**The amplitude is NOT derived.** **H_inf in this corpus is an A_s-normalised value** — the paper carries H ≤ 4.7×10¹³ GeV as a bound, and A_s = H²/(8π²ε M_Pl²) fixes H **from the observation**. **Computing ζ end-to-end from H is circular.**

**I had that arithmetic half-written.** It gives 4.5×10⁻⁵ against an observed 4.6×10⁻⁵ and **would have read as the amplitude derived while being an artifact.** It was withdrawn before it was claimed. **Do not reinstate it.**

## The single most important next action — worker work, in-lane
**Is there an independent route to H_inf?**

> If H can be **derived from CPP** rather than normalised to A_s, **the circularity breaks and the amplitude becomes a real prediction.** If it cannot, C-5's amplitude stays a consistency check permanently, and that should be stated in the paper rather than left implicit.

**This is the single thing standing between C-5 and a genuine result.** Everything else about it now either checks out or is a caveat.

## What was established
**Step A — the structure, from charge content alone, and the most durable item here.** qCP carries **both** polar and strong charge; eCP carries **only** polar; **the strong channel requires both partners to carry strong charge.**

| pairing | strong channel | coupling |
|---|---|---|
| Q-dominant ↔ Q-dominant | **open** | **α_s** |
| Q-dominant ↔ E-dominant | closed | α |
| E-dominant ↔ E-dominant | closed | α |

> **E-dominant couples at α whatever its partner — INDIFFERENT. Q-dominant reaches α_s only with its own kind — DISCRIMINATES.**
>
> **That is the founder's 3894 asymmetry, DERIVED rather than posited** — his walk-and-talk described the behaviour and the charge content produces it unasked. **Observation-independent**, which nothing else here is.

**Step B — couplings fixed before the ratio** (3901's discipline, honoured): α = 0.007297; **α_s(M_Pl) = 0.01970** from standard one-loop running (n_f = 6, Λ = 0.2 GeV, b₀ = 0.557). **No CPP input, no free choice.**

**Steps C/D:** f ~ 1/A ⇒ **f_E/f_Q = α_s/α = 2.70** against 3900's predicted **2.76**, band [1.7, 6.5] — **2.2% from centre, inside.**

**What survives the circularity check:** with δ_patch = ln(α_s/α) = 0.993 computed **independently**, **ℓ_req = 139.0 PSR vs ℓ_sat = 1/α = 137.0 — 1.4%**, and **the observation enters only at the sixth power** (ℓ_req ∝ ζ^{1/6}; ×10 in ζ_obs ⇒ ×1.5 in ℓ_req).

> **VERDICT: a consistency check, not a derivation.**

## ⚠ META-WARNING — attach this to CONV-046
**Three consecutive sessions have produced a computed number landing near a required one:** 1/α (3898), the O(1) saturation argument (3900), α_s/α (here).

**Three in a row is either a framework that works or a worker pattern-matching systematically. That cannot be told from the inside.**

**What can be established is independence, and they are not independent.** They are **one chain** — the brake fed the prediction, and this patch tested the prediction. **One chain, one weak observational input, two couplings.**

> **Weigh as ONE result, not three. The panel needs this stated, not inferred.**

## Caveats, not buried
- **f ~ 1/A is the re-stacking-dominated limit** of a two-rate steady state. **In the opposite limit f_E/f_Q → 1 and C-5 fails.** Which limit holds is load-bearing and untested.
- **Identifying CPP's strong coupling with SM α_s run to M_Pl is assumed**, not argued.

## C-5's debts
1–5. ~~Referent~~, ~~reservoir~~, ~~correlation length~~ (Gaussianity **cleared**), ~~brake~~ (consistent), ~~δ_patch~~ (predicted and tested, **inside band**).
6. **The circularity** — **NEW, and now the gate.** Independent H_inf or the amplitude is never more than consistent.
7. **Adiabaticity** vs Planck's isocurvature bound. **Untouched.**

## Owed
- **Isak:** recompile **EU-1 (V1.6)** and GR-2 (V2.11).
- **Maintainer:** CONV-046 — **with the meta-warning attached**; the amended DE escalation (3858); cosmic-web owed piece (3833); `DM_project_map.md` stale (3884).
- **EU-1 V1.7 (bundle):** 3854 VSL clarification; 3876 §5 as qualified by 3878. **Do not add C-5.**

**Anti-priorities:** **do not claim the amplitude is derived**; **do not present the three near-misses as independent evidence**; **do not reinstate the withdrawn end-to-end ζ**; do not report C-5 as working; follow **§0.5 D-1…D-6**; do not retire 3710; **nothing in this arc refutes n_s** — PRED-C-96 reads 0.9654 (V1.6).

## §15 Steps A–H
- **A** `session_logs/2026-09-11_session_210_log.md` (3903). **B** transcript row 3902. **C** development vignette (Session 210).
- **D** Tier 4: `reasoning/3902_affinity_ratio.md`.
- **E** Registries: `research_frontier.md` (3902 prepend); `id_block_registry.md` (next free 3904); `future_projects.md`; in-place update at `delta_patch.md` §5b. N/A: `predictions.md`, `axiom-registry.md`, `theorem-registry.md`, `master_glossary.md` — **no constant minted; amplitude not derived.**
- **F** none (no panel). **G** no PD minted. **H** this file.

## Governance note
**Check where every observational input came from before claiming a derivation.**

The affinity result was finished and the write-up was under way when the origin of H was checked. Had it not been, this session would have recorded "the amplitude is derived, 2% agreement" — and it would have been false, not by an arithmetic error but because one input was the answer in disguise.

> **The rule: before claiming X is derived, trace every input to X back to its source and confirm none of them was fixed by X.** Cheap, and it has now saved a false headline once.

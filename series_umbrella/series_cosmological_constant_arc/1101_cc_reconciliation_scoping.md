# CC Reconciliation — Founding Scoping (Patch 1101)

**Arc:** `series_umbrella/series_cosmological_constant_arc/` · **Charter:** `README-CCA.md`
**Status:** SCOPING. **NO VERDICT MOVED** — no THEO, no PRED, no count change; all conditional on
the c08 closed field equation. This document lays the three accounts side by side, states the
unification thesis, records the N⁴ demotion argument with its verification, and sets the
falsification-first plan. It does **not** edit any shared registry or the DP-Sea flagship.

---

## 1. The reconciliation question, sharply

CPP carries three accounts of `ρ_Λ ≈ 5.3×10⁻¹⁰ J/m³` (~10⁻¹²⁰ ρ_Planck). They agree on the order
for incompatible reasons. The umbrella must decide **which suppression is physical**, because a
dynamical account and a static account **cannot both be fundamental** — they predict different Λ(z).

- **(A) dynamical** — `OPEN-SR-5` Step C (Patch 0722). `ρ_Λ = c²H²/8πG = (1/8π) ρ_P (l_P/R_H)²`.
  Derivation: gravity couples to the SSV excess (c05) ⇒ the uniform Sea is inert; the only
  gravitating residual is the field energy `ρ = g²/8πG` of the largest gradient a discrete-UV
  (l_P), causally-bounded-IR (R_H) Sea cannot cancel — the horizon-scale mode, amplitude Φ ~ c²,
  coherence scale R_H = c/H. Both the (l_P/R_H)² scaling **and** the 1/8π are derived; Step D3
  selects the **future event horizon** as the IR scale (Li 2004; w_Λ(now) ≈ −1.02). Numerically
  2.56×10⁻¹⁰ J/m³, factor 2.07 of observed. **ρ_Λ ∝ H² ⇒ Λ time-varying ⇒ addresses "why now".**
- **(B) microscopic** — `OPEN-SM-6`. Paired-DP cancellation leaving `ρ_Λ ∝ E_P⁴ (l_P/R)²`,
  ~order of magnitude. SM.md cross-links SR-5 as "the same problem from the GR perspective" and the
  *expected solution form is already the (l_P/R)² form.*
- **(C) static** — `DP_sea_and_cage_composition.tex` (l.64/181/507). `ρ_vac ~ ρ_sea/N⁴ ≈ 10⁻¹²⁰ ρ_P`
  via "holographic bit recycling," N = 10³⁰ GPs per l_P. Asserted "resolved"; **constant** in time.

## 2. The unification thesis

**Claim (to be enacted via CC-U/3, not asserted here): (A) and (B) are one theorem, and the
suppression is dynamical.** The microscopic statement "the paired DP Sea cancels the bulk vacuum"
(B) and the GR statement "gravity sources only the SSV excess, so the uniform Sea is inert" (A) are
the **same fact two ways**; the leftover both leave is the horizon-scale uncancelled mode
`(l_P/R_H)²`. Excess-sourcing (c05) is the bridge: matter, DM, and Λ all gravitate by the same
mechanism, differing only in *what the gradient is* — matter/radiation = localized excess, swirls
= DM-amplitude excess, **Λ = the tiny residual non-uniformity of the ground state at the horizon
scale**. This is exactly the dark-energy↔dark-matter unification R2 needs (§5).

## 3. CC-U/1 — the N⁴ audit (the cheapest kill): DEMOTE, with proof

The static (C) account does **not** survive as a fundamental mechanism, for three independent
reasons; the number is kept, the *mechanism claim* is retired.

**(a) The coincidence: 1/N⁴ is (l_P/R_H)² evaluated today.** With N ≈ 10³⁰, the present Hubble
radius gives `R_H/l_P ≈ 8.5×10⁶⁰ ≈ N²` (`code/1101_cc_coincidence_check.py`). Hence
`1/N⁴ ≈ (l_P/R_H)²` **at the present epoch**. Because R_H grows with cosmic time while N is fixed,
`R_H ≈ N²·l_P` can hold at **one** epoch only — now. So the "constant 1/N⁴" is the dynamical
horizon suppression frozen at the present moment, not an independent static law. (The agreement is
loose — ~1.9 orders in the exponent, 10⁻¹²⁰ vs the derived ~10⁻¹²², which is itself the signature
of a coincidence-restatement, not a precise mechanism.)

**(b) Making N⁴ fundamental contradicts an established result.** Patch 0736 (SR-1 rederivation,
canonical nested-600-cell resolution) verified that lattice **resolution enters no prediction
formula** — all five SR predictions and the muon bound are unchanged under any resolution choice.
The 1004 commit states the consequence directly: *"GP-count cannot derive Λ without overturning
it."* A Λ that depends on N⁴ would make the lattice resolution physical and predictive, overturning
0736. So N⁴ cannot be load-bearing for Λ.

**(c) The input is unverified.** The "~10³⁰ GPs per l_P" estimate is Grok-origin and is **flagged
unverified and not-relied-upon** in the corpus (Patches 1004/1005), and `l_P` itself is the
*emergent* rest-frame Planck Sphere Radius, not a fundamental UV cutoff (1004). The N⁴ account rests
on a number CPP does not stand behind.

**Disposition.** Retain the energies/ratios elsewhere in the DP-Sea paper; **retire the claim that
the CC is "resolved" by ρ_sea/N⁴ via holographic bit recycling**, and reframe it to point at the
SR-5 dynamical mechanism (the N⁴ value = (l_P/R_H)² today). This is the **same epistemic-honesty fix
as TODO-016, in the same paper** — a flagship physics edit, so it is **drafted here and handed to
Thomas for the actual `.tex` edit/recompile/publish** (STOP-and-warn; not a worker push).

## 4. CC-U/2 — static vs dynamical: DYNAMICAL

Given §3, the physical suppression is (A). Λ is **time-varying** (ρ_Λ ∝ H²); the event-horizon
selection (Step D3) gives w_Λ(now) ≈ −1.02 and an evolving Ω_Λ — a genuine, falsifiable prediction,
distinct from a true constant. The R_H ≈ N²l_P coincidence is then **"why now" in disguise** (branch
i): the present-epoch equality of the static and dynamical numbers is the same coincidence the
dynamical reading already explains. **Branch ii** — that `R_H ~ N²·l_P` is a *derivable* substrate
relation (a holographic horizon-bit ↔ bulk-GP-count tie that would unify the two more tightly) — is
flagged as an optional **deeper** target, **not load-bearing** for the verdict and not pursued in
round 1.

## 5. CC-U/5 — wiring to the DM R2 gate

R2 (`R2_sea_gravitation_scoping.md`, Patch 0705) requires: uniform Sea must **not** gravitate
cosmologically (else Ω_Sea ~ 10⁴⁵–10¹²⁰) **while** its swirl-inhomogeneities **do** gravitate as DM.
Excess-sourcing delivers exactly this split: uniform Sea (ΔSSV = 0) inert; swirls (ΔSSV > 0)
gravitate. The 0705 file is **stale** — written before SR-5 Steps A–D (0720–0723), it calls the
sector "unbuilt." In fact Steps A–D delivered (i) derived suppression, (ii) the inert/gravitating
split, and (iii) Friedmann recovery (q flips at z ≈ 0.63); the DM-1 manuscript (0844) already
records "uniform-Sea-inert half essentially IN HAND." **Owed:** update R2's framing to
"uniform-Sea-inert half in hand, conditional on c08 + event-horizon selection." **This edit lives in
`dark_matter/` (DM 08xx lane) — propose to the DM window / integrator; do not edit from here.**
(Note: this does **not** revive structure formation — CONJ-COSMO-1's structure-formation role is a
separate, standing conditional-false verdict (Patch 0729); R2 is only the dark-energy/inert-Sea leg.)

## 6. CC-U/4 — the c08 cap (the deep dependency, the real mountain)

Everything above is conditional on the **c08 closed field equation** `G_μν = 8πG/c⁴ T_μν[LSP]` —
gravity sources from the LSP/excess, ground state excluded — which c08 itself calls an unsolved
conjecture ("the central challenge... not yet solved"). **Falsifier D2-1:** if the closed field
equation sources from absolute |SSV|, the ground state gravitates, the catastrophe returns, and the
CC suppression **and** the R2 split break **together**. This is the single place the umbrella can
fail wholesale; everything else is reconciliation of accounts that individually almost work. Closing
c08 is the genuine resolution of "the biggest embarrassment in physics" — it is **separable** from
the reconciliation, deep, and **not attempted in round 1**. Until it is closed, the honest grade is
**conditional**, exactly as SR-5 is already capped (hence the **no-THEO-for-conditional** discipline
applies — the unification is frontier-tracked, not registered as a theorem).

## 7. Plan & deferred actions

**Round-1 deliverables (this and the next few patches):**
1. **1101 (this patch):** scoping + arc container + coincidence-check. Private-lane; no shared file.
2. **DP-Sea N⁴ reframe:** draft the replacement text (CC-U/1 disposition) → Thomas's flagship edit.
   *(STOP-and-warn: `series_foundations/dp_sea_composition/DP_sea_and_cage_composition.tex`.)*
3. **Batched INT patch (CC-U/2,3):** `frontier_sectors/SR.md` (SR-5 ≡ SM-6 + dynamical verdict +
   N⁴ demotion note), `frontier_sectors/SM.md` (SM-6 = SR-5), `frontier_sectors/CONJ.md` (R2
   cross-link), `future_projects.md` + `README-SU.md` (register the umbrella).
   *(STOP-and-warn: all shared registries; CONJ.md is DM-lane-adjacent.)*
4. **R2 update (CC-U/5):** propose to the DM 08xx lane / integrator. *(Not edited here.)*

**Deferred / out of round-1 scope:** CC-U/4 (c08 closed field equation); branch-ii derivation of
`R_H ~ N²·l_P`; the `problem_histories/PH-OPEN-SR-5.md` cross-band trail.

## 8. Honest bottom line

The reconciliation is achievable and largely **already exists** in the SR-5 Step A–D arc — the
umbrella's contribution is **recognition + honest demotion of the N⁴ claim + explicit unification +
R2 wiring**, not a large new derivation. The *unconditional* CC solution remains gated on the c08
conjecture, which is real open physics. The deliverable of this arc, realistically, is: *"the three
accounts are one dynamical mechanism; the static N⁴ reading is a present-epoch coincidence and is
retired; SR-5 and SM-6 are one theorem; R2's inert-Sea half is in hand — all conditional on c08."*
That is a clean, defensible result. The trophy (closing c08) is named and separable.

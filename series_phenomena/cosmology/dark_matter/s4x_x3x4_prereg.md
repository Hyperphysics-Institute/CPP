# S4-X X3/X4 JOINT PREREGISTRATION (FROZEN) — clean-code replication + GP-limit ladder

**Patch 2786. Frozen 2026-07-23, BEFORE any production sweep.**
Authority: X3/X4 chartered in `s4x_charter.md` (X3 → PR1
fluke-exclusion; X4 → PR2 verbatim); the SEVEN BINDING instrument
requirements adopted at the S4-X bundle adjudication (2764 §4 items
1–6) and supplementary close (2765/2770 item 7); execution order per
2766 §7 / 2783 §3 item 1, pointed at the DM-1/2/3 OSF release path
(PRIME GOAL). Target of both instruments: the clean rv2714 residual —
a marginal, sign-definite, window-localized below-DH real-space
near-window slope (F1 2.56σ at a_s = 0.04, 2.82σ at 0.02;
κ_fit = 0.9032 × κ_D at 0.04) with k-space and far-window quiet
(F3 0.49σ, F2 0.53σ). The legacy 5.8–6.6σ X6 numbers are DEAD
(2714 self-pair defect); nothing in this prereg inherits them.

**Standing fences:** CONV-005 v2 blocking gate (≥20 states × ≥20
moves per geometry/code-path, |ΔH_inc − ΔH_full| ≤ 10⁻¹⁰·max(1,|ΔH|),
inverse-move antisymmetry, PASS line quoted in the record) precedes
EVERY production run; ANY gate failure blocks and the session reports
the defect. CONV-003 provenance on every load-bearing number.
CONV-006 authentication-before-adoption for any artifact found
uncommitted. Machinery = the committed 2761 clean pipeline VERBATIM
(fixed A path, S-drift fresh-summation checks at chunk boundaries,
checkpointed chunking) with ONLY the parameter/seed changes licensed
below. Candidate (B) 79.5% is NOT in scope; the v3 enactment does not
convene here; promotion remains barred until PR1–PR7 are all
evaluable. Same-font reporting of every committed outcome.

**Frozen physics constants (2714/2761 lineage, CONV-003):**
ℏc = 197.3269788, α_EM = 1/137.035999084, φ = (1+√5)/2,
a = 0.589/φ fm, κ_D = 2.0/a, n_CP = 2√2/a³, soft-core pair
interaction z_i z_j·[erfc + 1/√(r² + a_s²)] Ewald decomposition
exactly as `code/2761_rv2714_execution.py`.

**Reserved seeds (fresh, continuing the 20260798–802 block):**
20260803–20260816 inclusive, assigned per-chain below. No seed is
reused; a chain restarted for any reason resumes from checkpoint,
never re-seeds.

---

## §1 — X3: clean replication at the tension points [→ PR1 fluke-exclusion]

The charter's X3 ("one longer independent chain at the tension
point") is instantiated at BOTH clean tension points, since the clean
residual appears at both a_s values with the same sign:

| Chain | N | a_s (fm) | seed | eq | production sweeps |
|---|---|---|---|---|---|
| X3-R04 | 686 | 0.04 | 20260803 | 600 | 4800 (2× RV-MAIN) |
| X3-R02 | 432 | 0.02 | 20260804 | 400 | 3200 (2× RV-CORE) |

Committed observable per chain: the F1 near-window slope ratio
κ_fit/κ_D on the frozen windows verbatim from the RV-3 battery —
(0.08, 0.546) fm at a_s = 0.04; (0.04, 0.546) fm at a_s = 0.02 —
with **block-bootstrap covariance-aware errors (binding requirement
1): 24 equal contiguous sample blocks, 2000 bootstrap resamples,
fit re-run per resample; the quoted error is the bootstrap standard
deviation** (frozen here; no diagonal-error fits for any verdict
quantity anywhere in X3/X4).

**Committed replication classes (frozen):**
- **REPLICATED:** both chains individually give κ_fit/κ_D < 1, each
  consistent with its RV counterpart within 2σ combined, AND the
  pooled below-DH significance (inverse-variance combination of the
  four chains: RV-MAIN-A/B + X3-R04 at 0.04; RV-CORE + X3-R02 at
  0.02, then Stouffer across the two a_s points) is ≥ 3σ.
- **NOT-REPLICATED:** either new chain gives κ_fit/κ_D ≥ 1, OR the
  pooled significance falls below 2σ.
- **INCONCLUSIVE:** anything else.

REPLICATED converts the residual from "candidate" to "reproducible
feature of the clean pipeline" for PR1 accounting; NOT-REPLICATED
records the RV residual as statistical and PR1's F1 line is
re-evaluated on the pooled dataset. No PR1 verdict is enacted here in
any branch — X3 feeds the consolidated S4-X report; the panel
disposes.

---

## §2 — X4: the GP-limit ladder [→ PR2, verbatim bar]

PR2 (frozen, verbatim): ladder at minimum a_s = {0.04, 0.02, 0.01,
0.005} fm; ≥2 system sizes AND ≥2 independent chains at every
a_s ≤ 0.01 fm; joint (a_s, 1/L) extrapolation; **PASS bar:
κ_eff/κ_D consistent with 1 within total uncertainty ≤ 3%, and no
significant sign-staggered response.** (0.002 fm extension = optional
strengthening, NOT committed here.)

**Committed chain matrix** (archived clean rv2714 chains are
incorporated where they satisfy a rung's requirements — CONV-003
provenance: `data/rv2714/`; every NEW chain gate-v2-gated):

| Rung a_s | Chains (N, seed) | Status |
|---|---|---|
| 0.04 | 686 (RV-MAIN-A), 686 (RV-MAIN-B), 432 (RV-SIZE-S), 1024 (RV-SIZE-L) | archived |
| 0.02 | 432 (RV-CORE) archived; **686, seed 20260805**; **1024, seed 20260806** | mixed |
| 0.01 | **432, seed 20260807; 432, seed 20260808; 686, seed 20260809; 1024, seed 20260810** | new |
| 0.005 | **432, seed 20260811; 432, seed 20260812; 686, seed 20260813; 1024, seed 20260814** | new |

(≥2 sizes and ≥2 independent chains at 0.01 and 0.005: satisfied by
construction — 432×2 + 686 + 1024 per rung.) New-chain lengths: eq
400 / production 1600 at N = 432; eq 600 / production 2400 at
N ∈ {686, 1024} (the RV lengths, verbatim). Sampling cadence, k-shell
set (n² ≤ 27), profile binning: 2761 verbatim.

**Reserve chains (execute only if a committed chain's ESS < 100 on
the F1 window observable):** seeds 20260815–16, same geometry as the
deficient chain. Reserve activation is mechanical (the ESS
threshold), not discretionary, and is reported same-font.

**The seven binding requirements — frozen operationalizations:**

1. **Covariance-aware fitting:** block bootstrap as §1 (24 blocks ×
   2000 resamples) for EVERY verdict quantity in X3 and X4.
2. **Sliding-window map κ_fit(r_min, r_max):** committed grid
   r_min ∈ {0.04, 0.06, 0.08, 0.12, 0.16, 0.24} fm ×
   r_max ∈ {0.40, 0.546, 0.70, 0.88} fm (cells with r_min ≥ 2a_s
   only), computed per chain, reported as the full map with
   bootstrap errors.
3. **Two-component-form test:** on each rung's pooled profile, fit
   (A) single-Yukawa κ vs (B) Yukawa + second exponential mode
   (κ₂ free, amplitude free), covariance-aware likelihood;
   committed discriminant: ΔAIC ≥ 10 favoring (B) AND (B)'s
   asymptotic κ consistent with κ_D within 2σ ⇒ TRANSIENT-MODE
   reading (near-window residual is short-range structure, DH
   asymptotics intact); single-mode preferred with κ < κ_D at > 2σ
   ⇒ ASYMPTOTIC-SHIFT reading; else UNRESOLVED-FORM.
4. **Joint real/k-space fit, ONE shared asymptotic pole:** per rung,
   simultaneous fit of the real-space window profile and the small-k
   k²/S_zz intercept with a single shared κ_joint; report
   κ_joint/κ_D with bootstrap error.
5. **Explicit 1/L finite-size scaling of the F1 extraction:** at
   a_s = 0.04 (three archived sizes) and every new multi-size rung,
   fit κ_fit(L) = κ_∞ + c/L; **the PR2 extrapolation quantity is the
   joint (a_s, 1/L) surface fit κ(a_s, L) = κ_∞∞ + c₁·a_s^p + c₂/L
   with p ∈ {1, 2} selected by AIC (both reported)** — κ_eff ≡ κ_∞∞
   evaluates the PR2 bar.
6. **Moving-feature discriminant:** per chain, the deficit profile
   Δ(r) = ln g_env^sim(r) − ln g_env^DH(r) on the frozen binning;
   r* = argmax |Δ| within (2a_s, 3/κ_D). Committed: r* stable within
   15% across sizes at fixed a_s ⇒ FIXED-R (physical structure);
   r* correlated with L (Pearson |ρ| > 0.9 across ≥3 sizes and
   monotone) ⇒ FINITE-SIZE; else UNRESOLVED-LOCATION.
7. **High-resolution S_zz(k) vs HNC (cheap, archived-data leg —
   EXECUTES FIRST):** on the archived rv2714 accumulations, per
   chain, Δ(k) = S_zz^sim(k)/S_zz^HNC(k) with bootstrap errors at
   every committed shell with k ≤ 2π/(0.08 fm) — the near-window's
   conjugate range — explicitly reporting the k-range (if any) over
   which |Δ(k) − 1| > 2σ persists. HNC reference: the committed 2721
   solver (`code/2721_kinetic1_s3_hnc.py` lineage) at each rung's
   (a_s, n_CP, θ), verbatim.

**Committed X4 verdict (frozen):** PR2 PASS iff κ_eff/κ_D ∈
[0.97, 1.03] with total (bootstrap ⊕ extrapolation-model spread)
uncertainty ≤ 3% AND the sign-staggered response check (the frozen
RV-4 alternation battery, verbatim) fires zero significant
alternations on all new chains. PR2 FAIL iff κ_eff/κ_D outside the
band by > total uncertainty, or significant staggering appears.
PR2 UNRESOLVED otherwise. The verdict is recorded; enactment into
the PR ledger is panel business at the consolidated S4-X report.

---

## §3 — Execution and reporting contract

- **Order:** requirement-7 archived-data leg first (no new compute);
  then X3 chains; then X4 rungs ascending in cost (0.02 completions,
  then 0.01, then 0.005). Chunked, checkpointed, resumable across
  session windows per the 2761 pattern; chunk boundaries always at
  the S-drift check. AUTOMATON-1 scheduling may interleave; its
  prereg is separate (queue item 2).
- ONE record file `s4x_x3x4_record.md`, appended per completed leg,
  each append a numbered patch with reasoning fragment + scripts per
  the reasoning-capture rider. Gate-v2 PASS lines quoted per
  geometry.
- Partial-state honesty: if a session closes mid-ladder, the record
  states exactly which chains are complete; NO committed quantity is
  computed on a partial chain.
- No new registry IDs (CLONE-FIRST run at freeze: `s4x_x3x4_record`,
  seeds 20260803–16 unclaimed; no collisions).
- **Freeze declaration:** every chain geometry, seed, length, window,
  grid cell, fit form, threshold, class boundary, and verdict rule
  above was fixed before any new number was computed. The archived
  rv2714 numbers quoted are of record (2763) and are inputs, not
  outcomes. A discovered defect voids the affected leg and requires a
  fresh prereg patch, stated same-font — and, per the 2785 D1 lesson,
  this prereg's internal consistency was machine-checked at freeze:
  every committed (a_s, r_min) sliding-window cell satisfies
  r_min ≥ 2a_s; every rung at a_s ≤ 0.01 has ≥2 sizes and ≥2 chains;
  no seed collides with the 20260798–802 block or any earlier
  reservation.

---

## §PA-1 — PREREG ADDENDUM (Patch 2788; panel authority Q5: S4 archival advisory + S1 diagnostic-scope rationale, ratified 5–0)

Output-format addition only — no frozen prediction, threshold,
window, seed, or analysis rule changes: **every NEW X3/X4 chain
archives per-sample S_zz(k) (all committed shells) and per-sample
profile blocks**, so requirement-7-class comparisons on these chains
support the preregistered per-sample bootstrap that the rv2714
archive could not. DEV-1's diagnostic-envelope error model remains
ratified for the archived-data leg only; shellwise uncertainties
under DEV-1 are diagnostic envelopes and support no individual-shell
discovery claim.

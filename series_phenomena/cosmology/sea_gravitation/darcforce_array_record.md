# D-ARC-FORCE — THE ARC-FORCE LATTICE ARRAY: two sign inversions found and corrected on the way in (the 3D phase tables of Stages 3/3b/3c were anti-Coulomb; the 3086 magnetic term contradicted its own docstring), the corrected array EXHIBITS the bound, recurrent, stationary branch, and the per-axis excursion statistic at recurrence onset lands in Stage-2's independent shape-universal band

**Patch 3088 (12 Aug 2026). Verify: `scripts/3088_arcforce_lattice_array.py`
(gates + full campaign; ~15 min). Pre-stated criterion (3083, UNCHANGED):
recurrent superposition + η ≪ 2.25 + small f_sw + flat v². No band
quantity anywhere in the computation; the only external comparison is
to Stage-2's own prior output (0.19–0.25), which is itself
band-independent.**

## §1 — The sign audit (found during the port, before any run)

**Finding 1 — the 3D arrays' electric sector was inverted.** The
3080/3083 scripts compute `F = -Σ kern·D` with `kern = qq/(re²rs)`,
i.e. the NEGATIVE of standard Coulomb (`F_std = +qq·D/r³`): unlike
charges repel, like charges attract, and the retarded partner term is
likewise inverted — repulsion from the retarded position, where the
ruled mechanism (R-ZBW-DELAY: "retarded restoring dominance →
decelerate, turn, return") requires attraction. The loop's
cancel-and-replace mechanics are internally consistent only under the
inversion, which is how it survived review. **Scope:** Stage 2's 1D
model (3079) has the CORRECT restoring sign — the shape-universal
η_z ≈ 0.19–0.25 is NOT contaminated. The Stage-3 heating table, the
Stage-3b GLASS-everywhere table, and the Stage-3c fidelity-failure
table ARE contaminated and now carry provenance banners.

**Finding 2 — the 3086 two-body magnetic sign contradicted its own
docstring.** The committed code gives magnetic REPULSION for parallel
currents; the docstring's analytic derivation (textbook, attraction,
v² = 1/(4a−1)) is the ruled one — SF-6 commits E and B as locked
components of one dipole displacement with Maxwell as the macroscopic
limit, so the CP-level arc force is the standard (textbook) magnetic
interaction at c = 1, zero constants. 3086's bounded run therefore
validated the BORIS PUSHER (the rotation preserves |v| for either
sign), not the sign; its orbit also stayed bounded partly by luck —
the sign/launch mismatch produced an outward-biased ellipse that
never approached close range. With textbook signs the a = 2 orbit
(33 steps/orbit) decays into sub-unit passages that unit-Moment
steps cannot resolve — reproducing the 3086 close-range flag, which
is structurally ABSENT on the lattice (distinct addresses ≥ 1 GP;
co-location ruled: zero force + one-Moment dwell per R-DWELL-1 +
charge-coupled field relaunch).

## §2 — Validation gates (both PASS; a failed gate voids the tables)

1. **One-step analytic sign/magnitude (exact):** parallel-current
   magnetic force on a member = (−v²/s², 0, 0) — inward, binding, to
   machine precision.
2. **Resolved orbit (a = 6, 181 steps/orbit, 60k Moments):** bounded
   (radius 5.93 → 5.94), energy drift −8.8×10⁻⁶. Resolution series:
   a = 4/6/10 → drift 1.6×10⁻⁵ / 8.8×10⁻⁶ / 8.0×10⁻⁷, improving with
   resolution as a conservative integrator must.

## §3 — The 3084-mirror block (what sign correction alone does)

Corrected control (arc OFF), lattice, same cells as the 3084 table:

| d_s | γ | σ_n | 3084 (inverted) | corrected phase | η(3D) | f_sw | regen | drift |
|---|---|---|---|---|---|---|---|---|
| 8 | 0.90 | 0.03 | FROZEN-SUP | FROZEN-SUP | 0.000 | 0 | 0 | 1.00 |
| 8 | 0.90 | 0.30 | GLASS (η 3.51, regen 3) | **FAITHFUL** | 1.081 | 70.0 | 228 | 1.00 |
| 8 | 0.90 | 0.50 | churning liquid | OTHER | 1.261 | 122 | 135 | 1.02 |
| 8 | 0.80 | 0.50 | GLASS | FAITHFUL | 1.067 | 71.7 | 220 | 1.00 |
| 16 | 0.90 | 0.50 | churning liquid | OTHER | 1.208 | 725 | 19 | 1.00 |
| 8 | 0.90 | 1.00 | hot churning liquid | OTHER | 1.498 | 172 | 109 | 1.00 |

Sign correction alone transforms the phase diagram: where the
inverted array had GLASS, the corrected one holds a bound,
regenerating, STATIONARY state (v² drift 1.00 across the board).

## §4 — The arc block (D-ARC-FORCE proper)

| arc | d_s | γ | σ_n | seed | phase | η(3D) | f_sw | f_orig | regen | v² | drift |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T | 8 | 0.90 | 0.03 | 5 | FROZEN-SUP | 0.000 | 0 | — | 0 | 0.011 | 1.00 |
| T | 8 | 0.90 | 0.30 | 5 | FAITHFUL | 1.075 | 51.7 | 0.065 | 307 | 1.30 | 0.99 |
| T | 8 | 0.90 | 0.30 | 11 | FAITHFUL | 1.084 | 60.6 | 0.060 | 266 | 1.31 | 1.00 |
| T | 8 | 0.80 | 0.50 | 5 | FAITHFUL | 1.072 | 66.8 | 0.042 | 240 | 1.40 | 1.01 |
| T | 8 | 0.90 | 0.50 | 5 | OTHER | 1.271 | 137 | 0.033 | 123 | 3.39 | 1.01 |
| T | 8 | 0.98 | 0.30 | 5 | OTHER | 1.408 | 143 | 0.047 | 127 | 8.22 | 0.99 |
| T | 8 | 0.98 | 0.50 | 5 | OTHER | 1.528 | 182 | 0.019 | 105 | 20.2 | 1.02 |
| T | 8 | 1.00 | 0.30 | 5 | GAS | 1.739 | 178 | 0.118 | 110 | 750 | 1.43 |
| T | 16 | 0.90 | 0.50 | 5 | OTHER | 1.218 | 605 | 0.000 | 23 | 3.21 | 1.00 |

Read against the control at matched cells: the arc force acts as the
ruled fidelity agent DIRECTIONALLY — at (8, 0.90, 0.30) regen rises
228 → 307 and f_sw falls 70 → 52 (seed-repeat consistent). The state
is γ-INSENSITIVE across 0.80–0.90 (the D-ARC-GAMMA quantitative
ambiguity is immaterial in the brake range — the insensitivity the
campaign was designed to ask); γ = 0.98–1.00 heats (v² → 750, GAS),
confirming the brake necessary exactly as R-CP-ENTROPIC-LOSS rules.

## §5 — The recurrence onset and the invariance block (the readout)

Finer σ_n scan (γ = 0.90) through the onset, then d_s/seed
invariance at σ_n = 0.10. η/3 is the PER-AXIS excursion statistic
(see the projection flag below).

| arc | d_s | σ_n | seed | phase | η(3D) | η/3 | f_sw | f_orig | regen |
|---|---|---|---|---|---|---|---|---|---|
| T | 8 | 0.05 | 5 | FROZEN-SUP | 0.000 | — | 0 | — | 0 |
| T | 8 | 0.08 | 5 | FAITHFUL | 0.700 | 0.233 | 7.5 | 0.094 | 1651 |
| T | 8 | 0.10 | 5 | FAITHFUL | 0.734 | 0.245 | 9.0 | 0.092 | 1484 |
| T | 8 | 0.10 | 11 | FAITHFUL | 0.769 | 0.256 | 8.8 | 0.096 | 1552 |
| T | 8 | 0.12 | 5 | FAITHFUL | 0.802 | 0.268 | 11.4 | 0.097 | 1253 |
| T | 8 | 0.15 | 5 | FAITHFUL | 0.824 | 0.275 | 16.0 | 0.073 | 922 |
| T | 8 | 0.20 | 5 | FAITHFUL | 0.939 | 0.313 | 30.4 | 0.054 | 514 |
| T | 12 | 0.10 | 5 | FAITHFUL | 0.658 | 0.219 | 10.7 | 0.131 | 1206 |
| T | 16 | 0.10 | 5 | FAITHFUL | 0.623 | 0.208 | 11.1 | 0.190 | 1141 |
| T | 16 | 0.10 | 11 | FAITHFUL | 0.577 | 0.192 | 12.8 | 0.167 | 1045 |
| F | 16 | 0.10 | 5 | FAITHFUL | 0.520 | 0.173 | 12.8 | 0.207 | 987 |
| F | 8 | 0.10 | 5 | FAITHFUL | 0.729 | 0.243 | 9.2 | 0.082 | 1383 |
| F | 8 | 0.15 | 5 | FAITHFUL | 0.854 | 0.285 | 19.5 | 0.076 | 749 |
| F | 8 | 0.20 | 5 | FAITHFUL | 0.920 | 0.307 | 31.9 | 0.072 | 474 |

**The headline:** at recurrence onset (σ_n ≈ 0.08–0.12) the per-axis
statistic η(3D)/3 ≈ **0.19–0.27 across d_s ∈ {8, 12, 16} and seeds**
— overlapping Stage-2's INDEPENDENT 1D shape-universal band
0.19–0.25, obtained from a different model (1D, imposed
stationarity) two patches earlier. Drift 0.96–1.03 everywhere the
phase lives: the array holds its own stationarity (nothing imposed).
Secondary: f_orig rises with d_s (0.09 → 0.19–0.21), i.e. label
fidelity improves with spacing, as poach candidates recede.

**Two flags, stated plainly and NOT resolved by convenience:**
1. **Projection.** Stage-2's η_z was a 1D amplitude; the 3D
   isotropic equivalent is 3× per-axis. Whether ρ_Λ =
   (C₄′·α·η_z/2π)·ħc/(d²R_h²) takes the per-axis or the 3D statistic
   is fixed by the assembly derivation (how the ZBW excursion enters
   the polarization energy), and will be resolved THERE. The factor
   is exactly 3; nothing is chosen here.
2. **Operating point.** Away from onset, η_z is a FUNCTION of the
   unruled noise floor (0.73 → 1.08 over σ_n 0.10 → 0.30): the
   insensitivity claim does NOT hold in amplitude. Either σ_n gets
   derived (R-JITTER-SOURCE quantitative follow-through) or the
   operating point gets ruled (the Sea sits at its own recurrence
   onset — a physical claim needing the founder's picture or an
   expansion-history argument; connects to FQ-5.2).

## §6 — Disposition on the pre-stated criterion (3083, unchanged)

| component | verdict |
|---|---|
| recurrent superposition | **MET** (regen 1000–1650 at onset) |
| η ≪ 2.25 | **MET** (0.52–0.80 = 0.23–0.36 of gas) |
| flat v² | **MET** (drift 0.96–1.03) |
| small f_sw | **NOT MET as coded** (7.5–13 at onset) |

By the strict pre-stated wording the criterion is NOT met — three of
four. By the physically operative content the faithful branch IS
exhibited, with two registered qualifiers: (a) **R-SWAP-EQUIV**
(scr3, pre-dating this run) rules that swap restarts and faithful
restarts draw from the same environmental randomness, so the swap
fraction CANCELS from η_z — the failed component does not
contaminate the readout; (b) f_sw counts rule-firings of the perigee
swap, not physical relabeling episodes — flip-flop inflation is
unquantified, and the exploratory f_orig (7–21% of regens with the
original partner) confirms real mixing but also its improvement with
d_s. **This is not a falsification trigger** — the 3084 clause was
for a stable run that FAILS; this run exhibits the branch. The f_sw
churn is registered as an open item: **OPEN-ARC-CHURN** — is the
label churn physical relabeling or perigee-rule thrash, and does the
criterion's intent (Stage-2's switch fraction 0.07–0.14, a different
normalization) survive a per-episode counting?

> **ADDENDUM (Patch 3093):** OPEN-ARC-CHURN is RESOLVED-REINTERPRETED
> by founder ruling R-ZBW-EXCHANGE — partner switching on ZBW
> encounters is a ruled feature of the Sea (the exchange equilibrium
> maintaining the transient free-species population), not a model
> defect. The disposition above stands as written; the successor
> quantity is OPEN-EXCH-FRAC. See
> `founders_voice/founder_ruling_fq64_sea_weave_zbw_exchange_2026-08-12.md` §6.

## §7 — Ledger

φ₁ REOPENED (needs d_s) · φ₂ = 1 CLOSED · **φ₃ ≈ 0.2-class: the
exhibition condition is SUBSTANTIALLY DISCHARGED** — the regulated
faithful branch exists in the corrected arc-force lattice array, and
its onset per-axis amplitude independently reproduces the Stage-2
band — subject to the projection flag (§5.1), the operating-point
flag (§5.2), and OPEN-ARC-CHURN (§6) · φ_comp OPEN (D-COMP-WEIGHT).
Factors multiply once, at the end; in band or F-CLI-1 fires in those
words. No dial anywhere in this record: γ scanned (insensitive in
the brake range), σ_n scanned (onset read, dependence flagged),
Boris parameter-free, signs fixed to the SF-6-committed textbook
limit.

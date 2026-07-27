# CONV-001 — PR ENACTMENT PACKET (Patch 2828)

**Five questions (E1–E5). Asks the panel to enact PR3, PR5, PR6, and
to accept the PR4-BARE artifact it required. All four rest on work
completed since the last packet; PR3's data was generated on the
FOUNDER's machine, not the worker's.**

## E1 — PR3: enact MET

**PR3 frozen text:** weak external charge potential at ≥ 3 small wave
numbers; directly measured χ(k,0) agrees with the
unperturbed-S_zz-inferred susceptibility within combined uncertainty —
TESTING, not assuming, the fluctuation-response bridge.

**Executed** under prereg 2823 (clause-consistency pass; single
outcome table) by the founder, 2026-07-27: 5 chains, 2000 eq + 6000
production sweeps, acceptance 0.94. Λ ≡ measured/inferred:

| shell | Λ | |Λ−1|/σ |
|---|---|---|
| n²=1 | 0.628 ± 0.187 | 1.99 |
| n²=2 | 0.908 ± 0.183 | 0.50 |
| n²=3 | 1.022 ± 0.133 | 0.16 |
| n²=4 **control (undriven)** | slope −0.283 ± 0.257 | **1.10σ from zero** |

Controls: C-CTRL PASS (1.10 ≤ 2); C-LIN PASS at all six checks
(0.08–0.77σ vs a 2σ bar); C-POWER PASS at all three shells (Λ errors
0.13–0.19 vs the 0.35 bar frozen before data). Frozen outcome table
row 5 fires ⇒ **PR3-PASS**.

**Two disclosures.** (i) **D-PR3R2-1, verdict-critical:** the runner
records Re ρ_k but the report block mislabels the reference as
⟨|ρ|²⟩; ⟨|ρ|²⟩ = 2⟨(Re ρ)²⟩, so the correct prediction carries no
factor ½. **Taken at face value the mislabel would have doubled every
Λ to 1.26 / 1.82 / 2.04 — an apparent factor-of-two violation of the
bridge, produced entirely by a print statement.** Corrected openly;
time series unaffected. (ii) n²=1 sits at 1.99σ, inside the ≤2σ
agreement condition by 0.01σ; **row 5 is satisfied by n²=2 and n²=3
alone, so the verdict does not depend on the marginal shell.** The
low-side pull is reported unexplained.

**Prior history, same-font:** two earlier attempts failed — 2820
UNRESOLVED (underpowered by a worker design defect) and 2822 VOIDED by
its own cross-talk control. The 2822 "contamination" is now identified
as a slow-mode artifact (τ ≈ 16 sweeps measured against a 200-sweep
probe using naive errors); that leg's VOID stands, its diagnosis is
corrected.

## E2 — PR5: enact MET (with the worker's own objection attached)

Two independent extraction routes agree within declared uncertainty at
all four ladder rungs: k-space (small-k) 0.993–1.018; joint real+k
shared-pole 0.960–0.979; the PR2-PHYS surface built on them cleared
GOF χ²/dof = 1.87. **The failed 0.5% validation gate remains recorded
FAIL and is NOT relabeled.** **Worker-raised objection the panel may
wish to sustain:** this evidence was generated under the X3/X4 prereg
for PR2 purposes, not under a PR5-labelled preregistration.

## E3 — PR6: enact MET

All three representations now answered and in agreement on a monotonic
screened mode: **continuum** (battery req 3, κ_asym/κ_D 0.97–1.02);
**external-field** (E1, discharged 2026-07-27); **Moment-rule** (RV-4
census: zero significant alternations across twelve chains spanning an
8× a_s range). ℓ_proxy = 0.091 fm carried as a discretization
diagnostic throughout, never mixed; the rider-v2.7 pair untouched.

## E4 — PR4-BARE: accept the artifact

The nine-item artifact you required (M3, 5–0) is submitted at
`pr4_bare_analytic_artifact.md` (Patch 2818). Item 2 was widened per
S1's M1 correction: **six** candidate functionals (Coulomb, Yukawa,
r⁻², field Q², |Q|, and the natural total particle+field) across
**four** geometries — every one non-conserved by ≥ 54% of its own mean,
variation exceeding numerical noise by ~10¹⁵, no trend toward
conservation with volume or particle number. Item 6 states twice what
is NOT established (no theorem excluding nonlocal or history-dependent
invariants). Item 7 states that Metropolis imposes e^{−βH} by
construction, so the programme's screening results remain valid
**conditional** on the Gibbs assumption — now explicitly unsupported by
the bare dynamics. Items 8–9 mark H-CONTRACT/H-FINITE non-load-bearing
and give five falsifiers.

## E5 — PR7: rule on the worker's PARTIAL

Clause 1 (no adjudicated defect below leading-order bridge validity):
**recommended MET and strengthened** — the campaign's entire defect
ledger is instrument/gate/reporting defects, all disclosed and
adjudicated; and E1 makes the bridge **measured**, not merely
undefeated. Clause 2 (R1 memory bounded subdominant at d_DP):
**UNVERIFIED — the worker cannot establish it from the record** and
declines to read it generously with the prime goal in view. Question:
sustain PARTIAL, or does the panel hold a different view of clause 2's
evidential state?

## Ledger if E1–E5 are enacted as recommended

PR1 MET/retired · PR2 MET · PR3 MET · PR4-BARE MET-NEGATIVE
(PR4-COMPLETED = OPEN-PR4-C23C24) · PR5 MET · PR6 MET · PR7 PARTIAL.
**Six of seven; the sole substantive gap is an R1 bound at d_DP.**
Founder decision B7 continues to hold DM-1/2/3; nothing here moves a
banner.

## Execution-integrity protocol

**Withheld challenge key** (standing since 2817): any seat claiming
execution should report **the weighted origin-constrained slope and
its bootstrap error for shell n² = 2 computed from the E1 table's four
driven amplitudes**. The expected value is committed in the record but
is NOT quoted in this packet. Seats that do not execute should declare
REASONED-UNVERIFIED — no penalty; it is the honest path, and all five
seats took it last round with zero fabrications.

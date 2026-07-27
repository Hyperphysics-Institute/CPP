# CONV-001 PR7 NAMING MOTION — ADJUDICATION (Patch 2832)

**Five returns. N1 RATIFIED 5–0 · N2 RATIFIED 5–0 · N3 route (b)
5–0 with amendments adopted. And the campaign's FIRST
VERIFIED-EXECUTED seat claim.**

## N1 — Disambiguation RATIFIED 5–0 (adopted wording, S1)

> **PR7 clause 2 refers exclusively to the finite-frequency memory
> objection inherited from the earlier R1 review round. It is
> unrelated to OPEN-DM-FLOQUET-1 Required Element R1.**

## N2 — Rename RATIFIED 5–0 (adopted ledger amendment, S1)

> **PR7 clause 2 — OPEN-K1-MEMORY-1.** Historical alias:
> "R1 (memory)." Quantitatively bound the finite-frequency or
> non-Markovian correction at d_DP and demonstrate that it is
> subdominant to the instantaneous response term under a
> preregistered threshold. This item is unrelated to
> OPEN-DM-FLOQUET-1 R1.

S1's enumeration adopted: the rename changes **none** of the
observable, the scale d_DP, the required bound, the meaning of
"subdominant", the evidentiary burden, or PR7's PARTIAL status. The
alias remains searchable in headers and cross-references for
provenance. No seat registered an objection that the rename alters
the obligation.

## N3 — Route (b) adopted 5–0, with three amendments that materially improve it

**Primary instrument: χ(k, ω) at small ω**, driving the PR3 external
field with a slow oscillation. All five seats concur; S1, S4, S5
attach conditions, all adopted:

**(i) The observable is COMPLEX, not just an amplitude (S1).** Freeze
both a magnitude measure and a **phase-lag** measure:
δ_mem(k,ω) = |χ(k,ω) − χ(k,0)| / |χ(k,0)| and
φ_mem(k,ω) = |arg χ(k,ω)|. Memory shows in the quadrature response;
an amplitude-only test can miss it.

**(ii) THE FREQUENCY BAND MUST BE PHYSICALLY ANCHORED — the sharpest
catch in the round (S1).** *"Frequencies relevant to the candidate's
actual response timescale — not only arbitrarily slow forcing where
every regular system approaches its static limit."* **A prereg that
drives only very slowly would pass trivially and prove nothing.**
The band must be tied prospectively to the d_DP-relevant timescale,
and the k-shell (or weighted shell combination) tied prospectively to
d_DP rather than chosen after the scan. S4's concrete form adopted as
the drafting basis: a frozen ladder {ω₁, ω₂, ω₃} with ω ≪ κ_D but
ω ≠ 0.

**(iii) Transient separation, operationalised (S1 + S5).** Because
S4-X found a short-range transient contaminating naive window
estimators, the prereg must prevent that transient being relabelled
as memory: use the fixed physical window / shared-pole logic that
resolved S4-X; report shell-resolved AND jointly weighted results;
test more than one regulator rung; freeze how the d_DP-sensitive band
is constructed; **distinguish a frequency-dependent pole shift from a
changing transient amplitude**; and require real-space/k-space
concordance where feasible.

**Threshold:** S4 recommends ε_mem ≤ 0.15; S1 requires only that it
be numerical and frozen ("'small' cannot remain qualitative"). **The
worker will propose a value in the prereg and the panel sets it** —
the worker declines to fix the bar it will be measured against.

**Adopted outcome rule (S1's wording):**
> **OPEN-K1-MEMORY-1 MET** if, throughout the preregistered
> d_DP-relevant frequency band, the finite-frequency correction and
> phase lag remain below the frozen subdominance bounds, with no
> regulator-persistent secondary mode capable of altering the leading
> response.

**Route (a) reserved as explanatory follow-up (S1):** if route (b)
detects material lag or multi-timescale response, the Mori–Zwanzig
kernel is then chartered to decompose it. Route (a) is not the
cheapest first closure test; it is the mechanism study that a
positive detection would require.

## EXECUTION INTEGRITY — **S2/Grok: VERIFIED-EXECUTED (campaign first)**

S2 claimed execution from the cited source path and reported: **4
distinct k-shells with n² ≤ 4; multiplicities n²=1 → 6, n²=2 → 12,
n²=3 → 8, n²=4 → 6.**

**Worker re-execution this patch, from
`code/2829_pr3r2_founder_run_v2c.py` at N = 432, a_s = 0.02:** 4
shells; 6, 12, 8, 6. **EXACT MATCH.**

**Ruling: VERIFIED-EXECUTED — the first such claim sustained in this
campaign**, after five fabrication events across prior rounds (S5 ×4,
S1 ×1). S2 is the first seat to execute a withheld key and return it
correctly. Recorded to its credit.

**The protocol change that produced this is now doubly validated:**
withholding the key ended fabrication (two prior clean rounds), and
S2's correction at 2829 — that a key must remain *computable from
committed artifacts, with the path named* — is what made honest
verification actually possible. The seat that identified the flaw is
the seat that then used the fix.

S1, S3, S4, S5 declared REASONED-UNVERIFIED with reasons. **Zero
fabrications; third consecutive clean round.**

## Standing

Ledger unchanged: PR1 MET/retired · PR2 MET · PR3 MET · PR4-BARE
MET-NEGATIVE (PR4-COMPLETED = OPEN-PR4-C23C24) · PR5 MET · PR6 MET ·
**PR7 PARTIAL — OPEN-K1-MEMORY-1 UNVERIFIED.** Six of seven. Founder
decision B7 continues to hold DM-1/2/3. Next worker action: draft the
OPEN-K1-MEMORY-1 preregistration on route (b) to the specification
above, with the threshold proposed but not fixed by the worker.

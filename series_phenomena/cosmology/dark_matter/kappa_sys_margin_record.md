# κ_sys MARGIN — EXECUTION RECORD: GATE G1 FAILS (MARGINAL); THE FROZEN ROUTE C DESIGN EXECUTES; ITEM 1B REMAINS OPEN

**Patch 3052 (10 Aug 2026). The frozen pipeline
(`kappa_sys_margin_prereg.md`, Patch 3051; script
`code/3052_kappa_sys_margin.py`) run against the frozen Route A
ensemble. Reported exactly as printed; no threshold moved.**

## §1 — Census disclosure (factual-premise correction, before results)

The prereg text said "320 pairs per domain" — an arithmetic slip
(1280 files ÷ 4) made at metadata inspection; the actual census is
**std = 512 pairs, dom = 128** (matching the MEAS-2 record). The
prereg's operative word was ALL; the corrected primary uses all 512.
The 320-subset FIRST EXECUTION is disclosed: BOUND branch,
κ = 1.0515, 99% CI [0.668, 1.089], G1 FAIL — materially identical to
the corrected run; the slip changed nothing.

## §2 — Result (corrected primary, std domain, 512 pairs; gating)

- **|W| = 0**: the systematic deviation |D(t)| NEVER exceeds 3σ(t)
  anywhere in the post-transient window [48, 200). Peak |D| =
  6.92×10⁻⁴ at t = 158 vs σ(t_post) = 3.32×10⁻⁴ — the ensemble-mean
  response is consistent with zero throughout.
- BRANCH-BOUND fired from the last resolved point t_c = 28 (inside
  the transient): **κ_sys ≤ 1.0694, 99% CI [0.6414, 1.0859]**
  (full-pipeline bootstrap, 10000/10000 replicates resolved).
- **GATE G1: FAIL** — the CI includes 1 (marginal). δ = −0.086.
- Disclosed dom domain (128 pairs, non-gating): same shape — BOUND,
  κ = 1.0516, CI [0.879, 1.088].

## §3 — Honest physical reading (on the record, not a gate move)

The data show NO systematic memory above floor: the response relaxed
completely within the transient window and stayed at floor for 150+
Moments — QUALITATIVELY the L-6b claim's content, and consonant with
the Q1 no-tail diagnosis. But the frozen gate demands a MEASURED
contraction margin, and a response invisible at ensemble sensitivity
cannot yield one — the bound branch merely says the decay was at
least fast enough to hit floor by t_post, which brackets κ near 1
from the wrong side of resolvability. This is exactly the marginal
case the minority seats anticipated: the existing ensemble cannot
CERTIFY the margin. Per the ratified R3, their design now executes.

## §4 — Consequences (enacted per the ratified package)

- **G1 FAIL → the frozen Route C design class EXECUTES** (adjudication
  §1): matched exit-time domains; T_exit and T_BALL varied
  independently (arms with T_exit < T_BALL and > T_BALL; two
  geometrically distinct configurations sharing T_exit − T_BALL);
  the positive control must PASS in every inferential domain or that
  domain is prospectively non-interpretable.
- **NEW design requirement derived from THIS measurement** (for the
  Route C prereg): the systematic channel must be RESOLVABLE — design
  target peak|D|/σ ≥ 10 in every inferential domain. At β = 0.1 and
  512 pairs the peak reached ~2σ; the prereg patch chooses the
  (step amplitude, N_pairs) combination (e.g., a larger β step
  and/or more pairs) and freezes it BEFORE execution.
- **Item 1B: remains OPEN** (CONDITIONAL-DISCHARGE-PENDING resolves
  to NOT-DISCHARGED at this gate). The Q1 retirement and the trio's
  discharge do NOT finalize; OPEN-KMEM-TAIL-1 remains OPEN with
  Route C as the resolution vehicle. **Ledger: six of seven; PR7
  PARTIAL; B7 banners hold; Candidate (B) 79.5%
  PROVISIONAL-FAVORABLE — unchanged.**
- The L-6 amendment SPLIT (L-6a/L-6b) stands ADOPTED (it was not
  gate-conditional); L-6b's margin now attaches to Route C — which
  is the minority's original position, reached by the majority's own
  frozen mechanism.
- Enacted-and-standing regardless of the gate: all AUX discharges
  (QM-1 v2.12), the corpus sweeps, the neutrino rulings and STRUCT-1
  results, and the k < 71.5 bound.

## §5 — Next steps (in order)

(1) Route C preregistration patch: the frozen design class + the
resolvability requirement instantiated into concrete domains, step
amplitude, leg counts, S3-analog controls, and disposition tree —
frozen before any leg runs. (2) Founder mechanical action: Route C
executes on Kila6 (compute-scale estimate in the prereg patch).
(3) Single-round adjudication on completion, per the standing rule.

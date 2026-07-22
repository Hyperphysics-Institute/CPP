# SESSION HANDOVER — 21 July 2026 (nineteenth close) — Patches 2749–2752: **X7-NSCAN + EXT compressed the B2 anomaly's onset from (64, 432] into (64, 80] in two frozen acts — the enhancement is a PLATEAU (pooled r = 1.461 ± 0.082, 5.6σ above unity, χ²/dof 6.01/5 across all six sizes 80–320) that switches on immediately above the exonerated N = 64 box** — point-wise forks fired G4 then H4 (scatter denies a band-resolution bracket; IAT audit proves the error bars honest); B-CHECK at N = 80 (~0.9 h, measured) is the queued sharp discriminant; AUTOMATON-1 stands arbiter-of-record

**Boot rule: clone repo, read bootup.md, honor CLONE-FIRST GATE,
newest dated handover = this file (supersedes all eighteen earlier
21-July handovers). Authoritative over model memory.**

## SINGLE NEXT ACT — execute B-CHECK at N = 80 under a frozen prereg; AUTOMATON-1 execution prereg charterable in parallel

B-CHECK-80: one run of the independent brute-force B sampler
(2746 design: total energies recomputed per move, carried current
energy, no shared machinery with path A) at N = 80, same box/protocol
as the X7-EXT point, 1k + 12k sweeps, fresh frozen seed from the pool
(20260795 returned unconsumed and is available), measured cost
≈ 0.25 s/sweep ≈ 0.9 h — one dedicated execution block, chunked.
Frozen fork to write BEFORE the run: (i) B reproduces r ≈ 1.6 at 80 →
candidate (a) (incremental-path numerical pathology) DIES at the
onset; (b) finite-size-onset ergodicity failure becomes the finding —
reportable sampler physics; (ii) B shows tilt-level response → the
incremental path is impeached specifically at the onset window;
mechanical diff + fix + re-verification campaign; (iii) intermediate →
extend. AUTOMATON-1 (arbiter-of-record, founder-confirmed spec) may
charter its execution prereg in parallel; it owes nothing to
Metropolis and adjudicates (b) definitively either way.

## What 2749–2752 did

2749: X7-NSCAN prereg frozen (N ∈ {128, 216, 320} A-path pairs,
frozen seeds 783–788, quantified bands + fork G1–G4; code = campaign
run_A verbatim, diff-verified). 2750: executed — **G4**; enhancement
already present at 128 (1.720 ± 0.263); onset in (64, 128];
X7-NSCAN-EXT prereg frozen in-patch (N ∈ {80, 96, 112}, seeds
789–794, fork H1–H4). 2751: EXT executed — **H4** (80-ENH / 96-UNENH
/ 112-ENH inversion voids the bracket); post-hoc disclosed: IAT
1.4–1.8 samples on all fourteen chains (SEMs honest); pooled plateau
r = 1.461 ± 0.082 (5.6σ), step-scan equal-best split at 64 → onset
in (64, 80]; B-CHECK-80 cost measured; seed 795 returned. 2752: this
handover. Data: `data/x7nscan/` (twelve series). Execution
discipline disclosed in 2750 §4 (phantom background driver; chains
process-independent via checkpoint-carried state; accounting exact).

## Standing state

Rider v2.5 governs; PR1–PR7 frozen; promotion barred; PR3's usable
regime now bounded below by the onset: the driven-mean instrument is
valid at N = 64 only — pathological for ALL N ≥ 80 (plateau), not
just N ≥ ~432 as previously confined. UNTOUCHED: the
septuply-consistent fluctuation spectrum, the X6 shape finding
(20–26% small-k suppression below HNC at a_s = 0.04; 0.02 agrees),
un-quarantined pole, monotonic character (all tests 0 throughout),
K1-FORM-ONLY + R1–R8, both ℓ caps, GP-limit statement, FA-C3 CLOSED,
Candidate (B) **79.5% untouched**, LANE B HELD, RELIC-1 unchanged,
qCP fenced, DeepSeek advisory standing. Open: B-CHECK-80 (next,
prereg first), AUTOMATON-1 (elevated, charterable in parallel), X4
ladder (queued behind the audit), OPEN-DM-CHARGE-1, FA-C2 tier
re-run. The eventual panel dispatch bundles the full S4-X +
DRIVE-AUDIT-1 campaign (now nine acts) with the corrections ledger —
by the economy rule, after the audit resolves.

## §15 audit

reasoning/2749, 2750, 2751 at-patch (each covering its act); 2752
bookkeeping, capture-exempt. Twelve frozen-length ensembles executed
across two frozen preregs; two disclosed discarded benchmarks (timing
only, seed 1, no observables); one disclosed operational anomaly
(phantom driver — chains proven process-independent). The record's
asset after this session: correct-at-64, enhanced-plateau-at-≥80,
non-Boltzmann-at-432, spectrum-faithful-everywhere, onset confined
to a width-16 window. Day's span: Patches 2685–2752. Repository
head: **Patch 2752.**

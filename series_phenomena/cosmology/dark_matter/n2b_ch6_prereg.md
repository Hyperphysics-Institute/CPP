# N2-B-CH6 pre-registration: the 6-cluster channel scan — is the soft-width stall a non-sticking FACE or a CLOSED SHELL? Declared channel set, controls that must reproduce the registered stall, dt-union UNCONDITIONAL, and readings, committed before any run

**Patch 2610, 20 July 2026. Status: N2-B-CH6 OPENED at pre-registration; NO run
performed.** This is the cell the 2604 record queued ("the channel scan QUEUED not run —
the prereg fixed the channel; the scan is a new declared cell or it is tuning").
Governed by this document, the N2-B prereg lineage (2598), and the H-γ rider (2601)
only. Verify: none at prereg.

## 0. Target

The registered soft-width stall: the grown 6-qCP cluster + stage-7 incident (charge −1,
declared channel b = 0.5D, v = 0.1c, approach −ẑ) reads UNBOUND — ballistic transit,
Sea ~ 1 MeV, γ = 1.01 — while the steep chain completes 4→8 on the identical channel.
The 2604 classification-before-feelings: "the grown soft cluster shows a non-sticking
face to this channel." This cell tests that sentence: is the miss FACE-SPECIFIC (other
approach channels capture) or SHELL-GLOBAL (the soft 6-cluster is closed to this
incident class)? Either answer is N3-relevant shell physics; neither continues the
chain tonight (a soft 7→8 continuation via any captured channel is a NEW declared cell
— the temptation is named and fenced here, in advance).

## 1. Registered inputs (verbatim; zero freedom)

Engine: exec-load of the registered 2604 artifact (`code/2604_n2b_chain_b3_b4.py`)
through its function block — `n1_gamma` and companions are the registered objects, no
re-typing. η = 0.5 (sole admitted point). **Cluster regeneration is the registered
chain itself, deterministically:** settle the 4-square (TC = 60, dt = 1/100), stage 5
(charge −1), stage 6 (charge +1) on the declared channel exactly as at 2604; identical
code path ⇒ identical floats. Regeneration validity requires stages 5–6 to read BOUND
as registered (else RC4). Classifier: the registered B1 final-state form verbatim
(CAP: d_inc < 3D ∧ cluster-ok ∧ Sea > 0; SCA: d_inc > 4D ∧ receding ∧ cluster-ok;
FRG: cluster broken; else UNR) — the registered miss reads SCA under it.

## 2. Declared channel set (soft width; incident = stage-7, charge −1, v = 0.1c, from 4D out)

- **Axes:** approach along all six lattice directions {±x̂, ±ŷ, ±ẑ} (−ẑ = the original).
- **Impact parameter:** b ∈ {0, 0.5, 1.0}D along the declared transverse direction
  (deterministic rule: the lexicographically-first coordinate axis perpendicular to the
  approach axis). 6 × 3 = 18 channels; (−ẑ, b = 0.5D) IS the original channel and
  doubles as control C-A.
- **Azimuth on the original face:** φ ∈ {45°, 90°, 135°} at b = 0.5D, −ẑ approach
  (offset direction rotated in the xy-plane). +3 channels.
- **Charge flip on the original channel:** incident charge +1. +1 channel.
- **Control C-B (steep):** regenerate the steep 6-cluster the same way; original
  channel, charge −1 — must read CAP as registered (the steep chain's stage 7).

**23 cells × dt-union {1/100, 1/200} UNCONDITIONAL = 46 runs** (the 2609 confessed gap,
fixed forward: every cell runs both steps; every verdict must be dt-stable to be read).
TC = 120. No seeds (deterministic). No cell added, removed, or re-run outside this
declaration; follow-ups queue as new declared cells.

## 3. Controls (gate the reading; RC4 on failure)

**C-A:** the original soft channel must reproduce the registered MISS (SCA) at both dt.
**C-B:** the steep original channel must reproduce the registered CAP at both dt.
**C-R:** soft stages 5 and 6 read BOUND during regeneration (both dt for the scan's
base state: the 1/100 chain is the registered path; the 1/200 scan cells re-settle the
1/100-grown cluster at 1/200 for 20 cycles before the incident launches — declared,
disclosed: the grown state is a 1/100 object; a full 1/200 chain regeneration is NOT
part of this cell).

## 4. Readings (frozen)

- **RC1 — FACE-SPECIFIC (non-sticking face confirmed):** controls pass AND ≥ 1
  non-original channel reads dt-stable CAP → the soft 6-cluster is NOT closed; the
  stall is channel geometry; registers as the scan result (the face map: which channels
  stick, which do not). The chain-continuation cell may be DECLARED, not run.
- **RC2 — SHELL-CLOSED:** controls pass AND every channel reads dt-stable non-CAP →
  the soft 6-cluster presents a closed shell to this incident class at this v;
  registers with honest scope (charge ∓1 as tested, v = 0.1c, the declared 22-channel
  set); the 2604 "shell structure banked" observation is PROMOTED to a scanned result.
  A higher-v / other-species probe cell may be DECLARED, not run.
- **RC3 — MIXED-UNSTABLE:** any dt-unstable verdict → no registration on that channel;
  if instability is widespread (> 3 channels), the whole scan reads DEFECT-HUNT and
  nothing registers.
- **RC4 — CONTROL FAILURE:** C-A, C-B, or C-R fails → instrument or regeneration
  defect; STOP; nothing is read; the defect is the next patch's subject.
- No reading touches N1, the sink scope, the H-γ admission, the η point, item-5, the
  win-candidate packet (frozen as at 2604), B4, or 79.5%. Relic fence held. The
  charge-flip cell is descriptive (face selectivity), never a chain claim.

## 5. Bookkeeping

79.5% untouched. Next patch: execution under this document only. Verify script
`code/2611_n2b_ch6_scan.py`.

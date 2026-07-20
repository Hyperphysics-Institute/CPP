# N2B-FUNNEL-2 pre-registration: the funnel upper bound (b > 8D, ON, both widths) + the w = 2 OFF bracket stabilization — the two declared 2624 successors, committed before any run

**Patch 2639, 20 July 2026. Status: N2B-FUNNEL-2 OPENED at pre-registration; NO
run performed.** These are the two declared successors from the FUNNEL-1 record
(2624 §6: "offset grid b > 8D, ON, both widths" and "w=2 OFF bracket
stabilization (finer dt on the w=2 OFF family)"), carried in the 2636 handover
§3. Founder-free. Governed by this document and the FUNNEL-1 lineage (2620 →
2623 → 2624 M5). All quantities are classification quantities (CAP/SCA/UNR
class, deposit-free at reading level); v = 0.10c throughout — the DISC block is
not approached. Verify: none at prereg; execution next patch under this
document only.

## 1. Registered inputs (verbatim; zero freedom except the two disclosed items)

Engine: exec-load of the registered 2624 artifact (→ 2602 engine); `n1_gamma`,
`launch`, `classify`, constants are the registered objects. Single-incident
funnel cell on the settled 4-square, incident at [b·D, 0, 4D] with v = −0.10c ẑ,
TC = 120 — the registered 2624 M5 geometry, extended in b only. η = 0.5 (ON) /
η = 0 (OFF).

**Disclosed item 1 — the OFF-side classifier note.** The registered B1
classifier's CAP branch carries the conjunct `Sea > 0`. That conjunct is
sink-referential: at η = 0 the sink is algebraically removed and Sea is
machine-zero (2621 C2: −1.4×10⁻¹³ MeV), so its SIGN is floating-point residue,
not a physical observable. Hypothesis registered before any run: the 2624
"w = 2 OFF patchwork UNR/CAP" is at least partly this coin flip. The OFF-form
classifier for η = 0 cells = the registered classifier with the Sea conjunct
REMOVED (CAP iff d_inc < 3D ∧ sq_ok). Every OFF cell prints BOTH
classifications side by side (registered-form and OFF-form) plus the raw
classifier inputs (d_inc, vr, sq_ok, Sea) — nothing hides; the OFF-form reading
is primary for η = 0 iff control C-F2 passes.

**Disclosed item 2 — launch geometry at large b.** The registered launcher's
start height is fixed at 4D regardless of b; at b up to 16D the approach is
correspondingly oblique to the well. The funnel is defined IN the registered
geometry — the upper bound registered here is the registered instrument's upper
bound, stated as such.

## 2. Controls (gating; run FIRST)

- **C-F1 — convention-pin (METH-L2-015 pattern):** reproduce the registered
  2624 brackets: w = 4 ON b = 8 → CAP at dt = 1/200; w = 4 OFF last-CAP b = 5 /
  first-non-CAP b = 6 (registered-form classifier, dt = 1/200 legs). Failure →
  RC4, nothing reads.
- **C-F2 — OFF-form classifier conservatism:** the OFF-form classifier applied
  to the registered w = 4 OFF family must reproduce the SAME bracket
  (last-CAP 5 / first-non 6). If the OFF-form moves the registered w = 4
  bracket, the Sea-conjunct exposure extends to the REGISTERED record —
  disclosure-grade flag, the F2b family is read under BOTH classifiers with the
  discrepancy in front, and the 2624 R_f(OFF) = 5D entry is flagged for the
  founder's packet. (A control failure that is itself information; same font.)

## 3. Families (frozen grids)

- **F2a — upper bound (ON, η = 0.5):** b ∈ {9, 10, 12, 14, 16}D at both widths
  w ∈ {2, 4}, dt = 1/100 scan; dt-union {1/100, 1/200} on the bracket pair
  (last-CAP, first-non-CAP) exactly per the 2624 M5 protocol.
- **F2b — w = 2 OFF stabilization (η = 0):** b ∈ {1, …, 8}D at dt = 1/200
  (one halving finer than the 2624 scan); dt-union {1/200, 1/400} on the
  bracket pair. Both classifiers printed per Disclosed item 1.

Per cell, report class(es), d_inc, dcen; any FRG on its own line.

## 4. Frozen readings

- **RF-UB-BRACKET (per width):** a dt-stable (last-CAP, first-non-CAP) pair
  exists on the extended grid → **R_f(ON, w) registers as the bracket** — the
  funnel's upper bound is drawn; the 2624 "≥ 8D grid-exceeded" entry is
  superseded by citation.
- **RF-UB-EXCEED (per width):** CAP persists dt-stably through b = 16D →
  R_f(ON, w) ≥ 16D registers (lower bound raised 2×); the grid is declared
  exhausted at this instrument class and the successor is derivational (a
  reach that exceeds 16D at a 4D launch height is asking for the well's
  asymptotics, not a wider scan).
- **RF-UB-UNDRAWN (per width):** the bracket pair is dt-unstable → no upper
  bound drawn at that width; raw disclosed (the ROB-2 discipline: an
  instrument that disagrees with itself at marginal cells draws no walls).
- **RF-W2-DRAWN:** the w = 2 OFF family yields a dt-stable bracket under the
  primary classifier → **R_f(OFF, w = 2) registers**, and the 2620 RF1 class
  gate is then read at w = 2: R_f(ON, w2) − R_f(OFF, w2) ≥ 2D with both legs
  dt-stable → **RF1 (sink-mediated) EXTENDS to the soft width**; gate unmet →
  the w = 2 class registers as drawn-but-unclassified with the margin stated.
- **RF-W2-UNDRAWN:** dt-instability persists at {1/200, 1/400} → the w = 2 OFF
  boundary registers UNDRAWN-CONFIRMED at this instrument class; successor
  derivational. If the side-by-side classifier printout shows the instability
  living in the Sea coin flip alone (OFF-form stable, registered-form
  flipping), that diagnosis registers explicitly.
- Readings compose per width/family.

## 5. Fences

Classification only — no rates, no σ, no flux, no relic contact; deposits are
not read anywhere in this cell (Sea printed for OFF cells is a classifier-input
diagnostic at machine-zero scale, not a deposit); v = 0.10c only — the DISC
block is untouched; σ_cap 0.95c extension stays WITHHELD; EDGE-2(i) stays
queued; the 2624 record is NOT edited (superseded/flagged by citation only);
FW-1 is not implicated (no chain, no aimed-convention consumer sentence); AMB-1
untouched; **79.5% untouched under every reading.**

## 6. Bookkeeping

Prereg: this document (Patch 2639). Execution: `code/2640_n2b_funnel2.py`,
stages `controls | f2a | f2b`; record: `n2b_funnel2_record.md` (Patch 2640).
Reasoning fragments at both patches.

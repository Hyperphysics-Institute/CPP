# N2B-FUNNEL-2 execution record — VERDICTS RF-UB-BRACKET (w = 2: R_f(ON) ∈ [10, 12)D), RF-UB-UNDRAWN (w = 4; dt-stable floor raised to ≥ 9D), AND RF-W2-DRAWN WITH THE COIN-FLIP DIAGNOSIS CONFIRMED CELL-BY-CELL: R_f(OFF, w = 2) = 7D AND RF1 (SINK-MEDIATED) EXTENDS TO THE SOFT WIDTH

**Patch 2640, 20 July 2026.** Execution under `n2b_funnel2_prereg.md` (2639)
only. Verify: `code/2640_n2b_funnel2.py` (stages controls | f2a | f2b, all run).

## 1. Controls: BOTH PASS

- **C-F1 (convention-pin):** the registered 2624 brackets reproduce exactly —
  w = 4 ON b = 8 → CAP at 1/200; w = 4 OFF last-CAP b = 5 (REG = CAP) /
  first-non-CAP b = 6 (REG = SCA).
- **C-F2 (OFF-form conservatism):** the OFF-form classifier reproduces the SAME
  registered w = 4 OFF bracket (b = 5 CAP / b = 6 SCA). The fix is conservative;
  the OFF-form reading is primary for η = 0 per prereg. **Exposure disclosed at
  the registered bracket itself:** the b = 5 REG = CAP verdict rests on a
  residue of +5.7×10⁻¹³ MeV — the registered 2624 entry passed its Sea conjunct
  by the sign of machine noise that happened to land on physics's side. The
  bracket is confirmed under the fixed classifier, so the 2624 R_f(OFF, w4) = 5D
  entry STANDS with its exposure noted (no flag to the packet; the number is
  right).

## 2. F2a — the upper bound (ON, η = 0.5)

```
w=4 dt=1/100: b=9 CAP  b=10 SCA  b=12 SCA  b=14 SCA  b=16 SCA
  bracket: last-CAP b=9  -> 1/200 CAP   (dt-STABLE)
           first-non b=10 -> 1/200 CAP  (dt-UNSTABLE: SCA@1/100, CAP@1/200)
w=2 dt=1/100: b=9 CAP  b=10 CAP  b=12 SCA  b=14 SCA  b=16 SCA
  bracket: last-CAP b=10 -> 1/200 CAP   (dt-STABLE)
           first-non b=12 -> 1/200 SCA  (dt-STABLE)
```

- **w = 2 reads RF-UB-BRACKET:** **R_f(ON, w = 2) ∈ [10, 12)D**, both bracket
  legs dt-stable — the soft-width funnel's upper bound is DRAWN. The 2624
  "≥ 8D grid-exceeded" entry at w = 2 is superseded by citation.
- **w = 4 reads RF-UB-UNDRAWN:** the first-non-CAP cell (b = 10) flips
  SCA → CAP across the dt-halving; per the frozen reading (the ROB-2
  discipline), no upper bound is drawn at the steep width. The dt-STABLE
  last-CAP at b = 9 raises the standing lower bound: **R_f(ON, w = 4) ≥ 9D**
  (the same dt-union-stable CAP class the 2624 ≥ 8D registered on). Declared
  successor (NOT run; no escalation rung was pre-frozen for F2a): the w = 4
  bracket pair at dt-union {1/200, 1/400}.
- **Width coherence, registered as observation:** the soft width reaches
  FARTHER (bracket [10, 12) vs steep ≥ 9 with a marginal cell at 10) — the same
  ordering as the analytic wells (b_W(w2) = 4.5D > b_W(w4) = 2.5D). The funnel
  ordering follows the well ordering; no claim promoted.

## 3. F2b — the w = 2 OFF family: RF-W2-DRAWN, and the diagnosis is total

```
b : REG      OFF-form   d_inc   Sea residue
1 : UNR      CAP        1.07    -2.6e-13
2 : CAP      CAP        1.29    +3.1e-13
3 : CAP      CAP        1.19    +5.7e-14
4 : UNR      CAP        1.27    -1.4e-13
5 : UNR      CAP        1.00    -2.8e-13
6 : CAP      CAP        1.26    +4.0e-13
7 : UNR      CAP        1.20    -2.0e-13
8 : SCA      SCA        48.05   +2.8e-14
bracket (OFF-form): last-CAP b=7  -> 1/400 CAP  (dt-STABLE)
                    first-non b=8 -> 1/400 SCA  (dt-STABLE)
```

**The pre-registered hypothesis confirms cell-by-cell:** every b ∈ {1, …, 7}
cell is physically bound (d_inc ≈ 1.0–1.3D, deep inside the 3D gate) and the
REG class tracks the SIGN of the ~10⁻¹³ Sea residue with perfect correlation —
positive residue → CAP, negative residue → UNR, eight for eight including the
b = 8 scatter. The 2624 "patchwork UNR/CAP" was the coin flip, whole. The 2624
dt-instability at the b = 8 bracket also resolves: at {1/200, 1/400} both legs
read SCA stably — the unstable leg in 2624 was the coarse 1/100 one.

**R_f(OFF, w = 2) = 7D registers** (OFF-form primary, C-F2-licensed, both
bracket legs dt-stable at {1/200, 1/400}).

**The RF1 class gate at w = 2 (2620, read as frozen):**
R_f(ON, w2) − R_f(OFF, w2) = 10 − 7 = **3D ≥ 2D**, both legs dt-stable →
**RF1 — THE FUNNEL IS SINK-MEDIATED — EXTENDS TO THE SOFT WIDTH.** FUNNEL-1's
classification, previously discharged-at-class for w = 4 only, now holds at
BOTH widths: reach exceeds the potentials-only well by ≥ 5.5D (w2: 10 vs
b_W = 4.5) and exceeds the sink-off boundary by ≥ 3D at each width where drawn.

## 4. Standing

**FUNNEL-1 upgrades to DISCHARGED-AT-CLASS-BOTH-WIDTHS**, with the soft-width
upper bound drawn ([10, 12)D) and the steep-width floor raised (≥ 9D; upper
bound undrawn at this instrument, finer-dt successor declared). The Sea-conjunct
classifier defect is banked to the instrument-hazard lineage (borrowed-gate
transfer 2622, fixed-column launcher 2612, economy re-settle 2631/2638, and now
the sink-referential conjunct read at sink-off — four members, all caught by
controls or preregistered hypotheses, none by luck). Fences held: classification
only; no rates, no σ, no flux, no relic contact; v = 0.10c throughout, DISC
block untouched; σ_cap withheld; EDGE-2(i) queued; the 2624 record unedited
(superseded/confirmed by citation as itemized above); **79.5% untouched.**

## 5. DEP-1 maintenance (owed rows added here; the 2638 row lands one patch
late, disclosed)

Appended to `n2b_dep1_dependency_ledger.md` §1 at this patch:

- **ROB-2 drawn walls (2638):** sink — (halts are misses, Sea ≈ 0; the walls
  are sink-INDEPENDENT) | η LOW | aimed convention HIGH (the walls are the
  convention's walls) | Morse MED (target geometry) | γ-member LOW (0.1c) |
  split-clock LOW (14/14 dt-agreements).
- **FUNNEL-2 brackets + RF1-both-widths (2640):** sink HIGH (the class IS
  sink-mediated) | η MED | aimed conv. MED (launch-column offsets) | Morse MED
  (analytic member) | γ-member LOW | split-clock LOW (classification-grade,
  dt-union on every bracket).

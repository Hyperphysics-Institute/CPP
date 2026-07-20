# C7-D1 execution record — VERDICT D1-MIXED (mode-dependent, per-mode table registers, no summary claim): the PHYSICAL modes' floor is FLAT across a 4× TC range while m0's collapses FASTER than statistical with its mean dying to INCONCLUSIVE — one run, two behaviors, the internal control nobody had to ask for

**Patch 2651, 20 July 2026.** Execution under `c7_discriminant_campaign_prereg.md`
(2649) §3 ONLY — second arc of the frozen order. Verify: `code/2651_c7_d1.py`,
stages guardtest | tc60 | tc120 | tc240 | read, all run (checkpointed execution
per the runtime rider: per-member persistence, no member recomputed, no cell
extrapolated; the FULL grid completed — no UNRUN cells). Per the composite-only
rule: **this reading REGISTERS AND WAITS.**

## 1. Controls — ALL PASS

- **Guard-trigger tests (J4-2):** n<2 SEM assert fires; sem=0 ratio path guards
  to `inf` — both PASS.
- **C-D1 pin (TC = 60):** the ENTIRE 2635 registered ensemble table reproduces
  TO THE PRINTED DIGIT — all four modes, both dt, means AND SEMs exactly
  (m1 −73883±10585, m2 −51430±16683, ell −285741±54093, m0 −470732±121439 at
  dt=1/50; the dt=1/25 row likewise exact). The instrument is the registered
  instrument.

## 2. The floor vs TC (SEM ratios against the √(60/TC) reference: 0.71 at 120, 0.50 at 240)

```
dt=1/50   m0:  1.00 -> 0.25 -> 0.13   (<c> -470732 -> -89654 -> -1487 [INCONCLUSIVE])
          m1:  1.00 -> 1.05 -> 1.17   (<c>  -73883 -> -73529 -> -82950 [SIG-NEG throughout])
          m2:  1.00 -> 1.08 -> 1.07   (<c>  -51430 -> -56687 -> -58366 [SIG-NEG throughout])
          ell: 1.00 -> 0.91 -> 1.00   (<c> -285741 -> -325098 -> -343947 [SIG-NEG throughout])
dt=1/25   m0:  1.00 -> 0.31 -> 0.03   (<c> -1051091 -> -326050 -> -10308 [INCONCLUSIVE])
          m1:  1.00 -> 1.06 -> 1.06   (SIG-NEG throughout)
          m2:  1.00 -> 1.00 -> 0.96   (SIG-NEG throughout)
          ell: 1.00 -> 1.21 -> 1.24   (SIG-NEG throughout)
```

**Frozen reading: D1-MIXED.** The physical modes (m1, m2, ell) are D1-FLAT in
behavior — the floor does not fall with TC at either dt (ratios 0.91–1.24
against references 0.71/0.50), and their means are TC-stable. m0 alone
D1-SCALES — and faster than the statistical reference (0.25/0.13 and
0.31/0.03), with its MEAN collapsing to INCONCLUSIVE at TC = 240 at both dt.
Per the prereg, the per-mode table registers and no summary claim is written.

## 3. Observations registered without claim

1. **The pre-D1 expectation written at 2650 §3 is MET on the physical modes:**
   a static, phase-dependent offset spread across ensemble members produces a
   member-spread (SEM) that is TC-independent — sampling noise would fall as
   averaging extends; an offset statistic does not. The physical modes' flat
   floors and TC-stable means are the offset story's predicted signature,
   recorded BEFORE this arc ran.
2. **m0 is the unrequested internal control:** its collapse (mean and spread
   dying together, faster than √TC) shows the instrument DOES average down a
   genuine time-fluctuation when one is present — the flatness of m1/m2/ell is
   therefore not an instrument ceiling; it is a property of those modes'
   perturbation response. The two-behavior separation inside one run is the
   sharpest fact this arc produced.
3. **Mechanical note (not adjudication):** with D2-NO-ENTRY registered and D1
   not D1-SCALES-across-modes, BOTH 2648 supersession bars contain conjuncts
   that can no longer be satisfied by any D3 outcome (resolved requires
   D1-SCALES + D2-ENTRY; instability requires D2-ENTRY). This is arithmetic on
   the frozen bars, stated so the D3 session inherits it explicitly; the
   composite adjudication itself still waits for D3 per the frozen rule, and
   D3 retains independent value — it tests whether the object is local
   curvature AT ALL, which is the question the offset candidate answers in the
   negative and D3 can test by direct construction.

## 4. Standing

D1 DISCHARGED at D1-MIXED with the per-mode table above. Grid COMPLETE (no
UNRUN cells; the runtime rider's checkpoint mechanism was used, disclosed in
the verify header). Per the frozen order, **C7-D3 is next** — new
instrumentation under full J4 discipline; recommended for a fresh-budget
session. Composite adjudication only after D3. Fences held: no DM-consumer
sentence rides on this reading; 2513/2635 unedited; C7 text untouched; DISC
amendment scope untouched; FORM-1 charter untouched; **79.5% untouched.**
Reasoning: `reasoning/2651.md`.

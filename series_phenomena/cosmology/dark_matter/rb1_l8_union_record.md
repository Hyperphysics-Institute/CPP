# R-B item 1 execution record — VERDICT RB1-CLEAR: THE FORMATION WINDOW'S LOWER-ENDPOINT RIDER CLEARS; "CLOSURE PAYS DOWN TO L=8" STANDS UNDER THE FULL CONVENTION UNION

**Patch 2633, 20 July 2026.** Execution under `rb1_l8_truncation_prereg.md` (2632)
only. Verify: `code/2633_rb1_l8_union.py`.

## 1. Raw outputs (verbatim)

```
[INDEX] ring-count hist {3:16, 7:16} | E_close(8) = +83.2 +84.2 +84.4 | all > +FLOOR: True
[DIST ] ring-count hist {3:16, 7:16} | E_close(8) = +81.1 +79.3 +78.3 | all > +FLOOR: True
[FULL ] ring-count hist {3:16, 7:16} | E_close(8) = +81.1 +79.3 +78.3 | all > +FLOOR: True
```

## 2. Control — PASS (with a precision disclosure)

The INDEX member, run on the exec-loaded registered machinery itself, returns
+83.2 / +84.2 / +84.4 against the record's integer-rounded band "+83..+84"
(`reregistration_reach_s.md` line 21). The third dt value (+84.4) shows the
record's band was a two-significant-figure summary; the reproduction is the
registered artifact's own deterministic output at the record's stated precision,
and the INDEX ≠ DIST separation proves the namespace binding took (the 2574(c)
failure class this control exists to catch). Control PASS.

## 3. Reading (frozen at 2632 §2): RB1-CLEAR

DIST and FULL read E_close(8) = +81.1 / +79.3 / +78.3 — **above +FLOOR by ~40×
at every dt.** Closure pays at L = 8 under every admitted truncation convention.
**The lower-endpoint rider CLEARS; the formation window "even L ∈ [8, 22]" stands
whole, now convention-union-backed; the 2574 §3 caveat is DISCHARGED.** The
convention shift is real but small (−3 to −6 MeV from INDEX, ~5%), nowhere near
the floor.

## 4. Disclosed census (post-freeze, 2574(d) class — census only, no reading)

DIST and FULL returned IDENTICAL values to every printed decimal. Census of the
FULL-beyond-DIST extra neighbors at L = 8: **32 of 32 are SAME-charge** — and the
dance consumes reach lists only through opposite-charge target selection, so the
two conventions are dynamically identical BY STRUCTURE at this geometry. The
truncation that "binds" at L = 8 binds only on same-charge list members the
dynamics never uses; this is why the registered INDEX values were within ~5% of
the union despite discarding two neighbors at half the qCPs. (The 2574
zero-margin assert recommendation stands unchanged — the structural filter is a
property of THIS observable, not a general license.)

## 5. Standing

**R-B item 1 CLOSED (rider cleared; net integrity gain, favorable direction).**
The wall bracket (22, 24), payoff maximum, window body, E_close(16) pin: all
untouched as fenced. 79.5% untouched. R-B queue remaining, order fixed: item 2
(2513 mode curvatures under reach-S), item 3 (2549 ENDBOND-2 fragment), item 4
(2510 contention/pile statistics) — the last founder-free items.

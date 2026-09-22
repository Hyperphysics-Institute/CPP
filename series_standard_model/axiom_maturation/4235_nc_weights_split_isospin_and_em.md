# OPEN-EW-NC, Narrowed: the Constituent Weights Are an EM Part Already Derived Plus an Isospin Part of ±1, −2

**Patch:** 4235. **Lane:** EW. **Session:** 237.
**Works:** OPEN-EW-NC (registered 4213), route (a) — the elastic W⁰ capture-and-re-eject. **Result:** the target is
reduced by more than half before any mechanism is proposed. **Verify:** `series_standard_model/code/4235_nc_weight_split.py`.

## 1. Rows verbatim (D-11)

```
s^2 = 3/(8 phi) = 0.2318
Q_W(u) = +0.3820   Q_W(d) = -0.6910   neutron = -1.0000   proton = +0.0729
per +qCP core (u):            +0.3820 = isospin +1.000  +  EM -0.6180   [ = 1 - 1/phi = 1/phi^2 ]
per linear -eCP (d - u):      -1.0729 = isospin -2.000  +  EM +0.9271   [ = -2 + 3/(2 phi) ]
contact weights of 4216 (= -Q_W): core -0.382, linear +1.073   -> match 4216's -0.382 / +1.073
```

## 2. What the split says

4198/4216 sorted the measured neutral-current weight onto CPP constituents: −0.382 per +qCP core, +1.073 per
linear oscillator, and OPEN-EW-NC asked for a mechanism producing those numbers. They split exactly into two
pieces of different provenance:

- **An electromagnetic part, −4Q s² per constituent**, with s² = 3/(8φ) the 600-cell mode fraction SF-2 already
  derives. This is the charge of the constituent times the sector's mixing fraction; it is the photon–Z mixing
  read in CPP objects and **needs no new mechanism** — it is why 1/φ² appears (1 − 1/φ = 1 − (8/3)s²).
- **An isospin part: +1 per bare +qCP core, −2 per linear oscillator.** This is the whole of what route (a) has
  to produce.

## 3. The requirement on the elastic W⁰ event, stated once

A passing electron's −eCP is captured at a transient W⁰ centroid near a constituent and re-ejected by the
handed rule. The isospin weights say: **at a bare core the event throws the electron with unit weight one way;
where a linear −eCP is already held at the core (a down quark), the event throws it with double weight the
other way.** The −2 decomposes naturally as (−1: the event reversed by the resident −eCP) + (−1: the core's own
+1 event cancelled because its centroid is occupied) — that is the first thing to test, and it is a statement
about occupancy of the centroid, the same object 4231 made the seat of the binding. If the reversal-plus-
cancellation reading holds, route (a) reproduces Q_W's isospin structure with no number fitted, and the whole
of Q_W follows with the derived s². Not computed; posed. Route (b) (an interacting Z) is not needed for anything
in this split.

## 4. PD-008

Convenient: the split is exact and the EM half is "free." The check: the split is the Standard Model's own
(2T₃ − 4Qs²) restated per constituent — it is bookkeeping, not physics, until route (a) produces the ±1/−2.
What it buys is that the mechanism now has to produce two small integers, not two irrational numbers.

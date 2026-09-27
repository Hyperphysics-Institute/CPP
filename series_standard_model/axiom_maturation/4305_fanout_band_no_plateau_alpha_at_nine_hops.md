# The Fan-Out Band Reproduced and Extended: No Plateau (f ~ N⁻⁰·³⁸); f = 4πα to 0.1% at Nine Fan-Out Hops per PSR; One GP-Step per Hop Would Give 10⁻¹²

**Patch:** 4305. **Lane:** EW → foundations. **Session:** 240.
**Works:** TODO-4286-GMOMENT (M1), the decisive test of 4304 §4.
**Verify:** `series_standard_model/code/4305_fanout_band_extended.py` (sparse-matrix relay of pass 3's exact rule:
`series_phenomena/cosmology/sea_gravitation/scripts/3133_subpsr_cascade.py`, Patch 3135).

## 1. Reproduction

Same FCC lattice, same outward criterion (x·d > 0, all 12 at the origin), equal shares, single volley, band thickness as
rms(r)/⟨r⟩. The pass-3 table is reproduced to its last digit:

```
   N      <r>     rms  rms/<r>
   6    6.241   0.583   0.0934        (pass 3: 0.093)
  10    9.560   0.865   0.0905        (0.091)
  14   12.742   1.086   0.0853        (0.085)
  18   15.857   1.274   0.0803        (0.080)
  22   18.934   1.439   0.0760        (0.076)
```

## 2. Extension: the ratio does not stabilise

```
  24   20.463   1.515   0.0740
  40   32.569   2.022   0.0621
  56   44.575   2.423   0.0544
  72   56.545   2.764   0.0489
decline exponent over N = 24..72: f ~ N^-0.38 (no plateau); extrapolated to N = 1e30 GP-steps: f ~ 1.0e-12
```

Pass 3 flagged "whether it stabilises … requires larger N". It does not. The band's fractional thickness falls as about
N⁻⁰·³⁸ (rms ∝ N⁰·⁶, ⟨r⟩ ∝ N), with no plateau through N = 72 (beyond about 80 the lattice edge intrudes). **If a hop were
one GP-step, with about 10³⁰ per PSR, the band would be about 10⁻¹² of a PSR, not 10%.** The founder's ~10% band, and
pass 3's vindication of it, hold only if a DI-bit undergoes of order ten fan-out events between the origin and the PSR.

## 3. Where α falls

```
crossings of f = 4 pi alpha at N = [5, 9]   f(7..10) = [0.0937, 0.0927, 0.0918, 0.0905]
```

**At N = 9 hops, f = 0.0918 against 4πα = 0.09170: a match to 0.1%** (the earlier crossing at N = 5 is in the small-N
ripple). Under the per-layer reading α = f/4π, the fan-out rule reproduces the fine-structure constant if a DI-bit is
shared out nine times on its way from a GP to its PSR.

## 4. What I think

The test asked for in 4304 is done, and it sharpened rather than settled the question:

- The band is derived, and its value is set by one thing: the number of fan-out events per PSR. Nine gives α to 0.1%;
  six to ten give 1/131 to 1/139; a GP-step per hop gives nothing like it.
- So the corpus's own "~10% band" already *assumes* about ten fan-out events per PSR. That is a lattice parameter the
  founder has described in words (DI-bits "step outward along the edges between GPs"; the 4011 multihop path discussion,
  not yet read against this) but whose count per PSR is not on file in numbers.
- If that count is nine, α = 1/137 follows from the fan-out rule and the per-layer reading with no further input. If it
  is 10³⁰, the band collapses and the whole α = f/4π route fails. Nothing in between is a near miss: the dependence is a
  slow power law, so 1/137 needs the count within about ±1 of nine.

## 5. Founder question (a physical picture)

**Between leaving its GP and landing at the PSR, how many times is a DI-bit shared out among outward neighbours?** Is it
once for every GP it crosses (about 10³⁰), or a handful of re-radiations, of order ten? Your ~10% band, and 1/137 with it,
both say about nine.

## 6. PD-008

- **Convenient branch, marked.** "α at nine hops to 0.1%" is exactly the kind of match to distrust. Two readings of N
  (the per-layer rule, a construction) and one lattice count (hops per PSR, not on file) stand between it and a
  derivation. It is not reported as one.
- **What is solid.** Pass 3's table reproduced exactly; the band falls as N⁻⁰·³⁸ with no plateau; f = 4πα at N = 9; a
  GP-step-per-hop reading gives 10⁻¹².

**Erratum (Patch 4306):** the founder rules the sub-Moment sharing count is not a physical parameter. §3's nine-hop match to 0.1% is an artefact of the dial and is withdrawn as evidence; §2's no-plateau result stands. See `series_standard_model/axiom_maturation/4306_hop_count_is_a_dial_band_must_be_positional.md`.

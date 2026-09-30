# Saturation Is a Solid Band: With Error Bars, on a Crystal and on a Strained-Glass Proxy, the Fill Rises Toward One and Its Change in a Well Vanishes; 4328/4329's "Plateau Near 0.88" Was Premature

**Patch:** 4330. **Lane:** EW → foundations. **Session:** 241.
**Verify:** `series_standard_model/code/4330_fsat_lattice_robustness.py`.
**Owed by:** 4328 (f_sat on a faithful lattice) and 4329 (multi-seed runs with error bars). **Corrects:** 4328 §2/§3
and 4329 §3's "plateau near 0.88" (errata appended).
**No founder input this patch** (queued computation; PD-006).

## 1. Which lattice (D-7)

The corpus GP set is *"a densely nested lattice of 600-cells"* (`founders_vision.md`, 4 Apr 2026), locally icosahedral,
with its 7.356° deficit *"carried as strain, just like materials with icosahedral packing"* (A2 note, 4061): a strained,
glass-like 12-neighbour packing, not a crystal. Two stand-ins were run:

- **FCC**, the crystalline 12-neighbour lattice (the corpus's transport lattice, 2890);
- **GLASS**, a random dense packing (random sequential addition with a hard core) with each site joined to its 12
  nearest neighbours, as a proxy for strained icosahedral packing.

The exact icosahedral Z-module (integer sums of the icosahedral unit vectors) is dense in three dimensions, so "the same
GP" almost never recurs on it and a fill fraction is undefined there. It was not used.

## 2. Results (rows)

Rule R-DIBIT-FAMILY-EXCLUSION with stop criterion S1; the "well" is the same N into a 10%-smaller shell:

```
summary (mean +- sd over 3 seeds)
   FCC N =  1500: fill = 0.954 +- 0.005;  change in well = +0.015 +- 0.009
   FCC N =  3000: fill = 0.982 +- 0.006;  change in well = -0.000 +- 0.005
 GLASS N =  1500: fill = 0.936 +- 0.011;  change in well = +0.001 +- 0.012
 GLASS N =  3000: fill = 0.956 +- 0.009;  change in well = +0.003 +- 0.003

   FCC N =  6000 (one seed): fill = 0.996; in well 0.993; change -0.002
```

- **The fill keeps rising toward one** as N grows against the shell's site count: 0.954 → 0.982 → 0.996 on FCC, and
  0.936 → 0.956 on the glass proxy.
- **The change in a well is zero within error once the band is saturated** (FCC −0.000 ± 0.005; glass +0.003 ± 0.003).
- **Crystal and glass behave alike**, so the result does not depend on crystalline order.

## 3. Correction to 4328/4329

4328 and 4329 read a plateau near 0.88 off single runs at N = 3000–5000 on a larger shell. Those runs were **not yet
saturated**: the fill was still rising (0.858 → 0.884). With the shell small enough for N to exceed its site count
several times over, the fill climbs to 0.98–0.996. **Saturation is a solid band, f → 1**, not a band with one site in
eight empty. The founder's 4328 statement (*"there is only one DI-bit on each GP_PSR"*) holds in the saturated limit.

## 4. What this settles

- **α = PSR/(2L)** at saturation (f = 1). CAL-ZBW1-SWING's effective swing L/f (4329) is simply the swing L ≈ 68.5 PSR.
  4329's "the fill is absorbed" still holds algebraically; the fill just turns out to be one.
- **Local position invariance:** a saturated band keeps its fill in a well, and the extra DI-bits only deepen it, so
  k_α = 0 from the occupancy, within these runs' error. Combined with the founder's 4327 ruling (the swing scales with
  the PSR), both factors of α pass the atomic-clock test in this model.
- **What saturation requires:** N well above the shell's site count, which a 2–10%-deep band (about 10²⁸ GP layers)
  implies by a vast margin.

## 5. What I think

This removes the loose end 4328 opened. The founder's exclusion rule, run long enough, packs the band solid, and a
solid band is immune to gravitational squeezing. The chain now stands as **α = PSR/(2L), one calibrated swing,
LPI-safe, with the right sign of running**. The remaining physics is the running's magnitude (T1) and gravity in counts
(O2). The toy's limits are stated below.

## 6. PD-008

- **Convenient branch, marked.** "Saturation is solid" is the convenient outcome (it makes f = 1). It is supported by
  three seeds on two lattices with the fill rising monotonically, but these are small shells (a few thousand sites);
  whether the approach to one is complete or stops at 0.99-something is not resolved, and at the 10⁻¹⁵ level the
  clocks require it is not testable by simulation.
- **My error, stated.** 4328/4329 reported a plateau from unsaturated single runs; corrected here.
- **Solid:** fill rising toward one on both lattices; well change consistent with zero at saturation.
- **For the critic in the next window:** (i) whether an analytic argument (exclusion packing with a surplus of bits)
  shows f → 1 exactly; (ii) a larger-shell run to confirm the trend; (iii) whether the GLASS proxy's hard-core spacing
  (0.85) or neighbour count biases the result.

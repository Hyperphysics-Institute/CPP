# Family Exclusion Caps a Charge's Occupancy at One DI-bit per GP — the 4327 Escape Was Already in the Corpus — but LPI Also Needs the Band Saturated

**Patch:** 4328. **Lane:** EW → foundations. **Session:** 241.
**Founder:** `founders_voice/4328_ruling_dibit_family_exclusion_one_per_gp.md` (verbatim).
**Verify:** `series_standard_model/code/4328_family_exclusion_landing.py`.
**Answers:** 4327 §5. **Registers:** R-DIBIT-FAMILY-EXCLUSION (a clarification of the founder's 4308 rule, not a new
axiom).

## 1. The ruling, and where it already stood

A DI-bit advances from GP_origin toward GP_PSR in steps, and **each step goes only to a GP holding no DI-bit of the same
GP_origin family.** So GP_PSR holds at most one DI-bit per family, and this is what gives the landing shell its 2–10%
thickness rather than a one-GP surface.

**D-10: this rule is on file.** The founder's 4308 ruling already said the bits *"find their first GP_empty1 … choose the
one that is empty … if none is empty, continue moving."* 4328 clarifies that "empty" means empty of the same family.
**The escape 4327 proposed (a GP registers each source once) is not a new counting rule; it is his 4308 stepping rule.**
Registered here as **R-DIBIT-FAMILY-EXCLUSION** (clarification of 4308; A3′/AP-4 transport; axiom count unchanged).
4309's sharing-rule simulation (the 1.9% band) did not apply it and is flagged for a re-run.

## 2. What the rule does, on a toy (rows)

The FCC lattice (12 neighbours, the corpus's transport lattice, 2890). Each step goes to a random outward neighbour free
of the family, or any outward neighbour if none is free ("continue moving"). A bit stops once its summed path reaches P
edges on a GP holding no other family bit.

```
         N  max family bits on one GP   <r>/P  rms/<r>  band fill
        50                          1   0.670    0.081      0.033
       200                          1   0.689    0.099      0.107
       600                          1   0.700    0.099      0.305
      1500                          1   0.713    0.113      0.611
      3000                          1   0.775    0.129      0.858
    (N = 5000, separate run: fill 0.884)
```

- **Occupancy never exceeds one**, as he says: the rule enforces it by construction.
- **The band thickens as N grows past the shell's GP count** (rms width 8% → 13%): his "it is because of this rule that
  there is a shell thickness", confirmed in kind.
- **But the band is not filled solid.** The fraction of band GPs holding a family bit rises with N and appears to level
  off near 0.88 in this toy (with this band definition). **The rule caps the occupancy at one; it does not make it one.**

## 3. What that does to α and to local position invariance

With the target in the band, the occupancy it sees is the band fill f, so **α = f·PSR/(2L)** (4324).

- **Below saturation**, f depends on N against the band's GP count. In a gravitational well the band has fewer GPs, f
  rises as (1 + κ)², and 4327's **k_α = −2 returns**, excluded by about a million.
- **At saturation**, f sits at a constant f_sat fixed by the stepping rule and the lattice. A well only deepens the band
  (the extra bits land further out, one per GP), f does not change, and **k_α = 0**.

So the founder's rule rescues local position invariance **on one condition: every charge's band must be saturated**,
meaning N is large enough that the band fills to f_sat everywhere and the band's *depth*, not its fill, absorbs the
well. With a 2–10% band that is many GP-layers deep, saturation is the natural regime, but it has to be shown.

And f_sat is a **geometric number of the rule**, computable in principle rather than calibrated. CAL-ZBW1-SWING's "full
covering" becomes f = f_sat: L = f_sat·PSR/(2α) (e.g. 0.88 × 68.5 ≈ 60.6 PSR on the toy's number, not claimed).

## 4. What I think

His rule closes the loophole 4327 opened, and it was his rule all along (4308). Pressed to the end, it leaves one
honest gap and one opportunity. **The gap:** the rule prevents stacking but not voids. Local position invariance then
needs the band saturated, and a saturated band's fill f_sat is below one on the toy. **The opportunity:** f_sat is a
number the lattice and the stepping rule fix. So α = f_sat·PSR/(2L) has one calibrated factor (the swing) and one
computable one (the fill). Computing f_sat on the 600-cell's icosahedral neighbourhood, with the founder's exact stepping
rule and a principled band definition, is now a concrete, finite computation.

## 5. Founder question (a physical picture)

**When a charge's DI-bits land, does every grid point in the landing band end up holding one of them, or are there gaps?**
Your rule stops two from the same charge sharing a grid point, and in a small test that works exactly. But the bits
also leave gaps: about one grid point in eight inside the band gets none, even when there are plenty of bits. Is the
band packed solid in your picture (every grid point one bit), or is some emptiness natural? The answer changes α by
that fraction.

## 6. PD-008

- **Convenient branch, marked.** "The escape was already in the corpus" is welcome and is supported by the 4308 text
  quoted in §1; it is registered as a clarification, not claimed as a derivation.
- **Not established:** that the fill truly saturates (0.858 at N = 3000, 0.884 at N = 5000 — levelling, not proven); the
  value 0.88 (FCC toy, 10th–90th-percentile band, small P); that real bands are saturated.
- **Solid:** occupancy ≤ 1 under the rule (exact); the band thickens with N; below saturation k_α = −2 returns; at
  saturation k_α = 0.
- **For the critic in the next window:** (i) re-run 4309's band with R-DIBIT-FAMILY-EXCLUSION on the icosahedral
  neighbour set; (ii) the band definition (percentiles vs a density threshold) and its effect on f; (iii) whether f_sat
  approaches 1 at larger N and P, or a definite value below it.

# (P′) The Planck-Level ZBW's Coherent Footprint: No Corpus-Defined Lattice Count Gives 11.7; Any Universal Per-GP Rule Gives 2

**Patch:** 4317. **Lane:** EW → foundations / GR. **Session:** 241.
**Owed by:** 4313 §5 and the Session 240 boot card, task (P′).
**Verify:** `series_standard_model/code/4317_planck_zbw_footprint.py`.
**Status:** computation; no finding in print is changed. The 4313 flag ("11.7 ≈ 12") is resolved as a **miss**.

## 1. Inputs, each resolved against the lane that wrote it (D-7)

- **c04 Definition (Level 1, Planck ZBW):** *"Every elementary DP oscillates … at ν_P = 1/(2t_P)"*, energy E_P per cycle.
  A half-cycle is one Moment. **The Planck unit is one DP, which is two CPs.** c04's spatial-step relation caps the
  displacement at l_P per Moment.
- **0733 / `founders_vision.md` (15 Jun 2026, the founder's correction):** l_P is the baseline PSR, not the GP spacing.
  The GP lattice is finer, with R = PSR/s = 10³⁰ (GR-FE-1) or 10³² (EU budget).
- **4311 (founder, verbatim):** *"every GP emits the same number of DI-bits"* (AP-4). What a source does is set the
  **content** of its GP's broadcast, not the count.
- **4312/4313:** a unit charge is one GP's emission; the coupling is quadratic per source, so G_P = α^(−1/2) = 11.706.
  **G_P is a ratio:** the Planck unit's organised emission over a unit charge's.
- **R-OUTWARD-FANOUT (founder, 14 Aug 2026):** at every hop a GP's DI-bits split **equally** among all neighbours with
  a positive outward radial component, on the twelve icosahedral neighbours.

## 2. The neighbourhood, computed

The 600-cell built from its 120 vertices gives 12 nearest neighbours per vertex at edge 1/φ. Their tangent directions
have pairwise cosines {±1, ±1/√5}, which makes them an icosahedron. For a direction drawn at random, the number of
neighbours with a positive outward component is **exactly 6 every time** (the twelve are six antipodal pairs; ties have
measure zero). Equal shares therefore mean exactly 6 recipients per hop, with no fractional weight on file.

## 3. Pre-registered candidates (rows)

These were listed in the script before any was compared with 11.706.

```
candidate                                                                      G   G/G_P-1  alpha=1/G^2 alpha err
C1 the DP's two CPs (c04 Level 1 counts CPs)                               2.000   -82.92%        1/4.0  +3325.9%
C2 one GP's outward fan-out recipients (R-OUTWARD-FANOUT)                  6.000   -48.75%       1/36.0   +280.7%
C3 the twelve icosahedral neighbours                                      12.000    +2.51%      1/144.0     -4.8%
C4 two CPs x outward fan-out recipients                                   12.000    +2.51%      1/144.0     -4.8%
C5 GP + its twelve neighbours                                             13.000   +11.05%      1/169.0    -18.9%
C6 two CPs' GPs + both neighbourhoods (partners >> s apart, disjoint)     26.000  +122.10%      1/676.0    -79.7%
candidates within 2% of 11.706: 0  (none reaches it; C3 and C4 land on 12 = 2 x 6: one icosahedral fact, not two)
```

Every corpus-defined count is an integer, and the nearest is 12. At 12, α = 1/144, which is 4.8% off a quantity measured
to 10⁻¹⁰. **The 4313 flag is a miss.** C3 and C4 agreeing is not two confirmations; both are the same fact (twelve
neighbours in six antipodal pairs).

## 4. The per-CP requirement

```
c04 Level 1 is ONE DP = TWO CPs; with charge = one CP's emission, each CP of a Planck-level DP must organise
   G_P/2 = 1/(2 sqrt alpha) = 5.8531 GPs' emission; the outward half-shell is 6 (+2.51%).
```

## 5. The normalisation, which is the substantive result

G_P compares two sources, so any rule that applies to every GP alike also applies to the unit charge, and it cancels:

```
universal rule 'bare CP emission': Planck DP / unit charge = 2/1 = 2.0  (needs 11.706)
universal rule 'CP + outward fan-out recipients': Planck DP / unit charge = 14/7 = 2.0  (needs 11.706)
universal rule 'CP + 12 neighbours': Planck DP / unit charge = 26/13 = 2.0  (needs 11.706)
```

**Under any universal per-GP rule, the Planck-unit-to-charge ratio is the CP count of a DP, which is 2.** Candidates C2
to C6 above looked like 6 to 26 only because, read as absolute counts, they silently assume that a charge does *not*
recruit its neighbours while the Planck ZBW does. G_P = 11.7 therefore needs **something the Planck-level ZBW does that
a charged CP does not.** The difference has to lie in the oscillation, not in the lattice's neighbour structure, which
is the same at every GP.

## 6. The scale audit

```
GR-FE-1   R = PSR/s = 1e+30: a CP moving l_P per Moment crosses 1e+30 GPs per half-cycle (28.9 orders above 11.7); a path of 11.7 GPs needs v = 1.2e-29 c
EU budget R = PSR/s = 1e+32: a CP moving l_P per Moment crosses 1e+32 GPs per half-cycle (30.9 orders above 11.7); a path of 11.7 GPs needs v = 1.2e-31 c
```

If the Planck ZBW moves its CP about a Planck length per Moment, as c04's step cap allows and the pass-through picture
("crosses the centre … at its top speed") suggests, the CP passes about 10³⁰ GPs per half-cycle. The in-step set is then
either **not the path** (a per-instant set, such as the GPs whose broadcast state the oscillation sets in the same
Moment) or the excursion is **about one GP step**, which means a speed of about 10⁻²⁹ c. c04 does not state the
excursion in GPs. The founder's 4288 ruling leans to the first reading: a CP moving at light speed *"advances at one
Planck Sphere Radius (PSR) per Moment"*, which he thought unlikely in general *"unless this is at the smallest level"*,
and the Planck ZBW is the smallest level. On that reading the path is about 10³⁰ GPs and the in-step set must be a
per-instant set. Both readings are kept open until he answers §8. The icosahedral neighbourhood (spacing s, 10⁻³⁰ l_P) is the right object
only under the second reading or a per-instant one.

## 7. What I think

(P′) is answered in the negative for the lattice. **No count the corpus defines gives 11.7.** The integer counts miss
by at least 2.5% (4.8% in α). And the whole class of neighbour-recruitment readings cancels in the ratio, so it could not
have given 11.7 even if a count had matched. What survives is sharper than before. With the count rule and c04's Level 1,
**a Planck-level DP must organise 5.85 times as much emission per CP as a charged CP emits.** Only a property of the
oscillation can supply that factor, not a property of the neighbourhood. G_P = α^(−1/2) stays a **calibration**, as
labelled at 4310/4313.

## 8. Founder question (a physical picture)

**In one Planck-level ZBW half-cycle (one Moment), how far does the oscillating CP go: about a Planck length (about 10³⁰
GP steps), or about one step to a neighbour?** And **what does the oscillation do to the GPs around it that a charged CP
sitting still does not do?** The count needs a Planck-level DP to organise about 5.85 GPs' worth of emission per CP,
where a charge organises one. Whatever makes that difference is the thing that would derive α.

## 9. PD-008

- **Convenient branch, marked and not taken.** 12² = 144, and 144 − 137.036 ≈ 7 invites an "icosahedral count plus a
  correction" story. It is the a_e-shaped coincidence class the Session 240 detail (§4) lists as *not to be rediscovered
  as results*. No correction mechanism is on file, and none is proposed.
- **Convenient branch, marked and not taken.** The per-CP requirement 5.853 sits 2.5% from the half-shell 6. This is
  the same miss seen from the other end, and §5 shows the half-shell cancels in the ratio anyway.
- **Solid:** the 600-cell neighbourhood (12, icosahedral, six antipodal pairs, exactly 6 outward recipients); the
  normalisation cancellation (§5), which is an identity; the scale audit's orders of magnitude.
- **Assumed (stated, not derived):** c04 Level 1's "one DP" is the whole Planck unit, and the unit charge is one CP.
  If the Planck unit were several DPs, C1 would scale with their number. No such reading is on file.
- **For the critic in the next window:** check §5's claim that R-OUTWARD-FANOUT, being universal, recruits for a
  charge exactly as for a Planck DP. If the fan-out applies only to relayed DI-bits and not to a GP's own broadcast
  state, §5 still holds (it then recruits for neither), but that should be checked against AP-4d.

**Erratum (Patch 4318):** §6's open fork is settled at c04's frequency by the founder's own geometry: with two Moments per cycle, the Planck ZBW is a one-PSR flip each Moment (the first reading). His smooth profile needs at least 4–6 Moments per cycle, a fork now put to him. §5's "something the oscillation does" is his answer: the broadcast content changes every Moment while the count stays fixed. And the object to compute is not a Planck-mass footprint: 11.7 = e_P/e is a light-coupling ratio, without G. See `series_standard_model/axiom_maturation/4318_planck_zbw_on_the_moment_clock_and_alpha_is_light_not_gravity.md`.

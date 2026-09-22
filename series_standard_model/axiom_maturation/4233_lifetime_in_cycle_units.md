# The Neutron Lifetime in the Mechanism's Units: the Pocket Geometry Fixed, the Bracelet Factor Named

**Patch:** 4233. **Lane:** EW. **Session:** 237.
**Works:** 4231 §2b (the rate budget), the first of the two remaining sector computations.
**Verify:** `series_standard_model/code/4233_lifetime_in_cycle_units.py`.
**Result:** not a derivation of the lifetime. It is the measured rate rewritten in the reset mechanism's own units,
with the one factor the geometry already fixes divided out, so that what the substrate must supply is a single
named number with a recognisable shape. Two slips on the way (a doubled ħ; tree-level couplings for G_F) are in
the script's comments.

---

## 1. Rows verbatim (D-11)

```
SM rate in this form: Gamma = 7.196e-25 MeV  ->  tau = 915 s   (measured 878.4 s; the 4% residual is the radiative correction not included here)
per-cycle probability P = 1.44e-26;  in the g-form P = 2pi x [7.46e-04] x (m_e/m_W)^4 [1.63e-21] x (m_e/m_const) [1.63e-03] x (G_F_meas/G_F_tree)^2
pole-in-pocket (geometry, 4231) = 1.24e-03;  so (W0 present, aligned) x (outward) = 1.17e-23
compare (m_e/m_W)^4 (m_e/m_const) = 2.67e-24;  ratio = 4.37
```

## 2. What the numbers say

The measured rate, per ZBW cycle of the orbital, is P = 1.4×10⁻²⁶. The pocket geometry of 4231 — the −eCP
pole is inside an in-plane, on-circle pocket 1.2×10⁻³ of the time — is fixed by r_pocket/r_orbit = m_const/m_W
and takes out that factor. **What the substrate must supply is (W⁰ present at the orbit, aligned) × (the reset
sends the pole outward) = 1.2×10⁻²³ per cycle, and that number is (m_e/m_W)⁴ × (m_e/m_const) × 4.4.**

The shape is not accidental; it is the Standard Model's own, read in the picture:

- **(m_e/m_W)⁴** is the squared W propagator evaluated at the lepton-mass scale — in the picture, *the probability
  that a bracelet of mass m_W is present at the orbit when only m_e-scale energy is available*, as (E/m_W)² in
  amplitude. This is the factor the bracelet-formation rule has to produce, and it is the sector's missing input
  (no rule on file for how often the Sea throws up a W⁰ near a quark).
- **(m_e/m_const)** is one lepton Compton time per ZBW cycle: the outward branch has that fraction of a cycle to
  succeed in, which is what "the W⁰'s duration is 6×10⁻⁴ cycles" (4231) was already saying, up to the factor
  m_W/m_e between the bracelet's own duration and the lepton's.
- **4.4** is what is left for the alignment fraction and the outward-branch probability together — O(1), which
  is what a geometric alignment and a two-way branch should give. Nothing in the picture is asked to be
  unnaturally small or large.

## 3. What is and is not claimed

Claimed: the lifetime's suppression is entirely the bracelet-presence factor (E/m_W)⁴ times the pocket geometry;
the alignment and the branch are O(1). Not claimed: any derivation of (E/m_W)⁴ from the bracelet's SSV energetics.
That is the target — **a bracelet-formation amplitude that scales as (available energy / m_W)²** — and it is now
stated as a number the sector can aim at rather than as "the lifetime." Filed under the rate item.

## 4. PD-008

Convenient: reading the SM's propagator as a CPP bracelet-presence probability. It is a translation, not a result,
and I have said so. The inconvenient part is that nothing in the corpus produces (E/m_W)² yet; the lifetime remains
a target, now a precise one.

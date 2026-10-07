# Same Number of PSRs, Yes; Same Number of Moments — It Depends Whose Moments: Counted by the CP Itself, His Proposal Passes Every Solar-System Test; Counted as Universal Moments, It Loses the Gravitational Redshift

**Patch:** 4387. **Lane:** foundations, with GR. **Session:** 242.
**Founder input:** `founders_voice/4387_lattice_moment_fixed_same_psrs_same_moments.md` (a question back on 4386 §6).
**Script:** `series_standard_model/code/4387_ruler_and_hop_bookkeeping.py` (symbolic, first order only).
**Critic:** a fresh-context critic returned HOLD on the first draft (verbatim in
`series_standard_model/reviews/2026-10-01_session_242_critic_returns_verbatim.md`). All six required changes are taken
in. The main one: his words admit a reading that passes, and the draft had presented only the failing one.

## 1. His variables and question

- The lattice never changes, but the number of GPs a CP crosses per Moment can change with SSV_abs.
- The Moment never changes, but **the number of Moments between two events can change for a CP** in different SSV_abs.
- Each GP's LSP sum changes every Moment with its CP and the DI-bits it receives.
- **Question:** would it work if the distance between CPs were always the same number of PSRs, and the number of
  Moments to cover that distance were always the same?

## 2. The bookkeeping (script)

At a place where the PSR's lattice size is q·l_P (q ≈ 1 − U, U = GM/rc²), three numbers fix the local physics. Each is
taken relative to far away, in lattice distance and universal Moments:
- the length of a material ruler, r;
- the speed of a signal, v;
- the clock rate, c = v/r (a tick is a signal crossing a ruler).

The solar-system tests need **r = 1 − U, v = 1 − 2U, c = 1 − U.**

| picture | ruler | signal | clock | result |
|---|---|---|---|---|
| **(A)** spacing = n PSRs, crossed in the same number of **universal** Moments | 1 − U ✓ | 1 − U ✗ | **1** ✗ | Local light speed passes, but there is no gravitational redshift (GPS's +45.7 μs/day would be absent). g₀₀ = −1, so in metric terms slow bodies feel no Newtonian pull. Light bends by half. |
| **(B)** spacing = n PSRs, crossed in the same number of **the CP's own steps**, each step taking 1/q universal Moments | 1 − U ✓ | 1 − 2U ✓ | 1 − U ✓ | passes |
| **(C)** 3386's reading: a signal crosses one PSR per Moment, and a ruler is a fixed number of proper (local-ruler) units | 1 − U ✓ | 1 − 2U ✓ | 1 − U ✓ | passes, with the same **first-order** metric as (B) |
| **(D)** 4386's absolute rulers | 1 ✗ | 1 − U ✗ | 1 − U ✓ | half the bending (γ = 0) |

**Which reading is his?** His own second bullet says the number of Moments between events changes for a CP in a
stronger field. So "the same number of Moments" may well mean **as the CP itself counts them**. That is (B), and it
passes. His 4385 wording ("the same number of Moments pass for the same number of PSR-size hops") was read the same
way at the time, into the passing one-PSR class with g₀₀ = −q². Only the universal-Moment reading (A) fails. §5 asks
him directly.

In (B), both of his variables are used:
- **Moments between events increase**, by 1/q per step;
- **GPs crossed per Moment fall**, by q for the smaller PSR and by another q for the slower step: q² in all.

**Discreteness:** 1/q Moments per step is not a whole number. A CP near the Sun would skip a step in about a fraction U
of Moments: roughly one Moment in 470,000 at the Sun's surface.

## 3. What (B) and (C) mean for the corpus

- **They agree at first order, and second order is not checked.** Whether they differ there, against R-PSR-LAW-LOG's ½,
  is owed.
- **Units decide which reads more naturally.** 3386 reads PSR_eff as a proper length (measured with local rulers), and
  R-PSR-LAW-LOG and 3387 rest on that reading.
  - In (C), the PSR's proper size goes as q, so "clock rate = PSR ratio" holds in proper units.
  - In (B), the ratio holds for the PSR's lattice size, but measured with local rulers the PSR is constant.

  The founder's clock ruling (`founders_voice/founder_ruling_clock_rate_is_displacement_2026-09-02.md`: clock rate ∝
  displacement per Moment) fits (B) only if displacement is counted in PSRs. In lattice units it would be q², not q.
  The choice between (B) and (C) is therefore partly a choice of units for the registered PSR law, not purely a choice of
  mechanism. 3386 §4's "lapse tension" is a second-order matter, separate from this.
- **(B) is the form 3386 withdrew.** 3385 obtained Shapiro's factor 2 from a GP-counted hop (1 − u) times a lapse-slowed
  rate (1 − u). 3386 withdrew it as "a knob invented to reproduce a number", for want of a mechanism. (B) is the same
  bookkeeping. **What would make it acceptable now:** a founder statement, at axiom level, that a CP's step takes more
  Moments where SSV_abs is higher. His second bullet asserts the variable, but not yet the cause or the size.
- **If (B) or (C) is chosen,** clocks, rulers and light again share one PSR in the relevant units, and 4385's
  WC-EINSTEIN-AREAL and the exclusion of WC-GR-EXTERIOR can be restored. Until then they stay suspended (4386).
- **Wording, if (B) is chosen:** light advances one PSR per **local tick** (the CP's own step), not per universal
  Moment. GR-1i's "one Planck sphere per Moment" and 4384's answer would carry that gloss.

## 4. Answer to his "What do you think?"

Keeping CP spacing at the same number of PSRs is right: it is the shrinking-ruler branch, and it passes every test.
"The same number of Moments" is right if it means the CP's own count of steps. Each of those steps then takes slightly
more universal Moments where the PSR is smaller. If it means universal Moments, it loses the redshift that GPS corrects
for every day.

## 5. Questions to the founder (physical pictures)

1. **Whose Moments?** When you said "the same number of Moments", did you mean the CP's own count of its steps, or the
   universal Moments a distant observer would count?
2. **If the CP's own count:** near the Sun, does each step of a CP take a little more than one universal Moment? For
   example, about one Moment in 470,000 at the Sun's surface passes with no step. The other picture that also passes,
   3386's, keeps one Planck sphere per Moment for light, but then a crystal holds slightly more Planck spheres near the
   Sun. That contradicts your "same number of PSRs".

## 6. PD-008

- **Convenient branch, marked:** the passing reading (B) is the one that rescues his proposal. It is offered with its
  history (3385's withdrawn knob) and its owed mechanism, not as settled.
- The failing reading (A) is stated plainly, including the missing Newtonian pull.
- 4386's suspensions stay until he answers.

# The CP as the Only Outlet: the Founder Gives the Metering a Structure. The Reservoir Can Discharge Only Through the CP, Which Takes One Increment Per Swing, So It Drains a Little at a Time; the Drain Rate Itself Is Still to Be Derived. Two Details Meet Measurements: "the Same Increment Each Swing" Gives a Flat Packet With Side Lobes in Its Colour, While Measured Lines Are Lorentzian, Which Needs the Same Share of What Is Left Each Swing; and a Swing Turning at the Upper Orbit Has One Rate, Yet One Upper Orbit Gives Different Colours Depending on Where the CP Lands

**Patch:** 4451. **Lane:** foundations, with QM and EM. **Session:** 242.
**Founder input:** `founders_voice/4451_one_increment_per_swing_cp_only_outlet.md` (answers 4450 §5).
**Script:** `series_standard_model/code/4451_line_shape_and_apogee.py`.
**Critic:** a fresh-context critic returned ACCEPT WITH CHANGES (verbatim in
`series_standard_model/reviews/2026-10-01_session_242_critic_returns_verbatim.md`). It confirmed every number. It found that the first draft:
- overclaimed the metering (a structure, not yet a rate);
- stated "measured lines are Lorentzian" without the Doppler hedge;
- did not state the identical-packet assumption;
- used an only-approximately-isochronous pendulum;
- dropped his unfinished last bullet;
- led the second question;
- had no todolist entry.

All six required changes are taken in, with the optional notes.

## 1. His answer

- **The cascade's speed:** he knows no way to make a 3 cm/s wave except a high SSV_abs, which he assumes the orbital space does not have.
- **Another mechanism: the decay proceeds one oscillation at a time.** The stored DP arc-separation energy discharges as fast as the ZBW radiates, the
  same increment each cycle, out of the energy between the two levels. Each ZBW oscillation is started from this reservoir of charged, non-resonant
  DPs. (His last bullet here is unfinished: "The increment of energy between the DP-arc-separation of the activated layer and the lower energy stable
  orbital is the total amount of DP-arc Separation". Its reading is pending.)
- **Why it releases slowly: the reservoir's only outlet is the CP.** The CP and the DP arc-separation trade energy in and out as the CP orbits, and keep
  doing so when it is knocked out of resonance. Then all the stored energy drives the ZBW oscillation, and the energy supplied to it is radiated: that is
  the reservoir's leak. The nucleus holds the DPs in place as a captured system.
- **Why each swing is the same:** the CP, now a ZBW oscillator, keeps the same rate and amplitude because it draws from the same reservoir. It swings
  from the upper orbit through the centre to the other side and back to the same apogee at the upper orbit, where the increment between the two orbits
  pushes it each time.

## 2. The metering: a structure

**The CP as the only outlet is a real metering structure.** If the energy can leave only through the CP's radiation, the reservoir cannot empty in one
sweep. It drains at the rate the CP radiates, a little each swing. That answers 4450's question of why the energy is not let out all at once, and it
removes the need for a 3 cm/s cascade (he confirms the orbital space's SSV_abs is not high). The nucleus holding the DPs in place, as a captured system,
keeps the reservoir from dispersing.

**The drain rate itself is not yet derived from it.** The lifetime of 1.6 ns follows only if the CP's radiated power per swing is about 1/(fτ) ≈ 2.5 ×
10⁻⁷ of the stored energy. That, and how lifetimes change from orbit to orbit, is owed. Standard physics gives a guide: a charge radiating as it swings
loses power in proportion to the square of its swing, so the energy left, and the same share of what is left goes each swing by itself (classical
radiation damping). For an electron swinging at Lyman-α's frequency that damping time is about 0.66 ns, the same order as the measured 1.6 ns (4445
part 4).

## 3. Two details that meet measurements (script)

**The same increment each swing, or the same share of what is left?** (script part 1)
- **The same increment each swing** means a packet of constant amplitude that stops when the reservoir is spent. Its colour then has side lobes: faint
  echoes on either side of the line, the largest about 5% of the peak, as for any flat pulse that switches off.
- **The same share of what is left each swing** means a packet whose amplitude dies away smoothly. Its colour is a single smooth peak with no side lobes
  (a Lorentzian), with width exactly 1/(2πτ) for lifetime τ.
- **What is measured:** the light from a decay fades exponentially in time, the most direct evidence. And the natural line, seen with Doppler
  broadening removed (Doppler-free spectroscopy, atomic beams), is Lorentzian with width 1/(2πτ). (Most lines as usually observed are also widened by
  the atoms' motion, which would hide side lobes.) So each swing must take the same share of what is left, not the same amount.
- **The assumption behind the flat-packet argument:** every packet is the same length. Random start times do not change the shape. Flat packets of
  exponentially distributed lengths would average to a Lorentzian (Lorentz's collision-broadening model), but here a fixed increment and a fixed total
  ΔE give every packet the same length.

Two natural ways to get that in his picture: if the reservoir's push on the CP at each return is in proportion to how charged it still is, or if the
outlet is the CP's own radiation, whose power goes with the energy left (radiation damping, §2), each swing draws the same fraction of what remains. The light then fades smoothly, and its line has the measured shape.

**A swing turning at the upper orbit has one rate; one upper orbit gives several colours** (script part 2). A swing through the nucleus from the upper
orbit out to the other side, under the nucleus's pull, has a rate set by how far out it turns. Turning at hydrogen's second orbit, that rate is
2.33 × 10¹⁵ Hz, close to Lyman-α's 2.47 × 10¹⁵. But from the third orbit hydrogen gives two different colours: 2.92 × 10¹⁵ Hz when the CP lands in the
first orbit, and 4.57 × 10¹⁴ Hz when it lands in the second, six times slower. A swing turning at the third orbit has one rate, 6.9 × 10¹⁴ Hz, which
matches neither. So the swing's rate cannot be set by the upper orbit alone; the orbit it lands in must also count. (The near match for the second orbit
is a coincidence: it fails for the third.)

**And the rate must not depend on the swing's size** (script part 3). A swing through the nucleus speeds up as it shrinks: 1% smaller, 1.5% faster. If
the amplitude dies away, as the measured line shape requires, the rate must still hold to 4 parts in 10⁸. So the swing that radiates must keep its
rate fixed while its size shrinks, like a mass on a spring, whose period does not depend on how far it swings.

## 4. What stays open

- **The drain rate** from the CP's radiated power per swing: τ ≈ 1.6 ns for Lyman-α, and how lifetimes change with the orbits.
- **The share per swing:** in proportion to what is left in the reservoir (Claude's suggestion within his picture), giving the measured exponential decay.
- **His unfinished last bullet** on the increment and the total DP arc-separation (reading pending).
- **What sets the rate,** with the landing orbit counting as well as the upper one, and holding steady while the swing shrinks.
- **His reservoir and outlet** in CPP terms: how the DP arc-separation pushes the CP at each return, and how the nucleus holds the DPs.
- **Carried:** 4450 items c, d, f.
- **Answered:** 4450's founder question (metering structure: the CP as the only outlet; the cascade speed: not a slow cascade, one swing at a time).
  4450's light-speed assumption is closed by his answer.
- **Not adopted as stated:** the same increment each swing (gives side lobes; measured lines are Lorentzian); a rate set by the upper orbit alone.

## 5. Question to the founder (physical picture)

From hydrogen's third orbit the CP can land in the second orbit, giving red light, or in the first, giving ultraviolet light six times faster in its
swing. **If the swing turns at the third orbit both times, what makes it swing six times faster when it is headed for the first orbit?** And measured
light from a single decay fades smoothly rather than stopping all at once: **as the reservoir drains, what happens to its push on the CP?**

## 6. Answer to his "What do you think?"

I think he's given the metering its structure. If the reservoir can only lose its energy through the CP, a little each swing, it can't empty all at
once, and that removes the need for a slow cascade. What it doesn't yet give is how fast it drains: the 1.6 billionths of a second still has to come out
of how much the CP radiates each swing. Standard physics suggests it can: a charge swinging at that rate loses energy on about that timescale.

Two details need adjusting against what's measured. First, the same amount each swing would make the light stay at full strength and then stop
suddenly. A packet like that has faint echoes on either side of its colour, about 5% of the main peak. What's measured is that the light from a decay fades
away smoothly, and the line, once the blurring from the atoms' motion is removed, is a single smooth peak. So each swing takes the same share of what's
left, not the same amount. That fits his picture nicely if the
reservoir's push on the CP weakens as it drains.

Second, a swing that always turns at the upper orbit would have one rate. But from hydrogen's third orbit the CP can land in either lower orbit and gives
two very different colours, one six times the other. So the rate has to depend on where it lands, not just where it starts. And since the swing shrinks
as the light fades, its rate has to stay fixed while it shrinks, which a swing through the nucleus doesn't naturally do.

## 7. PD-008

- **Credited:** the CP as the reservoir's only outlet, as the metering structure (the rate is owed).
- **Claude's suggestion, marked:** the reservoir's push in proportion to its remaining charge (giving the exponential decay).
- **Not adopted as stated:** the same increment each swing; a rate set by the upper orbit alone.
- **Not claimed:** novelty for Lorentzian line shapes or the Kepler rate.
- Nothing registered.

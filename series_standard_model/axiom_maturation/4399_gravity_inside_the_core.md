# Gravity Inside the Black Hole: the Founder's Curve (Largest at the Edge, Zero at the Centre) Is Newton's Own Proof, and It Requires the Black Hole's Matter to Fill Its Interior. That Clashes With the Corpus's Ringdown Bound (3702: Most of the Mass Deep Inside) and Its Selected Drain Reading (3703). Where the Matter Goes Is the Question

**Patch:** 4399. **Lane:** foundations, with GR. **Session:** 242.
**Founder input:** `founders_voice/4399_gravity_inside_bh_max_at_edge_zero_at_centre.md` (answers 4398 §5, §8).
**Script:** `series_standard_model/code/4399_gravity_inside_the_core.py`.
**Critic:** a fresh-context critic returned HOLD on the first draft (verbatim in
`series_standard_model/reviews/2026-10-01_session_242_critic_returns_verbatim.md`). It confirmed the algebra, but the
draft had left out a recorded ringdown bound that his curve breaks (3702), had missed the corpus's own interior (3703),
and had presented the option it preferred without naming its main cost. All eight required changes are taken in.

## 1. His clarification

- "No net pull in any direction" inside the black hole meant **SSV_net = 0**: the plus and minus charges sit at equal
  distances around every CP, so the electric push balances. It did not mean zero gravity.
- **Gravity (the SSV_abs gradient) inside points to the centre, is largest at the edge, zero at the centre, and falls
  steadily between.**

His 4398 text said "there is no gravitational gradient, so the gradient is zero". 4398 §5 read that faithfully; he has
now revised it. 4398 §5's conclusion (the mass must sit in the edge layer) is withdrawn with his revision.

## 2. His curve is Newton's proof (script part 1)

His counting is Newton's own: along each line through a point inside a ball, the part toward the centre and beyond
(R + r) pulls inward and the part toward the near surface (R − r) pulls outward. Per unit of solid angle, the matter
grows with distance squared and the pull falls as one over distance squared, so each part pulls in proportion to its
length. The net is 2r, so the pull rises in proportion to r from zero at the centre. The outer layers cancel exactly,
which is the shell theorem; it holds exactly because the census u = Σm/r is harmonic. The script checks it by summing
inverse-square pulls over a shell.

## 3. His curve requires a filled interior, and that clashes with the ringdown bound

For the pull to be largest at the edge, the mass inside every radius r must satisfy m(r) ≤ M(r/R)²: **the matter must
be spread through the interior**. A uniform ball gives his curve exactly; any profile whose local density is at least
two-thirds of the mean density inside it also does. A mass drained to a small central core gives the opposite: the pull
grows inward toward the core.

The corpus already has a recorded constraint here:
- **3702 (estimate-grade, from a proxy potential):** the ringdown of merged black holes requires **≳ 90% of M inside
  2M**. "A uniform flat core (42% inside 2M) is excluded for black holes by the ringdown."
- At r = 2M (¾ of the 8m/3 radius), his curve allows **at most 56% of M inside**. **His curve and 3702's bound cannot
  both hold.**
- **3703** used that bound to choose between two readings of a saturated core: STOP (matter halts at 8m/3) and DRAIN
  (matter keeps falling at up to c/2 and collects in a Planck-density core ~10⁻²⁷ of 2M across, leaving the visible
  shell nearly empty). **The ringdown selected DRAIN.** His filled-core curve is the STOP picture.
- **4370** likewise had the end state as a Planck-density speck.
- **3623** (absorbed energy stored as CP vibration in the core) does not say where the energy sits, so it is neutral.
  Its CPs "at 1 PSR" spacing is Planck density, which 4370 used for the speck rather than a ball filled out to 8m/3.

**The trade, stated plainly:** draining to a central core puts the shift at 1 at r = 2m (a wave horizon), which is what
makes 3675's GR ringdown boundary work, and there his outward sign would matter (4398 §2's condition). A filled core
keeps the shift below 1 everywhere, so there is no wave horizon and the ringdown would have to be recomputed from
scratch. 4370 §2 and 3702 already disagree on whether the interior affects the ringdown; this patch does not settle that.

## 4. If the core is filled: what clocks do inside (script parts 3–5)

The shift follows the enclosed mass, β² = 2m(r)/r, and is continuous at the edge (true for any profile with no mass
sheet at the surface, so it is not evidence for his curve). The clocks are a separate choice. The numbers below are for
a uniform ball at the 8m/3 floor.

| | **A: Einstein's filled interior** | **B: Planck sphere pinned at ½** | **C: 3703's two clocks** |
|---|---|---|---|
| matter's clock, edge → centre | ½ → ¼ | ½ → ½ | ½ → ½ |
| clock of the waves' medium (the sea) | the same as matter's | the same | follows the enclosed mass |
| sideways light reach, edge → centre | ½ → ¼ | ½ → ½ | — |
| radial reach just inside the edge | 0.134 toward, 1.866 away | the same | — |
| a CP released at rest halfway in | **falls toward the centre** | **stays put**: the gradient acts on nothing | matter as B; waves as A |
| support, in Einstein's terms | positive pressure, reaching the energy density at the centre | an even tension, one third of the energy density | — |
| edge | no surface layer | a membrane with pressure but no energy (violates the dominant energy condition) | — |

- **A** keeps Einstein's link between the pull a CP feels and clocks slowing in the direction of the pull (measured in
  weak fields: Pound–Rebka, GPS). Its matter clock goes below ½, which the corpus allows for the sea's clock (3703) but
  not for matter's register. Two notes: the felt pull peaks slightly inside the edge (about 0.86R), because pressure adds
  to it; and 8m/3 is exactly where a uniform ball's central pressure reaches its energy density, the limit of ordinary
  matter, a coincidence worth noting.
- **B** keeps the floor, but **his gravity would act on nothing**: a CP released at rest inside stays at rest. That
  contradicts his own bullet that the gradient acts "as a gravitational force" on the middle region. B matches his curve
  only in the shift, not in force. Its tension is also backwards for a jammed core: a medium resisting further shrinking
  (his 4370 six-neighbour halt) supplies pressure, which is A.
- **C** is the corpus's existing interior (3703): the matter clock flat at ½ ("no register quantity continues below
  lapse ½"), the sea's clock following the enclosed mass. In a filled core the sea's clock would not reach zero, so C
  without DRAIN loses its wave horizon too.

**c/2:** B gives c/2 sideways throughout and in all directions only at the centre; just inside the edge every option
has radial reaches of 0.134 and 1.866. 3623's c/2 has no stated direction, so none of the options can be said to match
or miss it exactly.

## 5. What stays open

- **Where the matter goes:** his filled core against 3702's bound and 3703's DRAIN (founder question). Resolve or
  retract one.
- **The ringdown with a filled interior:** no wave horizon at 2M, so 3675/3702's ingoing boundary has to be redone,
  with echoes and damping (RCORE arc).
- **Non-uniform profiles** his curve allows: central clock and compactness for each.
- **Neutron stars:** any STOP-like filled interior bears on 3703's owed item 8 and the flat-core statics of 3634–3637.
- **A:** how the matter clock goes below ½ (R-DIBIT-COUNT-AT-FLOOR, 4356). **B:** the membrane at the edge and what the
  tension would be in CPP.
- **Carried:** 4398 (a), (b), (d)–(g), with 4398 (c) superseded by the first item; the 4397 items; 4311's floor
  attainment.

## 6. Answer to his "What do you think?"

His curve is right for a ball filled with matter, and his counting is Newton's own proof of it. But it holds only if a
black hole's CPs fill its interior. An earlier estimate (3702) found that the measured ringing of merged black holes
needs nearly all the mass packed deep inside, and 3703 chose "the matter keeps falling to a tiny dense core" for that
reason. His picture and that result cannot both stand, so the question is where the matter ends up.

## 7. Question to the founder (physical picture)

Picture matter falling into a black hole. When it reaches the edge, where the DI-bit shell fills the Planck sphere,
**does it stop and pile up, filling the ball out to the edge (your curve), or keep falling, at up to half light speed,
until it collects in a tiny dense speck at the centre (what the ringdown estimate wants)?**

And if it fills the ball: release a CP at rest halfway to the centre. **Does it start to fall toward the centre, or stay
where it is?** If it falls, clocks must keep slowing toward the centre (a quarter of far-away rate there for a uniform
ball). If it stays, what holds the edge?

## 8. PD-008

- **Convenient branch, marked:** B in the first draft (keeps the floor and c/2). Its cost, now named: in B his gravity
  moves nothing.
- **Inconvenient result surfaced:** his curve conflicts with the corpus's own ringdown bound (3702) and its selected
  DRAIN reading (3703). Stated, not resolved; 3702 is estimate-grade.
- **Withdrawn:** 4398 §5's edge-layer conclusion, on his revision.
- Nothing registered.

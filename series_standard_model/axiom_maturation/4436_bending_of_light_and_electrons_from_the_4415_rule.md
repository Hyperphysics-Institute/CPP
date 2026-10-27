# The Bending of Light and Electrons From the 4415 Rule: Realness as Mass Settles Equal Fall. The Bending Is Reproduced, Under Stated Assumptions: a CP Stepping at a Fixed Fraction of the Local Light Speed c/K (4415) and Turning Toward the Slower Side at the Snell Rate (His Limb Picture, as Claude Quantifies It) Has Exactly GR's First-Order Acceleration in Every Direction, Provided the Census Push Acts Only on the Rest-Mass Fraction, 1/γ². Run as a Step Rule, It Gives GR's Bending at Every Speed, Light Included. This Sits in Tension With "Realness Is Mass" for the Push

**Patch:** 4436. **Lane:** foundations, with GR and EM. **Session:** 242.
**Founder input:** `founders_voice/4436_equal_fall_accepted_realness_is_mass.md` (answers 4435 §5).
**Script:** `series_standard_model/code/4436_bending_solved.py`.
**Critic:** a fresh-context critic returned ACCEPT WITH CHANGES (verbatim in
`series_standard_model/reviews/2026-10-01_session_242_critic_returns_verbatim.md`). It confirmed the algebra and the GR comparison, and
supplied the Jacobi-index reading below. It found that the first draft:
- left unstated a conflict between the fading push and "realness is mass" with 4424's inertia;
- called 4434's split a misreading when it is also GR-consistent;
- claimed "solved" and closures beyond what is shown;
- asked a leading, physically off question;
- misfiled the Shapiro delay as second order;
- overstated equal fall for bound systems;
- integrated only the closed form.

All seven required changes are taken in, and the script now also runs the step rule itself.

## 1. His answer

- Platinum and titanium balls of the same mass fall alike, which **rules out his framing** that relativistic realness raises the fractional
  gravitational acceleration; and there is no reason for realness to switch on at light speed.
- **Corrected view: the amount of realness is the amount of mass effect (resistance to acceleration).** That resolves the equal-mass,
  equal-acceleration dilemma, and keeps realness as the carrier of the charged capacitor's extra mass (4417).
- **Is the bending of light and electrons now solved too?**

## 2. Equal fall

With realness as mass, a partly real organization adds inertia and weight in the same proportion, as ordinary mass does, which matches the
composition tests (4435) and his capacitor picture (4417). For bound matter one more thing is required and not shown: in this bookkeeping a
constituent's acceleration depends on its speed (averaged over directions, g(1 − ⟨v²⟩/3), exactly as in GR). Equal fall for a composite body then
needs the binding fields to gravitate as they do in GR (the virial cancellation, 4435). Recorded as his statement; not registered.

## 3. The bending, reproduced (script)

**The ingredients:**
- **WC-DP-SEA-PV (4392), a convention:** near a mass the local light speed is c/K, with K = 1 + 2U and U = GM/(rc²). (This puts in PPN γ = 1.)
- **4415 (Claude's rendering of his answer):** a CP steps each Moment by f × (local light speed), with f held in the sea's organization and
  changed only by forces. With no force, its speed is s = f c/K: it slows where K is higher.
- **His limb picture (4435, component (1)), as Claude quantifies it:** the inner limb, in slower space, lags, so the path turns toward the slower
  side at the Snell rate: dn/dt = s × (the sideways gradient of ln K), at every speed.
- **4403's census push** from the limb difference, allowed a factor P(f).

**The algebra** (c = 1, first order in U, g the Newtonian field toward the mass, so the gradient of ln K is 2g). For the velocity u = s n:

    du/dt = (ds/dt) n + s (dn/dt) = −(u·∇lnK) u + s²[∇lnK − n (n·∇lnK)] = 2s² g − 4 (u·g) u
    total:   a = g P + 2s² g − 4 (u·g) u

GR's first-order acceleration of a test particle (isotropic coordinates, PPN γ = 1, dropping the −4Ug term, which does not affect bending) is
a = g(1 + s²) − 4(u·g)u. **The content is that one factor matches both directions:** sideways (GR 1 + v²) and along the field (GR 1 − 3v²). Both
are met if and only if, for a push along g with a size depending only on speed, **P = 1 − f² = 1/γ²**.

**Checked two ways (script):**
- **Part 2**, integrating the closed form, is a consistency check: GR's acceleration integrates to GR's deflection.
- **Part 3** runs the step rule itself: store f, set the speed s = f/K, turn n at the Snell rate, add the push. It gives 2.0200 × 10⁻⁴,
  1.0000 × 10⁻⁵, 4.4691 × 10⁻⁶ and 4.0000 × 10⁻⁶ at v = 0.1, 0.5, 0.9 and 1, matching GR's (2GM/(bv²))(1 + v²) to the digits shown.
- **A constant push** (P = 1) bends everything too much, light by half again.

**Why the decomposition is legitimate for a particle (Jacobi's index).** In GR a particle's path follows an optical-like index
n_J = K √(E² − m²/K), whose gradient is ∇lnK × [1 + m²/(2p²)]. Multiplied out, that is exactly a full Snell term plus a term (1 − v²)g. So the
decomposition is the geodesic itself at this order: **the fading push is the rest-mass term of the matter index**, g × m²/E², acting on the
rest-mass fraction, not on energy or realness. This is not PV's mechanism (PV uses a Lagrangian with mass rule m ∝ K^(3/2)); it plays the role PV's
mass rule plays.

**How the work divides:** for a slow particle almost all the fall comes from the push (the refraction term 2s²g is tiny); for light it all comes
from the refraction, the push having faded to nothing. The split is not invariant: 4434's split also reproduces GR, as does 4403's bookkeeping.

## 4. The tension with "realness is mass", and with 4434

**With realness as mass**, the push would act on the whole moving organization: weight ∝ γm. With 4424's inertia (γ³m along the motion, γm across),
that gives an acceleration of g across and g/γ² along: 4434's split, not an isotropic 1/γ². Combined with this patch's full Snell-rate refraction, it
would give g(1 + 2v²) across, and light would bend half again too much.

**So the two must be reconciled.** Under this patch's split, the push couples to the **rest-mass fraction** (m²/E² = 1/γ²), and the gravity of the
motion's energy enters through the refraction. Under 4434's split, the push acts on the whole energy, and the refraction supplies only half
strength. Each reproduces GR. What rules 4434's split out here is only the choice of full Snell-rate refraction under the 4415 rule. Which one CPP
has is a physical question, put to him (§6).

## 5. What stays open

- **Which split:** the push on the rest organization with full-rate refraction (this patch), or the push on the whole moving organization with
  half-rate refraction (4434). How "realness is mass" fits each. Founder question.
- **The CPP mechanism of P = 1/γ²** (the rest-mass term of the matter index), if this split holds.
- **Second order:** the perihelion advance needs K's 2U² term, the −4Ug term, and second-order pieces of both the push and the refraction.
- **The Shapiro delay** is first order in U and follows from the local light speed c/K.
- **The assumptions:** WC-DP-SEA-PV (γ = 1 put in), 4415's rendering, and Snell-rate refraction (Claude's quantification of his limb picture).
- **Equal fall for bound systems** (binding fields gravitating as in GR).
- **Answered:** 4435's founder question (equal fall; realness is mass). **Supplied, in a different bookkeeping:** 4434 item 2 (the speed-growing
  part of the bending, from the 4415 rule with refraction). **Moved:** 4435 item 4 (the missing mass rule) into "the mechanism of P = 1/γ²".
- **Carried:** 4435 items 2, 3, 5; 4434 items 3, 4, 5.

## 6. Question to the founder (physical picture)

A fast electron passes the Earth. Its organization has two parts: its resting core (the electron's own rest mass) and the extra partly real DPs its
motion has gathered. **Does the Earth's limb push act on the resting core only, with the bending from the motion coming entirely from the slower
inner limb? Or does the push act on the whole moving organization, extra realness included?**

## 7. Answer to his "What do you think?"

His corrected view is right: realness is mass, adding weight and resistance to being pushed in the same proportion, so every material falls alike,
and the capacitor still gains mass through its organized DPs.

On the bending, it can be reproduced exactly, under stated assumptions. Take the rule from 4415: a particle steps at a fixed fraction of the local
light speed, so it slows where light slows, near a mass. Add his picture of the inner limb lagging and turning the path. Together they give exactly
the measured bending of light and relativity's extra bending of fast electrons, in every direction and at every speed. I checked it by running that
step rule past a mass. The condition is that the ordinary gravitational push, the one that makes a dropped ball fall, acts only on the particle's
resting mass, so that its effect fades as the particle nears light speed, down to nothing for light.

That raises one question, because it seems to pull against "realness is mass". If the push acted on all the electron's mass, its gathered realness
included, the inner-limb bending would have to be only half as strong for the totals to come out right. Both versions match relativity. Which one is
CPP's is for him to say, and I've asked him.

## 8. PD-008

- **Convenient branch, marked:** "the bending is solved." Withdrawn; it is reproduced given K = 1 + 2U, 4415's rendering, Snell-rate refraction, and
  P = 1/γ², which is required, not derived.
- **Owned:** the first draft's description of 4434's split as a misreading, and its leading question.
- Nothing registered.

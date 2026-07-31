# B1 MEETS THE SR SECTOR — A SIGN CONFLICT, AND A STRUCTURAL PROBLEM BENEATH IT

**Patch 2898. The founder asked directly: what should change, and should
the relativity sector be checked? Checked. The answer is worse than a
mismatched coefficient.**

---

## §1 — CANDIDATE 1: DOES SSV_abs COMPENSATE? NO.

**The idea, and it was a good one:** SSV_abs is computed from the *same*
arriving contributions as the drive — magnitude-sum where the drive is
vector-sum. Being a scalar with no preferred direction, its leading
correction must be even in v, i.e. β². If SSV_abs ∝ (1 − 0.201β²), then
μ = PSR/SSV_abs inherits exactly the growth B1 requires and **Newton I
would hold with no new physics.**

**Measured** (`code/2898_ssv_abs_velocity_dependence.py`, same integral,
magnitudes instead of axial projection):

| β | SSV_abs | S(β)/S(0) | implied c_S |
|---|---|---|---|
| 0.05 | 11.739785 | 0.9999999 | 0.00003 |
| 0.10 | 11.739782 | 0.9999997 | 0.00003 |
| 0.20 | 11.739771 | 0.9999988 | 0.00003 |

**c_S = 0.00003 against the required 0.201 — four orders of magnitude too
small. SSV_abs is flat to one part in 10⁶.**

**Why, in hindsight:** summing *magnitudes* over a symmetric sphere, the
fore contributions weaken by almost exactly what the aft ones gain. The
cancellation is near-perfect. Direct test confirms: D/(β·SSV_abs) still
drifts 8.03×10⁻³ — **identical to the uncorrected drift. SSV_abs
contributes nothing.**

## §2 — CANDIDATE 2: DOES PSR COMPENSATE? IT GOES THE WRONG WAY.

The SR sector specifies PSR under motion:

> **c05 §254:** *"contracts its PSR_eff = ℓ_P/(1 + k·ΔSSV) exactly as
> acceleration does in flat space… the PSR contraction is identical in
> both cases."*
>
> **c04 §163:** *"at relativistic velocities the PSR contracts severely."*

**B1 requires PSR to GROW as (1 + 0.201β²). The SR sector says it
CONTRACTS.**

In the c05 parameterisation with ΔSSV ∝ β², B1 requires
**k = −0.201** — a *negative* coefficient, i.e. PSR expanding with speed.

> **This is a SIGN conflict, not a magnitude mismatch. The SR sector does
> not fail to supply the compensation — it supplies the opposite,
> deepening the drag.**

## §3 — THE STRUCTURAL PROBLEM UNDERNEATH

The CPP primitive is **velocity-proportional**:

    d = (|SSV_net| / SSV_abs) · PSR         (displacement per Moment)

**not** acceleration-proportional. That distinction is decisive for
Newton I.

- **In a ∝ F mechanics:** free motion is automatic. F = 0 ⟹ a = 0 ⟹ v
  constant. Newton I costs nothing and is robust to any velocity-dependence
  of the coefficients, which affect only the *response to forces*.
- **In v ∝ SSV_net mechanics:** free motion must be *actively sustained*.
  SSV_net = 0 ⟹ d = 0 ⟹ **the CP stops.** So a coasting CP requires a
  permanently maintained nonzero drive, and Newton I requires that drive
  to be **exactly** proportional to v with an **exactly** constant
  coefficient.

> **Newton I is structurally fragile in CPP.** It demands two exact
> conditions where Newtonian mechanics demands none. **Both fail as
> currently specified:** the drive carries β² curvature (B1, measured,
> model-independent), and PSR carries β² contraction (SR sector,
> specified) — **and both push the same way, toward drag.**

## §4 — WHAT THIS DOES AND DOES NOT MEAN

**It is NOT a refutation of CPP.** It is a conflict between three things
that cannot all be right as stated:

1. the round-trip inertia mechanism (CONJ-FP-1, as modelled at 2884/2897)
2. the velocity-proportional primitive
3. the SR sector's contracting PSR

**Any one of the three could be the thing to change**, and the founder's
own standing instruction applies: *"All phenomena should fall out of this.
If it doesn't then this is the rule that should be changed."*

**It is also NOT established on the substrate.** §1–2 are computed in the
continuum retardation model of Patch 2884. That model reproduces the
Liénard–Wiechert null exactly, which is a real validation — but c = 0.201
remains a property of the model. **Registered as a limitation, not
waved.**

## §5 — THREE DIRECTIONS, FOR THE FOUNDER

**(A) The drive model is wrong.** The 2884 model treats the Sea as static
in the absolute frame. A self-consistent treatment — where the DP arcs
near a moving CP are themselves displaced by it, partially co-moving —
could change the β² term. **This is the cheapest to test and the worker
recommends it first.**

**(B) The primitive needs a distinct form for free motion.** If a free
coasting CP has SSV_net = 0, the primitive gives d = 0 and nothing moves;
so CPP currently *requires* a sustained drive. **If instead the
displacement carried forward were part of the state, Newton I would be
automatic — but that contradicts the founder's 7 July no-carried-velocity
ruling.** The tension between that ruling and the velocity-proportional
primitive is now explicit and is registered here as an open structural
question.

**(C) The SR sector's PSR needs re-derivation for inertial motion.** c05
asserts gravitational and inertial PSR contraction are *identical* via the
equivalence principle. **That identification is what forces the sign.** A
CP in free fall is accelerating; a coasting CP is not. Whether the
equivalence-principle identification holds for *uniform* motion is a
physics question, and it is the load-bearing assumption in the conflict.

## §6 — STANDING

Ledger untouched: 1B OPEN; PR7 PARTIAL; six of seven; B7 holds; Candidate
(B) 79.5%. G1 and P-A2-1 stand. Statics suspension per 2892 stands.

**CONJ-FP-1: Condition B closed (2895); Condition A open; LINK 2 open;
LINK 3 — the cross-sector test B1 enabled has been RUN and returns a SIGN
CONFLICT. Registered as the arc's principal open problem.**

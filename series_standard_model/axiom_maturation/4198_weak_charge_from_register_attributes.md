# The Contact Scalar, Assembled from What a CP Already Carries — Plus One Term

**Patch:** 4198. **Lane:** EW. **Session:** 236.
**Verify:** `series_standard_model/code/4198_weak_charge_from_register_attributes.py`.
**Works:** TODO-4196-CONTACTSCALAR item (1), both parts owed at 4197. **Status:** bookkeeping that
fits, with its free choices counted (§3). **No mechanism derived; nothing adopted.**

---

## 1. What SF-4 says a neutrino is

> *"The neutrino is identified as an unbound 3D orbital ZBW configuration of dipole-pair structures
> with no central CP anchor."* (SF-4 §, FI-α-3)

**Against 4197 §3.2** (*the linear ZBW's unit leaves as the antineutrino*): **the "no anchor" half
fits** — a neutrino in CPP is ZBW motion with nothing at its centre, which is what a captured −eCP's
oscillation against the +qCP becomes when the capture ends. **The "linear" half does not:** SF-4 says
3D orbital. Whether a linear mode set free becomes a 3D orbital one is not addressed anywhere I found.

## 2. The assembly

Q_W = 2T₃ − 4Q sin²θ_W, and CPP's 4 sin²θ_W = 3/(2φ). The second piece is **electric charge**, which a
register already reads. For the first, the trial is

> **2T₃ = (sum of the polarity signs of the unpaired CPs) + (a ZBW-mode term)**
> mode term: **0** for orbital ZBW about an anchor; **−1** for the **linear** ZBW of a captured −eCP
> (the founder's pointer); **+1** for unanchored ZBW with no central CP (the neutrino).

Paired CPs — Sea DPs, the electron's orbiting eDP — contribute nothing. Rows verbatim (D-11):

```
4 sin^2 theta_W = 3/(2 phi) = 0.92705

             polarity sum  mode  2T3 built  2T3 SM  charge  Q_W built   Q_W SM
up quark                1     0          1       1   0.667     0.3820   0.3820
down quark              0    -1         -1      -1  -0.333    -0.6910  -0.6910
electron               -1     0         -1      -1  -1.000    -0.0729  -0.0729
neutrino                0     1          1       1   0.000     1.0000   1.0000
proton  uud             2    -1          1       1   1.000     0.0729   0.0729
neutron udd             1    -2         -1      -1  -0.000    -1.0000  -1.0000
```

## 3. What is a check and what is a choice

- **Checks (no freedom):** the **up quark** and the **electron**. With mode = 0, *weak isospin is just
  the polarity sign of the unpaired CP*: +qCP → +1, −eCP → −1. Two for two.
- **Choices:** the mode terms −1 (down quark) and +1 (neutrino) are set to fit.
- **One consistency the choices then pass:** in d → u + e⁻ + ν̄ the polarity sum (0 → +1 − 1 + 0) and
  the mode term (−1 → 0 + 0 − 1) are **each conserved separately**.
- **Consequences, not independent tests:** proton and neutron.

**Reading.** Most of the weak charge needs **no new content**: A1′ already gives every CP a polarity
and a type, and type fixes the charge. **The one thing polarity and charge cannot supply is the mode
term — and that is exactly what the founder named as unique to the neutron.** The content question of
4196 narrows to: **how does a GP's register distinguish linear from orbital ZBW?** A linear
oscillation passes back and forth through the same GPs along one axis; an orbit does not. That is a
difference in *which GPs are revisited*, which a register that integrates arrivals could in principle
see. **Not shown.**

## 4. Where the three threads now meet

- 4193: a mirror-odd, time-even, CP-even displacement must be q (e·A), own A.
- 4194: its weight cannot be constant; 4196: measured physics says the weight is the partner's weak
  charge at contact, zero in free space.
- 4197–4198: that weight is polarity count − (3/2φ)·charge + the linear-mode term.

**Missing link: range.** The measured interaction is contact (~2×10⁻¹⁸ m), and nothing here says why
the gate reads only co-located partners and not their a/r far field (4184), which has no range at
all. SF-2's Z icosahedron is the obvious place to look; **not looked at.**

## 5. PD-008

No convenient branch. Weak points: §2's mode values are fitted; "polarity sign = weak isospin" is
tested on two particles of one generation; antiparticles, right-handed states (which have T₃ = 0 —
the assembly as written does not know about handedness at all) and the heavier generations are
untested. **The right-handed case is the serious one:** the weight must depend on the moving
particle's b as well as on the partner's content, and this patch does not say how.

# Under the Registered Relay the "Sail" Is Automatic and Gauss's Law Is a Theorem; α's LPI Then Needs a Charge's DI-bits to Fill Its Whole PSR Ball

**Patch:** 4355. **Lane:** EW → foundations. **Session:** 241.
**Founder:** `founders_voice/4355_answer_gp_reads_whole_arc_of_reradiation.md`.
**Verify:** `series_standard_model/code/4355_shell_mean_relay_lpi.py` (output `…lpi.out`, < 1 s).
**Answers:** 4354 §4. **Corrects:** 4354 §2–§3 (erratum appended there).

## 1. What the registered axioms already say (the founder was right to send me there)

- **AP-4** (A1′ row): a DI-bit carries {origin address, E, S}, a static snapshot of its origin GP's computed registers;
  E sums the contributions sourced by the CPs at that GP *together with those it integrated in the previous Moment*.
  R-CP-ONLY-SOURCE (3872): the arrivals are prior CP contributions relayed onward. That is the relay he describes.
- **AP-3 / A3′:** each Moment a GP computes its state from the arrivals over its PSR shell, all channels by the same
  icosahedral shell-sum.
- **GR-1j, Theorem "Exact statics"** (v1.0, 20 Aug 2026): one hop = one Moment = one PSR; the elementary operator is
  the **shell mean over the PSR** on the rigid lattice; static self-consistency is exactly Laplace for any PSR profile,
  and messenger conservation forces the two-level (lossless) relay.

So both of my 4354 questions were already answered on file:

1. **Sail or single point:** both. The CP is read at one GP (his first point), and that GP's state is the mean over its
   whole PSR shell (his second point: "an entire arc of re-radiation"). The dichotomy I posed was false.
2. **Lossless:** yes, by GR-1j (conservation forces the two-level relay; statics is exactly Laplace). Gauss's law and the
   1/R² field are theorems of the registered relay, not new rules.

## 2. Pressed to the end: what α does in a well under this relay

Static state u = M_R u + s (M_R the PSR-shell mean, s what the sources add each Moment). In Fourier space
û = ŝ/(1 − M̂(k)), and for the lattice shell 1 − M̂(k) = k²⟨r²⟩/6 (checked: 0.999 at small k, isotropic). So far from
the source

    u(r) = 6Q / (4π ⟨r²⟩ r),   Q = total injected per Moment,

and at a fixed distance measured in PSRs (r = ρR, ⟨r²⟩ ≈ R²) the census and the vector channel both go as **Q/R³**. The
R³ is the number of GPs in a PSR volume: the shell mean spreads the source over them. In a well (R → 0.9R on the same
lattice; AP-4's DI-bit count fixed):

```
source                                                      census u   vector V   (well / flat, any rho >> 1)
POINT  the charge's contribution at its own GP                1.372      1.372     = (1+κ)³  → k_α = −3
BAND   N DI-bits filling inward, N < GPs inside the PSR       1.372      1.372     = (1+κ)³  → k_α = −3
BALL   every GP inside the PSR holds one (N ≥ that count)     1.009      1.009     → k_α = 0 (lattice rounding)
```

k_α = −3 is excluded by Lange 2021 by ~10⁸. **The relay window is right, but LPI in the far field holds only if a
charge injects in proportion to the GPs in its PSR volume.** Under R-DIBIT-INWARD-FILL that happens in one case: the
family fills the whole PSR ball solid, down to the charge's own GP, in flat space and in a well. Exclusion then caps the
landed count at the ball's GP count, which scales with the PSR volume, and the R³ cancels. A band with an empty core
(N smaller than the ball) injects a fixed count, and fails.

The near field agrees: 4327's occupancy problem also disappears when the ball is full (fill 1 everywhere inside the PSR).

## 3. The question to the founder (physical picture)

When a charge's DI-bits land, do they fill its whole PSR sphere solid — every grid point from the PSR right down to
the charge itself — or only a band under the PSR with an emptier core? If the whole sphere, then in a gravitational
well, where the sphere holds fewer grid points, some of the charge's DI-bits find no free grid point at all: what happens
to those?

## 4. What changes elsewhere if the answer is "the whole sphere"

- N (a GP's DI-bits per Moment) must be at least the number of GPs inside a PSR, (4π/3)(R/a)³; GR-1j carries R/a as an
  open input, so this becomes a constraint linking the two.
- The excess (N minus the ball count, larger in a well) needs a rule; AP-5 D4 ("nothing discarded") suggests it is held
  or relayed, not lost. That rule must not feed back into Q, or the R³ returns.

## 5. PD-008

- **The convenient branch this refuses:** "the founder's answer plus AP-4 settles LPI." It settles the window and
  Gauss's law; the source count still decides α, and only the full ball passes.
- **Assumption stated:** α reads the relayed census/vector at the target at a fixed distance in PSRs (the arc's
  α = f·PSR/(2L), with f now the relayed value), and the swing L/PSR is invariant (4327, by ruling).
- **4354's "PSR cross-section → k_α = 0"** was for a count-conserving particle relay, not the registered shell mean;
  withdrawn (erratum on 4354).
- **For the critic:** (i) repeat §2 on the FCC and GLASS lattices of 4330; (ii) check the two-level dynamic relay leaves
  the static far field unchanged (GR-1j says statics is exempt); (iii) check whether GR-1j's registered source
  normalisation (∇²u = −(4πG/kc²)ρ) already implies an R-scaled injection for mass, and whether the same must hold for
  charge.

# One Cycle Cannot Be One Colour: the Founder Proposes a Perfectly Sinusoidal Single-Cycle Discharge, Not a Square Wave. 4448 Did Not Assume a Square Wave, and the Point Holds for the Smoothest Shapes: Any Pulse About One Cycle Long Spreads Over About Half Its Own Frequency or More (0.44 to 0.9, by Shape and by How Length Is Measured). One Frequency Needs Many Cycles; Hydrogen's Sharpness Needs Millions. His Moment-by-Moment Discharge Drive Is a Fine Mechanism for Delivering the Energy, but Something Must Meter It Out Over Millions of Swings

**Patch:** 4450. **Lane:** foundations, with QM and EM. **Session:** 242.
**Founder input:** `founders_voice/4450_sinusoidal_single_cycle_cascade.md` (answers 4449 §6).
**Script:** `series_standard_model/code/4450_smooth_one_cycle_spectrum.py`.
**Critic:** a fresh-context critic returned ACCEPT WITH CHANGES (verbatim in
`series_standard_model/reviews/2026-10-01_session_242_critic_returns_verbatim.md`). It confirmed the conclusion and the timing. It found that the
first draft:
- mislabelled a cosine with jumps as a sine cycle;
- used a Hann envelope only half a cycle wide;
- stated "more than half" against 4448's "a third to a half" without reconciling them;
- assumed a light-speed cascade without flagging it;
- called the Gaussian "the smoothest possible";
- had no todolist entry.

All six required changes are taken in, with the optional notes.

## 1. His answer

- **A mechanism:** the CP in an activated orbital is knocked out of resonance by a collision (with mass or a rogue wave). The DP arcs whose discharge
  it would have captured now discharge and drive it, each in the direction of its arc. The CP picks up the displacement and moves; the same happens the
  next Moment, until the reservoir is fully discharged.
- **On the single half-wave or full-wave cycle:** Claude appears to have assumed a square wave, whose Fourier components cover the whole spectrum. He
  proposed instead **a perfectly sinusoidal discharge containing only a single frequency.**
- It would be started by a single small discharge in the first perturbation of the collision, or by rogue-wave initiation of the CP "activating it to
  another stable resonant orbital". The perturbation's amount and direction trigger the cascade of DPs driving the discharge.
- **A cascade starting at one point in the DP Sea would spread, and the energy released would be precisely the difference between the two levels.**

## 2. The single sinusoidal cycle (script part 1)

**4448 did not assume a square wave.** It used the spread of a smooth, Gaussian-like pulse (1/π, and 0.44 for a Gaussian), as asserted numbers, without
computing a spectrum. A square wave would be broader still. His point deserves a direct answer, so here the spectra are computed for the smoothest
shapes about one cycle long:

| Pulse | Spread (width at half height of its power spectrum, as a fraction of its frequency) |
|---|---|
| one true sine cycle, starting and ending at zero | 0.90 (its peak shifts to 0.84 of the intended frequency) |
| one cosine cycle, with jumps at its ends | 0.81 |
| a smooth (Hann) envelope one cycle wide at half height | 0.72 |
| a Gaussian envelope, its amplitude one cycle wide at half height | 0.62 |
| a Gaussian envelope, its intensity one cycle wide at half height (4448's convention) | 0.44 |
| a Gaussian envelope 10 cycles wide | 0.062 |
| 100 cycles | 0.006 |
| measured Lyman-α | 0.00000004 |

The Gaussian is the pulse with the smallest product of length and spread. **This updates 4448's "a third to a half":** 0.44 is confirmed for its
convention, and the 1/π there was a rough estimate. A one-cycle pulse spreads over about half its own frequency or more, from 0.44 to 0.9 depending on
its shape and on how its length is measured. The spread falls only as the pulse lasts more cycles, roughly as (0.44 to 0.62) divided by the number of
cycles. His half-wave version is shorter still, so it spreads wider (4449).

**The reason is not the shape; it is the length.** A wave has a single frequency only if it goes on repeating. Any pulse that starts and stops within
about one cycle, however smooth, is made of a spread of frequencies about as wide as half the frequency itself. This holds for waves in general, the
same in radio, sound and light: a radio station whose signal lasted one cycle would be heard as a click across the whole dial. To be as sharp as
hydrogen's line, the light must keep oscillating at one rate for millions of cycles. "Sinusoidal" and "one frequency" both require the sinusoid to
continue.

**So his first picture is the one the measurements need** (4449): a steady swing, repeated millions of times, the energy coming out a little at a time.

## 3. His discharge drive, and its timing (script part 2)

**The drive is a fine picture of how the energy gets to the CP.** Knocked out of resonance, the CP is pushed each Moment by the DP arcs it would
otherwise have recaptured, until the reservoir is spent. The total released is ΔE, as he says. That is how the swing is powered.

**The timing is the issue.** He named no speed for the cascade. Assuming it spreads at the light speed (Claude's assumption), it would cross the atom's
radius (about 5 × 10⁻¹¹ m) in about 1.8 × 10⁻¹⁹ s, a two-thousandth of one cycle of Lyman-α light (a thousandth across the diameter). Yet the light keeps
coming for 1.6 ns, about 4 million cycles. The assumed speed barely matters: a single sweep across the atom lasting 1.6 ns would have to creep at about
3 cm/s. Any faster cascade empties the reservoir far too soon. So the reservoir cannot empty in one sweep. Something must meter it out: each swing draws
only about one part in four million of what is left (4449). That metering, and what fixes the swing's rate while it happens, is the open question.

**One clause to check.** His rogue-wave initiation "activating it to another stable resonant orbital" sounds like raising the CP (absorption), not
dropping it (emission). Claude reads it as the trigger for the drop; to be confirmed.

## 4. What stays open

- **What meters the discharge** over millions of swings, and what keeps every swing the same length (merges 4449 items a and b; the per-swing share
  1/(fτ) of what is left).
- **The cascade's speed** in his picture (Claude assumed light speed; the conclusion holds for any speed above a few cm/s).
- **His Moment-by-Moment discharge drive** in CPP terms: which DP arcs push the CP, and in which directions.
- **"Activating it to another stable resonant orbital":** absorption or the trigger for emission (pending his reading).
- **Carried:** 4449 items c, d, e.
- **Answered:** 4449's founder question, in part (the energy source: the discharging DP arcs driving the CP each Moment; the amount: ΔE).
- **Not adopted:** a single sinusoidal cycle as a single frequency. **Corrected:** that 4448 assumed a square wave. **Reconciled:** 4448's spread
  numbers against this patch's computed spectra.

## 5. Question to the founder (physical picture)

The atom keeps giving off hydrogen's ultraviolet light, at one steady rate, for about 4 million cycles over 1.6 billionths of a second. **How fast does
he picture the cascade spreading through the DP Sea? And what makes the reservoir release its energy so slowly, a little each swing, instead of all at
once, while keeping each swing the same length as the one before?**

## 6. Answer to his "What do you think?"

His discharge drive is a good picture of how the energy reaches the electron. Knocked out of resonance, it gets pushed each Moment by the DP arcs it
would otherwise have taken back, and the total released is exactly the energy between the two levels.

On the single cycle, I didn't assume a square wave; I used a smooth pulse, and a square wave would be worse. But it's worth answering directly, so I
computed the smoothest one-cycle pulses there are, including a true sine cycle that starts and ends at zero. Every one of them contains a spread of
frequencies about half its own frequency or more. The problem isn't the shape; it's the length. A wave has one frequency only if it keeps repeating. This
is true of all waves: a radio station that sent a single cycle would be heard as a click all across the dial. To be as sharp in colour as hydrogen's
line, the light has to keep swinging at one rate for millions of cycles. So the steady swing repeated millions of times, his first picture, is the one
the measurements need.

That brings up timing. If the cascade spread through the atom at anything like the speed of light, it would be over in a tiny fraction of one swing; to
last as long as the light does, a single sweep would have to crawl at about three centimetres a second. So something must be letting the energy out
slowly, a little each swing. My question is how fast he pictures the cascade spreading, and what meters the energy out while keeping every swing the
same length.

## 7. PD-008

- **Not softened:** a single sinusoidal cycle cannot be a single frequency; the measured line needs millions of cycles.
- **Corrected:** the reading that 4448 assumed a square wave. **Updated:** 4448's 1/π, superseded by computed spectra (0.44 to 0.9).
- **Assumption, marked:** the cascade at light speed (the conclusion holds for any speed above a few cm/s).
- **Not claimed:** novelty for the time–bandwidth relation.
- Nothing registered.

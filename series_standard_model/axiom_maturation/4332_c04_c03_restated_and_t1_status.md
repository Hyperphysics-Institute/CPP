# c04 v2.3 and c03 v2.2: Level 1 Restated Per the Founder's Rulings (ħ/2 per Half-Swing, Many Moments); T1 Status After His Answer

**Patch:** 4332. **Lane:** EW → foundations / QM-SR companions. **Session:** 241.
**Founder:** `founders_voice/4332_answer_swing_shortens_closer_to_electron.md` (verbatim).
**Clears:** TODO-4320-C04HALF (text). **Owes:** the founder's PDF recompiles of c04 and c03.

## 1. T1 status

The founder: *"the idea that the swing shortens as you get closer to the electron seems reasonable"*, but the rate
(PSR/(3π) per e-fold, equal screening per layer) is *"more quantitative than I could estimate."* So T1 stands where
4331 put it: **the direction agrees with the founder's picture; the logarithmic rate is a required law with no model
yet.** The DP-arc cloud model that would produce it stays queued (4331 (b)). No physical-picture question is pending
from him on it.

## 2. c04 → Version 2.3 (the text change the rulings required)

The founder's rulings: the Planck-level ZBW is a pass-through swing (4320); its half-swing carries ħ/2 (4320); its CPs
move at their V_i, so a half-swing spans many Moments (4325, which settled 4324's fork). c04 v2.2 still stated a
two-Moment cycle at ν_P = 1/(2t_P) with ħ = E_P t_P per half-cycle. Restated, every change marked "(Version 2.3)" in the
text:

- **Definition (Level 1):** the pass-through swing; CPs move by V_i each Moment, at most one PSR; the half-swing spans
  many Moments, its duration set by DP-arc build-up and release; **action per half-swing S₁/₂ = ħ/2** (the equation
  keeps its label). The old frequency and action statement is recorded as withdrawn.
- **The ratio:** ν_P/ν_C = m_P/(2m) (which needed ν_P = 1/(2t_P)) is replaced by the tick count **1/(ν_C t_P) = m_P/m**:
  one Compton radian spans m_P/m Absolute Moments (2.4 × 10²² for the electron, 1.3 × 10¹⁹ for the proton).
- **Proof of Proposition (mass):** its Planck-tick sentence restated with the tick count, E_cloud = ħ/(N_Planck t_P) =
  ħν_C. **The proposition and its proof are unchanged** (the 4320 §2 check: they never used ν_P).
- **Abstract, introduction (iii), table, remark (rest mass), consistency list, open problem (1), summary:** restated
  to match; the remark now says how many Planck half-swings a Compton wave organizes is open.
- Compiles cleanly (pdflatex, two passes, no undefined references).

## 3. c03 → Version 2.2

§ "The Scale of ħ and the ZBW Action" said every DP oscillates at 1/(2t_P), spending E_P per half-cycle, with total
action an integer multiple of ħ. Restated per the rulings (half-swing carries ħ/2 over many Moments; total action a
multiple of ħ/2), with the old sentence kept in place as the v2.1 reading. **Proposition prop:hbar is untouched**: it
states only the dimensional identity ħ = E_P·t_P, which holds by construction; a v2.2 scope note under it says its
"one tick … one quantum" reading is a statement of scale. A pre-existing LaTeX error (`\cdotV_i`
at l.487, which stopped the file compiling) is fixed as `\cdot V_i`; c03 now compiles cleanly.

## 4. What I think

This clears the one paper-level debt the session's rulings created. Both companions now say what the founder ruled and
keep the old statements visible as withdrawn readings, so a reader can follow the change. Nothing in either paper's
derivations moved. That was checked for c04 at 4320 §2, and for c03 the proposition is dimensional.

## 5. PD-008

- **Convenient branch, marked.** "No derivation moved" is exactly what one hopes for a text restatement; it rests on
  the 4320 §2 check (c04's proposition uses only the resonance radius) and on c03's proposition being an identity.
- **Done here (D-4) rather than deferred:** c03's proposition statement ("one tick of the universal clock corresponds
  to one elementary quantum of action") now carries a v2.2 scope note: it is a statement of scale; the physical carrier
  is the half-swing, ħ/2 over many ticks.
- **For the critic in the next window:** read the compiled c04 v2.3 and c03 v2.2 for any remaining sentence that still
  implies a two-Moment Planck cycle.

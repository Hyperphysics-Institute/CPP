# Independent Critic of the α Arc (4317–4332): the Algebra Holds; the LPI Pass Does Not — 4330 Had a Sign Bug

**Patch:** 4352. **Lane:** EW → foundations. **Session:** 241.
**Method:** the "For the critic in the next window" items of fragments 4317–4332 were given to a fresh context (an
independent critic with no stake in the arc), which re-derived, recomputed and re-ran the scripts. Its findings were then
checked here; the decisive one (§1) was confirmed by reading the code and the critic's outputs.
**Verify:** `series_standard_model/code/4352_fsat_outward_rule_fixed.py` (outputs in `…_fixed.out`).

## 1. 4330's "solid band" is an artefact (REFUTED)

`code/4330_fsat_lattice_robustness.py` line 44 selects outward steps with `g[cand] @ x > 0` — the *target position*
dotted with the current position. The founder's rule (and 4328/4329's code, and the 4011 note) is that the *step*
points outward, `(g[cand] − x) @ x > 0`. Near the current site almost every neighbour has positive dot product with x, so
the 4330 walk lets DI-bits step back inward. Walkers then pass through occupied sites until they find an empty one — an
internal-DLA process — and fill a solid ball whose size is set by N, not by the PSR: at N = 3000 the band was
[3.61, 7.75] for P = 7.2, 8, 10.8 and 12 alike. The "zero change in a well" of 4330 was built in.

With the rule as ruled (3 seeds each):

```
FCC   N=1500: fill 0.721 ± 0.009   well change +0.054 ± 0.029
FCC   N=3000: fill 0.780 ± 0.018   well change −0.004 ± 0.014
GLASS N=1500: fill 0.770 ± 0.036   well change −0.006 ± 0.004
GLASS N=3000: fill 0.802 ± 0.044   well change +0.012 ± 0.021
FCC   N=6000: fill 0.785           N=12000: fill 0.741
```

The fill does not approach 1. At high N the band sits beyond the PSR, placed by crowding (FCC N = 6000: [6.63, 11.00]
at P = 8), so a well that shrinks the PSR by 10% barely moves it — which does not test 4327's premise either way, and if
the Coulomb constant scales as the landing radius squared, a crowding-set radius brings back k_α ≠ 0.

**Consequence.** 4330's result and the erratum it appended to 4328/4329 are withdrawn. **Local position invariance via
occupancy is not established.** The swing half of the LPI argument (L scales with the PSR) holds by the founder's ruling —
a postulate, not a test.

## 2. Other items (verdicts)

| Item | Verdict |
|---|---|
| 4317 R-OUTWARD-FANOUT universal | confirmed; the ratio 2 is rule-independent |
| 4318 "content change" vs 4301's count α | unreconciled; moot since 4322 (pure count) |
| 4320 §2 line list | incomplete — c03 still carried four ZBW-frequency sentences; **fixed at this patch (c03 v2.3)** |
| 4322 §3 re-derivation; σ = s² | confirmed; σ = s² remains an assumption (no corpus cross-section definition) |
| 4323 PCD reading | confirmed (glossary), superseded by 4325 |
| 4324 §3 | confirmed, with a caveat: "the Moments cancel" follows from defining the per-Moment momentum as speed-independent (f₁ t_M); with ordinary ∫p dq it would depend on the speed profile |
| 4325 §2 | confirmed as an identity; **its wording "a prediction of the picture" is withdrawn** — L = PSR/(2α) restates α |
| 4326 k_α bound | **tighter bound exists:** Lange et al., PRL 126, 011102 (2021), Yb⁺ E3/E2 vs Cs: (c²/α)dα/dΦ = (14 ± 11)×10⁻⁹, ~50× tighter than Leefer 2013; additive counting is excluded by ~6×10⁷ |
| 4326 T1 sign | rests on an unstated assumption: that the stress raises the landing push by the same factor as it shortens the swing (with ħ/2 fixed, α = c f_push PSR t_M/ħ does not contain L otherwise) |
| 4328/4309 band re-run | not checkable on the icosahedral Z-module (sites never recur) |
| 4331 scheme | the comparison should use the physical (on-shell) running: 1/α(M_Z) ≈ 128.95, so the swing is 5.9% shorter at M_Z, L(M_Z) = 64.48 PSR (not 63.98). The coefficient PSR/(3π) per e-fold is scheme-independent; in position space the log starts near 0.24 λ̄_C, which weakens the "onset at c04's cloud diameter" alignment |
| 4332 c04/c03 | c04 v2.3 clean; c03 had four residual sentences — fixed (v2.3) |

## 3. An open problem the critic raised (plausible, not fully audited)

The Coulomb chain (4323) needs the flux beyond the landing band to be c·4πR²; saturation needs N well above the band's
site count. Beyond the band the flux then depends on N, and at atomic distances — where clocks measure α — occupancy is
far below 1 and scales as N/R², the unsaturated regime in which 4328 itself gave k_α = −2. Registered as
OPEN-ALPHA-FARFIELD-1 (TODO-4352-ALPHAFARFIELD).

## 4. What the arc now claims

- **α = PSR/(2L) with one calibrated swing (CAL-ZBW1-SWING)** — a fair, non-circular *relation*: L is ħ expressed in the
  charge's own action unit, calibrated to α. It is a re-expression, not a derivation.
- **LPI:** not passed. The swing part holds by postulate; the occupancy part is open (§1, §3).
- **Running:** a sign match resting on the equal-force assumption (§2); the logarithmic law is a requirement read off QED.

Headline: *α re-expressed as a calibrated swing; local position invariance and the running are constraints on the model,
not yet passed.*

## 5. PD-008

- **The convenient branch this refuses:** keeping "passes LPI" on the strength of 4330. The critic found the bug; I
  confirmed it in the code and in the critic's rerun outputs before accepting it.
- **Not re-run here:** the full grid (my own rerun timed out at 10 minutes); the recorded numbers are the critic's, from
  the same corrected rule, and are consistent across seeds and lattices.

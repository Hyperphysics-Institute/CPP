# The Flip Is One PSR: α = N/(8πR²), the Spacing Drops Out, and α Is Half the Fraction of Its PSR Sphere a GP's Volley Reaches Each Moment

**Patch:** 4322. **Lane:** EW → foundations. **Session:** 241.
**Founder:** `founders_voice/4322_ruling_flip_is_one_psr_zbw_tracks_the_line.md` (verbatim).
**Verify:** `series_standard_model/code/4322_psr_flip_alpha_is_sphere_fraction.py`.
**Answers:** 4320 §7. **Supersedes:** 4320 §3's working reading (one GP), §4's α = N/(8πR) and §5's "a line, not a
sphere" (erratum appended there).

## 1. The rulings

1. **The flip moves one PSR per Moment** (light speed), and *"the action increments are in terms of SSV_net (V_i)"*:
   ħ/2 is the action of a one-PSR displacement over one Moment.
2. **The oscillating ZBW DP tracks and affects the line of its transit:** *"There is no time for radiation in one
   Moment, only time for transit."* This is a statement about the ZBW's own footprint (the ~R GPs it crosses), and it
   stands as such (§5).

## 2. My question 2 was built on the reading he has now overruled

"α points to a line" (4320 §5) was computed with ħ/2 as a **one-GP** push (4320 §3, reading (i)). With the flip at one
PSR, the action quantum is R times larger, and the same counting points to the **sphere**. I put question 2 to him on
the wrong reading; his answer is about a different object (the ZBW's track), and it is correct as that (§5).

## 3. 4301 re-run with the ruling's action quantum (rows)

ħ/2 = f₁ · PSR · t_M (least force, one PSR of displacement, one Moment); c = PSR/t_M; Coulomb from counting as in 4301;
σ = s² (4301's stated assumption):

```
alpha under the three action quanta (sigma = s^2):
   4301  hbar   = one GP push over one Moment  : alpha = N/(4 pi R)
   4320  hbar/2 = one GP push over one Moment  : alpha = N/(8 pi R)
   4322  hbar/2 = one PSR flip over one Moment : alpha = N/(8 pi R^2)

4322: N/(4 pi R^2) = 2 alpha = 0.014595 = 1/68.518
   i.e. each Moment a GP's volley reaches one GP in 68.52 of the GPs on its PSR sphere
   R = 1e+30: N = 8 pi alpha R^2 = 1.834e+59 DI-bits per GP per Moment
   R = 1e+32: N = 8 pi alpha R^2 = 1.834e+63 DI-bits per GP per Moment
   The relation no longer contains R: alpha is a geometric fraction, the same for every GP spacing on file.
```

**α = ½ × (the fraction of the GPs on its PSR sphere that one GP's volley reaches in one Moment).** The unknown
spacing R has dropped out. This is the first form of the count relation that is **scale-free**: it no longer depends on
whether PSR/s is 10³⁰ or 10³².

## 4. The founder's covering picture is now within a factor 68.5 (rows)

```
The founder's covering condition (4303: one DI-bit per GP of the PSR sphere, N = 4 pi R^2):
   4301 form : alpha = R      -> 1e+30..1e+32  (x1e+32..x1e+34 too strong)
   4322 form : alpha = 1/2    -> x68.5 too strong  (the 10^32 tension of 4301/4303 becomes 1/(2 alpha) = 68.5)

Equivalently, a volley that covers, one GP deep, the sphere of radius r_cov (4304's surface reading):
   N = 4 pi r_cov^2/s^2 -> alpha = r_cov^2/(2 PSR^2) -> r_cov = sqrt(2 alpha) PSR = 0.1208 PSR (scale-free)
   (4304/4310 under the GP quantum: PSR_min = sqrt(alpha s PSR) = 8.5e-17 PSR at R = 1e30 -- the 1e16 tension)
```

The two tensions that ran through 4301–4311 both came from the one-GP action quantum:

- **4301/4303's 10³²:** "one DI-bit on every GP of the PSR sphere" made charge 10³²–10³⁴ too strong. Under the
  ruling, full covering gives α = ½, **68.5 times too strong.** The founder's covering picture is now in range.
- **4304/4310's 10¹⁶:** his 4304 reading (the volley covers a one-GP-deep surface at the smallest, black-hole PSR)
  gave a smallest PSR of 10⁻¹⁶ l_P, against the register floor l_P/2. Under the ruling it gives **r_cov = √(2α)
  PSR = 0.121 l_P, 4.1 times below the floor l_P/2**, with no dependence on R. 4311 dropped the surface-count
  identification because of the 10¹⁶; that reason no longer holds (§7).

## 5. The ZBW's track (his answer 2)

```
   R = 1e+30: the flip transits 1e+30 GPs (one PSR); a static charge sits on 1 GP
   The track is the ZBW's footprint; the volley N is every GP's emission (AP-4). They are different objects.
```

His picture — the flip has time only for transit, and it affects the line it crosses — is consistent with everything
above. The line is the ZBW's footprint, R GPs long. The volley N is what every GP emits (AP-4) and, by §3, it is a
surface-scale count. These two do not compete.

## 6. Where the 68.5 must live (pressed to the end)

The sharing rule cannot supply the 68.5 by itself. Under R-OUTWARD-FANOUT and 4309's sharing, DI-bits spread over the
GPs of a shell and land on distinct GPs while N < 4πR², so the covering fraction *is* N/(4πR²). A fan-out computation
would return the input. What AP-4 leaves open is **N itself**, and the founder's picture fixes it: every GP of the
sphere gets a DI-bit (4303), N = 4πR². Take that, and put the two per-landing factors of 4301 back in symbols —
σ (what a target intercepts, in units of s²) and p (the push per intercepted DI-bit, in GPs; 4299 says 1):

  **α = ½ · (N/4πR²) · (σ/s²) · p,**  and with full covering  **α = ½ · (σ/s²) · p.**

So on the founder's three pictures together (full covering, one-GP push, one-PSR flip for ħ/2), **2α = 1/68.5 is the
coupling efficiency of a single landing**: the fraction of a GP's worth of push that a charge actually takes from one
DI-bit landing on its GP. σ = s² and p = 1 were 4301's working assumptions, never derived. The derivation of α is now
the derivation of that one efficiency, and it no longer involves R, the covering, or gravity.

**Corpus search (D-1), done here.** No registered CP interception cross-section or partial-push rule exists. The
nearest object is the transport family's σ (`series_phenomena/cosmology/dark_matter/transport_family_unification.md`
§2, Patch 2890): *"the probability that a DI-bit is absorbed and re-emitted isotropically rather than continuing in
its direction"*, a free parameter of that family (0 to 1). **D-7: it is a per-hop scattering probability at any GP,
not the uptake of a landing DI-bit's push by a charged CP**, so it is not the same symbol. It is recorded as the
closest candidate mechanism for the landing efficiency, not identified with it.

## 7. What I think

This is the strongest step in the arc. With the flip at one PSR, **α stops depending on the unknown lattice spacing.**
The founder's covering picture, which failed by 10³² when the action quantum was a GP push, now fails by 68.5, and
his black-hole reading lands 4.1× below the register floor instead of 10¹⁶. Pressed to the end, the 68.5 cannot come
from the fan-out geometry (that returns its input); it has to be **what fraction of one landing a charge absorbs** —
a CP-level question (how a CP on its GP takes up a DI-bit's push), not a lattice-count question. Nothing is derived
yet.

## 7a. Founder question (a physical picture)

**When one DI-bit lands on the GP where a charged CP sits, does the CP take the whole push (moved one GP), or only part
of it?** On your pictures (every GP of the sphere reached, one-PSR flip for ħ/2), the measured α needs the CP to take
about 1/68.5 of a full push per landing (equivalently, about one landing in 68.5 acts on it). A full push would make
charge 68.5 times too strong. What in your picture of a CP receiving a DI-bit would give that fraction?

## 8. PD-008

- **My error, stated.** 4320 §5's "a line, not a sphere" was computed on the one-GP reading and was put to the founder
  as if it were the result; his answer 1 overturns it. Corrected here.
- **Convenient branch, marked.** "R drops out" is exactly what one wants from a derivation of α. It follows from the
  ruling and 4301's counting with σ = s²; if σ scales with R (a PSR-scale cross-section), R returns. D-7 check owed on
  σ against the corpus.
- **Convenient branch, marked, not taken.** r_cov = 0.121 PSR sits near the old 10% shell thickness (0.096, F-E2-3).
  That shell was closed as a toy hop count (4307–4308); no connection is claimed. Likewise 68.5 is not matched to any
  600-cell number.
- **Convenient branch, marked, not taken.** "4.1 below the floor" is not claimed as agreement: the floor's attainment
  is an assumption (4311), and 4.1 is a miss if the floor holds.
- **Solid:** α = N σ/(8π PSR²) from 4301's counting with the ruling's action quantum; the ratios in §3–§4.
- **Checked here (D-4): f₁ vs R f₁.** 4299 says one DI-bit moves a CP one GP, and 4301 makes one such push the work
  f₁·s. A one-PSR flip is R pushes, so its work is R·f₁·s = f₁·PSR, which is what §3 uses. Writing R f₁ as the *force*
  over the whole PSR would count each push twice (R f₁·PSR = R² f₁ s); that reading is rejected.
- **For the critic in the next window:** (i) re-derive §3 from 4301 independently; (ii) the σ = s² check against any
  corpus definition of a GP's interception cross-section (D-7); (iii) whether 4311's drop of the surface-count
  identification should be reversed now that it misses by 4.1 rather than 10¹⁶.

**Erratum (Patch 4323):** the result is restated in the founder's variable: **α = c/2**, c = DI-bits landing on one GP per Moment in the landing zone at the PSR (one GP in 68.5). "R drops out" holds for α, not for N: with a landing band of finite depth (4309's 2%), N = c × (band GPs) carries R. §6's "coupling efficiency of one landing" is the same statement with a whole push per landing read as occupancy. See `series_standard_model/axiom_maturation/4323_alpha_is_half_the_landing_concentration.md`.

**Erratum (Patch 4325):** the one-PSR flip in one Moment is superseded by the founder's 4325 ruling (the CP moves at V_i every Moment at the Planck level too). ħ/2 is the action of the half-cycle swing, and α = c·PSR/(2L) (4324). See `series_standard_model/axiom_maturation/4325_alpha_fixes_the_zbw_swing_not_its_duration.md`.

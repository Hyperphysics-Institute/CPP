# The 10% Shell Computation Is Valid as a Model, and Its 10% Holds Only if a PSR Is About Seven to Fourteen Hops Long; at One GP per Hop It Gives 10⁻¹²

**Patch:** 4307. **Lane:** EW → foundations. **Session:** 240.
**Founder:** `founders_voice/4307_instruction_reexamine_the_10pct_shell_computation.md`.
**Examined:** E-2 (Patch 2959, finding F-E2-3, σ_r/⟨r⟩ ≈ 0.096); pass 3 (3135, `3133_subpsr_cascade.py`); pass 4 (icosahedral);
4012 ("derived, not an estimate"); 4305 (extension to N = 72).

## 1. The computation's premises

1. Every DI-bit travels a fixed total number of hops, N, the PSR expressed in lattice steps. (The founder's "GP paths that
   add up to the PSR".)
2. At each hop, a site's DI-bits split equally among its neighbours with an outward radial component (R-OUTWARD-FANOUT).
3. A DI-bit's landing radius is the Euclidean distance it has reached after those N hops.

The band thickness σ_r/⟨r⟩ is then a pure function of N and the lattice. **Premises 1–3 are sound and match the founder's
stated mechanism (path-length variation).** The reasoning from them to the number is correct: 4305 reproduced pass 3 to
the last digit, and pass 4 agrees on the icosahedral lattice.

## 2. What the computation actually says

```
   N     FCC (pass 3 / 4305)    icosahedral (pass 4)
   6        0.0934                 0.0891
  10        0.0905                 0.0899
  14        0.0853                 0.0854
  22        0.0760                 0.0752
  40        0.0621                 0.0595
  72        0.0489                    —
  decline ~ N^-0.38 (FCC), ~ N^-0.3 (icosa); no plateau
```

**The 10% is the value at N ≈ 6–14.** E-2's toy used 7 hops; pass 3 read 6–22; pass 4 wrote that "N ≈ 6–14 sits at the
~9–10% plateau; N ≈ 80 would imply ~5%" and handed the choice of N back. Nothing in the three computations fixes N.

## 3. Where the premises meet the registered lattice

The corpus registers about 10³⁰ GPs per PSR (GR-FE-1; EU: 10³²), and the founder's transport rule has a DI-bit moving
one GP at a time. If a hop is one GP, then N ≈ 10³⁰, and the same computation gives a band of about **10⁻¹² of a PSR**
(4305's extrapolation). So:

- **The computation is valid. Its 10% output is valid only if the PSR is about seven to fourteen hops long.**
- On the registered GP count, with one GP per hop, the 10% shell does not follow; a band a trillionth of a PSR thick does.
- 4012's "derived, not an estimate" was true of the *procedure* and silent about N. The number was derived at a toy N.

## 4. What could make N ≈ 7–14 physical

The founder's 4306 ruling says the sub-Moment sharing count is not a calculated quantity. But the band's thickness *is*
a function of it, so one of the following must hold:

- **The hop is coarser than a GP.** The GP lattice is a nested hierarchy of 600-cells (founders_vision §2; the 4009
  extended-lattice ruling; 4012 noted a single 600-cell's fan-out diameter is 5 hops). If sharing happens at the level of
  cells rather than GPs, and a PSR spans about ten cells at the relevant level, the 10% band follows with N a geometric
  fact about the hierarchy, which is positional, as he requires.
- **The band is not 10%.** If sharing is per GP, the band is ~10⁻¹² and the founder's estimate, E-2 and passes 3–4 were
  all reading a toy scale.

I cannot decide between these from the corpus. The first would turn "about ten hops per PSR" from a dial into a
structural number, and it is the only reading on which the 10% survives.

## 5. Verdict, as asked

**Still valid as a computation; not valid as a derivation of 10% unless the PSR is about ten sharing-hops long.** The
corpus should not call F-E2-3 "derived" without that condition. Scope notes are added to 4012's reasoning file and the
pass-4 record (pass 3's was added at 4306).

## 6. Founder question (a physical picture)

**In the nested 600-cell hierarchy, at which level does a DI-bit's outward sharing happen, and how many of those units
lie along one PSR?** If the answer is about ten, your 10% band is a geometric fact of the hierarchy. If sharing is at
every GP, the band is a trillionth of a PSR.

## 7. PD-008

- **Convenient branch refused.** It would be easy to keep "10% derived" on file; it is conditional and now says so.
- **What is solid.** Premises 1–3 and the N-dependence; the two lattices agree; the registered GP count with one GP per
  hop gives 10⁻¹².

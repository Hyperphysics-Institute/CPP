# Teukolsky Leg 1 — the eikonal Carter constant's error, finally computed: the dissent seat was right, and the correction cuts against us

**Patch 3353, 30 Aug 2026 — Session 157.** Verify:
`code/3353_teukolsky_angular_verify.py`, **9/9 PASS** (all-FAST).
Charter: the full-Teukolsky item, taken by its separable angular half.

---

## §1 Why the angular sector first

Every result in this lane since Patch 3334 rests on the eikonal Carter
constant **Q_eik = (ℓ+½)² − m²**: the census, ℓ_crit, the excitation
budget, and the disjointness theorem. GPT objected to it twice —
CONV-034 ("an eikonal correspondence applied at ℓ = 2") and CONV-035
("materially more credible at ℓ ≳ 7 than at ℓ = 2"). **Nobody had ever
computed the error.** Matching the radial equations term by term
identifies the exact quantity as **Q_exact = A_{ℓm}(aω) − m²**, so the
approximation is precisely the claim A ≈ (ℓ+½)².

## §2 The error, quantified at the modes the lane actually uses

| mode | aω | **A_exact** | A_eik | rel. error | used by |
|---|---|---|---|---|---|
| (2,−2) | 0.2757 | 5.9891 | 6.2500 | **+4.36%** | census, 3334 |
| (2,+2) | 0.4366 | 5.9727 | 6.2500 | **+4.64%** | burial, 3333 |
| (3,−3) | 0.3809 | 11.9839 | 12.2500 | +2.22% | census, 3334 |
| (7,−7) | 0.7855 | 55.9636 | 56.2500 | **+0.51%** | ℓ_crit, 3339/3349 |
| (9,−9) | 0.9395 | 89.9579 | 90.2500 | +0.32% | discharge, 3349 |
| (12,−12) | 1.1529 | 155.9507 | 156.2500 | +0.19% | domain edge, 3339 |

**GPT was right in direction and the size is now on the record:**
worst low-ℓ error **+4.6%** against worst high-ℓ error **+0.5%** — a
factor of nine. The unquantified caveat the panel kept flagging is now
a number.

The correspondence also degrades monotonically with aω — (2,−2) runs
+4.2% at aω = 0 to +10.3% at aω = 1.5 — so the error is largest
exactly where this lane works, at high spin and high frequency.
Recorded rather than hoped.

## §3 The direction cuts against us, and that is why it is stated first

Q enters the radial function with a **minus** sign:
R = K² − Δ[(m−aω)² + Q]. The eikonal value **overshoots**, so the exact
Q is *smaller*, so R is *larger*, so the phase volume Φ is *larger* —
**trapping is slightly easier than the eikonal census assumed, and
ℓ_crit could move DOWN rather than up.**

That is the unfavourable direction. It does not overturn anything yet
(a +0.5% shift in A at ℓ = 7 is far below the ±1 already carried on
ℓ_crit), but it is the direction a reader should be told about without
having to derive it.

## §4 What survives untouched, and why

**The 3352 disjointness theorem is completely unaffected.** Its Step 3
used only **Q > 0**, never Q's value. Exact Q remains positive at every
sampled mode (minimum 1.97), so the stability result is insensitive to
this correction *by construction* — an accidental robustness worth
naming, since the theorem is now the lane's strongest claim.

## §5 What the failures taught, kept in the code

The self-validation check failed **three times** before passing, and
each failure was informative rather than fatal:

1. **m = 0 is wrong** — the discretisation imposes S = 0 at the poles,
   correct for m ≠ 0 and wrong for m = 0 (Legendre solutions satisfy
   P_ℓ(±1) = ±1). Fenced, with its reason; no reported mode has m = 0.
2. **Intermediate |m| < ℓ degrades** — the pole behaviour
   (1−x²)^{|m|/2} vanishes weakly there and a uniform grid resolves it
   poorly (error 1.8e−1 at ℓ = 5, 8). Fenced; no reported mode is one.
   A graded mesh or the (1−x²)^{|m|/2} substitution recovers it, and
   belongs with the s = −2 build.
3. **The tolerance was the wrong metric** — an absolute bar silently
   tightens as eigenvalues scale like ℓ(ℓ+1). Replaced by a *relative*
   bar benchmarked against the smallest effect claimed: discretisation
   error is 1.6e−7, a factor **11,690** below the +0.19% at ℓ = 12, so
   the measurement is not reporting its own grid.

**|m| = ℓ — the sector every reported mode lives in — reproduces
ℓ(ℓ+1) to machine precision at every N from 800 to 6400.**

## §6 Fence, declared before results and asserted in code

This is the **scalar (s = 0)** angular sector. The gravitational case
is s = −2, whose eigenvalue differs. This patch therefore
**characterises the correspondence's error and its scaling**; it does
**not** deliver gravitational separation constants, and it does **not**
deliver Teukolsky line positions. The radial sector is untouched.

## §7 Registry impact

- **The eikonal-Q criticism (CONV-034 Q3(iii), CONV-035 Q1) is
  DISCHARGED in size**: +4.6% at ℓ = 2, +0.5% at ℓ = 7, +0.19% at
  ℓ = 12, degrading with aω.
- **OPEN-GR-RCORE-3 remaining, now sharper:** (i) the s = −2 angular
  sector; (ii) the **radial** Teukolsky integration with
  Sasaki–Nakamura stabilisation and complex root-finding — *the heavy
  item, and the one where a higher model tier earns its keep*;
  (iii) Zel'dovich growth-time bounds.
- **Queued, not enacted:** a census re-run with exact Q to see whether
  ℓ_crit moves. Cheap, and it should be done before any GR-2 amendment
  that quotes ℓ_crit more precisely than ±1.

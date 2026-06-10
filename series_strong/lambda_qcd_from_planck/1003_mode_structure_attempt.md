# Patch 1003 — 600-cell mode structure: a negative result, and where it leaves the arc

**Project C / SS-1 `op:lambda_psr`. Route B, first real attempt. Result: does not close. Honest cap + escalation.**

Patch 1002 sharpened Route B to one falsifiable question — derive `α_s(E_P) = 0.0197…` to
sub-percent precision from the 600-cell mode structure — and proved the bar: because
`dΛ/Λ = (N/α_UV) dα_UV` amplifies by ~2300×, only an *exact* closed form counts. This patch takes
the run at it. The outcome is a clean negative, and I am recording it as such.

## 1. The mode structure (exact, computed)

The 600-cell graph Laplacian spectrum is exact and golden-ratio-structured
(`code/600cell_spectrum.py`):

```
adjacency eigenvalues:   12,  6+6/φ,  4φ,  3,  0,  −2,  −4/φ,  −3,  −6/φ
Laplacian L = 12I − A:    0,  6φ⁻²,  12−4φ,  9,  12,  14,  12+4/φ,  15,  12+6/φ
spectral gap  λ₁ = 6φ⁻² = 2.29180
largest       λ_max = 12 + 6/φ = 15.70820
```

This is the genuine, parameter-free "mode structure" Route B was to draw on. It is real and clean —
the question is only whether any invariant of it *fixes the coupling* to the required precision.

## 2. Falsification-first scan (the test, not a fishing trip)

I enumerated a fixed, pre-declared set of natural candidate values for the bare coupling — spectral
invariants (`λ₁`, `λ_max`, their ratios), golden-ratio powers, `sea_strength`, and the
PSR-motivated `g₀ = 1/2` — interpreted each as `g₀²`, and recorded the resulting `Λ_QCD`
(`code/verify_routeB_modescan.py`). **No denominator was fitted to the target**; reverse-fitted
"exact" matches (e.g. `gap/116.1`, which trivially hits `α_UV` because 116.1 was chosen to make it)
are excluded by construction — they encode the answer and prove nothing, exactly the failure mode
the 1002 sensitivity theorem warned against.

**Result: nothing lands within 20% on Λ_QCD** (the loosest bar the sensitivity theorem permits, and
itself far weaker than the sub-percent precision a real "derivation" would demand). The candidates
miss by −83% to +224%.

## 3. The one positive residue: g₀ = 1/2

The closest *principled* candidate is `g₀ = 1/2` — interesting because PSR saturation is
`PSR_eff → l_P/2`, the same 1/2. Taken as the bare coupling it gives a genuine parameter-free
prediction:

```
g₀ = 1/2  ⇒  α_s(E_P) = 1/(16π) = 0.01989  ⇒  Λ_QCD ≈ 0.31 GeV   (+42% vs 0.218).
```

That is a real, zero-parameter, order-of-magnitude-**plus** result: the QCD scale from `l_P` alone,
landing within ~40% of the true value with no PDG input. It is *not* nothing — it is the strongest
positive evidence the arc has produced that the scale is Planck-related at all. But +42% on Λ fails
the sub-percent bar by two orders of magnitude, and — critically — **I have not derived `g₀ = 1/2`
from `PSR_eff = l_P/2`**; the shared "1/2" is at present a numerical echo, not a proof. Promoting it
would be precisely the coincidence-grade reasoning 1002 ruled out as a method.

## 4. Verdict

**Route B, by 600-cell-invariant matching, does not close `op:lambda_psr`.** No natural spectral
invariant supplies `α_s(E_P)` to the required precision. Combined with the 1002 sensitivity theorem,
this is a **strong negative lean** on the central claim "the DP/QCD scale is Planck-derived."

It is *not* the final falsifier. One family of mechanism (invariant-matching) has failed; what
remains live is a genuinely **derived** mode-sum → running mechanism — an actual computation of the
non-logarithmic running from the lattice mode density (a heat-kernel / spectral-zeta treatment of
the graph Laplacian feeding the vacuum polarization), which would *produce* `α_s(E_P)` rather than
*match* it. That calculation is not attempted here and is the sole remaining path to upgrade.

## 5. Recommendation (honest operating stance)

Until such a derived mechanism exists:

1. **Adopt the "calibrated, not Planck-derived" stance as the operating answer** for the absolute
   DP/QCD scale — i.e. TODO-016 Track 1's honest position is, on current evidence, the *terminal*
   answer, not a placeholder. The DP spectrum's clean content remains the **ratios** (color factor
   3, geometric mean) and the IR self-consistency (Patch 1001); the absolute anchor is calibrated.
2. **Keep `op:lambda_psr` open** with its scope narrowed to the single derived-mechanism question
   above, and record the `g₀ = 1/2 → 0.31 GeV` residue as the best positive lead.
3. **Do not** upgrade SS-1 or the DP-Sea appendix to "derived." The appendix correction stays
   exactly Track 1 (honest "calibrated").

## 6. Pending shared-registry action (STOP-and-warn — deferred, NOT in this patch)

Recording this negative lean belongs in the shared registries — `frontier_sectors/` (the
`op:lambda_psr` frontier line), `future_projects.md` (Project 2b status → "attempted, negative lean,
narrowed"), and `todolist.md` (TODO-016 Track 2). Those are integrator-only / cross-lane files under
the two-window protocol, so **they are not touched here** and are flagged to Thomas for a separate
batched INT patch. This patch stays entirely in-lane (`lambda_qcd_from_planck/`).

*(Verify: `code/600cell_spectrum.py` exit 0; `code/verify_routeB_modescan.py` exit 0 — negative
result confirmed. No THEO/PRED registered; SS-1 and DP-Sea appendix untouched.)*

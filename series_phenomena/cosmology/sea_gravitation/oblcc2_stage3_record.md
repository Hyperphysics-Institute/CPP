# OBL-CC-2 STAGE 3 (C-SUB) — EXECUTED: the instrument reading (q_imp = 1/4π, PASS), the calibration audit (TWO constants CORPUS-FIXED, the lattice type CORPUS-FORCED), and the honest stop: ONE named substrate input remains; assembly BLOCKED pending it; no demanded value computed

**Patch 3067 (11 Aug 2026). Executes plan §3. Verify:
`scripts/3067_stage3_measurement_calibration.py`. The anti-extraction
rule enforced to the letter: the one open input's data-demanded value
is NOT computed, NOT stated, and NOT hinted; the derivation stops
where the substrate stops.**

## §1 — M-q² (the frozen instrument protocol): PASS

Committed 2902 engine, static single source, small ideal Sea
(a = 2.5, jitter disabled-and-disclosed), receivers at r ∈ [5, 15]
on four directions: envelope A = amp·r² = **0.079575 ± 2×10⁻⁶ =
1/4π to five digits** — the committed field convention read through
the RUNNING instrument, not the source code. Per-arrival unit-charge
imprint amplitude q_imp = 1/4π (engine units).

## §2 — The calibration audit: what the shipped corpus fixes

- **(FIXED) a_phys = l_P.** SF-2 line 1299, shipped: "l_P is the
  Planck-scale 600-cell lattice spacing." The fundamental spacing is
  corpus-fixed at the Planck length.
- **(FORCED) lattice class = FCC (z = 12).** The corpus's own
  coordination — the twelve-neighbour hop (SF-8), the 12-shell
  (SM-1/SF-4) — is the kissing-number-12 class. At nearest-neighbour
  normalization (nn = l_P): **C₄ = 24.8225**. The 3066 cubic value
  is retired; the lattice-type "founder ruling input" of 3066 §3 is
  RESOLVED BY CORPUS (z = 12), no ruling needed.
- **(PICTURE-IMPLIED, one-line founder confirmation requested)
  δ = a = l_P.** The founder's registered picture (3059: CPs each on
  their own GP) implies a DP's two CPs occupy ADJACENT GPs — the
  pair separation IS the lattice spacing. The engine's D0/spacing =
  0.24 is a simulation convenience, not physics. CONFIRM: "a Sea
  DP's two CPs sit on neighbouring GPs (separation = one lattice
  step)" — yes or a corrected picture.
- **(OPEN — the one remaining input) α_q ≡ q²_phys/ħc**, the
  Sea-composition-weighted imprint constant: which DP species
  populate the vacuum Sea, with what charge content (eCP polar
  charge; qCP polar + k-weighted strong per AP-4a), in what
  proportions. The corpus fixes the CHANNEL STRUCTURE (AP-4a; the
  O-2 constant k) but the worker has not located a shipped
  composition + charge-normalization statement sufficient to
  assemble α_q. Named input: **CORPUS LOCATION OR FOUNDER RULING.**

## §3 — The assembled structure (complete except α_q)

With a = δ = l_P (pending §2 confirmation) and C₄(FCC, nn=1):

  **ρ_Λ = (g_d k₂/8π)·C₄·α_q·ħc/(l_P²R_h²) = (C₄α_q/2π)·ħc/(l_P²R_h²)**

i.e. the derived coefficient = **4C₄·α_q = 99.29·α_q** in units of
Step C's (1/8π)ρ_P(l_P/R_h)². Every symbol except α_q is now fixed:
g_d = 2 (exact), k₂ = 2 (exact), C₄ = 24.8225 (corpus-forced FCC),
1/8π (exact field energy), l_P (corpus), R_h (the 3064 arrival
domain). **Assembly and the curve freeze are BLOCKED pending α_q**
— and per the anti-extraction rule, the value of α_q that would land
in the observational band is deliberately not computed here or
anywhere until α_q is fixed forward. If the forward α_q lands
outside, F-CLI-1 FIRES; if the corpus cannot fix α_q, the arc's
grade honestly carries "one underived substrate constant" and the
panel is told.

## §4 — Founder questions (the physics lane; two items, one line each)

**FQ-1 (confirmation):** do a Sea DP's two CPs sit on neighbouring
GPs — pair separation = one lattice step = l_P? **FQ-2 (the
composition):** what populates the vacuum Sea — eDPs only, or eDPs
and qDPs, and in what proportion — and what is each CP's charge in
natural units (the corpus's e/2-class polar charge; the k-weighted
strong content per AP-4a)? FQ-2's answer, run through AP-4a's
register arithmetic, IS α_q; the worker executes that arithmetic
forward on receipt.

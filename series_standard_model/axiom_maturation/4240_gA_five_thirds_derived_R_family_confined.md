# g_A from the Cage, First Computation — the 5/3 Is Derivable; R Is Confined to One Family; One Picture Question

**Patch:** 4240. **Lane:** EW → strong (TODO-4234-DELTA). **Session:** 238.
**Founder (22 Sep):** *"go ahead with the g_A calculation"* (with ideas on 4236 §3, filed at `founders_voice/4240_*`).
**Verify:** `series_standard_model/code/4240_gA_five_thirds_and_the_reduction_family.py`.
**Target:** g_A = 1.2754 = (5/3) × R, R = 0.7652 (4234). Bar: SF-3's — m_e, the 600-cell, SU(3).

## 1. Searched first (D-1, D-3, D-10, unscoped)

- `g_A|axial charge|axial coupling`, `SU\(6\)`, `magnetic moment`, `lower.component`, quark motion in the cage.
- **Found, and it corrects 4234's sweep in one respect:** the tree *does* carry a "CPP" g_A — `series_strong/notebooks/
  mc_su3_algebra.py` hard-codes `g_A_cpp = 1.27` from `full_benchmark_table.ipynb`, and `development_strong_series.md`
  Stage 17 calls it *"CPP gives 1.27, which is correct"* while the same document's audit says the formula behind the
  table entry is not evident and the table's trivially-matched entries are PDG values. **It is an entry, not a
  computation.** 4234's statement that no axial-charge *computation* exists stands; both places are annotated in this
  patch so the 1.27 cannot be cited as a CPP result.
- The objects this computation needs, located (D-3): the proton cage is SS-2's tetrahedral cell — u at V₁ and V₂, d at
  V₃, V₄ open, u–u 1.071 fm, u–d 0.620 fm (4134 quotes it); the colour singlet is SS-1c Thm (colour neutrality),
  *"totally antisymmetric … over V₁, V₂, V₃"*; the ground state is L = 0 (4126, 4134); the quark's charge is smeared by
  *"its ZBW orbital motion around its cage vertex"* at r_ZBW = ħc/m_const (master glossary, SS-2).
- **Symbol resolved (D-7), with a correction:** m_const is **assigned** in SS-2 (line 183: *m_const = m_p/3 = 313 MeV*;
  the script, line 98: `m_const = 938.3 / 3`), not derived. 4238 wrote *"SS-2 derives m_const = 312.7 MeV"* and
  `SI-1_unknowns_and_forward_maps.md` M9 labels it DERIVED (SS-2). Both overstate it; the SI-1 label is corrected here,
  4238 stands as the record with this correction beside it. Nothing in 4238's comparison changes (it compared values).
- Spin-½ as a two-state object is OPEN-QM-3 (4128/4129: not derivable from the classical A_i). The EW arc 4223–4228
  already uses quantum singlets and triplets; this patch uses the same premise and says so.

## 2. Rows verbatim (D-11)

```
==============================================================================
PART A -- the 5/3 from exchange symmetry of the SS-2 cage
==============================================================================
J=1/2, Jz=+1/2 state symmetric under V1<->V2 (unique: eigenvalue count 1):
  Delta u = +1.3333 (4/3)   Delta d = -0.3333 (-1/3)   g_A(R=1) = Delta u - Delta d = 1.6667 (5/3)
  classical product u^ u^ d_ (4126's shorthand, NOT the state): Delta u - Delta d = 3.0
  the ANTIsymmetric J=1/2 state would give g_A = -1.0000 -- excluded by colour x Pauli

==============================================================================
PART B1 -- Dirac quark in a cavity: one spinor, g_A AND mu_p
==============================================================================
calibration, massless: x = 2.0428 (2.0428), R = 0.6530 (0.653), mu/R = 0.2023 = closed form 0.2023
m = m_p/3 = 312.76 MeV:
  R_c = 0.589 fm   g_A = 1.2384   mu_p = 0.956   w = 0.193
  R_c = 0.620 fm   g_A = 1.2455   mu_p = 0.997   w = 0.190
  R_c = 0.631 fm   g_A = 1.2479   mu_p = 1.011   w = 0.188
  R_c = 0.883 fm   g_A = 1.3011   mu_p = 1.310   w = 0.164
  R_c = 1.071 fm   g_A = 1.3365   mu_p = 1.500   w = 0.149
  R_c = 1.500 fm   g_A = 1.4040   mu_p = 1.847   w = 0.118
  g_A = 1.2754 requires R_c = 0.757 fm (w = 0.1761); there mu_p = 1.167 vs 2.793 (-58%)
  mu_p never reaches 2.793 for R_c < 3 fm: mu_p(3.0 fm) = 2.477, where g_A = 1.539
  -> FAMILY B1 EXCLUDED: the lower-component reduction that gives R shrinks the moment to the cavity scale.

==============================================================================
PART B2 -- spin-orbit sharing at the constituent scale
==============================================================================
R = 0.7652; moment factor (1+R)/2 = 0.8826
  mu_p = 3.000 x 0.8826 = 2.648 vs 2.793 (-5.2%);  mu_n = -2.000 x 0.8826 = -1.765 vs -1.913 (-7.7%)
  (4126 at R = 1: mu_p +7.4%, mu_n +4.5%.)  ratio mu_p/mu_n unchanged at -1.500.
  -> FAMILY B2 SURVIVES at the naive model's own precision; it neither confirms nor fixes R.

==============================================================================
PART C -- B2 read as a moving Dirac quark: R = 1 - (2/3)(1 - m/E)
==============================================================================
R = 0.7652 requires m/E = 0.6479, k = 367.7 MeV = 1.176 m_const, hbar c/k = 0.537 fm
  k = hbar c / l_unit  (Lambda = 335, SS-2)    =  335.0 MeV:  R = 0.7883  g_A = 1.3138 (+3.0%)
  k = hbar c / r_ZBW   (= m_const)             =  312.8 MeV:  R = 0.8047  g_A = 1.3412 (+5.2%)
  k = hbar c / (u-d 0.620 fm)                  =  318.3 MeV:  R = 0.8006  g_A = 1.3343 (+4.6%)
  k = hbar c / (u-u 1.071 fm)                  =  184.2 MeV:  R = 0.9077  g_A = 1.5129 (+18.6%)
  -> single-|k| estimates at the three ~0.6-fm corpus scales give g_A 1.31-1.34 (+3.0 to +5.2%); at the u-u scale 1.51.
     None is a derivation: R needs the momentum DISTRIBUTION of the quark's motion in the cage, not one scale.

==============================================================================
PART C2 -- the corpus statement of quark motion in the cage found by search (4240 s1): SS-2 ZBW smearing at r_ZBW
==============================================================================
  p = hbar/r_ZBW        (= m_const c)          k =  312.8 MeV:  R = 0.8047  g_A = 1.3412 (+5.2%)
  p = (hbar/2)/r_ZBW    (L = hbar/2 at r_ZBW)  k =  156.4 MeV:  R = 0.9296  g_A = 1.5494 (+21.5%)
  -> which row applies, and whether the smearing motion is the CORE's (so it can rotate the spin axis the vertex sees)
     or is the spin circulation itself (so it cannot rotate its own axis), is a picture question: TODO-4240-CORE-MOTION.
```

## 3. What is established

**(A) The 5/3 is derived from the cage, conditionally.** Colour antisymmetric over V₁–V₃ (SS-1c) and Fermi statistics
make the rest of the state symmetric; L = 0 makes the spatial part symmetric; so the spin state must be symmetric under
V₁ ↔ V₂, the exchange of the two u's that the SS-2 cage places at mirror-equivalent vertices. There is exactly **one**
J = ½ state with that symmetry, and it gives Δu = 4/3, Δd = −1/3, **Δu − Δd = 5/3.** No SU(6) group is used — only
the cage's exchange symmetry, the corpus's colour singlet, and angular-momentum addition. **Conditional on** quantum
spin-½ (OPEN-QM-3) and on quarks obeying Fermi statistics, neither derived in CPP. Side result: the product state
u↑u↑d↓, the shorthand 4126 and 4134 used in prose, would give 3, not 5/3 — 4126's *numbers* used the correct formula
(4μ_u − μ_d)/3; only the prose shorthand is loose. 4134's |W| was computed on the product assignment; whether R-F3-ISO's
bound shifts with the true state is filed (TODO-4240-F3STATE) — the conclusion there rested on ⟨n·W⟩ = 0 by isotropy,
which does not depend on the spin state, so only the rms 0.67 is affected.

**(B) R cannot come from a lower-component (cavity) reduction.** One Dirac spinor gives both g_A and μ_p. At the
corpus's m_const, g_A = 1.2754 needs a 0.757-fm cavity, where μ_p = 1.17 against 2.79 (−58%); μ_p stays below 2.79 for
every cavity under 3 fm. The mechanism that reduces the spin projection must keep the moment at the constituent scale,
which is what 4126 found it to be (3.00 at R = 1). **Family B1 excluded** — with the caveat that the MIT boundary is
imported, so the exclusion is of the cavity mechanism, not of any CPP statement.

**(C) R must be spin–orbit sharing at the constituent scale (family B2).** If each quark's j is split s = Rj,
l = (1 − R)j, g_A is reduced by R and the moment by (1 + R)/2 = 0.883: μ_p 2.648 (−5.2%), μ_n −1.765 (−7.7%), ratio
unchanged. That is inside the naive model's own ±7% (4126), so B2 survives without being confirmed. This is the
light-front constituent-quark result in the literature (the Melosh/Wigner rotation of a moving quark's spin), where
g_A ≈ 1.25 and μ_p ≈ 2.8 come out together; **cited as the known family, not derived here.**

**(D) What fixes R in B2 is the quark's motion in the cage.** Read as a moving Dirac quark, R = 0.765 needs
k = 368 MeV = 1.18 m_const. The three corpus scales near 0.6 fm give g_A = 1.31–1.34 (+3 to +5%); the u–u scale gives
1.51. The corpus statement of quark motion found (SS-2's ZBW smearing at r_ZBW) gives 1.341 if its momentum is
ħ/r_ZBW and 1.549 if it is (ħ/2)/r_ZBW. **None is a derivation**: a single |k| is not a distribution, and — the real
gap — if the SS-2 smearing motion *is* the spin circulation itself, it cannot rotate its own axis and supplies no R.

## 4. PD-008 — the convenient branch, marked

The convenient branch was to take k = Λ_QCD = ħc/l_unit (SS-2's own confinement scale) and report **g_A = 1.314, 3%
from measurement, from the cage** — one line, every input on file. I have not, because (i) one |k| is not the
momentum distribution R depends on; (ii) choosing among four corpus scales after seeing the answer is a fit, and the
four span 1.31–1.51; (iii) whether the corpus's quark motion can rotate the spin axis at all is exactly the unresolved
picture question. **Result as it stands:** 5/3 derived (conditional on OPEN-QM-3 and Fermi statistics); R's mechanism
confined to spin–orbit sharing at the constituent scale, cavity excluded by the moment; R's value not derived.
Submitted to the next window for critique: the exclusion in (B) and the (1 + R)/2 moment estimate in (C).

## 5. Handed up (PD-006(a), one picture)

**Inside the proton, does each quark's +qCP core itself travel — circling its cage vertex at about r_ZBW (the SS-2
"ZBW smearing"), or wandering within the cell — while its orbital eDP circulates about it? Or does the core sit on its
vertex, so that the circulation at r_ZBW is the orbital eDP's alone?** If the core travels, its motion tilts the spin
axis the W⁰ vertex sees and R follows from how fast and in what pattern it travels (TODO-4240-CORE-MOTION). If it sits,
R needs another carrier and B2's mechanism must be found elsewhere.

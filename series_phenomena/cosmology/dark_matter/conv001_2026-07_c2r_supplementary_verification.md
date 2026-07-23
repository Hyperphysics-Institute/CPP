# CONV-001 C2R SUPPLEMENTARY VERIFICATION DISPATCH (round 2) — pasted deterministic outputs of all three verify scripts (S4's itemized demands; S1 concurring); the executable verification package (RV-2714 precedent); the REPAIRED distinguishing-number challenge (location designated, value committed nowhere); the panel-requested Q5 alternative-reading sweep (every faithful-adjacent reading fires the 50% bound); and the concrete v2.7 draft text for the Q4 vote

**Patch 2777, 22 July 2026. Companion to the round-1 adjudication
(`conv001_2026-07_c2r_returns_adjudication.md`, 2776). Package:
`c2r_verification_package.zip` (scripts + README; distributed via
the founder). Conversion tiers: independent execution + challenge
value = VERIFIED-EXECUTED; review of the outputs below =
REVIEWED-OUTPUTS (converts votes, not the label).**

## §1 — Provenance (S4 item Q3.2)

Patch order, committed and pushed: 2769 (L1 prereg) → 2770 (L1
record + script) → 2772 (L2 prereg) → 2773 (L2 record + script) →
2774 (L3 record + script) → 2775 (L4 readout + packet). The L4
readout postdates all leg executions; every record quotes only its
own script's output. All scripts deterministic, no seeds; numpy +
scipy only.

## §2 — Exact output: `code/2770_c2r_l1_closure.py` (S4 items Q1.1, Q2.1)

```
a           = 0.3640220194 fm
kappa       = 5.494173 fm^-1   (kappa*a = 2)
n_FCC       = 29.317844 fm^-3
alpha_imposed = a/(pi sqrt2)   = 0.08193374 fm
alpha_derived = kappa^2/(4pin) = 0.08193374 fm
D1 = |alpha_derived/alpha_imposed - 1| = 0.000e+00
S_cont      = 1/alpha = 12.2050 fm^-1
S_disc      = 7.5761 fm^-1   (lattice sum, cutoff 12a; conv 6.0e-08)
S_cont/S_disc = 1.6110   (L4 record: 1.611)
core-medium fraction 1-3e^-2 = 0.5940   (L4 record's '59% self-exclusion')
S_core(r<a, continuum medium) = 7.2497 fm^-1
S_outer_cont(r>a)             = 4.9553 fm^-1
shell-discreteness excess over outer continuum = +52.9%
identity check: S_disc = S_outer_cont*(1+excess): 7.5761
D2: ell_LO = committed envelope at derived alpha = 0.0904 +/- 0.0028 fm (no re-run owed, D1 = 0)
```

The D1 line is exact algebra, not tolerance: κ²/(4πn) = (4/a²)·a³/(4π√2) = a/(π√2) identically.

## §3 — Exact output: `code/2773_c2r_l2_profile.py` (S4 items Q1.2, Q1.3, Q4.1)

```
frozen inputs: a=0.3640220194 fm  kappa=5.494173 /fm  alpha=0.08193374 fm
diagonal self-medium term alpha*kappa = 0.450158  (effective stiffness 1+alpha*kappa = 1.450158)

== A0-FCC-ball ==
  sanity A0-FCC-ball R=7: N=2093  min-chord=1.000000 a  interior z: min=12 mode=12 max=12  -> PASS
    R=7 staggering  baseline: flip=0.442 neg=0.535   corrected: flip=0.067 neg=0.922
    R=7 window 0.45-1.30: l_base=0.0885 (R2=0.877)  l_L2=0.1920 (R2=0.661)  delta=+116.90%
    R=7 window 0.55-1.60: l_base=0.0914 (R2=0.929)  l_L2=0.3164 (R2=0.591)  delta=+246.17%
    R=7 window 0.70-1.80: l_base=0.0928 (R2=0.950)  l_L2=0.3431 (R2=0.696)  delta=+269.70%
  sanity A0-FCC-ball R=9: N=4321  min-chord=1.000000 a  interior z: min=12 mode=12 max=12  -> PASS
    R=9 staggering  baseline: flip=0.442 neg=0.535   corrected: flip=0.067 neg=0.922
    R=9 window 0.45-1.30: l_base=0.0885 (R2=0.877)  l_L2=0.1920 (R2=0.661)  delta=+116.90%
    R=9 window 0.55-1.60: l_base=0.0914 (R2=0.929)  l_L2=0.3164 (R2=0.591)  delta=+246.16%
    R=9 window 0.70-1.80: l_base=0.0928 (R2=0.950)  l_L2=0.3431 (R2=0.696)  delta=+269.69%

    deliverable (i): chi(r) on nn axis, sites q_A=-5.880e-02 q_B=-5.880e-02 (opposite-sign adjacent pair: False)
      t      chi_A        chi_B        chi_net
      0.05  -7.0218e+00  -6.1090e-02  -7.3895e+00
      0.15  -1.9163e+00  -8.3393e-02  -2.3114e+00
      0.25  -9.4138e-01  -1.1544e-01  -1.3732e+00
      0.35  -5.5052e-01  -1.6269e-01  -1.0333e+00
      0.45  -3.5057e-01  -2.3484e-01  -9.0748e-01
      0.55  -2.3484e-01  -3.5057e-01  -9.0748e-01
      0.65  -1.6269e-01  -5.5052e-01  -1.0333e+00
      0.75  -1.1544e-01  -9.4138e-01  -1.3732e+00
      0.85  -8.3393e-02  -1.9163e+00  -2.3114e+00
      0.95  -6.1090e-02  -7.0218e+00  -7.3895e+00
  A0-FCC-ball: delta-ell/ell = +210.92% +/- 67.17% (6 variants)

== A1-HCP-ball ==
  sanity A1-HCP-ball R=7: N=2037  min-chord=1.000000 a  interior z: min=12 mode=12 max=12  -> PASS
    R=7 staggering  baseline: flip=0.421 neg=0.480   corrected: flip=0.077 neg=0.902
    R=7 window 0.45-1.30: l_base=0.0914 (R2=0.947)  l_L2=0.1962 (R2=0.614)  delta=+114.57%
    R=7 window 0.55-1.60: l_base=0.0882 (R2=0.969)  l_L2=0.3121 (R2=0.572)  delta=+254.00%
    R=7 window 0.70-1.80: l_base=0.0880 (R2=0.971)  l_L2=0.3709 (R2=0.614)  delta=+321.43%
  sanity A1-HCP-ball R=9: N=4331  min-chord=1.000000 a  interior z: min=12 mode=12 max=12  -> PASS
    R=9 staggering  baseline: flip=0.421 neg=0.480   corrected: flip=0.077 neg=0.902
    R=9 window 0.45-1.30: l_base=0.0914 (R2=0.947)  l_L2=0.1962 (R2=0.614)  delta=+114.57%
    R=9 window 0.55-1.60: l_base=0.0882 (R2=0.969)  l_L2=0.3121 (R2=0.572)  delta=+254.00%
    R=9 window 0.70-1.80: l_base=0.0880 (R2=0.971)  l_L2=0.3709 (R2=0.614)  delta=+321.43%
  A1-HCP-ball: delta-ell/ell = +230.00% +/- 86.14% (6 variants)

== paired correction, all 12 variants ==
delta-ell/ell_LO = +220.46% +/- 77.83%
D3 = |delta| = 220.46%   vs   W = 3.1%   -> > W (feeds C2R-CORRECTED at L4)
ell_derived preview (L4 assembles): 0.0904*(1++2.2046) = 0.2897 fm (envelope +/-0.0028 carried at L4)

== analytic continuum cross-check (OBS-class, non-adjudicative) ==
corrected closure poles k^2 = kappa^2(-1 +/- i sqrt3)/2; k = 2.7471+4.7581i /fm
continuum decay length 1/Im(k) = 0.2102 fm ; oscillation wavelength 2pi/Re(k) = 2.2872 fm  (lattice readout above is the adjudicated object; this row is consonance only)
```

**Raw sample vector** (S4 Q4.1): the 12 paired per-variant deltas
are the twelve `delta=` lines above (A0: +116.90, +246.17,
+269.70, +116.90, +246.16, +269.69; A1: +114.57, +254.00, +321.43,
+114.57, +254.00, +321.43 — percent). No seed exists; the fit is
ordinary least squares on log(r·|f|) per frozen window; the quoted
±78% is the 1σ spread of the sample vector, not a fit covariance.
**Honesty-bound boolean** (S4 Q1.3): |mean(δ)| = 2.2046 > 0.50 →
True. Fired mechanically; committed at prereg 2772 before
execution.

## §4 — Exact output: `code/2774_c2r_l3_bracket.py` (S4 item Q2.2)

```
alpha=0.081934 fm  alpha'(site-matched, premise-rejected)=0.131995 fm
one-shot: A0 R=7 window [0.55,1.6]: ell(alpha') = 0.1679 fm (R2=0.554, neg-frac=0.554)
committed comparator (2688 L4 direct propagation): 0.1679 fm, R2~0.55
bracket registered OBS-class; no physics claim attaches (charter SS2 L3).
```

## §5 — Panel-requested Q5 alternative-reading sweep (S4 item Q5.2; labeled OBS-class scan, J2-rider precedent; `code/2777_c2r_q5_sweep.py`)

```
a=0.364022 fm  kappa=5.494173  alpha=0.081934  r_ws=0.201184 fm
baseline (point kernel): l=0.0914 fm  R2=0.929  neg=0.535

variant                                      diag   l (fm)     R2    neg      dl/l  >50%?
V0 committed cloud (diag=kappa)            5.4942   0.3164  0.591  0.922   +246.2%  FIRES
V1 no self-medium (diag=0)                 0.0000   0.2968  0.469  0.579   +224.7%  FIRES
V2 WS-averaged self-medium                 3.7587   0.3458  0.536  0.930   +278.4%  FIRES
V3 tighter cloud (2kappa shape)           10.9883   0.1850  1.000  0.000   +102.4%  FIRES

reading: if every faithful-adjacent regularization of the occupied
self-cell fires the bound, the non-convergence is a property of the
physics at kappa*a=2, not of the committed cloud reading. V1 (diag=0)
is NOT faithful (drops the occupied self-cell) and is included only
to isolate the diagonal's mechanical role.
```

S4's stated decision rule: "If the alternative minimal faithful
reading produces δℓ ≈ +220% (honesty bound still fires) → UPHOLD."
Every faithful-adjacent regularization fires (+102% to +278%);
even the non-faithful diagonal-off control fires. The
non-convergence is a property of the physics at κ·a = 2, not of
the committed Debye-cloud reading. (S4 Q5.3, the CORRECTED logic:
the threshold is the frozen charter §3 pair — CONFIRM requires
|δℓ/ℓ_LO| ≤ W = 0.031; CORRECTED requires the derivation to CLOSE,
which the prereg-committed 50% bound negates; both numbers frozen
at 2768/2772 before any value existed.)

## §6 — REPAIRED distinguishing-number challenge (for VERIFIED-EXECUTED claims, all seats)

Run `code/2777_c2r_challenge.py` from the package and report its
single printed value: the corrected-operator envelope length on
A0 (R = 7) in the challenge window [0.60, 1.50] fm — a
configuration printed by NO committed record, NO packet, and NO
output pasted above. The expected value is committed nowhere; the
worker re-runs at adjudication to authenticate. Also report one
self-chosen intermediate quantity of your run. Echoing any number
from this dispatch does not authenticate.

## §7 — v2.7 draft clause text (Q4 vote object; incorporates S5's quantification amendment)

> **Clause 8 (shape-axis disclosure, C2R).** The FG-OTHER proxy
> readout ℓ = 0.0904 ± 0.0028 fm (continuum-matched; leading order
> licensed by the 2767 occupancy ruling; α derived as the unique
> occupied-core closure, C2R-L1/2770) carries, beyond the
> strength-axis sensitivity bound (site-matched ℓ ≈ 0.168 fm,
> premise-rejected, C2R-L3/2774), a response-SHAPE sensitivity
> axis: distributing the per-site response over the leading-order
> occupied-core cloud moves the readout by δℓ/ℓ_LO = +220% ± 78%
> and removes the staggered mode (C2R-L2/2773; OBS-class;
> first-order non-convergent at κ·a = 2 — no corrected value
> ships). Shape sensitivity quantified via the frozen operator's
> response to the distributed charge cloud; strength bracket from
> the rejected site-normalization premise. Consumer sentences state
> that the value is conditional on the per-site response SHAPE,
> whose closure is registered as OPEN-DM-KINETIC-1's concrete
> question (C2R-L4/2775). The observation-grade cap and clause 7
> are unaffected by this clause.

## §8 — What converts what (recap)

S1/S4: execute the package (→ VERIFIED-EXECUTED, challenge value
required) or review §§2–5 (→ REVIEWED-OUTPUTS) and convert Q1–Q3,
Q5; vote Q4 on the §7 text. S3/S5: authenticate via §6 if claiming
execution; votes otherwise stand as reasoned-unverified. Adoption
motions re-run on the converted returns. Nothing is adopted, and
nothing revoked, until then.

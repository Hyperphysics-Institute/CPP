# Q_stiff — the contact eDP-polarizability calculation: a scoping / handoff specification

**Status:** SCOPING ONLY — no fabrication, no new number for the open quantity. This document poses the one
calculation that now decides the Cross-Rod dark-matter make-or-break, specifies it precisely, separates what is
**pinnable** from what genuinely needs the **substrate-thermodynamic / inter-CP-potential framework**, and lays
out the multi-session attack. It is the Q_stiff-analog of the 0887 edge-bond scoping doc, one level deeper.
**Lane:** SF-2 (electroweak) / FP root, cross-window with DM. **Author:** Opus (DM 08xx), 28 June 2026. No
registry IDs minted here; it points to the existing **OPEN-FP-SF-2-η** (`frontier_sectors/FP.md`,
`problem_histories/PH-OPEN-FP-SF-2-eta.md`). Diagnostic: `code/0897_qstiff_overlap_diagnostic.py`. **DM-1 stays
v1.0; no registry/SF/THEO/OPEN/founders edits.**

---

## 1. The calculation, in one line

Compute **Q_stiff ≡ α_pol(contact) / α_pol(free-cloud)** for the eDP composite — the factor by which the eDP's
electric polarizability is reduced at the coat hard-core contact (a ≈ 1 fm) relative to the free-cloud value
used in the London/dispersion estimate. From 0896, the entire Cross-Rod make-or-break has reduced to this single
number: **in-window (viable, discriminating) ⇔ Q_stiff ≲ 0.1; Q_stiff ~ 1 ⇒ E_ee ~ 40 MeV ⇒ falsification.**

## 2. Why this is the decider (the chain, from 0893→0896)

- 0893: E_ee via the coupling-ratio hierarchy ⇒ ~170 keV, in-window (construction 1) — but conditional.
- 0895: 4-model panel — not falsified, two criticisms folded; the decisive question is whether the soft-eDP
  London enhancement survives at contact; Route B is the resolver.
- 0896: reduced the make-or-break to one factor, E_ee = Q·E_ee,free with E_ee,free ≈ 41 MeV; Q = Q_damp·Q_stiff.
  **Q_damp ~ 0.5** (standard r-damping + repulsion, noble-gas anchored) buys only ~2× ⇒ ~20 MeV, still OUT. So
  in-window rests entirely on **Q_stiff ≲ 0.1** (a further ~10–120×). Q_stiff is the open quantity.

## 3. The pinnable first-cut (already banked — `code/0897`)

The one diagnostic that needs **no** framework, only pinned Compton sizes and the corpus contact radius:

| composite | Compton size ℏc/E | a/size at contact (a=1 fm) | regime |
|---|---|---|---|
| qDP | 0.75 fm | **1.34** | marginal-multipole; London "marginal at f=0.2" (0835) — estimate STANDS |
| eDP | 2.24 fm | **0.45** | **DEEP OVERLAP** — interpenetration to ~half its own size |

**Result (robust, direction-only):** the eDP **deeply overlaps** its neighbor at contact, where the free-cloud
induced-dipole picture is invalid and the polarizability is necessarily **quenched** (charges cannot freely
displace; Pauli/exchange dominate). So **Q_stiff < 1 is structurally forced for the eDP** — Review II's contact-
quench is now grounded in a regime diagnostic, not asserted. **Key asymmetry:** construction 2's
(E_qDP/E_eDP)⁶ = 729× enhancement assumes the *soft* eDP responds as a free cloud, but the eDP is precisely the
composite that deeply overlaps at contact — so the enhancement over-counts polarizability for the wrong
particle. This is the strongest principled statement available without the framework: **the quench direction is
real; only its magnitude is open.**

## 4. The underlying model and its pinnable inputs

The polarizability that enters the 0835 London depth is a **Drude/Lorentz oscillator**: α_pol = α_c·ℏc/(μ ω₀²),
ℏω₀ = E_DP, μ = m_DP/4 — i.e. a charge on a spring of frequency ω₀. Q_stiff is the reduction of this response
when the oscillator is driven into its **anharmonic/saturation regime** at deep overlap. Pinnable inputs (no
framework needed): E_eDP = 88 MeV (spring frequency), μ_e = 22 MeV, the unit charge, the contact a ≈ 1 fm, the
eDP Compton size 2.24 fm, the overlap ratio 0.45. **What is NOT pinnable from these alone:** the anharmonic
restoring law / exchange-repulsion shape that sets *how fast* α_pol falls once the induced displacement
approaches the composite size — i.e. the magnitude of Q_stiff.

## 5. The dependency chain (what's pinnable vs. framework)

```
Q_stiff  (in-window <=> <~0.1)
  |-- PINNABLE: overlap regime (a/size=0.45, deep)  -> Q_stiff<1 forced (direction)        [DONE, 0897]
  |-- PINNABLE: Drude free-cloud alpha_pol, sizes, contact a                                [pinned]
  +-- FRAMEWORK: anharmonic restoring law / exchange-overlap response of the eDP cage       [OPEN-FP-SF-2-eta]
        = how alpha_pol saturates as induced displacement -> composite size
        = the same inter-CP-potential / substrate-stiffness the SF-2 cage masses lack
        (FP.md: equilibrium/effective-T/ensemble/ergodicity/substrate-dynamics "undefined")
```
The magnitude of Q_stiff is the eDP-cage internal-stiffness response — **the OPEN-FP-SF-2-η root itself**,
now posed as one factor with a clean in-window threshold (≲0.1) instead of a vague "SSV charge-sum."

## 6. The multi-session attack plan (proposed order)

1. **Bracket Q_stiff from a saturating-Drude toy** (next session, Layer C/D, indicative-only): cap the induced
   dipole at p_max ~ e·(composite size) and compute the effective α_pol(contact)/α_pol(free) at a=1 fm. This
   uses only pinned inputs + a generic saturation cap; it gives a *first bracket* on Q_stiff and tests whether
   the ≲0.1 threshold is even reachable by saturation alone. **Risk:** the toy's saturation cap is generic, not
   CPP-derived — grade it indicative, do NOT promote a number from it.
2. **The eDP-cage stiffness from substrate geometry** (the real calc): derive the anharmonic restoring law of
   the eDP cage from the 600-cell constituent configuration — the actual inter-CP response. This is the
   OPEN-FP-SF-2-η deliverable; likely shares the substrate-thermodynamic closure path conjectured in FP.md.
3. **Cross-check against the qDP calibration:** the same machinery must reproduce the qDP's a/size=1.34
   marginal-multipole regime where 0835's f≈0.2 already works — a built-in consistency anchor.
4. **Feed Q_stiff back:** E_ee = Q_damp·Q_stiff·41 MeV ⇒ in-window or falsified; then (DM-lane) collapse
   N_dwarf → single σ/m curve, or retire the Cross-Rod candidate.

## 7. The falsifiable contract (pre-registered)

**If the eDP-cage stiffness calculation returns Q_stiff ≳ 0.1, the Cross-Rod candidate fails** (E_ee ≳ 2 MeV ⇒
too stiff to fragment at cluster velocities ⇒ velocity-independent ⇒ loses the discriminating trend). **Q_stiff
≲ 0.1 ⇒ in-window discriminating prediction.** The candidate has been built so this single SF-rooted factor can
kill it. The overlap diagnostic (§3) says the quench is real; whether it reaches ≲0.1 is the make-or-break.

## 8. Honest disposition

The make-or-break is no longer DM-local and no longer vague: it is the eDP-cage contact stiffness, = OPEN-FP-SF-
2-η, now sharply posed as one factor (Q_stiff) with a clean threshold (≲0.1) and a pinned direction (quench
forced by deep overlap). The DM lane can do nothing further without it. Recommended entry: step 1 (the saturating
-Drude bracket) as an indicative tractability probe, then step 2 (the real cage-stiffness derivation) as the
foundational arc. **No conditional in-window registration until Q_stiff is bracketed** (per 0896 — the favorable
reading is not the face-value lean).

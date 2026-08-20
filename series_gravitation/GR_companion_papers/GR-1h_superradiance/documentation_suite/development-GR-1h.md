# Development log — GR-1h (Superradiance and Boson Clouds)

**STATUS: reconstructed.** GR-1h predates the vignette convention; the
March 2026 authoring is thin because nothing was recorded at the time.

## March 2026 — the last of the batch

**Vignette 1 — a rate comparison instead of a scattering calculation.**
GR-1f had given the spinning source an azimuthal SSV broadcast, and its
angular frequency at the outer horizon is Ω₊ = ac/(r₊² + a²). From
there superradiance is almost immediate: a bosonic wave whose phase
velocity ω/m lags the rotating field gets dragged and amplified, so
ω < mΩ₊. The standard derivation scatters waves off the Kerr metric and
reaches the same condition. No new number, no discrepancy — the paper's
contribution is that the mechanism is visible.

**Vignette 2 — saying what a textbook number is.** The 29.3% maximum
extraction, (1 − 1/√2)Mc², is standard. What the paper adds is an
identification: that is the fraction of rest-mass energy held in the
azimuthal SSV at extremal spin, and the irreducible mass is what remains
once it has all been taken. Modest, and presented as modest.

**Vignette 3 — the observationally live end.** Ultralight bosons, if
they exist, form clouds that grow by superradiance and radiate
continuous gravitational waves at f_GW ≈ 2μc²/h — LIGO-band for
μ ~ 10⁻¹³–10⁻¹² eV around stellar-mass holes — while carving a depleted
Regge gap in the population's spin distribution. Both are real, testable
predictions. Both are also standard consequences of superradiance that
the ultralight-boson literature already pursues; CPP reproduces them
rather than owning them.

**Vignette 4 — the one genuinely distinguishing idea, left as a
question.** Open problem 2 asks whether the Planck core reflects
*bosonic* waves as GR-1d showed it reflects gravitational ones. If it
does, the cavity between barrier and core enhances the instability
beyond the GR prediction — a "Planck-core bomb." The paper registers it
as a question rather than claiming it, which is the right call and also
the reason the paper has no distinguishing signature to advertise.

## August 2026 — renamed, formatted, repaired

**Vignette 5 — an undefined macro.** The W-A2 pass (Patch 3274) found
`\EP`, the Planck energy, used throughout but never defined —
stash-verified as a pre-existing legacy defect, not introduced by the
formatting edits. Defined alongside `\mP`; 0 errors.

## Session 152, 20 Aug 2026 — the suite, and W-B closes

**Vignette 6 — no staleness, and a bottleneck instead.** All four open
problems are genuinely open, and **three of them turn on the same
uncomputed quantity: Planck-core reflectivity.** That is precisely what
GR-1d needs to convert its parameter-free echo delay into an amplitude.
Two papers, reached from different directions, stalled on one number
that sits behind `op:einstein`. Recorded as programme structure rather
than as two unrelated gaps: the strong-field interior is not one open
problem among many — it is the shared blocker for the arc's two most
observationally live results.

**Vignette 7 — the last row.** This suite completes OPEN-GR-PPP-1 W-B:
all eleven gravitational papers now carry documentation suites to the
SPIN-3 ten-file standard. Across the eleven, the pass produced one
in-paper correction (GR-1's ledger, Patch 3276), four staleness findings
recorded but not executed, two forward pointers on unexploited review
notes, and an arc-wide map of which claims have actually been reviewed —
which, for the eight legacy companions, is very nearly none of them.

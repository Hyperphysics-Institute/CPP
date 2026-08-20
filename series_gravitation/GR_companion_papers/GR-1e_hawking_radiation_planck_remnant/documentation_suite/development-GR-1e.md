# Development log — GR-1e (Hawking Radiation and the Planck Remnant)

**STATUS: reconstructed.** GR-1e predates the vignette convention; the
March 2026 authoring is thin because nothing was recorded at the time.

## March 2026 — an endpoint with a mechanism

**Vignette 1 — the charter from GR-1c.** GR-1c had established the
Planck core and noted, qualitatively, that evaporation should terminate
at a Planck-mass remnant, deferring the quantitative work as an open
problem. This paper took it up: not merely *that* evaporation stops, but
*why*, and *what holds up* what remains.

**Vignette 2 — the argument, and the alternative it rules out.** The
termination condition turned out to be geometric. The semiclassical
Hawking derivation requires N = r_S/l_P ≫ 1; at M ~ m_P, N → 2 and the
"horizon" is a boundary of width l_P separating two lattice cells from
three — no smooth near-horizon region, so the approximation is
undefined rather than inaccurate. The paper then does the thing that
makes the argument stick: it checks whether the *thermal* mechanism
fires first. It does not. At termination T_Haw = T_P/8π ≈ 0.040 T_P, 4%
of Planck. Geometry binds, with a factor of ~25 to spare.

**Vignette 3 — held up, not left over.** The remnant is claimed
mechanically stable at a self-sustaining fixed point: gravitational SSV
compression exactly balanced by CP Exclusion repulsion at
PSR_eff = l_P/2, requiring no external pressure. This is the strong form
of the claim — a specific object at a specific radius held by two
effects already in the theory — rather than the weak "the calculation
broke down, something remains."

**Vignette 4 — declining to solve the information paradox.** Remnant
scenarios are usually presented as paradox resolutions. This one
computes the remnant's capacity as order k_B, notes that this is far
below the original Bekenstein–Hawking entropy, and concludes that the
resolution must involve the entire radiation train rather than the
remnant. The unitarity question is deferred to a full quantum treatment
that has not been attempted.

## August 2026 — renamed, repaired, and a flag left standing

**Vignette 5 — a thorn in the macros.** The W-A2 pass (Patch 3274) found
that this paper's `\TH` macro collided with LaTeX's built-in thorn
character — a legacy compile defect predating the arc's reorganization,
stash-verified as pre-existing rather than introduced by the formatting
edits. Renamed `\THaw` at its definition and six use sites; 0 errors.

**Vignette 6 — the note that was addressed to this lane.** CONV-027
minted NOTE-GR-CSTAR-STRONGFIELD (census speed c_* → ~0.29c near the
exclusion radius) and flagged it explicitly for GR-1d/GR-1e; CONV-028
extended it. Neither has been folded in here.

## Session 152, 20 Aug 2026 — the suite

**Vignette 7 — the second consecutive paper with nothing stale.** Like
GR-1d, GR-1e's open problems are all still genuinely open: each requires
either a quantum-field treatment (the Bogoliubov calculation) or the
strong-field interior, and the field-equation programme reached neither.
The staleness pattern that hit GR-1b and GR-1c is confined to papers
whose open problems the arc actually went on to solve.

**Vignette 8 — a pointer, not a guess.** The c_* flag was recorded as a
forward pointer with the question stated honestly and left unanswered:
the geometric-breakdown criterion is about counting cells and may be
entirely untouched by a wave-speed change, while the force-balance
argument involves propagation and may not be. Working that out is
physics, and physics does not belong inside a documentation patch.

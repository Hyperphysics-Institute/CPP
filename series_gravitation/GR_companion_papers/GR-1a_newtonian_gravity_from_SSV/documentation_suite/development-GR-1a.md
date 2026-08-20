# Development log — GR-1a (Newtonian Gravity from SSV Shell Broadcast)

**STATUS: reconstructed.** GR-1a was written in March 2026, before the
development-vignette convention existed. The vignettes below are
reconstructed from git history, the paper itself, and the surviving
development notes; they are correspondingly thinner than a
contemporaneously-written log, and that thinness is the honest outcome
rather than a gap to pad.

## March 2026 — the classical-force sector closes

**Vignette 1 — a companion identified before it was written.** The
paper was scoped during the post-SR companion planning, where the
gravitational companion appeared on a list of topics flagged during the
special-relativity audit work (`../development/development_notes.md`).
The programme had already locked four companions — Absolute Moment,
Stiffness C, Born Rule, ZBW Mass — and gravity was the natural next
step, because two of those four supplied everything it needed: shell
broadcast from Stiffness C, and mass as stored polarization energy from
ZBW Mass.

**Vignette 2 — one asymmetry, written down.** The paper's substance is a
single observation: the eDP cloud's charges cancel while its ZBW
energies add, so mass-energy is a scalar source where charge is a signed
one. Universal attraction, unshieldability, G = ħc/m_P², the hierarchy
ratio, and the identity of inertial and gravitational mass all follow
without further postulates. Three commits over two days (V1 13 March;
V2 14 March, Grok; V3 14 March, Claude) brought it to the version that
still stands. What those revisions changed was not recorded, and this
log does not invent it.

**Vignette 3 — a boundary drawn in advance.** The paper's closing
section names what it cannot reach: the strong-field regime where the
PSR formula saturates, and dynamic spacetime where modified lattice
spacing feeds back on SSV propagation. Written as a promissory note, it
turned out to be an accurate map of the next ten papers — and, unstated
at the time, it also implied the arc's next necessary step, since a
scalar-only theory must miss the factor of two in light deflection.

## August 2026 — found, renamed, formatted, cross-checked

**Vignette 4 — the paper becomes GR-1a.** The arc's reorganization
(Patch 3230) moved eight companions into `series_gravitation/` and
re-identified c05 as GR-1a under the founder-approved layout. The
founder's PPP audit then found (Patch 3271) that the arc's formatting
was incomplete, and the W-A pass (Patch 3273) discovered this paper was
missing **both** its Plain Language Summary and its CP/GP Signature
subsection — one of only two companions missing more than the Signature
alone. Both were added; no technical content changed.

**Vignette 5 — the result gets a second derivation, five months
later.** The field-equation programme (Patches 3258–3262) derived the
general CPP field equation from the messenger census, and its exact
static sector produced k·Δ|SSV| = GM/rc² as the unique decaying
spherical vacuum solution — this paper's central relation, obtained
again from an entirely different starting point. GR-1a reached it by
shell-broadcast analogy in March; GR-1j reached it by census
conservation in August. Neither knew the other's route when it started.
That convergence is the strongest check this never-panel-reviewed paper
has, and it is worth more than a review round would have been.

## Session 152, 20 Aug 2026 — the suite

**Vignette 6 — documenting a paper with no review record.** The
`reviews-` file for this paper says, first sentence, that there is no
paper-level review basis. Writing a suite for early work invites
tidying — describing March's paper as though it had known where the arc
was going. It didn't. The version history is marked reconstructed, the
V1→V2→V3 content deltas are left blank because nobody wrote them down,
and the weakest step (the "by analogy" construction of Q_grav) is named
in the FAQ rather than smoothed over.

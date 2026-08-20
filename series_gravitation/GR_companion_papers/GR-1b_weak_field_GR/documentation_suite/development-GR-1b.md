# Development log — GR-1b (Weak-Field General Relativity)

**STATUS: reconstructed.** GR-1b predates the development-vignette
convention. The vignettes below are assembled from the paper, its
version block, and the August 2026 patches that touched it; the
authoring period is thin because nothing was recorded at the time.

## 2026 authoring — the second channel

**Vignette 1 — the observation that forced a structure.** GR-1a had
closed the classical-force sector with a scalar source, and a scalar
source has a hard ceiling: it bends starlight by 0.875″ against a
measured 1.75″. This paper's response was not to add a correction term
but to add a *component* — the DI-bit broadcast carries the net vector
**SSV**_net alongside the scalar |SSV|_abs, with the pair constructed
explicitly from the eDP cloud's polarization energy. |SSV|_abs sources
g_tt; **SSV**_net sources g_ij. In the weak field the two contributions
to deflection are equal, and the factor of two is recovered exactly.

**Vignette 2 — a conjecture named as one.** The paper defines the CPP
field equations as a self-consistency condition — the metric
reconstructed from the LSP summation must equal the metric governing LSP
propagation — and shows this is equivalent to the *linearised* Einstein
equations. It then stops, labelling the full nonlinear case a **strong
conjecture** requiring proof that the discrete lattice sum converges to
smooth Riemannian geometry. That refusal set the standard the arc was
later held to; when the field-equation programme ran in Session 150, it
had a bar to clear rather than a gap to fill.

**Vignette 3 — a claim withdrawn inside the paper.** At V3.3 (Patch
3204) the cosmological-constant item was labelled under OBL-CAL-LABEL:
candidate mechanism only, magnitude not derivable at current knowledge,
d_s^emp cosmology-calibrated and never predicted, and the earlier
bracketing language explicitly withdrawn at CONV-020. Mathematics
untouched. The withdrawal rides inside the paper that made the claim.

## August 2026 — renamed, formatted, and given its missing figures

**Vignette 4 — the figures that never existed.** The W-A formatting pass
added the CP/GP Signature subsection (Patch 3273). W-A2 then found
something sharper (Patch 3274): the paper cited three SVG figures that
had **never existed in the repository** — three captions had shipped
with no images behind them. Rather than delete the captions, three
figures were drawn *to* them: the four-component LSP channel map showing
the equal weak-field potentials, the lensing geometry with α = 4GM/c²b,
and the PSR-contraction curve with the exclusion radius. The .tex moved
from `svg` to `graphicx`, dropping an inkscape dependency.

## Session 152, 20 Aug 2026 — the suite, and a second staleness finding

**Vignette 5 — the Open Problems list has been overtaken.** Reading the
paper whole for the suite surfaced that two of its six open problems
were delivered by companions written since: item (2), the exact
Schwarzschild solution with a non-singular Planck-scale interior, is
GR-1c Theorem 1; item (3), the Kerr metric, is GR-1f (with GR-1g for
Kerr–Newman). Item (1) remains open as stated but is substantially
advanced by GR-1j; item (5) has been downgraded rather than advanced.

This is the second staleness finding in two sessions — GR-1's epistemic
ledger was the first — and the pattern is now explicit: **status
sections rot silently**, because no compile gate and no review round
checks whether last March's open problem is still open. The suite pass
is where a paper is read as a whole, which is why it is where staleness
surfaces.

**Vignette 6 — and the edit was NOT made.** The finding was recorded in
`phenomena-GR-1b.md` with a full status table and scoped to the founder
as a proposed W-D pass across the legacy companions. The distinction
being drawn: correcting a paper that contradicts *itself* is bookkeeping
and was executed unilaterally at Patch 3276; correcting a paper
overtaken by *later work* is a decision about how a legacy document
should read, and belongs to the founder.

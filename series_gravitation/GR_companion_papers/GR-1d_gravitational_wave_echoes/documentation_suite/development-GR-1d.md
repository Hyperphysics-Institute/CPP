# Development log — GR-1d (Gravitational-Wave Echoes from the Planck Core)

**STATUS: reconstructed.** GR-1d predates the vignette convention; the
March 2026 authoring is thin because nothing was recorded at the time.

## March 2026 — an observable from an occupancy rule

**Vignette 1 — the consequence chain.** GR-1c had registered "GW echoes
from the Planck core" as an open problem, noting only that a core at
r_S/2 acts as a reflective inner boundary and that the delay should go
like (r_S/c)·ln(r_S/l_P). This paper made that quantitative. The chain
worth noticing runs backwards a long way: the CP Exclusion Rule was
introduced for reasons unconnected to gravity; it produced a Planck core
in GR-1c; the core makes the interior reflective; reflectivity makes a
cavity; the cavity makes an observable. Four steps, none of which was
arranged with an echo in mind.

**Vignette 2 — where the calculation is GR's and where it is not.**
Because GR-1c's exterior is *exactly* Schwarzschild, the entire
tortoise-coordinate calculation runs on standard machinery — the
photon-sphere barrier at 3r_S/2 is GR's barrier, unmodified. CPP
contributes exactly one thing: an inner boundary at r₀ = r_S + l_P.
That division is what makes the result checkable by anyone who knows GR.

**Vignette 3 — a bet placed where the competitors hedge.** The paper's
comparison section is unusually forthright. Gravastars put the
reflective surface at r_S(1 + 10^−X); fuzzballs at the string length;
both parameters float, so both models survive a non-detection. CPP's
surface sits at r_S + l_P, and the delay reduces to
Δt(M) = (4GM/c³)·ln(2M/m_P) — determined by the remnant mass and the
fundamental constants alone. The paper advertises this as making CPP the
most tightly constrained echo model, which is the same thing as saying
it is the easiest to kill.

**Vignette 4 — half a prediction, labelled.** The delay is
parameter-free; the *amplitude* is not predicted at all, because
|R_core| = 1 is an assumption and the true reflectivity requires the
strong-field interior. No amplitude means no matched-filter template,
and no template means no search. All three are stated in the open
problems rather than glossed.

## August 2026 — renamed, formatted, and a flag left unexploited

**Vignette 5 — a note aimed at this paper, from a round it wasn't in.**
CONV-027 minted NOTE-GR-CSTAR-STRONGFIELD on the DeepSeek seat's
contribution: the emergent census speed drops to ~0.29c near the
exclusion radius, flagged explicitly for the GR-1d/GR-1e lane. CONV-028
extended it — a stress-dependent wave speed implies frequency-dependent
dispersion and birefringence of gravitational waves in strong fields.
Neither has been folded into this paper.

## Session 152, 20 Aug 2026 — the suite

**Vignette 6 — the paper that isn't stale.** After three consecutive
suite passes turning up overtaken open-problem sections (GR-1b, GR-1c,
and GR-1's ledger before them), this one has none: every item in GR-1d's
open problems is still genuinely open, because all four depend on the
strong-field *interior* and the field-equation programme deliberately
stopped at the exterior. That is a real difference and worth recording
as one — the staleness pattern is not universal, and papers whose open
problems sit behind `op:einstein` have simply not been overtaken.

**Vignette 7 — what was registered instead.** A forward pointer: the
c_* suppression near the exclusion radius sits in exactly the region the
echo cavity occupies, and would modify the tortoise-coordinate travel
time — and therefore the delay formula — if significant at the paper's
stated precision. Nobody has asked whether it is. That is a bounded,
well-posed question left for whoever next works this lane, recorded in
`reasoning-GR-1d.md` rather than acted on inside a documentation patch.

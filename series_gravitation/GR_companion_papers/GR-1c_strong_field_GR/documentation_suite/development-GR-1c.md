# Development log — GR-1c (Strong-Field GR and the Planck Core)

**STATUS: partially reconstructed.** The March 2026 authoring predates
the vignette convention and is thin. The August 2026 corrigendum is
documented in full, because it is the arc's reference case for handling
a defect in shipped work.

## March 2026 — the exact solution

**Vignette 1 — what happens if you don't expand.** The companion set had
Newton (zeroth and first order in the PSR response) and the weak field
(first order beyond). This paper's move was to keep the response whole.
Integrated over shells with GR-1a's exact source relation, it produced
the isotropic Schwarzschild metric with no approximation and no free
parameters — which meant the strong field was not a separate theory but
the same expression read at full strength.

**Vignette 2 — a singularity forbidden by an occupancy rule.** The CP
Exclusion Rule had been in the theory for unrelated reasons. Applied
here it bounds PSR_eff ≥ l_P/2, so the contraction stops and the metric
never reaches zero: a Planck-density core of radius r_S/2 replaces the
classical singularity, with a Planck-mass evaporation remnant and
ringdown echoes as consequences. Both were left qualitative and
registered as open problems — which is how GR-1d and GR-1e later got
their charters.

**Vignette 3 — a Proposition that outran its evidence.** The paper also
identified "the CPP equation that plays the role of Einstein's field
equations," a nonlinear wave equation for Δ|SSV| reducing to linearised
Einstein in the weak field. It shipped. Nothing checked it against the
paper's own exact solution, because at the time nothing existed that
could.

## August 2026 — the machinery convicts the paper

**Vignette 4 — the HALT fires against a published result.** The
field-equation charter (OPEN-GR-FE-1) included a §4 HALT rule: if the
new derivation's static reduction disagreed with GR-1c's published wave
equation, stop and register. At Patch 3258 it fired — and the defect was
in the *published* paper, not the new work. Symbolic Check 5 showed the
Proposition's compensator was O(a⁴) where GR-1c's own Theorem-1 solution
demands O(a³), with the O(a²) term cancelling identically, under every
reading of the stated formula. The rule was followed exactly: halt,
register as OPEN-GR-FE1-FTERM, leave the published paper untouched.

**Vignette 5 — written for the wrong potential.** The diagnosis (Patch
3259) was cleaner than the defect deserved. In the measured frame the
exact statement is the harmonicity of the *logarithmic lapse*
N = ln√(−g_tt/c²) = −2·artanh(kΔ|SSV|/2), and the true compensator is
O(u)·|∇v|² rather than O(u²)·□ln — a correct building block with one
power of u too many and an ln-vs-artanh resummation. No rescaling
repairs the published form. The same work produced the equivalence
identity: for generic v the two frames' equations differ by a pure
algebraic factor with no derivative terms, so the measured-frame
equation and the lattice census equation are one law in two variables.

**Vignette 6 — five seats, a ratification, and a preserved error.**
CONV-027 returned VERIFIED 5–0 on the mathematics, CORRECT-AND-SUFFICIENT
5–0 on the diagnosis, and APPROVE-EITHER 5–0 on the corrigendum, with
two seats independently executing the verify. The founder ratified, and
Patch 3262 enacted V2.2: Form A (boxed log-lapse harmonicity), Form B
(quasilinear with F_true), the equivalence identity displayed, and the
defective formula **preserved verbatim** in a Corrigendum Remark
carrying the whole discovery→repair→ratification chain. Solution-level
agreement had been exact throughout, so nothing downstream moved.

**Vignette 7 — the upgrade that wasn't taken.** With the Proposition
restated and proven equivalent to the ratified T-1, it would have been
easy to narrate `op:einstein` as closed. The enactment patch records the
opposite explicitly: no Einstein-equivalence claim smuggled; the problem
stands. Declining an upgrade during a repair, when attention is on the
repair, is the harder version of claim discipline.

## Session 152, 20 Aug 2026 — the suite, and a third staleness finding

**Vignette 8 — a retired geometry still on the page.** Reading the paper
whole surfaced that three of its five open problems have been delivered
or superseded — `op:kerr` by GR-1f, `op:echoes` by GR-1d, `op:hawking`
substantially by GR-1e. The sharp one is `op:24cell`, which asks for a
discrete-to-continuum proof "on the 600-cell lattice with 24-cell
Voronoi cells, requiring the eigenvalue spectrum established in Spin
III." Spin III now exists and supplies a spectrum — but on the **regular
dodecahedron**, because founder ruling A1 (Patch 3236) retired the
24-cell: the 600-cell's dual is the 120-cell. That item does not merely
list a solved problem as open; it states a superseded geometry as
current.

Recorded, not edited — the third finding under the same boundary held at
Patches 3283 and 3285: self-contradiction is bookkeeping, being overtaken
by later work is the founder's call.

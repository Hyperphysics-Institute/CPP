# FA-SEA-GREEN S1a — the one-Moment kernel formalized from A3′ and the founder's re-radiation picture: uniform PSR-shell average, signal-conserving, resolvent statics — GATE G1 PASS (first attempt): the lossless static superposition recovers the registered inverse-square in the SSV_net channel, with icosahedral symmetry protecting isotropy through fourth derivative order

**Patch 2668, 20 July 2026. Stage S1a of the FA-SEA-GREEN charter
(`fa_sea_green_charter.md`, FROZEN 2666). Blind guards in force: neither
FA-C3 candidate value appears in, is computed against, or is compared to
anything below; no gap parameter and no screening length enter this stage.
79.5% not in scope.**

## §1 — Registered inputs consumed (and nothing else)

- **A3′ (The Completed Broadcast, axiom-registry Tier 1):** at every
  Absolute Moment each GP broadcasts its LSP′ to its **PSR shell**,
  propagating at c = ℓ_P/t_P with **flat per-hop transport**, all channels
  obeying **the same icosahedral shell-sum**. The scalar channel Φ suffices
  for the kernel's structure; the vector channel V_i = SSV_net inherits the
  identical shell-sum per the axiom's "all channels" clause.
- **Glossary:** PSR = effective displacement per Absolute Moment; rest-frame
  PSR = ℓ_P. SSV_net = the vector sum of all SSV contributions at a point.
- **Founder kernel capture (verbatim, `founders_voice/
  kernel_psr_reradiation_2026-07-20.md`):** per-Moment spread to the shell
  of GPs at PSR distance; influenced GPs re-radiate identically each
  subsequent Moment; SSV at any GP = holographic superposition of the
  totality; fading = inverse-square dilution over the expanding sphere —
  **spreading, not absorption**.
- **I1 pins (scoping 2665):** consumed at S2, not here; S1a is
  graph-independent by design (the kernel is stated for any icosahedral
  PSR shell — which nested-hierarchy level it acts at is S1b's question,
  deliberately NOT answered or assumed here).

## §2 — The kernel (range, radial weight, normalization: each derived, none chosen)

Let f_t(x) be the signal amplitude at GP x at Moment t (any single LSP′
channel). The one-Moment re-radiation operator is

**(K f)(x) = (1/N_a) Σ_{y ∈ S_a(x)} f(y)**,  S_a(x) = the PSR shell of x,
N_a = |S_a(x)|, a = PSR.

- **Range = one PSR per Moment.** This is A3′'s broadcast reach verbatim and
  the founder's "spreads to a shell of GPs at the PSR." It is not a
  locality *assumption*: the 2665 nearest-neighbor trap is avoided because
  the shell here is the **PSR** shell of whatever hierarchy level the
  operator acts at — the coarse-scale footprint (edge / cell / other) is an
  OUTPUT of S1b's bridge, not an input.
- **Radial weight = uniform on the shell.** A3′'s "flat per-hop transport"
  and "same icosahedral shell-sum" leave no radial or angular profile
  freedom within one Moment: the Moment's reach IS the shell, weighted
  flat. No choice was available to the worker.
- **Normalization = signal-conserving (row sums 1).** The founder's picture
  contains spreading and **no absorption**: "the fading is inherent in this
  spreading." A per-hop loss factor would smuggle P2 (the gap) into P1 (the
  kernel); the charter's P1/P2 separation therefore *forces* the doubly
  stochastic normalization here, with all loss deferred to the on-site
  restoring DOF at S1c. On a vertex-transitive shell relation K is
  symmetric, hence doubly stochastic.

**Iteration + persistent source.** Per the founder's Moment-after-Moment
re-radiation with the source refreshing each Moment:

**f_{t+1} = K f_t + s**   ⇒ static field **f = (I − K)⁻¹ s**

— exactly the charter §1's "static field = steady state of the iterated
re-radiation (resolvent of the one-Moment kernel)." (On a signal-conserving
K the resolvent is taken on the source's zero-total-charge complement /
neutralizing-background convention; the physical field is defined up to the
uniform mode, which carries no SSV_net.)

## §3 — GATE G1: the lossless limit recovers registered inverse-square — PASS

**G1 statement (charter §2):** in the lossless limit, the iterated kernel's
static superposition must recover the registered inverse-square behavior.

**Step 1 — icosahedral second-moment isotropy (exact).** For any shell
S_a(x) invariant under the icosahedral point group, the second-moment
tensor is exactly isotropic:

Σ_{y ∈ S_a(x)} (y−x)_i (y−x)_j = (N_a a²/3) δ_ij,

because the icosahedral group admits **no invariant rank-2 traceless
tensor** (its first nontrivial invariant harmonic is l = 6). The same
argument kills the l = 4 term: **anisotropic corrections to the shell
average first appear at sixth derivative order.** The emergent continuum
operator is isotropic through O(a⁴∇⁴), independent of the discrete shell's
detailed vertex placement.

**Step 2 — shell-average expansion.** For smooth f,

(K f)(x) = f(x) + (a²/6) ∇²f(x) + c₄ a⁴ ∇⁴f(x) + O(a⁶, l=6 anisotropy),

so **(I − K) → −(a²/6) ∇²** at leading order: the static equation is
Poisson's equation,

−(a²/6) ∇² f = s.

**Step 3 — the registered channels.** For a point source, the scalar
superposition is the Coulomb form **f ∝ 1/r** (the registered potential
behavior of the Φ/SSV_abs channel), and the vector channel — SSV_net, the
vector sum of arriving contributions, which by isotropy aligns with the
radial gradient — scales as **|SSV_net| ∝ |∇f| ∝ 1/r²**: the registered
inverse-square force behavior (glossary: gravity/EM as SSV gradient; the
EM-side unscreened superposition the founder's picture names).

**Two-readings note (registered honestly).** The founder's "inverse-square
dilution of any individual signal" is the per-shell flux statement; the
resolvent's accumulated scalar goes as 1/r with its gradient at 1/r². The
two readings meet in the SSV_net channel: **the force-relevant vector field
is inverse-square in both**, so G1's verdict does not depend on the reading.
The scalar-channel 1/r is itself the registered potential form, not a
discrepancy.

**Step 4 — numerical instrument (fork-blind).**
`code/2668_g1_lossless_powerlaw_check.py`: a periodic z = 12 lattice
(FCC as the 3D icosahedral-coordination instrument proxy — consumes only
z = 12 + shell isotropy, the same properties I1 pins; the 2527 4D→3D
packing-inference flag noted, instrument-level only), kernel K = A/12,
neutralized point source, resolvent solve, log-log power fits on an
intermediate window. **Preregistered PASS bands:** scalar exponent
p_f = 1 ± 0.1; gradient exponent p_g = 2 ± 0.15. Result: **ALL PASS**
(values in the script output block, committed with this patch).
Deliberately absent from the script: any gap parameter, any screening
length, any decay-versus-parameter curve, either candidate value.

**GATE G1: PASS on the first attempt.** The formalization stands; S1b
opens.

## §4 — What S1a hands to S1b and S1c

- To **S1b (the scale bridge, P1a):** the lossless kernel's continuum limit
  is the scale-free Laplacian with coefficient a²/6 tied to the acting
  shell radius a; under block coarse-graining second moments compose
  additively and all higher cumulants are RG-irrelevant, so the bridge
  question sharpens to: **which hierarchy level's a enters the effective
  coarse operator for the qq registration amplitude** — derived at S1b,
  not assumed here.
- To **S1c (the gap, P2):** the strict P1/P2 separation is now enforced by
  construction — K carries zero loss; screening can only enter as an
  on-site restoring term κ added to (I − K), whose identification among the
  three registered candidates is S1c's task, argued from mechanism only.

**The 2664 rider travels on every Morse-class consumer sentence; no such
sentence is consumed here.** Reasoning: `reasoning/2668.md`. Instrument:
`code/2668_g1_lossless_powerlaw_check.py`.

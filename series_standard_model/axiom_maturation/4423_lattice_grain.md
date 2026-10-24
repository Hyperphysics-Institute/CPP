# The Lattice Grain, on the Registered Relay: GR-1j's Two-Level Relay Already Spreads Signals by the Wave Equation (T-1). Its Direction Dependence, From Sampling the PSR Shell With Discrete GPs, Is a 5-Design Effect of Order (kR)⁴ in Group Speed and Is Invisible by Many Orders at Any Accessible Energy. Its Direction-Free Term Is a Subluminal Group Slowing (kR)²/30, η = −1/15 in Planck Units: Blind to Time-of-Flight Tests but in Apparent Tension, by About 60, With Cosmic-Ray Threshold Bounds if It Applies to Hadrons

**Patch:** 4423. **Lane:** foundations, with GR and EM. **Session:** 242.
**Founder input:** "4422 applied. Please proceed: What's left is to show how each signal spreads, that electrons move by
relativity's laws, and that the lattice grain doesn't show." No new physics input; Claude's working at his request. This patch takes
the lattice grain and how a signal spreads; the electrons' dynamics is next.
**Script:** `series_standard_model/code/4423_lattice_grain.py`.
**Critic:** a fresh-context critic returned HOLD on the first draft (verbatim in
`series_standard_model/reviews/2026-10-01_session_242_critic_returns_verbatim.md`). It confirmed the arithmetic and the 5-design
property, and found several problems:
- The draft built on an assumed continuous-time stencil when the registered relay, with its own dispersion law, is already on
  file in GR-1j.
- It misstated a normalization.
- It used phase speed where time-of-flight and thresholds need group speed.
- It called the direction-free term "allowed" when cosmic-ray threshold bounds probably exclude it if it is universal.
- It misdescribed how a larger shell affects the even term.
- It left the global-orientation assumption and 4161's open loophole unstated.

All eight required changes are taken in, and the draft is rebuilt on GR-1j. A second critic accepted the rebuild with four
changes, all taken in: η's dependence on the Moment's length, composite suppression breaking the near-equal condition, the even
term's joint origin, and the D-9 entry. Its return is recorded below the first.

## 1. How a signal spreads: already registered

GR-1j's dynamics (Lemmas L1–L2, Theorem T-1) settles the form of the relay:
- **The two-level form.** Time-reversal invariance of a one-register, one-hop recurrence forces the two-level form
  u(t + τ) + u(t − τ) = 2[αM_R + (1 − α)I]u(t), with M_R the mean over the PSR shell of radius R. The one-level relay damps
  every mode.
- **The dispersion:** cos ωτ = α·m_R(k) + (1 − α), with m_R(k) = sinc(kR) for the continuum shell.
- **The continuum limit:** for every admissible α, the wave equation, with speed c = √α R/(√3τ). R-CSTAR-MAP sets
  c ≡ R_vac/(√3 t_P), so R_vac = √3 l_P at α = 1.

So **the registered relay spreads signals by the wave equation**, the covariant form 4422 needs, at one speed for every channel
that rides it. GR-1j derives this for the gravitational census, Δ|SSV|. That each channel's census (electric 1/R weight, strong)
rides the same recurrence remains 4422 item 1.

## 2. The direction-free term (script part 1)

For the continuum shell at α = 1, expanding cos ωτ = sinc(kR) gives the following, checked numerically:
- **Phase speed:** c[1 − (kR)²/90].
- **Group speed:** c[1 − (kR)²/30].

Time-of-flight and threshold kinematics use the group speed. With R = √3 l_P, kR = √3 E/E_P, the group slowing is
(1/10)(E/E_P)². In the usual parametrization E² = p² + m² + η p⁴/M_P² that is **η = −1/15**: universal and subluminal. Its sign and
size come jointly from the shell's finite radius and the discrete time step (and α), not from directional sampling: in continuous
time the same shell gives a phase slowing of (kR)²/40; the discrete step changes it to (kR)²/90.

**It assumes the Moment is exactly the Planck time.** R-CSTAR-MAP fixes only the ratio R_vac/τ ("not separately observable at
long wavelength"), so in general η = −(1/15)(τ/t_P)². A shorter Moment weakens it: the cosmic-ray tension of §4 would disappear
for τ ≲ 0.12 t_P (R ≲ 0.2 l_P). That is the honest form of the falsifier. (GR-1j already registers the dispersion
family as a falsifier-shaped residue, deliberately not yet used as a prediction.)

## 3. The direction-dependent term (script part 2)

The continuum shell is perfectly isotropic. Direction dependence comes only from **sampling the PSR shell with a finite number of
GPs**. Sampling it with the twelve icosahedral directions (a spherical 5-design, 4160), the group speed varies over 4000
directions by:

| kR | continuum | 12-point shell: mean − 1 | 12-point spread | 32-point shell spread |
|---|---|---|---|---|
| 0.8 | 0 | −2.18 × 10⁻² | 4.2 × 10⁻⁴ | 2.7 × 10⁻⁴ |
| 0.4 | 0 | −5.36 × 10⁻³ | 2.6 × 10⁻⁵ | 1.7 × 10⁻⁵ |
| 0.2 | 0 | −1.34 × 10⁻³ | 1.6 × 10⁻⁶ | 1.0 × 10⁻⁶ |
| 0.1 | 0 | −3.34 × 10⁻⁴ | 9.9 × 10⁻⁸ | 6.5 × 10⁻⁸ |

The spread scales as (kR)⁴, about 10⁻³ (kR)⁴ for the twelve-point shell, because the twelve directions average every quantity up to
fifth order as the whole sphere does. The 32-point shell (icosahedron plus dodecahedron vertices, equally weighted) is still a
5-design and does not improve the order. The mean slowing is the even term of §2 at every sampling.

**Sizes** (R = √3 l_P):

| signal | E/E_P | direction spread | even group slowing |
|---|---|---|---|
| visible light (2 eV) | 1.6 × 10⁻²⁸ | ~10⁻¹¹³ | ~10⁻⁵⁷ |
| TeV gamma ray | 8 × 10⁻¹⁷ | ~10⁻⁶⁶ | ~10⁻³³ |
| 3 × 10²⁰ eV cosmic ray | 2.5 × 10⁻⁸ | ~3 × 10⁻³³ | ~6 × 10⁻¹⁷ |

**The direction dependence does not show.** Laboratory tests of the direction dependence of light speed reach about 10⁻¹⁷ to
10⁻¹⁸. This assumes the global orientation of 4160 (the same twelve directions at every GP), the worst case; if orientations vary,
it averages down further. (Twelve-fold icosahedral coordination cannot tile flat three-dimensional space at all, which is why the
600-cell lives on the 3-sphere; the twelve-point shell is treated here as the relay's local sample.)

**One known loophole:** TODO-4161-STARVED. Where a GP or CP reads only a single arrival, it sees one of the twelve directions
itself, not their sum, and the anisotropy could appear at low order. The same caveat applies to this result.

## 4. The direction-free term against the data

- **Time-of-flight:** gamma-ray burst and blazar timing bound a quadratic scale E_QG,2 at roughly 10¹⁰ to 10¹² GeV (figures from
  memory; verification owed). The relay's E_QG,2 is about 5 × 10¹⁹ GeV (√15 E_P, in the Jacob–Piran convention
  v = 1 − (3/2)(E/E_QG,2)²; at τ = t_P), so time-of-flight is blind to it. No linear term exists,
  as GRB 090510 requires.
- **Cosmic-ray thresholds.** Maccione, Taylor, Mattingly and Liberati (2009; JCAP 0904:022; arXiv:0902.1756) used the Auger
  spectrum and assumed an effective field theory and a proton composition. They bound the proton's quadratic coefficient at about
  10⁻⁶, loosening to about 10⁻³ only where the proton and pion coefficients are both negative and nearly equal. **A universal,
  subluminal η = −1/15 sits in exactly that region and exceeds its bound by about 60.**
- **Caveats:**
  - Those bounds assume protons, while the Auger composition is mixed or heavier, which weakens them.
  - They assume effective field theory.
  - In CPP a proton's momentum is shared among its constituents, so its effective coefficient is suppressed: energies add, so
    η_eff = η Σ xᵢ³. For three equal shares that is 1/9 (about −0.007); a two-constituent pion gets 1/4 (about −0.017). The two
    coefficients are then **no longer nearly equal**, which takes the case out of the loosened region (about 10⁻³), and the
    relevant bound may move back toward 10⁻⁶: suppression may make the tension worse, not better. The comparison is open. (The
    equal-shares figure is illustrative; CPP constituents need not be partons, and in QCD the gluons' and sea quarks' share
    lowers Σ⟨x³⟩ further.)
  - It is not established that CP motion, as distinct from DI-bit waves, inherits the relay's p⁴ term at all.
  - Photon-sector quadratic bounds from ultra-high-energy photon limits also exist (Galaverni and Sigl 2008); verification owed.

**So the direction-free term is a live falsifier**, in apparent tension with cosmic-ray threshold bounds if it applies to
hadrons' constituents.

## 5. What stays open

- **TODO-4423-EVENTERM, the relay's even term against the data:** η = −(1/15)(τ/t_P)² (GR-1j, α = 1) against the cosmic-ray
  threshold bounds (about 60 times over in the universal case at τ = t_P; gone for τ ≲ 0.12 t_P); composite suppression and the
  near-equal condition; whether CP motion inherits it (check against 4161: the 12-edge rule quantises the displacement); photon-
  sector bounds; verification of the time-of-flight figures. Cross-reference GR-1j's dispersion family and TODO-4364-PREFFRAME.
- **α:** values below 1 change the even term; GR-1j prefers α = 1 (AP-3's per-Moment refresh).
- **Each channel's census on the same recurrence** (4422 item 1).
- **TODO-4161-STARVED:** arrival-starved regimes where the twelve directions could show.
- **Electrons by relativity's laws** (4422 item 4): next.
- **Closed in part:** 4422 item 6 (lattice discreteness): the direction dependence does not show (under global orientation, the
  worst case); the even term is reclassified as a falsifier check.
- **Carried:** 4422 items 1–5, 7.

## 6. Question to the founder

None this patch. If the cosmic-ray tension survives checking, whether the relay's slowing applies to the motion of a proton's
constituents may become a physical-picture question for him.

## 7. Report (Plain Language for him)

The grain of the lattice does not show in direction. The registered relay already spreads signals by the wave equation, and the
twelve neighbour directions sample the PSR shell so evenly that a signal moves at the same speed every way. Differences by direction
start only when a wave is squeezed almost to the size of a GP. For light that is a part in 10¹¹³, and even for the most energetic
particles ever seen it is a part in 10³², while experiments look at a part in 10¹⁸.

There is one direction-free effect: very short waves move slightly slower, by an amount that grows with the square of the energy.
Timing tests on gamma-ray bursts cannot see it. But the spectrum of the highest-energy cosmic rays limits exactly this kind of
slowing for protons, and at face value the relay's amount is about 60 times too large. There are possible ways out: the Moment may be
shorter than the Planck time (about eight times shorter would remove the conflict), the cosmic rays may be heavier nuclei, and
matter may not inherit the relay's slowing. Sharing a proton's momentum among its constituents is less clearly a way out, since it
can move the case into a region where the limits are tighter. This is now a sharp test of the theory, and I have filed it as one.

## 8. PD-008

- **Convenient branch, marked:** the first draft's "the even slowing is allowed", withdrawn; it is a live tension.
- **Owned:** the first draft's assumed stencil (the registered relay was on file), its normalization slip, and its use of phase
  speed.
- Nothing registered.

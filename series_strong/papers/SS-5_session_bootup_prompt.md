# SS-5 Session Bootup — Deuteron Binding Energy from Open-Vertex Nuclear Force

## Instructions for Claude

Pull the CPP repo and read `bootup.md`. This session is about writing a new paper: **SS-5 — Deuteron Binding Energy from Open-Vertex Tetrahedral Bonding**.

### What this paper will do

Derive the deuteron binding energy (experimental: 2.224 MeV) from the CPP open-vertex nuclear force mechanism established in SS-2. This is the programme's first result in nuclear physics — a genuinely new sector independent of all existing Layer B threads.

### The mechanism (from SS-2 and founders_vision.md)

The proton is a distorted tetrahedron with vertices {+u, +u, −d, +open}. Net charge +1 from geometry. The open positive vertex is the proton's bonding site.

The neutron is a distorted tetrahedron with vertices {+u, −d, −d, −open}. Net charge 0. The open negative vertex is the neutron's bonding site.

In the deuteron, the proton's open +vertex bonds to the neutron's open −vertex through DP chain insertion. The binding energy is the energy released when these two open vertices form a bond.

### Key numbers from SS-2

- l_unit = ℏc/Λ_QCD = 0.589 fm (lattice spacing)
- l_edge = l_unit/φ = 0.364 fm (tetrahedral edge length)
- r_proton = 0.883 fm (distorted tet + ZBW smearing, ε = 1.94)
- M₀ = m_e × z/φ = 3.790 MeV (base mass scale)
- σ ≈ 243 MeV/fm (string tension conjecture, SS-2/SS-4)
- μ_proton = 2.789 μ_N (0.1% agreement)

### What to read (in addition to bootup.md chain)

1. `series_strong/papers/SS-2_lattice_scale_nucleon_structure.tex` — §5 (proton structure), §6 (neutron structure), §7 (nuclear force discussion)
2. `founders_vision.md` — entries on proton structure, neutron structure, nuclear force (10 April 2026), open-vertex bonding
3. `series_strong/papers/SS-4_string_tension.tex` — for σ derivation and DP chain energy framework

### The calculation needed

1. **Inter-baryon distance:** The proton-neutron separation in the deuteron. This should follow from the open-vertex bond geometry — the +vertex of the proton bonds to the −vertex of the neutron across a DP chain of length related to l_unit.

2. **Bond energy:** The energy of the DP chain bond between the two open vertices. This involves:
   - Coulombic attraction between +qCP and −qCP across the gap
   - DP chain formation energy (related to σ × distance or to sea_strength × ℏc/r)
   - Cage distortion energy from accommodating the bond

3. **Binding energy:** B = E_bonded − E_unbonded. The target is B ≈ 2.224 MeV (experimental deuteron binding energy).

### What makes this a strong star shot

- **New sector:** First CPP prediction in nuclear physics. Completely independent of lepton masses, gauge couplings, and quark mass hierarchy.
- **Independent Layer A:** The calculation is geometric — cage vertex energies and DP chain bond mechanics. No operator formalism, no Gibbs equilibration, no trace identities. Potentially the cleanest Layer A result in the programme.
- **Precision target:** 2.224 MeV, measured to ~10 ppb. Even a 5–10% zero-parameter prediction is a powerful new star shot.
- **Cascade potential:** If the deuteron works, the same framework extends to ³He, ⁴He, ³H, and eventually the light nuclear binding curve. One mechanism, multiple predictions.

### Additional predictions to attempt in the same paper

If the primary calculation succeeds, try to also derive:
- Deuteron radius (experimental: 2.128 fm)
- Deuteron magnetic moment (experimental: 0.8574 μ_N)
- Proton-neutron mass difference (1.293 MeV) from the different cage distortion energies
- Qualitative argument for why the diproton and dineutron are unbound (same-polarity open vertices repel)

### Paper format

Follow `templates/paper-formatting.md`. Use the central bibliography `../../bibliography/cpp_references.bib`. Apply the Layer A/B/C framework from the start — label every assumption's epistemic status. This paper should be born clean.

### Context from the programme

This paper was identified as the highest-value next star shot during the swarm validation strategy discussion (16 April 2026, documented in founders_vision.md). The CPP programme's proof architecture depends on covering many independent sectors, not on perfecting individual papers. Nuclear binding is the most tractable new sector with the largest cascade potential.

---

*Prompt prepared by Claude Opus (Anthropic), 16 April 2026.*

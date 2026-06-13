# Mechanism — SR-2: The Spin-Bit Axiom

Plain mechanistic account of how the radiative tensor sector of gravity arises in Conscious Point
Physics, complementing the formal treatment in `../SR-2_spin_bit_axiom_quadrupole_formula.tex`.

## The starting point: a scalar + a vector

In the c07/c08 formulation, each Grid Point (GP) broadcasts a Lattice State Packet (LSP) to its
Planck-Shell-Radius neighbours every Absolute Moment. The packet carried one scalar, |SSV|_abs
(sourcing gravitational time dilation, g_tt), and one vector, SSV_net (sourcing spatial curvature
and gravitomagnetism, g_ij). This recovers Schwarzschild, the Newtonian potential, and weak-field
GR statics with notable economy.

## The gap: helicity ±2

A gravitational wave is transverse-traceless: it stretches one transverse axis while squeezing the
orthogonal one (the + and × polarizations), which is helicity ±2. A scalar carries helicity 0; a
vector carries helicity 0 and ±1. No combination — linear map, amplitude or gradient bilinear, or
collective mode — of a scalar and a vector on the lattice produces a first-order helicity-±2 mode.
The transverse-plane quadrupole that *is* the gravitational-wave signal has no source in a
scalar+vector packet. This is the helicity-±2 gap.

## Why no clever workaround exists (necessity)

Three independent attempts to fill the gap without a new ingredient all fail, each for a different
structural reason:
- **Bilinears.** V_iV_j does carry helicity-2 structure, but at second order in amplitude and at
  double the source frequency — not the first-order, source-frequency strain detectors see.
- **Collective modes.** The full long-wavelength spectrum of the scalar+vector field on the
  600-cell has exactly four branches, of helicity {0, 0, ±1}. A helicity-±2 basis vector simply
  does not exist in the span of one scalar and one vector. (The emergent-graviton route is *allowed*
  — CPP's Lorentz invariance is emergent, so Weinberg–Witten does not forbid it — but the lattice
  does not realise it.)
- **The non-radial twist.** Because each GP's 12 neighbours are icosahedrally arranged, every hop
  involves a turn; one might hope this puts a spin bit on the broadcast. It cannot: a rotation
  reorients vector components but cannot raise the tensor rank of the carried data, and any
  data-acting twist would instead give the broadcast a Planck-scale mass (excluded empirically to
  ~1e-46). CPP's absolute (Nexus) frame is exactly what keeps the broadcast flat and massless.

Conclusion: to carry the observed gravitational-wave polarizations, the substrate *needs* a
fundamental rank-2 ingredient. This is a conclusion, not a preference.

## The fix: the spin bit

The 600-cell already holds the chair. On the 12-vertex icosahedral neighbour shell, the five l=2
("quadrupole") functions form the irreducible representation H, and their m = ±2 components
{x²−y², xy} are *exactly* the + and × gravitational-wave polarizations. The axiom A3′ adds one
symmetric-traceless rank-2 field Q_ij to the broadcast — the "spin bit" — seated in this H slot.
That is the entire new ingredient: one degree of freedom, no new dial.

Three things then happen for free:
1. **Propagation.** The same icosahedral shell-sum that propagates the scalar and vector is
   rank-agnostic — it acts component-by-component — so Q_ij automatically obeys □Q_ij = source at
   exactly c.
2. **The coupling.** Requiring that the *same* Newton constant G governing the scalar sector govern
   the tensor sector fixes the source strength at λ = 16πG/c⁴ — the Einstein coupling — with no new
   parameter. The Einstein quadrupole formula h^TT = (2G/c⁴r) Q̈^TT is then *derived*, not asserted.
3. **No spurious modes.** Conservation makes the scalar and vector radiative tails cancel in the
   curvature, so the tidal response is pure tensor (Eardley class N₂), and the spatial trace the
   packet does not carry turns out to be redundant — fixed locally by the channels it does carry.

## Why the broadcast "completes" here

The icosahedral rotation group protects exactly the multiplets l = 0, 1, 2 (irreps A, T₁, H); any
l ≥ 3 has more than five components and cannot descend intact. So A ⊕ T₁ ⊕ H = 9 numbers is the
*entire* content the geometry can carry faithfully. The spin bit is not an arbitrary addition; it is
the last rung of a ladder (DI-bit → LSP → LSP′) that terminates at rank 2. There is no fourth rung.

## What this does and does not claim

It closes the radiative (helicity-±2) half of `op:einstein` — the tensor gravitational-wave sector.
It does **not** claim the full nonlinear Einstein equation with Λ (that is the broader OPEN-SR-4,
pending the cosmological-constant reconciliation). And the axiom is honestly mono-sectoral: the
strong sector can build spin-2 hadrons from orbital angular momentum without needing Q_ij, so the
spin bit earns its place by *necessity* in the radiative sector, not by breadth of motivation.

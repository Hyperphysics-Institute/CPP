# Spin-2 Task 1 — THE FLOW CHOICE: `Q_ij` lives in the GP→GP broadcast (option B) — the Lattice State Packet is extended for the third time, by the same logic that built it (Patch 1121)

**Sub-arc:** `series_relativity/op_einstein_closure/spin2_construction/` · **Charter:** `README.md`
· **Verify:** `code/1121_task1_source_configurational.py`
**Status:** Task 1 of the construction phase (the diagnostic phase closed at 1120). **DECISION:
option B** — the symmetric-traceless rank-2 degree of freedom `Q_ij` is carried in the **GP→GP
Lattice State Packet (LSP) broadcast**, extending it from four dynamical components
(`|SSV|_abs` scalar + `SSV_net` vector) to nine (+ the five-component `Q_ij`). Options A (CP
State Register attribute) and C (GP→CP instruction) are eliminated as the *home* of the
primitive — A because the source is irreducibly configurational, C because the readout is
derivable — though both flows participate: A's existing reports *assemble* the source, and C's
displacement map *reads out* the broadcast, as theorems, not axioms. **This is a decision
record and design-constraint registration. The axiom text is Task 2; NO VERDICT MOVED.**

---

## 1. The precedent — the packet has been extended before, for exactly this reason

The c07 glossary (canonical LSP definition) states it explicitly: the LSP **"supersedes the
SR-era DI-bit broadcast by adding the vector component needed for general relativity."** The
broadcast packet is not a frozen primitive; it is the place where, once before, a sector of
gravity demanded — and received — a new carried component:

| Rung | Packet content | Sector it unlocked |
|------|----------------|--------------------|
| 1 | DI-bit: scalar `\|SSV\|_abs` | Special relativity; time dilation (g_tt) |
| 2 | LSP: scalar + vector `SSV_net` | Weak-field GR statics; spatial curvature (g_ij); Schwarzschild |
| 3 | **extended LSP: scalar + vector + tensor `Q_ij`** | **The radiative tensor sector; GW polarizations; op:einstein (a)** |

Each extension was forced when the next sector of gravity exceeded the representational
capacity of the existing packet — the scalar alone could not carry spatial curvature; the
scalar+vector cannot carry helicity-±2 radiation (1109–1119, rigorously). **Option B is not a
novel architectural move; it is the third rung of an existing ladder, taken by the established
logic of the programme.**

## 2. The eliminations (each grounded, each with a verify demonstration)

**A — the CP State Register — is the wrong home, twice over.** (i) *Nothing to report:* the
mass quadrupole is **irreducibly configurational** — a single point mass has identically zero
quadrupole about its own location, for any mass (verify D1). A rank-2 "shape" attribute on a
single CP has no physical content to carry; the source quadrupole exists only as a property of
*extended configurations* — precisely 1120's finding that matter-side l=2 lives in the
relative-coordinate function space. (ii) *Double-counting hazard:* a CP-side rank-2 attribute
would sit alongside the emergent structures (ZBW orbital spin-½; configurational hadron/nuclear
l=2) that 1120 showed need no bit, inviting exactly the double-counting the kickoff handover
warns against.

**C — the GP→CP instruction — is the readout, not the carrier.** In the PCD cycle, the GP→CP
displacement instruction is the *output* of the Compute step: it is how the field acts on
matter (it is what stretches a detector arm). Once the broadcast carries `Q_ij`, extending the
displacement map to include the TT strain is a *derivation* within the existing metric-map
machinery (the Task 4 GR-recovery work) — a theorem, not a primitive. Placing the primitive in
C would also leave the field with no GP→GP channel to propagate in, forcing B anyway.

**The induction asymmetry decides it:** A or C, if chosen as the home, would each still require
a GP→GP transmission channel for `Q_ij` to propagate between Grid Points — i.e., **A or C would
induce B**. B alone induces neither: the source assembles from existing CP→GP reports (below),
and the readout derives from the existing Compute→Displace map. **B is the irreducible core.**

## 3. The source needs no new report (why A's job is already done)

The mass quadrupole of any configuration is assembled purely from **per-CP positions and
masses** — content the existing flows already carry: the CP→GP register reports the GP address,
and mass enters as the eDP polarization energy `E_pol = mc²` (c07's explicit LSP construction,
`|SSV|_abs = E_pol/V₀`). Verify D2 computes `Q_ij` for binary configurations from positions
alone. The Perceive/Compute steps can therefore assemble the local source quadrupole from what
GPs already know. **1114's gap statement is confirmed in its sharpest form: the missing piece
was never the source — it is the broadcast channel to radiate it into.**

## 4. Placement in the PCD cycle (the cycle's structure is untouched)

- **Perceive:** each GP receives its PSR shell's packets — now nine dynamical numbers each
  (1 + 3 + 5) instead of four. No new flow; a wider packet on the existing flow.
- **Compute:** the rank-agnostic icosahedral shell-sum (1113) processes `Q_ij` with the *same
  operator* that processes the scalar and vector — `□Q_ij = source` at c is native. The source
  term assembles from the perceived local matter configuration (§3).
- **Displace:** the metric map extends to include the TT sector (Task 4); the displacement
  instruction acquires its quadrupolar component *as output* (the C-readout, derived).

## 5. What B inherits from the diagnostic record (all already in hand)

- **Propagation at c, wave equation native** (1113: the shell-sum is rank-agnostic).
- **Massless, long-range carriage** (1119: absolute/Nexus-frame transport — the flat
  connection is empirically forced to 10⁻⁴⁶–10⁻⁵¹, and it is CPP-native).
- **Exact 5-fold degeneracy** (1120: the icosahedral H_g irrep protects the spin-2 multiplet
  intact — no lattice fine-structure of GW polarizations — where a cubic substrate would split
  it 2+3). The geometric slot identified in 1112 is the seat; 1119/1120 supply its
  masslessness and its protection.

## 6. The two standing design constraints (registered here, binding Tasks 2–4)

1. **No-ZBW-double-counting** (from the kickoff handover): `Q_ij` is the *radiative tensor
   field*, distinct from emergent orbital spin-½ (ZBW) and from matter's configurational l=2
   (hadrons, nuclei — 1120). The axiom must not re-derive, replace, or disturb either.
2. **No-static-double-counting** (registered this session): CPP divides gravity's labor — the
   scalar `|SSV|_abs` already recovers statics *exactly* (Schwarzschild, c07/c08), the vector
   carries gravitomagnetism. `Q_ij` must therefore be sourced by the **time-varying
   (TT-projected) part of the matter quadrupole only**: a static configuration has constant Q,
   `d²Q/dt² = 0`, and radiates nothing (verify D3 — which also exhibits the GW
   double-frequency signature `ω_GW = 2ω_orbit` and the `×`-channel oscillation from positions
   alone). This blocks the standard spin-2 bootstrap (a massless tensor coupled to full
   `T_μν` regenerating all of GR) from double-counting the recovered Newtonian sector. The
   precise covariant form of the source projection is **Task 3's central engineering problem**.

## 7. The justification preamble (the architect's framing, adopted)

For the axiom writeup and DG-3 submission, the justification is stated in this form —
**mono-sectoral by CPP's own division of labor; multi-evidential within the sector;
universally sourced in principle; observationally concentrated by instrumental access;
structurally load-bearing for three arcs**:

- *Mono-sectoral, honestly:* CPP's scalar and vector already carry statics and
  gravitomagnetism; the axiom is load-bearing for one sector — radiative tensor gravity. CPP
  cannot (and does not) borrow GR's trivial "every falling apple is spin-2 evidence" framing.
- *Multi-evidential within the sector:* (i) ~100+ direct interferometric detections; (ii)
  multi-detector polarization tests (GW170814 onward) favoring tensor over pure vector/scalar;
  (iii) **binary-pulsar orbital decay** — five decades of Hulse–Taylor agreement with the GR
  quadrupole formula (~0.2%), and the double pulsar J0737-3039 at the 10⁻⁴ level — an
  *independent channel* (back-reaction, not direct detection); (iv) the **no-dipole
  constraint**: scalar–vector gravities generically radiate dipole, stronger and with
  different orbital dependence; pulsar timing excludes it. One sector, four legs.
- *Deeply hidden, universally present:* gravity couples to everything — the tensor field,
  once granted, is sourced at every scale from fermions to the DP-Sea to cosmic binaries. Its
  *distinguishing* signature (helicity-2 radiation) is suppressed by gravity's weakness and
  becomes empirically accessible only through extreme amplification: astronomical masses,
  relativistic velocities, 10⁻²¹ strain precision over km baselines and decades of pulsar
  timing. The evidence concentrates in one channel because that is the only channel nature
  left open at our instrumental reach — the axiom is not special-purpose; *the telescope is*.
- *The architect's lattice parallel:* the 600-cell itself was once resisted in favor of simple
  cubic packing — and Step 7 showed the cubic choice would have *split the very spin-2
  multiplet this axiom requires* (E ⊕ T₂), while the icosahedral geometry protects it intact
  (H_g) and had pre-slotted its seat (1112). The spin bit is of the same category as the 4D
  lattice: a subtle, initially-resisted structural commitment that turns out to be what gives
  gravity its finesse from the subquantum to the cosmic scale. Twice now the programme has
  asked whether the substrate could borrow a capacity from dynamics (chirality by collision;
  spin-2 by superposition/twist), and twice the honest answer was that the substrate must own
  it as a primitive.
- *Structurally load-bearing:* the one bit closes `op:einstein` (a), removes the dark-sector
  cap, and unconditionalizes the CC reconciliation (SR-5 ≡ SM-6) — three dependent arcs on one
  axiom.

## 8. What this patch does and does not do

**Does:** fixes the flow (B); registers the eliminations and their grounds; registers the two
design constraints; adopts the justification preamble; stages Task 2. **Does not:** write the
axiom text (Task 2 — the precise statement: the new primitive, its H_g transformation law, its
shell-sum dynamics, its constraints, in minimal form); derive the coupling (Task 3); assemble
GR-recovery (Task 4); move any verdict. The axiom touches the foundational axiom inventory
only at Task 2+, with STOP-and-warn on every contested registry, and ships nowhere without
DG-3 swarm review (Task 5) and the architect's sign-off.

# Spin-2 Construction — the fix for op:einstein (a) (sub-arc charter)

**Folder:** `series_relativity/op_einstein_closure/spin2_construction/`
**Goal:** supply the missing **spin-2 (rank-2) degree of freedom** that the current CPP LSP lacks, so
that the CPP field equation sources the **helicity-±2 (transverse-traceless) gravitational-wave
polarizations** of GR — closing `op:einstein` (a) and removing the standing GW-polarization tension
(Patches 1109–1111).
**Opened:** Patch 1112. **Status:** OPEN — Step 1 done (the d.o.f. is identified and grounded; see
below). The full construction (broadcast law + wave equation + GR-recovery + GW-data confrontation)
remains a substantial effort. **op:einstein (a) NOT closed.**

---

## The diagnosis this fixes (from 1109–1110)
The LSP carries `|SSV|_abs` (l=0 scalar → g_tt) and `SSV_net` (l=1 vector → g_ij via the gradient
tensor). A scalar + vector cannot source the helicity-±2 GW modes (`h_xx−h_yy`, `h_xy`); c07 §6 asserts
the GR wave equation but its metric map provides no rank-2 d.o.f. So CPP is presently a scalar–vector
gravity, missing the spin-2 radiative sector.

## The candidate d.o.f. (Step 1, Patch 1112 — grounded)
The natural missing piece is the **l=2 quadrupole moment** of the local 600-cell shell deformation.
Computed on the icosahedral 12-edge neighbor shell (`code/1112_step1_l2_shell_mode.py`):
- the 5 l=2 functions are **fully resolved** on the 12 vertices (rank 5);
- l=2 is **orthogonal to l=0 and l=1** on the shell (an independent d.o.f., not a repackaging of the
  existing scalar/vector — guaranteed by the shell's spherical-5-design property, 1108);
- the **m=±2** components `{x²−y², xy}` are **exactly the GR `+` and `×` polarizations** (m=0,±1 are the
  longitudinal/shear helicity-0/±1 modes the LSP already carries).

So the fix is concrete: **extend the LSP from (l=0 scalar, l=1 vector) to include the l=2 quadrupole
`Q_ij`** (a symmetric traceless rank-2 broadcast), which the 600-cell shell supports natively.

## The construction path (the steps that remain)
1. **(done, 1112)** Identify + ground the d.o.f.: l=2 quadrupole of the shell deformation.
2. **(done, 1113) Broadcast law for `Q_ij`.** PROPAGATION is native: the PCD icosahedral shell-sum is
   rank-agnostic, so a broadcast `Q_ij` obeys `□Q_ij = source` (same operator as scalar/vector), and its
   helicity-±2 part propagates at c as the GW `+`/`×` modes. BUT the GP has no rank-2 d.o.f. to
   broadcast — `Q_ij` is a foundational LSP extension (600-cell H_g slot, but a postulate). So closure
   localizes to Step 3.
3. **(done, 1114 — the verdict) A GP quadrupole d.o.f. is NOT independently motivated.** CPP's
   fundamental flows carry only scalar+vector (CP→GP CSR: type/polarity/emergent-vector-spin; GP→GP:
   |SSV|_abs+SSV_net; GP→CP: displacement). Candidates fail: DP-sea polarization = the vector SSV_net;
   CP spin = emergent orbital *vector*; the H_g (l=2) slot exists but nothing excites it. Corpus mute
   (only matter-side nuclear quadrupoles). ⇒ closing (a) is an **explicit axiom extension** — add a
   rank-2 d.o.f. to flow A (CSR), B (LSP), or C (GP→CP). The architect's decision.
4. **GR-recovery** — show the extended (scalar+vector+tensor) metric map assembles into the full
   `G_μν = 8πG T_μν/c⁴` (this is the actual closure of op:einstein (a)).
5. **Confront GW data** — recover the observed tensor polarizations; re-examine c08's claim that
   scalar/vector modes are suppressed by `(l_P/λ)²` (now with the tensor modes genuinely present).

## Step 4 (1115) — run at the Einstein wall + the emergent option D
Testing the architect's proposal: a superposition / 2nd-order combination of SSV vectors cannot give
the LINEAR helicity-2 GW (the bilinear V_iV_j has the structure but at amp²/double-frequency). The
no-new-axiom route is therefore EMERGENT — permitted because CPP's preferred-frame/emergent-Lorentz
structure evades Weinberg–Witten (CPP is in the condensed-matter emergent-gravity class), and
consistent with CPP's emergentism (ZBW spin, emergent SR). Non-generic; hinges on the 600-cell
emergent-graviton calculation. So the options are A/B/C (fundamental axiom) **or D (emergent, no axiom)**
— attempt D first.

## Step 5 (1116) — THE ASSAULT: emergent-graviton calculation → option D RULED OUT
The dynamical matrix of the scalar+vector field on the icosahedral 600-cell lattice has 4 modes of
helicity {0,0,±1} only — no helicity-±2, for any couplings (helicity fixed by the representation). The
emergent route fails. **VERDICT: the spin-bit axiom (A/B/C) is NECESSARY** to carry gravity's tensor
sector; the architect's granularity intuition is the reason. CPP joins mainstream gravity (spin-2
fundamental). Remaining = engineer the axiom (which flow, its form, source coupling); the geometric slot
(H_g) and propagation (shell-sum) are in hand.

## Step 6 (1119) — THE THIRD ASSAULT: the architect's non-radiality (PSR-hop twist) mechanism
Testing the architect's remaining no-axiom route: the 600-cell's GPs are not radial to any propagation
direction, so each PSR hop involves an incremental turn — could the accumulated twist place a spin bit
on the GP→GP signal? Formalized as a **discrete connection** (per-edge transport `R_j` on the carried
data — genuinely absent from 1116, which used scalar coupling coefficients only). RESULT: the verdict
**survives**, three ways: (i) the representation bound — the carried (φ,V) space has J_z spectrum
{0,0,±1}, the helicity-±2 projector on it is identically zero, and rotations are irrep-preserving (a
twist reorients components; it cannot raise rank); (ii) a data-acting twist **gaps the vector sector**
at `M = 4|sin(θ/2)|` Planck masses and adds circular birefringence (`ω²_± = M² ± 4 sinθ·k`) — channel
optics, not new helicity; massless long-range propagation forces θ < 10⁻⁴⁶–10⁻⁵¹ (the geometric
quaternionic value θ = π/5 gives M ≈ 1.24 M_Planck, maximally excluded); (iii) the empirically-forced
flat connection (`R_j = I`, absolute/Nexus-frame carriage — CPP-native) is exactly the regime 1116
computed. **Byproduct banked:** the absolute-frame axiom is revealed as load-bearing — it is what keeps
the broadcast massless. Option D stays RULED OUT after **three assaults** (1115 bilinears, 1116
collective modes, 1119 connection); the spin-bit axiom stays NECESSARY.

## Step 7 (1120) — the tensor-meson test: f₂(1270) does NOT hit the wall; the second motivation dissolves
The kickoff handover's candidate second motivation, run to ground: can the strong sector build a spin-2
hadron emergently? **Yes** — and the corpus already contained the answer (SS-1e lists χ_c2(1P) as
"L=1, J=2", the same ³P₂ construction as f₂(1270); SS-6's deuteron quadrupole is orbital-dominated).
Demonstrated: (P1) L=1 ⊗ S=1 → J ∈ {0,1,2} with degeneracies {1,3,5} — the 5-dim J=2 multiplet is built
from emergent vectors only; (P2) the two-body relative-coordinate function space fully supports l=2
(rank 5 on lattice relative positions) — the resource the per-point broadcast lacks (4 components,
l ≤ 1) is unbounded in configurations; (P3) icosahedral branching protects the spin-2 multiplet exactly
(l=2 → H, irreducible — the H_g slot of 1112; first splitting at l=3), where a cubic lattice splits it
E ⊕ T₂ (2+3). **Honest accounting: the spin-bit axiom remains MONO-MOTIVATED by GW empirics** — its
strength is *necessity* (three closed assaults), not breadth. The wall is located with precision:
**per-point granularity** — matter can be spin-2; the radiating field cannot. The geometry pre-slots
*and protects* the seat the axiom will fill.

## Task 1 (1121) — THE FLOW CHOICE: option B — `Q_ij` lives in the GP→GP Lattice State Packet
The construction phase opens with the architectural decision. **B (LSP broadcast)** is the home of the
primitive: the packet extends from four dynamical components to nine (scalar + vector + the 5-component
`Q_ij`). The decisive arguments: (i) **precedent** — the c07 glossary states the LSP "supersedes the
SR-era DI-bit broadcast by adding the vector component needed for general relativity"; the tensor
extension is the *third rung* of an existing ladder (DI-bit scalar/SR → LSP scalar+vector/GR-statics →
extended LSP +tensor/GR-radiation), each forced when a sector of gravity exceeded the packet's capacity;
(ii) **A eliminated** — the source quadrupole is irreducibly configurational (a single point mass has
zero quadrupole about itself; verify D1), assembled from per-CP positions+masses the register already
reports (verify D2) — the missing piece was never the source, it is the channel (1114 sharpened);
(iii) **C eliminated as home** — the GP→CP instruction is the Compute step's *output* (the readout that
stretches a detector arm), derivable once B exists; (iv) **induction asymmetry** — A or C would each
still need a GP→GP channel (inducing B); B induces neither. PCD placement: Perceive 9 numbers, Compute
via the rank-agnostic shell-sum (1113) + source assembly, Displace via the extended metric map (Task 4).
B inherits the staged record: massless absolute-frame carriage (1119), protected H_g degeneracy (1120).
**Two binding design constraints registered:** no-ZBW-double-counting (the handover's) and
**no-static-double-counting** (new: the scalar keeps statics — Schwarzschild exact; `Q_ij` is sourced by
the time-varying TT-projected quadrupole only; verify D3 shows static ⇒ d²Q/dt²=0 ⇒ no radiation,
orbiting ⇒ ω_GW = 2ω_orbit). Justification preamble adopted: **mono-sectoral by CPP's labor division,
multi-evidential within the sector** (direct detections + polarization tests + binary-pulsar decay +
no-dipole constraint), universally sourced, instrumentally concentrated, load-bearing for three arcs.
Axiom text = Task 2. NO VERDICT MOVED.

## Resting state — DIAGNOSTIC PHASE COMPLETE (Steps 1–7); CONSTRUCTION PHASE OPEN (Task 1 decided)
The construction is fully mapped: the d.o.f. is identified (l=2 quadrupole), geometrically slotted
(600-cell H_g, 1112), and propagation-ready (rank-agnostic shell-sum, 1113) — but **absent from CPP's
axioms** (1114), so closing (a) is a foundational choice (add a rank-2 d.o.f. to a fundamental flow),
not a derivation. Steps 4–5 (source coupling `Q_ij ↔ T_μν`, full GR-recovery, GW-data confrontation)
are reachable only **after** that axiom choice.

## Falsifier / on-success
- **Falsifier:** if the 600-cell broadcast structure cannot carry a propagating l=2 quadrupole (e.g.
  the PCD cycle has no quadrupole channel, or it cannot propagate at c), the spin-2 sector cannot be
  built within CPP's current axioms, and the GW-polarization tension becomes structural.
- **On success:** op:einstein (a) closes; the dark-sector cap is removed; the CC reconciliation
  becomes an unconditional theorem; CPP reproduces the observed tensor GW polarizations.

## INDEX
Step log lives in the parent `../INDEX.md` (op:einstein arc). Step 1 = this patch (1112).

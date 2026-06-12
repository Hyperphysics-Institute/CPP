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

## Task 2 (1123) — THE AXIOM TEXT (candidate v0.1): A3′, the Completed Broadcast Axiom
The candidate text is drafted, private-lane, for DG-3 review before any registry touch. **Form of the
move: amendment, not addition** — the registry's A3 (DI-bit propagation) is the broadcast axiom, already
one rung behind the corpus (c07's LSP superseded the DI-bit without a registry amendment); A3′
consolidates the full ladder (DI-bit → LSP → LSP′) per the A6′ precedent; count stays 9 (dual accounting
→ 10 presented honestly for DG-3). **The packet completes to LSP′ = (Φ [A, l=0], V_i [T₁, l=1], Q_ij
[H, l=2]) — 1+3+5 = 9 dynamical components.** Clauses: C1 symmetric-traceless (5 exactly, H-protected);
C2 absolute-frame flat carriage (1119); C3 dynamics by the *same* rank-agnostic shell-sum (1113 — no new
dynamical law); C4 source = κ ∂²_t[traceless quadrupole density] assembled from existing reports, κ
fixed by the scalar-sector G (**zero new parameters**; statics killed by construction); C5 readout
demoted to derivation obligation. **The completion theorem** (verify 1123): the intact icosahedral
descents are exactly l = {0,1,2} (dimension bound: 2l+1 ≥ 7 > 5 for l ≥ 3, permanent) and LSP′ = A ⊕ T₁
⊕ H is *precisely* the protected content — **the ladder terminates at rank 2; no fourth rung; the axiom
is a completion**. Obligations: OB-1 quadrupole formula with scalar-G; **OB-2 polarization suppression
via CPP's conservation laws (the primary falsifier — the axiom ships with its own kill switch)**; OB-3
statics untouched; OB-4 no emergent double-counting. Falsifiers F1–F4 stated (polarization content, GW
speed = c, multiplet integrity as a lattice discriminant, dispersion ceiling). Registration path: DG-3 →
sign-off → single registry patch under STOP-and-warn. Recommended sequencing: Task 3 → Task 4 → DG-3.

## Task 3 (1124) — THE COUPLING AND THE QUADRUPOLE FORMULA: λ = 16πG/c⁴, zero new parameters
**C4 revised v0.1 → v0.2** (defect caught in derivation: a "quadrupole density" is origin-dependent —
not a legitimate local law; correct local source = the **traceless stress** T_ij^{TF}, GP-assemblable
from CP momentum flux, with the quadrupole emerging in the far field through conservation, exactly as in
GR). Chain (each link verified): □Q = −λT^{TF} → retarded far field (λ/8πr)M̈^{TF} → conservation
identity ∫T_ij d³x = ½M̈_ij (verified to 6×10⁻⁷ on an e=0.6 Kepler binary; consumes mass = CP-count and
momentum = displacement-rule conservation) → strain-valued readout + scalar-G matching ⇒
**λ = 16πG/c⁴** ⇒ **h^TT = (2G/c⁴r)Q̈^TT(t_ret)** — the Einstein quadrupole formula. **The arc's origin
gap closes: the equation c08 ASSERTED is now DERIVED** (d.o.f. from A3′, dynamics from 1113, source from
C4, coefficient from G-consistency). Luminosity inherited by TT-sector isomorphism (energy normalization
→ Task 4). **OB-3 discharged as theorem** (perfect-fluid T^{TF}=0 identically; tensor virial for bounded
statics — Schwarzschild untouched). **OB-2 part 1 discharged** (no monopole/dipole — the no-dipole
evidential leg is now a *consequence* of A3′; part 2 = readout helicity content → Task 4, the kill
switch). Observables with nothing to tune: Hulse–Taylor Ṗ_b = −2.4031×10⁻¹² (record 0.9983±0.0016 of
GR over 5 decades); double pulsar −1.2483×10⁻¹² (record 1.000 to 10⁻⁴); GW150914-class h ~ 3×10⁻²¹;
GW speed = c. NO VERDICT MOVED.

## Task 4 (1125) — THE READOUT, THE TT-ONLY RESPONSE, THE ENERGY CLOSURE: Eardley class N₂
The kill switch, sharpened and survived. The real trap: **the scalar and vector channels radiate too**
(1/r quadrupole tails at Newtonian strength — no Brans–Dicke suppression available); uncanceled, CPP
would predict breathing/longitudinal strain AND ~10% extra binary-decay luminosity — dead at the double
pulsar. **P1 (symbolic, exact):** for constraint-satisfying plane waves, R_{i0j0} depends ONLY on the
two TT combinations — scalar tail, vector tails, longitudinal, and trace all cancel in the curvature
(direct sympy computation + gauge-invariance counting). **P2 (discovery):** the harmonic pattern needs a
10th component (spatial trace τ, sourced by T_kk) the packet lacks — but **τ is redundant**: locally
completed from the channels, ∇τ = 3(∂_t h̄_{0i} − ∂_j Q_{ji}); verified = GR's (2G/c⁴r)M̈_kk to 10⁻¹⁹;
statics τ = 0 by virial (why c07/c08 never noticed). Physics ratifies the completion theorem: no second
A-slot needed — conservation makes it redundant. **C5 v0.2** codified (constraint-consistent assembly;
derived-unique vs postulate = explicit DG-3 question Q1). **P3:** six Eardley modes on an e=0.6 binary
(the armed trap — circular hides it, M̈_kk=0): breathing/long/vector ≤ 4×10⁻¹¹ of tensor with the
completion; **O(1) violation without it** (counterfactual documented). **P4:** sphere-integrated
Isaacson flux / Einstein luminosity = 1.000246 — source decay = field flux; normalization forced; the
scalar/vector tails carry no independent energy ⇒ no extra channel ⇒ **the double-pulsar 10⁻⁴ pass is
real**. OB-1 COMPLETED; OB-2 fully DISCHARGED; OB-4 DISCHARGED by architecture. **Tasks 1–4 complete —
the package is DG-3-ready** (review questions: Q1 completion-rule status; Q2 amendment-vs-addition).
NO VERDICT MOVED.

## Task 5 (1126) — DG-3 CYCLE OPENED: the A3′ review package dispatched
Self-contained package at `review/a3prime_axiom_review_package_v1.0.md` (CONV-001/dispatch-protocol
compliant: candidate v0.2 full text, OB-1..4 discharge claims, triage T1–T7 with T1 = the OB-2
kill-switch chain and T2 = the completion-rule status, reviewer steers, and the three construction
verify scripts embedded in full). Panel: ChatGPT, Copilot, Grok. Responses aggregate in
`review/reviews-A3PRIME.md`. First axiom-level change ever put to the panel — maximum scrutiny
requested. Registration remains gated on 3/3 + architect sign-off → single STOP-and-warn registry
patch. NO VERDICT MOVED.

## Round 1 + RESTATE (1127) — DG-3 returned 2× CONFIRM + 1× RESTATE; objection upheld; v0.3 + v1.1 re-fired
Grok and Copilot CONFIRM at SCRIPT-EXECUTED tier (T1(ii) leak hunt cleared; completion rule
"derived-unique"); ChatGPT RESTATE with one verdict-flipping T1(iii) objection — **upheld despite the
2–1 count**: the v1.0 energy claim outran P4's proof. Fix: **the Operational-Energy Lemma** (only
field↔matter coupling is C5 ⇒ emission = GR's quadrupole work, absorption = TT-only, bare-channel
Hamiltonian operationally empty) + **Script 4**: the eccentric ledger closes (TT flux / Peters f(e)
rate = 1.000640 at e=0.6 — no budget room for a hidden drain). All three reviewers' calibrations
applied; candidate → v0.3; T5 settled (amendment, 9, audit note 10); package → v1.1, re-dispatched.
Aggregation: `review/reviews-A3PRIME.md`. NO VERDICT MOVED.

## CYCLE CLOSED (1128) — DG-3 ROUND 2: 3/3 CONFIRM — A3′ PASSES THE PROGRAMME'S FIRST AXIOM-LEVEL REVIEW
ChatGPT withdraws its round-1 objection ("this closes my prior objection"; ledger independently
recomputed analytically: 0.999998), Grok and Copilot confirm at SCRIPT-EXECUTED. T2 unanimous
derived-unique. Final calibration applied (candidate → v0.4: "no independently operational energy
channel under C5"). Two rounds; one verdict-flipping objection raised, upheld against the vote count,
fixed with substance (lemma + Script 4), withdrawn by its author. **Registration gated only on the
architect's sign-off → single STOP-and-warn registry patch (axiom-registry.md A3→A3′, count 9 + audit
note; master_glossary.md LSP′ + DG-3 pin).** Aggregation: `review/reviews-A3PRIME.md`.

## REGISTERED (1129) — A3′ v0.4 enters axiom-registry.md with architect sign-off; **op:einstein (a) CLOSED**
The single STOP-and-warn registry patch: A3 → A3′ (count 9 + audit note 10), trajectory row (+1
d.o.f., 0 parameters), master_glossary LSP′ entry + DG-3 pin. Follow-ups queued (own warns):
frontier SR.md flip, theorem/prediction registrations, Phase 7A assembly, downstream
unconditionalizations. See `1129_registration_and_closure.md`.

## Resting state — ARC COMPLETE THROUGH REGISTRATION
Diagnostic (Steps 1–7) + Construction (Tasks 1–4) + Review (DG-3 3/3, two rounds) + Registration
(1129) all closed. The gravitational wave has its carrier.

## (superseded) Resting state — DIAGNOSTIC PHASE COMPLETE (Steps 1–7); CONSTRUCTION PHASE OPEN (Task 1 decided)
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

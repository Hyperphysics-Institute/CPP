# op:einstein Closure Arc — INDEX

**Folder:** `series_relativity/op_einstein_closure/` · **Charter:** `README.md`
**Kickoff handover:** `handovers/2026-06-11_session_156_c08_op_einstein_attack_kickoff.md`
**Status:** ATTACK OPEN — Step (b) examined (1107), cheapest kill does not fire. op:einstein NOT closed.

## Steps

| Step | Scope | Status |
|---|---|---|
| **(b)** | excess-vs-absolute \|SSV\| sourcing — cheapest kill | **1107: cheapest kill does NOT fire.** Source (b1) is pure-excess (F→0 at Δ\|SSV\|=0); uniform PSR_eff background is flat (b2, R=2(−ΩΩ''+Ω'²)/Ω⁴→0 const). Inert-Sea holds as c08 eq is written. |
| **(b′)** | rigorize the shell-sum reduction | **1108: conditionally CLOSED at leading order.** Neighbor shell = 600-cell 12-edge icosahedron = spherical 5-design: monopole Σv̂=0 exactly (absolute-\|SSV\| term annihilated), quadrupole isotropic exactly (operator = Laplacian); first anisotropy at deg 6. ⇒ shell-sum → ∇²(Δ\|SSV\|), no absolute term. Conditional on c05 (vector response) + c07 (12-edge shell). |
| **(cosmo)** | uniform-Sea cosmological/Friedmann mode | HANDOFF to SR-5 Step A/C (horizon mechanism); not a local-field-equation question. |
| **(a)** | nonlinear GR-recovery: F → R_μν − ½g_μν R | **OPEN — gap pinned (1109 + 1110).** 1109: scalar+vector LSP sources zero helicity-±2 (+,×) GW modes. 1110: audited companion 7 §6 — it ASSERTS the GR wave eq `□h̄=−16πG T/c⁴` + 'TT gauge' but its metric map sources `h_ij` from the gradient of the vector `SSV_net` (no helicity-2; TT is gauge-invariant so 'TT gauge' can't supply it); c07's own open-problems list concedes full tensor recovery unproven. ⇒ helicity-2 modes ASSERTED not derived; **gap = no spin-2 d.o.f. in the LSP**. Fork: extend LSP with a spin-2 lattice mode (the fix) **or** standing tension with observed tensor GW polarizations. NOT a falsification. |

## Patch log
- **1107** — Step (b): excess-vs-absolute check (doc + verify script + reasoning). New arc folder.
  Private-lane. op:einstein NOT closed; NO VERDICT MOVED (SR-5 D2 narrowed, not discharged).
- **1108** — Step (b′): shell-sum monopole annihilation via the icosahedral 12-edge shell (spherical
  5-design). (b)/(b′) excess-sourcing conditionally closed; cap now = just (a). New side-finding:
  deg-6 anisotropic-gravity prediction (frontier flag). op:einstein NOT closed; NO VERDICT MOVED.
- **1109** — Step (a) entry: GR-recovery summit LOCALIZED to the helicity-±2 (tensor GW) sector.
  Scalar+vector LSP sources zero helicity-2 (sympy); (a) reduces to auditing companion 7 §6's
  tensor-mode claim; falsifiable by GW polarization data. op:einstein NOT closed; NO VERDICT MOVED.
- **1110** — Step (a): audited companion 7 §6 — helicity-2 modes ASSERTED (GR wave eq + 'TT gauge'),
  NOT derived (metric map sources h_ij from gradient-of-vector; TT gauge-invariant; c07 concedes
  tensor recovery open). op:einstein (a) OPEN; gap pinned = no spin-2 d.o.f. in the LSP. Fork: spin-2
  lattice-mode extension (fix) vs tension with observed tensor GW polarizations. NO VERDICT MOVED.
- **1111** — INT frontier: recorded the (a) gap + GW-polarization tension (SR.md, CONJ.md). Pointers
  to this arc; flags the tension against c08's GW claim. No new ID. NO VERDICT MOVED.
- **1112** — opened the `spin2_construction/` sub-arc (the fix). Step 1: the missing spin-2 d.o.f. =
  the l=2 quadrupole of the 600-cell shell deformation — fully resolved + independent of l=0/l=1 on
  the icosahedral shell (rank 5, orthogonal); m=±2 = the GR +,× polarizations. Extend the LSP with a
  rank-2 Q_ij. (a) NOT closed (broadcast law + wave eq + GR-recovery remain). NO VERDICT MOVED.
- **1113** — spin-2 Step 2 (Q_ij broadcast law): PROPAGATION is native — the icosahedral shell-sum is
  rank-agnostic, so a broadcast Q_ij obeys □Q_ij=source (same operator as scalar/vector, 1108), its
  helicity-±2 part = the GW +,× modes at c; the 1112 falsifier does NOT fire. BUT the GP has no rank-2
  d.o.f. — Q_ij is a genuine foundational LSP extension (geometrically slotted by the 600-cell H_g,
  but a postulate). (a) closure localizes to one question: does the GP carry a quadrupole d.o.f.? (a)
  NOT closed. NO VERDICT MOVED.
- **1114** — spin-2 Step 3 (foundational audit): CPP's fundamental flows carry ONLY scalar+vector
  (CP→GP CSR: type/polarity/emergent-vector-spin; GP→GP: |SSV|_abs+SSV_net; GP→CP: displacement). No
  rank-2 d.o.f. anywhere; candidates (DP-sea polarization=vector, CP spin=emergent vector, H_g=slot
  but unexcited) all fail; corpus mute (only matter-side nuclear quadrupoles). VERDICT: closing (a)
  requires a NEW AXIOM (rank-2 in one of the 3 flows) — see 1115, which adds the emergent option D.
  (a) OPEN. NO VERDICT MOVED.
- **1115** — spin-2 Step 4 (run at the Einstein wall, current axioms): the SSV-vector superposition
  cannot give the LINEAR helicity-2 GW — linear ∂(V) and grad-bilinear ∂V∂V give zero; the 2nd-order
  V_iV_j (TLA's proposal) HAS helicity-2 structure but only at amp² + double frequency (not the
  observed first-order GW). Wall stands for any local polynomial in (φ,V). The EMERGENT route is
  permitted (Weinberg–Witten evaded by CPP's preferred-frame / emergent-Lorentz structure) — tested in
  1116.
- **1116** — spin-2 Step 5 (THE ASSAULT, emergent-graviton calculation): the dynamical matrix of the
  scalar+vector field on the icosahedral 600-cell lattice has 4 modes of helicity {0,0,±1} only — **NO
  helicity-±2, for ANY couplings** (helicity fixed by the scalar+vector representation; couplings set
  only dispersions). **Option D RULED OUT.** ⇒ closing op:einstein (a) / matching observed tensor GWs
  **REQUIRES a fundamental rank-2 d.o.f. — the spin-bit axiom (A/B/C) is NECESSARY.** The architect's
  granularity intuition is vindicated as the reason. Founder's-vision entry recorded. (a) OPEN pending
  the axiom choice. NO VERDICT MOVED.

## Cap status (for the CC umbrella)
Before 1107 the cap was "is the source excess or absolute?" After 1107 (Step b) the cheapest kill was
removed; after 1108 (Step b′) the shell-sum rigor is conditionally closed too — the entire
excess-sourcing / inert-Sea question is now **conditionally settled and grounded in 600-cell
symmetry**. The cap is therefore **just the nonlinear GR-recovery (a)** (+ the cosmological mode in
SR-5). The CC reconciliation's honest grade is unchanged (conditional on (a)), but the conditional is
now a single, well-posed GR-recovery problem.

After 1109, that problem is itself localized to the **helicity-±2 (tensor GW) sector**: the next pitch
is to audit **companion 7 §6** — does it produce two helicity-±2 modes from the 600-cell lattice (a
rank-2 d.o.f.), or only the helicity 0/±1 modes the scalar+vector LSP supports? That single question
decides op:einstein's (a), and it is empirically decidable (GW polarization observations).

**Resolved by 1110:** companion 7 §6 asserts (does not derive) the helicity-2 modes; op:einstein (a)
is genuinely open, gap = a missing spin-2 d.o.f.

**ARC RESTING STATE (after 1112–1114, the spin-2 construction sub-arc):** the fix is fully mapped and
the closure is now a *foundational choice*, not a derivation. (1112) the missing d.o.f. = the l=2
quadrupole, geometrically slotted by the 600-cell H_g representation; (1113) propagation is native —
the rank-agnostic shell-sum gives □Q_ij at c with helicity-±2 = the GW modes; (1114) but CPP's
fundamental flows carry only scalar+vector, so the rank-2 d.o.f. is **absent from the axioms** and must
be **added as a new axiom** (option A: CP State Register; B: LSP broadcast; C: GP→CP instruction).
CPP-as-axiomatized is a **scalar–vector theory of gravity** with a GW-polarization tension; the
cosmological-constant local half (b/b′) is unaffected.

**RESOLVED by 1116 (the emergent-graviton calculation):** option D is **ruled out**. The collective
spectrum of the scalar+vector field on the 600-cell is helicities {0,0,±1} — no spin-2, for any
couplings (representation-theoretic). The composite/bilinear route was already excluded (1115). So the
**spin-bit axiom (A/B/C) is NECESSARY** — closing op:einstein (a) and matching the observed tensor GW
polarizations requires a fundamental rank-2 d.o.f. The architect's granularity intuition is vindicated
as the reason (scalar magnitude + vector direction is representationally too poor to carry the l=2
quadrupole). This is the *normal* situation in physics (the graviton is fundamental in every working
theory of gravity); CPP joins the mainstream on this point. The remaining work is the deliberate
engineering of the axiom: which flow (A: CSR / B: LSP / C: GP→CP), its form, and the source coupling
`Q_ij ↔ T_μν`. The geometric slot (600-cell H_g, 1112) and the propagation (rank-agnostic shell-sum,
1113) are already in hand.

**RE-CONFIRMED by 1119 (the THIRD assault — the architect's non-radiality mechanism):** the PSR-hop
twist (GPs non-radial to propagation ⇒ an incremental turn per hop), formalized as the most general
discrete connection on the carried data (per-edge transports — genuinely untested by 1116, which used
scalar coupling coefficients only), **does not open a helicity-±2 channel**: rotations are
irrep-preserving (the (φ,V) space has no m=±2 content to project onto), and a data-acting twist would
Planck-gap the vector sector (`M = 4|sin(θ/2)|`; the geometric quaternionic value θ = π/5 gives
M ≈ 1.24 M_Planck) — excluded by massless long-range propagation to θ < 10⁻⁴⁶–10⁻⁵¹, forcing exactly
the flat (absolute/Nexus-frame) carriage that 1116 computed. Byproducts banked: the lattice-connection
gap + circular-birefringence laws, and the recognition that the absolute-frame axiom is load-bearing
(it is what keeps the broadcast massless). Option D is now closed after **three** independent assaults
(1115 bilinears, 1116 collective modes, 1119 connection); the spin-bit axiom stands NECESSARY on its
strongest footing.

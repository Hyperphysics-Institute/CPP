# A5-DISP RELAY COMPUTATION — THE O(kd) COEFFICIENT MATRIX VANISHES IDENTICALLY: CASE-Q

**Patch 2940 (2 Aug 2026). Executes `a5_disp_prereg.md` §4 with both
Patch 2938 binding upgrades. Verify script:
`code/2940_a5_disp_relay_symmetry.py` (stdlib, <30 s, 8 checks, all
PASS). Classification per the frozen bands of prereg §2: CASE-Q.
No experimental bound is cited or converted here; the conversion
patch follows with its own prereg per the frozen ordering.**

## §0 — Mandatory fresh reads performed (per handover 2939 §1)

(a) `Capotauro_chiral_mechanism_candidate.md` — full Reading C
structure re-read, NOT recalled: Q1' RESOLVED toward **vertex-aligned**
Reading C at Layer 2 (Finding C-W37, Patch 0419); ambient 3D residual
group is **H₃ ≅ I_h = I × ⟨P₃⟩, order 120, WITH the 3D inversion**
(Patch 0417 §9 parabolic-subgroup closure). The edge perturbation is
|e|·(1 + ε(ê·n̂)), ε = χ = φ⁻³ (§2.3). (b) THEO-SD-CHIR-1/2
derivation chain (Findings C-W40–C-W46, `frontier_sectors/SD.md` +
`FP.md`): the EM-sector coupling |M| = χ/6 is a **matrix element** of
the chirality operator Ĉ ∈ A₂ᵤ(D₅d) between matter-doublet states
{A₁g, A₂ᵤ} on the 12-vertex icosahedral cage; the ambient
(matter-free) reference configuration is chirality-NEUTRAL with full
I_h stabilizer and ⟨A_u⟩ = 0 by Schur orthogonality (Finding C-W44,
Orbital-ZBW). (c) F.1 Theorem 7.1 + building blocks: Mechanism A is
r(ê) = r₀(1 + δ(ê·n̂)); host-to-first-shell projection is UNIFORM at
û·n̂ = −1/(2φ) across all 12 links; first-shell-to-first-shell edges
satisfy **ê·n̂ = 0 exactly** (the whole cage lies in the slice
Re = φ/2).

**The handover's decision question, answered from the corpus:** the
ambient 3D residual group is **I_h with inversion** (not chiral I),
and the chirality is **matter-doublet matrix elements only, not a
bulk pseudoscalar condensate** (ambient A_u average = 0, registered
at Layer 3 in the THEO-SD-CHIR-2 chain itself). Per the handover,
this distinction decides the case — and it decides it toward CASE-Q,
by the derivation below.

## §1 — Setup

The photon is eDP-sea polarization transport via the PCD relay (SF-6
structural content only; Tier-2 tuned constants not used anywhere in
this document). Physical 3D space at a host vertex is the hyperplane
Im(ℍ) orthogonal to n̂ under vertex-aligned Reading C, with the
600-cell realized as the binary icosahedral group 2I of unit
quaternions and n̂ = (1,0,0,0) the host vertex. The two registered
breakings enter as:

- **FI-C-9 leg (spatial):** edge-length field
  L(e) = L₀(1 + ε(ê·n̂)), ε = χ = φ⁻³.
- **TARROW leg (temporal):** DI-bit rate field
  r(ê) = r₀(1 + δ(ê·n̂)) (Mechanism A).

Both are functions of the single scalar (ê·n̂) per link — this shared
functional form is the registered content of both legs and is the
load-bearing structural input.

## §2 — Three exact structural facts (each verified in the script)

**Fact 1 (perpendicularity confinement).** Every
first-shell-to-first-shell edge has ê·n̂ = 0 exactly (F.1
first-shell-perpendicularity; script C3: all 30 in-shell edges; the
12-vertex cage lies in the single slice Re = φ/2). Therefore the
in-hyperplane (transverse) relay links carry **zero** perturbation
from either leg — not small, zero. The perturbations live only on
host-to-shell links, whose projection onto n̂ is uniform at −1/(2φ)
across all 12 (script C2): any effect routed through host links is
identical on every 3D direction and renormalizes the relay
isotropically (a common clock/length rescaling carrying no 3D
directional information).

**Fact 2 (the inversion survives).** The stabilizer of the host
vertex inside the 600-cell's symmetry group has order 120 = I_h,
realized quaternionically as {v → qvq̄} ∪ {v → qv̄q̄}, q ∈ 2I (script
C4). The quaternion-conjugation element v → v̄ is in the stabilizer
and acts as the **exact 3D inversion P₃** of the physical hyperplane
(script C5). Both perturbation fields depend only on Re-components of
vertex differences, which every stabilizer element — including P₃ —
preserves exactly (script C6). Hence **the ambient perturbed medium
retains the full I_h including 3D parity, to ALL orders in ε and δ.**
This is not a perturbative statement: it is stabilizer structure.

**Fact 3 (no ambient pseudoscalar condensate).** The registered
chirality input (2938 upgrade 1) is the THEO-SD-CHIR-2 structure:
Ĉ ∈ A₂ᵤ(D₅d), magnitude χ/6, cage-shell averaging on the 12-vertex
icosahedral cage. On the AMBIENT Sea (no matter doublet occupying the
cage; the I_h-symmetric reference of Finding C-W44) the ambient
average of any A_u-type operator vanishes identically by Schur
orthogonality: Σ_{g∈I_h} det(g) = 0 (script C7/C8). The χ/6 coupling
activates only as a matrix element between matter-doublet states
(A₁g ⊗ A₂ᵤ ⊗ A₂ᵤ ⊃ A₁g allowed; the ambient channel
A₁g ⊗ A₂ᵤ ⊗ A₁g forbidden; script C8). **The Sea is chiral as a 4D
structure; its physical 3D section, as seen by the ambient EM relay,
is achiral.**

## §2′ — Fact 2′ (Equivariance Lemma; registered Patch 2944 after panel adjudication)

Let D = (V, E, {L(e)}, {r(e)}, ω_PCD) be the registered relay data
at vertex-aligned Reading C. Every component of D is I_h-invariant
(geometry: script C4; both scalar fields: script C6, lattice-wide;
ω_PCD ∥ n̂: every stabilizer element fixes n̂, in particular P₃).
Then any relay operator U defined intrinsically from D — U = F(D)
with F using no input beyond D — satisfies gUg⁻¹ = U for all
g ∈ I_h, since g·F(D) = F(g·D) = F(D). This closes, without
enumeration, the composite-structure classes raised at panel review
(ordered path products, multi-link and host-link interference,
beyond-first-shell contributions, polarization parallel transport
and holonomy): each is a function of invariant data. What the lemma
does NOT close is registered as conditions: (i) relay
intrinsicality — the SF-6 PCD rule must carry no structure external
to D (reopener R4); (ii) realized-state symmetry — the ambient Sea
must occupy an I_h-symmetric state; equivariant dynamics on a
symmetry-broken state does not inherit the zero (R1 expanded).
Operative-premise clarification: the odd-order vanishing rests on
the exact LOCAL P₃ symmetry of each admitted ambient relay state;
orientation averaging carries no proof weight for odd orders. See
`a5_disp_panel_adjudication.md` §2 for the adjudication record.

## §3 — The O(kd) coefficient matrix

Per prereg §4(ii), the output object is the 2×2 Hermitian coefficient
matrix M⁽¹⁾(k̂) over transverse polarization states at first order in
(k·d_DP), orientation-averaged over the ambient Sea. Every entry of
M⁽¹⁾ must be assembled from invariant tensors of the ambient medium's
effective symmetry group (which, after orientation averaging, is at
least the site group I_h by Fact 2), contracted with k̂ and
polarization bilinears. Channel by channel:

- **ξ₁ (polarization-averaged TOF, identity channel):** requires an
  invariant 3D vector b to form ξ₁(k̂·b). Multiplicity of the trivial
  irrep in the vector rep of I_h: (1/120)Σ tr(g) = **0** (script C7).
  ξ₁ ≡ 0.
- **γ (circular birefringence, helicity channel):** requires an
  invariant pseudoscalar (A_u condensate) or invariant pseudovector.
  (1/120)Σ det(g) = 0 and (1/120)Σ det(g)tr(g) = **0** (script
  C7/C8). γ ≡ 0.
- **Linear-birefringence channels:** require invariant odd-rank
  tensors (one k̂ index). None exist — see the general closure.

**General closure (covers all channels at once, to all orders in ε
and δ):** since the exact inversion P₃ ∈ I_h is a symmetry of the
ambient perturbed medium (Fact 2), every odd-rank invariant tensor
equals minus itself and vanishes; hence every odd power of (k·d_DP)
in the orientation-averaged dispersion matrix vanishes identically.
**M⁽¹⁾ = 0 in every channel. The leading mesh correction is
O(kd)².**

Why the T-leg cannot rescue a linear term: nonreciprocity
ω(k) ≠ ω(−k) requires a P-odd, T-odd invariant 3D vector in the
medium. sign(δ) is a 3D scalar under I_h — its vector direction n̂ is
orthogonal to the physical hyperplane, and no invariant 3D vector of
any parity exists (ξ₁ enumeration above). The temporal arrow is
present in the substrate but is directionally orthogonal to the 3D
relay; at O(kd) it decouples.

## §4 — Classification: CASE-Q

Per the frozen bands (prereg §2, §1 S3): **both breakings decoupled
from the EM relay at leading order — CASE-Q.** The naive quadratic
lattice expectation is recovered as a RESULT, with mechanism: (i)
exact perpendicularity confinement of both f(ê·n̂) fields away from
transverse relay links; (ii) intact 3D inversion in the residual I_h
(the quaternion-conjugation element); (iii) zero ambient pseudoscalar
condensate — the registered χ/6 chirality is matter-sector, not
propagation-sector. CASE-CB does **not** obtain for the ambient Sea
(γ ≡ 0); chirality-linear polarization rotation survives only as
matter-mediated optical activity inside cage-hosted doublet
structures, which is ordinary chiral-medium optics, not a mesh
effect. CASE-L does not obtain (ξ₁ ≡ 0, exactly, with registered
provenance — this is a symmetry zero, not an α1-pattern "small
because we need it small").

**Consequence per the frozen CASE-Q band:** A5-DISP proceeds as a
d_DP CEILING anchor via quadratic-order (E_QG,2-class)
time-of-flight limits. The conversion patch follows with its own
prereg citing this document's classification; no experimental number
is touched in this patch.

## §5 — Conditionality (binding, per 2938 upgrade 2) and reopeners

The CASE-Q classification inherits Mechanism-A conditionality from
BOTH legs: the spatial CAPACITY-1 verdict (V3, conditional on
Mechanism A with two named sub-conditions, one carried as not
derived) and the temporal TARROW-2 (W3→W1 conditional on Mechanism
A). It is additionally conditional on **vertex-aligned Reading C**
(Q1' resolution at Layer 2, Finding C-W37).

**Robustness to the origin question:** CASE-Q is INSENSITIVE to
primitive-vs-emergent (OPEN-CHIR-1d-β; the V2/OPEN-SM-4
matter-antimatter reopener; manifestation (v)). Propagation cares
about the present-epoch ambient medium symmetry, and under either
origin the ambient residual group is the same I_h with the same zero
A_u condensate. The 2938 addendum's operative statement is hereby
refined rather than contradicted: photons traverse a Sea that is
chiral **in 4D**; the ambient 3D section they couple to retains an
exact inversion, so S1's P-premise holds FOR THE AMBIENT EM RELAY as
a derived consequence, not as an imported assumption.

**Named reopener conditions (any one reopens this classification):**

- **R1** — a future closure delivering a nonzero ambient 3D
  pseudoscalar condensate or an I_h-breaking invariant vector in the
  ambient Sea (e.g., via manifestation (v) or a cosmological-epoch
  mechanism that tilts the ambient occupancy off the I_h-symmetric
  reference).
- **R2** — reopening of Q1' away from vertex-aligned Reading C. Under
  face-aligned n̂ the ambient residual is the order-12
  ℤ₂ × S₃, whose 3D point-group realization (D₃d with inversion vs
  D₃h without) was not adjudicated in the sketch; the symmetry
  analysis of §3 would have to be redone from scratch.
- **R3** — a demonstrated failure of Mechanism A's registered form
  r₀(1 + δ(ê·n̂)) (e.g., a rate law not expressible as a function of
  ê·n̂ per link would evade Fact 2's invariance argument).

## §6 — Ledger

Nothing moves: six of seven; PR7 PARTIAL (OPEN-K1-MEMORY-1B); B7
holds DM-1/2/3 release banners; Candidate (B) 79.5%
PROVISIONAL-FAVORABLE; 2855 Route-2 verdict PROVISIONAL with M1/M2
frozen. No value of η, d_DP, n_DP, or any experimental bound appears
in this document. Panel review of this classification precedes the
conversion patch per prereg §4(v).

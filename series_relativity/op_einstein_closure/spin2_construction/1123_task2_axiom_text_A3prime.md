# Spin-2 Task 2 — THE AXIOM TEXT (candidate v0.1): A3′, the Completed Broadcast Axiom — one scalar, one vector, one tensor; nine numbers; no fourth rung (Patch 1123)

**Sub-arc:** `series_relativity/op_einstein_closure/spin2_construction/` · **Charter:** `README.md`
· **Verify:** `code/1123_task2_completion_check.py`
**Status:** Task 2 of the construction phase. This document is the **candidate axiom text**,
drafted in the private lane for DG-3 swarm review (Task 5) and the architect's sign-off.
**The axiom registry (`axiom-registry.md`) is NOT touched by this patch** — registration is
deferred until after review and sign-off, per the kickoff handover's gate ("ships nowhere
without DG-3 review and the architect's sign-off") and the anti-collision discipline
(contested registries are touched once, with the reviewed final text, under STOP-and-warn).
**NO VERDICT MOVED.**

---

## 1. The form of the move: amendment, not addition

The registry's **A3** ("DI-bit propagation": DI-bits propagate between CPs at c = l_P/t_P) is
the broadcast axiom — and its content has already been extended once *de facto*: the c07
glossary records that the Lattice State Packet "supersedes the SR-era DI-bit broadcast by
adding the vector component needed for general relativity," yet the registry's A3 still reads
in its QM-era scalar form. The registry also has an established precedent for exactly this
situation: the **A6′ consolidation** (A6+A7+A8+A9 → one principle). Task 2 therefore proposes
the spin-bit axiom as **A3 → A3′: a consolidation amendment** that absorbs the DI-bit → LSP →
tensor ladder into one *closed* statement. Under this accounting the axiom count stays at 9.

**Honest dual accounting for DG-3:** reviewers may prefer to score the tensor clause as a new
axiom (count → 10), since it adds a genuine new degree of freedom rather than only
consolidating existing ones. The physics is identical either way; both accountings are
presented, and the registry entry will record whichever the review settles. What is *not* in
dispute: the move adds **one degree of freedom and zero parameters** (§4).

## 2. The candidate axiom text

> ### A3′ — The Completed Broadcast (Lattice State Packet) Axiom  *(candidate v0.1)*
>
> At every Absolute Moment, each Grid Point broadcasts to every GP on its PSR shell a Lattice
> State Packet whose dynamical content is the complete set of rotationally protected
> irreducible representations of the lattice point group:
>
> **LSP′ = ( x_GP, t_abs ; Φ, V_i, Q_ij )**
>
> where the dynamical components are:
> - **Φ ≡ |SSV|_abs** — scalar (icosahedral irrep **A**; l=0): sources gravitational time
>   dilation, g_tt. *(existing — the DI-bit rung)*
> - **V_i ≡ SSV_net** — vector (irrep **T₁**; l=1): sources spatial curvature and
>   gravitomagnetism, g_ij statics. *(existing — the c07 LSP rung)*
> - **Q_ij** — symmetric traceless rank-2 (irrep **H**; l=2): the radiative tensor sector.
>   *(new — the completing rung)*
>
> subject to the following clauses:
>
> **(C1) Algebraic constraint.** Q_ij = Q_ji and Q_kk = 0: exactly five components, filling
> the H slot. The lattice point group protects their five-fold degeneracy exactly (no
> fine-structure; 1120 P3).
>
> **(C2) Carriage.** All packet components are stated in the absolute (Nexus) frame; the
> per-hop transport of packet data is the identity (flat connection). [Forced empirically to
> one part in 10⁴⁶–10⁵¹: any data-acting per-hop twist Planck-gaps the broadcast — 1119.]
>
> **(C3) Dynamics.** Q_ij participates in the Perceive–Compute–Displace cycle *identically*
> to Φ and V_i: the Compute step applies the same icosahedral PSR shell-sum to all packet
> components. In the continuum limit this yields wave propagation at exactly c,
> □Q_ij = S_ij. [The shell-sum is rank-agnostic — 1113; no new dynamical law is introduced.]
>
> **(C4) Source.** S_ij = κ ∂²_t [ q_ij ], where q_ij is the **traceless second-moment
> (quadrupole) density of the local matter distribution**, assembled by the GP at the
> Perceive step from the CP positions and polarization energies (E_pol = mc²) it already
> receives, and κ is **fixed by the requirement that the same Newton constant G governing the
> scalar sector governs the tensor sector** (precise coefficient derived in Task 3; target
> κ → recovery of □h̄ = −16πG T/c⁴ in the TT sector). A static configuration has ∂²_t q_ij = 0
> and sources nothing. [No-static-double-counting — the scalar keeps Schwarzschild; 1121.]
>
> **(C5) Readout.** The GP→CP displacement instruction extends to include the strain derived
> from the local Q_ij via the metric map. *This clause is listed for completeness but is a
> derivation obligation (Task 4), not an independent axiom clause: the readout follows from
> the existing Compute→Displace machinery once the packet carries Q_ij.*

## 3. The completion theorem (why "completed" is literal — verify script)

Branching D^(l) under the icosahedral rotation group I, computed for l = 0–12 (and closed for
all l by a dimension bound): the SO(3) multiplets that descend **intact** — unsplit, hence
degeneracy-protected on the lattice — are **exactly l = 0 (→A), l = 1 (→T₁), l = 2 (→H)**.
Every l ≥ 3 splits (l=3 → T₂⊕G is the first), and *permanently* so: for l ≥ 3,
2l+1 ≥ 7 > 5 = the largest icosahedral irrep, so no higher multiplet can ever descend intact.
Therefore:

> **LSP′ = A ⊕ T₁ ⊕ H = 1 + 3 + 5 = 9 components = precisely the lattice's protected
> representation content — every protected irrep exactly once, and nothing else.**

The icosahedral irreps absent from the packet (T₂, G) are exactly those that never occur as an
intact l — they exist only as fragments of split multiplets. **The ladder terminates at rank
2. There is no fourth rung.** The axiom does not append an arbitrary component; it completes
the broadcast to the full content the geometry can carry faithfully — the structural answer to
"why was the world built this way": *the broadcast carries exactly what the lattice protects.*

## 4. Minimality, necessity, and the zero-parameter property

- **Necessary:** no smaller packet content carries helicity-±2 — three independent assaults
  closed (1115 bilinears; 1116 collective modes; 1119 the most general per-hop connection).
- **Minimal:** five components is the smallest rank-2 content (the irreducible symmetric
  traceless representation); C1 forbids surplus components.
- **Maximal/closed:** the geometry protects nothing higher (§3) — the amendment is final, not
  incremental.
- **Zero new parameters:** κ is fixed by the existing G (C4). The axiom adds a *degree of
  freedom*, not a *dial*. The zero-parameter prediction discipline of the programme is
  untouched.

## 5. Obligations incurred (the axiom's derivational debts, Tasks 3–4)

- **OB-1 (the quadrupole formula).** The far-field solution of C3+C4 must reproduce the
  Einstein quadrupole formula and □h̄_μν = −16πG T_μν/c⁴ in the TT sector, with the
  scalar-sector G and no adjustable coefficient. *(Task 3.)*
- **OB-2 (polarization suppression — the axiom's primary falsifier).** Q_ij has five
  components; only the helicity-±2 pair may radiate to the far zone at first order, or the
  axiom predicts extra GW polarizations in conflict with the multi-detector tests. The
  candidate mechanism mirrors GR's: CPP's conservation laws (CP-count conservation → mass
  conservation kills monopole-type sourcing; displacement-rule momentum conservation kills
  dipole-type) must be shown to tie the helicity-0, ±1 content of the far-zone solution to
  non-radiative source moments, exactly as ∂^μT_μν = 0 does in linearized GR. **If this
  derivation fails, A3′ as stated is falsified by existing polarization data** — the axiom
  ships with its own kill switch. *(Tasks 3–4; flagged for DG-3 as the primary attack
  surface.)*
- **OB-3 (statics untouched).** Confirm the static sector is exactly unchanged: S_ij = 0 for
  static sources by construction (C4); verify no induced static component enters via the
  readout (C5). *(Task 4.)*
- **OB-4 (no double-counting with emergent structure).** ZBW orbital spin-½ and
  configurational matter l=2 (hadrons, nuclei) are untouched: Q_ij couples to matter only via
  the C4 source assembly and the C5 strain readout. *(Task 4.)*

## 6. Falsifiers (stated at axiom level)

- **F1 — polarization content:** if OB-2 discharges, CPP predicts *pure tensor* GW
  polarization at first order (matching current data); detection of first-order
  scalar/vector GW polarization modes would falsify the discharged axiom — and failure to
  discharge OB-2 falsifies the axiom as stated.
- **F2 — propagation speed:** C3 predicts GW speed exactly c (the same shell-sum as light's
  substrate). GW170817's |c_GW/c − 1| ≲ 10⁻¹⁵ is passed by construction; any future confirmed
  deviation falsifies C3.
- **F3 — multiplet integrity:** C1 + the H-protection predict no polarization fine-structure
  or splitting-induced birefringence; this doubles as a **lattice discriminant** (a cubic
  substrate predicts 2+3 splitting — 1120).
- **F4 — dispersion:** C2 (flat carriage) predicts no helicity-dependent dispersion beyond
  the 10⁻⁴⁶-bounded twist ceiling (1119).

## 7. Path to registration (the gate, restated)

1. DG-3 swarm review of this candidate (Task 5; CONV-001 single-block dispatch), with OB-2
   flagged as the primary attack surface and the dual count-accounting (§1) put to reviewers.
2. Architect review and sign-off on the (possibly revised) text.
3. Only then: the registry patch — `axiom-registry.md` (A3 → A3′ entry, count summary, growth
   trajectory) and `master_glossary.md` (LSP′ entry) — contested files, touched once, with
   the final text, under STOP-and-warn and CONV-002 re-fetch.

**Sequencing note:** Tasks 3 (source coupling / OB-1) and 4 (GR-recovery / OB-2–OB-4) can
proceed against this candidate text *before* DG-3 dispatch — discharging OB-1 and OB-2 first
would let the swarm review the axiom together with its proofs, which is the stronger
submission. Recommended order: Task 3 → Task 4 → Task 5 (DG-3) → registration.

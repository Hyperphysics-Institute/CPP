# Spin-2 Task 3 — THE COUPLING AND THE QUADRUPOLE FORMULA: λ = 16πG/c⁴, zero new parameters — the equation c08 asserted is now derived, and Hulse–Taylor lands with nothing to tune (Patch 1124)

**Sub-arc:** `series_relativity/op_einstein_closure/spin2_construction/` · **Charter:** `README.md`
· **Verify:** `code/1124_task3_quadrupole_verification.py` · **Revises:** C4 of
`1123_task2_axiom_text_A3prime.md` (v0.1 → v0.2, changelog in that file)
**Status:** Task 3 of the construction phase. **OB-1 discharged** (waveform; luminosity
inherited, CPP-internal energy normalization → Task 4). **OB-3 discharged as a theorem.**
**OB-2 part 1 discharged** (no monopole, no dipole); part 2 (readout helicity content) →
Task 4. **NO VERDICT MOVED** (no THEO/PRED registered; results ride the candidate axiom
pending DG-3).

---

## 1. The C4 correction (v0.1 → v0.2) — caught by the derivation, and it strengthens the axiom

The v0.1 source clause read S_ij = κ ∂²_t[q_ij] with q_ij a local "quadrupole density." The
derivation exposes this as ill-formed: a density of the form ρ(x)·x_i x_j is
**origin-dependent** — it is not a legitimate local law, and no Planck-scale GP could assemble
"the binary's quadrupole" locally anyway. The correct local source is the **traceless local
stress tensor** (momentum-flux density):

> **C4 (v0.2).** S_ij = −λ T_ij^{TF}, where T_ij^{TF} is the traceless part of the local
> matter stress (momentum-flux) tensor — origin-independent, and assemblable by a GP at the
> Perceive step from the CP momentum flux it already registers — with λ fixed by the
> requirement that the same Newton constant G governing the scalar sector governs the tensor
> sector. (Derived below: λ = 16πG/c⁴.)

The quadrupole then **emerges in the far field through conservation**, exactly as in GR —
which is structurally better than v0.1 in three ways: the law is local and frame-clean; the
no-static constraint becomes a *theorem* (§3); and conservation enters the derivation chain
load-bearingly, which is precisely where OB-2 wants it.

## 2. OB-1: the coupling and the waveform (the chain, each link verified)

1. **Axiom (C3 + C4 v0.2):** □Q_ij = −λ T_ij^{TF}, propagation at c by the shell-sum.
2. **Retarded solution, far zone:** Q_ij(t, x) = (λ/4πr) ∫ T_ij^{TF}(t − r/c, x′) d³x′.
3. **The conservation identity:** ∫T_ij d³x = ½ d²M_ij/dt², where M_ij = ∫ρ x_i x_j d³x is
   the second mass moment. This identity consumes local conservation **twice** — mass and
   momentum. CPP anchors: **mass = CP-count conservation** (c07's explicit local rules: no CP
   created or destroyed at any GP; every departing CP arrives at exactly one neighbor);
   **momentum = the displacement-rule bookkeeping** (formal CPP statement assigned to Task 4
   as part of OB-2's completion). *Verified numerically on an eccentric (e = 0.6) Kepler
   binary to 6×10⁻⁷ (verify P1).*
4. **Therefore:** Q_ij(far) = (λ/8πr) M̈_ij^{TF}(t_ret).
5. **Readout convention + G-matching:** under the strain-valued convention (Q_ij enters the
   metric map as the TT strain, dimensionless — the convention Task 4 implements), matching
   the tensor sector to the *same* G that the scalar sector derived (c05) fixes

   > **λ = 16πG/c⁴** — the Einstein coupling, with **zero new parameters**.

6. **The result:** □Q_ij = −(16πG/c⁴) T_ij^{TF} and
   **h^TT_ij = (2G/c⁴r) Q̈^TT_ij(t − r/c)** — the Einstein quadrupole formula.

**The arc's origin gap closes here:** the 1110 audit's finding was that c08 *asserted* the
GR wave equation — "helicity-2 modes are ASSERTED (by writing the GR eq), NOT derived from
the LSP." That equation is now **derived**: the degree of freedom comes from the axiom
(A3′), the dynamics from the rank-agnostic shell-sum (1113), the source from local stress
(C4 v0.2), and the coefficient from G-consistency with the already-derived Newtonian sector.
Nothing in the equation is asserted any longer.

**The luminosity, inherited:** with λ fixed, the Q-sector field theory is **term-for-term
linearized GR's TT sector**. Every consistent consequence carries over as a theorem of the
isomorphism: the Einstein quadrupole luminosity P = (G/5c⁵)⟨Q⃛_ij Q⃛_ij⟩ and the Peters
orbital decay. The one CPP-internal debt: verifying that the shell-sum dynamics assigns the
field the standard energy normalization ((c⁴/32πG)-type density) — booked into Task 4
alongside the readout (it is the same calculation).

## 3. OB-3 discharged — statics, now as a theorem (verify P2)

- **(a) Perfect-fluid static matter** (stars, planets): T_ij = p δ_ij ⇒ **T^{TF} = 0
  identically**. The source never forms.
- **(b) Any bounded static system:** static ⇒ M̈_ij = 0 ⇒ ∫T_ij d³x = 0 by the identity of
  §2.3 — the **tensor virial theorem**. No far-zone radiation; residual near-zone Q from
  exotic static anisotropic stress is higher-multipole and PN-suppressed.
- **Consequence:** the scalar keeps Schwarzschild (c07/c08 exact recovery untouched); the
  spin-2 bootstrap's static double-counting hazard is structurally blocked. What v0.1 imposed
  as a filter clause, v0.2 *derives*.

## 4. OB-2 part 1 discharged — no monopole, no dipole (verify P3d)

The radiative multipole expansion of §2 begins at the quadrupole because conservation kills
everything below it: **mass conservation** (CP-count) makes the monopole moment
non-radiative (Ṁ = 0); **momentum conservation** makes the dipole non-radiative (D̈ = Ṗ_total
= 0 in the CM frame). Two consequences worth stating loudly:

- The **absence of dipole gravitational radiation** in binary-pulsar timing — which excludes
  generic scalar–vector gravities and is one of the four evidential legs of the
  justification preamble — is now a **consequence of A3′ + conservation**, not an input.
- What remains of OB-2 (part 2, Task 4): the helicity-0, ±1 content of the *propagating
  five-component* Q field — show the C5 readout's differential strain response is TT-only
  (the GR-side analog: non-TT components carry no 1/r curvature). This is the axiom's
  remaining kill switch and the heart of Task 4.

## 5. The observables, with nothing to tune (verify P3)

| Test | Prediction (λ = 16πG/c⁴, scalar-sector G) | Record |
|---|---|---|
| PSR B1913+16 (Hulse–Taylor) orbital decay | Ṗ_b = −2.4031×10⁻¹² | observed/GR = 0.9983 ± 0.0016 over ~5 decades |
| PSR J0737-3039 (double pulsar) orbital decay | Ṗ_b = −1.2483×10⁻¹² | observed/GR = 0.999963 ± 0.000063 |
| GW150914-class strain (2×30 M☉, 410 Mpc, 100 Hz) | h ~ 3×10⁻²¹ (order) | h ~ 10⁻²¹ observed |
| Dipole GW emission | none (conservation) | none observed (pulsar timing) |
| GW speed | exactly c (shell-sum) | \|c_GW/c − 1\| ≲ 10⁻¹⁵ (GW170817) |

Every line follows from the candidate axiom with the scalar sector's G and **no adjustable
coefficient anywhere** — the programme's zero-parameter discipline holds through its first
axiom-level extension.

## 6. State of the obligations and the path

| Obligation | Status |
|---|---|
| OB-1 (quadrupole formula) | **DISCHARGED** (waveform derived; luminosity inherited; energy normalization → Task 4) |
| OB-2 (polarization suppression) | **Part 1 DISCHARGED** (no monopole/dipole); part 2 (readout helicity content) → Task 4 |
| OB-3 (statics untouched) | **DISCHARGED as theorem** (T^{TF} = 0 for perfect fluids; tensor virial for all bounded statics) |
| OB-4 (no emergent double-counting) | Task 4 (with the readout) |

**Next: Task 4 — the GR-recovery assembly:** the C5 readout (metric-map extension), the
TT-only differential strain response (OB-2 part 2 — the kill switch), the field energy
normalization (closing OB-1's last debt), and OB-4. Then the DG-3 dispatch (Task 5) carries
the axiom *with* its proofs.

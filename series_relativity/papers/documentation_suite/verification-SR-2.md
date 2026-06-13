# Verification — SR-2: The Spin-Bit Axiom

Verification record for the spin-2 / `op:einstein` (a) arc. Unlike single-script papers, SR-2's
computational backing is distributed across the arc's per-step scripts (committed under
`../../op_einstein_closure/spin2_construction/code/` and `../../op_einstein_closure/`), each run at
its originating patch and registered with its theorem. This file is the catalogue; it explains what
each script verifies and why the distributed layout (rather than one `*_numerics.py`) is correct
here — the result is a necessity proof plus a construction, not a single numeric closure.

> Note on the H6 publication-audit advisory. `scripts/publication_audit.sh SR-2` emits a `[warn]`
> that no `*sr2*numeric*.py` exists. This is expected and not a defect: SR-2's verification lives in
> the arc scripts catalogued below, each tied to a registered theorem. The `[warn]` is advisory, not
> a `[FAIL]`.

## Necessity proof (§3) — the three assaults

1. **Helicity content of the scalar+vector substrate** (assaults 1–2).
   Verifies the dynamical matrix of the scalar+vector field on the 600-cell has long-wavelength
   modes of helicity {0, 0, ±1} only — no helicity-±2 for any icosahedral nearest-neighbour
   couplings; amplitude/gradient bilinears excluded (helicity-2 appears only at 2nd order in
   amplitude and double frequency). Origin: Patches 1115–1116.
2. **Per-edge connection (the non-radial twist)** (assault 3).
   Verifies (i) the representation bound — overlap of the carried-data character (2 + 2cos α) with
   the helicity-±2 character is exactly zero (to 1e-16 across the equivariant family and 200 random
   antipodal-consistent SO(3) connections); (ii) the Planck-scale gap M = 4|sin(θ/2)|; (iii) the
   empirical exclusion θ < 1e-46–1e-51. Origin: Patch 1119.

## The geometric seat (§4)

3. **`1123_task2_completion_check.py`** — verifies the icosahedral shell resolves the five l=2
   functions at rank 5, l=2 ⊥ l=0,1 on the shell (max overlap ≈ 9e-17, a spherical-5-design
   property), and the branching `D^(l)` under the icosahedral rotation group: l = {0,1,2} descend
   intact (A, T₁, H); l ≥ 3 split permanently. **Backs THEO-SR-EIN-1 (Completion Theorem).**

## The quadrupole formula (§6)

4. **`1124_task3_quadrupole_verification.py`** — verifies the conservation identity
   ∫T_ij d³x = ½ d²M_ij/dt² on an eccentric (e=0.6) Kepler binary to 6e-7; the statics theorem
   (T^{TF} = 0 for perfect fluids; ∫T_ij = 0 for bounded statics). **Backs THEO-SR-EIN-2 (Statics).**

## Response and energy (§7)

5. **`1125_task4_tt_response_energy.py`** — verifies the tidal response R_{i0j0} depends only on the
   two TT combinations (symbolic + counting); the six-mode armed-trap test (breathing/longitudinal/
   vector responses ≤ 4e-11 of tensor; counterfactual τ=0 gives O(1) violation, 2.6e-2 for e=0.6).
   **Backs THEO-SR-EIN-3 (TT-Response / Cancellation).**
6. **`1127_eccentric_energy_ledger.py`** — integrates the TT Isaacson flux over the sphere and
   compares to Peters' eccentric-enhanced rate (f(0.6) = 10.2279): ratio **1.000640 (grid)**;
   independent analytic recompute **0.999998**; circular-orbit flux 1.000246. **Backs
   THEO-SR-EIN-4 (Operational-Energy Lemma).**

## Figures

7. **`../../notebooks/SR-2_figures.py`** — regenerates the four figures (SVG + PDF) and re-runs the
   ledger check inline (reproduces 0.999998). Outputs to `../../figures/figures-SR-2/`.

## Compile

`pdflatex ×3 + bibtex` on `../SR-2_spin_bit_axiom_quadrupole_formula.tex`: clean (rc=0 throughout,
no undefined references or citations, all cited entries resolved from the central `bibliography/cpp_references.bib`, 19 pages).
Confirmed at the H6 publication audit (Patch 1144).

## Numbers that must stay synchronised (H3)

| Quantity | Value | Appears in |
|---|---|---|
| eccentric flux/Peters (grid) | 1.000640 | paper §7, theorem-registry THEO-SR-EIN-4 |
| eccentric flux/Peters (analytic) | 0.999998 | paper §7, theorem-registry THEO-SR-EIN-4 |
| circular flux/Einstein | 1.000246 | paper §7 |
| Hulse–Taylor Ṗ_b | −2.4031×10⁻¹² | paper §6 (Table) |
| double pulsar Ṗ_b | −1.2483×10⁻¹² | paper §6 (Table) |
| coupling | λ = 16πG/c⁴ | paper §5 (C4), §6 (boxed) |

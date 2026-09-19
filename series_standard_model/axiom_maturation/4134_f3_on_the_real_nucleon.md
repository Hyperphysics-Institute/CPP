# F3 on the Corpus's OWN Nucleon — the 4133 Sketch Withdrawn, and What Replaces It

**Patch:** 4134. **Lane:** EW/SS. **Session:** 234.
**Discharges:** TODO-4133-F3CALC steps 1–2 (step 3, the bracelet, is not run here).
**Verify:** `series_standard_model/code/4134_f3_nucleon_cage.py` (all checks printed).

---

## 0. Self-correction first: the 4133 sketch does not apply to the nucleon

Patch 4133 §3 offered a structural observation, explicitly labelled *stated, not yet tested*:

> under point inversion through the cage centre a polar V goes to −V and an axial A to +A, so
> any cage configuration that is inversion-symmetric — spins included — has b(−r) = −b(r) and
> the shell sum cancels pairwise.

Tested, it fails on the corpus's own object. **The nucleon is not an inversion-symmetric cage.**
SS-2 states it plainly:

> *"The proton occupies a single tetrahedral cell of the 600-cell lattice. V₁(−): up quark 1;
> V₂(−): up quark 2; V₃(+): down quark; V₄(+): open (nuclear binding site)."*

A regular tetrahedron admits **no inversion at all** (C1: T_d contains no i). Its achirality is
carried by a **mirror**, not by a centre. And the actual charge-bearing set is three vertices,
not four — the fourth is open. So the premise the 4133 observation needed is absent, and the
observation is **withdrawn as applied to the nucleon**.

This is the Session 233 method warning firing again, one patch later and on my own work:
*tested on a generic configuration rather than the corpus's own object.* The 4133 text said
inversion because the objects in view were the icosahedral 12-shell and dodecahedral 20-shell,
which **are** centrally symmetric — and those are not what the nucleon is made of. I carried a
premise across two different geometric objects without checking which one the nucleon uses.

**What is NOT damaged.** Patch 4101's antipodal-pairing derivation is about the **z = 12
coordination shell** — the icosahedron of bond directions around a single vertex — which is
antipodally paired 12/12 (C2). That is a different object from the tetrahedral **cell** the
nucleon occupies, and 4101 stands untouched. The conflation was 4133's, not 4101's.

## 1. What F3 actually asks under the amendment

The amendment's bit is **b ~ A·V**: one number per CP per Moment, A the axial channel (the CP's
spin axis), V = SSV_net, the GP's summed polar vector — *"every CP executes one Displace step
per its GP's computed SSV_net"* (`master_glossary.md`). That is the founder's GP-summation
picture (4109, re-confirmed 4133). So the per-arc bit-counting of 4101 is not the computation
the amendment calls for; the quantity is

$$ B_{tot} \;=\; \sum_i \mathbf{A}_i \cdot \mathbf{V}_i $$

and F3 asks whether it vanishes for a confined structure to the ~10⁻⁷ hadronic PV bound.

## 2. The computation, on the real proton

**Geometry (SS-2, distortion ε = 1.94):** u–u = 1.071 fm, u–d = 0.620 fm. The triangle closes
(C3). Charges +2/3, +2/3, −1/3; the down's captured −eCP *"oscillates linearly through the
central +qCP"* — radially, so it stays in the same plane. **Three charge-bearing points are
coplanar by construction**, and the configuration's own mirror is that plane (C3, det = −1).

**Result 1 — V is in the plane, for any radial law.** Checked at 1/r², 1/r and linear: the
out-of-plane component is identically zero (C4). Nothing here depends on the force law, only on
equivariance.

**Result 2 — the whole pseudoscalar collapses to one dot product.** With the constituent spins
along a common axis **n** (spin projections s_i = ±1),

$$ B_{tot} \;=\; \mathbf{n}\cdot\mathbf{W}, \qquad \mathbf{W} \;=\; \sum_i s_i \mathbf{V}_i $$

and **W lies in the quark plane**. So B_tot is **exactly zero** for a spin axis perpendicular to
that plane, and O(1) for a spin axis along W (C5).

**Result 3 — and this is the one worth keeping.** W = 0 **exactly** whenever the constituent
spins are all parallel, for a reason that is a theorem rather than an accident: the V_i are
pairwise action–reaction terms, so Σ_i V_i = 0 identically, and W = s·ΣV = 0 when every s_i is
equal. Enumerated over all eight ±1 assignments, W vanishes for exactly the two all-parallel
ones (C6b). **The SU(6) proton is not all-parallel** (u↑u↑d↓ — the assignment A3G-7 used at
4126), so W ≠ 0 in the cage frame: |W| = 1.17 in these units.

**Result 4 — what saves F3 is L = 0, and it saves it on average, not pointwise.** The nucleon
ground state is an s-wave: the internal frame is isotropically distributed relative to the spin
axis. Averaged over 200 000 isotropic cage orientations, ⟨n·W⟩ = −1.4×10⁻⁴ against an s.e.m. of
1.5×10⁻³ — consistent with exactly zero, as rotational invariance requires (C8). But the **rms
per nucleon is 0.67**: the cancellation is an average over orientations, not a pointwise
algebraic one like 4101's.

## 3. The new named requirement

> **R-F3-ISO.** A confined structure's internal frame must be uncorrelated with its spin axis to
> better than ~10⁻⁷. Equivalently: no spin–orientation correlation may survive in the ground
> state.

A residual correlation ε leaves B_tot ≈ ε·|W| ≈ 1.17 ε, so the ~10⁻⁷ hadronic PV bound caps
ε ≲ 10⁻⁷ — the same shape as 4101's antipodal-imbalance cap, reached by a different route.

**For nucleon ground states R-F3-ISO is guaranteed by L = 0**, and that is a real consilience
rather than a restatement: the *same* L = 0 that made ⟨L̂⟩ = 0 at 4126 — putting 100% of the
magnetic moment in the spin term, which is why A3G-7 could be computed at all — is what makes
⟨n·W⟩ = 0 here. One property of the ground state is doing both jobs.

**What is not guaranteed, and is the live risk:** the amendment introduces A_i as a *broadcast
channel*, so an A-dependent term in the dynamics could itself induce a spin–orientation
correlation — precisely the ε that R-F3-ISO bounds. That would not be a small correction to F3;
it would be F3's failure mode. It is also adjacent to TODO-4124-QUADRATIC, which flags that a
response quadratic in b is T-even and excluded by nothing yet on file. Filed as
**TODO-4134-SPINORIENT**.

**Excited states and L ≠ 0 are not covered by this argument at all**, and the corpus has no
statement that they should be. Filed with the above.

## 4. PD-008 — the convenient branch, marked

The convenient result would have been a pointwise algebraic cancellation on the nucleon,
matching 4101's strength and leaving nothing owed. **It is not available**: the tetrahedral cell
has no inversion, no ±1 spin assignment other than the all-parallel ones kills W, and the SU(6)
proton is not all-parallel. What I have instead is an orientation average plus a named,
falsifiable requirement. I state that as the weaker result it is, and the next window should
check whether an L = 0 argument really is enough to carry a 10⁻⁷ bound, or whether it merely
moves the burden onto the s-wave's exactness.

## 5. Status

F3: still **open**, and better characterised — it now rests on R-F3-ISO rather than on R-F3
(closed at 4133 as a founder question). No verdict moved. χ₄ remains provisionally adopted.
F5 remains the blocker. **TODO-4133-F3CALC step 3 (the W bracelet on the same footing) is NOT
run here and remains owed** — until it is, the argument has not shown why the bracelet's
response is handed while the cage's is not.

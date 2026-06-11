# Spin-2 Step 1 — the missing d.o.f. is the l=2 quadrupole of the shell (Patch 1112)

**Sub-arc:** `series_relativity/op_einstein_closure/spin2_construction/` · **Charter:** `README.md`
· **Verify:** `code/1112_step1_l2_shell_mode.py`
**Result:** the missing spin-2 degree of freedom is concretely identified and grounded — the **l=2
quadrupole moment of the local 600-cell shell deformation**, fully and independently supported by the
icosahedral neighbor shell, with its m=±2 part equal to the helicity-±2 GW polarizations. **op:einstein
(a) NOT closed** — this identifies the d.o.f. and the path; the broadcast law + wave equation + GR
recovery remain. **NO VERDICT MOVED.**

## The reasoning
The (a) gap (1109–1110) is that the LSP's l=0 (scalar `|SSV|_abs`) + l=1 (vector `SSV_net`) content
cannot source the helicity-±2 GW modes. In an angular-momentum decomposition of a field on the local
shell, the helicity-±2 modes live at **l=2** (the quadrupole). So the natural fix is a quadrupole
broadcast — *if* the 600-cell shell supports an independent l=2 mode.

## What was checked (`code/1112_step1_l2_shell_mode.py`)
On the 12-vertex icosahedral neighbor shell (the c07/c08 12-edge set):
1. **Full resolution.** The five l=2 functions `{xy, yz, zx, x²−y², 2z²−x²−y²}` sampled at the 12
   vertices have **rank 5** — the shell resolves the entire quadrupole, no degeneracy.
2. **Independence.** l=2 is **orthogonal to l=0 and l=1** on the shell (max overlap ≈ 9×10⁻¹⁷). It is a
   genuinely new degree of freedom, not a combination of the existing scalar + vector — a consequence
   of the shell being a spherical 5-design (1108): moments through degree 5 behave as on the sphere.
3. **Helicity content.** The m=±2 components `{x²−y², xy}` are precisely the transverse-plane
   quadrupole = the GR `+` (`h_xx−h_yy`) and `×` (`h_xy`) polarizations. The m=0 (`2z²−x²−y²`,
   longitudinal) and m=±1 (`xz, yz`, shear) components are the helicity-0/±1 modes the LSP already
   carries — so the quadrupole adds **exactly** the two missing helicity-2 modes and nothing
   redundant.

## Conclusion
**Extend the LSP** from `(|SSV|_abs : l=0, SSV_net : l=1)` to include a symmetric traceless rank-2
broadcast `Q_ij` (l=2), realized as the quadrupolar deformation of the local icosahedral shell. The
600-cell supports this natively; its m=±2 part supplies the helicity-±2 GW polarizations that are
currently unsourced. This converts "op:einstein (a) is open" into a concrete construction with the
degree of freedom fixed and grounded.

## What remains (the substantial effort)
The broadcast law for `Q_ij` in the PCD cycle; its wave equation `□Q_ij = source` and the check that it
gives two helicity-±2 modes at c matching `□h̄_μν = −16πG T_μν/c⁴` + the quadrupole formula; the full
GR-recovery `G_μν = 8πG T_μν/c⁴` from the extended (scalar+vector+tensor) map; and confrontation with
the observed tensor GW polarizations. These are Steps 2–5 (see `README.md`). Until then, op:einstein (a)
remains open and the GW-polarization tension stands — but the path is now concrete.

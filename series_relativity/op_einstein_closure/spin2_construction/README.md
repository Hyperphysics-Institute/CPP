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
3. **(the crux) Is a GP quadrupole d.o.f. independently motivated?** — examine the DP-sea polarization
   tensor, the CP 'spin state' (c07), and whether the PCD dynamics physically excite the H_g (l=2) mode.
   If yes, (a) closes without a new postulate; if not, closing (a) is an explicit axiom extension.
   (The wave equation itself is settled by 1113: `□Q_ij` from the rank-agnostic shell-sum.)
4. **GR-recovery** — show the extended (scalar+vector+tensor) metric map assembles into the full
   `G_μν = 8πG T_μν/c⁴` (this is the actual closure of op:einstein (a)).
5. **Confront GW data** — recover the observed tensor polarizations; re-examine c08's claim that
   scalar/vector modes are suppressed by `(l_P/λ)²` (now with the tensor modes genuinely present).

## Falsifier / on-success
- **Falsifier:** if the 600-cell broadcast structure cannot carry a propagating l=2 quadrupole (e.g.
  the PCD cycle has no quadrupole channel, or it cannot propagate at c), the spin-2 sector cannot be
  built within CPP's current axioms, and the GW-polarization tension becomes structural.
- **On success:** op:einstein (a) closes; the dark-sector cap is removed; the CC reconciliation
  becomes an unconditional theorem; CPP reproduces the observed tensor GW polarizations.

## INDEX
Step log lives in the parent `../INDEX.md` (op:einstein arc). Step 1 = this patch (1112).

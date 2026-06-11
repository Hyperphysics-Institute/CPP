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

## Resting state
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

# Spin-2 Step 2 — the Q_ij broadcast law: propagation is native, the d.o.f. is a postulate (Patch 1113)

**Sub-arc:** `series_relativity/op_einstein_closure/spin2_construction/` · **Charter:** `README.md`
· **Verify:** `code/1113_step2_broadcast_rank_agnostic.py`
**Result:** the "broadcast law" splits cleanly. **(i) Propagation is native** — the PCD icosahedral
shell-sum is rank-agnostic, so a broadcast quadrupole `Q_ij` automatically obeys `□Q_ij = source`,
the same wave operator as `|SSV|_abs`/`SSV_net`, and its helicity-±2 part propagates at c as the GW
`+`/`×` modes. **(ii) But the Grid Point has no quadrupole d.o.f. to broadcast** — the LSP is
scalar + vector, and `Q_ij` is a genuine new foundational degree of freedom (geometrically slotted by
the 600-cell H_g/l=2 rep, but a postulate). **op:einstein (a) NOT closed; the closure is localized to
one foundational question. NO VERDICT MOVED.**

## (i) Does the PCD shell-sum propagate a rank-2 field?  — YES
The icosahedral 12-edge shell-sum acts **component-wise** on whatever field a Grid Point broadcasts.
From 1108, `Σ v̂_i v̂_j = 4·I` (isotropic), so the discrete shell-Laplacian `L f(0) = Σ_shell[f(v)−f(0)]`
becomes `∝ ∇²f` in the continuum — and this is **rank-agnostic**: it sees the *components*, not the
tensor rank. Therefore, **if** a GP carries `Q_ij` and broadcasts it through the PCD cycle, the
Perceive–Compute step yields `□Q_ij = source` — the *identical* wave operator that 1108 derived for
the scalar and vector. A massless symmetric-traceless `Q_ij` has helicity-±2 polarizations
`{Q_xx−Q_yy, Q_xy}` that are both traceless and transverse (verified), so with `□Q=0` they propagate
at speed c. **The helicity-±2 GW polarizations are exactly the propagating part of `Q_ij`, carried by
the existing shell-sum machinery.** The 1112 falsifier ("the substrate can't carry / propagate a
quadrupole at c") therefore **does not fire** — propagation is free once the d.o.f. exists.

## (ii) Does the Grid Point have a quadrupole d.o.f. to broadcast?  — NO (and this is the whole gap)
The LSP is `(x_GP, t_abs, |SSV|_abs, SSV_net)`: field content = one scalar + one vector. A point's
state has no rank-2 part. The helicity-±2 modes require a symmetric-traceless `Q_ij` (5 components) at
the GP — a "shape" or **quadrupolar polarizability** — and 1109 already showed it cannot be
manufactured from the vector's gradient (`∂_(i V_j)` has zero helicity-2 for a plane wave). So `Q_ij`
is a **genuinely new degree of freedom**, not derivable from the existing scalar+vector substrate. The
600-cell's H_g (l=2) representation is the *geometric slot* that can hold it (1112), but **carrying it
is a foundational extension of the LSP**, i.e. a postulate.

## Honest conclusion
Step 2 localizes the entire `op:einstein` (a) closure to **one foundational question:** *does the Grid
Point carry an independent quadrupole degree of freedom `Q_ij`?*
- **If yes** (postulated or independently motivated): the rest is essentially in hand — the shell-sum
  propagates it (`□Q_ij`), its helicity-±2 part is the GW radiation, and what remains is the source
  coupling `Q_ij ↔ T_μν` (the quadrupole formula) and the full tensor GR-recovery.
- **If the substrate genuinely has only scalar + vector**: CPP cannot contain gravity's tensor sector,
  and the GW-polarization tension (1110–1111) is **structural**, not a missing derivation.

This is the honest middle ground between "native to the 600-cell" and "the substrate can't carry it":
the **propagation machinery is native** (the shell-sum is rank-agnostic), but the **degree of freedom
is not** (it must be added to the LSP). Closing (a) means **postulating a spin-2 Grid-Point d.o.f.** —
geometrically slotted by the 600-cell, but a genuine addition to CPP's foundational axioms. That is a
significant, clarifying statement about the programme's architecture: as currently axiomatized, CPP's
substrate carries scalar+vector gravity; the graviton-analog (the l=2 shape mode) is not contained in
it, though the lattice has exactly the right slot for it.

## What remains
- **Step 3 (the real foundational question):** is there *independent* CPP motivation for a GP
  quadrupole d.o.f.? Candidates to examine: the DP-sea polarization tensor; the CP "spin state"
  (c07 notes spin is a CP property); whether the H_g (l=2) shell mode is physically excited by the
  PCD dynamics rather than merely available. If one of these *is* a quadrupole d.o.f., (a) closes
  without a new postulate; if not, closing (a) is an explicit axiom extension.
- **Steps 4–5:** source coupling `Q_ij ↔ T_μν` (quadrupole formula) and full GR-recovery; confront the
  observed tensor GW polarizations and re-assess c08's `(l_P/λ)²` suppression claim.

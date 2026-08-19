# Development log — spin-III (600-cell Voronoi ZBW eigenvalues)

## Session 149, 19 Aug 2026 — from "never written" to v1.0 in one arc

**Vignette 1 — the discovery that the paper didn't exist.** The spin-arc
reorganization (Patch 3233) surfaced a full-history finding: Spin III had
never been written. The folder held data, figures, notebooks, and March-2026
development notes — but no .tex had ever existed in git history. The interim
draft (Patch 3234) was assembled from those materials plus fresh work, and
its most consequential act was honesty: the committed March lattice
computation had solved the WRONG problem (closed resonator — the CP-Exclusion
node was never encoded), so the draft diagnosed its own instrument, froze a
corrected one with verdict rules declared before data existed, and put the
domain question (24-cell vs true Voronoi cell) to the founder as A1.

**Vignette 2 — the ruling and the measurement.** The founder ruled A1 the
same session: the 24-cell carried no physical-picture weight; use the true
cell. The geometry pinned exactly (600-cell dual = 120-cell ⇒ regular
dodecahedron). Designing the corrected instrument surfaced a second trap —
ψ-Neumann is not Spin II's u-Neumann — closed by discretizing the u-equation
directly. Sphere control validated the instrument to five decimals; the true
cell returned the frozen verdict MODE2-RECOVERED at both densities (node
0.6670 vs 2/3; spectrum −0.31%) (Patch 3236).

**Vignette 3 — the analytic leg.** The founder said "proceed" and the
symmetry argument turned out crisp: exact character arithmetic (m_l = 0 for
l = 1..5), the Selection Theorem (first invariant anisotropy channel at
kR = 8.211 > 3π/2 — the lattice must choose Mode 2, with the eight global
interlopers identified as exactly the l=1⊕l=2 multiplets matching the
measured indices), and the Protection Theorem (O(ε₆²) positions; predicted
0.0026 vs measured 0.0031, neither leg knowing the other's number) (Patch
3238). OPEN-QM-8 moved to SUBSTANTIALLY RESOLVED.

**Vignette 4 — the panel and the ship.** CONV-026 (bundled with GR-1)
returned Q5 4–1 VALID with the gap confirmed by three independent routes,
Q8 3–2 RATIFY; four calibrations applied at V0.3 (Patches 3240–3245).
v1.0 SHIPPED at Patch 3248 under the paper production protocol. Deposit
awaits the SPIN-N naming confirmation and the Zenodo test run.

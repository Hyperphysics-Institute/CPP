# **D-ENTITY-1 RETURNED DEGENERATE — the frozen thresholds sat ABOVE the lattice spacing, so the graph was fully connected BY CONSTRUCTION and N_clus = 1 identically at every temperature.** The run measured the lattice, not the physics. **The design error is the worker's**, it was caught by the data within one run, and the correction is frozen here: **sub-lattice thresholds (0.5, 0.7, 0.9 × d_s) plus a PERCOLATION GUARD that voids any threshold whose mean aggregate spans more than half the DPs**

**Patch 3418 (23 Aug 2026). DM/DE block. Corrective; the 3416 prereg
otherwise stands unaltered.**

## §1 — The result and its diagnosis

VideoCPU returned **N_clus = 1.00–1.10 at all four temperatures and
all three thresholds.** With d_s = 4.636, the frozen thresholds were
5.563, 6.954 and 9.272 — **every one ABOVE the nearest-neighbour
spacing.** Any threshold exceeding the lattice spacing connects every
DP to its neighbours, so the component graph percolates and the count
is 1 by construction, independent of temperature and of any physics.

**The observable was measuring the lattice.** No reading is issued;
the frozen §4 branches do not apply because the input was degenerate.

## §2 — What went wrong in the design, owned

3416 §3 anticipated that r_clus was "a free choice [that] could
manufacture any answer" and guarded it by requiring **sign agreement
across thresholds**. That guard is real but insufficient: **it
protects against a threshold-dependent answer, not against all
thresholds being jointly degenerate.** The worker chose 1.2–2.0 × d_s
without checking them against the lattice spacing — **an error a
single line of arithmetic would have caught before the run**, and the
same class of oversight as the 3198 CV benchmark (a statistic applied
outside its valid regime).

## §3 — The correction, frozen

1. **Sub-lattice thresholds: r_clus ∈ {0.5, 0.7, 0.9} × d_s** — all
   BELOW the nearest-neighbour spacing, so an "aggregate" means DPs
   drawn closer together than the lattice baseline, which is what
   clumping physically is.
2. **PERCOLATION GUARD (new, frozen):** any threshold whose mean
   aggregate size exceeds 50% of the total DP count is **VOIDED** and
   carries no reading; if all three void, the verdict is
   **DEGENERATE/PERCOLATED** and no p is quoted.
3. Everything else in 3416 stands: the sign-agreement requirement,
   the frozen readings, the blind pre-declaration
   (QUINTESSENCE-SIDE), and §6's limits.

**Instrument change verified additive**: all pre-existing output keys
bit-identical with the probe enabled.

## §4 — Status

**Worker's pre-declaration is NOT yet scored** — the run produced no
admissible reading, so the QUINTESSENCE-SIDE declaration stands
pending the corrected run. Eight pre-declarations, two correct, one
outstanding.

Nothing here touches Λ, d_s^emp, the ledger, DISP-I3, or any DM
quantity. Kila6's β-ladder outranks all of it.

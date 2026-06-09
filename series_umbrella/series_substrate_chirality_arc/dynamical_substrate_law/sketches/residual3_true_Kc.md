# Residual 3: the True K_c (Exact Margin) — Wider than the Mean-Field Lower Bound

**Patch:** 0823 (Session 156, 8 June 2026) · **Type:** infrastructure result (chirality residual 3) · **Lane:** F.1 / `dynamical_substrate_law/` (verdict stays chirality-lane / DG-3).
**Answers:** chirality-lane residual 3 — replace the mean-field `K_c = 1/12` *lower bound* with the true critical coupling, making the primitive margin exact. **Verify:** `code/0823_residual3_true_Kc.py`. **Predecessors:** 0821 (residual 1), 0822 (residual 2).

---

## Result

The relevant order parameter for *emergent* chirality is the **uniform** ⟨η⟩ — a net global handedness (the `sign(n̂)` / det-coset condensation). Its condensation threshold is the **ferromagnetic** `K_c` of the η-model on the 600-cell. Computed three ways (verify 0823):

| estimate | value | note |
|---|---|---|
| mean-field `1/λ_max` | 0.0833 | the lower bound used through 0818–0822 |
| Bethe–Peierls `atanh(1/(z−1))` | 0.0912 | better estimate for `z=12` |
| finite-N Monte Carlo (susceptibility peak) | ≈ 0.100 | direct, on the actual 600-cell graph |

All three exceed the mean-field lower bound, as fluctuations require. **At `K_lift ≈ 0.053` the model is plainly disordered:** `⟨|m|⟩ ≈ 0.12` (finite-size residual, small) and `χ ≈ 0.94` — far below the susceptibility peak (≈ 5.3 near `K_c`).

**Exact margin:** with the true `K_c ≈ 0.091–0.100`, `K_lift/K_c ≈ 0.53–0.58`, so the primitive margin is **≈ 42–47%** — wider than the **36%** mean-field lower bound, exactly as anticipated. The uniform (net-handedness) mode does not condense at `K_lift`.

## Two reinforcing points

1. **The antiferromagnetic sign suppresses the relevant mode further.** The measured coupling is AFM (`C_nn < 0`), so the uniform-mode susceptibility is `χ_uniform = 1 + 12·C_nn ≈ 0.36 < 1` — actively *suppressed*, not merely sub-critical. A staggered mode (the AFM order) is not a net global handedness (not V1) and is frustrated by the 600-cell's odd cycles. So the AFM structure is intrinsically primitive-favoring. *(The AFM sign is somewhat convention-dependent — 0820 — so this is reinforcing, not load-bearing; the load-bearing fact is `K_lift < K_c` either way.)*

2. **Finite-system note.** The cosmological substrate is the extended tiling, so the thermodynamic `K_c` (estimated here by Bethe + a finite-N proxy on one 600-cell) is the relevant threshold; the precise extended-lattice value is a refinement that can only raise `K_c` above mean-field — i.e. only widens the margin.

## Where the season stands — all three residuals closed

- **Residual 1 (decisive): closed** (0821) — short-range coupling; no candidate η-mode orders.
- **Residual 2 (current completeness): closed** (0822) — O(δ³) current divergence-free, O(δ⁶)-suppressed at the physical bias.
- **Residual 3 (true K_c): closed** (this patch) — true `K_c ≈ 0.09–0.10`; exact margin **≈ 42–47%**, wider than the lower bound; AFM suppresses the relevant mode further.

The DG-3 input package (0907 §4) is now complete: derived `K_lift` with regime (0819–0821), the comparison at **true** `K_c` with the exact margin (this patch), the current-completeness check (0822), and the standing Mechanism-A conditionality. **None of the three residuals required the PCD layer.** The CAPACITY-1 verdict and the DG-3 swarm review are the chirality lane's.

## Scope held

Infrastructure (true `K_c` + exact margin). **No verdict moved** (V3/V1 stays chirality-lane, DG-3). No THEO, no ID, no CHIR.md / verdict-registry edits. Finite-N and AFM-convention caveats stated. Conditional on Mechanism A (OPEN-FP-F1-2).

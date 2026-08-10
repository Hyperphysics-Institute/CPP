# REPRODUCIBILITY NOTE — THE η/c_geo VERIFY SCRIPTS (THE CONV-013 AUX-1 [COP] ITEM)

**Patch 3038. Scope: the three scripts carrying the OPEN-QMRG-ETA
evidence. Everything needed for an exact rerun is on this page.**

**Environment.** Python 3 with NumPy only (no other dependencies).
Reference environment at this patch: Python 3.12.3, NumPy 2.4.4,
Linux x86_64. All three scripts are pure-NumPy bookkeeping
simulations; no BLAS-order or platform sensitivity is expected beyond
Poisson-stream identity (see seeds below), and every assertion band
is set wide of Poisson noise.

**Scripts, seeds, and invocation** (from the repository root; each
runs in seconds and prints PASS/FAIL verdict lines — a rerun is
successful iff every line is PASS):

1. `series_quantum_mechanics/code/3009_eta_mode_independence_check.py`
   — mode-independence of η via the A3′×I-3 cancellation + the two
   ingredient-breaking controls. Master seed: `default_rng(31009)`,
   set at module top; the Poisson streams derive from it
   deterministically. Run: `python3 <path>`.
2. `series_quantum_mechanics/code/3010_cgeo_relay_multiplicity_check.py`
   — the value c_geo = z = 12 (standing class), class-dependence
   (f-cone), and measured convention-inertness. Seed at module top.
   Run: `python3 <path>`.
3. `series_quantum_mechanics/code/3038_eta_mode_coverage_extension.py`
   — the ALL-MODES lemma (header) + extended coverage (3 dispersions
   × 4 profile families × 12 wavenumbers in 1D; 8 2D product modes;
   4-decade N-scan; exact-expectation identity checked per
   configuration; controls per dispersion). Master seed:
   `default_rng(30380809)`. Run: `python3 <path>`.

**Determinism statement.** Each script's randomness flows from its
single module-top `numpy.random.default_rng(seed)`; identical NumPy
versions reproduce identical streams and therefore bit-identical
printed values. Across NumPy versions the Generator bit-stream
contract (PCG64) has been stable; if a future NumPy breaks it, the
PASS/FAIL verdicts remain the reproduction target (bands are
noise-calibrated), and the printed values remain the target under a
matched version.

**Unprinted sentinels.** Each script computes an unprinted
KEY-DESIGN-RULE clause-(c) sentinel (a bookkeeping integer/rate from
a random unprinted configuration). These exist for panel key
challenges; a reproducing party can surface one by printing the named
variable, and a matched-version rerun must reproduce it exactly.

**What a successful rerun does and does not establish.** It
establishes the BOOKKEEPING-grade claims as labeled in the 3009/3010
records (v1.1 grade labels) and the ALL-MODES lemma — nothing at
microscopic-derivation grade.

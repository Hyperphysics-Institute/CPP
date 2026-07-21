# ALPHA-1 S4-E PREREGISTRATION (FROZEN) — the Ewald-grade hardening the seats demanded, under THEIR criteria, committed before any run

**Patch 2713, 21 July 2026. Method: Ewald summation (tinfoil BC,
α_ew = 5.6/L, half-space k-vectors |n|² ≤ 27), soft-core handled as a
short-range correction to the point-charge Ewald (finite at contact);
same closed parameters as S4-N (θ = 35.1495 MeV, q = e, n_CP =
58.636 /fm³). Runs: MAIN-A/B (N = 686, independent chains, seeds
20260731/2, 600 + 2400 sweeps), SIZE-S (N = 432, seed 20260733),
SIZE-L (N = 1024, seed 20260734), CORE (N = 432, a_s = 0.02, seed
20260735), each 400 + 1600 sweeps; a_s = 0.04 fm elsewhere.
Observables: signed all-bin charge profile ρ_z(r) with BLOCK-averaged
errors (10 blocks; answers the autocorrelation critique); S_zz(k) =
⟨|Σ z e^{ik·r}|²⟩/N from the maintained Ewald structure factors
(GPT item 5). Fits: covariance-aware weighted LSQ on ALL bins, signed
(no sign masking — the 2709 P2 mask is conceded and removed);
monotonic model A e^{−κr}/r vs damped-oscillatory
A e^{−κr}cos(k₀r+φ)/r, compared by AIC. Side computation: the true
FCC Voronoi (rhombic dodecahedron) self-cell fraction by direct MC
integration (answers DeepSeek's cell-shape attack).**

## Frozen criteria (the seats' own words made operational)

- **C1 (Gemini):** MAIN combined κ_fit within **2%** of κ_D = 5.4942
  /fm AND monotonic (no significant sign alternation, all-bin, 2σ,
  window 2a_s < r < 3/κ).
- **C2 (GPT):** S_zz(k) at the five smallest k-shells consistent with
  the DH form k²/(k²+κ_S²) with κ_S within **10%** of κ_D.
- **C3 (GPT):** the damped-oscillatory model NOT preferred: ΔAIC in
  its favor < 2 on every run.
- **C4 (GPT finite-size):** κ_fit drift across N = 432/686/1024 ≤ 5%.
- **C5 (GPT chains):** MAIN-A vs MAIN-B κ_fit agree within combined
  block errors.

**S4-E PASS = C1∧C2∧C3∧C4∧C5** → rider v3 auto-promotes and the Q4
enactment completes (2715); Gemini's Q3 flips to UPHOLD by their own
statement. **Any failure** → enactment holds at v2.5, failure reports
to the seats in full, nothing renamed.

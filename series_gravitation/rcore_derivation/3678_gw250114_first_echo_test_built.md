# The GW250114 first-echo test of THEO-PCD-SEA's falsifier is BUILT and VALIDATED, not yet RUN: GWOSC is unreachable from the worker's container (host_not_allowed), so the run is a mechanical action on Kila6/VideoCPU (or an allowlist change). Verdict rule frozen before the data. Self-test on synthetic noise: null peak 5.1 ± 0.3, injected SNR 8.7 recovered at 9.2 ± 1.0

**Patch 3678, Session 166, 7 Sep 2026.** Script `code/3678_gw250114_first_echo_search.py` (`--selftest` runs here, PASS; `--run` needs gwosc.org). Reasoning `reasoning/3678.md`. Ledger row 5 / §5 annotated. No paper touched. No panel.

## §1 What is built
A matched-filter first-echo search on GW250114 (H1, L1) with the BHP echo template of Uchikata et al. (arXiv:2309.01894, eqs. 4–5: barrier reflectivity R(f) fit for 0.6 ≤ χ ≤ 0.8) modified for a **partial surface R_surf = ⅔** (SEA's untaken fraction at the wave horizon, 3675 T2): h_echo = R_surf √(1 − R²) h₀ Σ (R_surf R)ⁿ⁻¹ e^{−i(2πf t_d + φ)(n−1)}. The ringdown h₀ is the (2,2,0) + (2,2,1) pair at the PRL's f, γ (247/221 Hz, 249/708 Hz) from t_peak + 6 t_Mf; overall amplitude and overall phase free (two orthogonal quadratures: cosine/sine ringdown), inter-echo phase φ on a 4-point grid, t_d ∈ [0.24, 0.31] s (prediction 0.27 s at χ = 0.68, 3676 T1). Whitening by a Welch PSD from 30 s of off-source data; p-value against ≥ 500 off-source background slots (BG2-style, 2309.01894 §III.B).

## §2 What was checked (self-test, runs here)
Synthetic noise from an analytic aLIGO-like PSD reproduces its PSD under Welch (ratio 1.01). Two normalization defects were found and fixed against the null (inner-product factor 2·fs, not 4·fs; quadratures must be the ringdown's cos/sin, not φ and φ + π/2, whose overlap was 0.87). After the fixes: **null search peak 5.06 ± 0.25 (12 draws); injected train at SNR 8.7 recovered at 9.22 ± 0.99.** The instrument separates the two hypotheses by ~4σ at the predicted amplitude.

## §3 Verdict rule (frozen in the script header, before the data)
DETECTED / SEA falsified: network peak ≥ 7 and p < 0.01. EXCLUDED / seat (3) closes: peak consistent with background (p > 0.1). Otherwise inconclusive. No retune after the data. Exhaustion trigger: if the real off-source background max exceeds 7 (non-Gaussian data), the instrument cannot decide and the item goes to the bundle as owed.

## §4 The mechanical action (Thomas / Isak)
Either add `gwosc.org` to the worker container's network allowlist and say so, or on Kila6/VideoCPU from the repo root:
```
pip install gwpy gwosc --break-system-packages
python3 series_gravitation/code/3678_gw250114_first_echo_search.py --run
```
Paste the printed block (per-detector peak SNR, t_d, p; network SNR; the rule's verdict) into the next session. Runtime: the background loop is the cost (500–1000 slots × 15 t_d × 4 φ); expect tens of minutes on Kila6.

## §5 Standing
Seat (3) OPEN, instrument ready. Next act: the register-sector statement (what SEA leaves to the matter metric), then the bundle. GR-2 V2.8 after the panel.

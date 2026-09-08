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

## §6 Amendment (Patch 3679, same session) — Windows run failed on gwpy's build chain, not on physics
Kila6 (Python 3.12, no MSVC) could not build `igwn-segments`, a gwpy dependency. gwpy removed: `--run` now fetches the 4096 s GWOSC HDF5 files with `gwosc` + `requests` + `h5py` (all prebuilt wheels on Windows) and reads `strain/Strain` directly; off-source = 300 s ending 40 s before the peak; on-source and background unchanged. Self-test re-run: PASS (identical numbers). Command, **from the repo root** (the earlier attempt ran from `/`):
```
cd ~/Documents/GitHub/CPP && \
pip install gwosc requests h5py scipy numpy --break-system-packages && \
python3 series_gravitation/code/3678_gw250114_first_echo_search.py --run
```
The two ~120 MB strain files download once into the repo root (add them to `.gitignore` if git status complains — they must not be committed).

## §7 Amendment (Patch 3680) — event name
GWOSC's v2 API resolves `GW250114_082203`, not `GW250114`; fixed. If `event_gps` fails the script uses the computed peak GPS 1420878141; if `get_event_urls` fails, set `GWOSC_H1_URL` and `GWOSC_L1_URL` to the 4096 s HDF5 links from the event's GWOSC page and rerun.

## §8 Run 1 on Kila6 (7 Sep 2026) — EXHAUSTION TRIGGER FIRED; instrument defect diagnosed, repaired by principle (Patch 3681)
**Verbatim output (review economy §4.6):**
```
GW250114_082203 GPS from GWOSC: 1420878141.2
  downloading https://gwosc.org/archive/data/O4b_4KHZ_R1/1420820480/H-H1_GWOSC_O4b_4KHZ_R1-1420877824-4096.hdf5
  H1: peak SNR 3816.66 at t_d = 0.240 s, tau = 0.240 s after t_peak-2s;  p = 0.896 (1000 background slots, background max 80733.18)
  downloading https://gwosc.org/archive/data/O4b_4KHZ_R1/1420820480/L-L1_GWOSC_O4b_4KHZ_R1-1420877824-4096.hdf5
  L1: peak SNR 15292.63 at t_d = 0.281 s, tau = 0.281 s after t_peak-2s;  p = 0.503 (1000 background slots, background max 52282.17)
NETWORK peak SNR 15761.71
```
**Diagnosis (recorded before the fix):** background maxima of 10⁴–10⁵ and peaks locked at τ = t_d on both detectors are the signature of spectral leakage from unconditioned data: real strain carries ~10⁻¹⁷ content below 10 Hz, and an 8 s rectangular cut leaks it across the band via sidelobes, swamping the ~10⁻²³ in-band noise; the "peak" is the template aligning with the segment-edge transient. The synthetic self-test had no such low-frequency content, so it could not catch this. **Reproduced:** the same synthetic noise plus a 10⁻¹⁷ × sin(2π·0.7 Hz) drift, run without high-pass or taper, gives SNR 1.2×10⁵ at t_d = 0.240, τ ≈ t_d.
**Repair by principle (the property that failed: out-of-band leakage):** (i) 4th-order Butterworth high-pass at 15 Hz, zero-phase, applied to the whole series before slicing; (ii) Tukey (α = 0.1) taper on every 8 s segment before the FFT — for on-source and background alike; (iii) NaN guards: the on-source window must be NaN-free (else exhaustion), off-source is the longest NaN-free stretch (≥ 60 s, ≤ 300 s) ending ≥ 40 s before the peak. **Nothing else changed:** template, phase grid, t_d range, thresholds, verdict rule as frozen at 3678 §3. Self-test re-run with the realistic low-frequency content included: null 4.97 ± 0.30, injected 8.7 → 9.41 ± 0.98, PASS.
**This is not a retune:** no signal number existed to steer toward; the run never reached the decision stage. Run 2 command unchanged: `python series_gravitation/code/3678_gw250114_first_echo_search.py --run` (the HDF5 files are cached; no re-download).

## §9 Run 2 on Kila6 (8 Sep 2026) — instrument working; output NOT the frozen statistic; two defects found and fixed (Patch 3682)
**Verbatim output (§4.6):**
```
GW250114_082203 GPS from GWOSC: 1420878141.2
  H1: 11513856 NaN samples in file (68.63 %)
  H1: off-source = 277 s ending 40 s before the peak
  H1: peak SNR 12.99 at t_d = 0.300 s, tau = 6.278 s after t_peak-2s;  p = 0.000 (1000 background slots, background max 6.96)
  L1: 11554816 NaN samples in file (68.87 %)
  L1: off-source = 277 s ending 40 s before the peak
  L1: peak SNR 12.88 at t_d = 0.266 s, tau = 6.249 s after t_peak-2s;  p = 0.000 (1000 background slots, background max 5.15)
NETWORK peak SNR 18.29
```
**Why the frozen rule does not apply to it.** The spec (3678 header) is a search at *t_peak + t_d*: the echo is time-locked to the known ringdown. The implementation instead maximized the template's start τ over the whole 8 s window — an unintended degree of freedom that turns the statistic into a generic ringdown-shaped burst search. Uchikata et al. lock the start to t_merger + Δt_echo ± 1 %. **Decoded:** the correlation lag convention was also reversed (defect 2), so "τ = 6.278 s" is the template *delayed by 8 − 6.278 = 1.722 s*, i.e. its ringdown placed 0.278 s before the peak and its first echo copy (t_d = 0.300 s later) at +0.022 s — on GW250114's own ringdown. L1: −0.249 + 0.266 = +0.017 s. The H1–L1 "offset" of 29 ms is Δt_d (34 ms), not a sky delay. **Run 2 detected the merger's ringdown through the template's echo term.** Not an echo; not the alternative's prediction; not SEA's falsification.
**Fixes (by principle, recorded before run 3):**
1. **Start lock (the frozen spec, now implemented):** template ringdown start held at t_peak + 6 t_Mf ± 2 ms — the PRL's peak-time precision (0.4 t_Mf = 0.13 ms) plus the one-/two-mode start ambiguity (6–10.5 t_Mf = 1.5 ms). Applied identically to on-source and to every background slot. The unlocked search is retained as a labelled *diagnostic* line only.
2. **Lag convention:** z = 2 fs · irfft(D · conj(H)/S), so z[j] is the overlap with the template delayed by j/fs. The previous conj placement mirrored the lag; it was invisible to a free-start search (a mirrored peak is still a peak) and fatal to a locked one — the self-test under the lock failed (3.3) until this was fixed, then passed.
**Self-test under the lock (realistic low-frequency content, conditioned):** null 3.58 ± 0.55 (fewer trials than the free search, as expected); injected 8.7 → 9.21 ± 1.03; free-start diagnostic on a null draw 5.66. **Thresholds unchanged and now conservative:** ≥ 7 & p < 0.01 → detected; background-consistent (p > 0.1) → excluded; exhaustion if background max > 7.
**Data-quality note for the record:** 68.6 % / 68.9 % of the 4096 s files are NaN (detector out of observing mode for most of the hour); 277 s of clean off-source data were found ending 40 s before the peak; the on-source window is NaN-free. Not a defect; recorded so the p-value's 1000 slots are understood to come from a 277 s stretch (slots overlap; effective independent count ≈ 277/8 ≈ 35 — the background *max* is the robust quantity, and it was 6.96 / 5.15 under the free search).
Run 3 command unchanged: `python series_gravitation/code/3678_gw250114_first_echo_search.py --run`.

## §10 Run 3 on Kila6 (8 Sep 2026) — THE FROZEN STATISTIC, SCORED (Patch 3683)
**Verbatim output:**
```
GW250114_082203 GPS from GWOSC: 1420878141.2
  H1: 11513856 NaN samples in file (68.63 %)
  H1: off-source = 277 s ending 40 s before the peak
  H1: [diagnostic, not the statistic] free-start peak 12.99 at t_d = 0.300, ringdown start -0.278 s from t_peak (GPS 1420878140.922)
  H1: LOCKED peak SNR 3.69 at t_d = 0.247 s (ringdown start +0.0012 s from t_peak);  p = 0.152 (1000 background slots, background max 4.56)
  L1: 11554816 NaN samples in file (68.87 %)
  L1: off-source = 277 s ending 40 s before the peak
  L1: [diagnostic, not the statistic] free-start peak 12.86 at t_d = 0.265, ringdown start -0.248 s from t_peak (GPS 1420878140.952)
  L1: LOCKED peak SNR 3.76 at t_d = 0.276 s (ringdown start +0.0020 s from t_peak);  p = 0.081 (1000 background slots, background max 4.29)
NETWORK peak SNR 5.27
```
**Diagnostic confirms the run-2 decode:** the free-start peaks are the merger itself (ringdown start −0.278 s / −0.248 s from t_peak with the template's echo copy on the real ringdown).
**Verdict by the frozen rule (3678 §3 / script header), applied as written:**
- *Detected (≥ 7 and p < 0.01)?* **No.** Locked 3.69 / 3.76, network 5.27, against the alternative's predicted 7.5 (first echo) – 8.7 (train). The network value equals the null expectation (√2 × 3.58 ≈ 5.1 from the self-test).
- *Excluded (background-consistent, p > 0.1)?* **H1 yes (p = 0.152); L1 no (p = 0.081).** The frozen rule names no combined-network p, and none is defined after the fact.
- **Formal outcome: INCONCLUSIVE by the letter — one detector short of the exclusion criterion.** Exhaustion trigger not fired (background maxima 4.56 / 4.29 < 7).
**Substantive reading (stated, not scored):** the observed amplitude is 3.4σ below the alternative's train prediction (8.7, σ ≈ 1.0 from the self-test) and 1.7σ below its conservative first-echo prediction (7.0). The two detectors' best-fit delays (0.247 s, 0.276 s) differ by 29 ms; a common echo would agree to a few ms. **THEO-PCD-SEA's null is consistent with the data; the coherent-return alternative is DISFAVORED at the 2–3σ level on GW250114 and not excluded.** Quantifier discipline: "disfavored on GW250114", not "excluded".
**Seat (3) of the triangulation:** moves from OPEN to **SCORED: consistent (SEA); alternative disfavored 2–3σ**. What would close it: (a) a pre-registered combined-network statistic (Fisher or coherent) frozen before use — owed, for a future event or a re-run with a new frozen header, not for this data; (b) the LVK's own O4 echo analysis of GW250114 when published.
**No retune:** R_surf, t_d range, phase grid, lock width, thresholds, and template are as frozen at 3678 §3 and 3682 §9.

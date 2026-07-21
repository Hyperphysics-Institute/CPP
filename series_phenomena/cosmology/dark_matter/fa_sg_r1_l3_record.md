# FA-SG-R1 LEG L3 RECORD — envelope-extraction robustness battery (METH-L2-021's own promotion battery): grand band ℓ = 0.0901 ± 0.0031 fm across window × observable × size axes on all four arenas — no axis blows the band open; the Fourier-filter cross-check concords; an attempted Hilbert demodulation reported INAPPLICABLE with diagnosis

**Patch 2686, 21 July 2026. Executing charter §2 R1-L3, all named
components, none optional. Observable axis enumerated pre-run: bin-mean
|f|, bin-median |f|, Fourier-filtered |f|·r. Verify:
`code/2686_r1_l3_battery.py`. 79.5% not in scope.**

## §1 — The three named components

**(i) Multi-window fits (Copilot's component):** the three frozen 2671d
windows, per arena, per size — all in §2's grid.

**(ii) Fourier-filter removal of the staggered component (DeepSeek's
component):** low-pass of the fine-binned (0.03 fm) log(|f|·r) profile
below the lattice carrier band (cutoff wavelength 0.20 fm > shell
spacing 0.10–0.15 fm), fitted in the same windows. Per-arena filtered
centres: A0 0.0904, A1 0.0865, A2 0.0898, A3 0.0904 fm — **concordant
with the unfiltered |f|·r readout** (observable-axis spread ≤ 0.0027 fm
everywhere).

**(iii) Window / observable / size robustness (GPT's component):** the
marginal band per choice axis, per arena:

| Arena | window-axis spread | observable-axis spread | size-axis spread | battery band (fm) |
|---|---|---|---|---|
| A0 | 0.0060 | 0.0011 | 0.0000 | 0.0904 ± 0.0030 |
| A1 | 0.0017 | 0.0027 | 0.0000 | 0.0880 ± 0.0024 |
| A2 | 0.0007 | 0.0026 | 0.0000 | 0.0915 ± 0.0027 |
| A3 | 0.0060 | 0.0011 | 0.0000 | 0.0904 ± 0.0030 |

**Grand band (all arenas × all enumerated axes, n = 72): ℓ = 0.0901 ±
0.0031 fm, range [0.0836, 0.0956].** The 2671 band was 0.091 ± 0.002:
the battery band is of the same order — **no window, observable, or
lattice-size axis blows the band open** (the R1-PASS L3 condition is
met on this leg's own terms; the arc class is set at the readout, not
here).

## §2 — Diagnostics (outside the band, disclosed same-font)

**Peak-envelope channel (leakage-free demodulation, supplementary):**
fit through the local maxima of the signed exact-shell |f·r| profile
(FCC R=7, [0.45, 1.8] fm): ℓ = 0.0902 fm — concordant.

**Attempted Hilbert (analytic-signal) demodulation: INAPPLICABLE.** A
fourth extraction was attempted — FFT-Hilbert envelope of the SIGNED
shell profile. It fails its validity preconditions and is reported as
attempted-and-inapplicable, not silently dropped: the signed profile's
carrier is irregular (radial sign runs +++−++−−−−−−…, not strict
alternation — the staggering is directional, scrambled by radial
projection) and the profile spans ~7 decades, so FFT edge leakage
dominates the extracted envelope (ℓ "readouts" 0.22–0.65 fm, R²-poor).
This extraction was NOT in the pre-enumerated observable axis; it enters
no band; it is preserved verbatim in the verify script for the panel.

**Fence audit:** clean. Next leg per frozen sequencing: L2.
Reasoning: `reasoning/2686.md`.

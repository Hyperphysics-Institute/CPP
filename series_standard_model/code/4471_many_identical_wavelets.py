"""Patch 4471 -- founder: if the central CP and each polarized DP make the same drop, each gives the same energy; if all their emissions are
identical, multiple wavelets could interact with the grating to produce the fine line.

Each wavelet: a flat pulse of 3 cycles at the line's rate (carrier 1 in frequency units).  N = 50 identical wavelets, arranged several ways;
the half-power width of the summed light's spectrum (share of the carrier; zero-padded FFT) is printed:
  (a) one wavelet;
  (b) N identical wavelets at the same moment (side by side): one bigger pulse, the same spread;
  (c) N identical wavelets at random moments, random phases (independent; power spectra averaged over realizations): still broad;
  (d) N identical wavelets one after another, in step, with no gap (each starts as the last ends, 3 periods later): one long wave, ~0.9/(3N);
  (e) as (d) with starts jittered (0.1 and 0.25 period): share of power left in the narrow core;
  (f) in step but with gaps (spacing 4 and 5 periods): the light splits into several lines 1/spacing apart within one wavelet's spread.
Flat wavelets have abrupt edges; spacing 3 also places side lines on the zeros of a 3-cycle wavelet's spectrum.
"""
import numpy as np
fs, T, PAD = 64, 2000.0, 8
t = np.arange(0, T, 1/fs)
f = np.fft.rfftfreq(PAD*t.size, 1/fs)
band = (f > 0.2) & (f < 1.8)
def wavelet(t0, phase=0.0, n=3):
    u = t - t0
    return np.where((u >= 0) & (u < n), np.cos(2*np.pi*u + phase), 0.0)
def spec(E):
    return np.abs(np.fft.rfft(E, n=PAD*t.size))**2
def width(S):
    S, ff = S[band], f[band]
    h = ff[S >= S.max()/2]
    return h.max() - h.min()
def peaks(S, rel=0.05):
    S, ff = S[band], f[band]
    idx = [i for i in range(1, len(S)-1) if S[i] >= S[i-1] and S[i] >= S[i+1] and S[i] >= rel*S.max()]
    return ", ".join(f"{ff[i]:.2f} ({S[i]/S.max():.2f})" for i in idx)
rng = np.random.default_rng(5)
N = 50
print(f"(a) one 3-cycle wavelet:                           width {width(spec(wavelet(10))):.3f}")
print(f"(b) {N} identical wavelets at the same moment:        width {width(spec(sum(wavelet(10) for _ in range(N)))):.3f}")
Sacc = 0
for _ in range(60):
    Sacc = Sacc + spec(sum(wavelet(rng.uniform(0, T-10), rng.uniform(0, 2*np.pi)) for _ in range(N)))
print(f"(c) {N} wavelets at random moments, random phases:   width {width(Sacc):.3f}")
Sd = spec(sum(wavelet(10 + 3*k) for k in range(N)))
print(f"(d) {N} wavelets in step, no gap (spacing 3):       width {width(Sd):.4f}  (0.9/(3N) = {0.886/(3*N):.4f})")
core = (f > 1 - 0.02) & (f < 1 + 0.02)
tot = Sd[band].sum()
for j in (0.1, 0.25):
    acc = 0
    for _ in range(30):
        acc = acc + spec(sum(wavelet(10 + 3*k + rng.normal(0, j)) for k in range(N)))
    share = acc[core].sum()/acc[band].sum()
    print(f"(e) as (d), starts jittered by {j} period: share of power in the narrow core {share:.2f}")
for sp in (4, 5, 6):
    S = spec(sum(wavelet(10 + sp*k) for k in range(N)))
    print(f"(f) in step with gaps, spacing {sp} periods: lines (frequency, relative height) at {peaks(S)}")

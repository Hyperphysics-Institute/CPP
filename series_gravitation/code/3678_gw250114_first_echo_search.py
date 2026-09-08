#!/usr/bin/env python3
"""
Patch 3678 — THE GW250114 FIRST-ECHO TEST OF THEO-PCD-SEA'S FALSIFIER (3677 §2).
Two modes:
  --selftest   : synthetic aLIGO-like noise (analytic PSD), inject the alternative's echo train at network SNR 8.7
                 at t_d = 0.27 s, and recover it with the same pipeline; also a null run (no injection). RUNS HERE.
  --run        : fetch the 4096 s H1/L1 open-data HDF5 files for GW250114 from GWOSC (pure Python: gwosc + requests +
                 h5py — NOT gwpy, whose igwn-segments dependency needs MSVC on Windows), whiten with a Welch PSD from
                 300 s of off-source data, search the on-source window t_peak + t_d, t_d in [0.24, 0.31] s, two
                 orthogonal quadratures x 4-point phase grid, report the peak network SNR and a p-value against up to
                 1000 off-source background slots. NEEDS network access to gwosc.org — BLOCKED in the Claude container
                 (x-deny-reason: host_not_allowed, 7 Sep 2026); run on Kila6/VideoCPU from the repo root:
                   pip install gwosc requests h5py scipy numpy --break-system-packages
                   python3 series_gravitation/code/3678_gw250114_first_echo_search.py --run

TEMPLATE (Uchikata et al. 2023, arXiv:2309.01894 eqs. 4–5, BHP model) with a PARTIAL surface R_surf = 2/3
(THEO-PCD-SEA's untaken fraction at the wave horizon, 3675 T2):
    h_echo(f) = R_surf * sqrt(1 - R(f)^2) * h0(f) * sum_{n=1}^{N} [R_surf R(f)]^{n-1} exp(-i (2 pi f t_d + phi)(n-1))
    R(f)      = their eq. (5) fit for 0.6 <= chi <= 0.8, chi = 0.68, detector-frame M = t_Mf / 4.925e-6 s = 68.4 Msun
    h0(t)     = the (2,2,0) ringdown: f220 = 247 Hz, gamma220 = 221 Hz (LVK PRL 135, 111403), plus the overtone
                f221 = 249 Hz, gamma221 = 708 Hz at the PRL's amplitude ratio (A221/A220 ~ 1 at 6 t_Mf — free here),
                started at t_peak + 6 t_Mf.
The overall amplitude is free (matched filter), so the OUTPUT is the recovered SNR; the PREDICTION under the
alternative is SNR ~ 7.5 (first echo) to 8.7 (train); under SEA, 0 (background only, expected peak ~ 3–4).

Verdict rule, FROZEN 7 Sep 2026 before any real data is seen (review economy §4). Self-test (synthetic aLIGO-like
noise, this file --selftest): null search peak 5.1 ± 0.3; injected train at SNR 8.7 recovered at 9.2 ± 1.0.
  DETECTED / SEA FALSIFIED : network peak SNR >= 7 AND p < 0.01 against >= 500 off-source background slots.
  EXCLUDED / seat (3) CLOSES: network peak SNR consistent with the background (p > 0.1) — the injection study shows
                             the predicted 7.5–8.7 would sit ~4 sigma above the null distribution, so a background-
                             consistent result excludes the coherent-return alternative at that level on this event.
  INCONCLUSIVE             : anything else; seat (3) stays open.
No refit of R_surf, t_d, the phase grid, or the template after seeing the data. Exhaustion trigger (§4.5): if the
GW250114 off-source data are non-Gaussian enough that the background max exceeds 7, this instrument cannot decide
and the matter goes to the bundle as an owed empiric, not to a retune.
"""
import argparse, numpy as np
from scipy.signal import welch
from scipy.fft import rfft, irfft, rfftfreq

# ---------------- event constants (LVK PRL 135, 111403) ----------------
EVENT = "GW250114_082203"    # GWOSC full event name (the short form "GW250114" 404s on api/v2)
GPS_PEAK = 1420878141.0      # 2025-01-14 08:22:03 UTC = GPS 1420878141 (18 leap s); refined from GWOSC if the API answers
T_MF = 0.337e-3; M_DET = T_MF / 4.925e-6; CHI = 0.68
F220, G220 = 247.0, 221.0; F221, G221 = 249.0, 708.0
R_SURF = 2.0 / 3.0; TD_PRED = 0.270; TD_LO, TD_HI = 0.24, 0.31
FS = 4096; FMIN, FMAX = 20.0, 1024.0

def R_barrier(f, chi=CHI, M=M_DET):
    x = 2 * np.pi * M * 4.925e-6 * f
    e1 = np.exp(-300 * (x + 0.27 - chi)); e2 = np.exp(-28 * (x - 0.125 - 0.6 * chi)); e3 = np.exp(19 * (x - 0.3 - 0.35 * chi))
    return (1 + e1 + e2) / (1 + e1 + e2 + e3)

def ringdown(t, a221=1.0, quad=0):
    """h0(t): two-mode ringdown starting at t = 0 (t_peak + 6 t_Mf), unit A220; quad=0 cosine, quad=1 sine (the two quadratures)."""
    h = np.zeros_like(t); m = t >= 0; osc = np.cos if quad == 0 else np.sin
    h[m] = np.exp(-G220 * t[m]) * osc(2 * np.pi * F220 * t[m]) + a221 * np.exp(-G221 * t[m]) * osc(2 * np.pi * F221 * t[m])
    return h

def echo_template(N, fs, td, phi, n_echo=20, a221=1.0):
    """Frequency-domain echo train (BHP model with partial surface) for inter-echo phase phi.
    Returns the two OVERALL-phase quadratures (cosine / sine ringdown) — these are near-orthogonal; phi is searched on a grid."""
    t = np.arange(N) / fs; f = rfftfreq(N, 1 / fs)
    R = R_barrier(f); Reff = R_SURF * R
    S = sum((Reff ** (n - 1)) * np.exp(-1j * (2 * np.pi * f * td + phi) * (n - 1)) for n in range(1, n_echo + 1))
    pref = R_SURF * np.sqrt(np.clip(1 - R ** 2, 0, 1)) * S * np.exp(-2j * np.pi * f * td)
    out = [pref * (rfft(ringdown(t, a221, q)) / fs) for q in (0, 1)]
    return out, f

PHI_GRID = (0.0, np.pi / 2, np.pi, 3 * np.pi / 2)

def matched_filter_snr(D, Hs, psd, f, fs, N):
    """Phase-marginalized SNR time series. Conventions: D, H are rfft/fs (continuous-FT scale), one-sided PSD psd(f).
    <a|b> = 4 Re int a* b / S df ;  z(tau) = 4 Re int_0^inf D* H e^{2 pi i f tau}/S df = 2 fs irfft(conj(D) H / S) (irfft folds the negative frequencies)  ;  sigma^2 = <h|h>."""
    df = f[1] - f[0]
    band = (f >= FMIN) & (f <= FMAX)
    w = np.where(band, 1.0 / psd, 0.0)
    out = []
    for H in Hs:
        sigma2 = float(4 * np.sum(np.abs(H) ** 2 * w) * df)
        z = 2 * fs * irfft(np.conj(D) * H * w, n=N)
        out.append(z / np.sqrt(sigma2))
    a, b = out
    return np.sqrt(a ** 2 + b ** 2)

def analytic_psd(f):
    """Rough aLIGO O4 design-like PSD (for the self-test only)."""
    fk = np.maximum(f, 5.0) / 215.0
    return 1e-49 * (fk ** -4.14 - 5 * fk ** -2 + 111 * (1 - fk ** 2 + 0.5 * fk ** 4) / (1 + 0.5 * fk ** 2)) + 1e-52

def condition(x, fs, f_hp=15.0):
    """Data conditioning (standard): 4th-order Butterworth high-pass at f_hp, zero-phase. Real strain carries ~1e-17
    content below 10 Hz; without this an 8 s rectangular cut leaks it across the band by sidelobes (Kila6 run 1,
    7 Sep 2026: SNR ~1e4, background max ~1e5, peaks locked at tau = t_d, i.e. on the segment edge)."""
    from scipy.signal import butter, sosfiltfilt
    sos = butter(4, f_hp, btype="highpass", fs=fs, output="sos")
    return sosfiltfilt(sos, x)

def taper(N, alpha=0.1):
    from scipy.signal.windows import tukey
    return tukey(N, alpha)

def whiten_search(d, fs, psd_of_f, N, td_grid):
    f = rfftfreq(N, 1 / fs); D = rfft(d * taper(N)) / fs; psd = psd_of_f(f)
    best = (0, None)
    for td in td_grid:
        for phi in PHI_GRID:
            Hs, _ = echo_template(N, fs, td, phi)
            rho = matched_filter_snr(D, Hs, psd, f, fs, N)
            i = int(np.argmax(rho)); best = max(best, (rho[i], (td, i / fs)))
    return best

def selftest(seed=7):
    rng = np.random.default_rng(seed); N = 8 * FS
    f = rfftfreq(N, 1 / FS); psd = analytic_psd(f); df = f[1] - f[0]
    def noise():
        # one-sided PSD S: E|x_rfft|^2 = S * FS * N / 2  (so that Welch recovers S)
        amp = np.sqrt(psd * FS * N / 2); ph = rng.uniform(0, 2 * np.pi, f.size)
        x = irfft(amp * np.exp(1j * ph), n=N)
        tt = np.arange(N) / FS
        x += 1e-17 * np.sin(2 * np.pi * 0.7 * tt + rng.uniform(0, 6)) + 3e-18 * np.sin(2 * np.pi * 3.1 * tt)   # realistic sub-10 Hz content
        return condition(x, FS)
    # PSD sanity: Welch of the synthetic noise vs the analytic PSD in band
    fw, pw = welch(noise(), fs=FS, nperseg=FS)
    m = (fw > 50) & (fw < 500); ratio = np.median(pw[m] / analytic_psd(fw[m]))
    print(f"  PSD sanity: Welch/analytic median ratio in 50–500 Hz = {ratio:.2f} (expect ~1)")
    td_grid = np.arange(TD_LO, TD_HI + 1e-9, 0.005)
    Hs, _ = echo_template(N, FS, TD_PRED, np.pi / 2); h = irfft(Hs[0] * FS, n=N)
    H = Hs[0]; band = (f >= FMIN) & (f <= FMAX)
    sig = np.sqrt(4 * np.sum((np.abs(H) ** 2 / psd)[band]) * df)
    results = {}
    for label, target in (("null", 0.0), ("inject_SNR8.7", 8.7)):
        vals = []
        for k in range(12):
            d = noise() + ((target / sig) * np.roll(h, 2 * FS) if target > 0 else 0.0)
            rho, (td, tau) = whiten_search(d, FS, analytic_psd, N, td_grid)
            vals.append(rho)
        results[label] = (np.mean(vals), np.std(vals), np.max(vals))
        print(f"  {label:14s}: recovered peak SNR mean {np.mean(vals):.2f} ± {np.std(vals):.2f} (max {np.max(vals):.2f}) over 12 noise draws")
    ok = 0.7 < ratio < 1.4 and results["null"][0] < 5.5 and results["inject_SNR8.7"][0] > 7.0
    print(f"  [{'PASS' if ok else 'FAIL'}] self-test: PSD ~1, null peak < 5.5, injected 8.7 recovered > 7")
    return ok

def _fetch_strain(det, gps, duration=4096, cache_dir="."):
    """Pure-Python GWOSC fetch (no gwpy: its igwn-segments dependency needs MSVC on Windows). Returns (t0, dt, strain)."""
    import os, requests, h5py
    from gwosc.locate import get_event_urls
    import os
    if os.environ.get(f"GWOSC_{det}_URL"):
        allu = [os.environ[f"GWOSC_{det}_URL"]]
    else:
        allu = get_event_urls(EVENT, detector=det, format="hdf5", sample_rate=FS)
    urls = [u for u in allu if f"-{duration}." in u] or [u for u in allu if "4096" in u] or allu
    if not urls:
        raise RuntimeError(f"no hdf5 strain URL for {det} from get_event_urls: {allu}")
    url = urls[0]; fn = os.path.join(cache_dir, os.path.basename(url))
    if not os.path.exists(fn):
        print(f"  downloading {url}"); r = requests.get(url, stream=True, timeout=600); r.raise_for_status()
        with open(fn, "wb") as fh:
            for chunk in r.iter_content(1 << 20): fh.write(chunk)
    with h5py.File(fn, "r") as h:
        x = h["strain/Strain"][:]; t0 = float(h["meta/GPSstart"][()]); dt = float(h["strain/Strain"].attrs["Xspacing"])
    return t0, dt, x

def run():
    from gwosc.datasets import event_gps
    try:
        gps = float(event_gps(EVENT)); print(f"{EVENT} GPS from GWOSC: {gps}")
    except Exception as e:
        gps = GPS_PEAK; print(f"GWOSC event_gps failed ({e}); using GPS_PEAK = {gps}")
    rhos = {}
    for det in ("H1", "L1"):
        t0, dt, x = _fetch_strain(det, gps)
        fs_file = int(round(1 / dt)); assert fs_file == FS, f"file sample rate {fs_file} != {FS}"
        i_peak = int(round((gps - t0) * FS))
        nan = np.isnan(x); print(f"  {det}: {nan.sum()} NaN samples in file ({100*nan.mean():.2f} %)")
        if nan[i_peak - 2 * FS: i_peak + 6 * FS].any(): raise RuntimeError(f"{det}: NaN inside the on-source window — instrument cannot decide (exhaustion trigger)")
        # off-source: the longest NaN-free stretch ending >= 40 s before the peak, capped at 300 s
        good = ~nan[: i_peak - 40 * FS]; end = good.size
        while end > 0 and not good[end - 1]: end -= 1
        start = end
        while start > 0 and good[start - 1] and end - start < 300 * FS: start -= 1
        x = condition(np.nan_to_num(x), FS)
        off = x[start:end]; print(f"  {det}: off-source = {off.size/FS:.0f} s ending {(i_peak - end)/FS:.0f} s before the peak")
        if off.size < 60 * FS: raise RuntimeError(f"{det}: < 60 s of clean off-source data — exhaustion trigger")
        fw, pw = welch(off, fs=FS, nperseg=4 * FS)
        psd_of_f = lambda f, fw=fw, pw=pw: np.interp(f, fw, pw)
        on = x[i_peak - 2 * FS: i_peak + 6 * FS]                     # on-source: t_peak - 2 s .. + 6 s
        td_grid = np.arange(TD_LO, TD_HI + 1e-9, 0.001)
        rho, (td, tau) = whiten_search(on, FS, psd_of_f, 8 * FS, td_grid)
        bg = []
        for k in range(1000):                                        # background: 8 s slots stepping 0.0054 s (0.02 t_d) through off-source
            s0 = int((0.5 + 0.0054 * k) * FS)
            if s0 + 8 * FS > off.size: break
            r, _ = whiten_search(off[s0: s0 + 8 * FS], FS, psd_of_f, 8 * FS, td_grid[::5]); bg.append(r)
        bg = np.array(bg); p = float(np.mean(bg >= rho)) if bg.size else float("nan")
        rhos[det] = (rho, td, tau, p, bg.max() if bg.size else float("nan"))
        print(f"  {det}: peak SNR {rho:.2f} at t_d = {td:.3f} s, tau = {tau:.3f} s after t_peak-2s;  p = {p:.3f} ({bg.size} background slots, background max {rhos[det][4]:.2f})")
    net = np.sqrt(sum(v[0] ** 2 for v in rhos.values()))
    print(f"NETWORK peak SNR {net:.2f}  — verdict rule (frozen, see header): >= 7 & p < 0.01 -> alternative DETECTED / SEA falsified; background-consistent (p > 0.1) -> alternative EXCLUDED / seat (3) closes; else inconclusive; background max > 7 -> exhaustion trigger")

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--selftest", action="store_true"); ap.add_argument("--run", action="store_true")
    a = ap.parse_args()
    if a.selftest or not a.run: selftest()
    if a.run: run()

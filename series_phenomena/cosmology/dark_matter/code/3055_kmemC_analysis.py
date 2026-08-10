#!/usr/bin/env python3
"""3055_kmemC_analysis.py — K-MEM ROUTE C frozen analysis (v2).

SUPERSEDES 3054_kmemC_analysis.py (retained). Implements
`kmemC_routeC_prereg_v2.md` (Patch 3055) §4-§5 VERBATIM.

Implements `kmemC_routeC_prereg.md` (Patch 3053) §4–§5 VERBATIM.
REFUSES an incomplete manifest (no interim looks). Disposition printed
in the §5 tree language ONLY, evaluated in the frozen order. Standing
NONE until the single panel round.
"""
import glob, json, os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.normpath(os.path.join(HERE, '../data/kmemC'))
T_STEP = 24
Z, NBOOT, BOOT_SEED, CHUNK = 2.576, 10000, 30530811, 4
SUST_REF0, SNR_NOTE = 2.6e-3, 10.0
def windows(x_half, T_END):
    t_post = int(T_STEP + 1.5 * x_half) + 6
    return t_post, max(12, min(48, (T_END - t_post) // 3))

ARMS = [('a0','iso',24.0,384,0.10,128,0.0), ('a0p','iso',16.0,264,0.10,128,0.0),
        ('a1','iso',32.0,384,0.10,128,-12.0), ('a2','iso',28.0,504,0.10,128,6.0),
        ('ak','margin',28.0,104,0.60,512,6.0)]

def band_psd(sig):
    f = np.fft.rfft(sig - sig.mean())
    return (np.abs(f) ** 2)[1:]

def main():
    try:
        cal = json.load(open(os.path.join(DATA, 'calibration.json')))
        rep = json.load(open(os.path.join(DATA, 'pilot_report.json')))
    except FileNotFoundError as e:
        print(f"REFUSING TO RUN: pre-launch artifact missing ({e.filename}) "
              "— calibration and pilot must be committed first.")
        return 2
    beta_f = rep['beta_f']
    nmap = {a[0]: (int(rep['N_projected']) if a[0]=='ak' else a[5]) for a in ARMS}
    missing = 0
    F = {}
    for tag, cls, x_half, T_END, beta, _N, _dt in ARMS:
        n = nmap[tag]
        for p in range(n):
            for br in ('step', 'ctrl'):
                pth = os.path.join(DATA, f'leg_{p:04d}_{br}_{tag}.json')
                if not os.path.exists(pth):
                    missing += 1; continue
                F[(p, br, tag)] = np.array(json.load(open(pth))['F'])
    total = sum(nmap[a[0]] for a in ARMS) * 2
    if missing:
        print(f"REFUSING TO RUN: manifest incomplete — {missing}/{total} "
              "legs missing."); return 2

    excl = {a[0]: set() for a in ARMS}
    for (p, br, tag), arr in F.items():
        if not np.isfinite(arr).all(): excl[tag].add(p)

    rng = np.random.default_rng(BOOT_SEED)
    s3_pass, s1_sig, kappa = {}, {}, {}
    for tag, cls, x_half, T_END, beta, _N, dt in ARMS:
        band = SUST_REF0 * beta / 0.10
        t_post, base = windows(x_half, T_END)
        LATE = slice(T_END - base, T_END)
        n = nmap[tag]
        used = [p for p in range(n) if p not in excl[tag]]
        m = len(used)
        S = np.stack([F[(p, 'step', tag)] for p in used])
        C = np.stack([F[(p, 'ctrl', tag)] for p in used])
        D = S - C

        # ---- S3-C sustained positive control (band recentred on drive)
        sust = np.abs(D[:, 60:100].mean() - D[:, LATE].mean(axis=1).mean())
        boots = np.array([np.abs(D[rng.integers(0, m, m), 60:100].mean()
                          - D[rng.integers(0, m, m), LATE].mean())
                          for _ in range(2000)])
        det = bool(np.percentile(boots, 0.5) > 0 and sust > 0)
        inband = bool(band / 2 <= sust <= band * 2)
        s3_pass[tag] = det and inband
        # ---- S1-C tail (Route B recipe verbatim, on F[T_STEP:])
        Sp = np.stack([band_psd(F[(p, 'step', tag)][T_STEP:]) for p in used])
        Cp = np.stack([band_psd(F[(p, 'ctrl', tag)][T_STEP:]) for p in used])
        nb = int(0.6 * Sp.shape[1]); ntail = max(3, nb // 10)
        resid = Sp.mean(0)[:nb] - Cp.mean(0)[:nb]
        tail = float(resid[:ntail].mean())
        scale = float(np.std(Cp.mean(0)[:ntail]) / np.sqrt(m))
        s1_sig[tag] = bool(abs(tail) > Z * scale)
        # ---- kappa_sys (3051 estimator, per-arm windows)
        Db = D.mean(0); Dv = Db - Db[LATE].mean()
        boots2 = np.empty((NBOOT, T_END))
        idx = rng.integers(0, m, size=(NBOOT, m))
        for b in range(NBOOT): boots2[b] = D[idx[b]].mean(0)
        sig_t = boots2.std(0)
        def est(Dv_, sig_):
            W = []
            for t in range(t_post, T_END - base):
                if abs(Dv_[t]) > 3 * sig_[t]: W.append(t)
                else: break
            if len(W) >= 8:
                w = np.array(W); y = np.log(np.abs(Dv_[w]))
                wt = (np.abs(Dv_[w]) / sig_[w]) ** 2
                return float(np.exp(np.polyfit(w, y, 1, w=np.sqrt(wt))[0])), 'FIT'
            for t in range(t_post - 1, T_STEP, -1):
                if abs(Dv_[t]) > 3 * sig_[t]:
                    return float((3 * sig_[t_post] / abs(Dv_[t]))
                                 ** (1.0 / (t_post - t))), 'BOUND'
            return np.nan, 'INDET'
        k, br = est(Dv, sig_t)
        ks = []
        for b in range(NBOOT):
            Dd = boots2[b] - boots2[b][LATE].mean()
            kb, _ = est(Dd, sig_t)
            if not np.isnan(kb): ks.append(kb)
        hi = float(np.percentile(ks, 99.5)) if ks else np.nan
        lo = float(np.percentile(ks, 0.5)) if ks else np.nan
        kappa[tag] = (k, lo, hi, br)
        print(f"[{tag}|{cls}|DT={dt:+.0f}] pairs {m}/{n}  S3-C: sust={sust:.3e} "
              f"band[{band/2:.2e},{band*2:.2e}] -> "
              f"{'PASS' if s3_pass[tag] else 'FAIL'}  "
              f"S1-C: tail={tail:.3e} (scale {scale:.3e}) -> "
              f"{'SIGNIFICANT' if s1_sig[tag] else 'c.w.z.'}  "
              f"kappa_sys[{br}]={k:.4f} 99%CI[{lo:.4f},{hi:.4f}]")

    iso = [a[0] for a in ARMS if a[1] == 'iso']
    valid = [t for t in iso if s3_pass[t]]
    zero = [t for t in valid if t in ('a0', 'a0p')]
    nonzero = [t for t in valid if t not in ('a0', 'a0p')]
    print("-" * 70)
    if len(valid) < 2 or not s3_pass['ak']:
        print("DISPOSITION: DISP-I3 INSTRUMENT — fewer than two isolation "
              "arms pass S3-C, or AK fails S3-C; no standing; panel.")
    elif any(s1_sig[t] for t in nonzero):
        f = [t for t in nonzero if s1_sig[t]]
        print(f"DISPOSITION: DISP-T THE FALSIFIER FIRES — control-valid tail "
              f"at DT != 0 in {f}; indictment of T-3 §6 / B-1 L-4 / L-6 "
              f"SUSTAINED; item 1B FAILS; Candidate (B) fails requirement 7.")
    else:
        p_iso = (len(zero) == 2 and all(s1_sig[t] for t in zero)
                 and all(not s1_sig[t] for t in nonzero))
        kk = kappa['ak']
        p_k = (kk[3] == 'FIT') and (kk[2] < 1.0)
        if p_iso and p_k:
            print("DISPOSITION: DISP-R RETIREMENT FINALIZED + MARGIN "
                  "CERTIFIED — the artifact reproduces at BOTH DT=0 "
                  "geometries and is absent at every valid DT != 0 arm; "
                  f"kappa_sys = {kk[0]:.4f} (99% upper {kk[2]:.4f}) < 1 at "
                  "AK; item 1B DISCHARGES -> SEVEN OF SEVEN. Panel confirms.")
        elif p_iso:
            print("DISPOSITION: DISP-P PARTIAL — isolation established (the "
                  "tail question retires); the margin leg remains open "
                  f"(AK branch {kk[3]}, 99% upper {kk[2]:.4f}); panel scopes.")
        elif 'a0' in valid and not s1_sig['a0']:
            print("DISPOSITION: DISP-X — the artifact fails to reproduce at "
                  "A0; the geometric diagnosis fails; Q1 standing reopens.")
        elif 'a0' in valid and s1_sig['a0'] and 'a0p' in valid and not s1_sig['a0p']:
            print("DISPOSITION: DISP-G GEOMETRY-SPECIFIC — the artifact is "
                  "real at the Route B box but does NOT follow DT=0 into a "
                  "distinct geometry; the DT mechanism is refuted; panel "
                  "re-diagnoses.")
        else:
            print("DISPOSITION: DISP-M3 IMPASSE — conflicted pattern; panel.")
    print("Evidentiary standing: NONE until the single panel round "
          "(prereg v2, Patch 3055 §5).")

if __name__ == '__main__':
    raise SystemExit(main())

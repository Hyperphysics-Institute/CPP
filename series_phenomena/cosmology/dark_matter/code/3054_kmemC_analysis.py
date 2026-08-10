#!/usr/bin/env python3
"""3054_kmemC_analysis.py — K-MEM ROUTE C frozen analysis.

Implements `kmemC_routeC_prereg.md` (Patch 3053) §4–§5 VERBATIM.
REFUSES an incomplete manifest (no interim looks). Disposition printed
in the §5 tree language ONLY, evaluated in the frozen order. Standing
NONE until the single panel round.
"""
import glob, json, os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.normpath(os.path.join(HERE, '../data/kmemC'))
T_STEP, T_END, LATE = 24, 288, slice(240, 288)
Z, NBOOT, BOOT_SEED, CHUNK = 2.576, 10000, 30530811, 4
SUST_REF0, SNR_NOTE = 2.6e-3, 10.0
ARMS = [('a0','diag',128,24.0), ('a1','inf',384,20.0),
        ('a2','inf',384,24.0), ('a3','inf',384,16.0)]

def band_psd(sig):
    f = np.fft.rfft(sig - sig.mean())
    return (np.abs(f) ** 2)[1:]

def main():
    cal = json.load(open(os.path.join(DATA, 'calibration.json')))
    rep = json.load(open(os.path.join(DATA, 'pilot_report.json')))
    beta_f = rep['beta_f']
    missing = 0
    F = {}
    for tag, role, n, _x in ARMS:
        for p in range(n):
            for br in ('step', 'ctrl'):
                pth = os.path.join(DATA, f'leg_{p:04d}_{br}_{tag}.json')
                if not os.path.exists(pth):
                    missing += 1; continue
                F[(p, br, tag)] = np.array(json.load(open(pth))['F'])
    total = sum(a[2] for a in ARMS) * 2
    if missing:
        print(f"REFUSING TO RUN: manifest incomplete — {missing}/{total} "
              "legs missing."); return 2

    excl = {tag: set() for tag, *_ in ARMS}
    for (p, br, tag), arr in F.items():
        if not np.isfinite(arr).all(): excl[tag].add(p)

    rng = np.random.default_rng(BOOT_SEED)
    s3_pass, s1_sig, kappa = {}, {}, {}
    band = (SUST_REF0 * beta_f / 0.10)
    for tag, role, n, x_half in ARMS:
        used = [p for p in range(n) if p not in excl[tag]]
        m = len(used)
        S = np.stack([F[(p, 'step', tag)] for p in used])
        C = np.stack([F[(p, 'ctrl', tag)] for p in used])
        D = S - C
        t_close = int(cal[tag]['T_close']); t_post = t_close + 6
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
            for t in range(t_post, 240):
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
        print(f"[{tag}|{role}] pairs {m}/{n}  S3-C: sust={sust:.3e} "
              f"band[{band/2:.2e},{band*2:.2e}] -> "
              f"{'PASS' if s3_pass[tag] else 'FAIL'}  "
              f"S1-C: tail={tail:.3e} (scale {scale:.3e}) -> "
              f"{'SIGNIFICANT' if s1_sig[tag] else 'c.w.z.'}  "
              f"kappa_sys[{br}]={k:.4f} 99%CI[{lo:.4f},{hi:.4f}]")

    inf_arms = [t for t, r, *_ in ARMS if r == 'inf']
    valid = [t for t in inf_arms if s3_pass[t]]
    print("-" * 70)
    # ---- frozen tree, in order
    if len(valid) < 2:
        print("DISPOSITION: DISP-I2 INSTRUMENT — fewer than two inferential "
              "arms pass S3-C; no tail or margin standing; panel diagnoses.")
    elif any(s1_sig[t] for t in valid):
        firing = [t for t in valid if s1_sig[t]]
        print(f"DISPOSITION: DISP-T THE FALSIFIER FIRES — control-valid "
              f"domain-robust tail in {firing}; the indictment of T-3 §6 / "
              f"B-1 L-4 / L-6 is SUSTAINED; item 1B FAILS on its named "
              f"falsifier; Candidate (B) fails requirement 7. Panel confirms.")
    else:
        p_iso = s1_sig['a0'] and all(not s1_sig[t] for t in valid)
        p_k = all((kappa[t][3] == 'FIT') and (kappa[t][2] < 1.0)
                  for t in valid)
        if p_iso and p_k:
            print("DISPOSITION: DISP-R RETIREMENT FINALIZED + MARGIN "
                  "CERTIFIED — the artifact is experimentally isolated "
                  "(present at DT=0, absent at DT=+-) and kappa_sys < 1 "
                  "certified in every valid arm; item 1B DISCHARGES -> "
                  "SEVEN OF SEVEN. Panel single round confirms.")
        elif p_iso:
            print("DISPOSITION: DISP-P PARTIAL — isolation stands (the "
                  "tail question retires); the margin leg remains open; "
                  "panel scopes the residual.")
        elif not s1_sig['a0']:
            print("DISPOSITION: DISP-X — A0 shows NO artifact; the "
                  "geometric diagnosis fails reproduction; all Q1 standing "
                  "reopens; panel (impasse-class).")
        else:
            print("DISPOSITION: DISP-M2 IMPASSE — conflicted pattern; "
                  "panel.")
    print("Evidentiary standing: NONE until the single panel round "
          "(prereg 3053 §5).")

if __name__ == '__main__':
    raise SystemExit(main())

#!/usr/bin/env python3
"""PATCH 2922 -- HYBRID ROUND 3b EXECUTION against the FROZEN prereg of
Patch 2921: parity-clean evaluator (linear interpolation between bin
centers, abort-grade exact-zero assert), odd-projected p0 channel;
everything else inherited verbatim from 2919/2920 (data, basis, gate,
bands, bootstrap, sanity register)."""
import json
import numpy as np

def pool(legs):
    M = np.array([np.array(e["S_px"])/np.maximum(np.array(e["N"]),1) for e in legs])
    W = np.array([e["N"] for e in legs], float)
    Nt = W.sum(0); wm = (M*W).sum(0)/np.maximum(Nt,1)
    var = ((M-wm)**2*W).sum(0)/np.maximum(Nt,1)
    return wm, np.sqrt(var/len(legs)), Nt

mob = json.load(open('data/2917_round2_legs_raw.json'))
ctl = json.load(open('data/2918_control_legs_raw.json'))
DESIGN = [(0.04,125),(0.07,107),(0.10,100),(0.14,89),(0.20,63),(0.0,63),(0.0,125)]
DATA = {}
for b,T in DESIGN[:5]:
    DATA[(b,T)] = pool([e for e in mob if abs(e["beta"]-b)<1e-9])
for b,T in DESIGN[5:]:
    DATA[(b,T)] = pool([e for e in ctl if e["T_meas"]==T])
mask = np.all([DATA[k][2] >= 200 for k in DESIGN], axis=0)
nb = int(mask.sum()); print(f"admitted bins: {nb}/72")

X = np.array([[1.0, 1.0/T, b, b**3] for b,T in DESIGN])
def fit_all(maps, ses):
    P = np.zeros((4,72)); chi2 = 0.0
    Y = np.stack([maps[k] for k in DESIGN]); S = np.stack([ses[k] for k in DESIGN])
    for j in np.where(mask)[0]:
        w = 1.0/S[:,j]; A = X*w[:,None]; y = Y[:,j]*w
        coef, *_ = np.linalg.lstsq(A, y, rcond=None)
        P[:,j] = coef; chi2 += float(((A@coef - y)**2).sum())
    return P, chi2
maps = {k: DATA[k][0] for k in DESIGN}; ses = {k: DATA[k][1] for k in DESIGN}
P, chi2 = fit_all(maps, ses)
print(f"ADEQUACY GATE (inherited, unchanged): chi2/dof = {chi2/(3*nb):.3f}  "
      f"({'PASS' if chi2/(3*nb) < 1.5 else 'FAIL'})")
gate_pass = chi2/(3*nb) < 1.5

# ---------- Stage 2, PARITY-CLEAN evaluator ----------
SOFT2 = 0.05**2
XC = np.arange(-11.5, 11.5+1e-9, 1.0)          # 24 bin centers
sp = 2.5
xs = sp*np.arange(-6,7); ys = sp*np.arange(-3,4)
cells = np.array([(x,y,z) for x in xs for y in ys for z in ys
                  if 1.0 <= np.hypot(y,z) <= 8.0])
rho_cell = np.hypot(cells[:,1], cells[:,2])
ring = np.searchsorted([3.0,5.0], rho_cell)

def kernel_axial(Rvec, pvec):
    xp = Rvec + 0.5*pvec; xm = Rvec - 0.5*pvec
    def f(x):
        r2 = (x*x).sum(-1); r = np.sqrt(r2)
        a = 1.0/(4*np.pi*(r2+SOFT2))
        return -a*x[...,0]/np.maximum(r,1e-12)
    return f(xp) - f(xm)

def pattern_at(patmap, ringidx, xi):
    """Linear interpolation between bin centers per ring; 0 outside [-11.5, 11.5]."""
    out = np.zeros_like(xi)
    for r in range(3):
        m = ringidx == r
        out[m] = np.interp(xi[m], XC, patmap[r], left=0.0, right=0.0)
    return out

def drive_from(patmap, beta):
    xi = cells[:,0]; dcur = np.sqrt((cells**2).sum(1))
    xi_ret = xi + beta*dcur
    pvec = np.zeros_like(cells); pvec[:,0] = pattern_at(patmap, ring, xi_ret)
    return kernel_axial(cells, pvec).sum()

def oddify(m): return 0.5*(m - m[:, ::-1])

# ABORT-GRADE parity assert (frozen 2921 s1): exact odd pattern -> exact zero
test = oddify(np.random.default_rng(0).normal(0,1,(3,24)))
z_test = drive_from(test, 0.0)
assert abs(z_test) < 1e-15, f"EVALUATOR PARITY ASSERT FAILED: {z_test}"
print(f"evaluator parity assert: |D0(0)|_exact-odd = {abs(z_test):.1e} < 1e-15  PASS")

BS = np.linspace(0.03, 0.25, 12)
def channels(P):
    p0m = oddify((P[0]*mask).reshape(3,24))               # frozen s2 projection
    even_res = (P[0]*mask).reshape(3,24) - p0m
    p1m = (P[2]*mask).reshape(3,24); p3m = (P[3]*mask).reshape(3,24)
    D0 = np.array([drive_from(p0m, b) for b in BS])
    D1 = np.array([drive_from(b*p1m + b**3*p3m, b) for b in BS])
    Xf = np.column_stack([BS, BS**3])
    k0, k03 = np.linalg.lstsq(Xf, D0, rcond=None)[0]
    kt, k3t = np.linalg.lstsq(Xf, D0+D1, rcond=None)[0]
    k1 = np.linalg.lstsq(Xf, D1, rcond=None)[0][0]
    return k0, -k03/k0, k1, kt, -k3t/kt, float(np.sqrt(np.mean(even_res**2)))

k0, c0, k1, ktot, ctot, evres = channels(P)
print(f"central: k0={k0:+.5e}  c0={c0:+.4f}   k1={k1:+.5e}   k_tot={ktot:+.5e}  c_tot={ctot:+.4f}")
print(f"even residue of p0 (noise gauge, unbanded): rms = {evres:.4f}")

rng = np.random.default_rng(2922)
B = {q: [] for q in ("c0","ctot","k0","k1","ktot")}
for _ in range(200):
    mb = {k: maps[k] + rng.normal(0,1,72)*ses[k] for k in DESIGN}
    Pb, _ = fit_all(mb, ses)
    bk0, bc0, bk1, bkt, bct, _ = channels(Pb)
    for q,v in zip(("c0","ctot","k0","k1","ktot"),(bc0,bct,bk0,bk1,bkt)): B[q].append(v)
B = {k: np.array(v) for k,v in B.items()}
s_c0, s_ct = B["c0"].std(ddof=1), B["ctot"].std(ddof=1)
print(f"bootstrap: c0 = {np.median(B['c0']):+.4f} +/- {s_c0:.4f}  "
      f"(16-84%: {np.percentile(B['c0'],16):+.3f} .. {np.percentile(B['c0'],84):+.3f})")
print(f"           c_tot = {np.median(B['ctot']):+.4f} +/- {s_ct:.4f}  "
      f"(16-84%: {np.percentile(B['ctot'],16):+.3f} .. {np.percentile(B['ctot'],84):+.3f})")
print(f"           k_tot = {np.median(B['ktot']):+.5e} +/- {B['ktot'].std(ddof=1):.2e}")

# sanity register (inherited)
c2918 = json.load(open('data/2918_control_fields.json'))
m125 = np.array(c2918['m125']); p0f = P[0]*mask
corr = float(np.corrcoef(p0f[mask], m125[mask])[0,1])
ampr = float(np.sqrt(np.mean(p0f[mask]**2))/np.sqrt(np.mean(m125[mask]**2)))
print(f"sanity (i): k0+k1 = {k0+k1:+.5e} [+0.011..0.014]; (ii) corr={corr:+.3f} ampr={ampr:.2f}")

def verdict():
    if not gate_pass: return "INCONCLUSIVE-MODEL"
    out = []
    if s_c0 <= 0.05:
        if abs(c0-0.2) < 0.05: out.append("STATIC-SEA CONFIRMED (provisional)")
        elif abs(c0-0.2) > 0.15: out.append("STATIC-SEA REFUTED (provisional)")
        else: out.append("STATIC-SEA INTERMEDIATE")
    else: out.append("STATIC-SEA INCONCLUSIVE (sigma)")
    if s_ct <= 0.05:
        if abs(ctot) < 0.05: out.append("TOTAL-CANCELLATION (provisional)")
        elif 0.10 <= ctot <= 0.30: out.append("TOTAL-RETAINED (provisional)")
        else: out.append("TOTAL-INTERMEDIATE (s4 commitment engages)")
    else: out.append("TOTAL INCONCLUSIVE (sigma)")
    return " | ".join(out)
V = verdict(); print("VERDICT:", V)
json.dump(dict(nb=nb, chi2_dof=chi2/(3*nb), k0=k0, c0=c0, k1=k1, ktot=ktot,
               ctot=ctot, s_c0=float(s_c0), s_ctot=float(s_ct),
               even_residue=evres, corr=corr, amp_ratio=ampr,
               boot={k: float(np.median(v)) for k,v in B.items()},
               verdict=V), open('data/2922_round3b_results.json','w'), indent=1)
print("archived: data/2922_round3b_results.json")

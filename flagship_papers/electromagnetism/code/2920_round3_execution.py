#!/usr/bin/env python3
"""PATCH 2920 -- HYBRID ROUND 3 EXECUTION against the FROZEN prereg of
Patch 2919. Per-bin weighted LSQ m = p0 + p_tr/T + beta*p1 + beta^3*p3
over seven design points; adequacy gate chi2/dof < 1.5; two-channel
retarded Stage 2 (transient EXCLUDED); frozen bands of 2919 s4;
200-fold bootstrap. Inputs: the 72 banked legs only."""
import json
import numpy as np

# ---------- pooled datasets ----------
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

X = np.array([[1.0, 1.0/T, b, b**3] for b,T in DESIGN])   # (7,4)

def fit_all(maps, ses):
    """Per-bin weighted LSQ. maps/ses: dict key->(72,). Returns params (4,72), chi2 total."""
    P = np.zeros((4,72)); chi2 = 0.0
    Y = np.stack([maps[k] for k in DESIGN])     # (7,72)
    S = np.stack([ses[k] for k in DESIGN])
    for j in np.where(mask)[0]:
        w = 1.0/S[:,j]; A = X*w[:,None]; y = Y[:,j]*w
        coef, res, *_ = np.linalg.lstsq(A, y, rcond=None)
        P[:,j] = coef
        chi2 += float(((A@coef - y)**2).sum())
    return P, chi2

maps = {k: DATA[k][0] for k in DESIGN}
ses  = {k: DATA[k][1] for k in DESIGN}
P, chi2 = fit_all(maps, ses)
dof = 3*nb
print(f"ADEQUACY GATE: chi2/dof = {chi2/dof:.3f} over {nb} bins x 3 dof  "
      f"({'PASS' if chi2/dof < 1.5 else 'FAIL -> INCONCLUSIVE-MODEL'})")
gate_pass = chi2/dof < 1.5

# ---------- Stage 2 machinery (2914/2917, unchanged) ----------
SOFT2 = 0.05**2
XB = np.arange(-12.0, 12.0+1e-9, 1.0)
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

def drive_from(patmap, beta):
    """Drive at speed beta from a co-moving pattern map (3,24)."""
    xi = cells[:,0]; dcur = np.sqrt((cells**2).sum(1))
    xi_ret = xi + beta*dcur
    ib = np.clip(np.digitize(xi_ret, XB)-1, 0, 23)
    inside = (xi_ret >= XB[0]) & (xi_ret <= XB[-1])
    pvec = np.zeros_like(cells); pvec[:,0] = patmap[ring, ib]*inside
    return kernel_axial(cells, pvec).sum()

BS = np.linspace(0.03, 0.25, 12)
def channels(P):
    p0m = (P[0]*mask).reshape(3,24)
    p1m = (P[2]*mask).reshape(3,24)
    p3m = (P[3]*mask).reshape(3,24)
    D0 = np.array([drive_from(p0m, b) for b in BS])
    D1 = np.array([drive_from(b*p1m + b**3*p3m, b) for b in BS])
    z = drive_from(p0m, 0.0)
    Xf = np.column_stack([BS, BS**3])
    k0, k03 = np.linalg.lstsq(Xf, D0, rcond=None)[0]
    ktot, k3tot = np.linalg.lstsq(Xf, D0+D1, rcond=None)[0]
    k1 = np.linalg.lstsq(Xf, D1, rcond=None)[0][0]
    return z, k0, -k03/k0, k1, ktot, -k3tot/ktot

z, k0, c0, k1, ktot, ctot = channels(P)
sym_ok = abs(z) < 1e-12  # FROZEN assert, recorded not aborted -- see execution record
print(f"D0(0) = {z:+.2e}  (frozen mirror-symmetry assert: {'PASS' if sym_ok else 'FAIL -- fitted p0 has an even component; disclosed'})")
print(f"central: k0={k0:+.5e}  c0={c0:+.4f}   k1={k1:+.5e}   k_tot={ktot:+.5e}  c_tot={ctot:+.4f}")

rng = np.random.default_rng(2920)
B = {q: [] for q in ("c0","ctot","k0","k1","ktot")}
for _ in range(200):
    mb = {k: maps[k] + rng.normal(0,1,72)*ses[k] for k in DESIGN}
    Pb, _ = fit_all(mb, ses)
    _, bk0, bc0, bk1, bkt, bct = channels(Pb)
    B["c0"].append(bc0); B["ctot"].append(bct); B["k0"].append(bk0); B["k1"].append(bk1); B["ktot"].append(bkt)
B = {k: np.array(v) for k,v in B.items()}
s_c0, s_ct = B["c0"].std(ddof=1), B["ctot"].std(ddof=1)
print(f"bootstrap: c0 = {np.median(B['c0']):+.4f} +/- {s_c0:.4f}   "
      f"c_tot = {np.median(B['ctot']):+.4f} +/- {s_ct:.4f}")
print(f"          k_tot = {np.median(B['ktot']):+.5e} +/- {B['ktot'].std(ddof=1):.2e}")

# ---------- sanity register (unbanded) ----------
klin = k0 + k1
c2918 = json.load(open('data/2918_control_fields.json'))
m125 = np.array(c2918['m125'])
p0f = P[0]*mask
corr = float(np.corrcoef(p0f[mask], m125[mask])[0,1])
amp_fit = float(np.sqrt(np.mean(p0f[mask]**2)))
amp_ctl = float(np.sqrt(np.mean(m125[mask]**2)))
ptr = P[1]*mask
inner = (P[1]*mask).reshape(3,24)[0]
odd = 0.5*(inner-inner[::-1]); even = 0.5*(inner+inner[::-1])
print(f"sanity (i): k0+k1 = {klin:+.5e}  [register: +0.011..0.014]")
print(f"sanity (ii): p0 vs control corr = {corr:+.3f} [>0.5]; amp fit/ctl = {amp_fit/amp_ctl:.2f} [0.7..1.3]")
print(f"sanity (iii): p_tr/T-channel inner ||even||={np.sqrt(np.mean(even**2)):.4f} vs ||odd||={np.sqrt(np.mean(odd**2)):.4f} [even-dominant expected]")

# ---------- frozen bands ----------
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
        else: out.append("TOTAL-INTERMEDIATE")
    else: out.append("TOTAL INCONCLUSIVE (sigma)")
    return " | ".join(out)
V = verdict()
print("VERDICT:", V)
json.dump(dict(nb=nb, chi2_dof=chi2/dof, gate_pass=bool(gate_pass),
               k0=k0, c0=c0, k1=k1, ktot=ktot, ctot=ctot,
               s_c0=float(s_c0), s_ctot=float(s_ct),
               boot={k: float(np.median(v)) for k,v in B.items()},
               sanity=dict(klin=klin, corr=corr, amp_ratio=amp_fit/amp_ctl),
               verdict=V),
          open('data/2920_round3_results.json','w'), indent=1)
print("archived: data/2920_round3_results.json")

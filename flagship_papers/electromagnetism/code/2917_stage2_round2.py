#!/usr/bin/env python3
"""PATCH 2917 Stage 2, ROUND 2 -- deterministic retarded drive from the
MEASURED round-2 response field. Identical machinery to 2914 Stage 2
(quasi-static emitters, trivial reception retardation, dipole state at
xi_ret = xi + beta*d, engine-matched softening); the ONLY changes frozen
at 2914 s4: five betas in the (beta, beta^3) per-bin fit (3 dof), and
the fresh round-2 fields file as input. Bands unchanged (2913 s3):
CANCELLATION |c|<0.05 / RETAINED [0.10,0.30] / sigma_c <= 0.05 required;
static-Sea target c = 1/5 exactly (2900). Bootstrap 200-fold.
"""
import json
import numpy as np

SOFT2 = 0.05**2
XB = np.arange(-12.0, 12.0+1e-9, 1.0)
RB = [(1.0,3.0),(3.0,5.0),(5.0,8.0)]
BETAS_FIT = (0.04, 0.07, 0.10, 0.14, 0.20)

d = json.load(open('data/2917_response_fields_round2.json'))['fields']
key = {0.04:'0.04',0.07:'0.07',0.10:'0.1',0.14:'0.14',0.20:'0.2'}
M  = {b: np.array(d[key[b]]['m']).reshape(3,24)  for b in BETAS_FIT}
SE = {b: np.array(d[key[b]]['se']).reshape(3,24) for b in BETAS_FIT}

sp = 2.5
xs = sp*np.arange(-6,7); ys = sp*np.arange(-3,4)
cells = np.array([(x,y,z) for x in xs for y in ys for z in ys
                  if 1.0 <= np.hypot(y,z) <= 8.0])
rho_cell = np.hypot(cells[:,1], cells[:,2])
ring = np.searchsorted([3.0,5.0], rho_cell)

def fit_p13(Mmaps):
    A = np.array([[b, b**3] for b in BETAS_FIT])
    AtAinv = np.linalg.inv(A.T@A)
    P = np.stack([Mmaps[b] for b in BETAS_FIT])
    coef = np.einsum('ij,jkl->ikl', AtAinv@A.T, P)
    return coef[0], coef[1]

def kernel_axial(Rvec, pvec):
    xp = Rvec + 0.5*pvec; xm = Rvec - 0.5*pvec
    def f(x):
        r2 = (x*x).sum(-1); r = np.sqrt(r2)
        a = 1.0/(4*np.pi*(r2+SOFT2))
        return -a*x[...,0]/np.maximum(r,1e-12)
    return f(xp) - f(xm)

def drive(beta, p1, p3):
    xi = cells[:,0]; dcur = np.sqrt((cells**2).sum(1))
    xi_ret = xi + beta*dcur
    ib = np.clip(np.digitize(xi_ret, XB)-1, 0, 23)
    inside = (xi_ret >= XB[0]) & (xi_ret <= XB[-1])
    p_ax = beta*p1[ring, ib]*inside + beta**3*p3[ring, ib]*inside
    pvec = np.zeros_like(cells); pvec[:,0] = p_ax
    return kernel_axial(cells, pvec).sum()

def c_from(p1, p3):
    bs = np.linspace(0.03, 0.25, 12)
    Ds = np.array([drive(b, p1, p3) for b in bs])
    X = np.column_stack([bs, bs**3])
    coef, *_ = np.linalg.lstsq(X, Ds, rcond=None)
    k, k3 = coef
    return k, -k3/k

p1, p3 = fit_p13(M)
k, c = c_from(p1, p3)
print(f"central: k_h = {k:+.5e}   c_hyb = {c:+.4f}")

rng = np.random.default_rng(2917)
cs, ks = [], []
for _ in range(200):
    Mb = {b: M[b] + rng.normal(0, 1, M[b].shape)*SE[b] for b in BETAS_FIT}
    q1, q3 = fit_p13(Mb)
    kk, cc = c_from(q1, q3)
    ks.append(kk); cs.append(cc)
cs = np.array(cs); ks = np.array(ks)
sig = cs.std(ddof=1)
print(f"bootstrap: c_hyb = {np.median(cs):+.4f}  sigma_c = {sig:.4f}  "
      f"(16-84%: {np.percentile(cs,16):+.3f} .. {np.percentile(cs,84):+.3f})")
print(f"          k_h  = {np.median(ks):+.5e}  sigma_k = {ks.std(ddof=1):.2e}")
print(f"frozen gate sigma_c <= 0.05: {sig <= 0.05}")
if sig <= 0.05:
    if abs(c) < 0.05: band = "CANCELLATION (provisional)"
    elif 0.10 <= c <= 0.30: band = "RETAINED (provisional)"
    else: band = "INTERMEDIATE"
else:
    band = "INCONCLUSIVE (sigma_c > 0.05)"
print("BAND:", band, "   [static-Sea target: c = 1/5 = 0.2000 exactly]")
json.dump(dict(k=float(k), c=float(c), boot_median=float(np.median(cs)),
               sigma_c=float(sig), p16=float(np.percentile(cs,16)),
               p84=float(np.percentile(cs,84)), band=band, round=2,
               betas=list(BETAS_FIT), legs=60),
          open('data/2917_stage2_round2_c_hyb.json','w'), indent=1)

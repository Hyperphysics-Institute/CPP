#!/usr/bin/env python3
"""PATCH 2914 Stage 2 -- deterministic retarded drive from the MEASURED
response field, beta^3 term modelled per the frozen prereg branch.
Emitters are quasi-static (centres fixed); reception retardation is
trivial (d = current distance); the dipole STATE at emission is the
co-moving pattern at xi_ret = xi + beta*d. Softening matches the engine.
Bootstrap propagates binwise SEs into c_hyb."""
import json
import numpy as np

SOFT2 = 0.05**2
XB = np.arange(-12.0, 12.0+1e-9, 1.0)
XC = 0.5*(XB[:-1]+XB[1:])
RB = [(1.0,3.0),(3.0,5.0),(5.0,8.0)]
BETAS_FIT = (0.05, 0.10, 0.20)

d = json.load(open('data/2914_response_fields.json'))['fields']
M = {float(b): np.array(d[b]['m']).reshape(3,24) for b in d}
SE = {float(b): np.array(d[b]['se']).reshape(3,24) for b in d}

# grid cells of the physical Sea (class-A geometry): centres
sp = 2.5
xs = sp*np.arange(-6,7); ys = sp*np.arange(-3,4)
cells = [(x,y,z) for x in xs for y in ys for z in ys
         if 1.0 <= np.hypot(y,z) <= 8.0]
cells = np.array(cells)
rho_cell = np.hypot(cells[:,1], cells[:,2])
ring = np.searchsorted([3.0,5.0], rho_cell)  # 0,1,2
rhat = np.zeros_like(cells); rhat[:,1] = cells[:,1]/rho_cell; rhat[:,2] = cells[:,2]/rho_cell

def fit_p13(Mmaps):
    """Per (ring, xi-bin): p = b*p1 + b^3*p3 least squares through 3 betas."""
    A = np.array([[b, b**3] for b in BETAS_FIT])
    AtAinv = np.linalg.inv(A.T@A)
    P = np.stack([Mmaps[b] for b in BETAS_FIT])          # (3,3,24)
    coef = np.einsum('ij,jkl->ikl', AtAinv@A.T, P)       # (2,3,24)
    return coef[0], coef[1]                              # p1, p3 maps

def kernel_axial(Rvec, pvec):
    """Axial force on +1 source at origin from unit-charge pair with
    dipole vector p at position Rvec (pair centre), softened engine kernel."""
    xp = Rvec + 0.5*pvec; xm = Rvec - 0.5*pvec
    def f(x):
        r2 = (x*x).sum(-1); r = np.sqrt(r2)
        a = 1.0/(4*np.pi*(r2+SOFT2))
        return -a*x[...,0]/np.maximum(r,1e-12)   # force ON source along -x_hat(pair->...) : source at origin, pair at Rvec: direction pair->source = -Rvec; repulsion from + charge pushes source along (0-xp)/|..| i.e. -xp/|xp|
    return f(xp) - f(xm)

def drive(beta, p1, p3):
    xi = cells[:,0]
    dcur = np.sqrt((cells**2).sum(1))
    xi_ret = xi + beta*dcur
    ib = np.clip(np.digitize(xi_ret, XB)-1, 0, 23)
    inside = (xi_ret >= XB[0]) & (xi_ret <= XB[-1])
    p1v = p1[ring, ib]*inside; p3v = p3[ring, ib]*inside
    p_ax = beta*p1v + beta**3*p3v
    pvec = np.zeros_like(cells); pvec[:,0] = p_ax
    return kernel_axial(cells, pvec).sum()

def c_from(p1, p3):
    bs = np.linspace(0.03, 0.25, 12)
    Ds = np.array([drive(b, p1, p3) for b in bs])
    X = np.column_stack([bs, bs**3])
    coef, *_ = np.linalg.lstsq(X, Ds, rcond=None)
    k, k3 = coef
    return k, -k3/k   # D = k b (1 - c b^2)  => c = -k3/k

p1, p3 = fit_p13(M)
k, c = c_from(p1, p3)
print(f"central: k_h = {k:+.5e}   c_hyb = {c:+.4f}")

rng = np.random.default_rng(2914)
cs = []
for _ in range(200):
    Mb = {b: M[b] + rng.normal(0, 1, M[b].shape)*SE[b] for b in BETAS_FIT}
    q1, q3 = fit_p13(Mb)
    cs.append(c_from(q1, q3)[1])
cs = np.array(cs)
print(f"bootstrap: c_hyb = {np.median(cs):+.4f}  sigma_c = {cs.std(ddof=1):.4f}  "
      f"(16-84%: {np.percentile(cs,16):+.3f} .. {np.percentile(cs,84):+.3f})")
print(f"frozen gate sigma_c <= 0.05: {cs.std(ddof=1) <= 0.05}")
json.dump(dict(k=k, c=c, boot_median=float(np.median(cs)),
               sigma_c=float(cs.std(ddof=1)),
               p16=float(np.percentile(cs,16)), p84=float(np.percentile(cs,84))),
          open('data/2914_stage2_c_hyb.json','w'), indent=1)

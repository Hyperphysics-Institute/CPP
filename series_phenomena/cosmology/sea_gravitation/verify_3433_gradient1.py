#!/usr/bin/env python3
# verify_3433_gradient1.py — G1: does arrangement change the mean expansion source?
# Step-A level test: surface-averaged inward gravitational flux over a comoving
# sphere, same enclosed mass, uniform vs strongly clumped arrangement.
# Gauss's theorem predicts EXACT invariance; the script measures it, and also
# the LOCAL surface-field variance (which SHOULD change wildly with clumping),
# exhibiting the field-level vs mean-level distinction the route conflated.
import numpy as np
rng = np.random.default_rng(3433)
G = 1.0; R = 1.0; N = 4000; M = 1.0; m = M/N; NS = 40000

def uniform_pts(n):
    p = rng.normal(size=(3*n, 3)); p /= np.linalg.norm(p, axis=1)[:, None]
    r = 0.92*R*rng.random(3*n)**(1/3)
    return (p*r[:, None])[:n]

def clumped_pts(n, k=25, s=0.02):
    centers = uniform_pts(k)          # radii <= 0.92 R
    out = np.empty((0, 3))
    while len(out) < n:
        idx = rng.integers(0, k, n)
        cand = centers[idx] + rng.normal(scale=s, size=(n, 3))
        cand = cand[np.linalg.norm(cand, axis=1) < 0.98*R]   # STRICTLY inside
        out = np.vstack([out, cand])
    return out[:n]

def flux_and_var(masses_pos):
    u = rng.normal(size=(NS, 3)); u /= np.linalg.norm(u, axis=1)[:, None]
    surf = R*u
    g_rad = np.zeros(NS)
    for i in range(0, NS, 2000):        # chunked pairwise field
        d = surf[i:i+2000, None, :] - masses_pos[None, :, :]
        r2 = np.einsum('ijk,ijk->ij', d, d)
        gvec = -G*m*np.einsum('ijk,ij->ik', d, r2**-1.5)
        g_rad[i:i+2000] = np.einsum('ik,ik->i', gvec, u[i:i+2000])
    mean_flux = 4*np.pi*R**2*np.mean(g_rad)          # ~ -4 pi G M_enc
    return mean_flux, np.std(g_rad), np.mean(g_rad)

fu, su, gu = flux_and_var(uniform_pts(N))
fc, sc, gc = flux_and_var(clumped_pts(N))
exact = -4*np.pi*G*M
# per-arrangement MC error on the mean flux: 4 pi R^2 * sigma/sqrt(NS)
mcu = 4*np.pi*R**2*su/np.sqrt(NS)/abs(exact)
mcc = 4*np.pi*R**2*sc/np.sqrt(NS)/abs(exact)
mc_err = np.hypot(mcu, mcc)          # error on the DIFFERENCE
diff  = abs(fc-fu)/abs(exact)
print(f"exact Gauss flux        : {exact:+.6f}")
print(f"uniform arrangement     : {fu:+.6f}   (rel dev {abs(fu-exact)/abs(exact):.2e})")
print(f"clumped arrangement     : {fc:+.6f}   (rel dev {abs(fc-exact)/abs(exact):.2e})")
print(f"arrangement difference  : {diff:.2e}  (MC error on difference {mc_err:.2e})")
print(f"local surface-g stddev  : uniform {su:.4f}   clumped {sc:.4f}   ratio {sc/su:.1f}x")
g1_effect = diff > 5*mc_err
print()
print("G1: arrangement effect on mean source beyond MC error?",
      "YES" if g1_effect else "NO — invariant (Gauss), field variance changed",
      f"{sc/su:.0f}x while mean did not")
print("F-G1 frozen reading:", "ROUTE SURVIVES" if g1_effect else
      "ROUTE DEAD at Step-A level (subject to G2 corpus audit)")

# --- multi-seed campaign: standardized arrangement differences over 8 seeds ---
print("\nmulti-seed campaign (8 seeds): standardized (clumped-uniform) flux differences")
zs = []
for seed in range(8):
    rng = np.random.default_rng(1000+seed)
    fu_, su_, _ = flux_and_var(uniform_pts(N))
    fc_, sc_, _ = flux_and_var(clumped_pts(N))
    err = 4*np.pi*R**2*np.hypot(su_, sc_)/np.sqrt(NS)
    zs.append((fc_-fu_)/err)
zs = np.array(zs)
print("z-scores:", np.array2string(zs, precision=2))
print(f"mean z = {zs.mean():+.2f} +/- {zs.std(ddof=1)/np.sqrt(len(zs)):.2f}   (bias test)")
biased = abs(zs.mean()) > 3*zs.std(ddof=1)/np.sqrt(len(zs))
print("systematic arrangement effect detected?", "YES" if biased else
      "NO — consistent with exact Gauss invariance")

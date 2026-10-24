"""Patch 4423 -- the founder: "Please proceed" on 4422's owed items. This patch: the lattice grain, on the REGISTERED relay.

The registered relay (GR-1j, Lemmas L1-L2, Theorem T-1): the two-level, discrete-time recurrence
    u(t + tau) + u(t - tau) = 2 [alpha M_R + (1 - alpha) I] u(t),
with M_R the mean over the PSR shell of radius R, and dispersion
    cos(omega tau) = alpha * m_R(k) + (1 - alpha),     m_R(k) = shell mean of cos(k . R e)
Continuum shell (N_V -> infinity): m_R = sinc(kR), isotropic; long-wavelength speed c = sqrt(alpha) R / (sqrt(3) tau)
(R-CSTAR-MAP: c = R_vac / (sqrt(3) t_P), so R_vac = sqrt(3) l_P at alpha = 1).

Part 1. The even (direction-free) term, alpha = 1, continuum shell: phase speed c[1 - (kR)^2/90], group speed c[1 - (kR)^2/30]
        (analytic; checked numerically here). In Planck units (R = sqrt(3) l_P): group 1 - (k l_P)^2/10, i.e. eta = -1/15 in
        E^2 = p^2 + m^2 + eta p^4 / M_P^2.
Part 2. The direction-dependent term, from a DISCRETE shell sample: the 12 icosahedral directions (a spherical 5-design, 4160)
        and a 32-point shell (icosahedron + dodecahedron vertices), against the continuum. Group speed over 4000 directions.
"""
import numpy as np
PHI = (1 + 5**0.5)/2
ico = []
for s1 in (1, -1):
    for s2 in (1, -1):
        ico += [[0, s1, s2*PHI], [s1, s2*PHI, 0], [s2*PHI, 0, s1]]
ico = np.array(ico, float); ico /= np.linalg.norm(ico, axis=1)[:, None]
dod = [[sx, sy, sz] for sx in (1, -1) for sy in (1, -1) for sz in (1, -1)]
for s1 in (1, -1):
    for s2 in (1, -1):
        dod += [[0, s1/PHI, s2*PHI], [s1/PHI, s2*PHI, 0], [s2*PHI, 0, s1/PHI]]
dod = np.array(dod, float); dod /= np.linalg.norm(dod, axis=1)[:, None]
shell32 = np.vstack([ico, dod])
rng = np.random.default_rng(4423)
dirs = rng.normal(size=(4000, 3)); dirs /= np.linalg.norm(dirs, axis=1)[:, None]

def omega(kR, shell=None, alpha=1.0):
    """omega*tau for wavenumber kR along each direction in dirs (tau = 1, R = 1)."""
    if shell is None:
        m = np.sinc(kR/np.pi)*np.ones(len(dirs))
    else:
        m = np.mean(np.cos(kR*(dirs @ shell.T)), axis=1)
    return np.arccos(alpha*m + 1 - alpha)

c = 1/np.sqrt(3)
print("Part 1 (continuum shell, alpha = 1): phase and group speed / c")
for kR in (0.4, 0.2, 0.1):
    w = omega(kR)[0]; h = 1e-5
    vg = (omega(kR + h)[0] - omega(kR - h)[0])/(2*h)
    print(f"  kR {kR:4.2f}: phase-1 {w/kR/c - 1:+.3e} (pred {-(kR**2)/90:+.3e})   group-1 {vg/c - 1:+.3e} (pred {-(kR**2)/30:+.3e})")

print("Part 2 (group speed / c over 4000 directions, alpha = 1):")
print(f"{'kR':>6s} | {'continuum spread':>16s} | {'12-pt: mean-1':>13s} {'12-pt spread':>12s} | {'32-pt: mean-1':>13s} {'32-pt spread':>12s}")
rows = []
for kR in (0.8, 0.4, 0.2, 0.1):
    h = 1e-4
    out = []
    for sh in (None, ico, shell32):
        vg = (omega(kR + h, sh) - omega(kR - h, sh))/(2*h)/c
        out.append((vg.mean() - 1, vg.max() - vg.min()))
    rows.append((kR, out))
    print(f"{kR:6.2f} | {out[0][1]:16.2e} | {out[1][0]:+13.3e} {out[1][1]:12.2e} | {out[2][0]:+13.3e} {out[2][1]:12.2e}")
k = np.array([r[0] for r in rows]); s12 = np.array([r[1][1][1] for r in rows]); s32 = np.array([r[1][2][1] for r in rows])
p12 = np.polyfit(np.log(k), np.log(s12), 1)[0]; p32 = np.polyfit(np.log(k[:2]), np.log(s32[:2]), 1)[0]
print(f"  direction spread scales as (kR)^{p12:.2f} for the 12-point shell (5-design); 32-point shell ~ (kR)^{p32:.2f} or smaller")
c12 = s12[-1]/k[-1]**4
print(f"  12-point coefficient: spread ~ {c12:.2e} (kR)^4")

print("\nPhysical sizes (R = sqrt(3) l_P, so kR = sqrt(3) E/E_P):")
for label, E_over_EP in (("visible light (2 eV)", 2e-9/1.22e19), ("TeV gamma ray", 1e3/1.22e19), ("3e20 eV cosmic ray", 3e11/1.22e19)):
    kR = np.sqrt(3)*E_over_EP
    print(f"  {label:22s} E/E_P {E_over_EP:.1e}: direction spread (12-pt) ~ {c12*kR**4:.0e}; even group slowing ~ {kR**2/30:.0e}")
print("  eta = -1/15 (universal, subluminal). Quoted bounds: time-of-flight E_QG,2 ~ 1e10-1e12 GeV (blind to E_QG,2 ~ 5e19 GeV);")
print("  UHECR threshold (Maccione et al. 2009, EFT, proton composition): |eta_p| < ~1e-6, loosening to ~1e-3 only where proton")
print("  and pion coefficients are both negative and nearly equal -- the universal case -- so eta = -1/15 is in tension by ~60x.")
print("  eta scales as (tau/t_P)^2 (R-CSTAR-MAP fixes only R/tau): the tension disappears for tau < ~0.12 t_P.")
print("  Composite suppression (eta_eff = eta sum x_i^3: proton 1/9, pion 1/4) breaks the near-equal condition; bound comparison open.")

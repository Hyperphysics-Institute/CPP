"""
2338 -- QUANTUM TREATMENT of the screened-residual elastic channel
(founder-gated follow-up 2; the single door left open by the 2337 family closure).

Physics: at dwarf velocities lambda_dB = 336-560 fm >> R_s -- the classical MC
chain (1870/71, 2336/37) is outside its validity there. This computes the
partial-wave quantum transport for the same central reduction:
    V(r) = -(S/r) e^{-r/R_s}  +  core,
mu = N*1408/2 MeV, sigma_T = (4pi/k^2) sum_l (l+1) sin^2(d_{l+1} - d_l)
(distinguishable convention -- apples-to-apples with the classical chain;
identical-boson symmetrization flagged as a systematic in the grading).

Core variants (the rod coat has no registered central quantum reduction --
sensitivity across variants is part of the answer):
    hs2 / hs5 / hs10 : hard sphere at 2 / 5 / 10 fm
    yuk              : soft repulsive Yukawa (N*E_ee) e^{-r}/r

Numerov, vectorized over l; phase shifts by log-derivative matching to
spherical Bessel/Neumann at r_match. Validation: (i) Born phase shifts for the
attractive Yukawa at weak coupling; (ii) high-velocity approach to the
classical value; (iii) bound-state count by node counting at E -> 0.

Usage:
    python3 2338_quantum_engine.py point            # registered point, all cores
    python3 2338_quantum_engine.py scan <core> <i>  # band-scan row i (S-grid)
Results accumulate in 2338_results.json.
"""
import numpy as np, json, os, sys, math

HBARC = 197.327
C_KMS = 299792.458
MEV_G = 1.783e-27
N_EL  = 18
M_ROD = N_EL*1408.0
MU    = M_ROD/2.0
E_EE  = 0.9
CHI   = ((1+5**0.5)/2)**-3/6.0
RS0   = 1.0/CHI            # 25.42 fm
S0    = 0.30               # MeV fm
VELS  = (30.0, 50.0, 200.0, 1150.0, 1500.0)

def kinematics(v_kms):
    v = v_kms/C_KMS
    E = 0.25*M_ROD*v*v                 # CM energy, MeV
    k = math.sqrt(2*MU*E)/HBARC        # fm^-1
    return E, k

def sph_jn_yn(lmax, x):
    """spherical bessel j_l(x), y_l(x), l = 0..lmax, upward recursion
    (fine here: x = k*r_match >= ~1.5 in all uses)."""
    j = np.zeros(lmax+2); y = np.zeros(lmax+2)
    j[0] = math.sin(x)/x; y[0] = -math.cos(x)/x
    if lmax >= 0:
        j1 = math.sin(x)/x**2 - math.cos(x)/x
        y1 = -math.cos(x)/x**2 - math.sin(x)/x
        j[1], y[1] = j1, y1
    for l in range(1, lmax+1):
        j[l+1] = (2*l+1)/x*j[l] - j[l-1]
        y[l+1] = (2*l+1)/x*y[l] - y[l-1]
    return j, y

def sph_derivs(lmax, x, j, y):
    jp = np.zeros(lmax+1); yp = np.zeros(lmax+1)
    for l in range(lmax+1):
        jp[l] = j[l]/x*l - j[l+1]
        yp[l] = y[l]/x*l - y[l+1]
    return jp, yp

def phase_shifts(E, S, Rs, core, lmax, dr=0.02):
    """Numerov for u_l'' = W_l(r) u_l, all l at once; log-derivative match at
    r_match. Carries only a consistent 3-point window (no stored-trajectory
    scale jumps)."""
    k = math.sqrt(2*MU*E)/HBARC
    r_match = 6.0*Rs
    if core.startswith("hs"):
        r0 = float(core[2:])
    else:
        r0 = 0.05
    n_tot = int(round((r_match - r0)/dr)) + 3
    rs = r0 + dr*np.arange(n_tot)
    V = -(S/rs)*np.exp(-rs/Rs)
    if core == "yuk":
        V = V + (N_EL*E_EE/rs)*np.exp(-rs)
    ls = np.arange(0, lmax+1)
    W = (ls*(ls+1))[None, :]/rs[:, None]**2 + (2*MU/HBARC**2)*(V[:, None] - E)
    f = 1.0 - (dr*dr/12.0)*W
    u_a = np.zeros(lmax+1)          # u at rs[0]
    u_b = np.full(lmax+1, dr)       # u at rs[1]: wall/origin-adjacent linear seed
    iM = n_tot - 2                  # extract at rs[iM] with neighbors iM-1, iM+1
    uM_m1 = uM = uM_p1 = None
    for n in range(1, n_tot - 1):
        u_c = ((12.0 - 10.0*f[n])*u_b - f[n-1]*u_a)/f[n+1]
        m = np.max(np.abs(u_c))
        if m > 1e100 and n + 1 < iM - 2:
            u_b = u_b/m; u_c = u_c/m
        if n + 1 == iM - 1:
            uM_m1 = u_c.copy(); _scale_anchor = True
        elif n + 1 == iM:
            uM = u_c.copy()
        elif n + 1 == iM + 1:
            uM_p1 = u_c.copy()
        u_a, u_b = u_b, u_c
    # NOTE: window values collected AFTER any renormalization that could touch
    # them would break consistency; renormalization only rescales (u_b, u_c)
    # jointly, and the window spans three consecutive n+1 values -- a rescale
    # between window points rescales all subsequent points by the same factor
    # relative to earlier ones. Guard: disable rescaling inside the window.
    up = (uM_p1 - uM_m1)/(2*dr)
    L = up/uM - 1.0/rs[iM]      # log-derivative of R = u/r (matching uses R'/R)
    x = k*rs[iM]
    j, y = sph_jn_yn(lmax, x)
    jp, yp = sph_derivs(lmax, x, j, y)
    num = k*jp - L*j[:lmax+1]
    den = k*yp - L*y[:lmax+1]
    return np.arctan2(num, den)

def sigma_T(E, S, Rs, core, lmax=None):
    k = math.sqrt(2*MU*E)/HBARC
    if lmax is None:
        lmax = int(max(6, math.ceil(k*6*Rs) + 4))
    d = phase_shifts(E, S, Rs, core, lmax+1)
    ls = np.arange(0, lmax+1)
    return (4*math.pi/k**2)*np.sum((ls+1)*np.sin(d[1:lmax+2] - d[0:lmax+1])**2)

def bound_count(S, Rs, core):
    """s-wave bound states by node count of the E->0 zero-energy solution."""
    d = phase_shifts(1e-9, S, Rs, core, 0)          # not used; do node count directly
    dr = 0.02
    r0 = float(core[2:]) if core.startswith("hs") else 0.05
    rs = np.arange(r0, 6*Rs, dr)
    V = -(S/rs)*np.exp(-rs/Rs)
    if core == "yuk":
        V = V + (N_EL*E_EE/rs)*np.exp(-rs)
    W = (2*MU/HBARC**2)*V
    f = 1.0 + (dr*dr/12.0)*(-W)
    u0, u1 = 0.0, dr
    nodes = 0
    for n in range(1, len(rs)-1):
        u2 = ((12.0 - 10.0*f[n])*u1 - f[n-1]*u0)/f[n+1]
        if u1 != 0 and u2*u1 < 0:
            nodes += 1
        u0, u1 = u1, u2
        if abs(u1) > 1e250:
            u0 /= 1e250; u1 /= 1e250
    return nodes

CONV = 1e-26/(M_ROD*MEV_G)   # fm^2 -> cm^2/g

if __name__ == "__main__":
    store = os.path.join(os.path.dirname(__file__), "2338_results.json")
    d = json.load(open(store)) if os.path.exists(store) else {}
    mode = sys.argv[1]
    if mode == "point":
        for core in ("hs2", "hs5", "hs10", "yuk"):
            row = {"nb": bound_count(S0, RS0, core)}
            for v in VELS:
                E, k = kinematics(v)
                row[str(int(v))] = sigma_T(E, S0, RS0, core)*CONV
            d["point_%s" % core] = row
            json.dump(d, open(store, "w"))
            print(core, {k2: (round(v2, 4) if isinstance(v2, float) else v2)
                         for k2, v2 in row.items()})
    elif mode == "born":
        # validation: weak-coupling attractive Yukawa (no core) vs Born formula
        # Born: tan d_l ~ d_l = -(2 mu S/hbc^2) * integral j_l(kr)^2 e^{-r/Rs} r dr... 
        # closed form for l=0: d_0 = (2 mu S)/(hbc^2) * (1/(2k)) * ln(1+4k^2Rs^2)
        Sw = 0.001
        E, k = kinematics(200.0)
        d0 = phase_shifts(E, Sw, RS0, "hs2", 2)[0]  # tiny core ~ none at weak coupling
        born0 = (2*MU*Sw/HBARC**2)*(1.0/(2*k))*math.log(1.0 + 4*k*k*RS0*RS0)
        print("Born check l=0 at 200 km/s, S=0.001: numeric %.6f vs Born %.6f (ratio %.3f)"
              % (d0, born0, d0/born0))
    elif mode == "scan":
        core = sys.argv[2]; i = int(sys.argv[3])
        Ss = np.linspace(0.15, 0.60, 16)
        Rss = np.linspace(15.0, 30.0, 7)
        S = float(Ss[i])
        row = []
        for Rs in Rss:
            sig = {}
            for v in (30.0, 50.0, 200.0, 1500.0):
                E, k = kinematics(v)
                sig[int(v)] = sigma_T(E, S, Rs, core)*CONV
            # windows incl. registered floor added
            FL = {30: 0.11, 50: 0.09, 200: 0.05, 1500: 0.04}
            tot = {v: sig[v] + FL[v] for v in sig}
            ok = (20 <= tot[30] <= 100 and 1 <= tot[50] <= 5
                  and 0.7 <= tot[200] <= 2.5 and tot[1500] <= 0.13)
            row.append([float(Rs), tot[30], tot[50], tot[200], tot[1500], bool(ok)])
        d["scan_%s_%02d" % (core, i)] = {"S": S, "rows": row}
        json.dump(d, open(store, "w"))
        npass = sum(1 for r in row if r[5])
        print("scan %s S=%.3f: %d/%d Rs points pass; tot@ (30,50,200,1500) at Rs=25.4-ish: %s"
              % (core, S, npass, len(row), [round(x, 3) for x in row[4][1:5]]))

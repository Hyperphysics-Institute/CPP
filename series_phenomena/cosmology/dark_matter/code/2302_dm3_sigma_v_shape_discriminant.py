"""
2302 -- DM-3 P3: the sigma(v)-shape discriminant. The CPP curve = classical capture
on the registered rod-rod screened residual + the MEASURED elastic floor (1871),
vs the generic velocity-dependent SIDM phenomenological form fitted to the SAME
low-velocity anchors. The discriminant is the JOINT SHAPE, especially the
high-velocity plateau.

CPP curve [J-DM3-3: capture SHAPE from the classical barrier computation on the
registered potential V(r) = -E_c (r_c/r) e^{-r/R_s} (E_c = 0.3 MeV, R_s = 25.42 fm,
mu = m_rod/2); ABSOLUTE normalized to the registered v1.2 dwarf anchor
sigma(50 km/s) = 4.6 cm^2/g -- shape is the claim, the anchor is the corpus's]:
capture = pi b_crit(v)^2 with b_crit from the effective-potential barrier
(capture-to-contact over the centrifugal barrier); floor = log-interpolation of
the 1871 MEASURED points.

Generic SIDM comparator: sigma(v) = sigma0 / (1 + (v/w)^4) (the standard
phenomenological transfer form), two parameters FITTED to the same dwarf + LSB
anchors (50 -> 4.6, 200 -> 0.80).

*** POST-RUN STATUS (folded at-patch): S1 STANDS (implementation-independent:
measured floor + same-data-fitted comparator). S2/S3 PROVISIONAL -- J-DM3-3-OPEN:
this implementation's capture shape CONTRADICTS the registered v1.2 anchors in
the mid/low band (gives 0.34 at LSB vs registered 0.74-0.85; ~50 at dSph vs
registered grazing-low). The registered anchors are authoritative; the corpus's
registered capture computation must be pulled and S2/S3 recomputed before the
DM-3 paper claims them. Resolution: Patch 2303. ***
"""
import math
HBARC = 197.327
CHI = ((1 + 5 ** 0.5) / 2) ** -3 / 6
RS, RC, EC = 1.0 / CHI, 1.0, 0.3
M_ROD = 18 * 1408.0
MU = M_ROD / 2.0
CKMS = 299792.458
M_ROD_G = M_ROD * 1.783e-27  # g
FLOOR_PTS = [(50, 0.12), (200, 0.06), (1150, 0.04), (1500, 0.035), (3500, 0.02)]

def floor(v):
    import math as m
    pts = FLOOR_PTS
    if v <= pts[0][0]: return pts[0][1]
    if v >= pts[-1][0]: return pts[-1][1] * (pts[-1][0] / v) ** 0.4
    for i in range(len(pts) - 1):
        (v1, f1), (v2, f2) = pts[i], pts[i + 1]
        if v1 <= v <= v2:
            t = (m.log(v) - m.log(v1)) / (m.log(v2) - m.log(v1))
            return m.exp(m.log(f1) + t * (m.log(f2) - m.log(f1)))

def b_crit(v_kms):
    """Max impact parameter for capture-to-contact over the centrifugal barrier
    [WRONG IN PRINCIPLE -- conservative dynamics cannot capture; kept as the
    2302 record; see header + Patch 2303]."""
    v = v_kms / CKMS
    E = 0.5 * MU * v * v  # MeV
    def reaches(b):
        L2 = (MU * v * b) ** 2
        r, rmax, vmax = 0.5, 220.0, -1e30
        while r < rmax:
            Veff = -EC * RC * math.exp(-r / RS) / r + L2 / (2 * MU * r * r)
            if Veff > vmax: vmax = Veff
            r += 0.25
        return E > vmax
    lo, hi = 0.0, 500.0
    for _ in range(50):
        mid = 0.5 * (lo + hi)
        if reaches(mid): lo = mid
        else: hi = mid
    return lo

b50 = b_crit(50.0)
cap50_raw = math.pi * b50 ** 2 * 1e-26 / M_ROD_G
CAP_NORM = (4.6 - floor(50)) / cap50_raw

def cpp(v):
    return CAP_NORM * math.pi * b_crit(v) ** 2 * 1e-26 / M_ROD_G + floor(v)

def fit_sidm():
    target = 4.6 / 0.80
    lo, hi = 60.0, 400.0
    for _ in range(60):
        w = 0.5 * (lo + hi)
        r = (1 + (200 / w) ** 4) / (1 + (50 / w) ** 4)
        if r > target: lo = w
        else: hi = w
    w = 0.5 * (lo + hi)
    s0 = 4.6 * (1 + (50 / w) ** 4)
    return s0, w

if __name__ == "__main__":
    s0, w = fit_sidm()
    print("=" * 78)
    print(" 2302 -- P3: the sigma(v) joint-shape discriminant")
    print(" SIDM comparator fit: sigma0 = %.2f cm^2/g, w = %.0f km/s" % (s0, w))
    print(" S1 (plateau): CPP measured floor 0.03-0.05 at v >= 1150 vs SIDM-fit")
    print("   1e-3-1e-4 -> x40-x150 divergence, pure shape. F1 -> F1' (three-way):")
    print("   detection 0.03-0.05 selects CPP; firm 0.5 kills CPP; firm null < 0.02")
    print("   kills the floor, favors SIDM.")
    print(" S2/S3: PROVISIONAL (J-DM3-3-OPEN; see header). Resolution: Patch 2303.")
    print("=" * 78)

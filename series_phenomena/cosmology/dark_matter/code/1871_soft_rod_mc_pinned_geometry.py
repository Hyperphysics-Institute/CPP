"""
1871 (derived from 1870) -- Gold-standard check on the derived floor shape S(v): full rigid-body rod-rod
MC with the SOFT screened coat force law replacing 1856's hard contacts.

Each rod: N = 18 point elements, spacing d_el = 4.7 fm (L ~ 80 fm; J8 -- spacing
implied by 1868's A_ref = N/4 at r_impl, registry pin still pending), rigid, thin-rod
inertia I = M L^2/12, mass M = N * 1408 MeV. Element-pairwise repulsive coat potential
    V(r) = E_ee * (r_c/r) * exp(-r/r_scr),  E_ee = 0.9 MeV, r_c = r_scr = 1 fm  [1813/SF-5]
CM frame, isotropic orientations, cold rods (omega_0 = 0; tumbling temperature not
modelled -- flagged), impact parameter uniform in a disk of R_samp = 55 fm (truncates
far-arm grazing contacts; same truncation at all v, so the SHAPE ratio is protected --
flagged for the absolute number). Symplectic Euler, dt*v = 0.03 fm, energy drift
monitored. Deflection theta from the final relative CM velocity.

    sigma_T(v) = pi R_samp^2 * < 1 - cos theta >_disk

OUTPUTS: (1) S_MC(v) = sigma_T(v)/sigma_T(50) vs the 1869 deflection-integral S(v);
(2) absolute sigma_T(50)/m vs the 1860 convention eps*0.11*N = 0.594 cm^2/g (this is
the ab-initio test of the normalization/multiplicity, which 1869 anchored rather than
derived); (3) cluster/group verdicts under the MC shape.
"""
import numpy as np

C_KMS = 299792.458
MEV_G = 1.783e-27
E_EE = 0.9
N_EL = 18
M_EL = 1408.0
D_EL = 1.15   # J8 PINNED: corpus rung spacing 1.0-1.3 fm (1812/0835); spread carried via CLI
M_ROD = N_EL * M_EL
L_ROD = (N_EL - 1) * D_EL
I_ROD = M_ROD * L_ROD ** 2 / 12.0
R_SAMP = 35.0
DTV = 0.025
Z0 = L_ROD / 2 + 15.0
RCUT = 15.0
SEED = 23
TUMBLE = False

S_1869 = {50: 1.0000, 200: 0.4388, 1150: 0.0816, 1500: 0.0563, 3500: 0.0122}


def run_batch(v_c, nt, rng):
    """Integrate nt trajectories at relative speed v_c (units of c). Returns 1-cos(theta) array, |dE|/KE max."""
    offs = (np.arange(N_EL) - (N_EL - 1) / 2.0) * D_EL          # (N,)
    # initial state
    phi = rng.uniform(0, 2 * np.pi, nt)
    b = R_SAMP * np.sqrt(rng.uniform(0, 1, nt))
    r1 = np.stack([b * np.cos(phi), b * np.sin(phi), -Z0 * np.ones(nt)], axis=1).astype(np.float32)
    r2 = np.zeros((nt, 3), np.float32); r2[:, 2] = Z0
    v1 = np.zeros((nt, 3), np.float32); v1[:, 2] = v_c / 2
    v2 = np.zeros((nt, 3), np.float32); v2[:, 2] = -v_c / 2

    def iso_dirs(n):
        u = rng.uniform(-1, 1, n); ph = rng.uniform(0, 2 * np.pi, n)
        s = np.sqrt(1 - u * u)
        return np.stack([s * np.cos(ph), s * np.sin(ph), u], axis=1).astype(np.float32)

    d1, d2 = iso_dirs(nt), iso_dirs(nt)
    w1 = np.zeros((nt, 3), np.float32); w2 = np.zeros((nt, 3), np.float32)
    if TUMBLE:  # equipartition-scale tumbling: tip speed ~ v/2, random perp axis
        for dd, ww in ((d1, w1), (d2, w2)):
            ax = np.cross(dd, iso_dirs(nt)); ax /= np.linalg.norm(ax, axis=1, keepdims=True)
            ww += ax * (v_c / L_ROD) * rng.uniform(0.5, 1.5, (nt, 1)).astype(np.float32)
    offs32 = offs.astype(np.float32)

    dt = DTV / v_c
    nsteps = int(np.ceil(2 * Z0 / DTV))                   # path/ (dt*v)
    KE0 = 0.5 * (M_ROD / 2.0) * v_c ** 2                         # reduced-mass KE (CM)

    def pair_pot_force(r1, d1, r2, d2):
        P1 = r1[:, None, :] + offs32[None, :, None] * d1[:, None, :]    # (nt,N,3)
        P2 = r2[:, None, :] + offs32[None, :, None] * d2[:, None, :]
        dvec = P1[:, :, None, :] - P2[:, None, :, :]                  # (nt,N,N,3)
        r = np.sqrt(np.sum(dvec * dvec, axis=-1))                     # (nt,N,N)
        act = r < RCUT
        rs = np.where(act, r, 1.0)
        Vp = np.where(act, E_EE * np.exp(-rs) / rs, 0.0)              # potential per pair
        # |F| = E*e^{-r}(1+r)/r^2, direction +dvec/r on rod1 (repulsive)
        Fmag = np.where(act, E_EE * np.exp(-rs) * (1 + rs) / rs ** 2, 0.0)
        Fvec = (Fmag / rs)[..., None] * dvec                          # (nt,N,N,3)
        F1seg = Fvec.sum(axis=2)                                      # (nt,N,3) on rod1
        F1 = F1seg.sum(axis=1)                                        # (nt,3)
        T1 = np.cross(offs32[None, :, None] * d1[:, None, :], F1seg).sum(axis=1)
        F2seg = -Fvec.sum(axis=1)
        T2 = np.cross(offs32[None, :, None] * d2[:, None, :], F2seg).sum(axis=1)
        return F1, T1, -F1, T2, Vp.sum(axis=(1, 2))

    Emax = 0.0
    for s in range(nsteps):
        F1, T1, F2, T2, Vtot = pair_pot_force(r1, d1, r2, d2)
        if s == 0: E0 = KE0 * 0 + 0.5 * M_ROD * (np.sum(v1 * v1, 1) + np.sum(v2 * v2, 1)) \
            + 0.5 * I_ROD * (np.sum(w1 * w1, 1) + np.sum(w2 * w2, 1)) + Vtot
        v1 += (F1 / M_ROD) * dt; v2 += (F2 / M_ROD) * dt
        w1 += (T1 / I_ROD) * dt; w2 += (T2 / I_ROD) * dt
        w1 -= np.sum(w1 * d1, 1, keepdims=True) * d1
        w2 -= np.sum(w2 * d2, 1, keepdims=True) * d2
        r1 += v1 * dt; r2 += v2 * dt
        d1 += np.cross(w1, d1) * dt; d2 += np.cross(w2, d2) * dt
        if s % 4 == 0:
            d1 /= np.linalg.norm(d1, axis=1, keepdims=True)
            d2 /= np.linalg.norm(d2, axis=1, keepdims=True)
        if s % 400 == 0 and s > 0:
            E = 0.5 * M_ROD * (np.sum(v1 * v1, 1) + np.sum(v2 * v2, 1)) \
                + 0.5 * I_ROD * (np.sum(w1 * w1, 1) + np.sum(w2 * w2, 1)) + Vtot
            Emax = max(Emax, float(np.max(np.abs(E - E0)) / (M_ROD * v_c ** 2 / 4)))
    vrel = v1 - v2
    ct = vrel[:, 2] / np.linalg.norm(vrel, axis=1)
    Erot = 0.5 * I_ROD * (np.sum(w1 * w1, 1) + np.sum(w2 * w2, 1))
    KEcm = 0.25 * M_ROD * v_c ** 2
    return 1.0 - ct, Emax, 1.0 - ct * ct, Erot / KEcm


if __name__ == "__main__":
    print("=" * 78)
    print(" 1870 -- soft-potential rigid-body rod-rod MC: S(v) gold-standard check")
    print(" N=18, d_el=4.7 fm, R_samp=55 fm, nt=800/velocity, dt*v=0.03 fm")
    print("=" * 78)
    import sys, json, os
    vels = [50, 200, 1150, 1500, 3500]
    nt = 600
    store = 'code/1871_results.json'
    if len(sys.argv) > 1:                     # single-velocity worker mode
        v = int(sys.argv[1])
        seed_off = int(sys.argv[2]) if len(sys.argv) > 2 else 0
        if len(sys.argv) > 3: globals()['DTV'] = float(sys.argv[3])
        if len(sys.argv) > 4:
            globals()['D_EL'] = float(sys.argv[4])
            globals()['L_ROD'] = (N_EL - 1) * D_EL
            globals()['I_ROD'] = M_ROD * L_ROD ** 2 / 12.0
            globals()['Z0'] = L_ROD / 2 + 15.0
        if len(sys.argv) > 5: globals()['TUMBLE'] = bool(int(sys.argv[5]))
        rng = np.random.default_rng(SEED + v + 1000 * seed_off)
        omc, Emax, sv, erot = run_batch(v / C_KMS, nt, rng)
        area = np.pi * R_SAMP ** 2
        d = json.load(open(store)) if os.path.exists(store) else {}
        key = str(v) if (seed_off == 0 and len(sys.argv) <= 3) else "{}_s{}_dt{}_d{}_t{}".format(v, seed_off, DTV, D_EL, int(TUMBLE))
        d[key] = [area * float(np.mean(omc)), area * float(np.std(omc) / np.sqrt(nt)), Emax,
                  area * float(np.mean(sv)), float(np.mean(erot))]
        json.dump(d, open(store, 'w'))
        print("{} done: sigma_T={:.2f}+/-{:.2f} fm^2, sigma_V={:.2f}, Erot/KE={:.3f}, Emax={:.1e}".format(
            key, d[key][0], d[key][1], d[key][3], d[key][4], Emax))
        sys.exit(0)
    d = json.load(open(store))
    res = {v: d[str(v)][0] for v in vels}
    err = {v: d[str(v)][1] for v in vels}
    for v in vels:
        sT, se, Emax = d[str(v)]
        print("  v={:>5} km/s: sigma_T = {:8.2f} +/- {:6.2f} fm^2   |dE|/KE_max < {:.1e}".format(
            v, sT, se, Emax))

    print("\n(1) SHAPE: S_MC(v) vs 1869 deflection integral")
    sref = res[50]
    print("    {:>6} {:>12} {:>10} {:>8}".format("v", "S_MC", "S_1869", "ratio"))
    for v in vels:
        smc = res[v] / sref
        print("    {:>6} {:>7.4f}+/-{:.4f} {:>10.4f} {:>8.2f}".format(
            v, smc, err[v] / sref, S_1869[v], smc / S_1869[v]))

    print("\n(2) ABSOLUTE normalization at v_ref = 50 km/s (ab-initio vs convention):")
    st_cm2 = sref * 1e-26
    som = st_cm2 / (M_ROD * MEV_G)
    print("    sigma_T,MC(50)/m = {:.3f} cm^2/g  vs convention eps*0.11*N = {:.3f}  (ratio {:.2f})".format(
        som, 0.30 * 0.11 * N_EL, som / (0.30 * 0.11 * N_EL)))

    print("\n(3) VERDICTS under the MC shape (convention-normalized at 50, capture added):")
    # capture term (1858 pipeline, chi point, flat E_c)
    import math
    CHI = ((1 + 5 ** 0.5) / 2) ** -3 / 6; RS = 1 / CHI

    def capture(vk):
        mu = N_EL * M_EL / 2; ke = 0.5 * mu * (vk / C_KMS) ** 2
        V = lambda r: (0.30 / r) * math.exp(-r / RS)
        if V(1.0) < ke: bb = 1.0
        else:
            lo, hi = 1.0, 3000.0
            for _ in range(200):
                m = 0.5 * (lo + hi)
                if V(m) > ke: lo = m
                else: hi = m
            bb = 0.5 * (lo + hi)
        return math.pi * bb * bb * 1e-26 / (N_EL * M_EL * MEV_G)

    f0 = 0.30 * 0.11 * N_EL
    for v, name, win in ((1150, "group", "[0.3,0.7]"), (1500, "cluster", "<0.35/<0.19/<0.13"),
                         (3500, "Bullet", "<0.7")):
        tot = f0 * res[v] / sref + capture(v)
        print("    {:>7} v={:>4}: total = {:.3f}   window {}".format(name, v, tot, win))
    print("\n" + "=" * 78)

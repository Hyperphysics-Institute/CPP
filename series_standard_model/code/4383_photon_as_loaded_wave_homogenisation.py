#!/usr/bin/env python3
"""Patch 4383 -- founder's two-part photon: the DI-bit shell carries the influence at one
PSR per Moment; the CPs inside respond (move by SSV_net), sign-dependently in thick shells,
and do not themselves move at c.  The photon is then a wave in a LOADED medium whose
response is modulated +/- on sub-wavelength scale (half the sites each sign).

Question: what does a symmetric +/-delta modulation do to the long-wave speed?
Part 1: 1D chain (scalar wave) -- numerical lowest mode, alternating and random signs.
Part 2: 3D random bond network -- numerical homogenisation of div(eps grad phi) = 0 vs.
        the second-order formula eps_eff = <eps> - <d eps^2>/(3<eps>)  (Landau & Lifshitz,
        Electrodynamics of Continuous Media, Sec. 9, problem).
Part 3: the cross term if the +/- modulation already exists in ordinary space.
"""
import numpy as np, scipy.sparse as sps, scipy.sparse.linalg as spl
rng = np.random.default_rng(4383)

print("Part 1: 1D chain, N sites, half + and half - sites; long-wave speed v (=1 unmodulated)")
def chain_speed(K, m):
    N = len(K)
    # ring: K[i] couples i and i+1
    main = np.zeros(N); off = []
    rows, cols, vals = [], [], []
    for i in range(N):
        j = (i+1) % N
        for a, b, v in ((i, i, K[i]), (j, j, K[i]), (i, j, -K[i]), (j, i, -K[i])):
            rows.append(a); cols.append(b); vals.append(v)
    Kmat = sps.csr_matrix((vals, (rows, cols)), shape=(N, N)).toarray()
    Minv = np.diag(1/np.sqrt(m))
    w2 = np.sort(np.linalg.eigvalsh(Minv @ Kmat @ Minv))
    # lowest nonzero modes come as a cos/sin doublet (wavelength N); disorder splits it at
    # first order, so average the pair (critic 4383)
    return np.sqrt(0.5*(w2[1] + w2[2])) * N / (2*np.pi)
N = 1600
for d in (0.1, 0.2, 0.3):
    one = np.ones(N); alt = np.array([1, -1]*(N//2))
    vK = chain_speed(1 + d*alt, one); vC = chain_speed(1/(1 + d*alt), one); vM = chain_speed(one, 1 + d*alt)
    rK, rC = [], []
    for seed in range(8):
        sg = alt.copy(); np.random.default_rng(seed).shuffle(sg)
        rK.append(chain_speed(1 + d*sg, one)); rC.append(chain_speed(1/(1 + d*sg), one))
    print(f"  delta={d}: alternating -> stiffness {vK:.5f} (pred {np.sqrt(1-d*d):.5f}), "
          f"compliance {vC:.5f}, inertia {vM:.5f} (pred 1)")
    print(f"             random (8 seeds) -> stiffness {np.mean(rK):.5f}+/-{np.std(rK):.5f}, "
          f"compliance {np.mean(rC):.5f}+/-{np.std(rC):.5f}")
print("  Stiffness (push needed per unit displacement) modulated +/- -> slower, v^2 = 1 - delta^2.")
print("  Compliance (displacement per unit push) or inertia modulated +/- -> no change (alternating).")
print("  In 1D the long-wave speed is the same for any arrangement (harmonic mean of stiffness).")
print("  (1D duality: in a 1D EM line eps plays the INERTIA role, so the 1D 'compliance' and")
print("   'inertia' rows are the same statement.)")

print("\nPart 1b: per-DP pairing (leading model).  The founder: a DP sits in ONE shell and its")
print("  + and - CPs respond oppositely, so the +/- pairing is inside every DP.  DP loading =")
print("  sum of its two halves' compliances (relative to unmodulated):")
for d in (0.1, 0.2, 0.3):
    comp = 0.5*((1 + d) + (1 - d))                   # compliance +/-d
    stiff = 0.5*(1/(1 + d) + 1/(1 - d))              # stiffness +/-d
    print(f"  delta={d}: compliance +/- -> loading {comp:.5f} (no change, all orders); "
          f"stiffness +/- -> loading {stiff:.5f} = 1/(1-d^2) -> v = {1/np.sqrt(stiff):.5f}")
print("  If all of the vacuum loading comes from the CPs, stiffness +/- gives v = sqrt(1 - delta^2).")

print("\nPart 2: domain-scale ALTERNATIVE: 3D simple-cubic network, bonds +/-d at random (half each)")
def sigma_eff_3d(n, w3):          # w3[ax] = bond values to +ax neighbour, shape (n,n,n)
    idx = np.arange(n**3).reshape(n, n, n); rows, cols, vals = [], [], []; rhs = np.zeros(n**3)
    for ax in range(3):
        i = idx.ravel(); j = np.roll(idx, -1, axis=ax).ravel(); w = w3[ax].ravel()
        rows += [i, j, i, j]; cols += [i, j, j, i]; vals += [w, w, -w, -w]
        if ax == 0:
            np.add.at(rhs, i, -w); np.add.at(rhs, j, w)
    A = sps.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))),
                       shape=(n**3, n**3)) + sps.identity(n**3)*1e-12
    psi, _ = spl.cg(A, -rhs, rtol=1e-11, maxiter=10000); psi = psi.reshape(n, n, n)
    return np.mean(w3[0]*(1 + np.roll(psi, -1, axis=0) - psi))
n = 24
for d in (0.1, 0.2):
    sg = rng.choice([-1, 1], size=(3, n, n, n))
    for label, w in (("compliance-modulated eps = 1 +/- d    ", 1 + d*sg),
                     ("stiffness-modulated  eps = 1/(1 -/+ d)", 1/(1 - d*sg))):
        ee = sigma_eff_3d(n, w); m, var = w.mean(), w.var()
        print(f"  d={d}: {label}: eps_eff={ee:.5f}  2nd-order (LL / bond EMA, z=6) {m - var/(3*m):.5f}"
              f"  -> speed {1/np.sqrt(ee):.5f}")
print("  Compliance-modulated: eps_eff ~ 1 - d^2/3 -> FASTER by ~d^2/6.")
print("  Stiffness-modulated:  eps_eff ~ 1 + 2d^2/3 -> SLOWER by ~d^2/3.")
print("  (eps is the CPs' loading of the shell wave: the more a CP is displaced per push, the more")
print("   it loads the wave.  Quasi-static homogenisation; valid for wavelength >> GP spacing.)")

print("\nPart 3: if ordinary space already has a sign modulation delta0, and the well adds delta1(eps):")
print("  speed change ~ -c*(delta0 + delta1)^2 -> first-order piece -2c*delta0*delta1.")
print("  If it enters light and clocks universally (g00) it renormalises G and is absorbed by the")
print("  calibration; if it enters light propagation differently from the Newtonian channel it")
print("  shifts gamma, and Cassini |gamma-1| < 2.3e-5 bounds 2*c*delta0*(d delta1/d eps) at ~1e-5 of")
print("  the first-order PSR coefficient.  At minimum it is a first-order term to account for.")
print("  Clean case: delta0 = 0 (no sign-dependent response in ordinary space; it appears only")
print("  with the shell excess).")

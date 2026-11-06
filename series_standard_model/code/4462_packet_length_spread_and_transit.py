"""Patch 4462 -- founder: (1) can we be certain of the photon pulse's length -- is the exponential the statistics of when photons are
detected after excitation, or the length of time each is radiated?  (2) a photon spread over all directions would need reassembling at
detection, perhaps after billions of years -- a new layer of postulate.  (3) the nucleus was his direction for the swing, not its power; the
energy emitted relates to the CP's KE from the start of its transit to its end on the other side.

Part 1. Histogram vs packet: flat packets starting together give detection times spread evenly over [0, L].  Lengths distributed as
        (L/tau^2) exp(-L/tau) (a gamma distribution of shape 2) reproduce the exponential histogram; exponential lengths do not (they give
        an exponential-integral curve).  For the gamma-2 lengths, two such photons overlap (two-photon interference visibility
        |<psi1|psi2>|^2 = min/max) on average exactly 1/2; identical packets overlap fully.
Part 2. A directed packet also spreads: a Gaussian beam of waist w0 diverges at lambda/(pi w0) (1/e^2 radius).  Illustrative waist 0.48 m
        (the packet's length c tau, reused as a width); radius and diameter after 1e9 light-years; the narrowest any starting waist allows after
        1e9 light-years (radius sqrt(2 lambda z/pi), at waist sqrt(lambda z/pi)).
Part 3. Transit timed by speed, not by the nuclear pull: distance from the upper Bohr radius through the nucleus to the lower one
        (n_u^2 + n_l^2) a0, at a speed set (i) by the upper level's KE (alpha c / n_u) or (ii) by the energy difference (1/2 m v^2 = dE);
        out-and-back = two passes.  Ordering compared with the measured lines.
"""
import numpy as np
rng = np.random.default_rng(1)
n = 10**6
bins = [0, 0.1, 1, 2, 3]
exp_hist = np.histogram(rng.exponential(1, n), bins)[0]/n
for label, L1, L2 in (("gamma-2 lengths", rng.gamma(2, 1, n), rng.gamma(2, 1, n)),
                      ("exponential lengths (does not reproduce the histogram)", rng.exponential(1, n), rng.exponential(1, n))):
    hist = np.histogram(rng.uniform(0, L1), bins)[0]/n
    print(f"Part 1  {label}: detection-time shares in 0-0.1, 0.1-1, 1-2, 2-3 tau = {np.round(hist, 3)} (exponential {np.round(exp_hist, 3)}); "
          f"mean overlap {np.mean(np.minimum(L1, L2)/np.maximum(L1, L2)):.3f}")
print("        exact: gamma-2 lengths 0.500; exponential lengths 2 ln2 - 1 = %.3f; identical packets 1.000" % (2*np.log(2)-1))
ly = 9.4607e15
for name, lam, w0 in (("Lyman-alpha", 121.6e-9, 0.48), ("visible 550 nm", 550e-9, 0.5)):
    th = lam/(np.pi*w0); z = 1e9*ly
    print(f"Part 2  {name}: divergence {th:.1e} rad; after 1e9 ly radius {th*z/ly:.0f} ly, diameter {2*th*z/ly:.0f} ly")
z = 1e9*ly; w_opt = np.sqrt(121.6e-9*z/np.pi)
print(f"        Lyman-alpha, any starting waist: radius after 1e9 ly is at least sqrt(2 lambda z / pi) = {np.sqrt(2)*w_opt:.1e} m "
      f"(at waist {w_opt:.1e} m); no start stays within a 10 m telescope")
a0, c, alpha, me, eV = 5.29177e-11, 2.99792458e8, 7.2973526e-3, 9.1093837e-31, 1.602176634e-19
RHc, Ry = 3.28984196e15, 13.605693
lines = (("Lyman-alpha", 2, 1), ("Lyman-beta", 3, 1), ("Balmer-alpha", 3, 2))
for label, speed in (("(i) upper-level KE", lambda nu, nl: alpha*c/nu),
                     ("(ii) energy difference", lambda nu, nl: np.sqrt(2*Ry*(1/nl**2-1/nu**2)*eV/me))):
    out = []
    for name, nu, nl in lines:
        f = speed(nu, nl)/(2*(nu**2+nl**2)*a0)
        out.append((name, f, RHc*(1/nl**2-1/nu**2)))
    print(f"Part 3  {label}: " + "; ".join(f"{n} {f:.2e} Hz (line {m:.2e})" for n, f, m in out))
    print(f"        Lyman-beta/Lyman-alpha {out[1][1]/out[0][1]:.2f} (measured {out[1][2]/out[0][2]:.2f}); "
          f"Lyman-beta/Balmer-alpha {out[1][1]/out[2][1]:.2f} (measured {out[1][2]/out[2][2]:.2f})")

"""Patch 4426 -- founder: the organized cloud of DP arc-separation grows to the size corresponding to the SSV_abs associated
with the speed; its volume is related to the PSR in each direction.

Test case: the cloud of a moving charge, as its field. ASSUMED: the census is Lienard-Wiechert (4411, conditional on the 1/R
weight per arrival and a single-hop relay), and the cloud's SSV_abs is its stored field energy (4417's square law, a requirement).
The core is contracted along the motion like the PSR (1/gamma along, unchanged across; 4410) -- an input. Gaussian units, q = 1, core radius a = 1, so the rest
field energy outside the core is U0 = q^2/(2a) = 0.5.
  E = q (1 - v^2) r_hat / (r^2 (1 - v^2 sin^2 theta)^(3/2))  (r from the present position), B = v x E
  energy density (E^2 + B^2)/(8 pi), momentum density (E x B)/(4 pi)
Integrated outside the contracted core x^2 gamma^2 + rho^2 = a^2 (substitute x = x'/gamma: outside the unit sphere in x').
Radial cutoff r' = 400 (about 0.25% of the energy lies beyond it; the rest row reads 0.4988 for 0.5).
Compare with gamma U0 (1 + v^2/3) and (4/3) gamma U0 v (the classical field-only values) and with the mass shell
E^2 - p^2 = U0^2. Then add the standard Poincare-stress terms (-gamma U0 v^2/3, -gamma U0 v/3; imported from classical physics,
stresses with no rest energy; the column is an identity by construction) and recheck. (Alternative cure: the covariant
Fermi/Rohrlich definition gives gamma U0 and gamma U0 v for the field alone.)
Part 2: surfaces of fixed potential phi = q gamma / sqrt(gamma^2 x^2 + rho^2) (from 4411): semi-axis along the motion q/phi
(unchanged), across gamma q/phi (grown), enclosed volume x gamma^2.
"""
import numpy as np
from scipy.integrate import dblquad
U0 = 0.5
def field_E_p(v):
    g = 1/np.sqrt(1 - v**2)
    # primed spherical coords (r', t) with x' = r' cos t, rho = r' sin t; physical x = x'/g; volume element dV = dV'/g
    def dens(rp, t, which):
        x = rp*np.cos(t)/g; rho = rp*np.sin(t)
        r = np.hypot(x, rho); s2 = (rho/r)**2
        Emag = (1 - v**2)/(r**2*(1 - v**2*s2)**1.5)
        Ex, Er = Emag*x/r, Emag*rho/r                  # components along motion and radial-across
        B = v*Er                                       # |v x E| (azimuthal)
        if which == 0:
            val = (Emag**2 + B**2)/(8*np.pi)
        else:
            val = (Er*B)/(4*np.pi)                     # (E x B)_x = E_rho B_phi
        return val*2*np.pi*rp**2*np.sin(t)/g
    E = dblquad(lambda t, rp: dens(rp, t, 0), 1, 400, 0, np.pi, epsabs=1e-10, epsrel=1e-8)[0]
    p = dblquad(lambda t, rp: dens(rp, t, 1), 1, 400, 0, np.pi, epsabs=1e-10, epsrel=1e-8)[0]
    return E, p
print("Part 1 (field of a moving charge outside its contracted core; U0 = 0.5):")
print(f"{'v':>5s} {'E_field':>9s} {'g U0(1+v^2/3)':>14s} {'p_field':>9s} {'(4/3) g U0 v':>13s} {'sqrt(E^2-p^2)':>14s} | {'with stresses: E':>17s} {'p':>8s} {'sqrt(E^2-p^2)':>14s}")
for v in (0.0, 0.3, 0.6, 0.9):
    g = 1/np.sqrt(1 - v**2)
    E, p = field_E_p(v)
    Es, ps = E - g*U0*v**2/3, p - g*U0*v/3
    print(f"{v:5.1f} {E:9.4f} {g*U0*(1+v**2/3):14.4f} {p:9.4f} {4/3*g*U0*v:13.4f} {np.sqrt(E**2-p**2):14.4f} | {Es:17.4f} {ps:8.4f} {np.sqrt(Es**2-ps**2):14.4f}")
print("  field alone: energy grows faster than gamma and the rest value E^2 - p^2 drifts (the classical 4/3 problem);")
print("  with the binding (Poincare) stresses the totals are gamma U0 and gamma U0 v, and the rest value stays U0.")
print("Part 2 (surfaces of fixed potential around the moving charge, absolute frame, q = 1, phi = 1):")
for v in (0.0, 0.3, 0.6, 0.9):
    g = 1/np.sqrt(1 - v**2)
    along, across = 1.0, g
    print(f"  v {v}: semi-axis along {along:.4f}, across {across:.4f}, enclosed volume x {along*across**2:.4f} (gamma^2 = {g**2:.4f})")
print("  a surface of fixed potential grows across the motion: the literal 'geometry grows'; the contracted core is an input.")

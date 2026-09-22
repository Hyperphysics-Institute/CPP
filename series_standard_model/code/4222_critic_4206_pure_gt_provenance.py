#!/usr/bin/env python3
"""4222 critic of 4206 -- (i) the conventions X = 3<cos> and <cos_e.nu> = <cos_e><cos_nu>, by Monte Carlo;
(ii) the provenance of the pure-GT numbers the model 'matches exactly'.
SM pure-GT coefficients for a J -> J' beta- transition (JTW):  a = -1/3 for every J;  A = -lam_{JJ'} with
lam = 1/(J+1) for J->J, so A = -2/3 at J=1/2 is a CLEBSCH factor and does not know the quark polarisation.
The inheritance model gives A = -pol_d, pol_d = Delta d_n/2 (the per-quark d polarisation of the neutron)."""
import numpy as np
rng = np.random.default_rng(4222)
# (i) conventions, Monte Carlo: W ~ (1 + h_e cos(theta_e, -s))(1 + h_nu cos(theta_nu, +s)), s isotropic w.r.t. z with <s.z> = pol
def mc(pol, he=1.0, hnu=1.0, N=400000):
    sz = np.where(rng.uniform(size=N) < (1+pol)/2, 1.0, -1.0)      # 4206: s = +z w.p. P, -z w.p. 1-P; <s_z> = 2P-1 = pol
    s = np.stack([0*sz, 0*sz, sz], 1)
    def draw(axis, h):
        # sample cos(theta) to axis from (1 + h c)/2, then a random azimuth about axis
        u = rng.uniform(size=N)
        c = np.where(abs(h) < 1e-9, 2*u-1, (-1 + np.sqrt((1-h)**2 + 4*h*u)) / h)
        a = axis; t = np.cross(a, rng.normal(size=(N,3))); t /= np.linalg.norm(t, axis=1)[:,None]; b = np.cross(a, t)
        phi = rng.uniform(0, 2*np.pi, N); sn = np.sqrt(1-c**2)
        return c[:,None]*a + sn[:,None]*(np.cos(phi)[:,None]*t + np.sin(phi)[:,None]*b)
    pe = draw(-s, he); pn = draw(+s, hnu)
    return 3*np.mean(np.sum(pe*pn,1)), 3*np.mean(pe[:,2]), 3*np.mean(pn[:,2])
pol = 2/3
a, A, B = mc(pol)
print("(i) Monte Carlo of the 4206 model, pure GT, pol = 2/3 (X = 3<cos>, statistical error ~0.005):")
print(f"      a = {a:+.3f}  A = {A:+.3f}  B = {B:+.3f}      4206 rows: -0.333  -0.667  +0.667   -> conventions CONFIRMED")
# (ii) provenance
print("\n(ii) Where each side's pure-GT A comes from:")
print(f"{'':52s} {'a':>7s} {'A':>7s} {'B':>7s}")
for J in (0.5, 1.0, 1.5):
    lam = 1/(J+1); print(f"{'SM pure GT, J->J, J=%.1f  (A = -1/(J+1), Clebsch)' % J:52s} {-1/3:+7.3f} {-lam:+7.3f} {+lam:+7.3f}")
for name, Dd in (('model, SU(6): Delta d_n = 4/3, pol = 2/3', 4/3), ('model, measured Delta d_n = Delta u_p = 0.84, pol=0.42', 0.84), ('model, fully polarised quark, pol = 1', 2.0)):
    p = Dd/2; print(f"{name:52s} {-1/3:+7.3f} {-p:+7.3f} {+p:+7.3f}")
l = -5/3; D = 1+3*l*l
print(f"{'SM at the SU(6) point lambda = -5/3 (full formula)':52s} {(1-l*l)/D:+7.3f} {-2*l*(l+1)/D:+7.3f} {2*l*(l-1)/D:+7.3f}")
print("""
Reading: a = -1/3 is polarisation-independent on both sides -- a GENUINE structural match (the pair leaves
back-to-back with a 1/3 bias whatever the parent spin does). A and B match at 2/3 = 2/3 because the SU(6)
per-quark d polarisation Delta d_n/2 = 2/3 happens to equal the J=1/2 Clebsch factor 1/(J+1) = 2/3. The two
numbers have no common input: change the quark polarisation and the model's A moves, the SM's does not.
The SM evaluated AT the SU(6) point (lambda = -5/3) gives A = -0.238, not -0.667.
So 4206 s2's 'exact, nothing fitted' is one genuine match (a) and one coincidence (A, B). Not a test passed.""")

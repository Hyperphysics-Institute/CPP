#!/usr/bin/env python3
"""4223 -- a, A, B from CPP-shaped ingredients, against the full V-A amplitude.
LEVEL 1 (target): M = [u-bar_p g^mu (1 - lam g5) u_n] [u-bar_e g_mu (1 - g5) v_nu], nucleons at rest, exact Dirac
   spinors, |M|^2 summed over e, nu, p spins, neutron spin +z; fit W = 1 + a b c_enu + A b c_e + B c_nu.
LEVEL 2 (minimal quantum inheritance model): the lepton PAIR is created in a spin state fixed by angular
   momentum: same-sense refill -> singlet |S> (no spin leaves the nucleon), opposite-sense -> triplet |T_m>
   coupled to the proton by Clebsch-Gordan so that n(1/2,+z) -> p + pair; the two senses add as amplitudes
   with ratio lam (c03). Each lepton is then ejected by the handed rule: electron along -spin with bias
   beta, antineutrino along +spin with bias 1:  W = Tr[ rho_pair (1 - b p_e.sigma_e)(1 + p_nu.sigma_nu) ].
   No Dirac algebra, no gamma5: only 'pair spin state' + 'ejection rule' + 'amplitudes add'.
LEVEL 3 (4206's classical model) for contrast: electron spin = quark spin s in BOTH channels."""
import numpy as np, itertools
I2 = np.eye(2); Z2 = np.zeros((2,2))
sx, sy, sz = np.array([[0,1],[1,0]],complex), np.array([[0,-1j],[1j,0]]), np.array([[1,0],[0,-1]],complex)
sig = [sx, sy, sz]
g0 = np.block([[I2, Z2],[Z2, -I2]]); gi = [np.block([[Z2, s],[-s, Z2]]) for s in sig]; g5 = 1j*g0@gi[0]@gi[1]@gi[2]
gam = [g0] + gi; eta = np.diag([1,-1,-1,-1])
def spinor_u(m, p, chi):   # positive energy
    E = np.sqrt(m*m + p@p); sp = sum(pk*sk for pk,sk in zip(p,sig)); return np.concatenate([np.sqrt(E+m)*chi, sp@chi/np.sqrt(E+m)])
def spinor_v(m, p, chi):   # antiparticle, m -> 0 allowed via limit E=|p|
    E = np.sqrt(m*m + p@p); sp = sum(pk*sk for pk,sk in zip(p,sig)); return np.concatenate([sp@chi/np.sqrt(E+m), np.sqrt(E+m)*chi])
up, dn = np.array([1,0],complex), np.array([0,1],complex)
def level1(lam, pe, pn, me=0.511, mN=939.0):
    Ee = np.sqrt(me*me + pe@pe); Enu = np.linalg.norm(pn)
    un = spinor_u(mN, np.zeros(3), up); tot = 0.0
    for chip in (up, dn):
        upb = spinor_u(mN, np.zeros(3), chip).conj() @ g0
        H = [upb @ gam[mu] @ (np.eye(4) - lam*g5) @ un for mu in range(4)]
        for che in (up, dn):
            ueb = spinor_u(me, pe, che).conj() @ g0
            for chn in (up, dn):
                vn = spinor_v(0.0, pn, chn)
                L = [ueb @ gam[mu] @ (np.eye(4) - g5) @ vn for mu in range(4)]
                M = sum(eta[mu,mu]*H[mu]*L[mu] for mu in range(4)); tot += abs(M)**2
    return tot / (Ee*Enu)     # remove the spinor-normalisation energies (2E each, up to constants)
# Level 2 pair states. Basis |e nu>: |uu>,|ud>,|du>,|dd>
S  = np.array([0, 1, -1, 0], complex)/np.sqrt(2)
T  = {+1: np.array([1,0,0,0],complex), 0: np.array([0,1,1,0],complex)/np.sqrt(2), -1: np.array([0,0,0,1],complex)}
def level2(lam, pe, pn, beta):
    # neutron +z -> proton (m_p) x pair: Fermi: pair singlet, proton +z.  GT: |1/2,+1/2> = -sqrt(1/3)|T0>|p+> + sqrt(2/3)|T+1>|p->
    # GT: pair created by the VECTOR operator sigma acting on the neutron: sum_i (sigma_i |n>) (x) |T_i> (Cartesian triplet),
    # = lam*[ |p+>|T0> - sqrt2 |p->|T+1> ], norm^2 = 3 lam^2. (Clebsch-normalised J=1/2 coupling would lose the sqrt3.)
    comps = {'p+': S + lam*T[0], 'p-': -lam*np.sqrt(2)*T[+1]}
    rho = sum(np.outer(v, v.conj()) for v in comps.values())
    pe_h = pe/np.linalg.norm(pe); pn_h = pn/np.linalg.norm(pn)
    Pe = np.eye(2) - beta*sum(c*s for c,s in zip(pe_h, sig)); Pn = np.eye(2) + sum(c*s for c,s in zip(pn_h, sig))
    return np.real(np.trace(rho @ np.kron(Pe, Pn)))
def level3(pe, pn, beta, g, pol):
    # 4206: s = +/-z with <s_z> = pol; e spin = s, ejected along -s (bias beta); GT (prob g): nubar spin +s; Fermi: -s
    pe_h = pe/np.linalg.norm(pe); pn_h = pn/np.linalg.norm(pn); W = 0
    for s, ps in ((+1,(1+pol)/2), (-1,(1-pol)/2)):
        W += ps*(1 - beta*s*pe_h[2])*(g*(1 + s*pn_h[2]) + (1-g)*(1 - s*pn_h[2]))
    return W
def fit(Wfun, beta):
    # sample directions, least-squares for (1, a b c_enu, A b c_e, B c_nu)
    rng = np.random.default_rng(1); rows, ys = [], []
    for _ in range(600):
        e = rng.normal(size=3); e/=np.linalg.norm(e); n = rng.normal(size=3); n/=np.linalg.norm(n)
        rows.append([1, beta*(e@n), beta*e[2], n[2]]); ys.append(Wfun(e, n))
    c, *_ = np.linalg.lstsq(np.array(rows), np.array(ys), rcond=None); return c[1:]/c[0]
def jtw(l): D = 1+3*l*l; return (1-l*l)/D, -2*l*(l+1)/D, 2*l*(l-1)/D
beta = 0.999; pe_mag = 0.511*beta/np.sqrt(1-beta**2)
print(f"{'':50s} {'a':>7s} {'A':>7s} {'B':>7s}   (beta = {beta})")
for l in (-1.2754, +1.2754, -100.0, 0.0):
    a1, A1, B1 = fit(lambda e,n: level1(l, pe_mag*e, 1.0*n), beta)
    print(f"{'LEVEL 1 V-A, lambda = %+.4f' % l:50s} {a1:+7.3f} {A1:+7.3f} {B1:+7.3f}")
print(f"{'JTW formula, lambda = -1.2754':50s} {jtw(-1.2754)[0]:+7.3f} {jtw(-1.2754)[1]:+7.3f} {jtw(-1.2754)[2]:+7.3f}")
print()
for l in (-1.2754, +1.2754, -100.0, 0.0):
    a2, A2, B2 = fit(lambda e,n: level2(l, e, n, beta), beta)
    print(f"{'LEVEL 2 pair-state model (sqrt3 fixed), lambda = %+.4f' % l:50s} {a2:+7.3f} {A2:+7.3f} {B2:+7.3f}")
print()
for g, pol, nm in ((1.0, 2/3, 'LEVEL 3 classical (4206), pure GT, pol 2/3'), (0.0, 2/3, 'LEVEL 3 classical (4206), pure Fermi, pol 2/3'), (0.83, 2/3, 'LEVEL 3 classical (4206), g=0.83, pol 2/3')):
    a3, A3, B3 = fit(lambda e,n: level3(e, n, beta, g, pol), beta)
    print(f"{nm:50s} {a3:+7.3f} {A3:+7.3f} {B3:+7.3f}")

print("\nLEVEL 2 vs LEVEL 1, max |difference| over (a, A, B), lambda sign matched (the two gamma5/lambda conventions differ by a sign):")
for b in (0.3, 0.7, 0.999):
    pm = 0.511*b/np.sqrt(1-b**2); worst = 0
    for l in (-1.2754, -0.5, -3.0, 0.8, 2.0):
        c1 = np.array(fit(lambda e,n: level1(-l, pm*e, 1.0*n), b)); c2 = np.array(fit(lambda e,n: level2(l, e, n, b), b))
        worst = max(worst, np.max(np.abs(c1-c2)))
    print(f"   beta = {b:5.3f}:  max |L2 - L1| = {worst:.1e}")
print("""
What the pair-state model contains, and nothing else:
  (1) helicity by the ejection rule: electron along -spin with bias beta, antineutrino along +spin with bias 1;
  (2) the pair's SPIN STATE fixed by angular momentum: same-sense refill -> singlet (nothing leaves the nucleon's spin);
      opposite-sense refill -> the triplet the vector operator sigma writes, all three components, so weight 3 lam^2;
  (3) the two senses add as AMPLITUDES with ratio lam (c03), and interfere only through the m=0 triplet component,
      which shares the proton state with the singlet.
Level 3 (4206) differs from Level 2 in exactly one place: it gives the electron a definite spin = the quark's in BOTH
channels. That is what a singlet forbids, and it is why its Fermi column is wrong and its A never depends on the channel.""")

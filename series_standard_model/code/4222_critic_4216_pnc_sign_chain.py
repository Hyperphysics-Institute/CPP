#!/usr/bin/env python3
"""4222 critic of 4216 -- the sign gamma5 -> sigma.p/mc re-derived by explicit Dirac algebra, and the
electron-nucleon PNC Hamiltonian rebuilt from the PDG neutral-current couplings, not taken from a
textbook 'standard form'.  Convention: gamma5 = i g0 g1 g2 g3 (Bjorken-Drell / PDG), P_L = (1-gamma5)/2."""
import numpy as np
I2 = np.eye(2); Z2 = np.zeros((2,2))
sx, sy, sz = np.array([[0,1],[1,0]]), np.array([[0,-1j],[1j,0]]), np.array([[1,0],[0,-1]])
sig = [sx, sy, sz]
g0 = np.block([[I2, Z2],[Z2, -I2]]); gi = [np.block([[Z2, s],[-s, Z2]]) for s in sig]
g5 = 1j*g0@gi[0]@gi[1]@gi[2]
print("gamma5 (BD) =", np.real_if_close(g5).astype(int).tolist())
# 1. Dirac reduction: positive-energy spinor of momentum p, spin along n; compute <gamma5>/<sigma.p/m>
m = 1.0
for trial in range(3):
    p = np.random.default_rng(trial).normal(size=3)*0.05*m
    E = np.sqrt(m*m + p@p); n = np.random.default_rng(10+trial).normal(size=3); n/=np.linalg.norm(n)
    # spin-n two-spinor
    w, v = np.linalg.eigh(sum(nk*sk for nk,sk in zip(n,sig))); chi = v[:, np.argmax(w)]
    sp = sum(pk*sk for pk,sk in zip(p,sig))
    u = np.concatenate([np.sqrt(E+m)*chi, sp@chi/np.sqrt(E+m)])
    g5_exp = (u.conj()@g5@u) / (u.conj()@u)
    spm_exp = (chi.conj()@sp@chi) / m
    print(f"  trial {trial}: <gamma5> = {g5_exp.real:+.5f}   <sigma.p>/m = {spm_exp.real:+.5f}   ratio = {(g5_exp/spm_exp).real:+.4f}  (expect +1 to O(p^2/m^2))")
# 2. Q_W from PDG couplings (tree), s^2 = CPP's 3/(8 phi)
phi = (1+5**.5)/2; s2 = 3/(8*phi)
gAe = -0.5; gVu = 0.5 - 4/3*s2; gVd = -0.5 + 2/3*s2
C1u, C1d = 2*gAe*gVu, 2*gAe*gVd
QW = lambda Z, N: -2*(Z*(2*C1u+C1d) + N*(C1u+2*C1d))
print(f"\nC1u = {C1u:+.4f}  C1d = {C1d:+.4f}   Q_W(p) = {QW(1,0):+.4f}   Q_W(n) = {QW(0,1):+.4f}   Q_W(Cs, tree) = {QW(55,78):+.2f}  (measured -72.6)")
print("""
3. Sign chain (each step explicit; the first draft of this script wrote the L_eff sign from memory
   with a leading minus and concluded 'OPPOSITE to 4216' -- that was the error, corrected here):
   Z exchange: L_Z = -(g/2c) J~.Z, J~ = sum_f f-bar g^mu (gV - gA g5) f, gA = T3, gV = T3 - 2Q s^2, g5 = g5_BD
   integrate out Z (L = 1/2 mZ^2 Z^2 - J.Z => Z = J/mZ^2):  L_eff = -(g/2c)^2 J~.J~/(2 mZ^2) = -(G_F/sqrt2) J~.J~
   [sign anchored: the same step for W exchange gives L = -(G_F/sqrt2)[u-bar g(1-g5)d][e-bar g(1-g5)nu], the Fermi form]
   e-q cross term, PV part:  L^PV = +(G_F/sqrt2) sum_q C1q (e-bar g^mu g5 e)(q-bar g_mu q),  C1q = 2 gAe gVq   [= Roberts 1408.5463 eq 3.9]
   NR nucleus: q-bar g_mu q -> delta_{mu0} n_q(r);  sum_q C1q n_q = -(Q_W/2) rho(r)
   => L^PV = -(G_F Q_W/(2 sqrt2)) rho (e^dag g5_BD e);   H = -L  =>  H_PNC = +(G_F Q_W/(2 sqrt2)) rho gamma5_BD
   Literature: Dzuba-Flambaum H = (G_F/sqrt2)(-Q_W/2) g5 rho with the Landau-Lifshitz g5 = -g5_BD  [arXiv:1210.3891 eq 1];
               Sahoo review   H = +(G_F/(2 sqrt2)) Q_W g5 rho                                    [physics/0508016 eq 52].
   The two agree with each other and with the chain above once the gamma5 conventions are matched.
   Reduction (step 1 above, explicit spinors): <gamma5_BD> = +<sigma.p>/m
   => H_NR = +(G_F Q_W/(4 sqrt2 m)) {sigma.p, rho};   v_extra = dH/dp = +(G_F Q_W rho/(2 sqrt2 m)) sigma
   => drift ALONG Q_W sigma; Q_W(n) = -1 => the electron drifts AGAINST its spin.   4216 sign CONFIRMED.
""")

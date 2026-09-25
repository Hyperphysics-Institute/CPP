#!/usr/bin/env python3
"""4284 -- PD-008 critic of 4276 (and 4273/4274), 4274's double-counting argument, and 4266's rejection.
Reuses 4276's machinery verbatim (its script, minus the driver loop), then:
 (A) g_A and r_p against the frame size at 4276's own length unit (m_q = m_p/3), to show the lever;
 (B) g_A with the u-u exchange removed;  (C) Gaussian vs the true route-(H) momentum distribution for the u;
 (D) ONE m_q throughout: r_ZBW = hbar c/m_q with m_q the value mu_p fixes (4272 sec.1: r_ZBW = hbar/mc, same m),
     lengths in r_ZBW units, t = u-d edge / r_ZBW;
 (E) the Pauli (exchange) kinetic energy of the u-u pair against separation: the one r-dependent kinetic term left.
"""
import os, pathlib, types, numpy as np
src=(pathlib.Path(__file__).parent/"4276_folded_square_frame.py").read_text()
src=src[:src.index("for ratio in (1.0,1.2")].replace("N=1_500_000","N=1_000_000")
M=types.ModuleType("m4276"); exec(src,M.__dict__)
e,z,O=M.e,M.z,M.O; MN=938.919; GA=1.2754; RP=0.8409; MUN=-1.91304

print("(A) 4276's length unit (m_q = m_p/3), shape u-u/u-d = 1.2 (4276's fitted a = 0.509 fm)")
for a in (0.35,0.42,0.509,0.60,0.70,0.85):
    D,n,th=M.fold(1.2,a); rp,g,s,sp,Ru,Rd=M.run((D,a),n)
    print(f"  a={a:.3f} fm  r_p={rp:.4f}  g_A={g:.4f} ({100*(g/GA-1):+.2f}%)  overlap p={sp:.3f}")

a=0.509; D,n,th=M.fold(1.2,a); u1,u2,d=M.geo((D,a)); ax=[z,e(u1,u2),e(u1,d)]
rng=np.random.default_rng(7); N=2_000_000
C1=M.sr**2*O(ax[0])+M.sr**2*O(ax[1])+M.ss**2*O(ax[2])
pg=rng.normal(size=(N,3))@np.linalg.cholesky(C1).T; fg=np.mean(1/np.sqrt((pg**2).sum(1)+1))
U=[rng.random(N) for _ in range(3)]
pt=M.smp(M.pa,M.Pa,U[0])[:,None]*ax[0]+M.smp(M.pa,M.Pa,U[1])[:,None]*ax[1]+M.smp(M.ps,M.Ps,U[2])[:,None]*ax[2]
ft=np.mean(1/np.sqrt((pt**2).sum(1)+1)); Rg,Rt=1/3+2/3*fg,1/3+2/3*ft; Rd=M.run((D,a),n)[5]
print(f"\n(C) u, no exchange: Gaussian R_u={Rg:.4f}  true-distribution R_u={Rt:.4f}  -> g_A shift {4/3*(Rt-Rg):+.4f}  (kurtosis pa {np.sum(M.pa**4*M.Pa)/M.sr**4:.2f}, Gaussian 3)")
print(f"(B) exchange off: g_A = {4/3*Rg+Rd/3:.4f} (Gaussian u), {4/3*Rt+Rd/3:.4f} (true u);  4276 row with exchange: 1.2681")

print("\n(D) ONE m_q throughout (r_ZBW = hbar c/m_q, m_q from mu_p).  t = u-d edge / r_ZBW")
M.rZ=1.0
for ratio in (1.0,1.2,2**0.5-1e-6):
    print(f"ratio u-u/u-d = {ratio:.3f}")
    for t in (0.05,0.2,0.4,0.6,0.8,1.0):
        D,n,th=M.fold(ratio,t); rpu,g,s,sp,Ru,Rd=M.run((D,t),n)
        Sl,So=(1+Ru)/2,(1+Rd)/2; mq=MN*(4*(2/3)*Sl+(1/3)*So)/3/2.79285; mn=MN/mq*(4*(-1/3)*Sl-(2/3)*So)/3; rp=rpu*197.327/mq
        print(f"  t={t:.2f}  m_q(mu_p)={mq:6.1f} MeV  r_p={rp:.4f} fm ({100*(rp/RP-1):+.1f}%)  g_A={g:.4f} ({100*(g/GA-1):+.2f}%)  mu_n={mn:.3f} ({100*(mn/MUN-1):+.1f}%)  overlap p={sp:.2f}")

print("\n(E) Pauli kinetic energy per u (units m_q c^2), shape 1.2, lengths in r_ZBW")
rng=np.random.default_rng(3); prev=None
for t in (0.4,0.6,0.8,1.0,1.2,1.5):
    D,n,th=M.fold(1.2,t); u1,u2,d=M.geo((D,t))
    cov=lambda u,o:M.sr**2*O(z)+M.sr**2*O(e(u,o))+M.ss**2*O(e(u,d)); C1,C2=cov(u1,u2),cov(u2,u1); I1,I2=np.linalg.inv(C1),np.linalg.inv(C2)
    p=rng.normal(size=(N,3))@np.linalg.cholesky(C1).T; T=np.sqrt((p**2).sum(1)+1)-1; qq=lambda P,I:np.einsum('ni,ij,nj->n',P,I,P)
    rc=np.exp(-(qq(p,I2)-qq(p,I1))/4)*(np.linalg.det(C1)/np.linalg.det(C2))**0.25*np.cos(p@(u2-u1)); sp=rc.mean()
    Tx=(T.mean()-sp*np.mean(T*rc))/(1-sp*sp); ex=2*(Tx-T.mean())
    s=f"  u-u={D:.2f}  overlap={sp:.2f}  pair Pauli excess={ex:+.4f}"
    if prev: s+=f"  dE/d(u-u)={(ex-prev[1])/(D-prev[0]):+.3f} m_q c^2/r_ZBW"
    prev=(D,ex); print(s)
print("\n-> (D): with one m_q, r_p >= +1.0% at every size and shape (floor at a collapsed frame); 4276's rows sit at +5% to +6%.")
print("   g_A then depends on t alone and spans -2.6% .. +0.5% over the allowed range; it is not pinned by r_p.")

#!/usr/bin/env python3
"""4269 -- the u-d exchange (TODO-4234-DELTA item (ii)), under colour = vertex.
Two consistent limits bound it:
 (L1) flavour pinned to seat (founder 4262: the d is bound to the +qCP vertex, the u's to the two minus vertices).
      The u-d exchanged configuration puts a d on a minus vertex -- not in the state -- so only the u-u exchange acts
      (4262): 2-orbital Slater of the two u-seat orbitals; the d keeps its own R.
 (L2) full SU(3) colour antisymmetry over the three seats with the spin-flavour part symmetric and factored out
      (the SU(6) 56, as 4240): the SPACE part is a 3-orbital Slater determinant of the seat orbitals, every quark
      sees the same one-body density, R_u = R_d.  Seat orbitals as 4262 (u seats: radial + diagonal + sideways;
      d seat: radial + two sideways), Gaussian shapes with 4244's REL rms; seat orbital independent of occupant
      (an approximation: 'a new seat means new forces', founders_voice/phenomenon_su3).
One-body density of an n-orbital Slater: rho(p) = (1/n) sum_ij (S^-1)_ji phi_i*(p) phi_j(p), S the overlap matrix."""
import numpy as np
rng=np.random.default_rng(11); N=3_000_000
rZ=197.327/(938.272/3); duu,dud=1.071/rZ,0.620/rZ; h=np.sqrt(dud**2-(duu/2)**2)
u1=np.array([-duu/2,0,0]); d=np.array([0,h,0]); u2=np.array([duu/2,0,0]); e=lambda a,b:(b-a)/np.linalg.norm(b-a); z=np.array([0,0,1.])
sr,ss=0.7917,0.5353
O=lambda n:np.outer(n,n)
Cu1=sr**2*O(z)+sr**2*O(e(u1,u2))+ss**2*O(e(u1,d)); Cu2=sr**2*O(z)+sr**2*O(e(u2,u1))+ss**2*O(e(u2,d))
Cd=sr**2*O(z)+ss**2*O(e(d,u1))+ss**2*O(e(d,u2))
def lnN(P,C): I=np.linalg.inv(C); return -0.5*np.einsum('ni,ij,nj->n',P,I,P)-0.5*np.log(np.linalg.det(2*np.pi*C))
def slater(orbs):
    Cs=[o[0] for o in orbs]; Rs=[o[1] for o in orbs]; n=len(orbs)
    comp=rng.integers(0,n,N); P=np.zeros((N,3))
    for k in range(n):
        m=comp==k; P[m]=rng.normal(size=(m.sum(),3))@np.linalg.cholesky(Cs[k]).T
    L=np.stack([lnN(P,C) for C in Cs]); q=np.exp(L).mean(0)
    A=np.exp(0.5*L)  # amplitudes (real part), phases e^{-ip.R}
    ph=np.stack([P@R for R in Rs])
    S=np.zeros((n,n))
    for i in range(n):
        for j in range(n): S[i,j]=np.mean(A[i]*A[j]*np.cos(ph[i]-ph[j])/q)
    Si=np.linalg.inv(S)
    rho=sum(Si[j,i]*A[i]*A[j]*np.cos(ph[i]-ph[j]) for i in range(n) for j in range(n))/n
    w=rho/q; f=1/np.sqrt((P**2).sum(1)+1)
    return S, np.mean(w), 1/3+2/3*np.mean(w*f)/np.mean(w)
MN=938.919; mq=938.272/3; xq=MN/mq; gA_t,mup_t,mun_t=1.2754,2.79285,-1.91304
def row(lab,Ru,Rd):
    g=4/3*Ru+Rd/3; Su,Sd=(1+Ru)/2,(1+Rd)/2; mp=(4*(2/3)*xq*Su+(1/3)*xq*Sd)/3; mn=(4*(-1/3)*xq*Sd-(2/3)*xq*Su)/3
    mf=mq*mp/mup_t; mnf=mn*mq/mf
    print(f"  {lab:44s} R_u={Ru:.4f} R_d={Rd:.4f}  g_A={g:.4f} ({100*(g/gA_t-1):+5.1f}%)  mu_p={mp:.3f} ({100*(mp/mup_t-1):+5.1f}%)  m_q(mu_p)={mf:.1f}  mu_n then {mnf:.3f} ({100*(mnf/mun_t-1):+5.1f}%)")
_,_,Rd0=slater([(Cd,d)])
S2,_,Ru2=slater([(Cu1,u1),(Cu2,u2)]); print("overlaps, u-seats:",np.round(S2,3).tolist())
row("(L1) flavour pinned: u-u exchange only",Ru2,Rd0)
S3,_,R3=slater([(Cu1,u1),(Cu2,u2),(Cd,d)]); print("overlaps, three seats (u1,u2,d):",np.round(S3,3).tolist())
row("(L2) full colour antisymmetry, 3 seats",R3,R3)
print("\n-> The u-d exchange is zero if the d never leaves the +qCP seat (L1, 1.310) and brings g_A to 1.272 (-0.3%) if")
print("   colour antisymmetry runs over all three seats (L2).  Which holds is a physical question (4269 s4).")

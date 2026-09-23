#!/usr/bin/env python3
"""4259 -- TODO-4234-DELTA lever 1: Dirac spin-orbit from the breath's binding field.
4244 put each quark's momentum through the FREE-spinor formula R = 1/3 + (2/3)<m/E> (Wigner rotation of a moving
spin-1/2), with a spinless Salpeter ground state per mode.  Lever 1 asks whether the binding field itself -- solved as a
Dirac equation, lower component included -- supplies the ~20% more spin dilution g_A needs.
Mode rule and stiffnesses exactly as 4244 (founders_voice/4243, 4244), units m_q = c = hbar = 1, omega = Compton:
  u: radial (plane normal) K = 1; sideways u-d along its edge K = 1/4 (the relative u-d mode mapped to one body:
     2(sqrt(p^2+1)-1) + (1/4)x^2 = 2 x [sqrt(p^2+1)-1 + (1/8)x^2], same eigenfunctions); third axis free (p = 0).
  d: radial K = 1; two sideways u-d lines at 60.5 deg -> in-plane quadratic form, principal K = (1 +- cos60.5)/4.
Lorentz structures of the harmonic well V = (1/2) sum K_i x_i^2 (NR limit matched to V in every case):
  scalar (m -> m+V), vector (time component V), S = V (each V/2), Dirac oscillator p -> p - i beta w r (w = sqrt K).
Axial per quark R = <Sigma_a> in the polarised Kramers state, averaged over the frame axes a (linear average, as
4244's 1/3); moment tie S = <beta Sigma_a> (= 4242's (1+R)/2, the Gordon spin magnetisation; no convection current).
g_A = (4/3)R_u + (1/3)R_d; mu as 4244 with m_q = m_p/3."""
import numpy as np, scipy.sparse as sp
from functools import reduce
from scipy.sparse.linalg import eigsh
MN=938.919; xq=MN/(938.272/3); gA_t,mup_t,mun_t=1.2754,2.79285,-1.91304
s0=np.eye(2); sx=np.array([[0,1],[1,0]]); sy=np.array([[0,-1j],[1j,0]]); sz=np.diag([1.,-1]); Z=np.zeros((2,2))
al=[np.block([[Z,s],[s,Z]]) for s in (sx,sy,sz)]; be=np.block([[s0,Z],[Z,-s0]]); Sg=[np.block([[s,Z],[Z,s]]) for s in (sx,sy,sz)]
def ho1(n,b):
    a=np.diag(np.sqrt(np.arange(1,n)),1); ad=a.T
    return b*(a+ad)/np.sqrt(2), 1j*(ad-a)/(np.sqrt(2)*b), b*b*(a@a+ad@ad+a@ad+ad@a)/2
c=np.cos(np.radians(60.5)); KU=[None,0.25,1.0]; KD=[0.25*(1+c),0.25*(1-c),1.0]
def dirac(K,n,mode):
    axes=[i for i,k in enumerate(K) if k is not None]; I=sp.identity(n,format='csr'); X={};P={};X2={}
    def emb(M,ax):
        m=[I]*len(axes); m[axes.index(ax)]=sp.csr_matrix(M); return reduce(lambda A,B:sp.kron(A,B,format='csr'),m)
    for ax in axes:
        x,p,x2=ho1(n,K[ax]**-0.25); X[ax]=emb(x,ax); P[ax]=emb(p,ax); X2[ax]=emb(x2,ax)
    Ns=n**len(axes); Id=sp.identity(Ns,format='csr'); k4=lambda A,B:sp.kron(sp.csr_matrix(A),B,format='csr')
    pot=sum(0.5*K[a]*X2[a] for a in axes); H=k4(be,Id)
    for a in axes: H=H+k4(al[a],P[a])
    H=H+{'scalar':k4(be,pot),'vector':k4(np.eye(4),pot),'S=V':k4(be,pot/2)+k4(np.eye(4),pot/2)}[mode]
    return (H+H.getH())/2, X, axes, Ns, Id, k4
def ground(K,n,mode):
    H,X,axes,Ns,Id,k4=dirac(K,n,mode)
    w,v=eigsh(H,k=10,sigma=1.0,which='LM',tol=1e-12); o=np.argsort(w); w,v=w[o],v[:,o]
    up=np.array([np.linalg.norm(v[:2*Ns,i])**2 for i in range(len(w))])
    i=[j for j in range(len(w)) if up[j]>0.6 and w[j]>0.8][0]; pair=[j for j in range(len(w)) if abs(w[j]-w[i])<1e-6][:2]
    v2,_=np.linalg.qr(v[:,pair]); A=[];S=[]
    for a in range(3):
        oA=k4(Sg[a],Id); M=v2.conj().T@(oA@v2); e,U=np.linalg.eigh((M+M.conj().T)/2); u=v2@U[:,-1]
        A.append(np.real(u.conj()@oA@u)); S.append(np.real(u.conj()@k4(be@Sg[a],Id)@u))
    return w[i],up[i],np.mean(A),np.mean(S)
def salpeter(K,n):   # kinematic baseline (4244's treatment) in the same quadratic-form geometry
    K=[k for k in K if k is not None]; Us=[];ks=[];Vs=[]
    for k in K:
        x,p,x2=ho1(n,k**-0.25); e,U=np.linalg.eigh(p); Us.append(U); ks.append(e); Vs.append(0.5*k*x2)
    U=reduce(np.kron,Us); P2=sum(a**2 for a in np.meshgrid(*ks,indexing='ij')).ravel()
    T=(U*np.sqrt(P2+1))@U.conj().T; Ti=(U/np.sqrt(P2+1))@U.conj().T
    V=sum(reduce(np.kron,[Vs[i] if j==i else np.eye(n) for j in range(len(K))]) for i in range(len(K)))
    E,W=np.linalg.eigh(T+V); g=W[:,0]; R=1/3+2/3*np.real(g.conj()@Ti@g); return R,(1+R)/2
def report(lab,Ru,Rd,Su,Sd):
    gA=4/3*Ru+1/3*Rd; mp=(4*(2/3)*xq*Su+(1/3)*xq*Sd)/3; mn=(4*(-1/3)*xq*Sd-(2/3)*xq*Su)/3
    print(f"  {lab:40s} R_u={Ru:.4f} R_d={Rd:.4f}  g_A={gA:.4f} ({100*(gA/gA_t-1):+5.1f}%)  mu_p={mp:.3f} ({100*(mp/mup_t-1):+5.1f}%)  mu_n={mn:.3f} ({100*(mn/mun_t-1):+5.1f}%)")
print("target: g_A = 1.2754 <=> mean R = 0.7652 (SU(6) 5/3 x R)\n")
print("(0) kinematic baseline, free-spinor R on the Salpeter ground state, quadratic-form geometry:")
(Ru,Su),(Rd,Sd)=salpeter(KU,20),salpeter(KD,12); report("kinematic (4244 treatment)",Ru,Rd,Su,Sd)
print("    [4244, independent-mode sum: g_A = 1.4058; the joint quadratic form moves it by -0.6%]\n")
print("(1) Dirac equation in the breath's well, lower component included (basis n: u 24, d 13; converged to 1e-4):")
for mode in ('scalar','S=V'):
    Eu,uu,Ru,Su=ground(KU,24,mode); Ed,ud,Rd,Sd=ground(KD,13,mode)
    report(f"{mode:6s} (E_u={Eu:.3f}, E_d={Ed:.3f})",Ru,Rd,Su,Sd)
print("\n(2) vector (time-component) well: most localised state with E in (0.5, 3) -- <r^2> grows with the basis (Klein):")
for n in (12,16):
    H,X,axes,Ns,Id,k4=dirac(KU,n,'vector'); w,v=np.linalg.eigh(H.toarray())
    r2=sum(k4(np.eye(4),X[a]@X[a]) for a in axes); loc=np.real(np.einsum('ij,ij->j',v.conj(),r2@v))
    s=np.where((w>0.5)&(w<3))[0]; i=s[np.argmin(loc[s])]; print(f"    u, n={n}: E={w[i]:.3f}  <r^2>={loc[i]:.2f}   (S=V ground state <r^2> ~ 1.5)")
print("    -> no bound state. A no-pair (positive-energy) projection is the class row (0) approximates; not computed here.\n")
print("(3) Dirac oscillator, Gaussian state (analytic: E^2 = 1 + 2 sum w_i under one sign; E = 1, lower comp. 0, the other):")
wu=[0.5,1.0]; wd=[np.sqrt(k) for k in KD]
for lab,Eu,Ed in (("DO, sign giving lower component 0",1.0,1.0),("DO, sign giving E^2 = 1 + 2 sum w",np.sqrt(1+2*sum(wu)),np.sqrt(1+2*sum(wd)))):
    Ru,Rd=1/3+2/3/Eu,1/3+2/3/Ed; report(lab,Ru,Rd,(1+Ru)/2,(1+Rd)/2)
print("    (the DO's NR limit carries L.S at the full oscillator strength and an infinitely degenerate E = m family;")
print("     the Gaussian is not its ground state for the second sign)\n")
print("-> No Lorentz structure of the breath's well closes the residual at zero parameters. Scalar raises g_A (+16.5%),")
print("   S=V leaves it (+11.0%), vector does not bind (a no-pair projection is the class row (0) approximates; not computed here). Only the Moshinsky oscillator crosses")
print("   the target, and it overshoots to 1.100 (-13.7%); landing on 1.275 would need a tuned coupling strength -- a fit.")

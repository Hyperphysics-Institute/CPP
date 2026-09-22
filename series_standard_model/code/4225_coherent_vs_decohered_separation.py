#!/usr/bin/env python3
"""4225 -- does the founder's 'spins mix until they separate, then the spin is fixed' survive as stated?
Two readings of 'fixed at separation':
  (A) coherent: the two leptons leave in the pair state of 4223 and each spin is fixed only when measured
      (i.e. by the ejection rule acting on the pair state);
  (B) decohered: at separation the pair collapses to ONE product configuration (e up/nubar down, etc.) with
      the probabilities of 4224, and each lepton is then ejected by the handed rule with its fixed spin.
Both give the same A and B (those depend only on the populations). They differ in a, the e-nubar angular
correlation, which depends on the coherence between |e+ nu-> and |e- nu+>."""
import numpy as np
sx, sy, sz = np.array([[0,1],[1,0]],complex), np.array([[0,-1j],[1j,0]]), np.array([[1,0],[0,-1]],complex); sig=[sx,sy,sz]
up, dn = np.array([1,0],complex), np.array([0,1],complex)
S = (np.kron(up,dn)-np.kron(dn,up))/np.sqrt(2); T0=(np.kron(up,dn)+np.kron(dn,up))/np.sqrt(2); Tp=np.kron(up,up)
def rho_pair(lam, coherent):
    comps = [S + lam*T0, -lam*np.sqrt(2)*Tp]
    rho = sum(np.outer(v, v.conj()) for v in comps)
    if not coherent:   # kill coherence between product configurations in the z basis
        rho = np.diag(np.diag(rho))
    return rho
def fit(rho, beta, n=1500):
    rng=np.random.default_rng(2); X=[]; y=[]
    for _ in range(n):
        e=rng.normal(size=3); e/=np.linalg.norm(e); v=rng.normal(size=3); v/=np.linalg.norm(v)
        Pe=np.eye(2)-beta*sum(c*s for c,s in zip(e,sig)); Pn=np.eye(2)+sum(c*s for c,s in zip(v,sig))
        X.append([1,beta*(e@v),beta*e[2],v[2]]); y.append(np.real(np.trace(rho@np.kron(Pe,Pn))))
    c,*_=np.linalg.lstsq(np.array(X),np.array(y),rcond=None); return c[1:]/c[0]
print(f"{'':44s} {'a':>7s} {'A':>7s} {'B':>7s}")
for lam, nm in ((-1.2754,'measured lambda'), (0.0,'pure Fermi'), (-1e4,'pure GT')):
    for coh in (True, False):
        a,A,B = fit(rho_pair(lam, coh), 0.999)
        print(f"{nm+', '+('(A) coherent' if coh else '(B) decohered at separation'):44s} {a:+7.3f} {A:+7.3f} {B:+7.3f}")
print("\nmeasured: a = -0.104 to -0.108 (recent measurements, uncertainty below 0.001); A = -0.119; B = +0.987")

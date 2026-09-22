#!/usr/bin/env python3
"""4227 -- the founder's restatement of the swapped allocation, built literally and evaluated.
'Release of the orbital eDP (antineutrino); then formation of a pair of opposite-spin DPs, one to replace
the qCP orbital (proton), one to fill the orbital of the liberated -eCP (electron).'
Built literally: antineutrino = the quark's orbital, spin s (+z); (proton, electron) = one created pair with
zero net angular momentum = singlet.  Evaluated with the ejection rule; plus the proton asymmetry C from
A and B (C = -x_C (A + B), x_C = 0.27484, the standard kinematic factor for neutron decay)."""
import numpy as np
sx, sy, sz = np.array([[0,1],[1,0]],complex), np.array([[0,-1j],[1j,0]]), np.array([[1,0],[0,-1]],complex); sig=[sx,sy,sz]
up, dn = np.array([1,0],complex), np.array([0,1],complex); k=np.kron
def fit(comps, beta=0.999, n=1500):
    rho = sum(np.outer(v, v.conj()) for v in comps.values()); rng=np.random.default_rng(3); X=[]; y=[]
    for _ in range(n):
        e=rng.normal(size=3); e/=np.linalg.norm(e); v=rng.normal(size=3); v/=np.linalg.norm(v)
        Pe=np.eye(2)-beta*sum(c*s for c,s in zip(e,sig)); Pn=np.eye(2)+sum(c*s for c,s in zip(v,sig))
        X.append([1,beta*(e@v),beta*e[2],v[2]]); y.append(np.real(np.trace(rho@k(Pe,Pn))))
    c,*_=np.linalg.lstsq(np.array(X),np.array(y),rcond=None); return c[1:]/c[0]
# founder's restatement, literally: |nubar: +z> (x) singlet_(p,e) = (p+ e- - p- e+)/sqrt2
vertex = {'p+': k(dn, up), 'p-': -k(up, up)}
a,A,B = fit(vertex); print(f"vertex (founder's restatement, literal):  a = {a:+.3f}  A = {A:+.3f}  B = {B:+.3f}")
# with the 10% nucleon admixture (4226 c)
lam=-1.2754; d=lam+1
S=(k(up,dn)-k(dn,up))/np.sqrt(2); T0=(k(up,dn)+k(dn,up))/np.sqrt(2); Tp=k(up,up)
a,A,B = fit({'p+': -np.sqrt(2)*k(dn,up)+d*T0, 'p-': np.sqrt(2)*k(up,up)-np.sqrt(2)*d*Tp})
xC=0.27484; C=-xC*(A+B)
print(f"nucleon (vertex + delta admixture):       a = {a:+.3f}  A = {A:+.3f}  B = {B:+.3f}   C = -x_C(A+B) = {C:+.4f}  (measured C = -0.2377 +/- 0.0026)")
# what is entangled with what, at the vertex: reduced states
psi = np.zeros(8, complex)  # basis p,e,nu
def idx(p,e,n): return p*4+e*2+n
psi[idx(0,1,0)] = 1/np.sqrt(2); psi[idx(1,0,0)] = -1/np.sqrt(2)     # (p+ e- - p- e+) nu+
rho = np.outer(psi, psi.conj()).reshape(2,2,2,2,2,2)
# purities
rho_pe_m = np.einsum('penPEn->pePE', rho).reshape(4,4); rho_en_m = np.einsum('penpEN->enEN', rho).reshape(4,4)
print(f"purity Tr(rho^2):  (proton, electron) pair = {np.real(np.trace(rho_pe_m@rho_pe_m)):.3f}   (electron, antineutrino) pair = {np.real(np.trace(rho_en_m@rho_en_m)):.3f}")
print("  -> at the vertex the proton and electron are the entangled pair (pure singlet); the antineutrino leaves in a product")
print("     state with them. The electron-antineutrino entanglement that a measures at the nucleon level is the delta admixture.")

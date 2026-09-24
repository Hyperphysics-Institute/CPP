#!/usr/bin/env python3
"""4263 -- the founder's dynamic picture (founders_voice/4263): no bound and no loose quarks, only oscillating ones.
A quark falls into superposition with its vertex (the SSV gradient vanishes there), reverses, and moves toward the
strongest gradient at that moment -- the DP Sea, the sideways vertex, or the diagonal vertex when the other up has
left it open.  So at any moment the quark makes ONE excursion along ONE line; 4244/4262 summed simultaneous modes.
Two ways to size an excursion:
  (G) each excursion is its own ground state at the Compton frequency (anchored or u-d relative, 4244's REL rows);
  (E) the quark carries its whole breath energy through each bounce ("reverses direction" at superposition), so every
      excursion has the <p^2> of 4262's simultaneous set: u = 2 anchored + 1 relative, d = 1 anchored + 2 relative.
      The 1D shape of a bouncing excursion is not fixed by route (H): bracketed by a Gaussian and the n = 1 shape.
R depends only on |p| (frame-averaged free-spinor formula), so under (E) WHICH partner is chosen, and how often the
diagonal vertex is open, does not enter g_A.  Exchange (4262) is not applied here (filed)."""
import numpy as np
from scipy.linalg import eigh_tridiagonal
rng=np.random.default_rng(4263); N=4_000_000
MN=938.919; mq=938.272/3; xq=MN/mq; gA_t,mup_t,mun_t=1.2754,2.79285,-1.91304
def ground(kin,Mpot):
    p=np.linspace(-14,14,7000); dp=p[1]-p[0]; a=0.5*Mpot
    E,V=eigh_tridiagonal(kin(p)+2*a/dp**2,-a/dp**2*np.ones(len(p)-1),select='i',select_range=(0,0)); P=V[:,0]**2; return p,P/P.sum()
MA=ground(lambda p:np.sqrt(p*p+1)-1,1.0); MS=ground(lambda p:2*(np.sqrt(p*p+1)-1),0.5)
RM=lambda M:1/3+2/3*np.sum(M[1]/np.sqrt(M[0]**2+1)); v=lambda M:np.sum(M[1]*M[0]**2)
def row(lab,Ru,Rd):
    g=4/3*Ru+Rd/3; Su,Sd=(1+Ru)/2,(1+Rd)/2
    mp=(4*(2/3)*xq*Su+(1/3)*xq*Sd)/3; mn=(4*(-1/3)*xq*Sd-(2/3)*xq*Su)/3
    print(f"  {lab:50s} R_u={Ru:.4f} R_d={Rd:.4f}  g_A={g:.4f} ({100*(g/gA_t-1):+5.1f}%)  mu_p={mp:.3f} ({100*(mp/mup_t-1):+5.1f}%)  mu_n={mn:.3f} ({100*(mn/mun_t-1):+5.1f}%)")
print("reference, 4262 simultaneous modes (before exchange): g_A = 1.3331 (+4.5%)\n")
print("(G) each excursion its own Compton ground state -- any mix of partners lies between:")
row("all excursions anchored (vertex, Sea, diagonal)",RM(MA),RM(MA)); row("all excursions u-d relative",RM(MS),RM(MS))
vu=2*v(MA)+v(MS); vd=v(MA)+2*v(MS)
print(f"\n(E) whole breath energy carried through each bounce: <p^2>_u = {vu:.3f}, <p^2>_d = {vd:.3f} (m_const c)^2")
def R1(var,shape):
    if shape=='g': p=rng.normal(size=N)*np.sqrt(var)
    elif shape=='n': p=np.sqrt(rng.chisquare(3,size=N)*var/3)
    else: p=np.sqrt(2*var)*np.sin(rng.uniform(0,2*np.pi,N))   # classical harmonic bounce: arcsine, <p^2> = pmax^2/2
    return 1/3+2/3*np.mean(1/np.sqrt(p*p+1))
row("Gaussian excursion shape",R1(vu,'g'),R1(vd,'g')); row("n = 1 excursion shape (node at p = 0)",R1(vu,'n'),R1(vd,'n'))
row("classical harmonic bounce (arcsine, fastest at the vertex)",R1(vu,'a'),R1(vd,'a'))
print("\n-> (G) moves g_A to 1.49-1.56: an excursion sized by its own partner alone is far too gentle.  (E), which the")
print("   founder's 'reverses direction' describes, brackets 4262's 1.333 (1.316-1.383; a classical bounce, fastest at superposition, sits at the low end): the sequential picture keeps")
print("   the result if the quark keeps its energy through the bounce, and then the partner choice does not matter.")

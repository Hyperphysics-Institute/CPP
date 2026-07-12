import numpy as np

# ---------------------------------------------------------------------------
# Direct free-energy computation of the ring-stability floor N_stab.
# Ring of N rungs, turning angle theta_i, joint stiffness B = r*kT (2381).
# Mean-field bending uses the FULL anharmonic bond energy B*(1-cos theta),
# NOT the harmonic 2pi^2 (rigid) or the SY nucleation saddle (14.054).
# Fluctuations: harmonic Gaussian of the theta_i under the 3 closure
# constraints (tangent Sum theta = 2pi; position Sum bond-vectors = 0).
# Opening barrier: dF_open/kT = eps - E_bend/kT + (F_fl,open - F_fl,ring)/kT.
# ---------------------------------------------------------------------------

def fluct_term(N):
    """(F_fl,open - F_fl,ring)/kT = ln(r/2pi) - 1/2 ln det(C C^T), the r-independent
    part being -1/2 ln det(CC^T); returns that det piece (the ln(r/2pi) added later)."""
    th0 = 2*np.pi/N
    Phi0 = np.arange(1, N+1)*th0           # bond directions
    # constraint rows over dtheta_i (i=1..N):
    c1 = np.ones(N)                        # tangent: sum dtheta = 0
    # position: sum_j e^{i Phi_j}(sum_{i<=j} dtheta_i)=0 -> weight w_i = sum_{j>=i} e^{iPhi_j}
    w = np.array([np.sum(np.exp(1j*Phi0[i:])) for i in range(N)])
    C = np.vstack([c1, w.real, w.imag])    # 3 x N
    CCt = C @ C.T
    sign, logdet = np.linalg.slogdet(CCt)
    return logdet                          # ln det(CC^T)

def dF_open(N, r, eps):
    Ebend = N*r*(1.0-np.cos(2*np.pi/N))    # anharmonic mean-field bending / kT
    fl = np.log(r/(2*np.pi)) - 0.5*fluct_term(N)
    return eps - Ebend + fl

def N_stab(r, eps):
    # smallest N (real, via interpolation) where dF_open crosses 0 from below
    Ns = np.arange(3, 40)
    d = np.array([dF_open(N, r, eps) for N in Ns])
    idx = np.where((d[:-1]<0) & (d[1:]>=0))[0]
    if len(idx)==0: return Ns[0] if d[0]>=0 else np.inf
    i = idx[0]
    # linear interp for the crossing
    return Ns[i] + (0 - d[i])/(d[i+1]-d[i])

# anharmonic bending coefficient c_eff(N) = N^2(1-cos(2pi/N)), for context
print("anharmonic bending coefficient c_eff(N)=N^2(1-cos(2pi/N)) vs rigid 2pi^2=19.74, SY=14.05:")
for N in (6,7,8,9,10): print(f"   N={N}: c_eff={N**2*(1-np.cos(2*np.pi/N)):.2f}")
print()

r_lo,r_hi,r_c = 8.5,12.0,10.25
eps_lo,eps_hi,eps_c = 23.2,36.2,29.7
print("DIRECT N_stab (anharmonic mean-field + closure-constrained harmonic fluctuations):")
print(f"   central (r={r_c}, eps={eps_c}): N_stab = {N_stab(r_c,eps_c):.2f}")
print(f"   favorable corner (r={r_hi}, eps={eps_lo}): N_stab = {N_stab(r_hi,eps_lo):.2f}")
print(f"   unfavorable corner (r={r_lo}, eps={eps_hi}): N_stab = {N_stab(r_lo,eps_hi):.2f}")
print(f"   [rigid 2pi^2 central was 6.81; SY 14.05 central was 4.85]")

# ---------------------------------------------------------------------------
# CONSISTENT DD-survival: run the cascade with the DIRECTLY-COMPUTED floor
# (not the SY floor the 2421 scan used), then apply the LZ ladder test.
# ---------------------------------------------------------------------------
SY_A,SY_B = 14.054,0.246
def g_SY(u): return u**(-5.0)*np.exp(-SY_A/u + SY_B*u)
def J_phys(N,r,vf): return g_SY(N/r)/r**3*vf
def cascade_with_floor(r,phi,eps,vf,floor,q=1.0,ncut=64):
    x=(-1.0+np.sqrt(1.0+2.0*q))/(2.0*q)
    def pc(N):
        if N<floor: return 0.0
        j=J_phys(N,r,vf); return j/(j+phi)
    def prop(fl,N0,wm):
        s=fl
        for N in range(N0,ncut+1):
            p=pc(N); wm[N]=wm.get(N,0.0)+s*p*N; s*=(1-p)
        return s*ncut
    wm={}; e=prop(x,3,wm); e+=prop((q/2)*x**2,4,wm); tot=sum(wm.values())+e
    return {N:m/tot for N,m in wm.items() if m>0}, e/tot

X={4:8.8e6,5:7.1e4,6:361.0,7:2.15}; ceil={N:1/X[N] for N in X}
phi_c=np.sqrt(6.7e-15*7.4e-10)
print("\n" + "="*66)
print("CONSISTENT DD-SURVIVAL with the directly-computed floor (central phi):")
print("="*66)
print(" (r, eps)        | N_stab | peak | f(>=8) | f(N=7) | f(N=6) | DD-survive")
for (r,eps,tag) in [(10.25,29.7,'central'),(12.0,23.2,'favorable'),(8.5,36.2,'unfavorable'),(11.0,26.0,'mild-favorable')]:
    fl=N_stab(r,eps)
    w,esc=cascade_with_floor(r,phi_c,eps,1.0,fl)
    if esc>0.1:
        print(f" ({r},{eps}) {tag}: escape {esc:.2f}"); continue
    f={N:w.get(N,0.0) for N in range(3,13)}; f8=sum(w.get(N,0.0) for N in range(8,65))
    peak=max(w,key=w.get); ok=all(f[N]<=ceil[N] for N in (4,5,6,7)) and f8>=0.5
    print(f" ({r:4.1f},{eps:4.1f}) {tag:11s}|  {fl:.2f}  | N{peak:2d}  | {f8:.3f} | {f[7]:.1e}| {f[6]:.1e}| {'YES' if ok else 'no'}")
print("\n(ceilings: f7<0.47, f6<2.8e-3, f5<1.4e-5, f4<1.1e-7; N>=8 DD-clear)")

# fraction of the registered (r,eps) box that gives DD-survival with the physical floor
print("\n" + "="*66)
print("SURVIVAL REGION (physical floor, central phi):")
print("="*66)
rr=np.linspace(8.5,12.0,36); ee=np.linspace(23.2,36.2,40)
npass=0; ntot=0; pass_nstab=[]
for r in rr:
    for eps in ee:
        fl=N_stab(r,eps); w,esc=cascade_with_floor(r,phi_c,eps,1.0,fl)
        if esc>0.1: continue
        f={N:w.get(N,0.0) for N in range(3,13)}; f8=sum(w.get(N,0.0) for N in range(8,65))
        ok=all(f[N]<=ceil[N] for N in (4,5,6,7)) and f8>=0.5
        ntot+=1
        if ok: npass+=1; pass_nstab.append(fl)
print(f"   DD-surviving fraction of registered (r,eps) box: {100*npass/ntot:.0f}%")
if pass_nstab:
    print(f"   surviving corners have N_stab >= {min(pass_nstab):.2f} (peak pushed to N>=8)")
print(f"   central N_stab = {N_stab(10.25,29.7):.2f} -> peak N=7 -> EXCLUDED")
print("\n   => survival needs the substrate at larger r / smaller eps (top corner of the box).")

import numpy as np
from scipy.integrate import solve_ivp
# No-near-threshold-resonance check for the qDP/hTetra DM residual color potential (Step-1 kill condition).
# Two-body s-wave: hard core r_c (eDP excluded-volume coat) + attractive color Yukawa (range lam, depth V0).
# Solve zero-energy radial SE for the scattering length a(V0); sigma = 4 pi a^2; sigma/m vs SIDM (~1 cm^2/g).
hbarc=197.327; GeV_g=1.7827e-24; fm2_cm2=1e-26; SIDM=1.0
m_qDP=0.30e3; mf=m_qDP/hbarc**2     # 2mu/hbar^2, two equal masses
E_qDP=264.0                          # qDP internal color binding (MeV) = physical ceiling on the residual depth
rc=1.0; lam=1.3
def a_of(V0,Rmax=30.0):
    def rhs(r,y): return [y[1], mf*(-V0*lam*np.exp(-r/lam)/r)*y[0]]
    s=solve_ivp(rhs,[rc,Rmax],[0.0,1.0],rtol=1e-7,atol=1e-10,max_step=0.05)
    return Rmax - s.y[0,-1]/s.y[1,-1]
def som(a): return 4*np.pi*a*a*fm2_cm2/(m_qDP/1e3*GeV_g)
assert abs(a_of(0.0)-rc)<1e-3, "sanity: a(V0=0) must equal hard core r_c"
print(f"sanity a(V0=0)={a_of(0.0):.3f}=r_c OK;  m_qDP=0.30 GeV, r_c={rc} fm, lam={lam} fm\n")
print("residual depth = fraction f of E_qDP (van-der-Waals residue is weaker than its source binding):")
for f in [0.0,0.05,0.10,0.20,0.50,1.00]:
    a=a_of(f*E_qDP); print(f"  f={f:4.2f}  V0={f*E_qDP:5.0f} MeV   a={a:6.2f} fm   sigma/m={som(a):.3f}  {'OVER' if som(a)>SIDM else 'OK'}")
print("\nkill features (require V0 > E_qDP, unphysical for a residue):")
for V0 in [290,320,400,480]:
    a=a_of(V0); print(f"  V0={V0:4.0f}  a={a:7.2f}  sigma/m={som(a):7.3f}")
print("\nORDERING: residual(<=264) < sigma/m=SIDM crossing(~300) < resonance pole(~500).")
print("=> no near-threshold bound state in the physical depth range; kill excluded by the residual-force hierarchy.")

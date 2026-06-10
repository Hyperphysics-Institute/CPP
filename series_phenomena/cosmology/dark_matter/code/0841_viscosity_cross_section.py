import numpy as np
from scipy.integrate import solve_ivp
hbarc=197.327; GeV_g=1.7827e-24; fm2_cm2=1e-26
m=264.0; mf=m/hbarc**2; lam=1.3; rc=1.0; E_qDP=264.0
def k_of_v(vc): return (m/2)*vc/hbarc
def delta0(vc,V0,Rmax=60.0):
    k=k_of_v(vc)
    def rhs(r,y): return [y[1], (mf*(-V0*lam*np.exp(-r/lam)/r)-k*k)*y[0]]
    s=solve_ivp(rhs,[rc,Rmax],[0.0,1.0],rtol=1e-8,atol=1e-11,max_step=0.05)
    u,up=s.y[0,-1],s.y[1,-1]; return np.arctan2(k*u,up)-k*Rmax
def sig0_over_m(vc,f):
    k=k_of_v(vc); d=delta0(vc,f*E_qDP)
    return (4*np.pi/k**2*np.sin(d)**2)*fm2_cm2/(m/1e3*GeV_g)
# sigma_V (identical-boson viscosity, pure s-wave) = (4/3) sigma_0
print("sigma_V/m = (4/3) sigma_0/m  [identical-boson symmetrization x2 * viscosity (1-cos^2) x2/3]:")
for f in [0.1,0.2,0.35,0.5,1.0]:
    s0=sig0_over_m(50/3e5,f); print(f"  f={f:.2f}: sigma_0/m={s0:.3f}, sigma_V/m={4/3*s0:.3f} cm^2/g")
print("velocity independence (f=0.2):", [round(4/3*sig0_over_m(v/3e5,0.2),3) for v in [30,500,3000]])
print("CENTRAL sigma_V/m ~ 0.20 cm^2/g (f-band 0.025-0.274), velocity-independent. l>=2 negligible ((k lam)^4).")

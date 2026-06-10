import numpy as np
from scipy.optimize import minimize_scalar, brentq
# Energetic EoS for the qDP/hTetra medium from the SAME residual color potential (0831):
#   E/N(rho) = kinetic + (z/2) * nearest-neighbor residual attraction.
# Two kinetic brackets straddle the many-body truth:
#   cell  : localized in free spacing L=d-rc  -> high kinetic (solid-like, UPPER bound)
#   fermi : (3/5)E_F free Fermi gas           -> low kinetic (delocalized, LOWER bound; most bindable)
hbarc=197.327; rc=1.0; lam=1.3; z=12; E_qDP=264.0
def minEN_cell(f,m):
    V0=f*E_qDP
    def g(rho):
        d=rho**(-1/3); L=d-rc
        if L<=0: return 1e9
        return hbarc**2*np.pi**2/(2*m*L**2)+0.5*z*(-V0*lam*np.exp(-d/lam)/d)
    return minimize_scalar(g,bounds=(0.02,0.99),method='bounded').fun
def minEN_fermi(f,m):
    V0=f*E_qDP
    def g(rho):
        d=rho**(-1/3)
        if d<=rc: return 1e9
        return 0.6*hbarc**2/(2*m)*(3*np.pi**2*rho)**(2/3)+0.5*z*(-V0*lam*np.exp(-d/lam)/d)
    return minimize_scalar(g,bounds=(0.02,0.99),method='bounded').fun
print("min E/N over rho vs residual depth fraction f (m_qDP=0.30 GeV, r_c=1.0, lam=1.3, z=12):")
print(f"{'f':>6}{'V0':>6}{'minE/N_cell':>13}{'minE/N_fermi':>14}  verdict")
for f in [0.05,0.10,0.20,0.35,0.50,0.75,1.00]:
    ec,ef=minEN_cell(f,300.0),minEN_fermi(f,300.0)
    v="DIFFUSE (both>0)" if (ec>0 and ef>0) else ("bracket-split" if ec>0 else "bound")
    print(f"{f:6.2f}{f*E_qDP:6.0f}{ec:13.1f}{ef:14.1f}  {v}")
fc=brentq(lambda f: minEN_fermi(f,300.0),0.05,1.5)
print(f"\nself-binding threshold (Fermi bracket): f_crit={fc:.2f} (V0={fc*E_qDP:.0f} MeV); physical ceiling f<=1; realistic f~0.05-0.2")
print("=> at realistic f, DIFFUSE in BOTH brackets (no self-bound saturation, no nuggets, no glueball-collapse);")
print("   residual-force hierarchy (residual<E_qDP) keeps medium below self-binding threshold AND off the 0831 resonance.")

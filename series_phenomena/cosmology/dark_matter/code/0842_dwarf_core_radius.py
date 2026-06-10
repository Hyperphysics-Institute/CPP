import numpy as np
from scipy.optimize import brentq
g_per_Msun=1.989e33; cm_per_pc=3.086e18; pc3_per_cm3=1/cm_per_pc**3
def rho1_Msun_pc3(som,v_kms,t_Gyr):     # one-scatter density: core forms where rho_NFW > rho_1
    v=v_kms*1e5; t=t_Gyr*3.156e16
    return (1.0/(som*v*t))/g_per_Msun/pc3_per_cm3
def nfw(r_kpc,rho_s,r_s): x=r_kpc/r_s; return rho_s/(x*(1+x)**2)
def r_core(rho_s,r_s,rho_1):
    try: return brentq(lambda r: nfw(r,rho_s,r_s)-rho_1,1e-3,10*r_s)
    except Exception: return None
print("rho_1 = 1/[(sigma_V/m) v t], t=10 Gyr:")
for v,n in [(30,"dwarf"),(200,"galaxy"),(1500,"cluster")]:
    print(f"  {n:8s} v={v:4d}: CPP(0.2)={rho1_Msun_pc3(0.2,v,10):.4f}  strongSIDM(1.0)={rho1_Msun_pc3(1.0,v,10):.4f} Msun/pc^3")
rho_s,r_s=0.02,1.5
print(f"\nrepresentative dwarf NFW (rho_s={rho_s}, r_s={r_s} kpc):")
for som,l in [(0.2,"CPP 0.20"),(1.0,"strong SIDM 1.0")]:
    print(f"  {l:16s}: r_core={r_core(rho_s,r_s,rho1_Msun_pc3(som,30,10)):.2f} kpc")
print("velocity-independent: same sigma_V/m=0.2 at all v -> mild cores at every scale (cannot make dwarf-large/cluster-small).")

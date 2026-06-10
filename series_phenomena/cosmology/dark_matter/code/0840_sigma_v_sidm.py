import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
hbarc=197.327; GeV_g=1.7827e-24; fm2_cm2=1e-26
m=264.0; mf=m/hbarc**2; lam=1.3; rc=1.0; E_qDP=264.0
def k_of_v(vc): return (m/2)*vc/hbarc
def delta0(vc,V0,Rmax=60.0):
    k=k_of_v(vc)
    def rhs(r,y): return [y[1], (mf*(-V0*lam*np.exp(-r/lam)/r)-k*k)*y[0]]
    s=solve_ivp(rhs,[rc,Rmax],[0.0,1.0],rtol=1e-8,atol=1e-11,max_step=0.05)
    u,up=s.y[0,-1],s.y[1,-1]; return np.arctan2(k*u,up)-k*Rmax
def som(vc,f,boson=False):
    k=k_of_v(vc); d=delta0(vc,f*E_qDP)
    pref=8 if boson else 4
    return (pref*np.pi/k**2*np.sin(d)**2)*fm2_cm2/(m/1e3*GeV_g)
v=np.logspace(1,3.7,40); vc=v/3e5
# CPP flat band (distinguishable s-wave): f=0.1 (upper) .. f=0.5 (lower Ramsauer); central f=0.2
hi=[som(x,0.1) for x in vc]; ce=[som(x,0.2) for x in vc]; lo=[som(x,0.5) for x in vc]
bos=[som(x,0.2,boson=True) for x in vc]
fig,ax=plt.subplots(figsize=(7.2,5.0))
ax.fill_between(v,lo,hi,color="#3b6fb0",alpha=0.18,label="CPP band (f=0.1–0.5, s-wave)")
ax.plot(v,ce,color="#1f4e8c",lw=2.2,label="CPP central (f≈0.2): σ/m≈0.15, flat")
ax.plot(v,bos,color="#1f4e8c",lw=1.2,ls="--",label="CPP central, identical-boson ×2 (≈0.3)")
# SIDM observational regions (approximate, literature)
ax.axvspan(20,60,color="#cfe8cf",alpha=0.5); ax.text(33,7,"dwarfs",fontsize=8,ha="center")
ax.axvspan(1000,2200,color="#f0d0d0",alpha=0.5); ax.text(1480,7,"clusters",fontsize=8,ha="center")
ax.fill_between([20,60],[0.5,0.5],[30,30],color="#2e8b57",alpha=0.13)
ax.text(34,1.4,"cores\nfavored",fontsize=7.5,ha="center",color="#2e7d32")
ax.fill_between([1000,2200],[1,1],[30,30],color="#b22222",alpha=0.12)
ax.text(1480,3.2,"excluded",fontsize=7.5,ha="center",color="#a01818")
ax.axhline(0.1,color="gray",ls=":",lw=0.8); ax.text(11,0.105,"coring threshold ~0.1",fontsize=7,color="gray")
ax.set_xscale("log"); ax.set_yscale("log"); ax.set_xlim(10,5000); ax.set_ylim(0.01,30)
ax.set_xlabel("relative velocity  v  [km/s]"); ax.set_ylabel(r"$\sigma/m$  [cm$^2$/g]")
ax.set_title("CPP qDP/hTetra self-interaction vs SIDM constraints (first-pass)")
ax.legend(fontsize=7.5,loc="lower left"); ax.grid(alpha=0.25,which="both",lw=0.4)
plt.tight_layout(); plt.savefig("series_phenomena/cosmology/dark_matter/figures/0840_sigma_over_m_velocity.png",dpi=150)
print("figure saved")
print(f"central f=0.2: sigma/m = {ce[0]:.3f} (dwarf) ... {ce[-1]:.3f} (cluster) -> FLAT")
print(f"boson x2 central: {bos[0]:.3f} flat;  f-band at fixed v: {lo[0]:.3f}-{hi[0]:.3f}")

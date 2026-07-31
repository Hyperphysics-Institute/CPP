import numpy as np
from wake_sign import axial_drive

print("ROBUSTNESS: does the drag sign survive geometry/cutoff variation?")
print(f"{'bmin':>6} {'bmax':>6} {'smax':>6} | {'eps=0.15':>12} {'eps=1.0':>12}")
print("-"*52)
for bmin,bmax,smax in [(0.5,8,60),(1.0,8,60),(2.0,8,60),(1.0,4,60),
                       (1.0,16,60),(1.0,8,120),(0.25,20,120)]:
    f1=axial_drive(0.15,bmin=bmin,bmax=bmax,smax=smax)
    f2=axial_drive(1.0, bmin=bmin,bmax=bmax,smax=smax)
    print(f"{bmin:6.2f} {bmax:6.1f} {smax:6.0f} | {f1:12.4e} {f2:12.4e}")

# How much directional (non-linear-response) forward impulse would be needed?
# Add: during DISCHARGE (|p| decreasing), a fraction eta of the arc's stored
# polarization delivers a purely axial FORWARD impulse to the CP.
def with_directional(eps, eta, v=1.0, bmin=1.0, bmax=8.0, nb=140,
                     smax=60.0, ns=6000):
    tau=eps/v; s=np.linspace(smax,-smax,ns); ds=s[0]-s[1]; dt=ds/v
    b=np.linspace(bmin,bmax,nb); w=2*np.pi*b*(b[1]-b[0])
    px=np.zeros(nb); pb=np.zeros(nb); F=0.0
    for sx in s:
        r2=sx**2+b**2; r=np.sqrt(r2); rx,rb=sx/r,b/r
        Ex,Eb=rx/r2,rb/r2
        a=np.exp(-dt/tau) if tau>0 else 0.0
        pmag_old=np.sqrt(px**2+pb**2)
        px=Ex+(px-Ex)*a; pb=Eb+(pb-Eb)*a
        pmag_new=np.sqrt(px**2+pb**2)
        disch=np.maximum(pmag_old-pmag_new,0.0)      # amount discharged
        pdotr=px*rx+pb*rb
        fx=(3*pdotr*rx-px)/r**3
        F+=np.sum((fx + eta*disch/r**3)*w)*ds
    return F

print("\nDIRECTIONAL-DISCHARGE REQUIREMENT (eps=0.15):")
print(f"{'eta':>8} | {'net axial':>13} | sign")
for eta in [0.0,0.5,1.0,2.0,5.0,10.0,20.0]:
    F=with_directional(0.15,eta)
    print(f"{eta:8.2f} | {F:13.4e} | {'FORWARD' if F>0 else 'backward'}")
lo,hi=0.0,50.0
if with_directional(0.15,hi)>0:
    for _ in range(50):
        m=0.5*(lo+hi)
        if with_directional(0.15,m)>0: hi=m
        else: lo=m
    print(f"\n  -> forward requires eta_crit ~ {0.5*(lo+hi):.3f}")

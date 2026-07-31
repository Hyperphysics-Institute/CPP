"""B1 -- LINEAR STABILITY OF THE COASTING SOLUTION.
Is the round-trip drive EXACTLY linear in v?  Newton I requires it.
Convergence-tested: the 0.2% curvature seen at 2884 is either physics or grid error."""
import numpy as np

def outbound(yx,yp,v,c=1.0):
    y=np.hypot(yx,yp); t2=-y/c; A=yx-v*t2
    disc=A*A*v*v+(c*c-v*v)*(A*A+yp*yp)
    return c*(A*v+np.sqrt(disc))/(c*c-v*v)

def drive(v,m=2.0,rmin=1.0,rmax=12.0,nr=160,nth=240,c=1.0):
    r=np.linspace(rmin,rmax,nr); th=np.linspace(0,np.pi,nth)
    R,TH=np.meshgrid(r,th,indexing='ij')
    yx,yp=R*np.cos(TH),R*np.sin(TH)
    w=(R**2)*np.sin(TH)*(r[1]-r[0])*(th[1]-th[0])*2*np.pi
    amp=1.0/outbound(yx,yp,v,c)**2
    return float(np.sum((amp/R**m)*(yx/R)*w))

print("CONVERGENCE: is the curvature in drive/beta real, or grid error?")
print(f"{'grid':>14} " + " ".join(f"{b:>11}" for b in (0.01,0.02,0.05,0.10,0.20)))
print("-"*76)
rows={}
for nr,nth,lab in ((160,240,"160x240 (2884)"),(320,480,"320x480"),(640,960,"640x960")):
    vals=[drive(b,nr=nr,nth=nth)/b for b in (0.01,0.02,0.05,0.10,0.20)]
    rows[lab]=vals
    print(f"{lab:>14} " + " ".join(f"{x:11.5f}" for x in vals))

print("\nfractional spread of drive/beta across beta (0.01 -> 0.20):")
for lab,v in rows.items():
    print(f"  {lab:>14}: {abs(v[-1]-v[0])/abs(v[0]):.5f}")

print("\nRichardson check at fixed beta=0.10 (grid -> infinity):")
for b in (0.01,0.10,0.20):
    a=drive(b,nr=160,nth=240)/b; c_=drive(b,nr=320,nth=480)/b; d=drive(b,nr=640,nth=960)/b
    print(f"  beta={b:4.2f}:  {a:11.5f} -> {c_:11.5f} -> {d:11.5f}   "
          f"deltas {c_-a:+.5f}, {d-c_:+.5f}")

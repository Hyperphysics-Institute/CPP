"""Does SSV_abs carry the SAME beta^2 curvature as the drive?
   If SSV_abs = S0(1 - c beta^2) with c = 0.201, then mu = PSR/SSV_abs
   inherits exactly the growth B1 requires and Newton I holds with NO new physics."""
import numpy as np
def outbound(yx,yp,v,c=1.0):
    y=np.hypot(yx,yp); t2=-y/c; A=yx-v*t2
    return c*(A*v+np.sqrt(A*A*v*v+(c*c-v*v)*(A*A+yp*yp)))/(c*c-v*v)

def integrals(v,m=2.0,rmin=1.0,rmax=12.0,nr=320,nth=480):
    r=np.linspace(rmin,rmax,nr); th=np.linspace(0,np.pi,nth)
    R,TH=np.meshgrid(r,th,indexing='ij'); yx,yp=R*np.cos(TH),R*np.sin(TH)
    w=(R**2)*np.sin(TH)*(r[1]-r[0])*(th[1]-th[0])*2*np.pi
    amp=1.0/outbound(yx,yp,v)**2
    f=amp/R**m
    D=float(np.sum(f*(yx/R)*w))          # axial vector sum  -> the drive
    S=float(np.sum(np.abs(f)*w))         # magnitude sum     -> SSV_abs
    return D,S

print("Does SSV_abs carry the same beta^2 curvature as the drive?")
print(f"{'beta':>6} {'D/beta':>12} {'SSV_abs':>14} {'S(b)/S(0)':>12} {'implied c_S':>12}")
print("-"*62)
D0,S0=integrals(1e-6)
for b in (0.05,0.10,0.15,0.20):
    D,S=integrals(b)
    ratio=S/S0; cS=(1-ratio)/b**2
    print(f"{b:6.2f} {D/b:12.5f} {S:14.6f} {ratio:12.7f} {cS:12.5f}")

print(f"\n  drive curvature   c_D = 0.20129  (B1, model-independent)")
print("  if c_S == c_D then mu = PSR/SSV_abs cancels it EXACTLY and Newton I holds")
print("\nDIRECT TEST -- is D/(beta * SSV_abs) constant in beta?")
print(f"{'beta':>6} {'D/(beta*S)':>16} {'frac dev from b->0':>20}")
base=None
for b in (0.01,0.05,0.10,0.15,0.20):
    D,S=integrals(b); q=D/(b*S)
    if base is None: base=q
    print(f"{b:6.2f} {q:16.8f} {abs(q-base)/abs(base):20.3e}")

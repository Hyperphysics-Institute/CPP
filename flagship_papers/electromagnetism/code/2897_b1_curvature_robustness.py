"""Is the beta^2 curvature coefficient ROBUST, or an artifact of integration range?
   Newton I requires mu(v)*D(v) = v exactly.  D = k v (1 - c v^2) forces
   mu(v) = 1/(k(1-c v^2)).  Compare c against the relativistic gamma^2 = 1+beta^2."""
import numpy as np
def outbound(yx,yp,v,c=1.0):
    y=np.hypot(yx,yp); t2=-y/c; A=yx-v*t2
    return c*(A*v+np.sqrt(A*A*v*v+(c*c-v*v)*(A*A+yp*yp)))/(c*c-v*v)
def drive(v,m,rmin,rmax,nr=320,nth=480):
    r=np.linspace(rmin,rmax,nr); th=np.linspace(0,np.pi,nth)
    R,TH=np.meshgrid(r,th,indexing='ij'); yx,yp=R*np.cos(TH),R*np.sin(TH)
    w=(R**2)*np.sin(TH)*(r[1]-r[0])*(th[1]-th[0])*2*np.pi
    return float(np.sum((1.0/outbound(yx,yp,v)**2/R**m)*(yx/R)*w))
def curvature(m,rmin,rmax):
    """fit D/beta = k(1 - c beta^2) over small beta"""
    bs=np.array([0.05,0.10,0.15,0.20]); y=np.array([drive(b,m,rmin,rmax)/b for b in bs])
    k=y[0]/(1-0*bs[0]); # first estimate
    # least squares on y = k - k c beta^2
    A=np.vstack([np.ones_like(bs),-bs**2]).T
    coef,*_=np.linalg.lstsq(A,y,rcond=None)
    k=coef[0]; c=coef[1]/k
    return k,c
print("Is c (the beta^2 coefficient) robust across model choices?")
print(f"{'m':>4} {'rmin':>6} {'rmax':>6} {'k':>11} {'c':>9}")
print("-"*44)
for m,rmin,rmax in ((2.0,1,12),(2.0,1,20),(2.0,2,12),(2.0,0.5,12),
                    (1.0,1,12),(3.0,1,12)):
    k,c=curvature(m,rmin,rmax)
    print(f"{m:4.1f} {rmin:6.1f} {rmax:6.1f} {k:11.4f} {c:9.5f}")
print("\nrelativistic reference: gamma^2 = 1/(1-beta^2)  =>  c = 1.0 exactly")
print("mu(v) must go as 1/(1 - c beta^2) for Newton I to hold at all v")

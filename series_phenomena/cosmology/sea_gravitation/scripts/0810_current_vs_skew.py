import numpy as np

# QUESTION: does a steady NESS current (broken detailed balance) necessarily produce
# an equal-time SKEW (the third moment that sources <F>_bulk = -4k^2 <d d'^2>)?
# TEST: a 2D Fokker-Planck system whose drift = -grad(V) + b, with b SOLENOIDAL.
#   V = (x^2+y^2)/2 (symmetric).  b = omega*(-y, x)  (rigid rotation; non-conservative).
# Standard result: because b . grad(V) = 0, the stationary pi ~ exp(-V) is UNCHANGED,
# yet there is a steady circulating current J = b*pi with div J = 0 and broken
# detailed balance. So: NESS current present, equal-time distribution still symmetric.

n=401; L=6.0; xs=np.linspace(-L,L,n); X,Y=np.meshgrid(xs,xs,indexing='ij'); h=xs[1]-xs[0]
D=1.0; omega=1.3
V=0.5*(X**2+Y**2)
pi=np.exp(-V); pi/=pi.sum()*h*h                      # symmetric stationary density
# drift
Ax=-X + (-omega*Y);  Ay=-Y + ( omega*X)              # -gradV + solenoidal b
def ddx(f): return np.gradient(f,h,axis=0)
def ddy(f): return np.gradient(f,h,axis=1)
# probability current J = A pi - D grad pi
Jx=Ax*pi - D*ddx(pi);  Jy=Ay*pi - D*ddy(pi)
divJ=ddx(Jx)+ddy(Jy)

print("="*64)
print("Is this a genuine NESS? (broken detailed balance)")
# circulation of the drift around a loop: nonzero => non-conservative => NESS
curlA = ddx(Ay)-ddy(Ax)
print(f"  curl(drift) center value = {curlA[n//2,n//2]:.3f}  (=2*omega={2*omega}); nonzero => NESS")
print(f"  max |steady current J| = {np.max(np.hypot(Jx,Jy)):.4f}  (nonzero => current present)")
print(f"  max |div J| (interior) = {np.max(np.abs(divJ[5:-5,5:-5])):.2e}  (~0 => stationary, div-free)")

print("="*64)
print("Equal-time moments of the stationary pi (skew diagnostics):")
def mom(fx): return np.sum(fx*pi)*h*h
print(f"  <x>   = {mom(X):+.3e}   <y>   = {mom(Y):+.3e}   (means)")
print(f"  <x^3> = {mom(X**3):+.3e}   <x y^2> = {mom(X*Y**2):+.3e}   (3rd moments)")
print(f"  <x^2 y> = {mom(X**2*Y):+.3e}  (the 2D analog of <d d'^2>-type skew)")
print("  => all odd/third moments ~ 0: the equal-time distribution is SYMMETRIC,")
print("     despite a nonzero steady circulating current.")

print("="*64)
print("CONCLUSION")
print("  A steady NESS current is div-free (stationarity) and, when it is the")
print("  pi-solenoidal type, leaves pi -- hence ALL equal-time odd moments -- UNCHANGED.")
print("  => 'broken detailed balance / O(delta^3) current' does NOT by itself imply an")
print("     equal-time skew. The DM bulk residual <d d'^2> sources from a SKEW of pi,")
print("     not from a current. Current and skew are different objects.")

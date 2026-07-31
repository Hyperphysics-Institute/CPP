"""
ROUND-TRIP TIMING ASYMMETRY -> NET AXIAL DRIVE?   (founder mechanism, 2 Aug)

CP at origin at t=0, moving +x at v. Static Sea of DPs at rest in the
absolute frame. For a response ARRIVING at the CP now:

  return leg : DP emitted at t2 = -|y|/c            (return distance = |y|)
  outbound   : CP emitted at t1 = t2 - s, where
               |y - v t1 x_hat| = c s   ->  solve the quadratic for s
               outbound distance d_out = c s

Two hypotheses for the amplitude the DP responds to:
  (A) RETARDED-DISTANCE response  : amp ~ 1/d_out^2
      (the DP responds to how far the CP WAS when it emitted)
  (B) LIENARD-WIECHERT response   : amp ~ 1/R_inst^2 with the LW angular
      factor, R_inst = separation at the INSTANT of reception
      (what a wave equation actually produces for a uniformly moving source)

Force on the CP from each DP is attraction along y_hat (induced response),
magnitude ~ amp / |y|^m. Axial component summed over a symmetric Sea.
Under (B) the axial sum must vanish; under (A) it need not.
"""
import numpy as np

def outbound_distance(yx, yp, v, c=1.0):
    """Solve |y - v t1| = c(t2-t1) with t2 = -|y|/c. Returns d_out = c*s."""
    y = np.hypot(yx, yp)
    t2 = -y/c
    A = yx - v*t2                      # = yx + v*y/c
    disc = A*A*v*v + (c*c - v*v)*(A*A + yp*yp)
    s = (A*v + np.sqrt(disc))/(c*c - v*v)
    return c*s

def axial_drive(v, mode, m=2.0, c=1.0, rmin=1.0, rmax=12.0, nr=160, nth=240):
    r  = np.linspace(rmin, rmax, nr)
    th = np.linspace(0, np.pi, nth)
    R, TH = np.meshgrid(r, th, indexing='ij')
    yx, yp = R*np.cos(TH), R*np.sin(TH)
    w = (R**2)*np.sin(TH)*(r[1]-r[0])*(th[1]-th[0])*2*np.pi   # volume element

    if mode == 'A':                                  # retarded-distance response
        amp = 1.0/outbound_distance(yx, yp, v, c)**2
    else:                                            # Lienard-Wiechert
        g2 = 1.0 - (v/c)**2
        sin2 = (yp/R)**2
        amp = g2/((1.0 - (v/c)**2*sin2)**1.5 * R**2)

    fmag = amp/R**m
    return float(np.sum(fmag*(yx/R)*w))              # axial component

print(f"{'beta':>7} | {'(A) retarded-dist':>19} | {'(B) Lienard-Wiechert':>21}")
print("-"*56)
for beta in [0.0, 0.01, 0.05, 0.1, 0.2, 0.4]:
    a = axial_drive(beta,'A'); b = axial_drive(beta,'B')
    print(f"{beta:7.3f} | {a:19.6e} | {b:21.6e}")

print("\nlinearity of (A) in beta (divide by beta):")
for beta in [0.01,0.02,0.05,0.1]:
    print(f"  beta={beta:5.3f}  drive/beta = {axial_drive(beta,'A')/beta: .6e}")

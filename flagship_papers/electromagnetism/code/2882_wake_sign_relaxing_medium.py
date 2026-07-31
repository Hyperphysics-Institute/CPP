"""
SIGN OF THE AXIAL WAKE DRIVE ON A UNIFORMLY MOVING CHARGE
through a sea of relaxing polarizable arcs.

Founder mechanism (Thomas, 2026-08): arcs ahead of the Position Plane are
charging; arcs behind are discharging; an arc just past the plane retains
its FORE-configuration polarization, whose + pole then faces the CP,
giving REPULSION = forward push. Question: does that stale-region forward
push beat the equilibrated far-rear backward pull?

Model (deliberately minimal, no CPP-specific assumptions):
  - unit positive charge at x = 0 in its own frame; medium streams past at -v
  - polarizable points on a cylindrical grid (axial s, radial b)
  - each carries vector polarization p with linear relaxation
        dp/dt = (chi*E(r) - p)/tau
    where E is the instantaneous Coulomb field of the charge
  - force on the charge from a dipole p at relative position r:
        F = [3(p.rhat)rhat - p]/r^3
  - report the AXIAL component summed over the medium, steady state.

The only free ratio is eps = v*tau/d, the lag distance in units of the
interaction scale -- i.e. eps_mem. We sweep it.
"""
import numpy as np

def axial_drive(eps, v=1.0, chi=1.0, bmin=1.0, bmax=8.0, nb=140,
                smax=60.0, ns=6000):
    """Steady-state axial force on the charge. eps = v*tau (d=1)."""
    tau = eps / v if v > 0 else 0.0
    s = np.linspace(smax, -smax, ns)          # stream from ahead to behind
    ds = s[0] - s[1]
    dt = ds / v
    b = np.linspace(bmin, bmax, nb)
    # weight: cylindrical shell volume element 2*pi*b*db
    w = 2*np.pi*b*(b[1]-b[0])

    px = np.zeros(nb); pb = np.zeros(nb)      # polarization components
    Fax = 0.0
    for k in range(ns):
        sx = s[k]
        r2 = sx**2 + b**2
        r = np.sqrt(r2)
        rx, rb = sx/r, b/r                    # unit vector charge -> point
        Ex, Eb = chi*rx/r2, chi*rb/r2         # Coulomb field at the point

        if tau > 0:                           # exponential relaxation step
            a = np.exp(-dt/tau)
            px = Ex + (px - Ex)*a
            pb = Eb + (pb - Eb)*a
        else:
            px, pb = Ex, Eb                   # instantaneous limit

        pdotr = px*rx + pb*rb
        fx = (3*pdotr*rx - px)/r**3           # axial force on the charge
        Fax += np.sum(fx*w)*ds
    return Fax

print(f"{'eps = v*tau/d':>14} | {'axial drive':>14} | sign")
print("-"*46)
rows=[]
for eps in [0.0, 0.02, 0.05, 0.1, 0.15, 0.2, 0.3, 0.5, 0.8, 1.2, 2.0, 4.0, 8.0]:
    F = axial_drive(eps)
    rows.append((eps,F))
    sign = "FORWARD (+)" if F > 1e-12 else ("backward (-)" if F < -1e-12 else "zero")
    print(f"{eps:14.3f} | {F:14.6e} | {sign}")

# locate any sign change
print("\nsign changes:")
found=False
for (e1,f1),(e2,f2) in zip(rows,rows[1:]):
    if f1*f2 < 0:
        found=True
        lo,hi=e1,e2
        for _ in range(60):
            mid=0.5*(lo+hi)
            if axial_drive(mid)*f1 < 0: hi=mid
            else: lo=mid
        print(f"  crossover between eps={e1} and {e2}  ->  eps_crit = {0.5*(lo+hi):.5f}")
if not found: print("  none in range")

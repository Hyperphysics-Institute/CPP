import numpy as np
# N_stab = c * r / eps  (kT-cancelled substrate number; 2382 sec2)
# Registered constituents (2381 rung-bond primitives):
c_SY, c_rigid = 14.054, 2*np.pi**2      # bending stiffness: fluctuation-corrected vs rigid
r_lo, r_hi = 8.5, 12.0                   # r = l_p/l_rung, ring kinetic placement (2383)
eps_lo, eps_hi = 23.2, 36.2              # eps = E_bond/kT_form, D1 band
THRESH = 6.2                             # DD-survival threshold (2421): N>=8-dominant, N<8 suppressed

def nstab(c,r,eps): return c*r/eps
def band(c):
    lo = nstab(c, r_lo, eps_hi); hi = nstab(c, r_hi, eps_lo)
    cen = nstab(c, (r_lo+r_hi)/2, (eps_lo+eps_hi)/2)
    return lo, cen, hi

print(f"c_rigid = 2*pi^2 = {c_rigid:.3f}   (ratio SY/rigid = {c_SY/c_rigid:.3f})\n")
print(f"DD-survival threshold: N_stab >= {THRESH}\n")
for name,c in [("SY (fluctuation-corrected)",c_SY),("rigid (2pi^2)",c_rigid)]:
    lo,cen,hi = band(c)
    verdict = "CLEARS" if cen>=THRESH else "FAILS (central below threshold)"
    print(f"{name}:  c={c:.3f}")
    print(f"   N_stab range [{lo:.2f}, {hi:.2f}]   central {cen:.2f}   -> central {verdict}")
    # what corner is needed to clear?
    if cen < THRESH:
        # solve r for N_stab=THRESH at eps central and eps_lo
        eps_c=(eps_lo+eps_hi)/2
        r_need_epsC = THRESH*eps_c/c; r_need_epsLo = THRESH*eps_lo/c
        print(f"   to reach {THRESH}: need r>= {r_need_epsC:.1f} (eps central) or r>= {r_need_epsLo:.1f} (eps low {eps_lo})")
        eps_at_rhi = c*r_hi/THRESH
        print(f"   at r=r_hi={r_hi}: need eps<= {eps_at_rhi:.1f} (lower {'third' if eps_at_rhi<28 else 'half'} of [23.2,36.2])")
    print()

# fraction of the (r,eps) box that clears, per coefficient
for name,c in [("SY",c_SY),("rigid",c_rigid)]:
    rr=np.linspace(r_lo,r_hi,200); ee=np.linspace(eps_lo,eps_hi,200)
    R,E=np.meshgrid(rr,ee); frac=(c*R/E>=THRESH).mean()
    print(f"{name}: fraction of registered (r,eps) box with N_stab>={THRESH}: {frac*100:.0f}%")

print("\n" + "="*66)
print("VERDICT")
print("="*66)
print(f"Central N_stab: SY {band(c_SY)[1]:.2f} (FAILS 6.2) | rigid {band(c_rigid)[1]:.2f} (clears 6.2)")
print("The candidate's fate hinges on the bending coefficient. For ACTIVATED ring")
print("pop-open (a thermal-fluctuation escape), the fluctuation-corrected SY value")
print("(14.054) is the physically appropriate one -> central N_stab ~ 4.8 < 6.2:")
print("formation floor at N~5, population N=5-7, which DD EXCLUDES. Survives only in")
print("the r-high/eps-low corner, or if the rigid 2pi^2 coefficient governs stability.")

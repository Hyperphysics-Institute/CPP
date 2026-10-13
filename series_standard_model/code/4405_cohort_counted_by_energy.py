"""Patch 4405 -- founder (on 4404): a body at rest starts falling at the first Moment (the gradient acts on each CP
directly); heavy and light fall alike because every CP gets the same grad SSV_abs; the mass is the stationary CPs
(central unpaired CP, cage CPs, polarized DP cloud) plus the moving CPs (orbital DP, linear oscillator); its stored KE
is exactly proportional to the CP cohort enrolled in the mass.

Part 1  'the same increase' for every CP: added to velocities with the one-PSR cap, the body's gain depends on its
        mix of fast and slow CPs; as a momentum gain proportional to each CP's energy, every body gains the same.
Part 2  the stored KE is (1/2) M v^2 with M the body's inertia.  Measured inertia is the body's energy / c^2:
          nuclear binding: Ti-48 and Pt-195 differ in mass per nucleon by ~0.09% (mass spectrometry);
          a closed system's momentum is (E/c^2) V, so faster-moving internal CPs count more than slow ones;
          a warmed ball is heavier by its heat / c^2.
        So "proportional to the cohort" holds if the cohort is counted by energy, not by number.
Part 3  the pull a body exerts (active mass, the SSV_abs it sources) must equal the inertia that stores its KE, or an
        Earth-ball pair would not conserve momentum: lunar laser ranging (Al vs Fe in the Moon) bounds the difference
        at ~4e-12 (Bartlett and van Buren 1986).
"""
u = 1.66053907e-27; c = 2.998e8
import numpy as np
print("Part 1: 'the same increase' for slow and near-cap CPs (cap: one PSR per Moment, speed < 1)")
rng = np.random.default_rng(0)
def body(frac_fast, n=200000, w=0.999):
    nf = int(n*frac_fast)
    d = rng.normal(size=(n, 3)); d /= np.linalg.norm(d, axis=1)[:, None]
    sp = np.where(np.arange(n) < nf, w, 1e-3)
    return d*sp[:, None]
def com_velocity(v):                      # centre-of-energy velocity: sum p / sum E (relativistic, c = 1)
    g = 1/np.sqrt(1 - np.sum(v*v, axis=1)); return (g[:, None]*v).sum(0)/g.sum()
dv = np.array([0, 0, 1e-4])
for name, f in (("material A (30% near-cap)", 0.3), ("material B (60% near-cap)", 0.6)):
    v = body(f); V0 = com_velocity(v)
    # (a) add dv to each CP's velocity, then clip speeds at the cap
    va = v + dv; s_ = np.linalg.norm(va, axis=1); va = va*np.minimum(1, 0.999/s_)[:, None]   # near-cap CPs cannot exceed the cap speed
    # (b) give each CP a momentum gain proportional to its energy: p_i += E_i dv
    g = 1/np.sqrt(1 - np.sum(v*v, axis=1)); p = g[:, None]*v + g[:, None]*dv
    E = np.sqrt(1 + np.sum(p*p, axis=1)); vb = p/E[:, None]
    print(f"  {name}: (a) velocity added, capped: body gains {(com_velocity(va)-V0)[2]/1e-4:.4f} dv;"
          f"  (b) momentum gain ~ energy: {(com_velocity(vb)-V0)[2]/1e-4:.4f} dv")
print("  -> only (b) gives every body the same gain whatever its mix of fast and slow CPs")

print("\nPart 2: what the body's inertia is")
for k, (A, m) in {"Ti-48": (48, 47.9479463), "Pt-195": (195, 194.9647911)}.items():
    print(f"  {k}: mass per nucleon {m/A:.6f} u")
d = (194.9647911/195)/(47.9479463/48) - 1
print(f"  difference per nucleon: {d*100:.3f}%  (atomic masses: ~0.087% from binding, ~0.005% from the neutron/proton mix)")
dE = 450*100      # J per kg, iron warmed by 100 K
print(f"  1 kg of iron warmed by 100 K: heavier by {dE/c**2:.1e} kg (its heat / c^2): more internal motion, more inertia")
print("  closed system: total momentum P = (E/c^2) V exactly -> each part counts by its energy, not by its number")

print("\nPart 3: action and reaction")
print("  the Earth pulls the ball with G M_E m_passive / r^2; the ball pulls the Earth with G M_E m_active / r^2;")
print("  momentum is conserved only if m_active/m_passive is the same for every material (LLR: Al vs Fe, ~4e-12);")
print("  with equal fall (passive = inertial) that makes active = inertial")

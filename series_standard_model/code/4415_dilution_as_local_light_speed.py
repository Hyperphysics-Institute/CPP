"""Patch 4415 -- the founder (on 4414): no DI-bits 'come back'; every GP emits the same number each Moment (AP-4); the CP is
moved by the totality at its GP; the front-back differential comes from the DP-arcs and separation; where there are more
fields mu-epsilon is higher, light is slower in absolute space, and the CP moves more slowly, losing nothing, and speeds up
again on leaving.

Part 1. Two readings on a path through a region where mu-epsilon is raised by K = 1.25:
  (F) feedback (4414's dilution): each Moment's step is rebuilt from the previous one times the CP's share s < 1 of the
      total; the speed decays everywhere and faster inside;
  (P) persistent organization (Claude's rendering of his answer): step = f x (local light speed c/K), with f held in the
      sea's DP organization and changed only by forces; the speed tracks light down and back up.
Part 2. Local measurement under WC-DP-SEA-PV (rulers and clocks K^-1/2): (P) reads the same local speed everywhere.
Part 3. What GR adds: for a body crossing a static well, energy conservation gamma_loc*sqrt(g00) = const raises the local
        speed inside. (P) alone keeps it fixed, so 4403's limb-difference acceleration must supply exactly that change,
        and it must undo it on the way out.
Part 4. Static-field constraint: QED index shifts in a 1 T field and the PVLAS bound, against the gravitating share of
        the field's energy.
"""
import numpy as np

# Part 1 -- 4414's dilution modelled faithfully: the step is rebuilt from the last step times the CP's share s of the total,
# with s < 1 everywhere (other sources always contribute) and s lower inside the field region.
n = 300
K = np.ones(n); K[100:200] = 1.25
c_loc = 1/K
f = 0.4
s_out, s_in = 0.999, 0.999/1.25          # illustrative shares; any s < 1 decays geometrically
vF = np.empty(n); vF[0] = f
for k in range(1, n):
    vF[k] = (s_in if K[k] > 1 else s_out)*vF[k-1]
vP = f*c_loc                              # Claude's rendering of his answer: step = f x local light speed, f held by the sea
print("Part 1 (absolute-frame speeds, light = 1 outside; feedback = 4414's iterated, normalized step):")
for k in (50, 99, 101, 150, 250):
    print(f"  Moment {k:3d}: K {K[k]:.2f}  light {c_loc[k]:.3f}  feedback {vF[k]:.3e}  persistent {vP[k]:.3f}"
          f"  persistent/light {vP[k]/c_loc[k]:.3f}")
print("  feedback decays even outside (s = 0.999) and collapses inside; the persistent rule has neither the background")
print("  decay nor the entry loss: it slows with light inside and recovers on exit.")

# Part 2
print("Part 2 (local measurement, rulers and clocks K^-1/2): coordinate speed x K =")
for k in (50, 150, 250):
    print(f"  Moment {k:3d}: local speed {vP[k]*K[k]:.3f}")

# Part 3
print("Part 3 (a body crossing a static well, GR / PV energy conservation, depth U = GM/(rc^2)):")
for v0 in (0.1, 0.5):
    g0 = 1/np.sqrt(1-v0**2)
    for U in (1e-6, 1e-3, 0.05):
        sqrt_g00 = 1/np.sqrt(np.exp(2*U))   # PV: g00 = 1/K, K = e^{2U}
        g_in = g0/sqrt_g00
        v_in = np.sqrt(1-1/g_in**2)
        print(f"  v_out {v0:.1f}  U {U:.0e}: local speed inside {v_in:.6f}  (persistent rule alone: {v0:.6f};"
              f" the gradient must add {v_in-v0:+.2e})")

# Part 4
A_e = 1.32e-24   # T^-2, Euler-Heisenberg
B = 1.0
print("Part 4 (static magnetic field, B = 1 T):")
print(f"  QED index shifts: n_par - 1 = {7*A_e*B**2:.1e}, n_perp - 1 = {4*A_e*B**2:.1e}; birefringence {3*A_e*B**2:.1e}")
print("  PVLAS final (Ejlli et al. 2020): delta n / B^2 = (19 +/- 27)e-24 per T^2 -- consistent with zero, ~5-10x above QED")
rho = B**2/(2*4e-7*np.pi)/(3e8)**2
U = 6.674e-11*rho*1.0**2/(3e8)**2          # potential scale over ~1 m of such energy density
print(f"  the field's energy as mass density: {rho:.1e} kg/m^3; its potential over ~1 m: U ~ {U:.0e}")
print("  a field's payloads raise SSV_abs linearly in |E| or |B|; if mu-epsilon tracked SSV_abs, light would slow")
print("  measurably in a magnet or capacitor. It does not, so mu-epsilon must track only the gravitating (G-weighted) part.")

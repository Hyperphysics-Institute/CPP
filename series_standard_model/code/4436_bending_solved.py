"""Patch 4436 -- founder: realness is mass (the amount of realness is the amount of mass effect), resolving equal fall; is the
bending of light and of fast electrons now solved?

Ingredients already on record:
  * WC-DP-SEA-PV (4392): near a mass the local light speed is c/K, K = 1 + 2U (U = GM/(r c^2)).
  * 4415 (Claude's rendering of his answer): a CP's step is f x (local light speed), f held in the sea's organization, changed only
    by forces. So with no force, its speed is s = f c / K: it slows where K is higher, and (his limb picture, 4435 component (1)) its
    path turns toward the slower side like a refracted ray: dn/dt = s * grad_perp(ln K).
  * 4403's census push from the limb difference, here allowed a speed factor P(s): a_push = g P(s).
Algebra (c = 1, grad ln K = 2 g to first order, g the Newtonian field vector):
    u = s n:  du/dt = (ds/dt) n + s dn/dt = -(u.grad lnK) u + s^2 [grad lnK - n (n.grad lnK)]
                    = 2 s^2 g - 4 (u.g) u
    total:   a = g P(s) + 2 s^2 g - 4 (u.g) u
GR (first post-Newtonian, PPN gamma = 1):  a = g (1 + s^2) - 4 (u.g) u
=> exact agreement in every direction iff P = 1 - f^2 (= 1/gamma^2; the rest-mass fraction): the push fades as 1/gamma^2, vanishing for light.
(Part 1 uses s for f at this order; Part 3 applies P to the local fraction f.)
Part 1: the identity. Part 2: the closed form integrated (a consistency check). Part 3: the step rule itself, run independently.
"""
import numpy as np
print("Part 1 (acceleration / g for motion across and along the field):")
for s in (0.1, 0.5, 0.9, 1.0):
    for P, name in ((lambda s: 1 - s**2, "push 1 - v^2"), (lambda s: 1.0, "push constant")):
        across = P(s) + 2*s**2; along = P(s) + 2*s**2 - 4*s**2
        print(f"  v {s}: {name:13s} across {across:.3f}  along {along:+.3f}   | GR across {1 + s**2:.3f}  along {1 - 3*s**2:+.3f}")
def deflect(v0, P, GM=1e-6, b=1.0, L=4000.0, n=400000):
    x, y = -L, b; s = v0; u = np.array([v0, 0.0]); pos = np.array([x, y])
    dt = 2*L/v0/n
    for _ in range(n):
        r = np.linalg.norm(pos); g = -GM*pos/r**3
        sp = np.linalg.norm(u)
        a = g*P(sp) + 2*sp**2*g - 4*(u @ g)*u
        u = u + a*dt; pos = pos + u*dt
    return np.arctan2(-u[1], u[0])
print("Part 2 (deflection past a point mass, GM = 1e-6, b = 1; finite path of +/- 4000 b):")
for v0 in (0.1, 0.5, 0.9, 1.0):
    dGR = 2e-6/v0**2*(1 + v0**2)*np.sqrt(1 - (1/4000)**2)  # finite-path correction negligible
    dP = deflect(v0, lambda s: 1 - s**2); dC = deflect(v0, lambda s: 1.0)
    print(f"  v {v0}: push 1 - v^2 -> {dP:.4e}   push constant -> {dC:.4e}   GR {dGR:.4e}")
print("  the 4415 rule (step = f x local light speed, with limb refraction) plus a census push fading as 1/gamma^2 gives GR's")
print("  bending at every speed, light included; a speed-independent push overshoots (light would get 3/2 of its bending).")

print("Part 3 (independent run of the step rule itself: store f; speed s = f/K; turn n at the Snell rate; push g P(f) on the velocity):")
def step_rule(v0, P, GM=1e-6, b=1.0, L=4000.0, n=400000):
    pos = np.array([-L, b]); nd = np.array([1.0, 0.0])
    r = np.linalg.norm(pos); K = 1 + 2*GM/r; f = v0*K
    dt = 2*L/v0/n
    for _ in range(n):
        r = np.linalg.norm(pos); K = 1 + 2*GM/r
        g = -GM*pos/r**3; gradlnK = 2*g/K
        s = f/K
        nd = nd + s*(gradlnK - nd*(nd @ gradlnK))*dt; nd /= np.linalg.norm(nd)   # Snell-rate turning
        u = s*nd + g*P(f)*dt                                                      # census push
        s = np.linalg.norm(u); nd = u/s; f = s*K
        pos = pos + u*dt
    return np.arctan2(-nd[1], nd[0])
for v0 in (0.1, 0.5, 0.9, 1.0):
    dGR = 2e-6/v0**2*(1 + v0**2)
    print(f"  v {v0}: step rule, push 1 - f^2 -> {step_rule(v0, lambda f: max(0.0, 1 - f**2)):.4e}   GR {dGR:.4e}")
print("  (Part 2 integrated the closed-form acceleration, a consistency check; Part 3 runs the rule itself.)")

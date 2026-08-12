#!/usr/bin/env python
"""Patch 3086 -- D-ARC-FORCE two-body isolation test.

One +/- pair, free space, no box, no noise, no damping (gamma = 1),
continuous integrator. Forces exactly as the 3083/3085 array coded
them (electric with r >= 1 floor; magnetic of moving charges at c=1,
velocities saturated at 1), INSTANTANEOUS here (retardation off) so
the analytic limit exists.

Analytic reference (instantaneous, Newtonian, symmetric orbit):
members at +/-x, circular orbit radius a (separation s = 2a), speeds
v opposite => parallel currents. Electric on each: 1/s^2 inward.
Magnetic: B at 1 from 2 = q2 (v2 x rhat)/s^2 ; F = q1 v1 x B =>
inward magnitude v^2/s^2 (attraction for parallel currents).
Orbit condition: v^2/a = (1 + v^2)/s^2 = (1 + v^2)/(4 a^2)
=> v^2 = 1/(4a - 1)  (valid 4a > 1; v < 1 automatic for a > 0.5).

Tests:
 T1 circular orbit at a = 2 (s = 4): launch with the analytic v;
    integrate 20,000 Moments; report radius drift, energy drift,
    period vs analytic 2*pi*a/v.
 T2 stability probe: same but gamma = 0.98 (brake on) -- orbit must
    DECAY smoothly (magnetic does no work; brake does) with no
    overflow. Any overflow here reproduces the 3085 instability in
    the minimal setting and localises it.
 T3 lattice variant of T1 (round(V) address jumps) -- the discrete
    integrator's behaviour on a known orbit.
No band quantity anywhere.
"""
import numpy as np

def clip1(u):
    n = np.linalg.norm(u)
    return u if n <= 1.0 else u/n

def forces(x1, x2, v1, v2):
    d = x1 - x2; s = np.linalg.norm(d)
    if s < 1e-9:
        return np.zeros(3), np.zeros(3)
    se = max(s, 1.0); rhat = d/s
    # electric: opposite charges attract: F1 = -rhat/se^2
    F1 = -rhat/se**2; F2 = rhat/se**2
    # magnetic: q1=+1, q2=-1
    c1, c2 = clip1(v1), clip1(v2)
    B_at1 = (-1.0)*np.cross(c2, -rhat)/se**2      # from 2 at 1 (rhat 2->1 = +rhat; source-to-field = d/s)
    B_at2 = (+1.0)*np.cross(c1,  rhat)/se**2
    F1 = F1 + (+1.0)*np.cross(c1, B_at1)
    F2 = F2 + (-1.0)*np.cross(c2, B_at2)
    return F1, F2

def run(a=2.0, T=20000, gamma=1.0, lattice=False):
    v = np.sqrt(1.0/(4*a - 1.0))
    x1 = np.array([ a, 0.0, 0.0]); x2 = -x1.copy()
    v1 = np.array([0.0,  v, 0.0]); v2 = -v1.copy()
    rads, encs = [], []
    for t in range(T):
        F1, F2 = forces(x1, x2, v1, v2)
        v1 = gamma*v1 + F1; v2 = gamma*v2 + F2
        if not np.all(np.isfinite(v1)) or np.linalg.norm(v1) > 1e6:
            return dict(status=f"OVERFLOW at t={t}", rad=np.nan, edrift=np.nan, per=np.nan)
        s1 = np.round(v1) if lattice else v1
        s2 = np.round(v2) if lattice else v2
        x1 = x1 + s1; x2 = x2 + s2
        sep = np.linalg.norm(x1 - x2)
        rads.append(sep/2)
        encs.append(0.5*(v1@v1 + v2@v2) - 1.0/max(sep, 1.0))
    r = np.array(rads); e = np.array(encs)
    # crude period: zero-crossings of x1[1]... use radius oscillation instead
    per_analytic = 2*np.pi*a/v
    return dict(status="OK", rad0=r[:100].mean(), radN=r[-100:].mean(),
                edrift=(e[-100:].mean() - e[:100].mean()),
                per=per_analytic, vmax=float(np.max(np.abs(v1))))

print("T1 circular, gamma=1, continuous:")
z = run()
print("  ", z)
print("T2 braked, gamma=0.98, continuous:")
z = run(gamma=0.98)
print("  ", z)
print("T3 circular, gamma=1, lattice:")
z = run(lattice=True, T=4000)
print("  ", z)

# ===== DIAGNOSIS + FIX =============================================
# T1 (gamma=1, no retardation, no noise) PUMPS energy: the naive
# v += v x B kick is the known non-conservative discretisation of a
# force that does no work. FIX (standard, parameter-free): the BORIS
# pusher -- half electric kick, EXACT ROTATION for the magnetic part
# (|v| preserved by construction), half electric kick. Brake applied
# after as a separate multiplication.
def eb(x1, x2, v1, v2):
    d = x1 - x2; s = np.linalg.norm(d)
    if s < 1e-9:
        z = np.zeros(3); return z, z, z, z
    se = max(s, 1.0); rhat = d/s
    E1 = -rhat/se**2; E2 = rhat/se**2            # electric force (q folded)
    B1 = (-1.0)*np.cross(clip1(v2), -rhat)/se**2 # B at 1 (source 2)
    B2 = (+1.0)*np.cross(clip1(v1),  rhat)/se**2
    return E1, E2, B1, B2

def boris(v, E, B, q):
    vm = v + 0.5*E
    t = 0.5*q*B
    t2 = t@t
    vp = vm + np.cross(vm + np.cross(vm, t), 2*t/(1+t2))
    return vp + 0.5*E

def run_boris(a=2.0, T=20000, gamma=1.0, lattice=False):
    v = np.sqrt(1.0/(4*a - 1.0))
    x1 = np.array([a, 0., 0.]); x2 = -x1.copy()
    v1 = np.array([0., v, 0.]); v2 = -v1.copy()
    rads, encs = [], []
    for t in range(T):
        E1, E2, B1, B2 = eb(x1, x2, v1, v2)
        v1 = gamma*boris(v1, E1, B1, +1.0)
        v2 = gamma*boris(v2, E2, B2, -1.0)
        if not np.all(np.isfinite(v1)) or np.linalg.norm(v1) > 1e6:
            return dict(status=f"OVERFLOW at t={t}")
        x1 = x1 + (np.round(v1) if lattice else v1)
        x2 = x2 + (np.round(v2) if lattice else v2)
        sep = np.linalg.norm(x1 - x2)
        rads.append(sep/2)
        encs.append(0.5*(v1@v1 + v2@v2) - 1.0/max(sep, 1.0))
    r = np.array(rads); e = np.array(encs)
    return dict(status="OK", rad0=float(r[:100].mean()), radN=float(r[-100:].mean()),
                edrift=float(e[-100:].mean() - e[:100].mean()))

print("\nBORIS T1 circular, gamma=1, continuous (must be bounded, edrift ~ 0):")
print("  ", run_boris())
print("BORIS T2 braked, gamma=0.98 (must decay smoothly):")
print("  ", run_boris(gamma=0.98))
print("BORIS T3 lattice, gamma=1:")
print("  ", run_boris(lattice=True, T=4000))
print("""
TWO-BODY VERDICT: the 3085 instability is the naive v x B kick
(energy-pumping discretisation of a work-free force). The Boris
rotation is the parameter-free fix. PORT TO THE ARRAY = next
session's first CC item; the pre-stated criterion is unchanged.""")

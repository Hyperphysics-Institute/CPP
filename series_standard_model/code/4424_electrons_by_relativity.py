"""Patch 4424 -- the founder: "Please proceed" (electrons moving by relativity's laws, 4422 item 4).

In CPP a CP carries no velocity; each Moment it steps by f x (local light speed), with f held in the sea's DP organization
(4415) and changed only by forces (his 4404: Delta SSV_abs is the F in F = ma). The question: what must a push do to f?

Part 1. Three update rules under a steady push F (absolute frame, per absolute Moment), m = c = 1:
   (N) Newtonian, capped at light speed: f += F dt, clipped at 1 -- hits the cap abruptly;
   (W) additive organization, clocked by the CP: the push adds F per tick of the CP's OWN clock to a stored count w, and the
       step is f = tanh(w). The CP's clock runs slow by sqrt(1 - f^2) (4408), so dw = F sqrt(1 - f^2) dt;
   (P) stored momentum, absolute Moments: the sea stores p; each absolute Moment's push adds F dt; the step is
       f = p / sqrt(m^2 c^2 + p^2). No CP clock factor is needed. Mathematically identical to (W).
   (R) relativity: p = gamma m v grows as F t, so f = F t / sqrt(1 + (F t)^2).
   (In 1D the force along the motion is the same in every frame, so a constant lab force is a constant proper force.)
Part 2. Energy and inertia: work done F dx against the energy the sea holds; longitudinal inertia (1/f) dE/df for three
        enrolment laws.
Part 3. Collinear velocity addition from adding organization counts: tanh(w1 + w2) = (u + v)/(1 + u v).
"""
import numpy as np
F = 1.0; dt = 1e-4; T = 3.0
t = np.arange(0, T + dt, dt)
fN = np.minimum(F*t, 1.0)
w = 0.0; fW = np.empty_like(t); x = 0.0; work = np.empty_like(t)
for i in range(len(t)):
    fW[i] = np.tanh(w); work[i] = x*F
    x += fW[i]*dt
    w += F*np.sqrt(1 - fW[i]**2)*dt
p = 0.0; fP = np.empty_like(t)
for i in range(len(t)):
    fP[i] = p/np.sqrt(1 + p**2); p += F*dt
fR = F*t/np.sqrt(1 + (F*t)**2)
print("Part 1 (speed / c under a steady push):")
for tt in (0.5, 1.0, 2.0, 3.0):
    i = int(round(tt/dt))
    print(f"  t {tt:.1f}: Newtonian-capped {fN[i]:.4f}   rapidity count, CP-clocked {fW[i]:.4f}   stored momentum {fP[i]:.4f}   relativity {fR[i]:.4f}")
print(f"  largest difference vs relativity: rapidity count {np.abs(fW - fR).max():.1e}, stored momentum {np.abs(fP - fR).max():.1e} (step {dt})")
gam = 1/np.sqrt(1 - fW**2)
print(f"  work done vs (gamma - 1): largest difference {np.abs(work - (gam - 1)).max():.1e}  -> the sea must hold (gamma - 1) m c^2")

print("Part 2 (longitudinal inertia (1/f) dE/df for three enrolment laws, relative to m):")
f = np.array([0.1, 0.5, 0.9, 0.99])
laws = {"(gamma - 1) m c^2 [relativity]": lambda f: 1/np.sqrt(1 - f**2) - 1,
        "(1/2) m v^2 / (1 - v^2)": lambda f: 0.5*f**2/(1 - f**2),
        "(1/2) m v^2 [Newton]": lambda f: 0.5*f**2}
h = 1e-6
for name, E in laws.items():
    mL = (E(f + h) - E(f - h))/(2*h)/f
    print(f"  {name:32s} " + "  ".join(f"v {fi}: {m:8.3f}" for fi, m in zip(f, mL)))
print("  gamma^3 for comparison:          " + "  ".join(f"v {fi}: {g:8.3f}" for fi, g in zip(f, (1 - f**2)**-1.5)))

print("Part 3 (collinear velocity addition, relativity's law restated as rapidity additivity -- a target, not an origin):")
for u, v in ((0.5, 0.5), (0.9, 0.9), (0.99, 0.5)):
    print(f"  u {u}, v {v}: tanh(atanh u + atanh v) = {np.tanh(np.arctanh(u) + np.arctanh(v)):.6f}"
          f"   (u + v)/(1 + uv) = {(u + v)/(1 + u*v):.6f}   Galilean u + v = {u + v:.2f}")

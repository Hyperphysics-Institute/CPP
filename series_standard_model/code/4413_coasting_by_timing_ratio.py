"""Patch 4413 (Claude-initiated, at the founder's request after 4412: 'work out how the substrate meets these conditions').

Proposal: the founder's 2 Aug 2026 round-trip asymmetry, read as a TIMING RATIO rather than as a force.  A CP moving at v
through DPs at rest in the sea gets its DI-bits back from distance r ahead after t_f = 2r/(c+v) and from behind after
t_a = 2r/(c-v).  The ratio (t_a - t_f)/(t_a + t_f) is exactly v/c -- at every speed, every distance, every coupling.
Coasting rule: each Moment the CP steps by the velocity its returns encode (plus whatever forces add).

Part 1  exactness of the ratio (all v, all r).
Part 2  a fixed per-reflection delay would bias it (drag); the rule needs reflections with no fixed delay.
Part 3  memory: if the returns encode the velocity averaged over the last W Moments (the round-trip window), the rule is
        v_n = mean(v_{n-1..n-W}):  uniform motion persists at any v (Newton I), the family is neutrally stable, and a kick
        leaves a lasting velocity change 2 dx/(W+1) (inertia from the round-trip memory).
Part 4  a bound pair moving together: each CP coasts by its own returns; mutual forces equal and opposite (census
        channel, 4411-4412) leave the pair's centre moving uniformly; the raw vector-sum forces of 4411 make it drive itself.
"""
import numpy as np

print("Part 1: (t_b - t_f)/(t_b + t_f) vs v (c = 1); r = reflector distance at emission, fore and aft reflectors at rest")
for v in (0.001, 0.1, 0.5, 0.9, 0.999):
    out = []
    for r in (1.0, 68.5, 1e6):
        tf, tb = 2*r/(1 + v), 2*r/(1 - v)
        out.append((tb - tf)/(tb + tf))
    print(f"  v = {v:6}: ratio at r = 1, 68.5, 1e6 -> " + ", ".join(f"{x:.12f}" for x in out))
print("  exact: independent of distance, charge, mass, sign of the sea's response; always < 1 (no CP reaches c)")

print("\nPart 2: a fixed reflection delay d (Moments) biases the readout low (a drag):")
for r in (10, 100, 1000):
    v, d = 0.3, 1.0
    tf, tb = 2*r/(1 + v) + d, 2*r/(1 - v) + d
    print(f"  r = {r:5}: read {(tb - tf)/(tb + tf):.6f} for true 0.3  (bias {(tb - tf)/(tb + tf)/0.3 - 1:+.2e})")

print("\nPart 3 (low-speed toy only): memory rule v_n = mean of the last W velocities")
W = 50
v = [0.2]*W
for n in range(400):
    v.append(np.mean(v[-W:]))
print(f"  uniform start 0.2 -> after 400 Moments {v[-1]:.12f} (persists: Newton I)")
v = [0.2]*W; v[-1] += 0.05          # a kick: one Moment's extra displacement 0.05
for n in range(5000):
    v.append(np.mean(v[-W:]))
print(f"  kick of 0.05 in one Moment -> lasting velocity {v[-1]:.6f}; change {v[-1]-0.2:.6f} vs 2*0.05/(W+1) = {2*0.05/(W+1):.6f}")
# characteristic roots of z^W = (1/W) sum_{k=0}^{W-1} z^k
coef = np.zeros(W + 1); coef[0] = 1.0; coef[1:] = -1.0/W
roots = np.roots(coef)
print(f"  roots: largest |z| = {max(abs(roots)):.6f} (one root at 1; next largest {sorted(abs(roots))[-2]:.4f}): neutrally stable")

print("\nPart 4 (illustration of the forces only; no coasting rule used): a co-moving pair (separation 1, speed V), forces per Moment k*(force)")
V, k = 0.3, 1e-3
for name, f_trail, f_lead in (("census channel (equal and opposite)", 1 - V*V, -(1 - V*V)),
                              ("raw vector sum of arrivals (4411)", 1 + V, -(1 - V))):
    cm_kick = k*(f_trail + f_lead)/2
    print(f"  {name:38s}: net push on the pair per Moment {cm_kick:+.2e}  ({'none' if abs(cm_kick) < 1e-15 else 'self-drive'})")
print("  with coasting by each CP's own timing ratio, the pair's centre moves uniformly only in the first case")

print("\nPart 5: the exact rule -- each Moment the CP steps by the ratio from returns arriving now (r = 10), with the")
print("actual unequal fore/aft windows (c t_f = 2r - dx_f, c t_b = 2r + dx_b)")
def readout(xs, n, r):
    def solve(sign):
        t = 2*r
        for _ in range(200):
            m = n - t; i = int(np.floor(m)); fr = m - i
            xm = xs[i]*(1 - fr) + xs[i + 1]*fr
            t = 2*r - sign*(xs[n] - xm)
        return t
    tf = solve(+1); tb = solve(-1)
    return (tb - tf)/(tb + tf)
r = 10
for v0 in (0.0, 0.2, 0.5, 0.8, 0.9):
    kick = 0.001; N = int(4*r/(1 - v0)) + 5
    xs = list(np.arange(N + 1)*v0); xs[-1] += kick
    for n in range(N, N + 4000):
        xs.append(xs[-1] + readout(xs, n, r))
    dv = np.diff(xs)[-1] - v0
    if v0 == 0.0: base = dv/kick
    g = 1/np.sqrt(1 - v0*v0)
    print(f"  v = {v0}: lasting dv per unit kick {dv/kick:.5f} (relative to rest {dv/kick/base:.3f}; 1/gamma^3 = {g**-3:.3f})")
print("  -> coasting and neutral stability hold at all speeds; the kick response falls with speed, close to (not equal")
print("     to) 1/gamma^3: the exact rule itself yields a speed-dependent longitudinal inertia.")
print("\nPart 6: reflectors moving at u (signals at c in the absolute frame):")
for v, u in ((0.3, 0.0), (0.3, 0.3), (0.0, 0.2), (0.5, -0.2)):
    tf = 2*10/((1 - u)*(1 + v)); tb = 2*10/((1 + u)*(1 - v))
    print(f"  v = {v}, u = {u}: ratio {(tb - tf)/(tb + tf):+.6f} = (v - u)/(1 - uv) {(v - u)/(1 - u*v):+.6f}")
print("  -> a CP at rest in a flowing sea reads 0; it is carried only if it steps in the reflectors' frame (an added rule)")

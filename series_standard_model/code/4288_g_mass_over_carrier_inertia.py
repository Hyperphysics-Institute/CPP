#!/usr/bin/env python3
"""4288 -- founders_voice/4288: a CP has no rest mass but has inertia m_i from the DP-arcs it makes (SF-6 l.227-233:
m_eff = m0 gamma, m0 a tuned toy parameter), and moves at its V_i, not necessarily c.
Each orbiting CP: charge q_i, z-angular momentum L_i (signed), inertia m_i  ->  moment mu_i = q_i L_i / (2 m_i).
Spin S = sum L_i.  The electron's measured relation mu = -g (e/2m_e) S with g = 2.0023.   Here
      g = -(2 m_e / (e S)) * sum_i q_i L_i / (2 m_i)          (speed does not appear)
Outer CP charge -e, inner CP charge +e; spin axis +z; units hbar = 1, masses in m_e."""
import itertools
def g(Lo,Li,mo,mi):
    S=Lo+Li; mu=(-1)*Lo/(2*mo)+(+1)*Li/(2*mi)
    return -2*mu/S, S
print("(1) checks against earlier patches")
print(f"  SPIN-1 (4286 F): both CPs inertia m_e, co-rotating, L_o : L_i = 4 : 2sqrt2 of hbar/2 total")
Lo=0.5*4/(4+2*2**0.5); Li=0.5-Lo
print(f"    L_o = {Lo:.4f}, L_i = {Li:.4f}  ->  g = {g(Lo,Li,1,1)[0]:.4f}  (4286: 0.1716)")
print(f"  speed-c massless outer (4286/4287): inertia = motion energy/c^2 = m_e/2, pass-through inner (L_i = 0) -> g = {g(0.5,0,0.5,1)[0]:.4f}")

print("\n(2) pass-through inner (L_i = 0, lily-pad through the core): g = m_e / m_out.  Outer speed from L = m_out v R = hbar/2:")
for mo in (1.0,0.5,0.25):
    gv=g(0.5,0,mo,1)[0]; print(f"  outer inertia m_out = {mo:.2f} m_e  ->  g = {gv:.3f}")
print("  with m_out = m_e/2 (g = 2):  v R = hbar/m_e = c r_ZBW, so v/c = r_ZBW / R:")
for R,tag in ((1.0,"route (H) radius"),(2.0,""),(5.0,""),(11.756,"SPIN-1's r_out")):
    print(f"    R = {R:6.3f} r_ZBW  ->  v = {1/R:.3f} c   {tag}")
print("  -> g = 2 does not need light speed; it needs the circulating -eCP's inertia to be half the electron's mass.")
print("     (m_out here is the moving inertia m0*gamma; at v << c it is m0.)")

print("\n(3) the founder's idea: CPs carry whole multiples of the action unit; the magnet is the difference.")
print("  Spin must be S = hbar/2.  Whole-hbar amounts (L_o, L_i in {0, +-1, +-2, ...} hbar):")
ok=[(a,b) for a,b in itertools.product(range(-3,4),repeat=2) if abs((a+b)-0.5)<1e-9]
print(f"    combinations with L_o + L_i = 1/2:  {ok if ok else 'none -- a sum or difference of whole hbar is never hbar/2'}")
print("  Half-hbar units (L in multiples of hbar/2), |L| <= 2 hbar, S = +hbar/2, equal inertia m_c for both CPs:")
for a,b in itertools.product([x/2 for x in range(-4,5)],repeat=2):
    if abs(a+b-0.5)>1e-9: continue
    # g = 2 needs  -(2/S) * (-a/(2m) + b/(2m)) = 2  ->  (a - b)/(S m) = 2  -> m = (a-b)/(2S) = (a - b)
    m=(a-b)/(2*0.5)
    sense="co-rotating" if a*b>0 else ("counter-rotating" if a*b<0 else "inner pass-through")
    if m>0:
        print(f"    L_o = {a:+.1f}, L_i = {b:+.1f} ({sense:18s}): g = 2 needs each CP's inertia m_c = {m:.2f} m_e"
              f"  (two CPs: {2*m:.2f} m_e of moving inertia)")
print("  -> the one combination with both CPs lighter than the electron is L_o = hbar/2, L_i = 0: the pass-through inner.")
print("     'One unit and two units' (hbar and hbar/2, counter-rotating) needs each CP at 1.5 m_e: 3 m_e of inertia in")
print("     an electron of mass m_e -- possible only if binding removes 2 m_e, which nothing on file supplies.")

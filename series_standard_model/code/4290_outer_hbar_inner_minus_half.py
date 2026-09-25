#!/usr/bin/env python3
"""4290 -- founders_voice/4290: outer -eCP carries L_o = +hbar, inner +eCP lily-pad L_i = -hbar/2 (opposite sense);
spin S = hbar/2.  Moment per CP mu_i = q_i L_i / (2 m_i) (4288; SF-6 far field), inertia m_i > 0.
Units hbar = 1, e = 1, masses in m_e; mu_B = 1/2.  Electron: mu = -g (1/2) S, g = 2.0023."""
import numpy as np
def mu(Lo,Li,mo,mi): return (-1)*Lo/(2*mo) + (+1)*Li/(2*mi)
print("(1) sign rule: a charge's moment points along its own angular momentum times its charge's sign.")
for q,L,name in ((-1,+1,"-e going +"),(+1,-1,"+e going -"),(+1,+1,"+e going +")):
    print(f"  {name}:  mu_z = {q*L/2:+.2f}")
print("  -> a -e going one way and a +e going the OTHER way make magnets pointing the SAME way (they add).")
print("     Opposite charges make opposing magnets only when they circulate the SAME way.")

print("\n(2) the founder's amounts, S = +1 - 1/2 = +1/2 (counter-rotating): magnets add")
for mo,mi in ((1,1),(0.5,0.5),(1.5,1.5),(2.0,1.0),(1.0,1e9)):
    m=mu(1,-0.5,mo,mi); g=-2*m/0.5
    print(f"  m_out = {mo:4.2f}, m_in = {mi if mi<1e6 else float('inf'):>5.2f} m_e:  mu_z = {m:+.4f}  ->  g = {g:.4f}")
print("  g = 2 needs  1/m_out + 1/(2 m_in) = 1/m_e  (so m_out >= m_e always; equal only if the inner is infinitely heavy).")
mo=1+1/np.sqrt(2); mi=1/(2*(1-1/mo))
print(f"  least total moving inertia: m_out = {mo:.4f}, m_in = {mi:.4f}, total = {mo+mi:.4f} m_e = (1+1/sqrt2)^2 = {(1+1/np.sqrt(2))**2:.4f}")

print("\n(3) the same amounts with magnets OPPOSING would need both CPs to circulate the same way: then S = 1 + 1/2 = 3/2:")
print(f"  S = {1+0.5:.1f} hbar -- not the electron's spin.")
print("  With hbar/2 as the unit and both circulating the same way, S = 1/2 only for (1/2, 0): the reading 4287-4289 used.")

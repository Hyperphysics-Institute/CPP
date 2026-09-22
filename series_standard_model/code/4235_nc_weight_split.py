#!/usr/bin/env python3
"""4235 -- OPEN-EW-NC: the constituent weights of 4216/4198 split into an isospin part and an electromagnetic part.
Q_W(q) = 2 T3(q) - 4 Q(q) s^2 per quark (tree), s^2 = 3/(8 phi) (CPP). Constituents: u = +qCP core + orbital eDP;
d = u + linear -eCP. So core weight = Q_W(u); linear-oscillator weight = Q_W(d) - Q_W(u)."""
phi=(1+5**.5)/2; s2=3/(8*phi)
def QW(T3,Q): return 2*T3 - 4*Q*s2
u=QW(+.5, 2/3); d=QW(-.5,-1/3); core=u; lin=d-u
print(f"s^2 = 3/(8 phi) = {s2:.4f}")
print(f"Q_W(u) = {u:+.4f}   Q_W(d) = {d:+.4f}   neutron = {u+2*d:+.4f}   proton = {2*u+d:+.4f}")
print(f"per +qCP core (u):            {core:+.4f} = isospin {2*0.5:+.3f}  +  EM {-4*(2/3)*s2:+.4f}   [ = 1 - 1/phi = 1/phi^2 ]")
print(f"per linear -eCP (d - u):      {lin:+.4f} = isospin {2*(-0.5)-2*0.5:+.3f}  +  EM {-4*(-1)*s2:+.4f}   [ = -2 + 3/(2 phi) ]")
print(f"contact weights of 4216 (= -Q_W): core {-core:+.3f}, linear {-lin:+.3f}   -> match 4216's -0.382 / +1.073")
print("\nReading: the EM part is -4 Q s^2 per constituent -- the charge times the 600-cell mode fraction already derived in SF-2 --")
print("and needs no new mechanism. The isospin part is +1 per bare core and -2 per linear oscillator. Route (a), the elastic")
print("W0 capture-and-re-eject, must produce ONLY this: a throw of unit weight one way at a bare +qCP, and a throw of DOUBLE")
print("weight the other way where a linear -eCP is already held at the core. The -2 = (-1 for the reversed event) + (-1 for")
print("the core's own event being cancelled) is the first thing to test.")

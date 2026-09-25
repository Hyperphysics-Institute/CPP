#!/usr/bin/env python3
"""4289 -- does SPIN-1 + SPIN-2 derive the electron's spin hbar/2, or take it as input?
SPIN-1 (eqs force_balance, L_total, thm:spin): +eCP at r_in, -eCP at 2 r_in, each mass m_e, circular Coulomb orbits
about the -eCP core:  omega^2 = k e^2/(m r^3),  L = m omega_out r_in^2 (2 sqrt2 + 4).
SPIN-2 (thm:ratio): the pair anchors at the mode-2 antinode r_th/3 and node 2 r_th/3 of the ZBW cloud, r_th = hbar/2mc.
SPIN-2 sec 'Scale Connection': the orbit is then placed at r_in = a0/(4(1+sqrt2)^2), 35.27x the anchoring radius."""
import numpy as np
hbar=1.054571817e-34; m=9.1093837015e-31; e=1.602176634e-19; k=8.9875517923e9; c=299792458.0
a0=hbar**2/(m*k*e**2); alpha=k*e**2/(hbar*c); rC=hbar/(m*c); rth=rC/2
def L_of(rin):
    wout=np.sqrt(k*e**2/(m*(2*rin)**3)); return m*wout*rin**2*(2*np.sqrt(2)+4)
print("(1) Coulomb balance allows a circular pair at EVERY r_in; L grows as sqrt(r_in):")
for f in (1/3/35.27*35.27, 1.0, 10.0, 35.27, 100.0):
    rin=f*rth/3; print(f"  r_in = {f:7.2f} x (r_th/3) = {rin:.3e} m:  L = {L_of(rin)/(hbar/2):.4f} hbar/2")
print("  L/(hbar/2) = 2(1+sqrt2) sqrt(r_in/a0) -- a continuous family; nothing in the balance selects hbar/2.")
rin_s1=a0/(4*(1+np.sqrt(2))**2)
print(f"  SPIN-1's r_in = a0/(4(1+sqrt2)^2) = {rin_s1:.4e} m is the solution of L(r_in) = hbar/2: L = {L_of(rin_s1)/(hbar/2):.6f} hbar/2")
print("  -> hbar/2 is the INPUT that fixes r_in; the 'exact to all digits' table recomputes the input.")

print("\n(2) the non-circular reading: both radii where SPIN-2 anchors them (antinode r_th/3, node 2 r_th/3):")
rin=rth/3
print(f"  r_in = r_th/3 = alpha a0/6 = {rin:.4e} m;  v_in/c = sqrt(6 alpha) = {np.sqrt(k*e**2/(m*rin))/c:.4f}")
Lnc=L_of(rin)
print(f"  L = (1+sqrt2) sqrt(alpha/6) hbar = {Lnc/hbar:.4f} hbar = {Lnc/(hbar/2):.4f} x hbar/2  (1/{(hbar/2)/Lnc:.2f} of the electron's spin)")
print(f"  closed form check: (1+sqrt2) sqrt(alpha/6) = {(1+np.sqrt(2))*np.sqrt(alpha/6):.4f}")

print("\n(3) SPIN-2's scale connection moves the pair to 35.27x the anchoring radii:")
print(f"  r_in(SPIN-1)/(r_th/3) = {rin_s1/(rth/3):.2f};  there, r = {rin_s1/rth:.2f} r_th and {2*rin_s1/rth:.2f} r_th -- beyond r_th,")
print("  where SPIN-2's mode-2 wave (defined on 0..r_th, free boundary at r_th) has no node or antinode to anchor to.")
print("  -> r_out = 2 r_in is imported to a scale where its anchoring condition does not apply.")

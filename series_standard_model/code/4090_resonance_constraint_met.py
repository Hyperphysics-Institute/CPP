"""4090 (EW lane) -- the resonance constraint met: CPP already contains a DERIVED detuned frequency pair.

4089 left a sharp constraint: a w-oscillation at the SAME frequency as the 3D circulation it pairs with gives
EXACTLY ZERO handedness (1:1 resonance => simple rotation). The bounded question was whether the corpus
contains a detuned oscillation.

IT DOES, and it is derived rather than assumed. SPIN-1: the captured DP's positive CP falls to r_in while its
negative CP is pushed to 2 r_in; both orbit the central -eCP; "the exact ratio of their angular frequencies is
2 sqrt(2) ~ 2.83. This ratio is not assumed; it falls out of the 1/r^2 Coulomb force law and the geometric
fact that the outer radius is exactly twice the inner radius."

S1  verify 2 sqrt 2 from SPIN-1's own stated inputs (1/r^2 balance, r_out = 2 r_in).
S2  handedness at that ratio, in 4089's model.
S3  HOW THE MAGNITUDE SCALES -- the honest check on whether this yields a prediction or just a number.
S4  WHAT IT DOES NOT SETTLE: the two orbits are COPLANAR (both about the same axis), so they do not by
    themselves form a double rotation. The w-leg is still required.
"""
import numpy as np
exec(open('/tmp/w/4089.py').read().split('print("R1')[0])   # reuse motion_bivector and pf

print("S1  verify the 2 sqrt 2 ratio from SPIN-1's stated inputs")
# circular orbit under 1/r^2 central force: m w^2 r = k/r^2  => w ~ r^(-3/2)
r_in, r_out = 1.0, 2.0
w_in, w_out = r_in**-1.5, r_out**-1.5
print(f"    w ~ r^(-3/2) from 1/r^2 balance;  r_out = 2 r_in")
print(f"    w_in / w_out = {w_in/w_out:.6f}   2*sqrt(2) = {2*np.sqrt(2):.6f}")
assert abs(w_in/w_out - 2*np.sqrt(2)) < 1e-9
print("    => reproduced exactly. The corpus's detuned pair is DERIVED, not fitted.")

print("\nS2  handedness at the corpus's own ratio")
for label, r in (("1:1 (resonance)", 1.0), ("SPIN-1 ratio 2 sqrt 2", 2*np.sqrt(2))):
    val = pf(motion_bivector(0.0, Om=r))
    print(f"    Om/w = {r:8.5f}  ({label:22s})  pseudoscalar = {val:+.4f}")
print("    => at the corpus's own derived ratio the handedness is nonzero. 4089's resonance constraint is")
print("       SATISFIED by a structure already in the theory, with nothing added.")
assert abs(pf(motion_bivector(0.0, Om=2*np.sqrt(2)))) > 1

print("\nS3  how does the magnitude scale? (the check that decides prediction vs mere number)")
print("     Om/w      pseudoscalar     pseudoscalar / (2*Om/w)")
for r in (1.05, 1.4142, 2.0, 2.8284, 4.0):
    v = pf(motion_bivector(0.0, Om=r))
    print(f"    {r:7.4f}   {v:+10.4f}      {v/(2*r):+.4f}")
print("    => |pseudoscalar| = 2 x (frequency ratio), exactly. The magnitude is LINEAR in the ratio and")
print("       carries no structure of its own: 2 sqrt 2 produces 5.657 rather than any distinguished value.")
print("       So this yields NO zero-parameter prediction. It removes an obstruction; it predicts nothing.")

print("\nS4  what it does not settle")
print("    SPIN-1's two orbits are COPLANAR -- the inner and outer CPs orbit the same central -eCP about a")
print("    common axis. Two coplanar circulations do NOT make a double rotation (4072: a pseudoscalar needs")
print("    two ORTHOGONAL planes spanning all four dimensions). So the detuned pair supplies the FREQUENCY")
print("    RATIO the constraint needs, but NOT the second plane: the w-leg is still required and still")
print("    unexplained. The founder's oscillation remains the only candidate for it.")

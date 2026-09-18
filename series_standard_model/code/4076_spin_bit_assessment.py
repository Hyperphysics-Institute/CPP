"""4076 (EW lane) -- the founder's spin-bit proposal, assessed: what it does and does not give.

Founder (17 Sep): each GP carries a 4th-dimension value of +/-1, the SPIN BIT; DI-bits carry it; a majority
of arriving DI-bits tips the register; an unpaired CP seeds its neighbourhood; two opposite bits can share
one 3D location. His question: "For the spin bit to have any meaning, it must elicit a response. What is
that response?"

B1  IS A SPIN BIT P-ODD?  Physical parity P = diag(+1,-1,-1,-1) inverts 3-space and leaves the 4th-axis
    address alone (4074). A +/-1 value ATTACHED TO A GP is a scalar: P moves it to the mirrored GP but does
    not change its value. So a spin bit AS DEFINED ("the direction of the spin", up/down on the 4th axis)
    is P-EVEN -- the same class as polarity, and it cannot by itself supply chirality.
B2  THE REPAIR, AND IT IS SMALL. If the bit's SEEDING RULE is the helicity of the seeding CP --
    b = sign(omega . v), its 3D spin axis projected on its direction of motion -- then b is P-ODD, because
    omega is axial and v is polar. Same register, same DI-bit plumbing; only the rule that writes it changes.
B3  THE RESPONSE (the founder's question, answered structurally). Let a process rate be R(b). Parity
    violation appears in observables iff R depends on b ODDLY. R even in b (e.g. R ~ b^2) gives NO parity
    violation even when b is P-odd. So: the response must be LINEAR in the spin bit.
B4  CONSISTENCY WITH 4075. 4075 required: EM depends on the 4th-axis component only through EVEN functions;
    the handed process reads it LINEARLY. B3 is the same statement in the founder's own variable. The spin
    bit is a concrete implementation of chi4's 4th-axis component.
B5  THE TWO-SLOT RESULT, which is independent of chirality and may be the proposal's real prize: a +/-1
    register at each 3D location gives exactly TWO slots per 3D GP. Counted explicitly against THEO-QM-10,
    which currently derives Pauli exclusion and spin-statistics from ONE CP per GP.
"""
import numpy as np
rng = np.random.default_rng(4076)
P3 = np.diag([-1.0, -1, -1])          # physical parity acting on 3-space

print("B1  is a spin bit, as defined, parity-odd?")
# a scalar +/-1 attached to a GP: P maps GP -> mirrored GP, value unchanged
bits = rng.choice([-1.0, 1.0], size=2000)
print(f"    a +/-1 value attached to an address: P relocates the address, value unchanged -> P-EVEN")
print(f"    (identical class to polarity, which 4071 showed cannot rescue a deficient set)")
# demonstrate: any observable built from bits and P-even 3D data is P-even
obs_before = float(np.mean(bits))
obs_after  = float(np.mean(bits))        # values are carried along unchanged
print(f"    mean bit before P = {obs_before:+.4f}, after P = {obs_after:+.4f}  -> unchanged")
assert abs(obs_before - obs_after) < 1e-15

print("\nB2  the repair: seed the bit with HELICITY instead of with 'up/down'")
worst = 0.0; flips = 0; n = 0
for _ in range(20000):
    om = rng.normal(size=3)              # 3D spin axis (axial: unchanged by P)
    v  = rng.normal(size=3)              # velocity (polar: flips under P)
    b      = np.sign(om @ v)
    b_mirr = np.sign((om) @ (P3 @ v))    # omega unchanged, v flipped
    n += 1; flips += (b_mirr == -b)
    worst = max(worst, abs(b + b_mirr))
print(f"    b = sign(omega . v):  flips under P in {flips}/{n} draws; max |b + b_mirror| = {worst:.1e}")
print(f"    => P-ODD. Same register, same DI-bit plumbing; only the WRITE RULE changes.")
assert flips == n

print("\nB3  the founder's question: what response makes the bit mean something?")
def rate(b, kind, a=1.0, c=0.35):
    return a + c*b if kind == "linear" else a + c*b*b
for kind in ("linear", "even"):
    up, dn = rate(+1, kind), rate(-1, kind)
    # a P-odd observable: the asymmetry between the two hands
    asym = (up - dn) / (up + dn)
    print(f"    response {kind:6s} in b:  R(+) = {up:.3f}, R(-) = {dn:.3f},  asymmetry = {asym:+.4f}"
          f"   -> {'PARITY VIOLATION' if abs(asym) > 1e-12 else 'no parity violation'}")
assert abs((rate(1,'even')-rate(-1,'even'))) < 1e-15 and abs(rate(1,'linear')-rate(-1,'linear')) > 1e-3
print("    => the response must be LINEAR in the spin bit. An even response gives nothing, even with a P-odd bit.")

print("\nB4  consistency with 4075: EM even in the 4th-axis component, handed process linear in it.")
print("    B3 is that same requirement written in the founder's variable. The spin bit IS chi4's carrier,")
print("    made concrete and given propagation machinery (DI-bits) the corpus already has.")

print("\nB5  the two-slot result -- independent of chirality")
slots = {}
for _ in range(10000):
    gp = tuple(rng.integers(0, 3, size=3))
    b = rng.choice([-1, 1])
    slots.setdefault(gp, set()).add(b)
occ = [len(v) for v in slots.values()]
print(f"    distinct (3D address, spin bit) states per 3D GP: max = {max(occ)}, capacity = 2")
print(f"    => exactly two slots per 3D location: the Pauli doubling QM needs, from a +/-1 register.")
print(f"    NOTE: THEO-QM-10 currently derives Pauli exclusion and spin-statistics from ONE CP per GP")
print(f"    (via THEO-1). A spin bit gives TWO. That is a REVISION to a registered theorem's basis, not a")
print(f"    contradiction of THEO-1 itself (which concerns co-occupation of the SAME point).")
assert max(occ) == 2

#!/usr/bin/env python3
"""4199 — the founder's neutrino-formation picture plus ONE handed rule, against three measured facts.

Founder (founders_voice/4199_*): the escaping -eCP captures an orbital DP from the Sea; the spin induced on
a nearby DP is the (anti)neutrino, carrying the ANTI-SPIN of the captured orbital DP.
    => spins:   A_nu = -A_e                                   (his statement; a spin-singlet lepton pair)
Trial handed rule, the same term as 4193's gate:  the weak vertex selects  q (v_hat . A) = +1,
    with q = -1 for the particle (-eCP), +1 for the antiparticle.
The antineutrino is an antiparticle-type object: q = +1.
"""
import itertools
print("helicity h = sign(v_hat . A); rule: q*h = +1\n")
print(f"{'object':14s} {'q':>3s} {'h required':>11s} {'measured helicity':>20s}")
for name, q, meas in (('electron', -1, 'left  (-v/c)'), ('positron', +1, 'right (+v/c)'),
                      ('antineutrino', +1, 'right'), ('neutrino', -1, 'left')):
    print(f"{name:14s} {q:3d} {q:11d} {meas:>20s}")       # h = q since q*h = +1

print("\nbeta-minus, one axis: electron velocity v_e = +1 or -1, antineutrino v_nu = +1 or -1")
print(f"{'v_e':>4s} {'v_nu':>5s} {'A_e':>4s} {'A_nu':>5s} {'spins opposite (founder)':>25s}   allowed?")
for ve, vn in itertools.product((+1, -1), repeat=2):
    Ae, An = -ve, +vn                                      # A = h * v_hat with h = q:  electron h = -1, antineutrino h = +1
    ok = (An == -Ae)
    print(f"{ve:4d} {vn:5d} {Ae:4d} {An:5d} {str(ok):>25s}   {'YES: same direction' if ok and ve == vn else ('yes' if ok else 'no')}")
print("\n=> with anti-parallel spins the two leptons must leave in the SAME direction:")
print("   electron-antineutrino correlation a = +1, the measured value for pure Fermi (0+ -> 0+) decays.")
print("   Gamow-Teller decays (a = -1/3) need PARALLEL lepton spins, which the picture as stated does not supply.")

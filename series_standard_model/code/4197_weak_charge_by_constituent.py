#!/usr/bin/env python3
"""4197 — the founder's pointer (the down quark's linear -eCP oscillator) tested against weak charges.

Weak vector charge of a fermion: Q_W = 2 T3 - 4 Q sin^2(theta_W). CPP's own angle: sin^2 = 3/(8 phi) (SM-6).
CPP constituents (master_glossary, SS-2): every quark has a central +qCP CORE; a down-type quark has in
addition a captured -eCP LINEAR OSCILLATOR. So a nucleon = 3 cores + n_d oscillators.
"""
phi = (1 + 5 ** 0.5) / 2
s2 = 3 / (8 * phi)
QW = lambda T3, Q: 2 * T3 - 4 * Q * s2
u, d, e, nubar = QW(.5, 2/3), QW(-.5, -1/3), QW(-.5, -1), -QW(.5, 0)
core, osc = u, d - u
print(f"sin^2 theta_W = 3/(8 phi) = {s2:.5f}")
print(f"per +qCP core            (= up quark)         {core:+.5f}     [1/phi^2 = {phi**-2:.5f}]")
print(f"per captured -eCP linear oscillator (= d - u) {osc:+.5f}")
print(f"free electron (bare -eCP + orbiting eDP)      {e:+.5f}")
print(f"oscillator minus free electron                {osc - e:+.5f}     [antineutrino carries {nubar:+.5f}]")
print()
print(f"{'':10s} {'cores':>5s} {'oscillators':>11s} {'Q_W built':>10s} {'measured / SM':>22s} {'H1: oscillators only':>22s}")
for name, nd, meas in (('proton', 1, '+0.0719 +/- 0.0045'), ('neutron', 2, '-0.99 (SM)')):
    print(f"{name:10s} {3:5d} {nd:11d} {3*core + nd*osc:+10.4f} {meas:>22s} {nd*osc:+22.4f}")
print(f"\nratio proton/neutron:  built {(3*core+osc)/(3*core+2*osc):+.3f}   measured about -0.073   H1 alone {0.5:+.3f}")

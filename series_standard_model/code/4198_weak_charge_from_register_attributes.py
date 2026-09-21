#!/usr/bin/env python3
"""4198 — can the weak charge be assembled from what A1' already gives a CP (polarity, type -> charge)?

Q_W = 2 T3 - 4 Q sin^2(theta_W), with CPP's 4 sin^2 = 3/(2 phi).   Trial assembly from CPP constituents:
    2 T3  =  (sum of polarity signs of the UNPAIRED CPs)  +  (ZBW-mode term)
    mode term:  0  orbital ZBW about an anchor (free electron; quark core)
               -1  LINEAR ZBW of a captured -eCP (down quark)             [founder's pointer, 4197]
               +1  unanchored ZBW with no central CP (neutrino, SF-4 FI-alpha-3)
Paired CPs (the DPs of the Sea, the electron's orbiting eDP) contribute zero to both sums.
"""
phi = (1 + 5 ** 0.5) / 2
k = 3 / (2 * phi)
#            name        unpaired CPs as (polarity, electric charge)     mode   2T3(SM, left-handed)
rows = [('up quark',     [(+1, +2/3)],                                    0,    +1),
        ('down quark',   [(+1, +2/3), (-1, -1)],                         -1,    -1),
        ('electron',     [(-1, -1)],                                      0,    -1),
        ('neutrino',     [],                                             +1,    +1),
        ('proton  uud',  [(+1, +2/3)] * 3 + [(-1, -1)],                  -1,    +1),
        ('neutron udd',  [(+1, +2/3)] * 3 + [(-1, -1)] * 2,              -2,    -1)]
print(f"4 sin^2 theta_W = 3/(2 phi) = {k:.5f}\n")
print(f"{'':12s} {'polarity sum':>12s} {'mode':>5s} {'2T3 built':>10s} {'2T3 SM':>7s} {'charge':>7s} {'Q_W built':>10s} {'Q_W SM':>8s}")
for name, cps, mode, t3 in rows:
    pol = sum(p for p, _ in cps); Q = sum(q for _, q in cps)
    built = pol + mode
    print(f"{name:12s} {pol:12d} {mode:5d} {built:10d} {t3:7d} {Q:7.3f} {built - k*Q:10.4f} {t3 - k*Q:8.4f}")

#!/usr/bin/env python3
"""4236 -- direction of the neutral-current push on a passing electron, per constituent, isospin part only,
compared with the direction of the handed throw (ejection rule: an electron leaves AGAINST its own spin).
NC drift (4222/4216): v_extra along +Q_W sigma. Isospin part of Q_W per constituent: +1 (bare +qCP core), -2 (linear -eCP)."""
iso = {'bare +qCP core (u)': +1, 'linear -eCP at a core (d - u)': -2}
print(f"{'constituent':34s} {'iso weight':>10s}   NC push on the electron          vs handed throw (against spin)")
for k,v in iso.items():
    d = 'ALONG its spin' if v>0 else 'AGAINST its spin'
    same = 'OPPOSITE' if v>0 else 'SAME, x2'
    print(f"{k:34s} {v:+10d}   {d:32s} {same}")
print("\nConsequence for route (a): a capture-and-re-eject of the passing electron by the ejection rule throws it AGAINST its")
print("spin every time. That can be the linear-oscillator event (same sign, double weight) but it CANNOT be the bare-core event,")
print("whose push is ALONG the spin. The bare-core event is a different act, or the bare-core weight is what remains when the")
print("handed event is REMOVED: with a uniform handed contribution -1 per constituent removed from both, the residual is")
print("core: +1 - (-1) = +2 ... no integer pattern survives that; so the bare-core event is genuinely opposite-signed.")

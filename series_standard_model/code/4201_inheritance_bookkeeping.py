#!/usr/bin/env python3
"""4201 -- angular-momentum bookkeeping of the founder's inheritance picture (founders_voice/4201_*).
Down quark = +qCP core + orbital DP of sense s (units of hbar/2 as +1/-1). The escaping -eCP TAKES that
DP (electron spin = s). The bare core refills from the Sea with a DP of sense s_new; an adjacent Sea DP
is left with -s_new and is the (anti)neutrino.  Ejection rule (4199, relocated): a lepton of label q
leaves along q * (its own spin)."""
for s in (+1,):
    print(f"down-quark orbital sense s = {s:+d};  electron takes it -> A_e = {s:+d}")
    print(f"{'refill sense':>13s} {'up quark':>9s} {'antineutrino':>13s} {'total after':>12s} {'lepton pair':>12s} {'channel':>8s}   v_e   v_nubar")
    for s_new in (+1, -1):
        A_nu = -s_new
        total = s + s_new + A_nu
        pair = 'singlet' if A_nu == -s else 'triplet'
        ch = 'Fermi' if pair == 'singlet' else 'GT'
        v_e, v_nu = -s, +A_nu                 # q_e = -1, q_nubar = +1
        print(f"{s_new:+13d} {s_new:+9d} {A_nu:+13d} {total:+12d} {pair:>12s} {ch:>8s}   {v_e:+d}     {v_nu:+d}")
print("\nFermi row: electron and antineutrino leave the same way (a = +1, measured).")
print("GT row: opposite ways for this spin axis; the measured GT correlation is a = -1/3 (three orientations averaged).")
print("Angular momentum: total after = total before in both rows. One neutral lepton per decay, as measured.")

#!/usr/bin/env python3
"""4246 -- TODO-4235-NC-ISOSPIN: the founder's 4240 picture applied to the neutral-current scene, channel by channel.
Objects (all on file): the W0 centroid holds ONE captured -eCP (SF-2 Def. activated W0: "one +-eCP at the centroid");
it captures any CP in a non-zero-gradient host -- a free electron's -eCP or a quark's linear -eCP (Prop. capture);
founder 4240: passage is carried by inertia, the two -eCPs leave the centroid region in a mixed state that resolves
in each interaction; the NC event is elastic, so at a down quark ONE -eCP must stay as its linear oscillator.
Channels for a passing electron e beside a constituent:
  DIRECT   : e transits the centroid and leaves; the constituent is untouched.       amplitude  T_dir
  EXCHANGE : the resident -eCP leaves as the outgoing electron; e takes its place.   amplitude -T_ex (identical fermions)
The PV push is the INTERFERENCE of the event amplitude with photon exchange, so it carries the amplitude's sign;
beta-decay helicity (the ONESIGN primitive) is |T|^2 and does not fix that sign -- see the last block."""
phi=(1+5**.5)/2; s2=3/(8*phi)
def iso(occupied, blocked=True, Tdir=1.0, Tex=1.0):
    direct = 0.0 if (occupied and blocked) else Tdir
    exch   = -Tex if occupied else 0.0
    return direct+exch
print("channel table (push along the electron's spin = +)")
print(f"  bare +qCP core (u):  direct {+1:+d}, exchange none           -> iso {iso(False):+.0f}")
print(f"  down quark (d):      direct blocked (centroid holds its linear -eCP, capacity one), exchange {-1:+d} -> iso {iso(True):+.0f}")
print(f"  per constituent:     core {iso(False):+.0f};  linear = d - core = {iso(True)-iso(False):+.0f}   (4235 target: +1, -2)")
print(f"  in units of the bare-core event: the MAGNITUDES and the u/d RELATIVE sign follow; the bare-core sign itself is an input here.")
print("\nwhat each alternative would give (why each premise is load-bearing)")
print(f"  direct NOT blocked at d (capacity > 1):           d iso = {iso(True,blocked=False):+.0f}   (needs -1)")
print(f"  exchange without the fermion sign (bosonic -eCPs): d iso = {0+1:+.0f}   (needs -1)")
for f in [1.0,0.99,0.9]:
    print(f"  d's centroid occupied a fraction f = {f:.2f} of formations: d iso = {(1-f)*1 + f*(-1):+.2f}")
print("\nwith the derived EM part (-4 Q s^2, s^2 = 3/(8 phi)), tree level:")
QWu=iso(False)-4*(2/3)*s2; QWd=iso(True)-4*(-1/3)*s2
print(f"  Q_W(u) = {QWu:+.4f}  Q_W(d) = {QWd:+.4f}  proton = {2*QWu+QWd:+.4f}  neutron = {QWu+2*QWd:+.4f}")
Z,N=55,78; print(f"  Cs-133: Z Q_W(p) + N Q_W(n) = {Z*(2*QWu+QWd)+N*(QWu+2*QWd):+.2f}   (measured -72.6 as used at 4216; tree level, no radiative corrections)")
print("\nsub-leading, bounded not claimed: an up quark's orbital-eDP pole sits in the centroid pocket 1.2e-3 of the time (4231);")
print("if that pole counted as a resident -eCP, u iso = 1 - 2(1.2e-3) = %.4f. It is half of a neutral eDP, not a bare -eCP; not applied." % (1-2*1.2e-3))
print("\nthe bare-core SIGN, two readings:")
print("  (R1) 4216's displacement reading (NC = a push rule with the CC's q): the exchange channel IS the CC act -- the W0 releases")
print("       the resident -eCP, which leaves AGAINST its spin (primitive, 4201) -- and 4216 found the captured object carries the CC")
print("       sign in both currents. The direct channel is its fermion-exchange partner: ALONG. All signs + magnitudes then follow from")
print("       one primitive + capacity one + Fermi statistics. Load-bearing step: applying the exchange sign to a push weight.")
print("  (R2) amplitude reading: beta helicity is |T|^2; the NC push is 2 Re(A_gamma* T_dir), so the bare-core sign needs the phase of")
print("       the direct transit relative to photon exchange. Founder 4240 element 3 (the W0 holds the arc energy one Moment) is a delay,")
print("       i.e. a phase -- the candidate carrier. Owed: TODO-4246-NCPHASE.")

#!/usr/bin/env python3
"""4224 -- the pair state of 4223 read back in inheritance bookkeeping: for a neutron of spin +s, which
final spin configuration (proton, electron, antineutrino) occurs with what probability, and what the naive
inheritance bookkeeping (electron keeps the quark's sense s; antineutrino counter to the refill) can and
cannot produce.  Pair state (4223): |p+>[ |S> + lam |T0> ] + |p-> [ -sqrt2 lam |T+1> ],  S = (ud - du)/sqrt2,
T0 = (ud + du)/sqrt2, T+1 = uu ; 'u' = along s.  Amplitudes for product configurations follow."""
import numpy as np
lam = -1.2754
amp = {  # (proton, electron, nubar)
 ('+', '+', '-'): (1 + lam)/np.sqrt(2),     # p unchanged, e keeps s, nubar against s  <- the naive inheritance event
 ('+', '-', '+'): (lam - 1)/np.sqrt(2),     # p unchanged, e REVERSED, nubar along s
 ('-', '+', '+'): -np.sqrt(2)*lam,          # p flipped, both leptons along s
}
Z = sum(abs(a)**2 for a in amp.values()); assert abs(Z - (1 + 3*lam**2)) < 1e-12
print(f"lambda = {lam};  1 + 3 lambda^2 = {Z:.4f}\n")
print(f"{'final (p, e, nubar) along s':32s} {'amplitude':>10s} {'probability':>12s}   naive inheritance (e = s, nubar = -refill) can make it?")
notes = {('+','+','-'): 'YES: same-sense refill, everything as pictured',
         ('+','-','+'): 'NO: electron reversed; nubar PARALLEL to the refill sense',
         ('-','+','+'): 'YES: opposite-sense refill, electron keeps s'}
for k, a in amp.items():
    print(f"{'p'+k[0]+'  e'+k[1]+'  nubar'+k[2]:32s} {a:+10.4f} {abs(a)**2/Z:12.4f}   {notes[k]}")
pe = (abs(amp[('+','+','-')])**2 + abs(amp[('-','+','+')])**2 - abs(amp[('+','-','+')])**2)/Z
pn = (-abs(amp[('+','+','-')])**2 + abs(amp[('-','+','+')])**2 + abs(amp[('+','-','+')])**2)/Z
pp = (abs(amp[('+','+','-')])**2 + abs(amp[('+','-','+')])**2 - abs(amp[('-','+','+')])**2)/Z
print(f"\nspin along s carried out (neutron fully polarised):   <sigma_e> = {pe:+.3f}   <sigma_nubar> = {pn:+.3f}   <sigma_p> = {pp:+.3f}")
print(f"check against 4223's coefficients:  -A = {pe:+.3f} (A = -0.119),  B = {pn:+.3f} (B = +0.987)")
print(f"proton flips in {abs(amp[('-','+','+')])**2/Z:.1%} of decays; the electron leaves against the quark's sense in {abs(amp[('+','-','+')])**2/Z:.1%}")
print(f"the naive inheritance event (proton unchanged, electron keeps s, antineutrino counter) is {abs(amp[('+','+','-')])**2/Z:.2%} of decays:")
print(f"   its amplitude is (1 + lambda)/sqrt2 = {(1+lam)/np.sqrt(2):+.3f} -- the same-sense and opposite-sense amplitudes nearly CANCEL there.")
print("\nSame table at lambda = +1.2754 (in-phase), for contrast:")
for l in (+1.2754,):
    Z2 = 1+3*l*l
    for k, f in ((('+','+','-'), (1+l)/np.sqrt(2)), (('+','-','+'), (l-1)/np.sqrt(2)), (('-','+','+'), -np.sqrt(2)*l)):
        print(f"   {'p'+k[0]+'  e'+k[1]+'  nubar'+k[2]:28s} {abs(f)**2/Z2:8.4f}")

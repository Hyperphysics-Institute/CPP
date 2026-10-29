"""Patch 4449 (rebuilt after HOLD) -- founder: the CP swings at a steady rate millions of times while emitting, the count adding up
to the energy (he now doubts it); proposes instead a single burst over a half-wave discharge of the orbital DP reservoir.

Part 1. The steady swing as an energy sum (the quantitative form of his first picture; 4445 part 4): a charge swinging at Delta E / h
        with hydrogen's measured strength radiates with lifetime 1.6 ns; each swing gives up 1/(f tau) ~ 2.5e-7 of what remains (about
        2.6 micro-eV at first, less later); about 4e6 swings per lifetime release 63%; the sum over the whole decay is Delta E.
Part 2. A half-wave burst is shorter than 4448's one-cycle photon, so its colour spread is broader still (at least 1/3 to 1/2).
Part 3. Light vs the orbits' classical revolution rates.  For one-level jumps (n+1 -> n) the light lies between the two orbits'
        rates (proof: f/(Ry/h) = (2n+1)/(n^2 (n+1)^2) lies between 2/(n+1)^3 and 2/n^3).  This follows from a smooth E_n ~ -1/n^2
        (mean value theorem: Delta E / h = Delta n x f_rev(n*) for some n* in between); it is the correspondence principle, not a
        clue to a joint mechanism.  For larger jumps the light tends to the Delta n-th harmonic and can exceed both (6->3, 7->5).
Part 4. Targets for his reservoir discharge: exponential drain (energy loss in proportion to what is left; Lorentzian line of width
        1/(2 pi tau)), a steady swing rate while the amplitude decays, a per-swing share 1/(f tau) of what remains.
"""
import numpy as np
Ry_h, eV, h = 3.2898e15, 1.602e-19, 6.626e-34
f_rev = lambda n: 2*Ry_h/n**3
fL, tau, dE = 2.467e15, 1.596e-9, 10.2
N = fL*tau
print(f"Part 1  per-swing share 1/(f tau) = {1/N:.2e} of what remains: {dE/N*1e6:.1f} micro-eV at first; {N:.1e} swings per lifetime release {1-np.exp(-1):.0%}; total over the decay {dE} eV (= h f)")
print(f"Part 2  half-wave burst: shorter than one cycle, colour spread broader than ~{1/np.pi:.2f} of itself (atomic lines ~4e-8)")
print("Part 3  transition: orbit-left rate | light | orbit-entered rate | light / orbit-entered")
for nu, nl in ((2, 1), (3, 2), (10, 9), (100, 99), (3, 1), (6, 3), (6, 4), (7, 5), (10, 3)):
    fl = Ry_h*(1/nl**2 - 1/nu**2)
    tag = "between" if f_rev(nu) < fl < f_rev(nl) else "NOT between"
    print(f"        {nu:>3} -> {nl:<3}: {f_rev(nu):.3e} | {fl:.3e} | {f_rev(nl):.3e} | {fl/f_rev(nl):.3f}  ({tag}; jump of {nu-nl})")
ok = all(f_rev(n+1) < Ry_h*(1/n**2 - 1/(n+1)**2) < f_rev(n) for n in range(1, 2001))
print(f"        one-level jumps n = 1..2000 all between: {ok}")
print(f"Part 4  exponential drain: after tau, {np.exp(-1):.3f} of the energy left; linewidth 1/(2 pi tau) = {1/(2*np.pi*tau):.1e} Hz; "
      f"rate steady to {1/(2*np.pi*tau)/fL:.0e}; per-swing share {1/N:.1e} of what remains")

"""Patch 4475 -- founder: the energy stored in the upper orbital lives in its DP-arc cloud; when the electron CP drops to the
lower orbital, the cloud still holds the upper energy; the part no longer sustained by the CP's give-and-take (the difference
between the two orbitals) must be shed, while the lower orbital's share drops down and is sustained.

Checks (standard numbers; toy signals, not CPP dynamics):
Part 1 -- the rhythms available in hydrogen (n = 2 -> 1): each orbital's revolution rate, each orbital's energy / h, and the
          line, Delta E / h.  Shedding at either orbital's own rhythm gives the wrong colour.
Part 2 -- a cloud holding a fading upper share (amplitude a_up = exp(-t/2tau)) at rhythm f_up and a lower share at rhythm f_low,
          in two sequences: (i) his: the CP drops first, so the lower share is fully present from the start (a_low = 1) while the
          unsustained excess fades; (ii) a gradual hand-over (a_low = sqrt(1 - exp(-t/tau))).  The cross term (what an overlap of the
          two does in the standard picture, 4460 5) runs at f_up - f_low at every moment, however the mixture changes; its strength
          follows a_up x a_low.  Measured: the rate of the cross term through the emission; where its strength peaks; and a
          constant added to both rhythms (an energy zero) drops out.
          Part 2 confirms an identity for fixed rhythms (cross = 2 a_up a_low cos 2 pi (f_up - f_low) t); it is not a test of
          whether the rhythms stay fixed.  The fading is imposed, not self-consistent (in self-consistent semiclassical theory
          the pulse is hyperbolic-secant shaped).
"""
import numpy as np
h = 4.135667696e-15      # eV s
Ry = 13.605693           # eV
f_rev = lambda n: 2*Ry/(h*n**3)     # Bohr revolution rate
f_E = lambda n: Ry/(h*n**2)         # binding energy / h
dE = Ry*(1-1/4)
print("Part 1: hydrogen rhythms (Hz)")
print(f"  revolution rate:   n=2 {f_rev(2):.3e}, n=1 {f_rev(1):.3e}")
print(f"  binding energy/h:  n=2 {f_E(2):.3e}, n=1 {f_E(1):.3e}")
print(f"  line, Delta E/h:   {dE/h:.4e}  (= difference of the energy rhythms: {f_E(1)-f_E(2):.4e})")
print(f"  shedding at the upper orbital's rhythm would give {f_E(2)/(dE/h):.2f} x the colour; at the lower's, {f_E(1)/(dE/h):.2f} x")

print("Part 2: two rhythms in one fading cloud (toy units: f_up = 13, f_low = 10, line = 3; tau = 40 line periods)")
fs = 400; tau = 40/3
t = np.arange(0, 6*tau, 1/fs)
for seq, offset in (("his sequence (lower share full from the drop)", 0.0), ("his sequence", 1000.0),
                    ("gradual hand-over", 0.0), ("gradual hand-over", 1000.0)):
    fu, fl = 13+offset, 10+offset
    a_up = np.exp(-t/(2*tau))
    a_lo = np.ones_like(t) if seq.startswith("his") else np.sqrt(1-np.exp(-t/tau))
    psi = a_up*np.exp(-2j*np.pi*fu*t) + a_lo*np.exp(-2j*np.pi*fl*t)
    dens = np.abs(psi)**2                                   # what the overlap does: |psi|^2
    cross = dens - a_up**2 - a_lo**2                        # = 2 a_up a_lo cos(2 pi (fu-fl) t)
    m = (a_up*a_lo) > 1e-3
    i = np.where(m[:-1] & m[1:] & (cross[:-1]*cross[1:] < 0))[0]
    zc = t[i] - cross[i]*(t[i+1]-t[i])/(cross[i+1]-cross[i])   # interpolated zero crossings
    per = 2*np.diff(zc)
    print(f"  {seq}, energy zero shifted by {offset:>6}: cross-term rate from zero crossings: mean {1/np.mean(per):.6f}, spread {np.std(1/per):.1e} (line = 3)")
    st = a_up*a_lo
    print(f"     strength (a_up x a_low) peaks at t = {t[np.argmax(st)]/tau:.2f} tau; at t = 0 it is {st[0]:.2f}; from 2 tau to 4 tau it falls by e^{np.log(st[int(2*tau*fs)]/st[int(4*tau*fs)]):.2f}")

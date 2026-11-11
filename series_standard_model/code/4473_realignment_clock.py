"""Patch 4473 -- founder: after the collision, the DP-arc cloud loses its organizing CP and begins to collapse; on each discharge cycle a
portion of the arcs, aligned with the photon's direction, discharges; the forces between DPs then change, realigning the arcs and making a new
increment available; repeated increments of the same energy and duration give repeated waves of the same colour, a narrow line.

Toy model (not CPP dynamics): the stored energy drains over N cycles (exponential, as measured), and the time to realign for the next increment
depends on what is left: period T = T0 x (E/E0)^(-p).  p = 0: a fixed realignment time (a clock); p > 0: realignment slows as the cloud empties;
p < 0: it speeds up (as the Coulomb-timed swing of 4460 5 does); either sign smears the line.  The emitted wave has phase advancing by one cycle per realignment; its spectrum's half-power width (share of the starting
frequency) is printed, against the width from the fading alone (p = 0).
Also: the energy per increment -- fixed increments (a flat envelope that stops after N cycles) versus a share of what is left (exponential),
cf. 4451 3, 4461 3.2: the largest side lobe of each spectrum, relative to the peak, is printed (flat: ~0.047; exponential: none).
"""
import numpy as np
Ncyc = 2000                       # cycles over which the energy falls to 1/e (toy; a real photon ~ millions)
fs = 32                           # samples per starting period
tmax = 6*Ncyc                     # in starting periods
t = np.arange(0, tmax, 1/fs)
E = np.exp(-t/Ncyc)               # energy left
def width(sig):
    S = np.abs(np.fft.rfft(sig, n=4*sig.size))**2
    f = np.fft.rfftfreq(4*sig.size, 1/fs)
    m = (f > 0.2) & (f < 3)
    S, f = S[m], f[m]
    h = f[S >= S.max()/2]
    return h.max() - h.min(), f[np.argmax(S)]
amp = np.sqrt(E)                  # field amplitude ~ sqrt(energy)
for p in (0.0, 1e-4, 1e-3, 1e-2, 0.5, 1.5, -1e-3):
    rate = E**p                   # cycles per starting period (period grows as E^-p)
    phase = 2*np.pi*np.cumsum(rate)/fs
    w, fpk = width(amp*np.cos(phase))
    print(f"p = {p:<6}: half-power width {w:.1e} of the starting frequency (peak at {fpk:.3f}); fading alone gives 1/(2 pi N) = {1/(2*np.pi*Ncyc):.1e}")
# tolerance for a real Lyman-alpha photon: over one e-fold of energy the rate shifts by ~p; it must stay within the natural width 1/(2 pi N)
Nreal = 3.9e6
print(f"Real Lyman-alpha (N ~ {Nreal:.1e} cycles): a realignment time depending on the energy left as E^-p must have |p| of order {1/(2*np.pi*Nreal):.0e} or less (at that value the line is already roughly doubled)")
# fixed increments (flat envelope stopping at N cycles) versus shares of what is left (exponential)
def largest_side_lobe(sig):
    n = 16*sig.size
    S = np.abs(np.fft.fft(sig, n=n))**2      # complex (one-sided) wave, so no mirror-image term
    f = np.fft.fftfreq(n, 1/fs)
    m = (f > 0.5) & (f < 1.5)
    S, f = S[m], f[m]
    k = np.argmax(S)
    # walk down from the peak to the first minimum on the high side, then take the largest value beyond it
    j = k
    while j+1 < S.size and S[j+1] < S[j]:
        j += 1
    return S[j:].max()/S[k]
tt = np.arange(0, 3000, 1/fs)     # short toy so the lobes are resolved: N = 50 cycles; long window so the exponential tail is complete
flat = np.where(tt < 50, 1.0, 0.0)*np.exp(2j*np.pi*tt)
expo = np.exp(-tt/(2*50))*np.exp(2j*np.pi*tt)   # amplitude e-folds over 2N, energy over N
print(f"Equal increments (flat envelope, stops at N cycles): largest side lobe {largest_side_lobe(flat):.3f} of the peak (cf. 4451's ~0.047)")
print(f"Shares of what is left (exponential fading): largest side lobe {largest_side_lobe(expo):.1e} of the peak (numerical floor: no side lobes, a smooth Lorentzian)")

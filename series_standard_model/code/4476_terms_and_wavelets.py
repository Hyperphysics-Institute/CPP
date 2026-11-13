"""Patch 4476 -- founder: orbitals are made of ZBW oscillations (the indivisible unit, hbar); each orbital may have its own
frequency, beating against the other; the colour is not the orbital speed; every wavelet must diffract like the whole photon,
which seems to contradict E = hf.

Part 1 -- sum or difference: the two orbitals' rhythms (energy / h, zero at ionisation; and with rest energy) added and
          subtracted, against Lyman-alpha.
Part 2 -- the Ritz combination principle with measured vacuum wavelengths (NIST, fine-structure-averaged, rounded):
          every line is a difference of two "terms", one per level, so f(3->1) = f(3->2) + f(2->1).
Part 3 -- the factor of two: if each level's rhythm is 2E/h (Dirac's ZBW rate) instead of E/h, the difference is twice the colour.
Part 4 -- a grating sorts crest spacing, not energy per crest: the diffraction angle of a train of crests at spacing lambda is
          the same for any amplitude (scaled by 1e-6 or 1): the peak angle is printed for both.
"""
import numpy as np
h = 4.135667696e-15; c = 2.99792458e8; Ry = 13.605693; mc2 = 510998.95
E = lambda n: -Ry/n**2
lya = (E(2)-E(1))/h
print("Part 1: sum or difference (Hz)")
for label, z in (("zero at ionisation", 0.0), ("rest energy included", mc2)):
    fu, fl = (z+E(2))/h, (z+E(1))/h
    print(f"  {label}: upper {fu:.6e}, lower {fl:.6e}; difference {fu-fl:.4e} ({(fu-fl)/lya:.3f} x Ly-a); sum {abs(fu+fl):.4e} in size ({abs(fu+fl)/lya:.3g} x Ly-a)")
print("Part 2: Ritz combination from measured vacuum wavelengths")
lam = {"Ly-a (2->1)": 121.567e-9, "Ly-b (3->1)": 102.5722e-9, "H-a (3->2)": 656.461e-9}
f = {k: c/v for k, v in lam.items()}
for k, v in f.items(): print(f"  {k}: {v/1e12:.3f} THz")
s = f["Ly-a (2->1)"] + f["H-a (3->2)"]
print(f"  f(2->1) + f(3->2) = {s/1e12:.3f} THz vs f(3->1) = {f['Ly-b (3->1)']/1e12:.3f} THz; relative difference {abs(s-f['Ly-b (3->1)'])/s:.1e}")
print("Part 3: rhythm 2E/h per level gives a difference of", f"{2*(E(2)-E(1))/h/lya:.0f} x Ly-a")
print("Part 4: grating (1200 lines/mm, first order) for a 2,000-crest train at 500 nm (toy)")
lam0 = 500e-9; d = 1e-3/1200
x = np.arange(0, 2000*lam0, lam0/40)
for amp in (1.0, 1e-6):
    field = amp*np.cos(2*np.pi*x/lam0)
    # the grating equation picks the angle where the path step d sin(theta) is one crest spacing; find the train's crest spacing from its spectrum
    F = np.abs(np.fft.rfft(field, n=8*x.size)); k = np.fft.rfftfreq(8*x.size, x[1]-x[0])
    lam_peak = 1/k[np.argmax(F)]
    print(f"  amplitude {amp:g}: crest spacing found {lam_peak*1e9:.3f} nm -> first-order angle {np.degrees(np.arcsin(lam_peak/d)):.4f} deg")

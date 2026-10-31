"""Patch 4456 -- founder: action per cycle is not fixed (except for the smallest single-increment displacement); larger displacement per Moment
means more action; the in-and-out propagation rate of the displacement sets the colour and changes with energy; in phase synchrony it forms a
pattern fixed along the photon's length, like a radio wave's.

Two measured constraints any internal picture must meet:
Part 1. Same colour, same energy.  Each photon's energy is h f, whatever its source or packet: single-photon calorimeters (transition-edge
        sensors, e.g. Cabrera et al. 1998, ~0.15 eV resolution; X-ray microcalorimeters ~2 eV at 6 keV) give one energy for one colour,
        within their resolution.  ILLUSTRATIVE (energy taken linear in displacement): if the action per cycle grew with the displacement
        independently of the rate, photons of one colour would come in a spread of energies.
Part 2. Every colour travels at the same speed.  Fermi's GRB 090510 (Abdo et al. 2009): photons from ~10 keV to 31 GeV, after ~7 billion
        years of travel, the 31 GeV photon 0.829 s after the trigger.  Fractional speed difference a few parts in 1e18 (assuming emission
        together; gamma-ray energies; lower energies rest on other evidence, e.g. lambda and f measured separately agreeing on c).
Part 3. A floor test for a smallest single increment: photons are seen with no lower cutoff (radio, extremely low frequency); and h per
        Moment would be a Planck-scale energy if the Moment is near the Planck time (the Moment's size is not fixed here).
"""
h, eV = 6.62607015e-34, 1.602176634e-19
f = 5.0e14
print(f"Part 1  photons at {f:.1e} Hz: energy h f = {h*f/eV:.4f} eV each, every time")
for scale in (1.5, 2.0):
    print(f"        if action per cycle grew with displacement (x{scale}) at the same rate: energy {scale*h*f/eV:.4f} eV  <- not seen")
yr = 3.156e7
T = 7.3e9*yr           # light-travel time, approximate
dt = 0.829             # 31 GeV photon's arrival after the trigger, s (Abdo et al. 2009)
print(f"Part 2  travel time ~{T:.1e} s; arrival spread < ~{dt} s; fractional speed difference < ~{dt/T:.0e}")
for name, fr in (("FM radio 100 MHz", 1e8), ("AM radio 1 MHz", 1e6), ("ELF 3 Hz", 3.0)):
    print(f"Part 3  {name}: photon energy {h*fr/eV:.1e} eV")
tP = 5.391e-44
print(f"        h per Planck time: {h/tP/eV:.1e} eV (a Planck-scale energy)")

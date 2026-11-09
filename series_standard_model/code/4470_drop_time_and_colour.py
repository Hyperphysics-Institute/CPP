"""Patch 4470 -- founder: a lower-energy photon comes from a longer shell drop, the drop time corresponding to the frequency (a faster drop is a
higher-velocity cohort, more DP-arc polarization), with a collective eigenmode of the cohort giving a correspondingly narrow line.

Part 1. If the drop time set the colour (f = 1/drop time), what colour would each measured upper-level lifetime give, against the measured line?
Part 2. The other split: the colour is the cohort's ringing rate (an eigenmode), the drop's duration is how long it rings.  Cycles per photon
        = f x upper lifetime (the upper level's emission envelope only).  The natural width uses both levels' decay rates,
        (Gamma_upper + Gamma_lower) / (2 pi): for Balmer-alpha from 3s and 3d the lower level is 2p (1.596 ns), which dominates; from 3p the
        lower level is 2s (metastable, ~0).
Lifetimes (standard values): H 2p 1.596 ns; H 3p 5.27 ns, 3d 15.6 ns, 3s 158 ns; H 1s hyperfine (21 cm): A = 2.87e-15 /s (~11 Myr; formal --
in the interstellar medium collisions and Doppler motion dominate the observed width).  The Balmer-alpha routes differ in colour only by fine
structure, up to ~10 GHz (~2e-5 of the frequency).
"""
import numpy as np
yr = 3.156e7
G2p = 1/1.596e-9
rows = (("Lyman-alpha (2p -> 1s)", 2.466e15, 1.596e-9, 0.0),
        ("Balmer-alpha 3p -> 2s", 4.568e14, 5.27e-9, 0.0),
        ("Balmer-alpha 3d -> 2p", 4.568e14, 15.6e-9, G2p),
        ("Balmer-alpha 3s -> 2p", 4.568e14, 158e-9, G2p),
        ("21 cm (hyperfine)", 1.4204e9, 1/2.87e-15, 0.0))
for name, f, tau, Glow in rows:
    life = f"{tau/yr/1e6:.0f} million years" if tau > 1e6 else f"{tau*1e9:.3g} ns"
    w_up = 1/(2*np.pi*tau); w_both = (1/tau + Glow)/(2*np.pi)
    print(f"{name:24s} line {f:.3e} Hz, upper lifetime {life}; 1/tau = {1/tau:.1e} Hz (misses by {f*tau:.0e}x); "
          f"cycles f*tau = {f*tau:.1e}; natural width: upper only {w_up:.1e} Hz, both levels {w_both:.1e} Hz ({w_both/f:.1e} of f)")

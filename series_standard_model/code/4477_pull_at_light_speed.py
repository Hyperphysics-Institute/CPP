"""Patch 4477 -- founder: the whole photon lands in one place because, when one part of the DP-arc 'bubble' is pricked by an
absorber, the rest of the photon follows down into that place, the parts arriving at different times, with any coordination
travelling at light speed.

Test (standard numbers): a single photon split by a beam splitter to two detectors ~10 m apart (Guerreiro et al. 2012).
If the pull from a click at A travels at c, it reaches B only after the light time A->B.  If B's half of the train has already
passed B by then, B acts on its own half and the two detectors act independently: coincidences at about the uncorrelated
rate, P_AB / (P_A P_B) ~ 1.  Measured (spacelike configuration): ~1.2e-3.  The decisive point is timing: each click comes within ~1 ns of arrival.
"""
c = 2.99792458e8
sep = 10.0                       # m, detector separation (approx.)
t_light = sep/c
trains = {"Lyman-alpha photon (1.6 ns lifetime)": 1.596e-9,
          "visible atomic photon (10 ns lifetime, typical)": 10e-9,
          "heralded photon, ~1 ps (illustrative; the paper does not state a coherence time)": 1e-12}
print(f"light time between detectors {sep:.0f} m apart: {t_light*1e9:.1f} ns")
for k, tau in trains.items():
    print(f"  {k}: train passes a detector in ~{tau*1e9:.3g} ns ({c*tau:.3g} m long); "
          f"pull from A arrives {t_light/tau:.3g} train-durations after B's half has passed")
print("Light-speed pull, independent halves: P_AB/(P_A P_B) ~ 1 (classical-wave level; Grangier's limit alpha >= 1)")
# Guerreiro et al. 2012, Table I: P(1,1), P_A, P_B
sp = 2.3e-7/(1.703e-2*1.090e-2); tl = 2.2e-7/(1.616e-2*1.019e-2)
print(f"Measured (Guerreiro et al. 2012, Table I): spacelike P_AB/(P_A P_B) = {sp:.2e}; timelike control {tl:.2e} (each +-~50%, 4 +- 2 counts per 30 min)")
print(f"Independent halves would give ~1: about {1/sp:.0f}x too many coincidences")
print(f"Click timing: coincidence window 1 ns, detector jitter 0.4 ns, against {t_light*1e9:.0f} ns for anything travelling at c between detectors")

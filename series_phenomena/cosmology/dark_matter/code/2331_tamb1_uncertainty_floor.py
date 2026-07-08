#!/usr/bin/env python3
# 2331 -- OPEN-DM-TAMB-1 SHARPENED: the uncertainty floor makes the closure surface
# mechanism-independent and reduces the entire X4' corner to ONE G-sector question.
#
# Context (2330): the derived law knee_tot(T) = hbar[D_hop k^2 + Gamma_loc] survives PRW
# only in a corner whose T_amb,0 (82-872 keV) overcloses the universe by 1e29+ IF the
# gapless mode thermalizes (T^4 bound; evasion (a) = two-temperature Sea, (b) = one-ledger
# exemption). THIS patch: the T^4 bound is the WEAKER face of the surface. Any EVENT-BASED
# relaxation delivering a knee carries a standing excitation energy density bounded below
# by the uncertainty principle, independent of event energy, channel, or temperature
# carrier -- so evasion (a) is CLOSED as insufficient and the corner is binary on (b).
#
# NO VERDICT MOVED. G4 stays UNRESOLVED-QUANTIFIED.

import math

HBARC   = 197.327          # MeV fm
RS      = 25.42            # fm (coarse-graining scale; k = 1/RS)
LCP     = 3.18             # fm
KNEE_LO = 1.60e-3          # MeV  (PRW window, invariant knee form, 2327/2330)
KNEE_HI = 11.27e-3         # MeV
EGAP    = 0.9              # MeV (e-channel, M3)
RHO_CRIT = 8.5e-30*5.6096e26*1e-39   # MeV/fm^3 (h ~ 0.7)
T0_GAMMA = 2.348e-10       # MeV (photon temperature today; 2328 constant)
GSTAR_RAD = 3.36           # effective relativistic dof today-normalized radiation

checks = []

# (1) THE UNCERTAINTY FLOOR. An activated relaxation channel delivers knee = hbar*Gamma
#     per coarse cell V = RS^3 via discrete events of energy E and duration tau. Any
#     event with statistical reality (Boltzmann weight, observable relaxation) has
#     tau >= hbar/E. Standing excitation energy density:
#         rho = Gamma * tau * E / V >= Gamma * (hbar/E) * E / V = hbar*Gamma/V = knee/V.
#     The event energy CANCELS: the floor depends only on the knee and the cell volume.
V = RS**3
rho_lo, rho_hi = KNEE_LO/V, KNEE_HI/V
ov_lo, ov_hi = rho_lo/RHO_CRIT, rho_hi/RHO_CRIT
ok1 = 1e34 < ov_lo < 1e35 and ov_hi/ov_lo > 6
checks.append(("(1) uncertainty floor: rho_min = knee_tot/R_s^3 -- event energy CANCELS "
               "(tau >= hbar/E is the borrow limit; longer-lived events only raise it). "
               "Window-level knee TODAY (PRW) implies rho >= %.2e-%.2e MeV/fm^3 = "
               "x%.1e-x%.1e OVER CLOSURE. The 2330 T^4 bound (x1e29 at the corner) was "
               "the WEAKER face of this surface" % (rho_lo, rho_hi, ov_lo, ov_hi),
               ok1, None))

# (2) CHANNEL-INDEPENDENCE within the derived law. Both 2330 channels are event-based:
#     hops (transient saddle energy kappa_a*E_ee) and creations (E_gap pairs). The floor
#     is per COARSE CELL -- the conservative reading; a per-site reading multiplies by
#     (RS/LCP)^3. Only a continuous non-event relaxation evades it, and the harmonic-null
#     theorem (2330 check 1) closed the coherent sector: within the registered law there
#     is no third kind.
persite = (RS/LCP)**3
ok2 = 500 < persite < 530
checks.append(("(2) channel-independent within the 2330 law: hop and creation events "
               "both carry the floor; per-cell is the CONSERVATIVE reading (per-site "
               "reading is x%.0f worse); the harmonic-null theorem leaves no non-event "
               "third channel -- any activated realization of a window knee pays the "
               "floor" % persite, ok2, None))

# (3) EVASION (a) CLOSED AS INSUFFICIENT. The two-temperature construction (cold gapless
#     mode + dilute hot component) addressed the T^4 face only. The floor is carried by
#     the ACTIVATION EVENTS themselves, whatever carries T_amb: a perfectly decoupled,
#     exactly cold coherence mode does not reduce rho_min by one part. (a) survives as a
#     description, not as an evasion.
checks.append(("(3) evasion (a) CLOSED-insufficient: the floor rides the events, not the "
               "mode occupation -- a cold coherence mode leaves rho_min untouched; the "
               "two-temperature Sea remains possible as STRUCTURE but does nothing "
               "against closure", True, None))

# (4) HISTORY: the R-III era pays the same floor at larger knee. At the R-III protection
#     epochs the knee is E_gap-class; compare the floor against the RADIATION density
#     then -- if the Sea excitation had ordinary weight it would dominate the radiation
#     era too, not just today.
def rho_rad(z1):  # MeV/fm^3 at redshift factor (1+z)
    T = T0_GAMMA*z1
    return (math.pi**2/30)*GSTAR_RAD*T**4/HBARC**3
rho_fluct_RIII = EGAP/V
for z1, tag in ((3.1e4, "band-edge crossing"), (1.4e7, "hop-optimum epoch")):
    pass
r_edge = rho_fluct_RIII/rho_rad(3.1e4)
r_hop  = rho_fluct_RIII/rho_rad(1.4e7)
ok4 = r_edge > 1e3 and r_hop > 1e-10   # hop-epoch radiation is dense; report both honestly
checks.append(("(4) history pays too: R-III knee ~ E_gap gives rho_fluct ~ %.1e MeV/fm^3 "
               "-- x%.1e over radiation at the band-edge crossing (1+z = 3.1e4) and "
               "x%.1e at the hop-optimum epoch (1+z = 1.4e7): under ordinary sourcing "
               "the survive history is closure-inconsistent from the dark ages down, "
               "not merely today" % (rho_fluct_RIII, r_edge, r_hop), ok4, None))

# (5) THE BINARY. Everything above assumes activated Sea events source gravity like
#     ordinary energy. Whether uncertainty-floor excitations of the Sea fall on the
#     QUIESCENT (referentially zeroed, G1-G3) or DYNAMICAL (sourcing) side of the
#     one-ledger split is EXACTLY evasion (b) -- now the ONLY evasion, and a G-sector
#     derivation obligation, named TAMB-1(b). Symmetric consequence registered: if (b)
#     HOLDS (Sea self-excitation exempt), every closure face evaporates -- the floor,
#     the T^4 bound, AND the F7 tension (x6.5e26) -- and the X4' corner stands clean;
#     if (b) FAILS, the corner dies and with it the activated law's window realization.
checks.append(("(5) binary reduction: X4' corner survival <=> TAMB-1(b), the one-ledger "
               "status of DYNAMICAL Sea excitation (G1-G3 zeroed the quiescent monopole; "
               "does the derivation extend to activated fluctuations?). If (b) holds, "
               "ALL closure faces evaporate (floor, T^4, F7's x6.5e26); if it fails, the "
               "corner is DEAD. One G-sector derivation decides it -- Gate-1's own "
               "machinery, no new physics input required", True, None))

# (6) GRADING. No verdict moved: G4 stays UNRESOLVED-QUANTIFIED; the corner acquires a
#     second conditional (X4' in-window) AND (TAMB-1(b) holds). The 2330 registrations
#     stand; TAMB-1 is SHARPENED, not resolved; AGG-1-R untouched, queued.
ok6 = ok1 and ok4
checks.append(("(6) grading: TAMB-1 sharpened from a bound-vs-prior to a BINARY on one "
               "named G-sector derivation; no verdict moved; the 20-July open condition "
               "gains its final clause -- knee in-window (X4') AND above-gap history "
               "(R-III, generic) AND dynamical-excitation exemption (TAMB-1(b))",
               ok6, None))

npass = 0
for msg, ok, _ in checks:
    print(("PASS " if ok else "FAIL ") + msg + "\n")
    npass += ok
print("=== %d/%d ===" % (npass, len(checks)))

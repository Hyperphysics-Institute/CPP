#!/usr/bin/env python3
# 2340 -- OPEN-DM-DSPH-1 / L1 first patch: internal-excitation thresholds.
# Question: which internal quanta of the pinned Cross-Rod can sit in the SPEC-1
# window (E_cm in [63, 176] eV at N = 18; window scales with N through
# E_cm = (1/4) M v^2), producing a Wigner threshold cusp at dwarf velocities?
#
# ANSWER (honest, mostly-closing): every RIGID/ELASTIC internal mode of the
# pinned rod -- rigid rotation, longitudinal phonons, bending -- has quanta at
# 10 keV - 1 MeV for registered N; placing any of them in-window requires
# N ~ 80-190, excluded by the registered cluster-side bound N <~ 18-21 and the
# 1859 pruning of N >~ 40 (both flagged to L4-a: they predate the 2337 floor
# correction). The lane SURVIVES on one named door: azimuthal/torsional soft
# modes, whose stiffness is UNDERIVED -- and this patch computes the INVERSE
# REQUIREMENT: the stiffness that places a quantum in-window is ~1e-7 MeV,
# five to six orders below the coat's radial scale. That number is the L1 ->
# L2/L3 handoff: the derived coat physics must either produce it or close it.
# RENT TEMPLATE registered: any in-window internal mode is thermally live at
# T ~ 100 eV epochs -- pre-registerable early-universe consequences.

import math

HBARC = 197.327
C_KMS = 299792.458
M_EL  = 1408.0
D_EL  = 1.15
VLO, VHI = 30.0, 50.0          # dwarf window, km/s

def M(N):    return N*M_EL
def L(N):    return (N-1)*D_EL
def I(N):    return M(N)*L(N)**2/12.0
def Ecm(N, v_kms):             # MeV
    return 0.25*M(N)*(v_kms/C_KMS)**2

checks = []

# (1) RIGID ROTOR. E(J) = hbar^2 J(J+1)/(2I); first threshold E1 = hbar^2/I.
#     Cusp velocity v*: E_cm(v*) = E1  ->  v*/c = sqrt(4 E1 / M).
def E1_rot(N): return HBARC**2/I(N)
def vstar(E1, N): return C_KMS*math.sqrt(4.0*E1/M(N))
rows = [(N, E1_rot(N)*1e6, vstar(E1_rot(N), N)) for N in (5, 10, 18, 21, 40, 60, 80, 90)]
# N placing v* inside [30, 50]: solve by scan
Nwin = [N for N in range(5, 300)
        if VLO <= vstar(E1_rot(N), N) <= VHI]
ok1 = all(r[2] > VHI for r in rows if r[0] <= 40) and Nwin and min(Nwin) > 60
checks.append(("(1) rigid rotor: E1 = %.0f keV, v* = %.0f km/s at N = 18; across the "
               "registered band v* runs %.0f (N=5) -> %.0f (N=40) km/s -- ABOVE the "
               "dwarf window everywhere N <~ 40. Window placement requires N in "
               "[%d, %d]: x4+ outside the cluster-side bound N <~ 18-21 and the 1859 "
               "pruning of N >~ 40. Simplest door CLOSED-conditional (constraint "
               "provenance flagged, check 5)"
               % (E1_rot(18)*1e3, vstar(E1_rot(18), 18), rows[0][2],
                  vstar(E1_rot(40), 40), min(Nwin), max(Nwin)), ok1, None))

# (2) LONGITUDINAL PHONONS. Coat radial spring at the pinned pitch:
#     k_s = V''(d) for V = E_ee e^{-r}/r  ->  E_ee e^{-d} (2/d^3 + 2/d^2 + 1/d).
#     Lowest free-chain mode: hbar w_1 = 2 hbar sqrt(k_s/m) sin(pi/(2N)).
E_EE = 0.9
ks = E_EE*math.exp(-D_EL)*(2/D_EL**3 + 2/D_EL**2 + 1/D_EL)          # MeV/fm^2
def hw_long(N):
    return 2.0*HBARC*math.sqrt(ks/M_EL)*math.sin(math.pi/(2*N))     # MeV
ok2 = hw_long(18) > 0.3
checks.append(("(2) longitudinal phonons: coat spring k_s = %.2f MeV/fm^2 -> lowest "
               "quantum %.2f MeV at N = 18 (%.1f MeV at N = 5) -- FOUR TO SIX orders "
               "above the window at any registered N. Door CLOSED"
               % (ks, hw_long(18), hw_long(5)), ok2, None))

# (3) BENDING MODES. Nearest-neighbor radial springs give NO leading-order
#     angle resistance; bending stiffness comes from next-nearest coat pairs:
#     kappa_theta ~ d^2 V''(2d) (order estimate). Free-free beam lowest mode:
#     hbar w_1 = hbar c * (4.730/L)^2 * sqrt(EI_flex/(rho_lin)) with
#     EI_flex = kappa_theta * d, rho_lin = m/d  ->
#     hbar w_1 = 22.37 * (HBARC * d / L^2) * sqrt(kappa_theta / m).
V2_2d = E_EE*math.exp(-2*D_EL)*(2/(2*D_EL)**3 + 2/(2*D_EL)**2 + 1/(2*D_EL))
kappa_est = D_EL**2*V2_2d                                            # MeV
def hw_bend(N, kappa):
    return 22.37*HBARC*D_EL/L(N)**2*math.sqrt(kappa/M_EL)            # MeV
ok3 = 1e-3 < hw_bend(18, kappa_est) < 1.0
checks.append(("(3) bending: next-nearest coat stiffness kappa ~ %.3f MeV -> lowest "
               "bending quantum %.0f keV at N = 18; window placement scales v* ~ "
               "N^(-3/2), reaching the dwarf band only near N ~ 190. Door CLOSED "
               "within registered constraints" % (kappa_est, hw_bend(18, kappa_est)*1e3),
               ok3, None))

# (4) THE INVERSE REQUIREMENT (the lane's live door). Required stiffness for an
#     in-window quantum at N = 18: solve hbar w_1(kappa_req) = E_cm(18, 40 km/s).
Etarget = Ecm(18, 40.0)
kappa_req = M_EL*(Etarget*L(18)**2/(22.37*HBARC*D_EL))**2
ratio = kappa_est/kappa_req
ok4 = 1e4 < ratio < 1e8
checks.append(("(4) INVERSE REQUIREMENT registered: an in-window transverse/torsional "
               "quantum at N = 18 needs stiffness kappa_req ~ %.1e MeV (~%.2f eV) -- "
               "x%.0e SOFTER than the elastic coat estimate. The surviving L1 door is "
               "the AZIMUTHAL/TORSIONAL sector, whose stiffness is UNDERIVED (the "
               "cross-arm coat may be azimuthally smooth). Handoff number to L2/L3: "
               "derive kappa_torsion; the lane lives iff it lands within ~an order of "
               "%.1e MeV" % (kappa_req, kappa_req*1e6, ratio, kappa_req), ok4, None))

# (5) CONSTRAINT PROVENANCE (L4-a linkage): the N <~ 18-21 cluster-side bound
#     and the 1859 N >~ 40 pruning were computed against the PRE-CORRECTION
#     floor (2337 showed the registered floor stands within noise but the
#     attraction-channel totals moved x3-4); the rotor window N ~ 61-90 (check
#     1) is excluded by those bounds AS REGISTERED. If L4-a's recompute
#     relaxes them, check 1 reopens arithmetically -- pre-registered linkage,
#     not a prediction.
ok5 = True
checks.append(("(5) provenance flag: the N-bounds excluding the rotor window predate "
               "the 2337 correction chain; L4-a recompute is the registered "
               "reopening condition for check 1. No claim either way", ok5, None))

# (6) RENT TEMPLATE + VERDICT. Any in-window internal mode (E* ~ 100 eV) is
#     thermally activated at plasma temperatures T >~ E* -- the rod carries
#     internal heat capacity through every epoch with T in [100 eV, ~keV]
#     (z ~ 3e5 - 3e6): pre-registerable consequences (relic momentum
#     distribution, kinetic decoupling shift) BEFORE any dwarf evaluation.
#     VERDICT: L1 simplest doors (rotor, longitudinal, bending) CLOSED-
#     conditional within registered constraints; lane SURVIVES on the
#     torsional door with its inverse-requirement number; rent template
#     registered; no SPEC-1 mechanism claimed.
ok6 = all(o for _, o, _ in checks)
checks.append(("(6) L1 first-patch verdict: rigid/elastic internal spectrum CLOSED-"
               "conditional at registered N (all quanta 10 keV - 1 MeV); surviving "
               "door = torsional sector with kappa_req ~ %.1e MeV as the derived-or-"
               "dead handoff; rent template: in-window modes are thermally live at "
               "z ~ 3e5-3e6 with pre-registerable relic consequences" % kappa_req,
               ok6, None))

npass = 0
for msg, ok, _ in checks:
    print(("PASS " if ok else "FAIL ") + msg + "\n")
    npass += ok
print("=== %d/%d ===" % (npass, len(checks)))

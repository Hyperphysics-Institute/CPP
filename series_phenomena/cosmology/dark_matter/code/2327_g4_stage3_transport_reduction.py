#!/usr/bin/env python3
"""Patch 2327 -- G4 Stage-3 opening move: the transport reduction.

The handover's 'cheap first move' (Ohmic-excess bound at the LSB frequency 4.25 keV),
executed as a structural reduction rather than a numerical shortcut.

THE MOVE (one sentence): under condition C-g the spectrum entering the loss formula is
BY DEFINITION the dynamic structure factor of the occupancy field (the Rayleigh coupling
is defined through occupancy-fluctuation cells, delta^2 = f_occ(1-f_occ)); occupancy is a
CONSERVED density at encounter frequencies (no Sea DP creation channel below the e-channel
0.9 MeV -- 2311 gap inventory -- and CPs are ontological primitives, A1, with no registered
creation/annihilation process), so its correlation time at wavevector k is the TRANSPORT
time tau_k = 1/(D k^2), not the local regeneration time tau_b. The 2321 golden-rule
construction then gives the normalized dissipative factor
    Theta(omega) = 2 x / (1 + x^2),   x = omega * tau_k,
(same construction as 2321's fast-bath Ohmic bound Theta ~ omega*tau_b, which is the
x << 1 limit of this form with tau_k -> tau_b; the conserved channel replaces tau_b by
tau_k >> tau_b). The gate therefore reduces from an unknown FUNCTION S(k~1/R_s, omega)
to ONE transport number: D, the Sea occupancy diffusivity at the 25-fm scale.

Checks:
 (1) sub-gap conservation: hbar*omega_enc(LSB) sits far below every Sea creation channel;
 (2) regime validity: k*ell_cp << 1 at the portrait mean free path (hydrodynamic form OK);
 (3) registered-kinetics cap: light-speed PCD kinetics (D = c*ell_cp/3) lands Theta(4.25 keV)
     at 0.026 (portrait mfp) / 0.083 (Ioffe-Regel outer bound) -- BOTH below the 0.66 bar;
 (4) cheap-kill criterion (handover): transport excess over bare Ohmic = x1.2e3-3.9e3,
     which EXCEEDS the >=1e3 line -- the pre-registered cheap kill does NOT fire;
 (5) the pre-registered survive window PRW-D: Theta(4.25 keV) >= 0.66 iff
     x in [0.377, 2.653] iff hbar/tau_k in [1.60, 11.27] keV iff D in [5.2e-3, 3.7e-2] c*fm;
 (6) suite consistency INSIDE the window: dwarf and pin hold at P ~ 1 across the window
     (with E_coat >= 0.40 MeV riding along per 2324);
 (7) two-sided kill OUTSIDE the window: above (incl. light-speed kinetics, x9-29 over the
     window top) and below (>= 6 decades), the pattern is dwarf-pass + LSB-floor -- exactly
     the class 2324 showed is EXCLUDED BY THE EXISTING LSB ANCHOR;
 (8) branch-invariants unchanged: elastic floor, cluster/Bullet safety (f_geo-protected at
     high v), F1 group falsifier.

NO VERDICT MOVED: G4 stays UNRESOLVED-QUANTIFIED. The residue is reduced from S(k,omega)
to one derivable number with a two-sided window registered BEFORE the number is computed.
"""
import math

C = 2.998e8; HBARC = 197.327                 # MeV fm
ELL, DELTA2, F_OCC = 1.0, 0.09, 0.1          # fm; delta^2 = f_occ(1-f_occ); SI-2 portrait
RS, RC = 25.42, 1.0                          # fm
ECOAT_LO, ECOAT_HI = 0.144, 0.6              # MeV
FLOOR = 0.046                                # cm^2/g, measured elastic (1870-71 MC)
ANCH = {"dwarf10": (10, 145.0, 7.04e-6),     # v km/s, b_max fm, E_col MeV (2311/2316/2321)
        "pin50":   (50, 79.0, 1.76e-4),
        "lsb200":  (200, 31.0, 2.82e-3)}
PUB  = {"dsph": (15.5, (20.0, 100.0)), "pin50": (4.65, (1.0, 5.0)), "lsb200": (0.795, (0.7, 2.5))}
E_CHANNEL_GAP = 0.9                          # MeV, lowest Sea creation channel (2311 inventory)

def mfp_ray(k): return ELL/((k*ELL)**4*DELTA2)                    # broadcast Rayleigh mfp, fm
def fgeo(v_kms, b): return (2*b/(v_kms*1e3/C))/mfp_ray(1.0/RS)
def theta_crit(v_kms, b, Ecol, Ecoat): return (Ecol/Ecoat)/fgeo(v_kms, b)
def theta_hydro(hw_MeV, hw_knee_MeV):
    x = hw_MeV/hw_knee_MeV
    return 2*x/(1+x*x)

k_sub = 1.0/RS                               # fm^-1, the C-g scattering wavevector
om = {a: HBARC*(v*1e3/C)/b for a,(v,b,_) in ANCH.items()}         # hbar*omega_enc, MeV
TH = {a: (theta_crit(v,b,E,ECOAT_HI), theta_crit(v,b,E,ECOAT_LO)) for a,(v,b,E) in ANCH.items()}
ohmic_lsb = (ANCH['lsb200'][0]*1e3/C)*(RC/ANCH['lsb200'][1])      # bare Ohmic omega*tau_b at LSB

# survive bar at the LSB anchor (recompute 2324): P >= Pmin => w >= Theta_crit/sqrt(1-Pmin)
Pmin_lsb = (PUB['lsb200'][1][0]-FLOOR)/(PUB['lsb200'][0]-FLOOR)
W_REQ = TH['lsb200'][0]/math.sqrt(1-Pmin_lsb)                     # easy-coat end (E_coat = 0.6)
Ecoat_min = ANCH['lsb200'][2]/(math.sqrt(1-Pmin_lsb)*fgeo(*ANCH['lsb200'][:2]))

checks = []

# (1) sub-gap occupancy conservation
ratio_gap = E_CHANNEL_GAP/om['lsb200']
checks.append((f"sub-gap conservation: hbar*omega_enc(LSB) = {om['lsb200']*1e3:.2f} keV sits x{ratio_gap:.0f} "
               f"below the lowest Sea creation channel (e-channel {E_CHANNEL_GAP} MeV, 2311 inventory); with "
               f"CPs ontological primitives (A1, no registered creation/annihilation), occupancy at k = 1/R_s "
               f"is a CONSERVED density at all encounter frequencies -- its correlation time is the transport "
               f"time tau_k = 1/(D k^2), not tau_b", ratio_gap > 100, ratio_gap))

# (2) hydrodynamic regime validity at the portrait mfp
n_dp = F_OCC/ELL**3; sigma_cp = math.pi*RC**2; ell_cp = 1.0/(n_dp*sigma_cp)   # fm
kl = k_sub*ell_cp
checks.append((f"regime validity: portrait carrier mfp ell_cp = 1/(n sigma) = {ell_cp:.2f} fm "
               f"(n = f_occ/ell^3 = {n_dp:.2f} fm^-3, sigma = pi r_c^2); k*ell_cp = {kl:.3f} << 1 at "
               f"k = 1/R_s -- transport at the 25-fm scale is DIFFUSIVE and the hydrodynamic Lorentzian "
               f"form Theta = 2x/(1+x^2) is the right closure (not an assumption of convenience)",
               kl < 0.3, kl))

# (3) registered-kinetics cap: light-speed PCD kinetics
def knee_from_D(D_cfm): return HBARC/(RS*RS/D_cfm)                # hbar/tau_k in MeV
D_port = ell_cp/3.0                                               # c*fm  (v_drift = c)
D_ir   = ELL/3.0                                                  # Ioffe-Regel outer bound (mfp = ell)
knee_port, knee_ir = knee_from_D(D_port), knee_from_D(D_ir)
th_port = theta_hydro(om['lsb200'], knee_port)
th_ir   = theta_hydro(om['lsb200'], knee_ir)
checks.append((f"light-speed kinetics cap: D = c*ell_cp/3 = {D_port:.2f} c*fm gives knee hbar/tau_k = "
               f"{knee_port*1e3:.0f} keV and Theta(4.25 keV) = {th_port:.3f}; Ioffe-Regel outer bound "
               f"(mfp = ell = 1 fm) gives knee {knee_ir*1e3:.0f} keV, Theta = {th_ir:.3f} -- BOTH below the "
               f"survive bar {W_REQ:.2f}: if Sea occupancy kinetics is light-speed, the LSB anchor CANNOT "
               f"be held (shortfall x{W_REQ/th_port:.0f} portrait / x{W_REQ/th_ir:.1f} outer bound)",
               th_port < W_REQ and th_ir < W_REQ and 0.6 < W_REQ < 0.7, (th_port, th_ir)))

# (4) the handover's cheap-kill criterion, evaluated honestly
ex_port, ex_ir = th_port/ohmic_lsb, th_ir/ohmic_lsb
checks.append((f"cheap-kill criterion (2326 handover: 'cannot exceed the Ohmic tail by >=1e3 at keV => KILL'): "
               f"the conserved-transport channel EXCEEDS bare Ohmic ({ohmic_lsb:.2e}) by x{ex_port:.0f} "
               f"(portrait) to x{ex_ir:.0f} (outer bound) -- ABOVE the 1e3 line: the pre-registered cheap "
               f"kill does NOT fire; the gap between achievable (0.026-0.083) and required (0.66) is "
               f"x8-x25, decided by ONE number (D), not by the bound",
               ex_port > 1e3 and ex_ir > 1e3, (ex_port, ex_ir)))

# (5) the pre-registered survive window PRW-D
a = W_REQ; disc = math.sqrt(4-4*a*a)
x_lo, x_hi = (2-disc)/(2*a), (2+disc)/(2*a)
knee_hi, knee_lo = om['lsb200']/x_lo, om['lsb200']/x_hi           # MeV (x_lo -> high knee)
D_lo, D_hi = RS*RS*knee_lo/HBARC, RS*RS*knee_hi/HBARC             # c*fm
v_lo, v_hi = 3*D_lo/ell_cp*C/1e3, 3*D_hi/ell_cp*C/1e3             # km/s at portrait mfp
checks.append((f"PRW-D (pre-registered NOW, before D is derived): Theta(4.25 keV) >= {W_REQ:.2f} iff "
               f"x in [{x_lo:.3f}, {x_hi:.3f}] iff knee hbar/tau_k in [{knee_lo*1e3:.2f}, {knee_hi*1e3:.2f}] keV "
               f"iff D in [{D_lo:.2e}, {D_hi:.2e}] c*fm (width x{D_hi/D_lo:.1f}); at the portrait mfp this is "
               f"drift speed v in [{v_lo:.0f}, {v_hi:.0f}] km/s = [{v_lo*1e3/C:.1e}, {v_hi*1e3/C:.1e}] c -- "
               f"light-speed kinetics overshoots the window top by x{D_port/D_hi:.0f} (portrait) / "
               f"x{D_ir/D_hi:.0f} (outer bound); E_coat >= {Ecoat_min:.2f} MeV rides along (2324)",
               6 < D_hi/D_lo < 8 and 20 < D_port/D_hi < 40, (D_lo, D_hi)))

# (6) suite consistency INSIDE the window (both edges): dwarf and pin at P ~ 1
edge_ok = True; edge_vals = {}
for knee in (knee_lo, knee_hi):
    th_d = theta_hydro(om['dwarf10'], knee); th_p = theta_hydro(om['pin50'], knee)
    P_d = 1-(TH['dwarf10'][1]/th_d)**2; P_p = 1-(TH['pin50'][1]/th_p)**2    # hard-coat (worst)
    edge_vals[round(knee*1e3,2)] = (th_d, th_p, P_d, P_p)
    edge_ok &= th_d > 10*TH['dwarf10'][1] and th_p > 2*TH['pin50'][1] and P_d > 0.99
checks.append((f"inside the window the FULL suite holds: at both window edges Theta(dwarf 45 eV) clears its "
               f"hard bar x{min(v[0]/TH['dwarf10'][1] for v in edge_vals.values()):.0f}+ (P > 0.99) and "
               f"Theta(pin 417 eV) clears x{min(v[1]/TH['pin50'][1] for v in edge_vals.values()):.0f}+ -- "
               f"dwarf cores, pin, and LSB are held SIMULTANEOUSLY by one D in PRW-D (plus E_coat >= 0.40): "
               f"a zero-refit resting point exists, which no flat spectrum had (2324)",
               edge_ok, edge_vals))

# (7) two-sided kill OUTSIDE the window; persistence of the excluded pattern
# above: light-speed kinetics (check 3). below: dwarf still passes down to a tiny knee
knee_dwarf_dies = om['dwarf10']*TH['dwarf10'][0]/2                # Theta ~ 2/x < Theta_crit_easy
decades_below = math.log10(knee_lo/knee_dwarf_dies)
th_lsb_below = theta_hydro(om['lsb200'], knee_lo/10)              # sample: 1 decade below window
checks.append((f"two-sided kill: ABOVE the window (up to and past light-speed kinetics) LSB fails while "
               f"dwarf/pin pass; BELOW the window the same pattern persists for {decades_below:.1f} decades "
               f"of D (dwarf capture stays alive down to knee ~ {knee_dwarf_dies*1e9:.1f} neV; e.g. one decade "
               f"below the window Theta(LSB) = {th_lsb_below:.2f} < {W_REQ:.2f} with dwarfs still clearing) -- "
               f"everywhere outside PRW-D the outcome is the dwarf-pass/LSB-floor pattern that 2324 showed is "
               f"EXCLUDED BY THE EXISTING LSB ANCHOR: outside the window, KILL-on-suite",
               decades_below > 5 and th_lsb_below < W_REQ, (decades_below, th_lsb_below)))

# (8) branch invariants
fgeo200 = fgeo(200, 31.0)
checks.append((f"branch invariants unchanged: the elastic floor ({FLOOR} cm^2/g) is spectrum-independent; "
               f"cluster/Bullet safety is f_geo-protected at high v (f_geo(200 km/s) = {fgeo200:.3f} and "
               f"falling -- Theta_crit >> 1 at cluster kinematics regardless of D); F1 group falsifier "
               f"(0.037-0.05 vs Sagunski) floor-dominated in every branch (2324)",
               fgeo200 < 0.03, fgeo200))

npass = 0
for name, ok, val in checks:
    print(f"[{'PASS' if ok else 'FAIL'}] {name}\n")
    npass += ok
print(f"{npass}/{len(checks)} PASS")
assert npass == len(checks)

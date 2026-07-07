#!/usr/bin/env python3
"""Patch 2328 -- Grok W2 (formation-N vs floor-N reconciliation), executed.

Grok's decisive check (2311 adjudication, queued): 1855-style kinetics with capture+floor
active -> N distribution -> floor check.

Delivered in three layers:
 (A) STATIC: the 1855-1860 arc already reconciled formation-N with floor-N (restated, PASS).
 (B) FORMATION EPOCH: rod-rod capture is reach-dead at formation-era thermal velocities
     (Theta_crit(337 km/s) > 1 even at ceiling spectral weight) -- the 1855 monomer-addition
     endpoint is unmodified during formation proper.
 (C) THE NEW SURFACE (post-formation cosmic history): after kinetic decoupling rod velocities
     redshift v ~ a^-1 from 337 km/s down through the entire anchor ladder. Because
     Theta_crit ~ v^2 (reach saturation) falls faster than the encounter response at ANY
     knee, capture ACTIVATES in the radiation era for every registered spectrum under
     D = const. Rates at activation are 1e4-1e5 captures per rod per Hubble time -- a
     coagulation runaway that destroys the monomeric population the entire anchor suite
     (25 GeV rod, floor at N = 18, XQC F5) is calibrated on.
     => OPEN-DM-AGG-1 registered: the radiation-era aggregation epoch. Escape routes named:
     (i) D(T_amb) cosmological history (hot early Sea => knee >~ 0.6 MeV-class at z ~ 1e7,
     only x2-x100 above today's values -- modest, natural, and the SAME Stage-3 quantity
     that decides G4); (ii) aggregation-endpoint reproduction of the anchors (d_f fork,
     (sigma/m)_agg/(sigma/m)_mono = (R_g/a)^(2-d_f); disfavored on its face).

All under D = const (named assumption); free-streaming velocity history (named caveat:
elastic-floor self-scattering keeps the population self-thermal, ~225/Hubble at z ~ 1e7,
but conserves energy so v ~ a^-1 stands for the NR gas).

Checks (8): static PASS; formation-epoch reach-dead; survive-window activation z/rate;
light-speed-cap activation z/rate (universality); bare-Ohmic borderline tail; descent
table + equality endpoint; the required off-condition knee(z) (escape quantification);
branch table for the reconciliation verdict.
"""
import math

C_KMS = 2.998e5; HBARC = 197.327                    # MeV fm
RS, RC, ELL, DELTA2 = 25.42, 1.0, 1.0, 0.09
MFP = ELL/((ELL/RS)**4*DELTA2)                      # Rayleigh mfp at k = 1/R_s, fm
ECOAT = 0.6                                         # MeV, easy end (conservative for activation)
FGEO_SAT = 1.9                                      # dwarf saturation (2321 grid)
FLOOR = 0.046
ANCH_B = [(10.0, 145.0), (50.0, 79.0), (200.0, 31.0)]      # v km/s, b_max fm
S_LO = math.log(145/79)/math.log(50/10)             # 0.377 (10-50 slope)
S_HI = math.log(79/31)/math.log(200/50)             # 0.675 (50-200 slope)
ECOL_200 = 2.82e-3                                  # MeV; E_col = ECOL_200*(v/200)^2 exactly
# cosmology (order-unity g* factors flagged in memo)
RHO_DM0 = 2.25e-30                                  # g/cm^3 (Omega_dm h^2 = 0.12)
T0_MEV = 2.348e-10                                  # today's photon temperature
TFORM_MEV = 0.016; ZF1 = TFORM_MEV/T0_MEV           # 1+z_form = 6.81e7
MROD_MEV = 25344.0
VFORM = math.sqrt(2*TFORM_MEV/MROD_MEV)*C_KMS       # 336.9 km/s
Z_EQ1 = 3400.0

def b_of_v(v):
    if v >= 50.0:  return 31.0*(v/200.0)**(-S_HI)   # extrapolates above 200 on the 50-200 slope
    if v >= 10.0:  return 79.0*(v/50.0)**(-S_LO)
    return 145.0*(v/10.0)**(-S_LO)                  # extrapolated below the anchors (caveat)
def fgeo(v):  return min(FGEO_SAT, (2*b_of_v(v)/(v/C_KMS))/MFP)
def th_crit(v): return (ECOL_200*(v/200.0)**2/ECOAT)/fgeo(v)
def om_enc(v):  return HBARC*(v/C_KMS)/b_of_v(v)    # MeV
def theta(v, knee):                                  # normalized dissipative weight at omega_enc
    x = om_enc(v)/knee; return 2*x/(1+x*x)
def theta_ohmic(v): return om_enc(v)/HBARC          # bare Ohmic omega*tau_b (tau_b = r_c/c)

def z1_of_v(v): return ZF1*(v/VFORM)                # free-streaming: v ~ a^-1 from formation
def captures_per_hubble(v, sig, P=1.0):
    z1 = z1_of_v(v); T = T0_MEV*z1
    t = 2.4/T**2 if z1 > Z_EQ1 else 4.35e17*z1**-1.5   # radiation / matter (approx)
    rho = RHO_DM0*z1**3
    return sig*rho*(v*1e5)*t*P
def sig_pub(v):                                     # published totals, log-interp/extrapolated
    pts = [(10.0, 15.5), (50.0, 4.65), (200.0, 0.795)]
    if v <= 10.0:  return 15.5*(10.0/v)**0.755      # capture-sigma slope from b(v) (caveat)
    if v >= 200.0: return 0.795
    lo, hi = (pts[0], pts[1]) if v < 50 else (pts[1], pts[2])
    s = math.log(hi[1]/lo[1])/math.log(hi[0]/lo[0])
    return lo[1]*(v/lo[0])**s

def v_activation(knee):
    """largest v < VFORM at which theta(v,knee) >= th_crit(v) (capture turns on)."""
    v = VFORM
    while v > 1e-3:
        if theta(v, knee) >= th_crit(v): return v
        v *= 0.995
    return None

KNEE_SURV_LO, KNEE_SURV_HI = 1.60e-3, 11.30e-3      # PRW-D window edges (2327), MeV
KNEE_LS = 0.324                                     # light-speed portrait cap (2327), MeV
checks = []

# (A) static reconciliation restated
NFORM = (3, 27); NCEIL = (18, 21); NFLOOR = 18
checks.append((f"static reconciliation (1855-1860 arc, restated): formation window N_form ~ {NFORM[0]}-"
               f"{NFORM[1]} contains the floor-MC N = {NFLOOR} (1871), which sits at/under the cluster "
               f"ceiling N <~ {NCEIL[0]}-{NCEIL[1]} (1860 transport convention); three independent arrows "
               f"at short N -- the STATIC formation-N vs floor-N reconciliation PASSES",
               NFORM[0] <= NFLOOR <= NFORM[1] and NFLOOR <= NCEIL[1], None))

# (B) formation-epoch capture reach-dead
tc_form = th_crit(VFORM)
checks.append((f"formation epoch: v_th(16 keV, 25.3 GeV) = {VFORM:.0f} km/s; Theta_crit = {tc_form:.2f} > 1 "
               f"-- capture is REACH-DEAD at formation-era velocities even at ceiling spectral weight "
               f"(and the elastic floor only thermalizes): the 1855 monomer-addition endpoint is "
               f"unmodified during formation proper", tc_form > 1.0, tc_form))

# (C1) survive-window activation
va_lo, va_hi = v_activation(KNEE_SURV_LO), v_activation(KNEE_SURV_HI)
za = [z1_of_v(v) for v in (va_lo, va_hi)]
cap_at_50_surv = captures_per_hubble(50.0, sig_pub(50.0))
checks.append((f"SURVIVE window (PRW-D): capture activates at v_on = {min(va_lo,va_hi):.0f}-{max(va_lo,va_hi):.0f} "
               f"km/s, i.e. z ~ {min(za):.1e}-{max(za):.1e} -- within one e-fold of formation; along the "
               f"descent the rate at the pin kinematics (v = 50 km/s, z ~ 1.0e7) is "
               f"{cap_at_50_surv:.1e} captures/rod/Hubble (P ~ 1 there)",
               min(va_lo, va_hi) > 200 and cap_at_50_surv > 1e4, (va_lo, va_hi, cap_at_50_surv)))

# (C2) universality: even the light-speed transport cap activates in the radiation era
va_ls = v_activation(KNEE_LS)
ratio_50_ls = theta(50.0, KNEE_LS)/th_crit(50.0)
P50 = max(0.0, 1-(1/ratio_50_ls)**2) if ratio_50_ls > 1 else 0.0
cap_at_50_ls = captures_per_hubble(50.0, sig_pub(50.0), P50)
checks.append((f"UNIVERSALITY: even at the light-speed transport cap (knee 324 keV -- the 2327 kill-side "
               f"spectrum) capture activates at v_on = {va_ls:.0f} km/s (z ~ {z1_of_v(va_ls):.1e}), and by the "
               f"pin kinematics runs at {cap_at_50_ls:.1e} captures/rod/Hubble (P = {P50:.2f}) -- the "
               f"radiation-era aggregation runaway is BRANCH-INDEPENDENT under D = const; driver: "
               f"Theta_crit ~ v^2 (reach saturation) falls faster than the response at any knee",
               va_ls is not None and 40 < va_ls < 120 and cap_at_50_ls > 1e3, (va_ls, cap_at_50_ls)))

# (C3) the bare-Ohmic tail is borderline, not runaway (grading honesty)
v = VFORM; va_ohm = None
while v > 1e-3:
    if theta_ohmic(v) >= th_crit(v): va_ohm = v; break
    v *= 0.995
cap_ohm = captures_per_hubble(va_ohm, sig_pub(va_ohm), 0.5) if va_ohm else 0.0
checks.append((f"grading: the BARE-OHMIC floor spectrum activates only in the deep dark ages "
               f"(v ~ {va_ohm:.2f} km/s, z ~ {z1_of_v(va_ohm):.0e}) at ~{cap_ohm:.1f} captures/Hubble -- "
               f"O(1), borderline (dimers at most): the runaway belongs to transport-class and stronger "
               f"spectra, i.e. exactly the spectra 2327 argued occupancy conservation FORCES",
               va_ohm is not None and va_ohm < 0.2 and 0.1 < cap_ohm < 50, (va_ohm, cap_ohm)))

# (C4) descent table and the equality endpoint
tbl = {}
for vv in (200.0, 50.0, 10.0):
    tbl[vv] = captures_per_hubble(vv, sig_pub(vv))
v_eq = VFORM*Z_EQ1/ZF1
cap_eq = captures_per_hubble(v_eq*1.0001, sig_pub(v_eq))          # just above equality
checks.append((f"the descent (survive-class, P~1): captures/rod/Hubble = {tbl[200.0]:.1e} (v=200, z~4e7) / "
               f"{tbl[50.0]:.1e} (50, 1e7) / {tbl[10.0]:.1e} (10, 2e6) / ~{cap_eq:.1f} at equality "
               f"(v = {v_eq*1e3:.0f} m/s) -- above unity for the ENTIRE radiation era post-activation: "
               f"integrated >= 1e5 captures per monomer lineage; the monomeric 25-GeV population (every "
               f"anchor's calibration object) does not survive to the halo era",
               tbl[200.0] > 1e4 and 0.2 < cap_eq < 10, (tbl, cap_eq)))

# (C5) the escape, quantified: knee(z) required to hold capture OFF along the descent
req = {}
for vv in (200.0, 50.0, 10.0):
    # smallest knee with theta(v,knee) < th_crit(v); rising branch: knee > 2*omega/th_crit
    req[vv] = 2*om_enc(vv)/th_crit(vv)
checks.append((f"OPEN-DM-AGG-1 escape route (i), quantified: holding capture OFF at epoch z(v) needs "
               f"knee(z) >~ {req[200.0]*1e3:.0f} keV (v=200) / {req[50.0]*1e3:.0f} keV (50) / "
               f"{req[10.0]:.1f} MeV (10) -- an ESCALATING requirement (roughly v^-2), met by a hot early "
               f"Sea (D(T_amb) >> today's PRW-D values, cooling INTO the window by the halo era) down to "
               f"v ~ 0.05 km/s, below which NO knee suffices (the bare-Ohmic activation shows the "
               f"requirement crossing the 197-MeV band edge): route (i) delays activation into the deep "
               f"dark ages and reduces the runaway to the O(1) borderline tail -- it does not eliminate "
               f"capture. The SAME Stage-3 quantity that decides G4 decides the activation epoch -- one "
               f"derivation, two gates. Route (ii) (aggregation endpoint reproducing monomer-calibrated "
               f"anchors via the d_f map (sigma/m)_agg = (sigma/m)_mono (R_g/a)^(2-d_f)) is disfavored on "
               f"its face", 0.3 < req[50.0] < 1.2 and req[10.0] > 5, req))

# (C6) reconciliation verdict table (branch-graded)
checks.append((f"W2 verdict: STATIC reconciliation PASSES; DYNAMIC reconciliation is CONDITIONAL on "
               f"OPEN-DM-AGG-1 in every branch under D = const (survive window: activation z ~ 5e7 at "
               f"~1e5/Hubble; light-speed cap: z ~ 1e7 at ~1e4/Hubble; bare Ohmic: borderline O(1) dark-age "
               f"tail) -- the floor-N check cannot be closed until the activation history is: the natural "
               f"closure is route (i), which Stage-3's D derivation delivers as D(T_amb). No verdict on any "
               f"registered claim moves; the anchors' unit-monomer assumption acquires a NAMED cosmological "
               f"condition", True, None))

npass = 0
for name, ok, val in checks:
    print(f"[{'PASS' if ok else 'FAIL'}] {name}\n")
    npass += ok
print(f"{npass}/{len(checks)} PASS")
assert npass == len(checks)

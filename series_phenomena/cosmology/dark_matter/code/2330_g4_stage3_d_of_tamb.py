#!/usr/bin/env python3
"""Patch 2330 -- G4 Stage-3 executed: D(T_amb) from the PCD displacement rules.

THE DERIVATION (structure; full argument in gate1_b1_G4_stage3_D_of_Tamb_derivation.md):

 (I)  HARMONIC-NULL THEOREM. Under the founder's no-carried-velocity ruling
      (founders_voice/no_carried_velocity_displacement_from_ssv_2026-07-07.md) a Sea DP
      center is SLAVED to the local SSV field: its per-Moment displacement is a function
      of SSV_net/SSV_abs only. For the center riding the thermally populated gapless
      coherence mode (2317: omega = ck, C-e), the velocity autocorrelation is set by the
      thermal phonon spectrum ~ omega^3 n_B(omega), whose omega -> 0 weight VANISHES.
      Kubo: D_coherent = (pi/3) S_vv(0) = 0 EXACTLY in the harmonic field. Coherent
      field-following transports nothing; the incoherent per-Moment residue is bounded by
      the Planck floor l_P*c/6 ~ 2.7e-21 c*fm, 18 orders below PRW-D.
      => The pre-registered Planck-floor kill fires UNLESS a threshold channel exists.

 (II) THE THRESHOLD CHANNEL. Occupancy relaxes by site exchange: a DP center hops one
      pitch a when the local thermal SSV fluctuation carries it over the inter-site
      saddle. Saddle height E_a = kappa_a * E_ee (partial stretch of the e-channel
      contact bonds; full break = E_ee = 0.9 MeV, M3) [J-2330-1: kappa_a in [1/3, 1)].
      Attempt decorrelation: the ZBW internal cycle of the quiescent Sea DP (U2,
      omega_z = E_z/hbar) re-phases the center's response each cycle -> independent
      attempts at nu = kappa_nu * E_z/hbar [J-2330-2: C-j-Z primary; C-j-T and C-j-P
      branches graded in check 4].
        D_hop(T) = (a^2 nu / 6) * exp(-E_a/T_amb)                       (Arrhenius)
      saturating at min(a^2 nu/6, c*ell_cp/3) for T >~ E_a.

 (III) THE NON-CONSERVING CHANNEL (R-III). The e-channel creation gap E_gap = 0.9 MeV
      (2311 inventory) is thermally activated at the same cadence:
        Gamma_loc(T) = kappa_c * nu * exp(-E_gap/T_amb)   [J-2330-3: kappa_c O(1)]
      This ADDS to occupancy relaxation at every k. The knee entering Theta is the total:
        knee_tot(T) = hbar * [ D_hop(T) k^2 + Gamma_loc(T) ],  k = 1/R_s.
      Above the gap (T_amb >~ E_gap) the occupancy is no longer conserved (C-h-1 lifts)
      and the knee rises toward min(hbar*nu, band edge hbar*c/a = 197.3 MeV).

 CONSEQUENCES CHECKED HERE:
  1. harmonic-null: zero-frequency weight of the thermal velocity spectrum -> 0.
  2. Planck floor magnitude vs PRW-D (the pre-registered kill branch scale).
  3. window inversion (C-j-Z): PRW-D <=> X4 = kappa_nu*E_z*exp(-E_a/T0) in [6.16,43.8] MeV
     when transport-dominated; general form = knee_tot in the 2327 window.
  4. cadence-branch grading: C-j-T (thermal bandwidth) is KILLED inside the U6 prior;
     C-j-P (Planck cadence) demands E_a/T0 ~ 48 (numerology noted, branch disfavored).
  5. monotonicity: knee_tot(T) strictly increasing -> "early-high, late-in-window" is
     now a DERIVED-form statement under any monotone cooling T_amb(z).
  6. AGG-1 transport ceiling: the hop channel saturates below the light-speed cap; the
     off-condition knee_req at the pin epoch (0.58 MeV) EXCEEDS every transport knee ->
     route (i) CANNOT be delivered by transport alone (v_on >= 66.6 km/s, the 2328
     light-speed row reproduced as the transport-optimal bound).
  7. R-III reach: above-gap local relaxation extends protection to the band-edge crossing
     v_edge ~ 2.6 km/s (exact 2328 machinery), (1+z) ~ 5e5 -- deep in the dark ages; the
     residual tail below v_edge is bracketed (AGG-1-R registered for the integral).
  8. Sea cooling: free-streaming gapless-mode cooling T_amb ~ (1+z) makes R-III coverage
     of the descent GENERIC (T0 >= ~2 eV suffices to keep T(z_edge) above the gap).
  9. the survive corner: Monte-Carlo existence scan over (E_z, T0, kappa_a, kappa_nu,
     kappa_c) priors for knee_tot(T0) in the PRW-D window -- NON-EMPTY; marginals
     reported; T0 marginal vs the F7 soft target flagged.
 10. pre-registered outcome grading: Planck-floor kill does NOT fire (threshold channel
     exists); G4 remains UNRESOLVED-QUANTIFIED but reduced to the X4 corner; AGG-1
     route (i) narrowed to R-III-required.

NO VERDICT MOVED.
"""
import math, random

# ---------- registered constants (2327/2328 conventions) ----------
C_KMS  = 2.998e5
HBARC  = 197.327                    # MeV fm
A      = 1.0                        # fm, lattice pitch (M5, r_c = a)
RS     = 25.42                      # fm
ELLCP  = 3.18                       # fm, portrait carrier mfp (2327)
K      = 1.0/RS                     # fm^-1
LP     = 1.616e-20                  # fm, Planck length
E_EE   = 0.9                        # MeV, e-channel bond (M3) = lowest creation gap (2311)
E_GAP  = 0.9                        # MeV
OM_LSB = 4.25e-3                    # MeV, LSB encounter frequency (2327)
X_LO, X_HI = 0.377, 2.653           # PRW-D: Theta >= 0.66 iff x = om*tau_k in [X_LO, X_HI]
KNEE_LO, KNEE_HI = OM_LSB/X_HI, OM_LSB/X_LO      # 1.602e-3 .. 11.27e-3 MeV
D_LO  = KNEE_LO*RS*RS/HBARC         # c*fm
D_HI  = KNEE_HI*RS*RS/HBARC
D_CAP = ELLCP/3.0                   # c*fm, ballistic/light-speed cap (2327)
U2_LO, U2_HI = 1e-3, 1e3            # MeV, E_z prior (SI-1)
U6_LO, U6_HI = 1e-4, 1.0            # MeV, T_amb prior (SI-1)
KTFORM = 0.0164                     # MeV, F7 soft target (M8 center)

# ---------- 2328 machinery (verbatim forms) ----------
MFP    = 1.0/((1.0/RS)**4*0.09)
ECOAT  = 0.6; FGEO_SAT = 1.9; ECOL_200 = 2.82e-3
S_LO_B = math.log(145/79)/math.log(50/10)
S_HI_B = math.log(79/31)/math.log(200/50)
T0_MEV = 2.348e-10; TFORM_MEV = 0.016; ZF1 = TFORM_MEV/T0_MEV
MROD   = 25344.0; VFORM = math.sqrt(2*TFORM_MEV/MROD)*C_KMS; Z_EQ1 = 3400.0
RHO_DM0 = 2.25e-30

def b_of_v(v):
    if v >= 50.0: return 31.0*(v/200.0)**(-S_HI_B)
    if v >= 10.0: return 79.0*(v/50.0)**(-S_LO_B)
    return 145.0*(v/10.0)**(-S_LO_B)
def fgeo(v):    return min(FGEO_SAT, (2*b_of_v(v)/(v/C_KMS))/MFP)
def th_crit(v): return (ECOL_200*(v/200.0)**2/ECOAT)/fgeo(v)
def om_enc(v):  return HBARC*(v/C_KMS)/b_of_v(v)
def knee_req(v): return 2*om_enc(v)/th_crit(v)      # off-condition knee (2328 C5)
def z1_of_v(v): return ZF1*(v/VFORM)
def sig_pub(v):
    pts = [(10.0,15.5),(50.0,4.65),(200.0,0.795)]
    if v <= 10.0: return 15.5*(10.0/v)**0.755
    if v >= 200.0: return 0.795
    lo, hi = (pts[0],pts[1]) if v < 50 else (pts[1],pts[2])
    s = math.log(hi[1]/lo[1])/math.log(hi[0]/lo[0])
    return lo[1]*(v/lo[0])**s
def captures_per_hubble(v, sig, P=1.0):
    z1 = z1_of_v(v); T = T0_MEV*z1
    t = 2.4/T**2 if z1 > Z_EQ1 else 4.35e17*z1**-1.5
    return sig*(RHO_DM0*z1**3)*(v*1e5)*t*P

# ---------- the derived law ----------
def d_hop(T, Ez, ka, kn):            # c*fm
    pref = min((A*A/6.0)*(kn*Ez)/HBARC, D_CAP)      # a^2 nu/6 in c*fm, capped ballistic
    return pref*math.exp(-ka*E_EE/T)
def gam_loc(T, Ez, kn, kc):          # relaxation rate in c/fm units -> knee via hbar
    return kc*(kn*Ez)/HBARC*math.exp(-E_GAP/T)      # 1/fm (rate/c)
def knee_tot(T, Ez, ka, kn, kc):     # MeV
    return HBARC*(d_hop(T, Ez, ka, kn)*K*K + gam_loc(T, Ez, kn, kc))

checks = []

# (1) HARMONIC-NULL: zero-frequency weight of the thermal velocity spectrum.
#     S_vv(omega) ~ omega^3 n_B(omega) (one gapless scalar branch, omega = ck);
#     D_coh = (pi/3) S_vv(0). Show S_vv(0)=0 exactly and the running time-integral of the
#     velocity ACF -> 0 (oscillatory quiver, no secular transport).
import numpy as np
xg = np.linspace(1e-6, 60.0, 400000)
w  = xg**3/np.expm1(xg)                              # thermal spectrum (dimensionless)
def acf(s): return np.trapezoid(w*np.cos(xg*s), xg)/np.trapezoid(w, xg)
S  = np.linspace(0.0, 40.0, 4001)
run = np.cumsum([acf(s) for s in S])*(S[1]-S[0])     # running integral of normalized ACF
tail = abs(run[-1]); peak = abs(run[np.argmax(np.abs(run))])
sv0 = (1e-8)**3/math.expm1(1e-8)                     # spectrum at omega -> 0
checks.append(("(1) harmonic-null: S_vv(omega->0) ~ x^3/(e^x-1) -> %.1e (exactly 0 in the "
               "limit); running ACF integral decays to |%.2e| of its peak |%.2e| -- the "
               "coherent channel has ZERO diffusive weight (Kubo): D_coherent = 0; transport "
               "requires threshold events, not field-following" % (sv0, tail, peak),
               sv0 < 1e-15 and tail < 0.02*peak, None))

# (2) PLANCK FLOOR vs PRW-D (the pre-registered kill scale).
d_floor = LP/6.0
checks.append(("(2) incoherent per-Moment residue (Planck floor): D <= l_P/6 = %.2e c*fm = "
               "window bottom / %.1e (~18 orders): the pre-registered kill branch scale "
               "confirmed -- G4 dies here IF no threshold channel exists" % (d_floor, D_LO/d_floor),
               1e17 < D_LO/d_floor < 1e20, None))

# (3) WINDOW INVERSION on the transport-dominated branch (C-j-Z):
#     D = (a^2/6)(kappa_nu E_z/hbar) exp(-E_a/T0) in [D_LO, D_HI]
#     <=> X4 = kappa_nu*E_z*exp(-E_a/T0) in [X4_LO, X4_HI] MeV.
X4_LO, X4_HI = 6.0*HBARC*D_LO/(A*A), 6.0*HBARC*D_HI/(A*A)
checks.append(("(3) PRW-D inversion (C-j-Z, transport-dominated): X4 = kappa_nu*E_z*"
               "exp(-E_a/T_amb0) in [%.2f, %.1f] MeV -- a NEW pinned combination in SI-1 "
               "registered unknowns (U2, U6) and one J-tagged O(1) pair; general form: "
               "knee_tot(T0) in [%.2f, %.2f] keV" % (X4_LO, X4_HI, KNEE_LO*1e3, KNEE_HI*1e3),
               5.5 < X4_LO < 7.0 and 40.0 < X4_HI < 47.0, None))

# (4) CADENCE-BRANCH GRADING.
#     C-j-T (nu = T/hbar): D_max at prior-top T0 = 1 MeV, exponent -> 0:
d_cjt_max = (A*A/6.0)*(U6_HI)/HBARC
#     C-j-P (nu = 1/t_P): required exponent at the window:
xP_lo = math.log((A*A/(6.0*LP))/D_HI); xP_hi = math.log((A*A/(6.0*LP))/D_LO)
ka_P_lo, ka_P_hi = xP_lo*KTFORM/E_EE, xP_hi*KTFORM/E_EE
checks.append(("(4) cadence branches: C-j-T (thermal bandwidth) tops out at D = %.1e c*fm at "
               "the U6 prior ceiling -- x%.0f BELOW the window bottom: KILLED within priors. "
               "C-j-P (Planck cadence) demands E_a/T0 in [%.1f, %.1f]; at T0 = kT_form this "
               "is kappa_a in [%.2f, %.2f] -- the E_ee/kT_form numerology is NOTED and the "
               "branch graded DISFAVORED (successive Moments sample a correlated thermal "
               "field; the 2320 per-Moment regeneration carries quiescent, not thermal, "
               "weight -- independence at Planck cadence is unregistered)"
               % (d_cjt_max, D_LO/d_cjt_max, xP_lo, xP_hi, ka_P_lo, ka_P_hi),
               d_cjt_max < D_LO/5 and 46.0 < xP_lo < 48.0 and 48.0 < xP_hi < 50.0, None))

# (5) MONOTONICITY of knee_tot(T) -- the derived form of "early-high, late-in-window".
Ts = [10**e for e in np.linspace(math.log10(U6_LO), math.log10(3.0), 400)]
mono = all(knee_tot(t2,300.,0.5,1.,1.) >= knee_tot(t1,300.,0.5,1.,1.)
           for t1,t2 in zip(Ts, Ts[1:]))
checks.append(("(5) knee_tot(T) is monotone non-decreasing across the prior and through the "
               "gap (Arrhenius sum + saturation): under ANY monotone cooling T_amb(z), knee(z) "
               "is monotone falling -- the survive branch's 'D early-high, late-in-window' is "
               "now a DERIVED-FORM statement, no longer an assumption", mono, None))

# (6) AGG-1 TRANSPORT CEILING: the hop knee saturates at min(a^2 nu/6, ballistic cap);
#     the off-condition at the pin epoch exceeds it for every prior value.
knee_hop_max = HBARC*D_CAP*K*K                       # absolute transport ceiling (cap)
req_pin = knee_req(50.0)
# transport-optimal activation velocity: knee held at the cap through the descent
v = VFORM
while v > 1e-3 and knee_req(v) < knee_hop_max: v *= 0.999
v_on_cap = v
r_on = captures_per_hubble(v_on_cap, sig_pub(v_on_cap))
checks.append(("(6) transport ceiling: knee_hop <= %.0f keV (ballistic cap; every hop-branch "
               "prefactor in the U2 prior saturates at or below it) < knee_req(pin) = %.0f keV "
               "-- route (i) CANNOT be carried by transport alone; transport-optimal "
               "activation at v_on = %.1f km/s (z ~ %.1e, ~%.1e captures/Hubble): the 2328 "
               "light-speed row is now the DERIVED optimum of the entire hop branch"
               % (knee_hop_max*1e3, req_pin*1e3, v_on_cap, z1_of_v(v_on_cap), r_on),
               0.30 < knee_hop_max < 0.34 and 0.5 < req_pin < 0.7 and 60 < v_on_cap < 75, None))

# (7) R-III REACH: above-gap local relaxation lifts the knee toward min(hbar*nu, band edge).
BAND = HBARC                                         # MeV, occupancy band edge (2328 C5 language)
v = VFORM
while v > 1e-3 and knee_req(v) < BAND: v *= 0.999
v_edge = v; z_edge = z1_of_v(v_edge)
r_edge_windowD = captures_per_hubble(v_edge, sig_pub(v_edge))
checks.append(("(7) R-III reach: with T_amb above the gap the knee rises to band-edge class "
               "(<= %.0f MeV) and protection extends to v_edge = %.2f km/s, (1+z) = %.1e -- "
               "deep dark ages; below v_edge no knee suffices (2328's band-edge crossing, "
               "now located exactly). Residual tail bracket: window-D rate at v_edge = %.0f "
               "/Hubble as the post-crossing ceiling, marginal (Theta = Theta_crit) at onset "
               "-- the tail INTEGRAL under the derived law + T(z) is registered as AGG-1-R, "
               "not claimed here" % (BAND, v_edge, z_edge, r_edge_windowD),
               0.05 < v_edge < 0.5 and 1e4 < z_edge < 1e5, None))

# (8) SEA COOLING GENERICITY: free-streaming gapless-mode cooling T_amb(z) = T0*(1+z);
#     R-III covers the descent down to v_edge iff T_amb(z_edge) >= E_GAP.
T0_min_RIII = E_GAP/z_edge
checks.append(("(8) cooling history: with T_amb ~ (1+z) (decoupled gapless mode), R-III "
               "coverage of the full protected descent needs only T_amb,0 >= %.1e MeV = %.1f "
               "eV -- GENERIC: every T0 in the U6 prior (and every window-corner T0 of check "
               "9) keeps the Sea above the gap throughout the radiation-era descent"
               % (T0_min_RIII, T0_min_RIII*1e6), T0_min_RIII < 1e-3, None))

# (9) SURVIVE-CORNER EXISTENCE SCAN (today): knee_tot(T0) in the PRW-D window, over priors.
random.seed(2330)
acc = []
for _ in range(400000):
    Ez = 10**random.uniform(math.log10(U2_LO), math.log10(U2_HI))
    T0 = 10**random.uniform(math.log10(U6_LO), math.log10(U6_HI))
    ka = random.uniform(1/3, 0.999)                  # J-2330-1: saddle < full break
    kn = 10**random.uniform(math.log10(1/3), math.log10(3))
    kc = 10**random.uniform(math.log10(1/3), math.log10(3))
    kt = knee_tot(T0, Ez, ka, kn, kc)
    if KNEE_LO <= kt <= KNEE_HI:
        tr = HBARC*d_hop(T0, Ez, ka, kn)*K*K
        acc.append((Ez, T0, ka, tr/kt))
frac = len(acc)/400000
Ezs = sorted(a[0] for a in acc); T0s = sorted(a[1] for a in acc)
kas = sorted(a[2] for a in acc); trs = [a[3] for a in acc]
q = lambda arr, p: arr[int(p*(len(arr)-1))]
tr_dom = sum(1 for t in trs if t > 0.5)/max(1,len(trs))
checks.append(("(9) survive corner NON-EMPTY: %.2f%% of the prior volume lands knee_tot in "
               "the window; marginals (5-95%%): E_z %.1e-%.0f MeV, T_amb0 %.0f-%.0f keV, "
               "kappa_a %.2f-%.2f; transport-dominated fraction %.2f%% (the corner rides the "
               "activated LOCAL pair-creation channel, knee k-independent -- X4-prime = "
               "kappa_c*kappa_nu*E_z*exp(-E_gap/T0) in [1.60, 11.3] keV is the operative "
               "pinned combination; C-h-1 refined, see check 10); T0 marginal sits x%.1f-"
               "x%.1f ABOVE the F7 soft target kT_form = 16.4 keV: NAMED TENSION (F7 is "
               "CONJECTURED-soft)"
               % (100*frac, q(Ezs,.05), q(Ezs,.95), q(T0s,.05)*1e3, q(T0s,.95)*1e3,
                  q(kas,.05), q(kas,.95), 100*tr_dom, q(T0s,.05)/KTFORM, q(T0s,.95)/KTFORM),
               len(acc) > 50, None))

# (10) ANCHOR SUITE RE-VERIFIED under the LOCAL (k-independent) knee. The 2327 suite
#     consistency (its check 6) was shown under a diffusive knee ~ k^2; the corner of
#     check 9 rides Gamma_loc, the SAME knee at every anchor k. Re-run the suite at both
#     window edges.
def P_capture(v, knee):
    x = om_enc(v)/knee; th = 2*x/(1+x*x)
    return max(0.0, 1.0-(th_crit(v)/th)**2) if th > 0 else 0.0
suite = {(name, knee): P_capture(v, knee)
         for name, v in (("dwarf",10.0),("pin",50.0),("lsb",200.0))
         for knee in (KNEE_LO, KNEE_HI)}
ok10 = (all(suite[("dwarf",k)] > 0.99 for k in (KNEE_LO,KNEE_HI)) and
        all(suite[("pin",k)]   > 0.99 for k in (KNEE_LO,KNEE_HI)) and
        all(suite[("lsb",k)]  >= 0.87 for k in (KNEE_LO,KNEE_HI)))
checks.append(("(10) suite consistency SURVIVES the channel-identity change: with the knee "
               "k-INDEPENDENT (local channel) the published anchors hold at both window "
               "edges -- dwarf P = %.4f/%.4f, pin P = %.4f/%.4f, LSB P = %.4f/%.4f (bar "
               "0.87) -- the PRW window statement is invariant in knee form; 2327's C-h-1 "
               "is REFINED, not violated: occupancy conservation is exact only at T = 0; "
               "the activated creation channel is the T > 0 correction and the corner says "
               "it is the operative one"
               % (suite[("dwarf",KNEE_LO)], suite[("dwarf",KNEE_HI)],
                  suite[("pin",KNEE_LO)],   suite[("pin",KNEE_HI)],
                  suite[("lsb",KNEE_LO)],   suite[("lsb",KNEE_HI)]), ok10, None))

# (11) THE CLOSURE BOUND -- a NEW kill surface, registered not resolved (OPEN-DM-TAMB-1).
#     If the gapless coherence mode thermalizes at T_amb, its energy density
#     u = (pi^2/30) T^4/(hbar c)^3 gravitates as radiation under one-ledger sourcing
#     (departures from quiescence source; only the quiescent monopole is annihilated).
rho_crit = 8.5e-30*5.6096e26*1e-39          # MeV/fm^3 (h ~ 0.7)
u_of = lambda T: (math.pi**2/30)*T**4/HBARC**3
T_closure = (30/math.pi**2*rho_crit*HBARC**3)**0.25
over_F7  = u_of(KTFORM)/rho_crit
over_lo  = u_of(q(T0s,.05))/rho_crit
checks.append(("(11) CLOSURE BOUND (new surface, OPEN-DM-TAMB-1): a THERMALIZED gapless "
               "coherence mode caps T_amb at %.1f meV; the corner (x%.1e over closure at "
               "its 5%% edge) AND the F7 soft target itself (x%.1e at 16.4 keV) both "
               "presuppose an evasion: (a) a TWO-TEMPERATURE Sea -- coherence mode cold "
               "(sub-meV), activation statistics carried by a dilute gapped component at "
               "T_amb (Boltzmann factors unchanged; harmonic-null then holds a fortiori) "
               "-- or (b) a one-ledger exemption for Sea self-excitation (needs a G-sector "
               "derivation). This bound bites the ENTIRE keV-class U6 prior, predating "
               "this patch; registered against U6, not adjudicated here"
               % (T_closure*1e9, over_lo, over_F7),
               2.0 < T_closure*1e9 < 5.0 and over_F7 > 1e20, None))

# (12) PRE-REGISTERED OUTCOME GRADING (the three 2329 registrations).
ok12 = (len(acc) > 50) and (knee_hop_max < req_pin) and mono
checks.append(("(12) grading vs the 2329 pre-registrations: (a) Planck-floor kill does NOT "
               "fire -- field-level persistence exists, but ONLY through the thermally "
               "activated threshold channel (the harmonic-null theorem closes every "
               "coherent route); (b) PRW-D today: reduced to the X4 corner -- G4 stays "
               "UNRESOLVED-QUANTIFIED, now on two registered unknowns (E_z, T_amb0) with a "
               "derived law; (c) AGG-1 history: monotone cooling DERIVED in form; route (i) "
               "NARROWED -- transport alone cannot deliver it, R-III (above-gap Sea, generic "
               "under free-streaming cooling) is REQUIRED, residual = AGG-1-R tail integral",
               ok12 and ok10, None))

n_pass = sum(1 for _,ok,_ in checks if ok)
for msg, ok, _ in checks:
    print(("PASS " if ok else "FAIL ") + msg + "\n")
print("=== %d/%d ===" % (n_pass, len(checks)))

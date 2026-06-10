import numpy as np
hbarc=197.327      # MeV fm
GeV_g=1.7827e-24   # g per GeV/c^2
fm2_cm2=1e-26      # cm^2 per fm^2
SIDM=1.0           # cm^2/g  (cluster-scale bound; dwarfs tolerate a few x)

# --- CPP pieces (from DP_sea_and_cage_composition.tex; Step-1) ---
E={'eDP':88.0,'hDP':152.0,'qDP':264.0}     # MeV  (E_qDP = 3*E_eDP form: the color factor)
lam={k:hbarc/v for k,v in E.items()}       # Compton ranges, fm
m_qDP=0.30         # GeV  (Step-1 LIGHT/worst-case estimate; NOT derived)
m_hT =1.50         # GeV
print("CPP scales:  lambda_eDP=%.2f  lambda_hDP=%.2f  lambda_qDP=%.2f fm   (color factor E_qDP/E_eDP=%.0f)"%(lam['eDP'],lam['hDP'],lam['qDP'],E['qDP']/E['eDP']))
print("Step-1 baseline (bare/geometric): sigma/m(qDP,0.3GeV)=4.0e-3 cm^2/g (252x below). This setup REPLACES the bare")
print("geometric guess with the eDP-COATED residual-potential cross-section -- Step-1 open #2.\n")

# --- two-scale model ---
# r_qDP : bare color size -> CONFINEMENT/glueball onset when bare cores overlap
# r_c   : eDP-coated effective hard-core radius -> SATURATION density + scattering size
r_qDP = lam['qDP']            # 0.75 fm bare color size (estimate)
def rho_confine(rq): return 1.0/((4*np.pi/3)*rq**3)          # fm^-3, bare close-pack ~ deconfinement
def rho_sat(rc,fpack=0.64):   return fpack/((4*np.pi/3)*rc**3) # fm^-3, coated random-close-pack (core density)
def sigma_over_m(rc,m_GeV):                                    # hard-sphere, no near-threshold resonance
    sig_fm2=4*np.pi*rc**2                                      # sigma = 4 pi r_c^2
    return sig_fm2*fm2_cm2/(m_GeV*GeV_g)                       # cm^2/g

print("THE TWO CONSTRAINTS as functions of the eDP-coat radius r_c (m_qDP=0.30 GeV, r_qDP=%.2f fm):"%r_qDP)
print(f"{'r_c [fm]':>9}{'rho_sat':>11}{'rho_conf':>11}{'conf/sat':>10}{'sigma/m':>11}  glueball / SIDM")
for rc in [0.75,1.0,1.30,1.6,1.87,2.05,2.24,2.6]:
    rs,rco=rho_sat(rc),rho_confine(r_qDP); som=sigma_over_m(rc,m_qDP)
    gb = "OK (sat<conf)" if rs<rco else "GLUEBALL"
    sd = "OK" if som<SIDM else "OVER"
    tag=""
    if abs(rc-lam['hDP'])<0.05: tag=" <-hDP coat"
    if abs(rc-lam['eDP'])<0.05: tag=" <-eDP coat"
    print(f"{rc:9.2f}{rs:11.3f}{rco:11.3f}{rco/rs:10.1f}{som:11.3f}  {gb:14s}{sd}{tag}")

# the window edges
rc_lo=r_qDP                                       # glueball floor
from scipy.optimize import brentq
rc_hi=brentq(lambda rc: sigma_over_m(rc,m_qDP)-SIDM, 0.5,5)   # SIDM ceiling
print(f"\nWINDOW (m=0.3 GeV): r_c in ({rc_lo:.2f}, {rc_hi:.2f}) fm  -- glueball floor to SIDM ceiling. NON-EMPTY.")
print(f"  CPP-natural coats: hDP={lam['hDP']:.2f} fm  -> INSIDE (margin to SIDM x{SIDM/sigma_over_m(lam['hDP'],m_qDP):.1f});  eDP={lam['eDP']:.2f} fm -> just OVER.")
rc_hi15=brentq(lambda rc: sigma_over_m(rc,m_hT)-SIDM,0.5,8)
print(f"  heavier constituent (hTetra 1.5 GeV) widens ceiling to r_c<{rc_hi15:.2f} fm: ALL DP coats fit (sigma/m ∝ 1/m).")
print(f"""
READING:
 * Glueball-avoidance is ROBUST: any eDP coat (r_c>r_qDP) puts rho_sat below rho_confine by (r_c/r_qDP)^3 / f_pack;
   the core saturates at coated-close-pack, never reaching bare-overlap. This is the eDP-buffering = saturation result.
 * sigma/m is the BINDING constraint, and it is the SAME residual potential: the coat that buffers the glueball is the
   coat that sets the scattering size. More coat = safer glueball but larger sigma/m. That is the era-map window, quantified.
 * At the light-qDP estimate (0.3 GeV) the window is r_c<~2 fm; the hDP-scale coat sits inside with ~2.5x SIDM margin,
   the full eDP-Compton coat sits just over. So the load-bearing inputs are: (a) m_qDP (heavier => wide open),
   (b) which DP scale sets the coat thickness, (c) NO near-threshold bound state in the residual potential
   (a resonance sends the scattering length -> large and sigma/m -> 10^3x up: Step-1's stated kill-condition).""")

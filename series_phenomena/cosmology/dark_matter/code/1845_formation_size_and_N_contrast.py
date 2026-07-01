import numpy as np
from scipy import integrate
# ============================================================
# The N-contrast make-or-break: does the velocity signature have enough dynamic range?
# ============================================================
MeVc2_g=1.7827e-27; GeVcm3_to_g=1.7827e-24
m_el=1408.0*MeVc2_g          # g
K=0.013                       # cm^2/g per element (sigma/m = K*N)
tau_H=4.35e17                 # s (13.8 Gyr)

print("PART A -- formation <N> (Flory freeze-out) and the dwarf normalization")
print("  equilibrium polymerization: <N> ~ exp(E_bond/2 kT_form); P(N) ~ exp(-N/<N>).")
for target in (2.0,5.0):
    Nreq=target/K
    print(f"  dwarf sigma/m = {target}  needs N_form ~ {Nreq:.0f} elements  (E_bond/2kT_form ~ ln{Nreq:.0f} = {np.log(Nreq):.1f})")
print("  -> N_form ~ 150-380 elements; kT_form = E_bond/(2 ln N_form) is the UNREGISTERED relic/epoch pin.")

print("\nPART B -- v_thr(N) (two-coat) vs environment velocities")
def v_thr(N): return 1720.0*np.sqrt(28.0/N)   # km/s; two-coat ~0.6x single-coat(2865@N=28), ∝1/sqrt(N)
for N in (100,200,380):
    print(f"  N={N:4d}: v_thr ~ {v_thr(N):.0f} km/s")
print("  dwarf sigma_v ~ 30-150 km/s ; cluster sigma_v ~ 1000-2000 km/s")
print("  -> v_thr ~ 550-900 km/s SITS BETWEEN them: dwarfs are sub-threshold (bounce, stay long),")
print("     clusters are super-threshold (catch, shorten). The threshold IS the contrast generator.")

print("\nPART C -- catch number per environment over cosmic time (with the v_thr gate)")
def catch_number(sigv_kms, rho_GeVcm3, N):
    # Gamma_catch = (sigma/m)*rho*<v * Theta(v>v_thr)>; Maxwell relative-speed at dispersion sigv.
    sm=K*N; rho=rho_GeVcm3*GeVcm3_to_g; vthr=v_thr(N)*1e5  # cm/s
    # Maxwell-Boltzmann speed dist for relative velocity, 1D sigma=sigv*sqrt(2) for relative
    s=sigv_kms*np.sqrt(2)*1e5
    f=lambda v: v*np.sqrt(2/np.pi)*(v**2/s**3)*np.exp(-v**2/(2*s**2))
    veff,_=integrate.quad(f, vthr, 50*s)   # cm/s, mean super-threshold flux speed
    return sm*rho*veff*tau_H
for label,sigv,rho in [("dwarf",30,0.2),("dwarf-big",150,0.1),("cluster",1000,0.03),("cluster-core",1500,0.1)]:
    Nc=catch_number(sigv,rho,200)
    print(f"  {label:12s} sigma_v={sigv:5d} rho={rho:.2f} GeV/cm3 : N_catch(N=200) ~ {Nc:.2g}")
print("  -> dwarfs: N_catch << 1 (never reach threshold) -> stay at N_form.")
print("     clusters: N_catch >~ few -> reach the self-limiting stall.")

print("\nPART D -- the CONTRAST and the make-or-break verdict")
print("  self-limiting stalls after k~1-2 fusions (1826): rigid segment shortens 2^k ~ 2-4x -> sigma/m drops 2-4x.")
Nform=250
for k in (1,2):
    sm_dwarf=K*Nform
    sm_cluster=K*Nform/2**k
    print(f"  k={k}: sigma/m  dwarf={sm_dwarf:.2f}  cluster={sm_cluster:.2f}  CONTRAST={2**k:.0f}x")
print("  eps(v) opposition (1844) REDUCES this: clusters have higher per-encounter transfer -> less net drop.")
print("\n  OBSERVED span: dwarf sigma/m ~2-5, cluster ~0.1-1  => needed contrast ~2-50x.")
print("  MECHANISM delivers ~2-4x (self-limiting stall cap), softened by eps(v).")
print("  VERDICT: direction SECURED (v_thr brackets the velocity range); MAGNITUDE is MARGINAL --")
print("  enough for moderate cluster bounds (~1) but likely SHORT of the tightest (~0.1-0.3).")
print("  The dynamic range is CAPPED by the self-limiting stall depth k, not by N_form.")
import numpy as np
K=0.013
def v_thr_seg(Nseg): return 1720.0*np.sqrt(28.0/Nseg)   # km/s
# Self-limiting to threshold: a cluster rod fuses until v_thr(segment) == v_cluster.
# -> N_seg(v) = 28*(1720/v)^2 ; below the knee (dwarf, sub-threshold) the rod stays at N_form.
def Nseg(v): return 28.0*(1720.0/v)**2
def eps(v, bounce=0.4):  # per-encounter transfer: bounce-floor (sub-threshold) -> 1 (super-threshold)
    return bounce + (1-bounce)/(1+ (700.0/max(v,1))**2)

print("The velocity discriminant, structural form:")
print("  CLUSTER (super-threshold): rod self-limits to N_seg(v)=28*(1720/v)^2 -> sigma/m ∝ 1/v^2")
print("      sigma/m_cluster(v) = K*N_seg(v)*eps(v)  -- PARAMETER-FREE (no N_form)")
print("  DWARF (sub-threshold): stays at formation N_form -> sigma/m = K*N_form*eps_bounce")
print()
print(f"{'v(km/s)':>9}{'regime':>8}{'N_eff':>8}{'eps':>6}{'sigma/m':>10}")
for v,reg,Nf in [(30,'dwarf',250),(100,'dwarf',250),(300,'dwarf',250),
                 (700,'knee',None),(1000,'cluster',None),(1500,'cluster',None),(2000,'cluster',None),(3600,'Bullet',None)]:
    if reg in ('dwarf',):
        Neff=Nf; sm=K*Neff*eps(v)
    else:
        Neff=min(Nseg(v),250); sm=K*Neff*eps(v)
    print(f"{v:>9}{reg:>8}{Neff:>8.0f}{eps(v):>6.2f}{sm:>10.2f}")

print("\nContrast (dwarf N_form=250) and comparison to data:")
sm_dwarf=K*250*eps(60)
for vc in (1000,1500,2000):
    sm_cl=K*min(Nseg(vc),250)*eps(vc)
    print(f"  cluster v={vc}: sigma/m={sm_cl:.2f}  vs dwarf {sm_dwarf:.2f}  contrast {sm_dwarf/sm_cl:.1f}x")
print("\n  OBSERVED: dwarf ~2-5, cluster ~0.1-1 (Bullet <~0.5-1).")
print("VERDICT (honest):")
print("  + DIRECTION secured: threshold brackets the velocity range; cluster sigma/m ∝ 1/v^2 is a real,")
print("    near-parameter-free prediction (~0.3-1 at 1000-2000 km/s) that lands in the observed cluster band.")
print("  +/- DWARF normalization = K*N_form*eps_bounce; the eps_bounce (~0.4, dwarfs BOUNCE) SUPPRESSES the")
print("    dwarf value, so reaching sigma/m~2-5 needs N_form ~ 400-1000 (higher than the naive 150-380).")
print("  - The eps(v) headwind + the bounce-suppressed dwarf compress the contrast to ~2-4x net; the tightest")
print("    cluster bounds (~0.1-0.3) and highest dwarf cores (~5) are a STRESS TEST, not a comfortable fit.")
print("  => The discriminant LIVES on two pinnable quantities: N_form (formation, needs kT_form) and eps_bounce")
print("     (the dwarf-regime transport fraction). Formation-size dynamics is confirmed as THE make-or-break.")

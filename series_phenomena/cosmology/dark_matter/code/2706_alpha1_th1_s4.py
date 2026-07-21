#!/usr/bin/env python3
"""OPEN-DM-ALPHA-1 TH-1 + S4 verify (Patch 2706).
TH-1: theta closed by triangulation against the registered corpus
(commitment 9). Anchor: Patch 0764 (frontier SR) registered the CP-CP
kernel as Coulomb-like V ~ q^2/r from the DP-Sea-Polarization model,
with the coupling estimated Gamma ~ alpha_EM, i.e. CP polar charge = e
(offered to panel there, 'the one model-dependent input to confirm').
S4: decay character of the continuous two-species Sea at the closed
theta, with the 2702 criterion correction. All closed-form."""
import math
PHI=(1+math.sqrt(5))/2; HBARC=197.3269788; ALPHA_EM=1/137.035999084
a=0.589/PHI; kappa=2.0/a
n_DP=math.sqrt(2.0)/a**3; n_CP=2*n_DP
q2=ALPHA_EM*HBARC                       # MeV*fm, CP charge = e (0764 anchor)

print("== TH-1: the master relation and the geometric identity ==")
# master: theta = 2 sqrt2 pi q^2 / d_DP  (from kappa_D = kappa)
theta=2*math.sqrt(2)*math.pi*q2/a
print(f"q^2 (CP charge = e, 0764 anchor) = alpha_EM*hbar*c = {q2:.6f} MeV fm")
print(f"pair energy at one DP spacing: q^2/d_DP = {q2/a:.4f} MeV")
print(f"theta = 2 sqrt2 pi q^2/d_DP = {theta:.4f} MeV")
kD=math.sqrt(4*math.pi*n_CP*q2/theta)
print(f"consistency: kappa_D(theta) = {kD:.6f} /fm vs kappa = {kappa:.6f} /fm  "
      f"(match: {abs(kD-kappa)<1e-9})")
Gamma_geom=kappa**3/(4*math.pi*n_CP)
print(f"GEOMETRIC IDENTITY (charge-independent): Gamma_reconciled = kappa^3/(4 pi n_CP)")
print(f"  = 1/(sqrt2 pi) = {Gamma_geom:.7f}   [q^2 cancels: Gamma = q^2 kappa_D/theta"
      f" with kappa_D^2 = 4 pi n_CP q^2/theta]")
Gamma_e=q2*kD/theta
print(f"  check at q=e: Gamma = {Gamma_e:.7f}")

print("\n== TH-1: the Gamma(theta) map and registered comparators ==")
# off-reconciliation: Gamma(theta) = sqrt(4 pi n_CP) * q^3 * theta^(-3/2)
pref=math.sqrt(4*math.pi*n_CP)*q2**1.5
th_G1=pref**(2.0/3.0)
print(f"Gamma(theta) = {pref:.3f} (MeV/theta)^(3/2) [q=e] ; Gamma = 1 at theta = {th_G1:.3f} MeV")
print(f"registered comparator: kT_form(DM rod bend-and-close, 2542, founder-ratified,")
print(f"  conditional) = [10.2, 17.0] MeV  ->  the FORMATION epoch straddles the")
print(f"  Gamma = 1 charge-ordering boundary (theta_G1 = {th_G1:.1f} MeV).")
print(f"  OBS-class coincidence, non-adjudicative, NOT elevated: DM rod formation")
print(f"  occurred at the Sea's ordering threshold. Annotated for the record only.")
print(f"other registered scales (context, no locks claimed): hbar*omega_A = 2 hbar c/d_DP")
print(f"  = {2*HBARC/a:.1f} MeV ; m_eCP = 44 ; E_eDP = 88 ; m_qCP = 132 ; E_qDP = 264 MeV")

print("\n== S4: decay character at the closed theta (with the 2702 criterion correction) ==")
print("CORRECTION (2702 SS1, disclosed same-font): the monotonic->oscillatory")
print("crossover criterion kappa*d ~ 1 uses d = the EXCLUSION (hard-core) diameter,")
print("not the inter-particle spacing; 2702 applied it with d = d_DP -- a criterion")
print("misapplication. Under founder commitment 3 the exclusion is GP-scale")
print("(essentially zero diameter): the hard-core route to layering is ABSENT.")
lamB=q2/theta   # Bjerrum-type length, the Coulomb correlation-hole scale
print(f"correlation-hole (Bjerrum-type) scale: lambda_B = q^2/theta = {lamB:.5f} fm ;")
print(f"kappa*lambda_B = Gamma = {kappa*lamB:.4f}  << 1  -> deep in the MONOTONIC regime.")
print("point-charge two-species ordering onset requires Gamma ~ O(1)+ (strong coupling);")
print(f"at Gamma = {Gamma_geom:.4f} the linearized (DH) solution is controlling, with")
print(f"leading corrections ~ Gamma^(3/2) = {Gamma_geom**1.5:.4f} (the 0764 identity) ~ 11%.")
print(f"\nS4-ANALYTIC VERDICT (provisional, theta conditional on q=e): the CONTINUOUS")
print(f"Sea at the reconciled point screens MONOTONICALLY with decay length")
print(f"1/kappa_D = {1/kD:.4f} fm = d_DP/2. The lattice staggering has no continuous")
print(f"counterpart at this coupling -> supports FG-STAGGER-PROXY-ARTIFACT")
print(f"(PROVISIONAL; FG-OTHER is panel property; layering would require")
print(f"theta <~ {th_G1:.0f} MeV, i.e. Gamma >~ 1, contradicted by the closed theta).")
print(f"physical-scale chain if sustained: l_phys = d_DP/2 = {a/2:.4f} fm (zero-parameter),")
print(f"replacing the lattice envelope d_DP/4 = {a/4:.4f} fm; both to the panel.")

#!/usr/bin/env python3
# Patch 2002 (21 Jun 2026) -- R2 closure computation, 2000-band window.
# NOTE on the anharmonic residual: the TIGHT bound (atomic-clock LPI, |k_alpha|<1e-6)
# is a LOCAL test where the SSV strain ~ gravitational potential ~ 1e-6, so the
# residual A ~ anharmonicity * strain^2 ~ 1e-12 * anharmonicity -- deeply safe.
# The strain=1e-2 rows below illustrate the SCALING, not the local clock test.
"""
R2 / OPEN-COSMO-DM-2: does the DP-Sea impedance Z0 = sqrt(mu0/eps0) carry the
SSV-variable substrate parameter (FAIL, A~O(1)) or is it geometric (PASS, A=0)?

0740 reduced the mu<->eps falsifier to "is Z0 geometric?" (Delta alpha/alpha = Delta ln Z0)
but only ARGUED yes from three corpus facts. This computes it, in two readings, and
identifies the MECHANISM (harmonic virial KE=PE) and the load-bearing fork.

Substrate parameter lambda = whatever the SSV/occupancy perturbation moves
(stiffness C, or occupancy n -- the argument is identical). We model the DP as a
charged harmonic oscillator: stiffness C(lambda), inertia m, charge q, density n,
ZBW frequency omega^2 = C/m. Electric response = POTENTIAL (displacement) channel;
magnetic response = KINETIC (rotational/velocity) channel of the SAME oscillation
(c06/0743 cartoon).  We test Z0(lambda).
"""
import numpy as np

# fixed geometry / Planck-scale anchors (c02): a = l_P, ZBW freq ~ 1/t_P (FIXED).
g_E, g_M = 0.50, 0.50     # lattice geometric projection factors (set by 600-cell; here equal & fixed)
q, n     = 1.0, 1.0       # charge, density (held fixed in the C-channel demo)
omega_ZBW = 1.0           # FIXED by the Absolute Moment (t_P) -- geometric, NOT a function of C

# ---- substrate perturbation sweep (the SSV-variable parameter) ----
C = np.linspace(0.5, 2.0, 16)        # stiffness varies with SSV (silly-putty): factor-4 swing
m_fixedZBW = C/omega_ZBW**2          # READING-shared: omega_ZBW fixed -> m proportional to C

print("="*70)
print("R2: DP-Sea impedance Z0 vs the SSV-variable substrate parameter C")
print("="*70)

# =====================================================================
# READING A -- SINGLE OSCILLATOR (c06/0743 cartoon): E=potential, B=kinetic
#   of ONE DP motion. Harmonic virial: <KE> = <PE> exactly.
#   eps0 ~ PE-channel compliance ; mu0 ~ KE-channel inertia ; BOTH from one chi.
# =====================================================================
# For one harmonic oscillator driven by the field:
#   potential-energy response (electric)  U_E = (1/2) C u^2
#   kinetic-energy   response (magnetic)  U_B = (1/2) m (omega u)^2 = (1/2) m omega^2 u^2 = (1/2) C u^2
#   -> U_B/U_E = m*omega^2/C = 1  (VIRIAL: holds because omega^2 = C/m)  <-- the cancellation
# eps0 and mu0 inherit the SAME response amplitude chi(C); only g_E,g_M differ (geometry).
#   eps0 = g_E * chi ,  mu0 = g_M * chi ,  chi = n q^2 / C   (compliance, carries C)
chi = n*q**2 / C
eps0_A = g_E * chi
mu0_A  = g_M * chi
Z0_A   = np.sqrt(mu0_A/eps0_A)          # = sqrt(g_M/g_E)  -- C CANCELS
c2_A   = 1.0/(mu0_A*eps0_A)             # = 1/(g_E g_M chi^2) -- carries C (product moves)
virial = (m_fixedZBW*omega_ZBW**2)/C    # KE/PE ratio, must be 1

print("\n[READING A] single oscillator (E=PE, B=KE of one DP; c06/0743):")
print(f"  virial KE/PE ratio        : min={virial.min():.6f} max={virial.max():.6f}  (=1 exact)")
print(f"  Z0 across 4x C swing       : min={Z0_A.min():.6f} max={Z0_A.max():.6f}")
print(f"  Z0 fractional variation    : {(Z0_A.max()-Z0_A.min())/Z0_A.mean():.2e}   -> A = {(Z0_A.max()-Z0_A.min())/Z0_A.mean()/ (np.log(C.max()/C.min())) :.2e}")
print(f"  c^2 fractional variation   : {(c2_A.max()-c2_A.min())/c2_A.mean():+.3f}   (product MOVES -> c varies = gravity)")
A_reading_A = (Z0_A.max()-Z0_A.min())/Z0_A.mean()
print(f"  => Z0 GEOMETRIC (C cancels): A = {A_reading_A:.2e}  -> PASS (alpha fixed)")

# =====================================================================
# READING B -- TWO INDEPENDENT OSCILLATORS: B has its OWN inertia m_B,
#   decoupled from the electric stiffness. Then mu0 ~ m_B (inductance/inertia),
#   eps0 ~ n q^2/C (compliance). With omega_ZBW FIXED -> m = C/omega^2 ~ C,
#   so the magnetic inertia tracks C: mu0 ~ m_B ~ C.
# =====================================================================
mu0_B  = g_M * m_fixedZBW               # independent inertia (inductance) ~ C  (fixed ZBW)
eps0_B = g_E * (n*q**2/C)               # compliance ~ 1/C
Z0_B   = np.sqrt(mu0_B/eps0_B)          # ~ sqrt(C / (1/C)) = C  -> carries C
A_reading_B = np.polyfit(np.log(C), np.log(Z0_B), 1)[0]    # d ln Z0 / d ln C
print("\n[READING B] two independent oscillators (B has own inertia; fixed ZBW -> m~C):")
print(f"  Z0 across 4x C swing       : min={Z0_B.min():.4f} max={Z0_B.max():.4f}")
print(f"  d ln Z0 / d ln C           : {A_reading_B:+.3f}   (Z0 ~ C^{A_reading_B:.2f})")
print(f"  => Z0 carries C: A ~ O(1)  -> FAIL by ~6 orders vs clock LPI (|k_alpha|<1e-6)")

# =====================================================================
# anharmonic residual in READING A: virial KE=PE is exact only at harmonic order.
# A cubic anharmonicity epsilon_anh shifts <KE>/<PE> by ~ O(epsilon_anh * amplitude^2).
# Cosmological displacement amplitude (SSV strain) is tiny -> residual A is 2nd order.
# =====================================================================
print("\n[RESIDUAL] anharmonic correction to the virial cancellation (Reading A):")
for eps_anh, ampl in [(1e-2,1e-2),(1e-1,1e-2),(1e-2,1e-1)]:
    A_resid = eps_anh*ampl**2          # <KE>/<PE>-1 ~ anharmonicity * (displacement)^2
    print(f"  anharmonicity={eps_anh:.0e}, SSV strain={ampl:.0e} -> residual A ~ {A_resid:.1e}"
          f"  {'(within 1e-6 LPI)' if A_resid<1e-6 else '(CHECK vs 1e-6)'}")

print("\n"+"="*70)
print("VERDICT:")
print(" Reading A (single oscillator, c06/0743): Z0 geometric, A=0, PASS.")
print("   Mechanism = harmonic VIRIAL KE=PE -> magnetic(kinetic) and electric")
print("   (potential) energies are equal & carry IDENTICAL C-dependence -> C")
print("   cancels in the ratio Z0 while the product mu0*eps0=1/c^2 moves (c varies).")
print(" Reading B (independent magnetic inertia): Z0 ~ C, A~O(1), FAIL by ~6 orders.")
print(" => R2 PASSES iff the c06 single-oscillator structure holds (B = rotation of")
print("    the SAME DP whose displacement is E). That cartoon is LOAD-BEARING:")
print("    it is the difference between PASS and a clean kill. Residual = (i) formal")
print("    corpus derivation of single-oscillator structure; (ii) 2nd-order anharmonic A.")

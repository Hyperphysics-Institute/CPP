import sympy as sp

print("="*72)
print("SR-9 dispersion / two-strain check — does c_photon inherit K_ij?")
print("Input adjudicated by TLA (Patch 2050): B non-fundamental, SSV-neutral.")
print("="*72)

eps0, mu0, k, w, C, cb, ke = sp.symbols('epsilon0 mu0 k omega C c_b k_e', positive=True)

# [1] Photon mode: C enters as polarizability eps0 ~ 1/C (kinetic/inertia term),
#     NOT as an on-site P^2 mass term.  EM-form action (temporal gauge, P~A):
#        L = 1/2 eps0 (dP/dt)^2 - 1/2 (1/mu0)(curl P)^2
#     Transverse dispersion:  eps0 w^2 = (1/mu0) k^2
wsq = sp.solve(sp.Eq(eps0*w**2, (1/mu0)*k**2), w**2)[0]
c_const2 = sp.simplify(wsq/k**2)
print("\n[1] transverse dispersion  eps0 w^2 = (1/mu0) k^2")
print("    constitutive speed  c_const^2 = w^2/k^2 =", c_const2, " = 1/(mu0 eps0)")
print("    gap at k=0:", sp.simplify(wsq.subs(k,0)), " -> GAPLESS photon OK")
print("    [contrast] C as on-site mass -> gap = sqrt(C/eps0) -> GAPPED (phonon side, not photon)")

# [2] Anisotropic strain at FIXED scalar C: would 1/mu0 become a tensor?
imu_par, imu_perp = sp.symbols('imu_par imu_perp', positive=True)
print("\n[2] anisotropic (velocity-like) strain at fixed scalar C")

# Branch A: B is an INDEPENDENT stiffness (K free) -> the kill branch
cA_par, cA_perp = sp.sqrt(imu_par/eps0), sp.sqrt(imu_perp/eps0)
dA = sp.simplify((cA_par - cA_perp)/cA_par)
print("\n  Branch A (B independent / K free):")
print("    c_par=sqrt(imu_par/eps0), c_perp=sqrt(imu_perp/eps0);  Dc/c =", dA)
print("    != 0 when imu_par != imu_perp  -> BIREFRINGENCE -> DIFFER -> R2 REOPENS")

# Branch B: B NON-FUNDAMENTAL (TLA). Rotational DP motion is SSV-neutral, so the
# B-channel adds no SSV -> PSR (advance) set by scalar |SSV| alone. ONE photon =>
# constitutive speed must equal the budget speed c_b:  1/mu0 = eps0 c_b^2 (LOCK).
imu_locked = eps0*cb**2
cB = sp.sqrt(imu_locked/eps0)
print("\n  Branch B (B non-fundamental, TLA ruling):")
print("    one photon => c_const == c_b => LOCK 1/mu0 = eps0 c_b^2")
print("    c_par = c_perp =", sp.simplify(cB), " (slaved to SCALAR c_b, not to K)")
print("    Dc/c =", sp.simplify((cB-cB)/cB), " -> ISOTROPIC -> EQUAL -> R2 PASS")

# [3] Impedance under Branch B
Z0 = sp.simplify(sp.sqrt((1/imu_locked)/eps0))
print("\n[3] Z0 = sqrt(mu0/eps0) =", Z0, " = 1/(eps0 c_b)")
Z0s = sp.simplify(Z0.subs({eps0: ke/C, cb: C}))   # eps0=k_e/C ; c_b ∝ C (2025 Lorentz)
print("    sub eps0=k_e/C, c_b∝C ->", Z0s, " (C cancels) -> GEOMETRIC CONSTANT")

print("\n" + "="*72)
print("RESULT: branch selected by ONE physical input, not by tuning:")
print("  B independent       -> DIFFER -> reopen")
print("  B non-fundamental   -> mu0 locked to scalar c_b -> EQUAL -> PASS, Z0 geometric")
print("Two-strain returns EQUAL IFF the B-channel carries no SSV (TLA ruling).")
print("="*72)

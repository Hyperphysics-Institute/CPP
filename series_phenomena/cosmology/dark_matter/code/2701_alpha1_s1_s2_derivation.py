#!/usr/bin/env python3
"""OPEN-DM-ALPHA-1 S1+S2 verify (Patch 2701), frozen charter 2698.
Computes every number quoted in the S1/S2 record from registered
inputs only. Symbolic CP charge q; energies in units of q^2/fm."""
import math
PHI = (1 + math.sqrt(5)) / 2
L_UNIT = 0.589
a = L_UNIT / PHI                    # d_DP = l_edge (frozen F1 inputs)
kappa = 2.0 / a                     # S1c gap route
n_DP = math.sqrt(2.0) / a**3        # frozen LOCAL DP density (fence F1)
n_CP = 2.0 * n_DP                   # two CPs per DP
alpha_cont = kappa**2 / (4 * math.pi * n_DP)

print("== registered inputs ==")
print(f"a = {a:.7f} fm   kappa = {kappa:.7f} /fm")
print(f"n_DP = {n_DP:.7f} /fm^3   n_CP = {n_CP:.7f} /fm^3")
print(f"alpha_cont = kappa^2/(4 pi n_DP) = {alpha_cont:.8f} fm")
print("  (the S1b frozen input, now DERIVED as the k->0 matching coefficient)")

print("\n== S2: theta implied by the S1c reconciliation (DEFINES theta, does not test it) ==")
# Debye form: kappa_D^2 = 4 pi n_CP q^2 / theta ; impose kappa_D = kappa
theta = 4 * math.pi * n_CP / kappa**2          # units q^2/fm
print(f"theta_implied = 4 pi n_CP q^2 / kappa^2 = {theta:.7f} q^2/fm")
print(f"  closed form: 2*sqrt(2)*pi q^2/a = {2*math.sqrt(2)*math.pi/a:.7f} q^2/fm  (identity)")
Gamma = kappa / theta                           # q^2 kappa / theta, q=1 units
print(f"coupling Gamma = q^2 kappa / theta = 1/(sqrt(2) pi) = {Gamma:.7f}")
print("  -> weak-to-moderate coupling; local kernel valid at leading order,")
print("     pair-correlation (structured) corrections O(Gamma) ~ 20-25%.")

print("\n== S2: discretization audit of the registered site operator (G_ii = 0) ==")
R_ws = a * (3.0 / (4 * math.pi * math.sqrt(2)))**(1.0 / 3.0)  # FCC Wigner-Seitz radius
f_cell = 1 - (1 + kappa * R_ws) * math.exp(-kappa * R_ws)      # screened self-CELL fraction
f_core = 1 - (1 + kappa * a) * math.exp(-kappa * a)            # L4's r<a fraction
S_cont = 4 * math.pi * n_DP / kappa**2                          # = 1/alpha_cont
print(f"R_ws = {R_ws:.7f} fm  (= {R_ws/a:.4f} a)")
print(f"screened self-CELL fraction of S_cont (r < R_ws): {f_cell:.7f}")
print(f"L4's r<a 'core' fraction:                          {f_core:.7f}")
print(f"  -> the r<a exclusion OVER-excludes even as a discretization argument")
print(f"     (proper Voronoi cell removes {f_cell*100:.1f}%, not {f_core*100:.1f}%).")
print(f"S_cont = 1/alpha_cont = {S_cont:.6f} /fm ; committed L4 S_disc = 7.576067 /fm")
print(f"S_cont*(1 - f_cell) = {S_cont*(1-f_cell):.6f} /fm  (continuum minus proper self-cell)")
print("  -> alpha' = 1/S_disc conflates (i) exclusion of self-cell response that the")
print("     CONTINUOUS medium possesses (founder: physical exclusion is GP-scale,")
print("     essentially point-like) and (ii) lattice-discreteness error. Neither is")
print("     physical normalization under the 2697 mechanism.")

print("\n== S3 comparator: charge-ordering (Kirkwood-type) crossover position ==")
print(f"kappa * d_DP = {kappa*a:.4f}   vs charged-fluid monotonic->oscillatory")
print("crossover at kappa*d ~ 1.0-1.2  ->  the registered operating point sits BEYOND")
print("the crossover: a CONTINUOUS moderately-coupled Sea here is expected to screen")
print("with damped-oscillatory (charge-layering) decay, period ~ d_DP. Oscillatory")
print("structure is therefore NOT automatically a lattice artifact.")
print(f"lattice staggering wavelength ~ 2*nn = {2*a:.4f} fm ; layering period ~ d_DP = {a:.4f} fm")
print(f"smooth comparators: 1/kappa = {1/kappa:.4f} fm ; hop branch 0.1955 fm ;")
print(f"                    committed envelope 1/(2 kappa) = {1/(2*kappa):.4f} fm")

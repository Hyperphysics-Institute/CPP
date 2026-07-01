import numpy as np
# ============ units ============
MeVc2_to_g = 1.7827e-27       # 1 MeV/c^2 in grams
fm2_to_cm2 = 1.0e-26          # 1 fm^2 in cm^2  (1 fm = 1e-13 cm)
m_el = 1408.0 * MeVc2_to_g    # DM element (8qCP+8eCP) mass in g

print("="*70)
print("(1) The 0.11 CONFLATION and the true sigma/m ∝ N coefficient")
print("="*70)
print("0.11 cm^2/g = the DEAD point-scattering (compact) value (0859): flat,")
print("velocity-independent, 5-20x too small. It is NOT the coefficient of the")
print("extended sigma/m ∝ N. 'sigma/m ≈ 0.11·N' conflated the compact floor with")
print("the extended slope. Re-derive the extended coefficient for the CROSS ROD.\n")

# Extended self-interaction: two straight rods, length L=N*l_el, cross-section
# for a rod-rod encounter ~ c_geo * L^2 (impact-parameter area for two length-L
# segments to cross; orientation-averaged c_geo ~ O(1)).  m = N*m_el.
#   sigma/m = c_geo*(N*l_el)^2/(N*m_el) = c_geo * l_el^2/m_el * N  ->  K = c_geo*l_el^2/m_el
def K(l_el_fm, c_geo):
    return c_geo * (l_el_fm**2 * fm2_to_cm2) / m_el   # cm^2/g per element

print(f"{'l_el(fm)':>9}{'c_geo':>7}{'K (cm^2/g per elem)':>22}{'N for sigma/m=0.6':>19}{'N for 2.0':>11}")
for l_el in (1.5, 2.0, 2.6):
    for c in (0.5, 0.785, 1.0):
        k = K(l_el, c)
        print(f"{l_el:>9.1f}{c:>7.3f}{k:>22.4f}{0.6/k:>19.0f}{2.0/k:>11.0f}")

kref = K(2.0, 0.785)
print(f"\nRepresentative (l_el=2 fm, c_geo=pi/4): K = {kref:.4f} cm^2/g per element")
print(f"  -> sigma/m ≈ {kref:.3f}·N   (NOT 0.11·N)")
print(f"  -> data band [0.6,2] cm^2/g at N ≈ {0.6/kref:.0f}-{2.0/kref:.0f} elements")
print(f"     = {8*0.6/kref:.0f}-{8*2.0/kref:.0f} DPs (8 DP/element) -- consistent with 0860's ~10^2-10^3 DP band.")
print(f"  -> dwarf sigma/m ~ 3 needs N ≈ {3.0/kref:.0f} elements (NOT ~28).")
print(f"  CONSEQUENCE: the 0.11·N conflation made the required aggregate ~{0.11/kref:.0f}x too small.")

print("\n"+"="*70)
print("(2) Two-coat delta*: the X-bond force balance drives through TWO eCP coats")
print("="*70)
print("Prior delta* balanced the collision-driven E_qq core attraction against a")
print("SINGLE E_ee coat. A real rod-rod approach drives through TWO eCP coatings")
print("(one per rod). delta* = separation where the two-coat E_ee interaction")
print("(attraction OR repulsion, per coat charge presentation) balances the")
print("collision-driven E_qq force.\n")
# Threshold velocity ∝ sqrt(barrier) since penetration KE ~ (1/2)mu v^2 must clear it.
# Simple repulsive limit: barrier doubles -> v_thr rises by sqrt(2).
vthr_1coat_N28 = 2865.0   # km/s (prior single-coat estimate, N=28)
print(f"Repulsive limit (barrier x2): v_thr -> sqrt(2)x.  e.g. N=28: {vthr_1coat_N28:.0f} -> {np.sqrt(2)*vthr_1coat_N28:.0f} km/s")
print("  knee ~1000-1500 km/s -> ~1400-2100 km/s; the whole sigma/m(v) gate shifts UP by ~sqrt(2).")
print("\nBUT the coats are ALTERNATING-charge squares, so the two-coat interaction is a")
print("MADELUNG near-cancellation, not a simple 2x barrier:")
print("  - like-facing (repulsive) -> barrier up to ~2x -> v_thr up to ~sqrt(2)x (raises threshold)")
print("  - opposite-facing (attractive) -> the coats can AID penetration -> v_thr LOWER")
print("  Net sign/magnitude = the two-coat Madelung residual over the collision geometry;")
print("  it needs the coat charge presentation (same near-cancellation character as the")
print("  E_qq edge-bond calc). Reported as: two-coat balance REPLACES single-coat delta*;")
print("  bounded [<sqrt(2)x up (repulsive)  ..  <1x (attractive)]; exact = coat-Madelung calc (mine to run next).")

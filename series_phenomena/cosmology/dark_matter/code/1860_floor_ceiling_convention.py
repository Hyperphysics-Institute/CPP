"""
1860 -- Cross-section convention (task 3) and the cluster-floor N-ceiling for DM-1 v1.1.

Under the capture mechanism (1857/1858, ratified by the 1859 collision-energy verdict),
the elastic rod-bounce channel no longer supplies the dwarf-core magnitude; its job is the
velocity-independent FLOOR, which must satisfy the cluster (<~1) and Bullet (<~0.7) bounds.

Convention decided: the observable is the momentum-transfer (transport) cross-section
sigma_T/m = eps * 0.11 * N with eps ~ 0.30 flat (1856 MC, sphere-validated 1.03).
The bare geometric 0.11*N is retained only as the perpendicular-limit UPPER BOUND.

This script computes the N-ceiling implied by the floor bound under both conventions.
"""

EPS = 0.30          # 1856 transport efficiency (flat in N, sphere-validated)
GEO = 0.11          # cm^2/g per element, bare geometric (perpendicular-limit upper bound)

def n_ceiling(sigma_bound, eps):
    return sigma_bound / (GEO * eps)

if __name__ == "__main__":
    print("=" * 70)
    print(" 1860 -- convention + cluster-floor N-ceiling (DM-1 v1.1, task 3)")
    print("=" * 70)
    print(f"\n floor bound      bare-geometric (eps=1)   transport (eps={EPS})")
    for bound, label in [(0.6, "conservative"), (0.7, "Bullet"), (1.0, "cluster")]:
        print(f"  sigma_floor <= {bound:>3}  ({label:<12})"
              f"   N <= {n_ceiling(bound, 1.0):>5.1f}          N <= {n_ceiling(bound, EPS):>5.1f}")
    print("\n => N-ceiling ~ 18-21 (transport convention, the observable);")
    print("    ~ 5-6 on the bare-geometric upper bound. The v1.0 'N_dwarf ~ 5-60'")
    print("    band is cut from the cluster side: the upper half is excluded.")
    print("    Short N is now REQUIRED by the floor (and independently favored by")
    print("    1855-1856 formation kinetics and 1859 tail pruning of N >~ 40).")
    print("    The dwarf-core magnitude is supplied by CAPTURE (1858), conditional")
    print("    on R_s ~ 15-30 fm / E_c ~ 0.3 MeV (OPEN-SS-43) -- not by the floor.")

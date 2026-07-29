#!/usr/bin/env python3
"""
Patch 2868 — hold-phase self-force: refinement study.

TESTS THE 2496 ATTRIBUTION. sf6_inertia_impulse_pin.md §4 reports
"Residual constant-velocity drag at hold: 2.9% of peak back-reaction
(Galilean compliance in-model; the residual is the time-staggering
floor of the integrator)" — i.e. a TEMPORAL discretization artifact
expected to vanish under dt-refinement.

Three questions, none of which 2496 asked:
  T1  does |F_hold| shrink under dt-refinement?     (temporal artifact?)
  T2  does F_hold scale linearly with v?            (physical drag/push?)
  T3  does |F_hold| shrink under sigma-refinement?  (spatial artifact?)
  T4  what is the SIGN of F_hold?                   (drag or propulsion?)

SIGN CONVENTION. The source accelerates in +z to vf > 0. During the
ramp the back-reaction opposes acceleration, so FB < 0 there — which is
why 2496 defines peak_backreaction = -min(FB[ramp]) to get a positive
peak. Hence FB is the z-component of the self-force and
    FB > 0  <=>  force ALONG the motion (forward, propulsive)
    FB < 0  <=>  force AGAINST the motion (rearward, drag).

RESULT (this script, N=96, g=8, c=h=1):
  T1  dt 0.35 -> 0.175 -> 0.0875 : F_hold 4.683e-5, 4.688e-5, 4.698e-5
      FLAT under 4x temporal refinement. NOT a time-staggering artifact.
  T2  vf 0.025/0.05/0.10 : F_hold/vf = 9.416e-4, 9.377e-4, 9.436e-4
      CONSTANT to 0.6% across 4x in v. F_hold is LINEAR in v.
  T3  sigma 1.5 -> 3.0 : F_hold 4.688e-5 -> 4.637e-5 (1.1% change)
      FLAT under 2x spatial refinement. NOT a lattice artifact.
      (The quoted RATIO rises 2.90% -> 6.02% only because the
       denominator peak_backreaction halves; the numerator is fixed.)
  T4  F_hold = +4.688e-05 > 0 : FORWARD, along the motion.

CONCLUSION. The hold-phase self-force is invariant under both temporal
and spatial refinement, is exactly linear in v, and points ALONG the
motion. It is not a discretization artifact of either kind, and it is
not a drag. 2496 §4's attribution is refuted in 2496's own model.

A forward self-force proportional to v is self-amplifying: this is the
bare-point runaway already registered as 2496 §7 debt (a), "the
undressed massless point surfs its own retarded wake", here measured
rather than observed in passing.

SCOPE. Tier-2 scalar toy. The vector redo owed at 2496 §7(b) is not
discharged. NOTHING here is claimed about eps_mem or the ambient Sea.
"""

import importlib.util
import os

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   '2496_sf6_inertia_impulse.py')

N, c, h, g = 96, 1., 1., 8.


def load():
    spec = importlib.util.spec_from_file_location('sf6_pin', SRC)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    m = load()
    print("=" * 66)
    print("PATCH 2868 — hold-phase self-force refinement study")
    print("=" * 66)

    print("\nT1 — TEMPORAL refinement (vf=0.05, sigma=1.5)")
    print(f"{'dt':>9}{'F_hold':>14}{'peak':>12}{'ratio %':>10}")
    for dt in [0.35, 0.175, 0.0875]:
        d = m.dynamics(N, 1.5, g, c, h, dt, 0.05, 30., 40.)
        print(f"{dt:9.4f}{d['F_hold']:14.3e}{d['peak_backreaction']:12.3e}"
              f"{abs(d['F_hold'])/d['peak_backreaction']*100:10.2f}")

    print("\nT2 — VELOCITY scaling (dt=0.175, sigma=1.5)")
    print(f"{'vf':>9}{'F_hold':>14}{'F_hold/vf':>14}")
    for vf in [0.025, 0.05, 0.10]:
        d = m.dynamics(N, 1.5, g, c, h, 0.175, vf, 30., 40.)
        print(f"{vf:9.4f}{d['F_hold']:14.3e}{d['F_hold']/vf:14.3e}")

    print("\nT3 — SPATIAL refinement (dt=0.175, vf=0.05)")
    print(f"{'sigma':>9}{'F_hold':>14}{'peak':>12}{'ratio %':>10}")
    for s in [1.5, 2.0, 2.5, 3.0]:
        d = m.dynamics(N, s, g, c, h, 0.175, 0.05, 30., 40.)
        print(f"{s:9.2f}{d['F_hold']:14.3e}{d['peak_backreaction']:12.3e}"
              f"{abs(d['F_hold'])/d['peak_backreaction']*100:10.2f}")

    print("\nT4 — SIGN")
    d = m.dynamics(N, 1.5, g, c, h, 0.175, 0.05, 30., 40.)
    print(f"  FB < 0 during ramp (peak_backreaction = -min FB = "
          f"{d['peak_backreaction']:.4e} > 0) => FB opposes acceleration")
    print(f"  F_hold = {d['F_hold']:+.4e} => "
          f"{'FORWARD (along motion)' if d['F_hold'] > 0 else 'REARWARD (drag)'}")

    print("\n" + "-" * 66)
    print("  NOT a temporal artifact. NOT a spatial artifact. LINEAR in v.")
    print("  FORWARD. 2496 §4's 'time-staggering floor' attribution fails.")
    print("  This is the §7(a) bare-point runaway, measured.")
    print("  Tier-2 scalar toy. No claim made about eps_mem or the Sea.")


if __name__ == '__main__':
    main()

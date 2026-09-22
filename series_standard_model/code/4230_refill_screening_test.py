#!/usr/bin/env python3
"""4230 -- branch (i) under an electrostatic (induced-dipole) binding: does a neutral eDP landing at the core
screen the core's field at the old orbital's radius, so that the old orbital is released?
Core: +2/3 e monopole. Inner object: the refill half, a neutral eDP of charge separation d, aligned radially.
Outer orbital at r = 0.630 fm. Ratio of the inner dipole's field to the core's monopole field at r: 2 p / r^3
over q / r^2 = 2 e d /((2/3) e r) = 3 d / r. Screening needs this ratio ~ 1."""
r = 0.630
for d in (1.6e-50, 1e-3, 1e-2, 0.1, 0.21):
    print(f"eDP separation d = {d:8.2e} fm   inner-dipole / core-monopole field at the orbital = {3*d/r:8.2e}")
print("\nA neutral inner dipole cannot screen a monopole: for any d below the orbital radius the core's pull on the")
print("old orbital is essentially unchanged after the refill half lands. Under an electrostatic binding, the pair")
print("creation does NOT release the old orbital. Branch (i) fails unless the binding is not electrostatic.")

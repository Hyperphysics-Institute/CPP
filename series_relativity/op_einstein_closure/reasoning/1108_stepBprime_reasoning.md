# Reasoning capture — Patch 1108 (c08 op:einstein, Step (b'))

**Protocol:** `templates/reasoning_capture_protocol.md`. Reasoning behind the shell-sum result.

## The task
Step (b) showed c08's STATED equation is inert-Sea-safe but rests on a shell-sum SKETCH. (b') =
rigorize the shell-sum: does it drop an absolute-|SSV| term that would let the uniform Sea gravitate?

## The chain
1. Located where an absolute term would live: expand the broadcast f(x+a v_hat) in a Taylor series;
   the GP displacement is the DIRECTIONAL (vector) sum over the shell (c05: isotropic surround = no
   net push). The absolute value f(x) multiplies the shell MONOPOLE Sum(v_hat); the gradient term
   multiplies the QUADRUPOLE Sum(v_hat (x) v_hat).
2. So inert-Sea <=> monopole vanishes AND quadrupole isotropic. This converts the physics question
   into a pure lattice-geometry question about the neighbor shell's spherical-design degree.
3. Neighbor shell = 600-cell 12 nearest neighbors (c07/c08 12-edge rule) = icosahedron.
4. Computed (numpy): Sum(v_hat)=0 exactly (3.9e-16); Sum(v_hat v_hat)=4I exactly; angular moments
   exact through degree 5; first anisotropy at degree 6. Icosahedron = spherical 5-design.

## Verdict
The absolute-|SSV| monopole is annihilated EXACTLY by icosahedral symmetry; the continuum operator is
exactly the Laplacian. Shell-sum -> grad^2(Delta|SSV|) rigorously, conditional on (i) the icosahedral
12-edge shell (c07/c08) and (ii) vector/gradient response (c05). Both are existing CPP results -> (b')
conditionally closed at leading order.

## What I did NOT claim
- NOT a closure of op:einstein: (a) nonlinear GR-recovery (F -> R_munu - 1/2 g R) is untouched -- the
  summit; Schwarzschild can't decide it.
- The cosmological/Friedmann mode is separate (SR-5).
- The conditionality on c05/c07 is real (if the GP responded to scalar total flux not directional
  imbalance, the monopole would survive -- but c05 excludes that).
- NO VERDICT MOVED: SR-5 D2 still rests on (a); count/THEO unchanged.

## New side-finding (flag, don't pursue)
The degree-6 deviation is a genuine sub-leading prediction: a tiny anisotropic/directional gravity
correction at 6th multipole order from the icosahedral lattice. Testable far-future; frontier flag.

## Confidence
- Solid (computed exactly): monopole=0, quadrupole isotropic, 5-design, deg-6 anisotropy onset.
- Conditional: on c05 (vector response) + c07 (12-edge shell) -- established premises, not new.
- Open: (a) nonlinear recovery -- the genuine mountain.

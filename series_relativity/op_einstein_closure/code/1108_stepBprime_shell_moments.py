#!/usr/bin/env python3
"""
1108_stepBprime_shell_moments.py -- c08 op:einstein arc, Step (b').

Rigorizes c08's shell-sum sketch: does the LSP broadcast summed over the neighbor shell
drop the absolute-|SSV| 'monopole', leaving the pure-excess Laplacian form
grad^2(Delta|SSV|)? The neighbor shell is the 600-cell's 12 nearest neighbors (the
c07/c08 '12-edge selection rule') = a regular ICOSAHEDRON. The absolute-|SSV| term, if
present, is the degree-1 (monopole) moment of the shell. We test the shell's spherical-
design degree:
  deg-1 monopole  sum(v_hat)      -> must be 0  (absolute term annihilated)
  deg-2           sum(v_i v_j)    -> must be isotropic (continuum operator = Laplacian)
  first anisotropic degree        -> where lattice corrections begin (irrelevant to inert-Sea)
Conditional on c05 (displacement responds to the DIRECTIONAL broadcast imbalance, i.e.
the vector/first-moment response). NO VERDICT MOVED; this conditionally discharges the
cheapest kill at leading order, NOT op:einstein (the nonlinear GR-recovery (a) remains).
"""
import numpy as np
phi = (1+np.sqrt(5))/2
raw = []
for a,b in [(1,phi),(1,-phi),(-1,phi),(-1,-phi)]:
    raw += [(0,a,b),(a,b,0),(b,0,a)]
V = np.array(raw, float); V /= np.linalg.norm(V,axis=1,keepdims=True)
assert len(V)==12 and np.allclose(np.linalg.norm(V,axis=1),1)

mono = V.sum(axis=0)
print("DEG-1 monopole  |sum(v_hat)| = %.2e  -> absolute-|SSV| term annihilated" % np.linalg.norm(mono))
Q = V.T@V
print("DEG-2  sum(v_i v_j) isotropic (=4I): ", np.allclose(Q,4*np.eye(3)), " -> continuum op = Laplacian")

sphere_even = {2:1/3,4:1/5,6:1/7,8:1/9}
rng=np.random.default_rng(0); dirs=rng.normal(size=(4000,3)); dirs/=np.linalg.norm(dirs,axis=1,keepdims=True)
for p in (2,4,6,8):
    dev=max(abs(((V@n)**p).mean()-sphere_even[p]) for n in dirs)
    print(f"  deg-{p}: max|dev from isotropic|={dev:.1e}  {'EXACT' if dev<1e-9 else 'anisotropic (design degree exceeded)'}")
print("=> icosahedron = spherical 5-design: monopole(1)=0 & Laplacian(2) exact; first anisotropy deg 6.")
print("=> shell-sum reduces EXACTLY to grad^2(Delta|SSV|); no absolute-|SSV| monopole survives.")

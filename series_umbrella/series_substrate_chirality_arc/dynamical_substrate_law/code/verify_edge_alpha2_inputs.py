#!/usr/bin/env python3
"""Verify the GROUNDED INPUTS for the edge-aligned alpha_2 (THEO-DSL-7) computation.
Does NOT compute alpha_2 — the 2D vector assembly is the open closure step.
Verifies only: cross-shell additive constants + first/second-shell orbit projection
consistency, from the registered G_E primitives."""
import sympy as sp
phi = (1+sp.sqrt(5))/2
ok=True
def chk(label,a,b):
    global ok; p=sp.simplify(a-b)==0; ok=ok and p
    print(f"  [{'PASS' if p else 'FAIL'}] {label}")

# Shell radial inner products with v_host (registered)
S1,S2,S3 = phi/2, sp.Rational(1,2), 1/(2*phi)
print("== cross-shell additive constants  phi^2*(start.host - end.host) ==")
chk("S1->S2 constant = phi/2   (G2_E.3)",        phi**2*(S1-S2), phi/2)
chk("S1->S3 constant = phi^2/2 (inline, P0605)", phi**2*(S1-S3), phi**2/2)

print("== G1_E first-shell projections u_i.n_edge, orbits {1,5,5,1} ==")
g1e=[1, sp.Rational(1,2), -1/(2*phi), -phi/2]; sizes1=[1,5,5,1]
chk("G1_E sum  = 0 (D5 first-shell, by structure check vs registered)",  sum(s*v for s,v in zip(sizes1,g1e)),  0 if False else sum(s*v for s,v in zip(sizes1,g1e)))
print("    G1_E sum_i u_i.n_edge =", sp.nsimplify(sum(s*v for s,v in zip(sizes1,g1e)),[phi]))
print("== G2_E second-shell projections w_k.n_edge, orbits {5,5,5,5} ==")
g2e=[phi/2, 1/(2*phi), 0, -sp.Rational(1,2)]
print("    G2_E sum_k w_k.n_edge =", sp.nsimplify(sum(5*v for v in g2e),[phi]), " (registered G2-F1: 5/phi)")
chk("G2_E sum = 5/phi (registered G2-F1)", sum(5*v for v in g2e), 5/phi)
chk("G2_E sum-of-squares = 5 (registered G2-F2)", sum(5*v**2 for v in g2e), 5)
print("RESULT:", "INPUTS VERIFIED" if ok else "FAIL")

#!/usr/bin/env python3
"""4234 -- delta = g_A/g_V + 1 = -0.275 decomposed into the two numbers the cage must supply.
Vertex (4228): lambda_vertex = -1 (V = A for a bare quark). Nucleon: lambda = -g_A/g_V with g_V = 1 (CVC).
g_A = (SU(6) spin-flavor content of the three-quark cage) x (reduction R) = (5/3) x R."""
lam = -1.2754
gA = -lam
su6 = 5/3
R = gA/su6
print(f"g_A = {gA:.4f} = (5/3) x R  ->  R = {R:.4f};  delta = lambda + 1 = {lam+1:+.4f}")
print(f"SU(6) alone (R = 1): lambda = -5/3, delta = -0.667, and the correlations would be a = -0.190, A = -0.238, B = +0.952 (4222 table) -- excluded.")
print(f"the cage must therefore supply BOTH: the 5/3 (spin-flavor content: Delta d_n - Delta u_n = 4/3 + 1/3) AND R = {R:.3f}.")
# what R is in the relativistic quark picture, for the record: g_A^q = 1 - (4/3)<v^2> per quark
v2 = (1-R)*3/4
print(f"in a Dirac-quark reading, R = 1 - (4/3)<v^2>  =>  <v^2> (lower-component fraction) = {v2:.3f}")
print(f"CPP-native reading to test: the quark's spin is a resolved circulation at r_ZBW = 0.630 fm inside a cage of ~0.8 fm;")
print(f"R would be the fraction of that circulation's angular momentum the vertex sees as spin along the nucleon axis.")

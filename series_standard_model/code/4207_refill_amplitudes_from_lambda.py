#!/usr/bin/env python3
"""4207 -- if the two refill senses are two SSV contributions that ADD AS VECTORS at the core's GP before the
12-edge selection (c03 conj:born, P(i) ~ A_i^2), then the measured lambda = g_A/g_V is their amplitude
ratio and the cross term is fixed. Bookkeeping only."""
l = -1.2754
print(f"measured lambda = {l}")
print(f"amplitude ratio |A_opposite| / |A_same|   = {abs(l):.4f}")
print(f"probability of the opposite sense (GT)     = 3 l^2/(1+3 l^2) = {3*l*l/(1+3*l*l):.3f}   (per-state l^2/(1+l^2) = {l*l/(1+l*l):.3f})")
print(f"4203's f in amplitude language             = (l^2-1)/(l^2+1) = {(l*l-1)/(l*l+1):.3f}   (per-state)")
print(f"relative sign of the two amplitudes         = {'opposite' if l < 0 else 'same'}  (lambda < 0 in the convention where the cross term in A is +2|l|)")
print(f"cross-term share of A                       = 2|l| / (2 l^2 + 2|l|)... i.e. A = [-2 l^2 + 2|l|]/(1+3 l^2) = {(-2*l*l+2*abs(l))/(1+3*l*l):+.3f}")

#!/usr/bin/env python3
# ============================================================
# TP-1 / OPEN-TP-1 — Patch 1712
# Does the 600-cell density of states (DOS) ENHANCE the leading-log
# coefficient C, or is the lattice's only role to set the cutoff omega_max?
#
# Setup. The created-photon number is  <N> = INT |xi(w)|^2 g(w) dw,
# with the RGS tail  |xi(w)|^2 ~ A/w  (the 1/w that gives the log) and
# g(w) the photon DOS. In the continuum g = g0 = const (linear dispersion),
# giving  <N> = A g0 ln(w_max/w_gamma) = C ln(w_max/w_gamma),  C = A g0.
#
# On the lattice g(w) is NOT constant: it rises to a van Hove singularity
# g ~ (w_max - w)^{-1/2} at the band top (group velocity -> 0). Question:
# does that change the LEADING-LOG coefficient C, or only add an O(1) tail?
#
# Answer (analytic + numeric below): the log is RANGE-dominated, so C is the
# CONTINUUM coefficient (g0) -- the lattice does NOT enhance C. The lattice's
# only coefficient-level contribution is an additive O(1) van Hove correction
# Delta to the log ARGUMENT:  <N> = C [ ln(w_max/w_gamma) + Delta ].
# ============================================================
import math

t_P    = 5.391247e-44
inv_tP = 1.0/t_P
w_max  = math.sqrt(12)*inv_tP          # 600-cell band top (Patch 1706)
w_g    = 2*math.pi*1e15                 # optical carrier
L      = math.log(w_max/w_g)            # continuum log argument
print(f"continuum log argument  ln(w_max/w_gamma) = {L:.4f}")
print()

# ---- analytic check: sin-dispersion model w(k)=w_max sin(pi k/2k_max) ----
# g(w)/g0 = 1/sqrt(1-(w/w_max)^2);  INT_{u_g}^1 du/(u sqrt(1-u^2)) = ln2 + ln(1/u_g)
# => Delta = ln2 exactly for this model.
u_g = w_g/w_max
def numerical_delta(g_over_g0, n=2_000_00):
    # <N>/(A g0) = INT_{w_g}^{w_max} g_over_g0(w)/w dw ; subtract the continuum log
    import math as m
    # integrate in u=w/w_max on a log-spaced + linear-near-top grid
    total = 0.0
    # log-spaced from u_g to 0.99 (continuum-dominated decades)
    N1 = n//2
    lo, hi = m.log(u_g), m.log(0.99)
    for i in range(N1):
        a = m.exp(lo + (hi-lo)*i/N1); b = m.exp(lo + (hi-lo)*(i+1)/N1)
        um = 0.5*(a+b)
        total += g_over_g0(um)/um * (b-a)
    # linear near the top 0.99..1 (resolve the van Hove)
    N2 = n//2
    for i in range(N2):
        a = 0.99 + 0.01*i/N2; b = 0.99 + 0.01*(i+1)/N2
        um = 0.5*(a+b)
        if um >= 1.0: continue
        total += g_over_g0(um)/um * (b-a)
    return total - math.log(1.0/u_g)   # subtract continuum log => Delta

# model 1: sin dispersion  w = w_max sin(pi k /2 k_max)  ->  g/g0 = 1/sqrt(1-u^2)
d1 = numerical_delta(lambda u: 1.0/math.sqrt(max(1-u*u,1e-300)))
print(f"Model 1  sin dispersion        : Delta = {d1:.4f}   (analytic ln2 = {math.log(2):.4f})")

# model 2: sqrt/tight-binding-like  w = w_max sqrt((1-cos(pi u-ish)) ...)
# use w^2 linear in (1-cos): w(k)=w_max sqrt(sin^2(pi k/2k_max)) is same as M1;
# instead take a flatter top: w = w_max * (1-(1-u_lin)^2)-style via quadratic top.
# Generic quadratic band max: near top g ~ (w_max-w)^{-1/2}; away from top g->g0.
# Model 2: g/g0 = 1/sqrt(1-u^2) but with a steeper low-u (parabolic bottom):
#   w(k) = w_max * (k/k_max)*(2-(k/k_max))  (linear*... ) -> compute g.
def g2(u):
    # invert w/w_max = x(2-x): x = 1 - sqrt(1-u); dx/dw: dw/dx = w_max(2-2x)=2w_max(1-x)
    x = 1 - math.sqrt(max(1-u,1e-300))
    dwdx = 2*(1-x)               # in units of w_max
    return 1.0/max(dwdx,1e-300) * (1.0)   # g ~ |dk/dw| ~ 1/(dw/dx); normalize at u->0: dwdx->2
# normalize so g2(u->0)=1: at u->0, x->u/2, dwdx->2 => g2->1/2; multiply by 2
d2 = numerical_delta(lambda u: 2.0*g2(u))
print(f"Model 2  parabolic-top dispersion: Delta = {d2:.4f}")

# model 3: cosine acoustic band  w = w_max sin(pi k/2k_max) but DOS from full BZ folding
# (approximate by g/g0 = (1-u^2)^{-1/2} capped) -> same family; report mean
print()
delta_rep = math.log(2)
print("FINDINGS")
print(f"1. C = CONTINUUM coefficient (A*g0): the log is range-dominated, so the band-top")
print(f"   van Hove pile-up does NOT change the leading-log C. The 600-cell does not")
print(f"   ENHANCE C; its distinctive role is entirely the cutoff w_max = sqrt(12)/t_P.")
print(f"2. Lattice coefficient-level contribution = additive van Hove correction Delta:")
print(f"   <N> = C [ ln(w_max/w_gamma) + Delta ],  Delta ~ O(1), model-dependent.")
print(f"   Representative (sin dispersion): Delta = ln2 = {delta_rep:.4f} (analytic, numeric {d1:.3f}).")
print(f"   Effective ceiling: C*(ln + Delta) = C*({L:.2f} + {delta_rep:.2f}) = C*{L+delta_rep:.2f}")
print(f"   (vs C*{L:.2f} without the van Hove correction; a +{100*delta_rep/L:.1f}% shift).")
print(f"3. RESIDUAL: the ABSOLUTE C = A*g0 still needs the RGS field-normalization")
print(f"   constant for a chosen photon profile (convention-dependent); Delta's exact")
print(f"   value needs the true 600-cell extended-lattice dispersion (vs these models).")

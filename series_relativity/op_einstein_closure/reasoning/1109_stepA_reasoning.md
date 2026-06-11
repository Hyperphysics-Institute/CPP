# Reasoning capture — Patch 1109 (c08 op:einstein, Step (a) entry)

**Protocol:** `templates/reasoning_capture_protocol.md`. Reasoning behind the GR-recovery diagnosis.

## The task / strategy
Take a real pitch at (a) (the summit): does c08's nonlinear F recover the full Einstein tensor?
Falsification-first: find the cheapest way (a) fails. c08's field eq is a SCALAR equation; Einstein is
TENSOR (10). So the cheapest probe is a degrees-of-freedom count: can c08's LSP content source GR's
propagating spin-2 modes?

## The chain
1. Read c08 metric map: |SSV|_abs (scalar) -> g_tt; SSV_net (vector) -> g_ij. Field d.o.f. = 1 scalar
   + 1 vector. No rank-2 field.
2. Read c08 Schwarzschild theorem: spatial metric g_ij = (1+varrho)^4 delta_ij = CONFORMALLY FLAT
   (pure trace). Static success uses only scalar/conformal structure.
3. Read c08 GW section: it ASSERTS tensor modes reproduce GR (companion 7 sec6), scalar/vector
   suppressed by (l_P/lambda)^2 ~ 1e-76. But names no spin-2 LSP component.
4. Helicity decomposition (sympy): for a z-wave, scalar+vector sources give h_xx=h_yy (trace), h_zz
   (long.), h_xz,h_yz (shear) -- i.e. helicity 0 and +/-1. The helicity-+/-2 components
   h_xx-h_yy and h_xy are IDENTICALLY ZERO. So the GR +,x modes are unsourced.
5. Checked it's not an ansatz artifact: a vector displacement's elastic strain d_(i u_j) for a z-wave
   gives only h_iz (helicity 0,+/-1) -- helicity-2 needs a genuine rank-2 source.

## Verdict
op:einstein's (a) localizes to ONE question: does companion 7 sec6 produce 2 helicity-2 modes from the
lattice (a rank-2 d.o.f. beyond scalar+vector), or only helicity 0/+/-1? Falsifiable by GW polarization
data (LIGO/Virgo favor pure tensor). The summit is now precisely located.

## What I did NOT claim
- NOT a closure of op:einstein.
- NOT a falsification of c08: the tensor modes are attributed to companion 7 sec6, which I have NOT
  audited. The honest finding is that the c08-LEVEL metric map can't carry helicity-2; companion 7
  sec6 must be audited to decide.
- NO VERDICT MOVED; D2 still conditional; count/THEO unchanged.

## Next pitch
Audit companion 7 sec6: does it derive 2 helicity-2 GW modes from the 600-cell lattice? That decides
(a) and is the true remaining summit.

## Confidence
- Solid (computed): scalar+vector cannot source helicity-+/-2; Schwarzschild spatial metric conformal.
- Open/unaudited: companion 7 sec6's tensor-mode claim. This is the crux.

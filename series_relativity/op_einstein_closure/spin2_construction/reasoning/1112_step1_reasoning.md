# Reasoning capture — Patch 1112 (spin-2 construction, Step 1)

**Protocol:** `templates/reasoning_capture_protocol.md`. Reasoning behind identifying the missing d.o.f.

## The task
1110 pinned the op:einstein (a) gap: no spin-2 d.o.f. in the LSP. "Begin the fix" = identify the
missing d.o.f. concretely and check the 600-cell supports it (not build the whole spin-2 sector).

## The chain
1. Helicity-+/-2 modes live at l=2 (quadrupole) in an angular decomposition. LSP has l=0 (|SSV|_abs)
   + l=1 (SSV_net); missing l=2. So the candidate fix = a quadrupole broadcast.
2. Tested on the icosahedral 12-edge shell (numpy): the 5 l=2 functions have rank 5 (fully resolved);
   l=2 orthogonal to l=0,l=1 (independent, by the 5-design property of 1108); m=+/-2 = {x^2-y^2, xy}
   = the GR +,x polarizations.
3. So the fix = extend the LSP with a symmetric traceless rank-2 Q_ij (the l=2 shell quadrupole). The
   600-cell supports it natively; m=+/-2 supplies exactly the 2 missing helicity-2 modes.

## What I did NOT claim
- NOT a closure of (a). Identifying + grounding the d.o.f. is Step 1; the broadcast law, wave equation,
  GR-recovery, and GW-data confrontation (Steps 2-5) are the substantial remaining effort.
- NO VERDICT MOVED.

## Honest note
This is a promising, well-grounded direction (the d.o.f. is real and native to the 600-cell), but
whether the PCD broadcast cycle actually carries a propagating l=2 quadrupole at c -- and whether the
full tensor GR-recovery follows -- is genuinely open. The falsifier (no quadrupole channel in PCD) is
real.

## Confidence
- Solid (computed): the icosahedral shell supports an independent, fully-resolved l=2 mode whose m=+/-2
  part = the helicity-2 polarizations.
- Open: the broadcast law, the wave equation, the full GR-recovery -- the actual closure of (a).

# Reasoning capture — Patch 1107 (c08 op:einstein, Step (b))

**Protocol:** `templates/reasoning_capture_protocol.md`. Verbatim reasoning behind the Step (b) result.

## What I set out to test
The kickoff handover's falsification-first entry: run (b) before (a). (b) = does the uniform Sea
ground state cancel from c08's field equation, or can absolute |SSV| re-enter and let it gravitate
(reviving the catastrophe and killing the dark sector)?

## The chain
1. Read c08 eq:field_eq in full. Observed: the equation is written ENTIRELY in Δ|SSV| (excess) —
   both the Laplacian and the nonlinear F term. Absolute |SSV| appears only via PSR_eff labelling
   the metric the covariant derivative uses.
2. Two re-entry routes for absolute |SSV|: (b1) the source, (b2) the metric background.
3. (b1): F prefactor 2k(Δ|SSV|)²/(1+kΔ|SSV|)² → 0 at Δ|SSV|=0 (sympy, leading O(Δ²)); ∇²(const)=0.
   So uniform Sea ⇒ LHS=0 ⇒ sources nothing. No absolute |SSV| in the source.
4. (b2): the real subtlety — PSR_eff is set by ABSOLUTE |SSV|. But computed Ricci for g=Ω²η:
   R=2(−ΩΩ''+Ω'²)/Ω⁴, which is 0 for constant Ω. So a UNIFORM absolute |SSV| ⇒ flat background
   (mere unit rescaling). Curvature needs gradients of Ω = gradients of |SSV| = excess. Closed.

## Verdict
Cheapest kill does NOT fire: excess-sourcing/inert-Sea holds as c08's equation is written, through
both routes. The catastrophe does not return.

## What I deliberately did NOT claim
- NOT a closure of op:einstein. The excess form rests on c08's proof SKETCH (shell-sum); rigorizing
  that (no dropped absolute-|SSV| term) is the open (b′) task.
- The cosmological/Friedmann mode is SEPARATE (SR-5 Step A/C), not settled by a local field equation.
- (a) nonlinear GR-recovery (F → R_μν−½g_μν R) is untouched — the summit.
- NO VERDICT MOVED: SR-5 Step D2 is narrowed (cheapest kill removed), not discharged.

## Confidence
- Solid: (b1)/(b2) for c08's STATED equation (the form is manifestly excess-based; uniform background
  flat is a standard GR fact, computed).
- Open/conditional: shell-sum rigor (b′); nonlinear recovery (a). These are the genuine mountain.

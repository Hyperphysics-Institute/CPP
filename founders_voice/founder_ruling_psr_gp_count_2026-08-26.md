# Founder ruling — the PSR as a computed absolute GP count (26 Aug 2026)

**Captured verbatim per CONV-009. Registered at Patch 3444. Context:
UNIV-1 S2's Q1 (is the CP Displace distance PSR-scaled or absolute?)
was put to the founder; the answer specifies the PSR-side conversion
and its calibration status.**

## The founder's statement, verbatim

> The PSR has no currently computed or predicted number of GPs. It
> will need to be calibrated for the current STP (or other
> convenient/accessible space) and can then be used as a metric. The
> PSR sums the contributions of many DI-bits from the current and
> past Moments from the surrounding GPs. The SSV_abs is the outcome
> of the summation of the absolute number of DI-bits reaching each
> GP, and that computation in turn determines the absolute number of
> GPs (i.e., the PSR) it corresponds to.

## Mechanism details newly on record

1. **The PSR is an absolute GP count**, determined per-GP by
   computation: DI-bit summation → SSV_abs → the number of GPs the
   next propagation step reaches.
2. **The summation has memory — QUALIFIED by the founder, Patch 3445,
   verbatim:** "the memory of past Moments is not carried as a
   coherent memory. There is only the summation of every Moment's
   DI-bits from the GP_origin broadcasting to the GP_PSR and its
   rebroadcasting as the GP_origin to its PSR, etc., until a tiny,
   mixed/amalgamated portion of the original broadcast shows up as
   the 'memory' of the original GP_origin DI-bit broadcast." So:
   history enters only through **relay recursion** — each Moment's
   summation is of freshly arriving DI-bits, some of which are
   re-broadcast descendants of older broadcasts, amalgamated and
   attenuated. No register carries the past; the past persists only
   as its diluted echo in the present arrival stream. *(Anti-erasure:
   the original line above read "history-dependent, not
   instantaneous" — a shorthand the founder would not leave
   unqualified; superseded as stated.)*
3. **Calibration status**: no computed or predicted value exists; the
   PSR's absolute scale is to be calibrated empirically at STP (or
   another accessible condition) and thereafter used as a metric.

## Bearing on UNIV-1 (worker note)

The universality lemma never needs the PSR's absolute value — only
its *scaling* with SSV_abs and whether matter's Displace shares that
scaling. Calibration-at-STP is therefore fully compatible with the
lemma. **Q1 remains open**: this ruling fixes the SSV_abs → PSR
conversion (the A-side, already the definitional premise); the
SSV_net → Displace-distance conversion (the B-side, the hinge) is
still unstated. Q1 is re-posed in refined form at Patch 3444's S1
amendment, together with a candidate conversion rule for the founder
to confirm or correct.

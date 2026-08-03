# A5-DISP CONVERSION PRE-REGISTRATION — THE d_DP CEILING FORMULA, FROZEN BEFORE ANY BOUND IS CITED

**Patch 2942 (2 Aug 2026). Executes the CASE-Q band of
`a5_disp_prereg.md` §2 following the Patch 2940 relay classification
and the Patch 2941 economy-governance amendment. This document is
committed BEFORE any experimental limit is looked up or cited: it
freezes the conversion formula, the treatment of the underived
quadratic coefficient, the sign convention, and the source-class
rules. The conversion patch (next) cites numbers; this one contains
none. PANEL-PENDING: this prereg and the conversion it governs enter
the combined review package per Patch 2941.**

## §1 — What is being converted

Patch 2940 established (CASE-Q, conditional per its §5): the leading
mesh correction to ambient photon dispersion is quadratic,

  v(E)/c = 1 − ξ₂ · (E · d_DP / ħc)² + O((kd)⁴),

with ξ₂ the dimensionless quadratic relay coefficient, UNDERIVED at
this patch (its computation is a full O(kd)² relay arc, registered
below as the refinement path). Matching to the standard
quantum-gravity phenomenology parametrization
v(E)/c = 1 ∓ (E/E_QG,2)² gives the identification

  E_QG,2 = ħc / (√ξ₂ · d_DP),

and therefore any experimental lower limit E_QG,2 ≥ E_lim converts to
a **d_DP ceiling**:

  **d_DP ≤ (ħc / E_lim) · ξ₂^(−1/2).**

This is bound-type (charter-compliant) and reaches the **d_DP**
factor, not n_DP (per the 2936 M3 binding requirement that every
A5-class channel state which scarce factor it constrains).

## §2 — Frozen treatment of the underived coefficient ξ₂ (CONV-004)

Under the measured-coefficient / Galilean-layer discipline (CONV-004),
the ceiling is registered as the FORMULA above with ξ₂ explicit, and
the QUOTED NUMERIC CEILING is evaluated at the structural reference
point **ξ₂ = 1**, with the ξ₂^(−1/2) scaling stated wherever the
number appears. No claim is made that ξ₂ = 1; the claim is that the
ceiling scales as stated. If a future relay arc derives ξ₂ with
registered provenance, the ceiling is re-evaluated at the derived
value in a successor patch — the ξ₂ = 1 quote is a reference
normalization, not a physics assertion. A derived ξ₂ ≪ 1 would
weaken the ceiling as ξ₂^(−1/2) and must be exhibited as a formula
with registered provenance per the standing anti-α1 rule (inherited
verbatim from `a5_disp_prereg.md` §2 CASE-L band, applied here to the
quadratic coefficient).

## §3 — Frozen sign convention

sign(ξ₂) is underived (subluminal vs superluminal at quadratic
order). Published limits differ by propagation sign. Frozen rule:
**the BINDING ceiling uses the WEAKER (more conservative) of the
best published subluminal and superluminal quadratic limits from an
admissible source; both are reported.** No sign is chosen to obtain
a stronger ceiling.

## §4 — Frozen source-class rules (admissibility, fixed in advance)

An admissible limit must satisfy ALL of:

1. **TOF-class only.** Time-of-flight / energy-dependent-arrival
   analyses. Birefringence-class limits are INADMISSIBLE here:
   Patch 2940 established γ ≡ 0 for the ambient Sea (CASE-CB does not
   obtain), so vacuum-birefringence bounds constrain a coefficient
   CPP predicts to vanish and convert to no d_DP information.
2. **Quadratic-order (n = 2, E_QG,2-class) photon-sector limits**,
   published in peer-reviewed venues (preprints admissible only as
   secondary corroboration, never as the binding source).
3. **Independent error structure; no CPP-corpus ancestry** (trivially
   satisfied by astrophysical sources; stated per the 2936 M3
   requirements).
4. **Best-limit rule:** the binding ceiling uses the strongest
   admissible limit per sign at the time of the conversion patch;
   stronger future limits TIGHTEN the ceiling by simple substitution
   in a successor patch (no re-derivation needed — the formula is
   frozen here).

## §5 — What the conversion patch will contain

(i) The admissible limits found, with full citation provenance;
(ii) the binding ceiling from §1–§4 applied mechanically;
(iii) a stdlib verify script reproducing the arithmetic (CONV-003);
(iv) a PANEL-PENDING banner per Patch 2941 — the ceiling is VOID if
the combined review overturns CASE-Q;
(v) the ledger line. The conversion patch performs NO judgment calls:
every discretionary element is frozen in this document. If a
situation arises that this prereg's rules do not cover, the
conversion HALTS and the gap is registered rather than resolved
ad hoc.

## §6 — Conditionality inheritance and ledger

The ceiling inherits, verbatim, the full Patch 2940 §5 conditionality
stack (Mechanism A on both legs — CAPACITY-1 with two named
sub-conditions + TARROW-2 — plus vertex-aligned Reading C) and its
reopeners R1–R3, PLUS the ξ₂ reference-normalization caveat of §2
above. Ledger untouched: six of seven; PR7 PARTIAL; B7 holds;
Candidate (B) 79.5%; 2855 PROVISIONAL. No experimental number, no
value of η, d_DP, n_DP, or ξ₂ appears in this document.

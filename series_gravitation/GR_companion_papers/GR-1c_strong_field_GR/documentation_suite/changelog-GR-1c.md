# Changelog — GR-1c: Strong-Field General Relativity and the Planck Core

**Paper:** `series_gravitation/GR_companion_papers/GR-1c_strong_field_GR/GR-1c_strong_field_GR.tex`
**Convention:** canonical filename never carries a version suffix.

**STATUS: partially reconstructed.** No changelog was kept before the
August 2026 corrigendum. V1–V2.1 are recorded from git history and the
.tex date line; V2.2 is fully documented because it was executed under
the corrigendum protocol.

---

## V1 – V2.1 — 17 March 2026 onward

Authoring and revision history not recorded contemporaneously. The
paper's substance — the exact Schwarzschild theorem, the Planck-core
theorem, the field-equation Proposition, and the Kerr sketch — dates
from this period.

## V2.2 — 20 August 2026, Patch 3262 (Session 150) — **CORRIGENDUM**

**The field-equation Proposition was defective and is corrected.** Full
chain, because this is the arc's reference case for how a shipped error
is handled:

- **Found** (Patch 3258): the T-1 census derivation's charter-§4 HALT
  check compared its static reduction against this paper's published
  wave equation. Symbolic Check 5 showed the Proposition's compensator
  term failing **against this paper's own exact Theorem-1 solution** —
  O(a⁴) where the required compensator is O(a³), with the O(a²) term
  cancelling identically, under flat-□, curved-□, and literal-k readings
  alike. Per the HALT rule the paper was **not** adjusted; the defect
  was registered as OPEN-GR-FE1-FTERM.
- **Diagnosed** (Patch 3259): the Proposition had been written for the
  wrong potential. The exact measured-frame statement is the harmonicity
  of the *logarithmic lapse* N = ln√(−g_tt/c²) = −2·artanh(kΔ|SSV|/2);
  the true compensator is F_true = (k²Δ|SSV|/2)/(1−(kΔ|SSV|/2)²)·|∇Δ|SSV||²_g.
  The original was a correct building block with one power of u too many
  and an ln-vs-artanh resummation; no rescaling repairs it.
- **Approved** (Patch 3261): review round CONV-027 returned
  **APPROVE-EITHER 5–0** on the corrigendum, and VERIFIED 5–0 on its
  mathematics.
- **Ratified and enacted** (Patch 3262): on the founder's ratification,
  the Proposition was restated — Form A (boxed log-lapse harmonicity),
  Form B (quasilinear with F_true), plus the generic-v equivalence
  identity showing the measured-frame and lattice-frame equations are
  **one equation in two variables**. The defective formula is preserved
  verbatim in a Corrigendum Remark with the full discovery→repair→
  ratification chain (anti-erasure). The old proof sketch was rewritten
  to the variable-change derivation; downstream remarks and `op:einstein`
  re-pointed. **`op:einstein` REMAINS OPEN — no Einstein-equivalence
  claim was smuggled in.**
- Solution-level agreement was **exact throughout**: the metric, the
  classical tests, and the weak field were untouched by the defect, and
  GR-1i's 8/8 verify stands.
- Machine verification: `code/3259_fterm_reconciliation_verify.py` (8/8,
  all exact-symbolic). Compile gate clean, zero undefined refs.

## Re-identification — 19 August 2026, Patch 3230 (Session 149)

Moved into `series_gravitation/GR_companion_papers/` and re-identified
**c08 → GR-1c** (OPEN-ORG-023 Item 2). The move also dissolved a
directory-named-.tex defect.

## PD-001 formatting — 20 August 2026, Patch 3273 (Session 150)

W-A: CP/GP Signature subsection added. Compile clean.

## Documentation suite — 20 August 2026, Patch 3285 (Session 152)

OPEN-GR-PPP-1 W-B row 6: ten-file suite produced; this changelog
created. **A staleness finding was registered** (see
`phenomena-GR-1c.md`): three of the paper's five Open Problems have been
delivered or superseded since, and `op:24cell` additionally rests on a
geometry the founder has since retired. No .tex change — the correction
is scoped to the proposed W-D pass.

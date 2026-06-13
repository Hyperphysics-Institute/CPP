# Changelog — SR-2: The Spin-Bit Axiom

Canonical filename (no version suffix): `SR-2_spin_bit_axiom_quadrupole_formula.tex`.
Version archaeology lives here per the operating_system.md version-archaeology
architecture rule; the `.tex` title block shows only the current version line.

## v0.2 — 12 June 2026 (Phase 7B complete)

- **C14 step-5 audit-trail sweep** executed: the two uncited substantive method
  invocations flagged by the sweep were added — METH-L3-003 (the Step-0 audit
  confirming the second-assault dynamical matrix carried no per-edge transport, so the
  third assault was genuinely untested) in §3, and METH-L3-004 (the would-be-axiom
  discipline: terminal branch at the necessity conclusion in §3, refusal branch at the
  τ-redundancy in §7). All 13 methods of the 1133 plan are now cited.
- **Figure PDFs generated** by re-running `notebooks/SR-2_figures.py` (matplotlib;
  ledger check reproduced 0.999998). The four figure includes were switched from
  `\includesvg` to `\includegraphics{...pdf}`, so the paper compiles with plain
  `pdflatex` + `graphicx` and needs no inkscape (SR-1 convention). Committed SVGs left
  untouched; only the four PDFs are added.
- **Compile verified end-to-end:** `pdflatex ×3 + bibtex`, all rc=0, no undefined
  references or citations, all six bibliography entries resolved, 19 pages.

## v0.1 — 12 June 2026 (Phase 7B first full draft)

- First `.tex` of the spin-2 / `op:einstein` arc. Produced in Phase 7B per
  `series_relativity/op_einstein_closure/flagship_assembly_scope.md` (SKELETON LOCK,
  Patch 1135).
- Transcribed from the 13 step/task documents — `op_einstein_closure/1107–1110`,
  `spin2_construction/1112–1129` — plus the DG-3 review suite, onto the locked
  10-section skeleton. Transcription-and-framing, not derivation: no verdict moved.
- Four theorems stated to match the registry verbatim (THEO-SR-EIN-1 Completion,
  THEO-SR-EIN-2 Statics, THEO-SR-EIN-3 TT-Response/Cancellation, THEO-SR-EIN-4
  Operational-Energy Lemma). Axiom A3′ stated as registered (amendment, count 9,
  audit note 10). Four falsifiers stated as PRED-O-35..38 (open, uncounted).
- Conditionality harmonized (Gap 5): `op:einstein` (a) CLOSED for the radiative
  sector; (b) conditionally closed with the shell-sum reduction rigorization named as
  the residual; the substrate-microscopic energy functional flagged as a declared
  refinement, not a debt.
- Figure-to-section map per the lock: fig1 (H_g seat) → §4; fig2 (two assaults) → §3;
  fig3 (eccentric ledger) → §7; fig4 (lattice discriminant) → §9.
- Inline `[METH-Lx-NNN ...]` citations placed per the 1133 citation plan
  (`1133_c14_methods_audit.md` §4).
- Bibliography (`SR-2_references.bib`): external GW literature added; internal CPP
  companions referenced by programme ID in prose.

### Open for 7B completion / 7C
- C14 step-5 audit-trail sweep (uncited substantive method invocations) before 7C dispatch.
- Required-subsection placement confirmed: §1.1 Open Problems Addressed; §8.1 CP/GP
  Signature; §11.1 Swarm-Validation Contribution; §11.2 Problem Status.
- Figure PDFs: only SVGs are committed; `\includesvg` is used (svg package, inkscape
  conversion). Pre-generated PDFs can be added if the build environment lacks inkscape.
- 7C review pass: framing + over-claim only, not new math (components are DG-3-closed).

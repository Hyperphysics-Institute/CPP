# Compile status of the deposit candidates

**Generated at Patch 4344** by `bash code/compile_pass.sh` (pdflatex, two passes, run in each paper's own folder with auxiliary files in a scratch directory, so relative figure paths resolve as in a real build). Re-run before any deposit; Isak's build needs every row at 0 errors.

**121 of 122 deposit candidates compile with no errors.**

History: 4343 found 98/123 clean, but its method copied each folder elsewhere and so misreported relative figure paths (SR-1, DM-1). 4344 fixed the method, converted the QM-series and SM-6 figure SVGs to the PDFs the papers include, fixed the LaTeX faults below, and removed a development transcript from the queue (123 → 122).

| Errors | Paper | Most frequent kinds |
|---|---|---|
| 6 | `series_foundations/dp_sea_composition/DP_sea_and_cage_composition.tex` |  1 ! Package svg Error: File `dpsea_fig6_experimental_timeline.svg' is missing.; 1 ! Package svg Error: File `dpsea_fig5_theory_comparison.svg' is missing. |

**The one remaining failure:** the DP-Sea paper includes six figures (`dpsea_fig1_composition_spectrum.svg` … `dpsea_fig6_experimental_timeline.svg`) that have never been in the repository and are not produced by its notebooks. They need to be supplied (or the figure environments removed) before deposit.

## Faults fixed at 4344

- SR-2, SF-8: `\newcommand{V_i}{V_i}` — Patch 4164's SSV_net → V_i text replacement had rewritten the macro name; SR-2 also had `$V_i\equivV_i$`.
- SF-2: two version lines closed `\date{` early (`)}}` mid-block); `\eDP` used but undefined.
- dynamical_substrate_law: a Patch-3212 script had put the Version 1.1–1.3 lines inside a header comment, before `\documentclass`; moved into the real `\date`. `\ehat` undefined.
- SS-1: a stray duplicate Keywords/Plain Language block before `\documentclass`.
- SS-1b: `theorem*` undeclared; math in a section title without `\texorpdfstring`.
- SS-8, SS-9: a control character (`\x0b`) where `\varphi` belonged (a `\v` escape); SS-8's committed `.bbl` had unescaped math.
- SF-6 (`\partialV`, `\DeltaV`), GR-1f and QM-1 (`V_i` outside math), SD-5 (`\Ntot`, optional-argument bracket), face_aligned (`✓`, `\nhatedge`), edge_aligned (double subscript), o_delta_squared (`\\ [` read as a spacing argument), DP-Sea (`±` in a listing).

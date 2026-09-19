# SSV_net Audit — Survey Before Execution

**Patch:** 4145. **Lane:** GR/WORKFLOW. **Session:** 234.
**Scopes (does not execute):** TODO-4142-SSVAUDIT.
**Founder note (19 Sep):** *"the SSV_net notation, both as pot and disp, is used extensively
throughout the entire corpus and will need an entire corpus review as well as a glossary change."*
Correct on both counts. This patch measures the job and stages it; it renames nothing.

---

## 1. The measurement

| | |
|---|---|
| occurrences of `SSV_net` / `SSV_{net}` / `SSV\_net` | **1,662** |
| files containing it | **410** |
| by extension | **364 .md, 43 .py, 3 .tex** |
| of the 410, append-only history (`handovers/`, `session_logs/`, `archive/`) | **33** |

Distribution by series: series_phenomena 108, series_gravitation 60, series_relativity 49,
founders_voice 41, series_standard_model 36, flagship_papers 32, series_quantum_mechanics 26,
handovers 20, then single digits.

**The shape this reveals, and it is better than feared: only three `.tex` files use the token** —
`GR-1b_weak_field_GR`, `GR-2_echo_falsifier`, `QM-1_schrodinger_emergence`. The published papers
are almost untouched; the exposure is internal documentation and 43 verify scripts. A published-
paper rename would mean recompiles and version bumps across the series. This one does not.

## 2. The root of the ambiguity, located

`master_glossary.md` line 29, the canonical definition, verbatim:

> | SSV_net | Net SSV | The vector sum of all SSV contributions at a point |

**That definition is neutral between the two roles.** A "vector sum of contributions at a point"
describes the broadcast summation and the CP's displacement instruction equally well. Every
downstream use inherited the ambiguity from here. Line 64 then assigns `V_i = SSV_net` to the
l=1 metric component, and the A1′ Displace clause assigns it to what a CP moves by — two
incompatible specialisations of one neutral parent.

**This one line is the highest-value edit in the whole audit**, and it is one line.

## 3. What the survey could NOT establish, and why I am not reporting it

I wrote a regex classifier to sort the 1,662 occurrences into ^pot / ^disp / ambiguous by
surrounding keywords. **Its output is not trustworthy and I am discarding it**: its file count
disagreed with grep's (475 vs 410, a whitespace-splitting bug), and spot-checking its "samples"
showed context windows that did not contain the token at all.

Rather than publish a number I cannot stand behind — twice today I have had to withdraw one —
I record the finding that matters: **role classification cannot be done by pattern matching.**
Deciding whether a given "SSV_net" means the broadcast potential or the displacement field
requires reading the surrounding physics. That makes this a **reading job across ~377 live files**,
not a find-and-replace, and it should be planned and budgeted as such.

## 4. Staged plan (registered, not started)

- **Stage 0 — naming decision.** The tokens `^pot` / `^disp` are mine (Patch 4142). Settle them
  before anything is renamed; renaming twice across 377 files is the one avoidable disaster here.
- **Stage 1 — the glossary.** Rewrite `master_glossary.md` line 29 into two entries plus a note
  that the bare token is deprecated. One file. Immediately useful even if nothing else moves,
  because it stops new ambiguous uses.
- **Stage 2 — the axiom text and the 43 verify scripts.** A1′/A3′, `templates/`, and every `.py`
  that reads or names the quantity. Code must agree with the glossary or the gates drift.
- **Stage 3 — the three `.tex` papers**, with recompiles: GR-1b, GR-2, QM-1.
- **Stage 4 — the remaining live `.md`**, series by series, heaviest first (series_phenomena,
  series_gravitation, series_relativity).
- **Never — `handovers/`, `session_logs/`, `archive/` (33 files).** Append-only history. They
  record what was written at the time and are not corrected retroactively; the anti-erasure
  convention already governs this.

## 5. The one thing I am not deciding

Under PD-006 the sequencing above is mine. **The tokens are not** — they are terminology in
Thomas's theory, the corpus will carry them permanently, and the cost of changing them after
Stage 4 is prohibitive. Put to him as a single bounded question (§6 of the turn). I am not
proceeding past Stage 0 without it.

## 6. Status

No physics. No verdict moved. Nothing renamed. TODO-4142-SSVAUDIT remains open, now scoped.
χ₄ provisionally adopted; **F5 remains the blocker.**

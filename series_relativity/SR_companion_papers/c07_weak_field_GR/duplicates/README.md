# NON-CANONICAL — excluded from all sweeps and citations

**Registered Patch 3201 (16 Aug 2026) by the F-SW-10 R-2 sweep.**

Nothing in this folder is canonical. Nothing in it may be cited, compiled,
graded, or treated as a source of record. Automated sweeps and delta audits
**must skip this directory.**

## What is actually here

| File | What it really is |
|---|---|
| `c07_weak_field_GR.tex` | **MISNAMED.** Not c07. Titled *"Inertial Mass from Zitterbewegung"* — a stale copy of **c04** (`c04_ZBW_hbar_mass_units.tex`). Lines 320–350 were byte-identical to live c04 at the time of registration. |
| `weak field GR.tex` | Stale draft. Filename contains spaces, violating repo naming convention. |
| `weak_field_general_relativity.tex` | Stale draft. |

The canonical c07 is one level up: `../c07_weak_field_GR.tex`.
The canonical c04 is at
`../../c04_ZBW_hbar_mass_units/c04_ZBW_hbar_mass_units.tex`.

## Why this file exists

The R-2 sweep found that a fix scheduled for live c04's inertia conclusion
would leave the shadow copy here carrying the superseded text. A later
grep-based sweep would then surface two inconsistent statements of where
inertia lives, with nothing in the tree indicating which one governs. That is
the precise drift mode delta audits exist to prevent, and it is invisible to
any sweep that greps only the live tree.

## Disposition

**Deletion is recommended and NOT performed.** A delta audit does not silently
destroy artifacts; the founder may want the history. Founder disposition is
requested at the F-SW-10 close record. Until then this quarantine notice is the
control.

Full reasoning: `series_relativity/audits/3201_fsw10_r2_arc_cancel_turnaround_findings.md` §4.

# NON-CANONICAL — excluded from all sweeps and citations

**Registered Patch 3201 (16 Aug 2026) by the F-SW-10 R-2 sweep.**

Nothing in this folder is canonical. Nothing in it may be cited, compiled,
graded, or treated as a source of record. Automated sweeps and delta audits
**must skip this directory.**

## What is actually here

| File | What it really is |
|---|---|
| ~~`c07_weak_field_GR.tex`~~ | **DELETED, Patch 3202, on founder authorization of 16 Aug 2026.** It was misnamed: not c07 but a stale copy of **c04**, titled *"Inertial Mass from Zitterbewegung"*, byte-identical to live c04 through lines 320–350 — including the inertia-conclusion sentence amended in the same patch. Recoverable from git history if ever wanted. |
| `weak field GR.tex` | Stale early draft of c07 proper (135 lines vs. live c07's 863). Filename contains spaces, violating repo naming convention. **Byte-identical to the file below.** |
| `weak_field_general_relativity.tex` | Stale early draft of c07 proper. Byte-identical to the file above — the two are redundant copies of one draft. |

**Status of the two survivors.** They are honest, obviously-superseded early
drafts of c07 — not shadows of current text — so their drift risk is far lower
than the deleted ghost's. They were **not** covered by the founder's deletion
authorization, which named the ghost copy specifically. They remain quarantined
pending separate disposition.

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

**The ghost copy is deleted (Patch 3202).** For the two surviving drafts,
deletion is recommended and NOT performed. A delta audit does not silently
destroy artifacts; the founder may want the history. Founder disposition is
requested at the F-SW-10 close record. Until then this quarantine notice is the
control.

Full reasoning: `series_relativity/audits/3201_fsw10_r2_arc_cancel_turnaround_findings.md` §4.

# series_gravitation — the CPP gravitational arc

**Created:** 19 Aug 2026, Patch 3228 (Session 149), per the Session 148
founder rulings and the Patch 3225 scoping assessment
(`series_relativity/audits/3225_gr1_scoping_assessment.md`).

## What this series is

The series parent **GR-1** (`papers/GR-1_local_gravitation_from_SSV_shell_broadcast.tex`)
plus, pending re-identification and file moves (tracked as **OPEN-ORG-023**),
the eight gravitational companions currently filed under
`series_relativity/SR_companion_papers/`:

| Current ID | Content | Lines (approx.) |
|---|---|---|
| c05 | Newtonian gravity from SSV shell broadcast | 349 |
| c07 | Weak-field GR (two-component LSP; SSV_net vector) | 877 |
| c08 | Strong-field GR: exact isotropic Schwarzschild; Planck core r_S/2 | 991 |
| c09 | Gravitational-wave echoes from the Planck core | 714 |
| c10 | Hawking evaporation with a Planck remnant | 599 |
| c11 | Kerr from azimuthal SSV_net | 648 |
| c12 | Kerr-Newman (M, J, Q) | 617 |
| c13 | Superradiance | 651 |

c14 (quark confinement) and c15 (colour charge) are strong-sector papers
misfiled in the SR companion folder; they belong under SS-1, **not** here.
Founder ruling on their refiling is still owed (OPEN-ORG-023).

## Standing rulings (do not relitigate)

- **Series paper first; the gravitational flagship comes later**, once the
  series is complete (SS-1 → SS-1a–f → SF-5 precedent).
- **GR-1 claims exact reproduction of the SOLUTIONS** (Schwarzschild in
  isotropic coordinates, Kerr, Kerr-Newman), **not** derivation of the
  general field equations. The derivation is registered as **OPEN-GR-FE-1**
  (`frontier_sectors/GR.md`).
- **Classical tests: results-only table in GR-1; all four derivations in ONE
  dedicated tests companion** (**OPEN-GR-TESTS-1**). The Patch 3226
  instruction placing the tests inside GR-1 is withdrawn (see the Session
  148 handover §5 and the Patch 3227 handover correction).
- **SR-1 keeps its name** — it is genuinely a special-relativity paper; the
  gap was a missing parent, not a mistitled one.
- **Deposit hold:** the eight companions (and GR-1 itself until the series
  identity settles) are **held out of deposit wave 1** — a Zenodo preprint
  can only be withdrawn, never erased, and their identifiers are about to
  change (OPEN-ORG-023).

## Layout

- `papers/` — GR-1 and, after re-identification, the series papers.
  Filenames carry no version suffixes; versions live in the in-file
  CHANGELOG header.
- `code/` — verify scripts (`<patch>_*.py`).
- `reasoning/` — verbatim per-patch reasoning fragments (`<patch>.md`).

Per-paper four-tier `documentation_suite/` subfolders are created when a
paper accumulates multi-session work (operating_system.md §4).

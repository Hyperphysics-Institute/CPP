# OSF RE-DEPOSIT MANIFEST — what has changed since the last deposit (Patch 3203)

**Prepared 16 Aug 2026 at the founder's request.** Question asked: *which PDFs
need updating on OSF, given the last update was around the DM candidate?*

---

## §1 — What I can and cannot determine (read this first)

**I CAN determine, exactly:** which `.tex` files have changed in git since any
given date. That is a hard, verifiable fact and §3 is that list.

**I CANNOT determine what is actually live on OSF.** Nothing in this repo is a
reliable record of it:

- `paper_catalog.md` is the designated tracker of OSF/arXiv state. It was
  **last updated 21 June 2026 (Patch 1609)** — roughly two months stale as of
  this writing, and it predates the entire QM re-grounding arc, the CC arc, the
  SR audits, and the DM Route C campaign.
- Almost every row in it reads **"OSF pending"** rather than a deposit date or
  version. Only SM-6 and SM-7 read "Registered on OSF."
- `research_priorities.md` §242 records that OSF Open-Ended Registration
  `10.17605/OSF.IO/JXE8D` was stuck in *"Pending Admin Contributor Approval"*
  for 38+ days as of the Session 36 close, with a Zenodo fallback contemplated.
  Whether that ever resolved is not recorded anywhere in the repo.

**Therefore:** §3 is the *candidate* list — everything that has moved since the
DM-1 deposit. Converting it to an *action* list requires one person to open OSF
and read off what is actually deposited and at what version. That is a
five-minute job for Isak and cannot be done from the repo. Claude Code has the
same limitation for the same reason: the information does not exist locally.

**Standing recommendation:** whoever does that pass should write the result
back into `paper_catalog.md` — a per-paper deposit date and deposited version.
The catalog going stale is why this question is hard to answer at all, and it
will recur every time otherwise.

## §2 — Anchor date

The last OSF deposit activity traceable in git is
`series_phenomena/cosmology/dark_matter/DM-1/documentation_suite/osf-deposit-DM-1.md`,
last touched **6 July 2026** (`6af5cbc6`). This matches the founder's
recollection ("the proposed DM candidate or something around that time") and is
used as the anchor below.

## §3 — Candidate list: 24 `.tex` files changed since 6 July 2026

Excludes `duplicates/`, `development/`, `drafts/`, `archive/`.

### Flagship papers (6)
| File | Note |
|---|---|
| `flagship_papers/electromagnetism/sf-6_electromagnetism.tex` | **v1.3 as of Patch 3202** — emission generalized. Recompile owed. |
| `flagship_papers/electromagnetism/SF-8/sf-8_emergent_electrostatics.tex` | Sections pending; check ship state before depositing. |
| `flagship_papers/electroweak/sf-2_electroweak.tex` | |
| `flagship_papers/electroweak/sf-2_companion.tex` | |
| `flagship_papers/neutrinos/sf-4_neutrinos.tex` | v1.0 SHIPPED Session 54. |
| `flagship_papers/strong/sf-5_strong.tex` | v1.0 SHIPPED. |

### Quantum mechanics series (6) — **the whole series moved**
`QM-1_schrodinger_emergence`, `QM-2_superposition`, `QM-3_bell_entanglement`,
`QM-4_measurement_problem`, `QM-5_qft_emergence`, `QM-6_capstone`.

*These six are the highest-priority block.* They carry the QM re-grounding arc
(Patches 2995–3014) that resolved the QM-1 phase-provenance problem. Any
QM-series PDF now on OSF predates that resolution and states a retired
ontology.

### Relativity series (8)
| File | Note |
|---|---|
| `series_relativity/papers/SR-1_special_relativity_emergence.tex` | Rebilled as a grounding paper; five predictions formally withdrawn. **A stale SR-1 on OSF would show withdrawn predictions as live — the most consequential staleness on this list.** |
| `series_relativity/papers/SR-2_spin_bit_axiom_quadrupole_formula.tex` | |
| `c01_absolute_moment_postulate` | |
| `c02_dipole_stiffness_C` | |
| `c03_born_rule` | |
| `c04_ZBW_hbar_mass_units` | **v2.1 as of Patch 3202.** Recompile owed. |
| `c06_dipole_chain_patterns_as_mass_EM_subtrate` | **v2.3 as of Patch 3202.** Recompile owed. |
| `c07_weak_field_GR` | |

### Cosmology / dark sector (4)
`DM-1_substrate_dark_matter_candidate` (changed *since* its own deposit —
re-deposit likely needed), `DM-2_sea_gravitation_dark_sector`,
`DM-3_discriminating_predictions`, `DM-1/section_population_finding_draft`
(draft fragment — probably not for deposit).

## §4 — Suggested order of work

1. **SR-1** — withdrawn predictions showing as live is a correctness problem,
   not a freshness problem.
2. **The six QM papers** — retired ontology, as a block.
3. **c04 / c06 / SF-6** — recompiles already owed from Patch 3202; deposit in
   the same pass.
4. Everything else, at convenience.

Items 3's PDFs are owed regardless; folding the deposit into that pass costs
nothing extra.

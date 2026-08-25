# Zenodo DOI Injection Log — 2026-08-24

## What happened

On 2026-08-24, 118 production Zenodo DOIs were reserved for the entire CPP paper corpus. The DOIs were then injected into all bibliography files across the repo so that every cross-reference between CPP papers now carries a real, permanent DOI.

## Files modified

### Central bibliography
- `bibliography/cpp_references.bib` — 31 existing entries updated (replaced "Zenodo DOI pending" with real DOIs, added `doi=` and `url=` fields), 77 new entries added. Total: 32 → 109 entries.

### Local series bibliographies
- `series_quantum_mechanics/papers/cpp_qm_series.bib` — 11 CPP entries updated (c1–c6, cpp2040a–f). Added `doi=` and `url=` fields.
- `series_electroweak/papers/cpp_ew_series.bib` — 7 CPP entries updated (cpp_ew1–4, cpp2040a, cpp2040f, cpp5014). Replaced OSF DOIs with Zenodo DOIs; OSF DOIs preserved in `note=` field.
- `series_strong/papers/cpp_strong_series.bib` — 13 CPP entries updated (cpp_ss1–5, cpp_ew1/2/5, cpp2040e/f, c14, cpp_sm_paper2, stiffness_c). Added `doi=` fields; OSF DOIs preserved where they existed.
- `series_foundations/series_superdeterminism/cpp_foundations_series.bib` — 7 CPP entries updated (cpp_sd1–4, cpp2040a, cpp_ew2, c14). Added `doi=` fields.
- `series_gravitation/GR_companion_papers/GR-1b_weak_field_GR/gr_companion.bib` — 22 CPP entries updated (long keys: abshier2026am/stiff/born/mass/grav/zdc/gr; short keys: c1–c15). Added `doi=` fields. Notes updated with new paper designations (e.g., c5→GR-1a, c14→SM-11, c15→SM-12).

### Backups
Every modified file has a `.backup` copy alongside it (the pre-injection version).

## Key-to-DOI mapping for local bib entries

### cpp_qm_series.bib
| Bib key | Paper | Zenodo DOI |
|---|---|---|
| abshier2026c1 | c01 | 10.5281/zenodo.22084799 |
| abshier2026c2 | c02 | 10.5281/zenodo.22084801 |
| abshier2026c3 | c03 | 10.5281/zenodo.22084803 |
| abshier2026c4 | c04 | 10.5281/zenodo.22084809 |
| abshier2026c6 | c06 | 10.5281/zenodo.22084811 |
| cpp2040a | QM-1 | 10.5281/zenodo.22084616 |
| cpp2040b_super | QM-2 | 10.5281/zenodo.22084618 |
| cpp2040c | QM-3 | 10.5281/zenodo.22084620 |
| cpp2040d | QM-4 | 10.5281/zenodo.22084622 |
| cpp2040e | QM-5 | 10.5281/zenodo.22084630 |
| cpp2040f | QM-6 | 10.5281/zenodo.22084632 |

### cpp_ew_series.bib
| Bib key | Paper | Zenodo DOI | Old OSF DOI |
|---|---|---|---|
| cpp_ew1 | EW-1 | 10.5281/zenodo.22084471 | 10.17605/OSF.IO/6DM45 |
| cpp_ew2 | EW-2 | 10.5281/zenodo.22084473 | 10.17605/OSF.IO/3XNK5 |
| cpp_ew3 | EW-3 | 10.5281/zenodo.22084477 | 10.17605/OSF.IO/ZWQRY |
| cpp_ew4 | EW-4 | 10.5281/zenodo.22084479 | 10.17605/OSF.IO/SDW7G |
| cpp2040a | QM-1 | 10.5281/zenodo.22084616 | — |
| cpp2040f | QM-6 | 10.5281/zenodo.22084632 | — |
| cpp5014 | SS-1 | 10.5281/zenodo.22084743 | — |

### cpp_strong_series.bib
| Bib key | Paper | Zenodo DOI |
|---|---|---|
| cpp_ss1 | SS-1 | 10.5281/zenodo.22084743 |
| cpp_ss2 | SS-2 | 10.5281/zenodo.22084761 |
| cpp_ss3 | SS-3 | 10.5281/zenodo.22084764 |
| cpp_ss4 | SS-4 | 10.5281/zenodo.22084768 |
| cpp_ss5 | SS-5 | 10.5281/zenodo.22084772 |
| cpp_ew1 | EW-1 | 10.5281/zenodo.22084471 |
| cpp_ew2 | EW-2 | 10.5281/zenodo.22084473 |
| cpp_ew5 | EW-5 | 10.5281/zenodo.22084481 |
| cpp2040e | QM-5 | 10.5281/zenodo.22084630 |
| cpp2040f | QM-6 | 10.5281/zenodo.22084632 |
| c14 | SM-11 | 10.5281/zenodo.22084693 |
| cpp_sm_paper2 | SM-2 | 10.5281/zenodo.22084699 |
| stiffness_c | SR-1 | 10.5281/zenodo.22084735 |

### cpp_foundations_series.bib
| Bib key | Paper | Zenodo DOI |
|---|---|---|
| cpp_sd1 | SD-1 | 10.5281/zenodo.22084636 |
| cpp_sd2 | SD-2 | 10.5281/zenodo.22084638 |
| cpp_sd3 | SD-3 | 10.5281/zenodo.22084640 |
| cpp_sd4 | SD-4 | 10.5281/zenodo.22084646 |
| cpp2040a | QM-1 | 10.5281/zenodo.22084616 |
| cpp_ew2 | EW-2 | 10.5281/zenodo.22084473 |
| c14 | SM-11 | 10.5281/zenodo.22084693 |

### gr_companion.bib (long keys)
| Bib key | Paper | Zenodo DOI |
|---|---|---|
| abshier2026am | c01 | 10.5281/zenodo.22084799 |
| abshier2026stiff | c02 | 10.5281/zenodo.22084801 |
| abshier2026born | c03 | 10.5281/zenodo.22084803 |
| abshier2026mass | c04 | 10.5281/zenodo.22084809 |
| abshier2026grav | GR-1a | 10.5281/zenodo.22084492 |
| abshier2026zdc | c06 | 10.5281/zenodo.22084811 |
| abshier2026gr | GR-1b | 10.5281/zenodo.22084494 |

### gr_companion.bib (short keys)
| Bib key | Paper | Zenodo DOI |
|---|---|---|
| c1 | c01 | 10.5281/zenodo.22084799 |
| c2 | c02 | 10.5281/zenodo.22084801 |
| c3 | c03 | 10.5281/zenodo.22084803 |
| c4 | c04 | 10.5281/zenodo.22084809 |
| c5 | GR-1a | 10.5281/zenodo.22084492 |
| c6 | c06 | 10.5281/zenodo.22084811 |
| c7 | GR-1b | 10.5281/zenodo.22084494 |
| c8 | GR-1c | 10.5281/zenodo.22084502 |
| c9 | GR-1d | 10.5281/zenodo.22084506 |
| c10 | GR-1e | 10.5281/zenodo.22084508 |
| c11 | GR-1f | 10.5281/zenodo.22084510 |
| c12 | GR-1g | 10.5281/zenodo.22084514 |
| c13 | GR-1h | 10.5281/zenodo.22084516 |
| c14 | SM-11 | 10.5281/zenodo.22084693 |
| c15 | SM-12 | 10.5281/zenodo.22084697 |

## OSF DOI registry

Historical OSF DOIs (priority timestamps) are preserved at:
`~/Documents/Projects/hyperphysics-rebuild/generator/osf_doi_registry.json`

## Related files (in hyperphysics-rebuild repo)
- `generator/zenodo_doi_map.json` — full 118-paper DOI map
- `generator/zenodo_deposit_state.json` — Zenodo draft state
- `generator/zenodo_dois.bib` — standalone bib with all 118 Zenodo entries
- `generator/osf_doi_registry.json` — historical OSF DOIs

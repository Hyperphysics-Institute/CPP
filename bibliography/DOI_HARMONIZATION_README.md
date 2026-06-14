# DOI Harmonization Worksheet — bibliography/cpp_references.bib

**Purpose.** The master bibliography currently asserts the umbrella project DOI
`10.17605/OSF.IO/JXE8D` for 17 CPP self-citations (+2 in note) and no DOI for 12.
Reality: CPP stopped using the single open registration after a problem and now
registers most papers individually, so most of those umbrella DOIs are wrong and
the blanks are unfilled. This worksheet maps each entry to its real DOI so the
master bib can be harmonized in one automated pass.

## Columns
- `bib_key` — exact key in `bibliography/cpp_references.bib` (the join key; do not edit).
- `paper_id`, `version`, `title` — context, from the entry's note/title (read-only).
- `current_doi_claim` — what the entry asserts today: `UMBRELLA` / `umbrella-in-note` / `NONE`.
- **`REAL_DOI__fill`** — fill with the DOI OSF actually issued for this paper.
- **`KEEP_UMBRELLA_open_project__Y_N`** — `Y` only for the 6–8 papers that genuinely
  live in the original *open* registration (they legitimately share the umbrella DOI);
  leave `REAL_DOI__fill` blank for those.
- `osf_url__optional` — direct OSF URL if handy (else automation derives from DOI).

## Automation rules (per row)
1. `REAL_DOI__fill` present → set `doi = {REAL_DOI}` AND replace the `\url{...}` in `note`
   with `\url{https://doi.org/REAL_DOI}`.
2. `KEEP_UMBRELLA = Y` → keep `10.17605/OSF.IO/JXE8D` (do not change).
3. Both blank (not yet registered) → **strip the wrong DOI**: remove the `doi` field and the
   umbrella `\url{}` from note; set note to end with "OSF deposit pending". Do NOT leave a
   fabricated DOI. (A wrong DOI is worse than none.)

## Notes
- New companion papers (SS-1a..e; any promoted theorems) get ADDED as rows once registered —
  not in this initial set (they don't exist in master yet).
- After applying, re-run `scripts/publication_audit.sh <ID>` per paper; bibliography is
  central-only (OS §10), so the only change is DOI/note content, not structure.

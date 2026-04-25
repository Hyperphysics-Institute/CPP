# Strong Sector Data — External Data Sources

**Scope:** This directory is the canonical location for external empirical data files used by scripts across the Strong Sector series (SS-1, SS-2, ..., and future papers). The data files themselves are **not distributed with the CPP repository**; this README documents what data is required, where to obtain it, and where to place the downloaded files so that the series' scripts can find them.

**Maintenance:** This is a living document. URLs and access points for scientific-data sources change over time as distribution mirrors are reorganized, new editions supersede old ones, and canonical hosting locations migrate. When the URLs below break or when newer data editions supersede those listed, this file should be updated directly rather than requiring code-level patches. Every other reference to external data in the repository (scripts, papers, documentation) points *to* this file rather than duplicating its content, so a single edit here propagates correctly.

**Why external data is not distributed in the repo:** Redistributing third-party scientific data in our repository raises licensing and version-drift concerns that are disproportionate to the benefit. Researchers who wish to reproduce the CPP programme's empirical predictions download the data directly from the canonical source, which has the side benefit of ensuring each researcher engages with the data at its original distribution point — confirming data version, field-format specification, and any errata or updates issued since original publication. The friction is small and the verification quality improved.

---

## AME 2020 — Atomic Mass Evaluation (2020)

**Used by:** SS-8 (`ss8_empirical_map_extended.py`, `ss8_polytope_enumeration.py`); future Strong Sector papers with empirical-binding-energy content (SS-7 migration candidate, SS-9/SS-10 when drafted, OPEN-SS-23 extensions).

**Citation:** M. Wang, W. J. Huang, F. G. Kondev, G. Audi, S. Naimi, "The AME 2020 atomic mass evaluation (II). Tables, graphs and references," *Chinese Physics C* **45**, 030003 (2021). DOI: 10.1088/1674-1137/abddaf.

The citation is the permanent identifier. Use it in all paper references. The URL below is the current known-good download location as of the date at the top of this document; it is not a substitute for the citation and should not be treated as permanent.

**Current known-good download location (as of 24 April 2026):**

Primary: IAEA Nuclear Data Section, AMDC (Atomic Mass Data Center) mirror.
`https://www-nds.iaea.org/amdc/ame2020/mass_1.mas20`

The file is distributed in the standard mass.mas20 Fortran fixed-width format (FORMAT: `a1,i3,i5,i5,i5,1x,a3,a4,1x,f14.6,f12.6,f13.5,1x,f10.5,1x,a2,f13.5,f11.5,1x,i3,1x,f13.6,f12.6`). See the file's own preamble block for the full field-by-field specification and the `'#'`/`'*'` sentinel conventions for estimated and non-calculable values.

If the primary URL above fails, the AME 2020 data is also available via the Chinese Physics C supplementary materials associated with the Wang et al. 2021 paper, and via the original authors' distributions. Search terms: "AME 2020 mass.mas20 download" or "AMDC AME 2020 atomic mass evaluation."

**Expected local filename:** `ame2020_mass.txt`

**Expected local location:** `series_strong/data/ame2020_mass.txt` (relative to the CPP repository root — i.e., this file's directory).

**Expected file size:** approximately 0.8 MB (roughly 3500 lines plus a header block).

**Verification after download:** the file's header block should begin with lines identifying it as the AME 2020 mass evaluation, and the first data row (after the format specification block) should be the free neutron at position `(Z=0, A=1)`. A quick sanity check: the file should contain exactly one row per observed or extrapolated nuclide, with the lightest rows (hydrogen, helium isotopes) early in the file.

**Loader:** `series_strong/papers/ame2020_loader.py` parses the mass.mas20 format and returns a dictionary keyed by `(Z, A)`. The loader defaults to looking for the file at `series_strong/data/ame2020_mass.txt` (the location documented above) and raises a `FileNotFoundError` with a pointer back to this README if the file is not present.

---

## How to download and install AME 2020

From your CPP repository root:

1. Download the AME 2020 mass data file from the canonical source listed above.
2. Rename (if needed) or save the downloaded file as `ame2020_mass.txt`.
3. Place the file at `series_strong/data/ame2020_mass.txt` within your local CPP repository.
4. Verify placement: `ls series_strong/data/` should show `ame2020_mass.txt` alongside `data-README.md` and `.gitkeep`.
5. The `.gitignore` in this directory is configured to exclude `ame2020_mass.txt` so that it is not accidentally committed to the repository on a subsequent patch.

After step 4, any Strong Sector script that uses the AME 2020 loader will find the data automatically.

---

## Future data sources

Additional external data sources may be added to this document as the Strong Sector series extends. Anticipated candidates:

- **NNDC / ENSDF evaluated nuclear structure data** — for nuclear-level-scheme content in future papers.
- **Alpha-cluster radius measurements** — when SS-9/SS-10 extends the 600-cell geometric scale grounding beyond the current $\Lambda_\text{QCD}$-fixed version.
- **Electromagnetic transition data** — for electromagnetic-contribution content beyond the pure-strong-force Strong Sector.

Each new source will be added as a sibling section to the AME 2020 section above, following the same template: citation, current URL, expected local filename and location, verification procedure, and which Strong Sector scripts depend on it.

---

**Related documentation:**
- `templates/operating_system.md` §11 — file naming conventions (papers, scripts, data files)
- `programmatic_decisions/PD-002-verification-tier-taxonomy.md` — verification tier definitions (INSPECTED / INDEPENDENTLY RECOMPUTED / SCRIPT-EXECUTED). Script-executed verification of data-dependent claims requires the external data files listed in this document.
- Individual paper-level READMEs (`series_strong/papers/SS-*/` folders) for paper-specific scripts and artifact inventories.

**Maintenance log:**
- 24 April 2026 — Initial version. AME 2020 section created for SS-8 v0.2 reproducibility scope. Authored during Claude Opus session with Thomas Lee Abshier, ND.

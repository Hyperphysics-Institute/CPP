# Open Problems Organization — Decision Pending

**Location:** `/CPP/open_problems/Open_Problems_Organization.md`
**Created:** 12 April 2026
**Status:** DECISION NEEDED — document and return

---

## The Question

Should open problems, conjectures, and propositions be stored centrally or distributed by series?

---

## Current State (April 2026)

Two patterns coexist in the repo:

**Centralized (current for open problems):** The `open_problems/` folder at root holds 50+ files with sector prefixes sorting them: OPEN-P-SS-*, OPEN-P-SM-*, OPEN-P-EW-*, OPEN-P-QM-*, OPEN-P-SD-*, OPEN-P-GLOBAL-*, plus conjecture files (CONJ-EW-1.md, CONJ-SM-6.md). The root-level registries (`predictions.md`, `axiom-registry.md`, `postulates_and_theorems.md`) are also centralized.

**Distributed (current for documentation):** The 7-file documentation suite per paper (mechanism, glossary, phenomena, philosophy, development, reviews, keywords) lives inside `series_[name]/papers/`. You find them next to the paper they document.

The OPEN-P notation was introduced mid-process. Some open problem files ended up in series subdirectories rather than the central folder.

---

## Arguments for Centralized (all in `/CPP/open_problems/`)

1. **Cross-cutting visibility.** An open problem in the strong sector (e.g., derive σ from lattice modes) may be the key to unlocking an SM-series result. A single folder shows the full landscape at a glance.

2. **Consistent with other registries.** `predictions.md`, `axiom-registry.md`, and `postulates_and_theorems.md` are all centralized at root. Open problems are the same kind of cross-cutting registry.

3. **Prefix naming already sorts by sector.** OPEN-P-SS-*, OPEN-P-SM-*, etc. give you sector filtering without directory separation.

4. **Simpler for new AI sessions.** "Read `open_problems/`" is one instruction. "Check each series directory for local open problems" requires knowing all series.

5. **Easier to count and audit.** "How many open problems do we have?" is `ls open_problems/ | wc -l`.

---

## Arguments for Distributed (each in `series_[name]/open_problems/`)

1. **Locality of reference.** When working on SM-9, you naturally look in the SM directory. Having the related open problems there keeps context together.

2. **Matches documentation suite pattern.** If `mechanism-SM-8.md` lives in the SM directory, why shouldn't `OPEN-P-SM-cage-1.md`?

3. **Reduces root clutter.** 50+ files in one folder is manageable; 200+ (as the programme grows) may not be.

4. **Natural for contributors.** A physicist interested in the strong sector browses `series_strong/` and finds everything relevant — papers, docs, AND open problems.

---

## Hybrid Option

Keep the central `open_problems/` folder as the registry of record, but allow series directories to contain symlinks or short stub files pointing back to the central registry. Best of both worlds, but adds complexity.

---

## What Needs Deciding

1. **Primary location:** Central (`open_problems/`) or distributed (`series_[name]/open_problems/`)?
2. **Conjectures:** Same location as open problems, or in `postulates_and_theorems.md` only?
3. **Propositions:** Same question — `propositions.md` at root is already centralized.
4. **Migration:** If distributed, move existing files from `open_problems/` to series directories. If centralized, sweep any strays back to `open_problems/`.

---

## Interim Rule (until decided)

New open problems go in `/CPP/open_problems/` with the standard prefix naming (OPEN-P-[SERIES]-[name].md). If a file ends up elsewhere, move it to `open_problems/` during the next housekeeping session. This preserves the existing pattern until a deliberate decision is made.

---

*Created 12 April 2026 during repo housekeeping session.*
*Return to this decision when the open problems count exceeds 75, or during the next major repo restructuring, whichever comes first.*

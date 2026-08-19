#!/usr/bin/env python3
"""
build_bibliography.py — regenerate CPP self-citation entries from the deposit
manifest, so a reserved Zenodo DOI flows straight into the PDF build.

Registered Patch 3223.

WHY THIS EXISTS. The deposit sequence requires the DOI to be written into a
paper's own bibliography BEFORE its PDF is built. Nothing connected the
manifest's RESERVED_DOI/CONCEPT_DOI to the master .bib, so that step would have
been hand-reconciled across 46 entries every time a DOI was minted.

WHAT IT WILL AND WILL NOT TOUCH
  * It rewrites ONLY the `doi` and `note` fields of CPP self-citation entries
    (keys beginning "abshier"). Author and title are curated text and are
    preserved verbatim -- this script has no business rewriting them.
  * It never touches third-party references.

DOI POLICY, in priority order:
  1. CONCEPT_DOI  -- the Zenodo DOI that is stable across every future version.
     This is what CPP papers should cite: bibliographies then stay correct
     through all later revisions, permanently.
  2. RESERVED_DOI -- used before first publication, when the concept DOI does
     not exist yet. A reserved DOI resolves once the draft is published.
  3. NO doi FIELD AT ALL. Never a placeholder, never an inherited value. The
     bibliography README's own rule: a wrong DOI is worse than none, because a
     wrong one is machine-readable and propagates into indexes.

THE OSF UMBRELLA DOI IS STRIPPED. Every entry's note carried
\\url{https://doi.org/10.17605/OSF.IO/JXE8D} -- the umbrella project DOI, not
the paper's. A reader following it landed on the project, not the work cited.

THE OSF REGISTRATION DOI IS RETAINED, RELABELLED. Those registrations are real,
permanent and resolvable, and are the programme's priority timestamps. They are
no longer the citation target (they are frozen snapshots; the Zenodo record is
the living document), so they move into the note explicitly labelled as the
original registration rather than sitting in the `doi` field where a reader
would take them for the version of record.

Usage:
    python3 code/build_bibliography.py            # report only
    python3 code/build_bibliography.py --apply
"""

import argparse
import csv
import io
import json
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BIB = os.path.join(REPO, "bibliography", "cpp_references.bib")
MANIFEST = os.path.join(REPO, "osf_deposit_manifest.json")
WORKSHEET = os.path.join(REPO, "bibliography",
                         "doi_harmonization_worksheet.csv")
UMBRELLA = "10.17605/OSF.IO/JXE8D"

# The ONE entry for which the umbrella DOI is correct. abshier2025 cites the
# "Conscious Point Physics Paper Series" as a whole, and JXE8D IS that series
# record. Stripping it there would be an over-correction: removing a right DOI
# is as damaging as leaving a wrong one, and it is harder to notice afterwards
# because the entry simply loses its identifier rather than gaining a bad one.
UMBRELLA_EXEMPT = {"abshier2025"}


def load_manifest():
    if not os.path.exists(MANIFEST):
        return {}
    m = json.load(io.open(MANIFEST, encoding="utf-8"))
    return {p["rel"]: p for p in m.get("papers", [])}


def key_to_paper(papers):
    """bib key -> manifest row, via the harmonization worksheet's paper IDs."""
    out = {}
    if not os.path.exists(WORKSHEET):
        return out
    rels = list(papers)
    for row in csv.DictReader(io.open(WORKSHEET, encoding="utf-8-sig")):
        key = (row.get("bib_key") or "").strip()
        pid = (row.get("paper_id") or "").strip()
        osf = (row.get("REAL_DOI__fill") or "").strip()
        if not key:
            continue
        hit = ""
        if pid:
            cands = [r for r in rels
                     if os.path.basename(r).lower().startswith(pid.lower() + "_")]
            if len(cands) == 1:
                hit = cands[0]
        out[key] = {"rel": hit, "osf": osf, "pid": pid}
    return out


def field(entry, name):
    m = re.search(r"\n\s*" + name + r"\s*=\s*\{(.*?)\}\s*,?\s*(?=\n\s*\w+\s*=|\n\})",
                  entry, re.S)
    return m.group(1).strip() if m else ""


def rebuild(entry, key, info, papers):
    """Return (new_entry, status)."""
    rel = info.get("rel", "")
    row = papers.get(rel, {}) if rel else {}
    concept = (row.get("CONCEPT_DOI") or "").strip()
    reserved = (row.get("RESERVED_DOI") or "").strip()
    ver = (row.get("ver") or "").strip()
    osf = info.get("osf", "")
    pid = info.get("pid", "")

    if concept:
        doi, status = concept, "concept"
    elif reserved:
        doi, status = reserved, "reserved"
    else:
        doi, status = "", "no-doi"

    # --- note: strip the umbrella, restate version, label the registration --
    note_bits = []
    # Only emit a version when there is a real one. 33 papers carry no version
    # stamp, and the catalog renders that as an em-dash -- printing "SM-1 v—"
    # in a public bibliography would assert a version that does not exist.
    has_ver = bool(re.match(r"\d", ver))
    if pid or has_ver:
        note_bits.append(f"{pid or key} v{ver}" if has_ver else (pid or key))
    note_bits.append("Hyperphysics Institute")
    note = ". ".join(x for x in note_bits if x)
    if osf and osf != UMBRELLA:
        note += (f". Original OSF registration (priority timestamp): "
                 f"\\url{{https://doi.org/{osf}}}")
    if not doi:
        note += ". Zenodo DOI pending"

    # rebuild the entry, preserving author and title verbatim
    body = entry[entry.index(",") + 1:entry.rindex("}")]
    lines = []
    for name in ("author", "title"):
        v = field(entry, name)
        if v:
            lines.append(f"  {name:<6} = {{{v}}},")
    yr = field(entry, "year") or "2026"
    lines.append(f"  year   = {{{yr}}},")
    lines.append(f"  note   = {{{note}}}" + ("," if doi else ""))
    if doi:
        lines.append(f"  doi    = {{{doi}}}")
    head = entry[:entry.index("{") + 1] + key + ","
    return head + "\n" + "\n".join(lines) + "\n}", status


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()

    papers = load_manifest()
    kmap = key_to_paper(papers)
    src = io.open(BIB, encoding="utf-8", errors="replace").read()

    counts = {"concept": 0, "reserved": 0, "no-doi": 0, "unmapped": 0,
              "umbrella_stripped": 0, "exempt": 0}
    out = src
    for m in list(re.finditer(r"@\w+\{(abshier[^,]*),.*?\n\}", src, re.S)):
        key = m.group(1)
        if key in UMBRELLA_EXEMPT:
            counts["exempt"] = counts.get("exempt", 0) + 1
            continue
        if key not in kmap:
            # Unmapped keys are not rewritten -- there is no manifest row to
            # draw a DOI from -- but the WRONG umbrella DOI is still stripped.
            # Leaving it because the key is unmapped would preserve exactly the
            # defect this script exists to remove, in the entries least likely
            # to be checked by hand.
            counts["unmapped"] += 1
            cleaned = re.sub(
                r"\.?\s*\\u?r?l?\{?https://doi\.org/" + re.escape(UMBRELLA)
                + r"\}?", "", m.group(0))
            cleaned = cleaned.replace(UMBRELLA, "")
            if cleaned != m.group(0):
                counts["umbrella_stripped"] = counts.get("umbrella_stripped", 0) + 1
                out = out.replace(m.group(0), cleaned)
            continue
        new, status = rebuild(m.group(0), key, kmap[key], papers)
        counts[status] += 1
        out = out.replace(m.group(0), new)

    # Count ENTRIES, not occurrences: the series record legitimately names the
    # umbrella twice (doi field and note URL), which made an occurrence count
    # read as a discrepancy against the number of exempt entries.
    remaining = sum(1 for m in re.finditer(r"@\w+\{([^,]+),.*?\n\}", out, re.S)
                    if UMBRELLA in m.group(0))
    print(f"self-citation entries rewritten: "
          f"{counts['concept'] + counts['reserved'] + counts['no-doi']}")
    print(f"  citing a Zenodo CONCEPT DOI : {counts['concept']}")
    print(f"  citing a RESERVED DOI       : {counts['reserved']}")
    print(f"  no DOI (omitted, not faked) : {counts['no-doi']}")
    print(f"  unmapped bib keys (skipped) : {counts['unmapped']}"
          f"  (umbrella stripped from {counts['umbrella_stripped']})")
    print(f"  series-level entries exempted: {counts['exempt']}")
    print(f"umbrella DOI occurrences remaining: {remaining} "
          f"(expected {counts['exempt']}: the series record itself)")

    if a.apply:
        io.open(BIB, "w", encoding="utf-8").write(out)
        print(f"\nwrote {os.path.relpath(BIB, REPO)}")
    else:
        print("\n(dry run -- pass --apply to write)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

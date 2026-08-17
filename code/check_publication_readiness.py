#!/usr/bin/env python3
"""
check_publication_readiness.py — decide which papers are ready to deposit.

Registered Patch 3207 (16 Aug 2026).

The gate is an ACTUAL COMPILE, not a heuristic. Each paper is built in an
isolated temp directory with its own source directory on TEXINPUTS, two
pdflatex passes so cross-references resolve. A paper that does not produce a
PDF cannot be deposited, whatever its version stamp claims.

Content flags are then applied to papers that DO compile:
  BLOCKER  — must be fixed before deposit
  MASSAGE  — should be reviewed; publishable but reads as internal
  NOTE     — informational

Usage:
    python3 code/check_publication_readiness.py [--jobs N] [--limit N]
"""

import argparse
import os
import re
import shutil
import subprocess
import tempfile
from concurrent.futures import ProcessPoolExecutor

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXCLUDE = ("archive/", "/duplicates/", "duplicates/", "/development/")

# --- content flag patterns -------------------------------------------------
# BLOCKERS: unfinished text, or text that must not appear in a public deposit.
BLOCKERS = [
    (r"\\todo\b|\bTODO\b|\bFIXME\b|\bTK TK\b", "unfinished marker (TODO/FIXME)"),
    (r"\bPLACEHOLDER\b|\blorem ipsum\b", "placeholder text"),
    (r"do not circulate|not for distribution|INTERNAL ONLY|CONFIDENTIAL",
     "not-for-circulation marker"),
    (r"\?\?\?+", "literal ??? in source"),
]

# MASSAGE: internal programme machinery that is meaningful in-repo but reads
# as jargon to an outside reader. Not wrong, just not for a public artifact.
MASSAGE = [
    (r"\bOPEN-[A-Z][A-Z0-9-]+", "internal open-problem ID (OPEN-...)"),
    (r"\bPatch\s+\d{3,4}[a-z]?\b", "internal patch number"),
    (r"\bCONV-\d+\b|\bPD-\d+\b|\bF-SW-\d+\b|\bR-[A-Z]{2,}-",
     "internal governance code"),
    (r"\bfounder ruling\b|\bfounders_voice\b", "internal governance reference"),
]


def find_papers():
    out = []
    for root, dirs, files in os.walk(REPO):
        dirs[:] = [d for d in dirs if d not in (".git",)]
        for fn in files:
            if not fn.endswith(".tex"):
                continue
            rel = os.path.relpath(os.path.join(root, fn), REPO).replace("\\", "/")
            if any(p in rel for p in EXCLUDE):
                continue
            try:
                with open(os.path.join(root, fn), encoding="utf-8",
                          errors="replace") as fh:
                    if "\\title{" not in fh.read():
                        continue
            except OSError:
                continue
            out.append(rel)
    return sorted(out)


def compile_one(rel):
    """Build in isolation. Returns a result dict; never raises."""
    src = os.path.join(REPO, rel)
    srcdir = os.path.dirname(src)
    res = {"path": rel, "ok": False, "err": "", "undef_ref": 0,
           "undef_cite": 0, "pages": 0}
    try:
        with tempfile.TemporaryDirectory() as td:
            shutil.copy(src, td)
            base = os.path.basename(rel)
            env = dict(os.environ)
            # Source dir on TEXINPUTS so \input, figures and .bib resolve.
            env["TEXINPUTS"] = f"{srcdir}//:{td}//:"
            env["BIBINPUTS"] = f"{srcdir}//:"
            log = ""
            for _ in range(2):
                p = subprocess.run(
                    ["pdflatex", "-interaction=nonstopmode",
                     "-file-line-error", base],
                    cwd=td, env=env, capture_output=True, text=True,
                    errors="replace", timeout=180)
                log = p.stdout
            pdf = os.path.join(td, base[:-4] + ".pdf")
            if os.path.exists(pdf) and os.path.getsize(pdf) > 5000:
                res["ok"] = True
                res["pages"] = len(re.findall(r"\[\d+", log))
            else:
                m = re.search(r"^(?:.*?:\d+:|!)\s*(.+)$", log, re.M)
                res["err"] = (m.group(1).strip()[:110] if m
                              else "no PDF produced")
            res["undef_ref"] = len(re.findall(
                r"Reference `[^']*' on page .* undefined", log))
            res["undef_cite"] = len(re.findall(
                r"Citation `[^']*' on page .* undefined", log))
    except subprocess.TimeoutExpired:
        res["err"] = "TIMEOUT (>180s per pass)"
    except Exception as e:                                    # noqa: BLE001
        res["err"] = f"{type(e).__name__}: {e}"[:110]
    return res


def scan_content(rel):
    try:
        with open(os.path.join(REPO, rel), encoding="utf-8",
                  errors="replace") as fh:
            text = fh.read()
    except OSError:
        return [], []
    # Strip comment lines: internal notes in % comments never reach the PDF.
    body = "\n".join(re.sub(r"(?<!\\)%.*$", "", ln) for ln in text.splitlines())
    blockers, massage = [], []
    for pat, label in BLOCKERS:
        n = len(re.findall(pat, body, re.I))
        if n:
            blockers.append(f"{label} ×{n}")
    for pat, label in MASSAGE:
        n = len(re.findall(pat, body))
        if n:
            massage.append(f"{label} ×{n}")
    return blockers, massage


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--limit", type=int)
    args = ap.parse_args()

    papers = find_papers()
    if args.limit:
        papers = papers[:args.limit]
    print(f"Compiling {len(papers)} papers with {args.jobs} workers...")

    with ProcessPoolExecutor(max_workers=args.jobs) as ex:
        results = list(ex.map(compile_one, papers))

    for r in results:
        r["blockers"], r["massage"] = scan_content(r["path"])
        if not r["ok"]:
            r["verdict"] = "BLOCKED — does not compile"
        elif r["blockers"]:
            r["verdict"] = "BLOCKED — content"
        elif r["massage"] or r["undef_ref"] or r["undef_cite"]:
            r["verdict"] = "MASSAGE"
        else:
            r["verdict"] = "READY"

    order = {"READY": 0, "MASSAGE": 1, "BLOCKED — content": 2,
             "BLOCKED — does not compile": 3}
    results.sort(key=lambda r: (order[r["verdict"]], r["path"]))

    out = os.path.join(REPO, "publication_readiness.md")
    with open(out, "w", encoding="utf-8") as fh:
        w = fh.write
        n = len(results)
        counts = {k: sum(1 for r in results if r["verdict"] == k)
                  for k in order}
        w("# Publication readiness — which papers can be deposited\n\n")
        w("**Generated by `code/check_publication_readiness.py` "
          "(Patch 3207).** Re-run any time; nothing here is hand-maintained.\n\n")
        w("**The gate is an actual compile.** Every paper is built in an "
          "isolated temp directory, two `pdflatex` passes so cross-references "
          "resolve, source directory on `TEXINPUTS`. A paper that does not "
          "produce a PDF cannot be deposited, whatever its version stamp "
          "says. Content flags are applied only to papers that compile.\n\n")
        w(f"| Verdict | Count | Meaning |\n|---|---|---|\n")
        w(f"| **READY** | {counts['READY']} of {n} | Compiles clean, no "
          "unfinished markers, no internal jargon in the rendered text. "
          "Deposit as-is. |\n")
        w(f"| **MASSAGE** | {counts['MASSAGE']} | Compiles, but the PDF "
          "carries internal programme machinery (patch numbers, OPEN- IDs, "
          "governance codes) or has unresolved refs/citations. Publishable "
          "after a read-through. |\n")
        w(f"| **BLOCKED — content** | {counts['BLOCKED — content']} | "
          "Compiles, but contains unfinished markers or not-for-circulation "
          "text. Must be fixed. |\n")
        w(f"| **BLOCKED — compile** | "
          f"{counts['BLOCKED — does not compile']} | Produces no PDF. "
          "Cannot be deposited at all. |\n\n")
        w("Comment lines (`%`) are stripped before content scanning — "
          "internal notes in comments never reach the PDF and are not "
          "flagged.\n\n---\n\n")

        for verdict in order:
            rs = [r for r in results if r["verdict"] == verdict]
            if not rs:
                continue
            w(f"## {verdict} — {len(rs)}\n\n")
            if verdict == "READY":
                w("| Paper | Pages |\n|---|---|\n")
                for r in rs:
                    w(f"| `{r['path']}` | {r['pages'] or '—'} |\n")
            elif verdict == "BLOCKED — does not compile":
                w("| Paper | First error |\n|---|---|\n")
                for r in rs:
                    w(f"| `{r['path']}` | {r['err'] or '—'} |\n")
            else:
                w("| Paper | Findings |\n|---|---|\n")
                for r in rs:
                    bits = list(r["blockers"]) + list(r["massage"])
                    if r["undef_ref"]:
                        bits.append(f"undefined refs ×{r['undef_ref']}")
                    if r["undef_cite"]:
                        bits.append(f"undefined citations ×{r['undef_cite']}")
                    w(f"| `{r['path']}` | {'; '.join(bits)} |\n")
            w("\n")

    print(f"publication_readiness.md written.")
    for k in order:
        print(f"  {k:30}: {counts[k]}")


if __name__ == "__main__":
    main()

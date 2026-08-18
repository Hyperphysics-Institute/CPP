#!/usr/bin/env python3
"""
identifier_glossary.py — make internal programme identifiers legible to the
public, per the founder ruling of 16 Aug 2026.

RULING: "If there is internal code/jargon that the public cannot read, it is
noise and distracts from the content. If it is in a public paper, it should be
intelligible to the public with minimal effort (going to a reference, or a
glossary, or appendix, or a footnote)."

METHOD. The corpus carries 1138 identifier sites across 62 papers but only ~85
DISTINCT identifiers. Rewriting prose at 1138 sites in shipped papers is not
something that can be done reliably without risking the mathematics, so the
ruling's appendix option is taken instead: each affected paper gains a short
generated appendix glossing ONLY the identifiers it actually uses. The
identifiers stay in the text, so traceability is preserved, and the reader
reaches a plain-language explanation without leaving the PDF.

Glosses come from two sources, harvested first and hand-written second:
  1. "**One-line statement:**" fields in research_frontier.md and
     frontier_sectors/*.md   (authoritative; already written for the programme)
  2. glossary/identifier_glosses_manual.md  (for identifiers with no such field)

Usage:
    python3 code/identifier_glossary.py --build     # emit merged registry
    python3 code/identifier_glossary.py --report    # coverage, change nothing
    python3 code/identifier_glossary.py --inject    # write appendices
    python3 code/identifier_glossary.py --inject --only path/to/paper.tex
"""

import argparse
import io
import os
import re
import sys
from collections import Counter, defaultdict

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANUAL = os.path.join(REPO, "glossary", "identifier_glosses_manual.md")
REGISTRY = os.path.join(REPO, "glossary", "programme_identifiers.md")
EXCLUDE = ("archive/", "/duplicates/", "duplicates/", "/development/")

BEGIN = "% BEGIN GENERATED IDENTIFIER APPENDIX -- do not edit by hand"
END = "% END GENERATED IDENTIFIER APPENDIX"

# Identifiers must not end in a hyphen: a trailing hyphen means the regex has
# truncated a longer identifier (OPEN-FP-SF-2-$\eta$ contains LaTeX math and
# was being captured as "OPEN-FP-SF-2-"). Four phantom identifiers in the first
# survey came from exactly this.
# Five identifier families appear in public papers, not one. The 3211 pass
# glossed only OPEN-, leaving ~1530 THEO-/FI-/PRED-/CONJ-/PH- sites across 58
# papers unexplained -- the same defect the ruling was issued to fix.
#   OPEN-  unresolved question        THEO-  proved theorem
#   FI-    foundational input         PRED-  registered prediction
#   CONJ-  conjecture                 PH-    problem history
ID_RE = re.compile(r"\b(?:OPEN|THEO|FI|PRED|CONJ|PH)-[A-Z0-9][A-Z0-9-]*[A-Z0-9]")


def strip_comments(text):
    """% comments never reach the PDF, so they are not public jargon."""
    return "\n".join(re.sub(r"(?<!\\)%.*$", "", ln) for ln in text.splitlines())


def papers():
    out = []
    for root, dirs, fs in os.walk(REPO):
        dirs[:] = [d for d in dirs if d != ".git"]
        for fn in fs:
            if not fn.endswith(".tex"):
                continue
            p = os.path.relpath(os.path.join(root, fn), REPO).replace("\\", "/")
            if any(x in p for x in EXCLUDE):
                continue
            try:
                t = io.open(os.path.join(REPO, p), encoding="utf-8",
                            errors="replace").read()
            except OSError:
                continue
            if "\\title{" in t:
                out.append((p, t))
    return sorted(out)


def harvest_theorem_sources():
    """THEO- glosses from the dependency graph and the theorem registry.
    Graph style:    **THEO-SM-1** (Particle-type cage taxonomy): ...
    Registry style: | **THEO-SS-17** | Short name | Full statement |
    """
    gl = {}
    g = os.path.join(REPO, "theorem-dependency-graph.md")
    if os.path.exists(g):
        txt = io.open(g, encoding="utf-8", errors="replace").read()
        for m in re.finditer(
                r"\*\*((?:THEO|PROP|FI|PRED|CONJ)-[A-Z0-9-]+)\*\*\s*\(([^)]{4,200})\)", txt):
            gl.setdefault(m.group(1), (m.group(2).strip(), "theorem-graph"))
    r = os.path.join(REPO, "theorem-registry.md")
    if os.path.exists(r):
        txt = io.open(r, encoding="utf-8", errors="replace").read()
        for ln in txt.splitlines():
            if not ln.startswith("|"):
                continue
            cells = [c.strip().strip("*") for c in ln.strip().strip("|").split("|")]
            if len(cells) >= 2 and re.fullmatch(
                    r"(?:THEO|PROP|FI|PRED|CONJ)-[A-Z0-9-]+", cells[0]):
                for cand in cells[1:]:
                    if len(cand) > 8:
                        gl.setdefault(cells[0], (cand, "theorem-registry"))
                        break
    return gl


def harvest_frontier():
    gl = {}
    srcs = [os.path.join(REPO, "research_frontier.md")]
    fsdir = os.path.join(REPO, "frontier_sectors")
    if os.path.isdir(fsdir):
        srcs += [os.path.join(fsdir, f) for f in sorted(os.listdir(fsdir))
                 if f.endswith(".md")]
    for src in srcs:
        if not os.path.exists(src):
            continue
        txt = io.open(src, encoding="utf-8", errors="replace").read()
        for m in re.finditer(
                r"#{2,4}\s*(OPEN-[A-Z0-9-]+)[^\n]*\n(.*?)(?=\n#{2,4}\s|\Z)",
                txt, re.S):
            s = re.search(r"\*\*One-line statement:\*\*\s*(.+)", m.group(2))
            if s and m.group(1) not in gl:
                gl[m.group(1)] = (s.group(1).strip(), "frontier")
    return gl


def read_manual():
    gl = {}
    if not os.path.exists(MANUAL):
        return gl
    for ln in io.open(MANUAL, encoding="utf-8", errors="replace"):
        ln = ln.strip()
        if not ln or ln.startswith("#") or ln.startswith("`") or "|" not in ln:
            continue
        k, _, v = ln.partition("|")
        k, v = k.strip(), v.strip()
        if ID_RE.fullmatch(k) and v:
            gl[k] = (v, "manual")
    return gl


def tex_escape(s):
    """Glosses are prose from Markdown; make them LaTeX-safe."""
    s = s.replace("\\", "\\textbackslash{}")
    for ch in "&%$#_{}":
        s = s.replace(ch, "\\" + ch)
    s = s.replace("~", "\\textasciitilde{}").replace("^", "\\textasciicircum{}")
    return s


def collect():
    gl = harvest_frontier()
    for k, v in harvest_theorem_sources().items():
        gl.setdefault(k, v)
    for k, v in read_manual().items():
        gl.setdefault(k, v)          # frontier wins; manual fills gaps
    used = Counter()
    per_paper = defaultdict(set)
    for p, t in papers():
        body = strip_comments(t)
        found = set(ID_RE.findall(body))
        for i in found:
            used[i] += 1
            per_paper[p].add(i)
    return gl, used, per_paper


def build_registry(gl, used):
    L = ["# Programme identifier glossary", "",
         "**Generated by `code/identifier_glossary.py --build`. Do not edit "
         "this file** — edit `glossary/identifier_glosses_manual.md`, or the "
         "`**One-line statement:**` field in `frontier_sectors/`, then "
         "rebuild.", "",
         "Plain-language glosses for the internal identifiers appearing in "
         "public papers, per the founder ruling of 16 August 2026. Each "
         "affected paper carries a generated appendix glossing only the "
         "identifiers it uses; this file is the single source those "
         "appendices draw from.", "",
         "| Identifier | Papers | Gloss | Source |", "|---|---|---|---|"]
    for i in sorted(used, key=lambda x: (-used[x], x)):
        g, src = gl.get(i, ("**NO GLOSS**", "missing"))
        L.append(f"| `{i}` | {used[i]} | {g} | {src} |")
    L.append("")
    io.open(REGISTRY, "w", encoding="utf-8").write("\n".join(L) + "\n")


def appendix_block(ids, gl):
    L = [BEGIN,
         "\\clearpage",
         "\\section*{Appendix: Programme identifiers used in this paper}",
         "\\addcontentsline{toc}{section}{Appendix: Programme identifiers}",
         "",
         "\\noindent This programme tracks its results, assumptions and "
         "unresolved questions under short identifiers, so that a claim and "
         "its dependencies can be cited precisely. Prefixes denote the kind of "
         "item: \\texttt{THEO-} a proved theorem, \\texttt{FI-} a foundational "
         "input the derivation assumes, \\texttt{PRED-} a registered "
         "prediction, \\texttt{CONJ-} a conjecture, \\texttt{OPEN-} an "
         "unresolved question, \\texttt{PH-} a problem history. Those "
         "appearing in this paper are glossed below; no external document is "
         "needed to read them.",
         "",
         "\\begin{description}"]
    for i in sorted(ids):
        g, _ = gl.get(i, ("(gloss pending)", "missing"))
        L.append(f"  \\item[\\texttt{{{tex_escape(i)}}}] \\hfill \\\\ {tex_escape(g)}")
    L += ["\\end{description}", END]
    return "\n".join(L)


def inject(gl, per_paper, only=None):
    changed, skipped = [], []
    for p, t in papers():
        if only and p != only:
            continue
        ids = per_paper.get(p, set())
        if not ids:
            continue
        if "\\end{document}" not in t:
            skipped.append((p, "no \\end{document}"))
            continue
        block = appendix_block(ids, gl)
        if BEGIN in t:                      # idempotent refresh
            # The replacement is LaTeX and full of backslashes; a string repl
            # would have them parsed as regex escapes ("bad escape \c").
            new = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END),
                         lambda _m: block, t, flags=re.S)
        else:
            new = t.replace("\\end{document}", block + "\n\n\\end{document}", 1)
        if new != t:
            io.open(os.path.join(REPO, p), "w", encoding="utf-8").write(new)
            changed.append((p, len(ids)))
    return changed, skipped


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--build", action="store_true")
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--inject", action="store_true")
    ap.add_argument("--only")
    a = ap.parse_args()

    gl, used, per_paper = collect()
    missing = [i for i in used if i not in gl]

    if a.build or a.report:
        print(f"distinct identifiers in papers : {len(used)}")
        print(f"total sites                    : {sum(used.values())}")
        print(f"papers affected                : "
              f"{sum(1 for p in per_paper if per_paper[p])}")
        print(f"glossed                        : {len(used) - len(missing)}")
        print(f"MISSING GLOSS                  : {len(missing)}")
        for i in sorted(missing):
            print(f"    {i}  ({used[i]} papers)")
    if a.build:
        build_registry(gl, used)
        print(f"\nwrote {os.path.relpath(REGISTRY, REPO)}")
    if a.inject:
        if missing:
            print("REFUSING TO INJECT: identifiers without glosses would "
                  "render as '(gloss pending)' in a public PDF. Add them to "
                  "glossary/identifier_glosses_manual.md first.",
                  file=sys.stderr)
            return 1
        changed, skipped = inject(gl, per_paper, a.only)
        for p, n in changed:
            print(f"  +appendix ({n:2} ids)  {p}")
        for p, why in skipped:
            print(f"  SKIP  {why:22}  {p}")
        print(f"\n{len(changed)} papers updated, {len(skipped)} skipped.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

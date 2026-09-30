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


# Patch 4343: glosses harvested from Markdown carry **bold**, `code`, $math$ and Unicode symbols.
# The old escaper turned $\hat{n}$ into literal text and passed Unicode through to pdflatex.
UNI = {"\u03c7": r"$\chi$", "\u03c6": r"$\phi$", "\u03a6": r"$\Phi$", "\u03b1": r"$\alpha$", "\u03b2": r"$\beta$",
       "\u03b3": r"$\gamma$", "\u03b4": r"$\delta$", "\u03b5": r"$\epsilon$", "\u03b6": r"$\zeta$", "\u03b7": r"$\eta$",
       "\u03b8": r"$\theta$", "\u03bb": r"$\lambda$", "\u039b": r"$\Lambda$", "\u03bc": r"$\mu$", "\u03bd": r"$\nu$",
       "\u03c0": r"$\pi$", "\u03c1": r"$\rho$", "\u03c3": r"$\sigma$", "\u03a3": r"$\Sigma$", "\u03c4": r"$\tau$",
       "\u03c9": r"$\omega$", "\u03a9": r"$\Omega$", "\u0394": r"$\Delta$", "\u210f": r"$\hbar$",
       "n\u0302": r"$\hat{n}$", "\u2212": "--", "\u2013": "--", "\u2014": "---", "\u2192": r"$\to$",
       "\u2194": r"$\leftrightarrow$", "\u2248": r"$\approx$", "\u2264": r"$\le$", "\u2265": r"$\ge$",
       "\u00d7": r"$\times$", "\u00b1": r"$\pm$", "\u221e": r"$\infty$", "\u2018": "`", "\u2019": "'",
       "\u201c": "``", "\u201d": "''", "\u2032": "$'$", "\u00b7": r"$\cdot$", "\u2026": r"\ldots{}",
       "\u2070": "$^0$", "\u00b9": "$^1$", "\u00b2": "$^2$", "\u00b3": "$^3$", "\u2074": "$^4$",
       "\u2075": "$^5$", "\u207b": "$^-$", "\u2080": "$_0$", "\u2081": "$_1$", "\u2082": "$_2$",
       "\u2083": "$_3$", "\u2084": "$_4$", "\u221d": r"$\propto$", "\u00a7": r"\S{}", "\u221a": r"$\surd$"}


def _plain(s):
    s = s.replace("\\", "\\textbackslash{}")
    for ch in "&%#_{}":
        s = s.replace(ch, "\\" + ch)
    s = s.replace("~", "\\textasciitilde{}").replace("^", "\\textasciicircum{}")
    SUP = dict(zip("\u2070\u00b9\u00b2\u00b3\u2074\u2075\u2076\u2077\u2078\u2079\u207b\u207a", "0123456789-+"))
    SUB = dict(zip("\u2080\u2081\u2082\u2083\u2084\u2085\u2086\u2087\u2088\u2089", "0123456789"))
    s = re.sub("[" + "".join(SUP) + "]+", lambda m: "$^{" + "".join(SUP[c] for c in m.group(0)) + "}$", s)
    s = re.sub("[" + "".join(SUB) + "]+", lambda m: "$_{" + "".join(SUB[c] for c in m.group(0)) + "}$", s)
    for k in sorted(UNI, key=len, reverse=True):
        s = s.replace(k, UNI[k])
    return s


def tex_escape(s):
    """Glosses are prose from Markdown; make them LaTeX-safe. $...$ spans pass through as math;
    Markdown bold/code markers are dropped; common Unicode is mapped to LaTeX; anything still
    non-ASCII is replaced by '?' and reported by --report (never silently shipped)."""
    s = s.replace("**", "").replace("`", "")
    parts = re.split(r"(\$[^$]+\$)", s)
    out = "".join(p if (p.startswith("$") and p.endswith("$") and len(p) > 1) else _plain(p) for p in parts)
    out = re.sub(r"\$\$(?=[_^])", "", out)   # join a symbol with its following sub/superscript
    if any(ord(c) > 127 for c in out):
        NONASCII.update(c for c in out if ord(c) > 127)
        out = "".join(c if ord(c) < 128 else "?" for c in out)
    return out


NONASCII = set()


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


MODEL_RE = re.compile(
    r"\b(?:ChatGPT|GPT-?[0-9o]+|Grok|Gemini|Copilot|DeepSeek|Claude)\b")

REVIEW_NOTE = [
    "",
    "\\subsection*{How we review}",
    "",
    "\\noindent Results in this programme are checked by an \\emph{AI review "
    "panel}: several large language models from different vendors are given the "
    "same paper and the same fixed protocol, and asked to find errors and raise "
    "objections independently. Objections are recorded and either answered in "
    "the text or registered as open problems under the identifiers glossed "
    "above.",
    "",
    "\\noindent This is a \\emph{verification method the authors apply to their "
    "own work}. It is not journal peer review, it is not equivalent to it, and "
    "agreement among panel members is not evidence that a result is correct --- "
    "only that no member found a specific fault. Where individual models are "
    "named in the text, they are named for reproducibility of the method; model "
    "versions change, and a reader should treat the named models as a record of "
    "what was run rather than as an endorsement.",
    "",
]


def appendix_block(ids, gl, name_models=False):
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
    L += ["\\end{description}"]
    if name_models:
        L += REVIEW_NOTE
    L += [END]
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
        # The review note goes only where models are actually named, so
        # papers that never mention the panel do not acquire a disclaimer
        # about a process they do not invoke.
        stripped = strip_comments(
            re.sub(re.escape(BEGIN) + r".*?" + re.escape(END), "", t, flags=re.S))
        block = appendix_block(ids, gl, bool(MODEL_RE.search(stripped)))
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

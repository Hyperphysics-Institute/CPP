#!/usr/bin/env python3
# integrity_audit.py — publication INTEGRITY gate (OPEN-WORKFLOW-PREDICTION-AUDIT).
#
# Registered Patch 2477 (Session AUDIT-WARM-2476), 15 July 2026, in response to the
# SR-1 triage (Patches 2471-2475): a normalisation convention billed for four months
# as a zero-parameter prediction, five void predictions, a false theorem (H.1), and
# four citations of Monte-Carlo scripts that were stubs. Every defect was invisible
# at read-time. This tool checks the ARTIFACTS, not the prose.
#
# Distinct from scripts/publication_audit.sh's completion checks (did each mandated
# artifact get touched); this gate asks: is what got touched REAL. It is invoked by
# publication_audit.sh and inherits into the gate's FAIL. It can also run standalone,
# per-paper or programme-wide.
#
# FAIL conditions (from handovers/2026-07-15_* and frontier_sectors/WORKFLOW.md
# OPEN-WORKFLOW-PREDICTION-AUDIT (a)-(f)):
#   F1  cited script absent from the repo                              [spec (a)]
#   F2  cited script does not parse / does not execute (with --run)    [spec (b)]
#   F3  cited script imports outside stdlib without declaring it       [spec (b)]
#   F4  stub code: empty-collection init + pass-only loop/function     [spec (a,b)]
#   F5  elision markers in code ("for brevity", "in this response",
#       "full version in repo", ...)                                   [gate spec]
#   F6  dimensional-necessity billing in paper prose ("dimensional
#       analysis forces the prefactor")                                [spec (d)]
#   F7  frontier WITHDRAWN/RETRACTED status vs live zero-parameter
#       billing in the same paper                                      [spec (f)]
# WARN conditions (need a human adjudicator; cannot be graded mechanically):
#   W1  hard-coded numeric output: print of a string literal carrying
#       high-precision decimals (the fabricated-MC signature)          [spec (c)]
#   W2  absorption billing: "absorbed into the normalisation" /
#       "set to unity" cohabiting with "zero-parameter"                [spec (d)]
#   W3  elision markers in prose (.tex/.md) — common academic usage,
#       flagged for review, not auto-failed
#   W4  possible circularity: a variable named target/expected/ref
#       assigned a literal AND used before the comparison section      [spec (c)]
#   W5  identity billing: "by construction" / "exactly recovers"
#       within reach of "prediction" (the gamma-bridge pattern)        [spec (e)]
#
# stdlib only. Exit 0 = clean, 1 = FAIL present, 2 = usage/setup error.
#
# Usage:
#   python3 scripts/integrity_audit.py --paper SR-1
#   python3 scripts/integrity_audit.py --dir series_relativity
#   python3 scripts/integrity_audit.py --all [--report out.md]
#   add --run to actually execute cited scripts (timeout 240 s each)

import argparse, ast, os, re, subprocess, sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

# ---------------------------------------------------------------- helpers

STDLIB = set(getattr(sys, "stdlib_module_names", ())) | {"__future__"}

ELISION_RE = re.compile(
    r"for brevity|in this response|full (?:version|implementation) (?:in|available)|"
    r"left as an exercise|would be implemented|actual implementation|"
    r"simplified for (?:this|the) (?:demo|example|illustration)", re.I)

DIMFORCE_RE = re.compile(
    r"dimensional analysis[^.\n]{0,120}?(?:forces|fixes|requires|implies|sets|determines)"
    r"[^.\n]{0,120}?(?:prefactor|coefficient|identically|unity|order one|order-one)", re.I | re.S)

ABSORB_RE = re.compile(
    r"absorbed into the normali[sz]ation|absorbed into k\b|set to unity|"
    r"consistent use of units|taken to be unity", re.I)

ZEROPARAM_RE = re.compile(
    r"zero[- ]parameter|no adjustable parameters?|parameter[- ]free|"
    r"no free parameters?", re.I)

WITHDRAWN_RE = re.compile(
    r"WITHDRAWN|RETRACTED|VOID(?:ED)?\b|REVERSED|REJECTED|DEMOTED|"
    r"\*\*(?:withdrawn|retracted|void(?:ed)?|reversed|rejected|demoted)\*\*")

IDENTITY_RE = re.compile(
    r"(?:by construction|exactly recovers|identically equal|is an identity)", re.I)

HARDCODED_PRINT_RE = re.compile(
    r"""print\s*\(\s*(?:f?["'])[^"']*\d\.\d{5,}[^"']*["']\s*(?:\)|,)""")

CITE_RE = re.compile(r"""[\w./\\-]+?\.(?:py|ipynb|sh)\b""")

TARGETVAR_RE = re.compile(r"^\s*(target|expected|reference|ref_value|exp_val)\w*\s*=\s*[\d(\[-]",
                          re.M | re.I)

def read(path):
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            return f.read()
    except OSError:
        return ""

def rel(p):
    return os.path.relpath(p, REPO)

# ------------------------------------------------------- citation resolve

def collect_citations(paperdir):
    """All script filenames cited in .tex/.md under paperdir (recursive,
    skipping .git). Returns {cited_token: set(citing_files)}."""
    cites = {}
    for root, dirs, files in os.walk(paperdir):
        dirs[:] = [d for d in dirs if d != ".git"]
        for fn in files:
            if not fn.endswith((".tex", ".md")):
                continue
            path = os.path.join(root, fn)
            txt = read(path).replace("\\_", "_")   # un-escape LaTeX underscores
            for m in CITE_RE.finditer(txt):
                tok = m.group(0)
                if m.start() > 0 and txt[m.start() - 1] in "*?":
                    continue   # glob fragment (e.g. `*_numerics.py`), not a citation
                tok = tok.replace("\\", "/").lstrip("./")
                base = os.path.basename(tok)
                # skip obvious non-repo references and self-references
                if base in (fn,) or base.startswith(("http", "www.")) \
                        or "..." in tok or "/." in tok or base in ("thisfile.py",):
                    continue
                after = txt[m.end():m.end() + 60]
                planned = bool(re.search(
                    r"planned|forthcoming|to be (?:written|added|committed)|TODO",
                    after, re.I))
                key = cites.setdefault(tok, {"citers": set(), "planned": True})
                key["citers"].add(rel(path))
                key["planned"] &= planned   # planned only if EVERY cite says so
    return cites

def resolve(tok, paperdir, basename_index):
    """Resolve a cited token to a repo path: relative to paperdir, repo root,
    then by unique basename anywhere in the repo."""
    if "github.com" in tok and "/main/" in tok:
        tok = tok.split("/main/", 1)[1]
    for anchor in (paperdir, REPO):
        p = os.path.normpath(os.path.join(anchor, tok))
        if os.path.isfile(p):
            return p
    if tok.startswith("CPP/"):
        p = os.path.normpath(os.path.join(REPO, tok[4:]))
        if os.path.isfile(p):
            return p
    hits = basename_index.get(os.path.basename(tok), [])
    if len(hits) == 1:
        return hits[0]
    if len(hits) > 1:
        # prefer the copy nearest the paper (longest shared path prefix)
        def shared(p):
            a, b = rel(p).split("/"), rel(paperdir).split("/")
            n = 0
            while n < min(len(a), len(b)) and a[n] == b[n]:
                n += 1
            return n
        best = sorted(hits, key=shared, reverse=True)
        if shared(best[0]) > 0 and (len(best) == 1 or shared(best[0]) > shared(best[1])):
            return best[0]
    return None

def build_basename_index():
    idx = {}
    for root, dirs, files in os.walk(REPO):
        dirs[:] = [d for d in dirs if d != ".git"]
        for fn in files:
            if fn.endswith((".py", ".ipynb", ".sh")):
                idx.setdefault(fn, []).append(os.path.join(root, fn))
    return idx

# --------------------------------------------------------- script checks

def check_script(path, run=False):
    """Return list of (LEVEL, CODE, detail) findings for one .py file."""
    out = []
    src = read(path)
    if not src.strip():
        out.append(("FAIL", "F4-STUB", "file is empty"))
        return out
    m = ELISION_RE.search(src)
    if m:
        out.append(("FAIL", "F5-ELISION", f'marker "{m.group(0)}"'))
    if HARDCODED_PRINT_RE.search(src):
        out.append(("WARN", "W1-HARDCODED-PRINT",
                    "print() of a string literal carrying >=6-sig-fig decimals "
                    "(fabricated-output signature; verify the number is computed)"))
    if TARGETVAR_RE.search(src):
        out.append(("WARN", "W4-CIRCULARITY?",
                    "target/expected/reference variable assigned a literal; "
                    "check the input data is not generated from it"))
    # AST-level stub detection
    try:
        tree = ast.parse(src)
    except SyntaxError as e:
        out.append(("FAIL", "F2-NOPARSE", f"SyntaxError line {e.lineno}: {e.msg}"))
        return out
    empty_inits, mutated = set(), set()
    for node in ast.walk(tree):
        if isinstance(node, (ast.For, ast.While, ast.FunctionDef, ast.AsyncFunctionDef)):
            body = [n for n in node.body
                    if not (isinstance(n, ast.Expr) and isinstance(n.value, ast.Constant))]
            if len(body) == 1 and isinstance(body[0], ast.Pass):
                kind = type(node).__name__
                name = getattr(node, "name", "")
                out.append(("FAIL", "F4-STUB", f"{kind} {name} body is a bare pass "
                            f"(line {node.lineno})"))
        if isinstance(node, ast.Assign):
            is_empty = isinstance(node.value, (ast.List, ast.Dict)) \
                and not getattr(node.value, "elts", None) \
                and not getattr(node.value, "keys", None)
            for t in node.targets:
                if isinstance(t, ast.Name):
                    if is_empty and t.id not in empty_inits and t.id not in mutated:
                        empty_inits.add(t.id)
                    else:
                        mutated.add(t.id)   # any other assignment fills it
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) \
                and node.func.attr in ("append", "extend", "add", "insert", "update") \
                and isinstance(node.func.value, ast.Name):
            mutated.add(node.func.value.id)
        if isinstance(node, ast.Subscript):  # x[k] = ... style
            tgt = node.value
            if isinstance(tgt, ast.Name):
                mutated.add(tgt.id)
    never_filled = empty_inits - mutated
    for name in sorted(never_filled):
        # only flag if the name is USED after the empty init (the SR-1 pattern)
        uses = sum(1 for n in ast.walk(tree)
                   if isinstance(n, ast.Name) and n.id == name
                   and isinstance(n.ctx, ast.Load))
        if uses:
            out.append(("FAIL", "F4-STUB",
                        f"'{name} = []/{{}}' never filled but used {uses}x "
                        "(SR-1 fabricated-MC pattern)"))
    # imports vs stdlib
    nonstd = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            nonstd |= {a.name.split(".")[0] for a in node.names}
        elif isinstance(node, ast.ImportFrom) and node.module and node.level == 0:
            nonstd.add(node.module.split(".")[0])
    nonstd -= STDLIB
    nonstd = {m for m in nonstd
              if not os.path.isfile(os.path.join(os.path.dirname(path), m + ".py"))}
    if nonstd:
        declared = re.search(r"pip install|requirements|dependenc|requires:", src, re.I)
        lvl = "WARN" if declared else "FAIL"
        code = "F3-NONSTDLIB" if not declared else "W-NONSTDLIB-DECLARED"
        out.append((lvl, code, f"non-stdlib imports: {', '.join(sorted(nonstd))}"
                    + ("" if declared else " (undeclared)")))
    if run:
        try:
            r = subprocess.run([sys.executable, path], capture_output=True,
                               timeout=240, cwd=os.path.dirname(path))
            if r.returncode != 0:
                tail = (r.stderr or r.stdout)[-300:].decode(errors="replace")
                out.append(("FAIL", "F2-RUNFAIL", f"exit {r.returncode}: ...{tail}"))
        except subprocess.TimeoutExpired:
            out.append(("WARN", "W-TIMEOUT", "did not finish in 240 s"))
        except OSError as e:
            out.append(("FAIL", "F2-RUNFAIL", str(e)))
    return out

# ----------------------------------------------------------- prose checks

def check_prose(paperdir):
    out = []
    for root, dirs, files in os.walk(paperdir):
        dirs[:] = [d for d in dirs if d != ".git"]
        for fn in files:
            if not fn.endswith((".tex", ".md")):
                continue
            path = os.path.join(root, fn)
            txt = read(path)
            for m in DIMFORCE_RE.finditer(txt):
                ctx = txt[max(0, m.start() - 400):m.end() + 400]
                if re.search(r"withdraw|retract|correct(?:ion|ed)|is invalid|"
                             r"that argument|earlier versions?", ctx, re.I):
                    continue   # quoted inside a withdrawal — not live billing
                out.append(("FAIL", "F6-DIMFORCE", rel(path),
                            m.group(0)[:110].replace("\n", " ")))
            is_tex = fn.endswith(".tex")
            if is_tex and ABSORB_RE.search(txt) and ZEROPARAM_RE.search(txt):
                out.append(("WARN", "W2-ABSORB-BILLING", rel(path),
                            "absorption language cohabits with zero-parameter billing"))
            m = ELISION_RE.search(txt) if is_tex else None
            if m:
                out.append(("WARN", "W3-ELISION-PROSE", rel(path),
                            f'"{m.group(0)}"'))
            if is_tex and IDENTITY_RE.search(txt) and ZEROPARAM_RE.search(txt) \
                    and re.search(r"predict", txt, re.I):
                out.append(("WARN", "W5-IDENTITY-BILLING", rel(path),
                            "identity language + prediction billing in one file "
                            "(gamma-bridge pattern; adjudicate)"))
    return out

def live_zeroparam(path):
    """True if the file carries zero-parameter billing OUTSIDE withdrawal context."""
    txt = read(path)
    for m in ZEROPARAM_RE.finditer(txt):
        ctx = txt[max(0, m.start() - 250):m.end() + 250]
        if not re.search(r"withdraw|retract|correct(?:ion|ed)|void", ctx, re.I):
            return True
    return False

def check_frontier(paper_id, paperdir):
    """F7: WITHDRAWN status in the frontier vs live zero-parameter billing."""
    out = []
    frontier_files = [os.path.join(REPO, "research_frontier.md")]
    sect = os.path.join(REPO, "frontier_sectors")
    if os.path.isdir(sect):
        frontier_files += [os.path.join(sect, f) for f in os.listdir(sect)
                           if f.endswith(".md")]
    withdrawn = []
    pid = re.escape(paper_id)
    for f in frontier_files:
        for i, line in enumerate(read(f).splitlines(), 1):
            for m in re.finditer(rf"(?<!OPEN-)\b{pid}\b", line):
                window = line[max(0, m.start() - 150):m.end() + 150]
                if WITHDRAWN_RE.search(window):
                    withdrawn.append(f"{rel(f)}:{i}")
                    break
    if not withdrawn:
        return out
    live_own, live_neighbor = [], []
    for root, dirs, files in os.walk(paperdir):
        dirs[:] = [d for d in dirs if d != ".git"]
        for fn in files:
            if fn.endswith(".tex") and live_zeroparam(os.path.join(root, fn)):
                (live_own if fn.upper().startswith(paper_id.upper())
                 else live_neighbor).append(rel(os.path.join(root, fn)))
    wsrc = (f"{withdrawn[0]}" + (f" +{len(withdrawn)-1} more"
            if len(withdrawn) > 1 else ""))
    if live_own:
        out.append(("FAIL", "F7-CONTRADICTION", live_own[0],
                    f"frontier records withdrawal ({wsrc}) but the paper "
                    "still bills zero-parameter"))
    elif live_neighbor:
        out.append(("WARN", "W-F7-NEIGHBOR", live_neighbor[0],
                    f"{paper_id} withdrawal in frontier ({wsrc}); this "
                    "co-resident paper bills zero-parameter — check "
                    "inheritance (blast radius)"))
    else:
        out.append(("WARN", "W-FRONTIER-NOTE", withdrawn[0],
                    "withdrawal recorded in frontier; no live "
                    "zero-parameter billing found (consistent)"))
    return out

# --------------------------------------------------------------- drivers

def foreign(relpath, paper_id, all_ids):
    """True if this path belongs to a DIFFERENT paper (per-paper scope guard)."""
    if not paper_id or not all_ids:
        return False
    up = relpath.upper().replace("\\", "/")
    for oid in all_ids:
        if oid == paper_id.upper():
            continue
        for seg in up.split("/"):
            if seg == oid or seg.startswith(oid + "_") or seg.startswith(oid + "-"):
                return True
    return False

def audit_paper(paper_id, paperdir, basename_index, run=False, all_ids=None):
    findings = []          # (level, code, where, detail)
    cites = collect_citations(paperdir)
    checked = set()
    for tok, meta in sorted(cites.items()):
        citers = {c for c in meta["citers"] if not foreign(c, paper_id, all_ids)}
        if not citers:
            continue
        p = resolve(tok, paperdir, basename_index)
        if p is None:
            if meta["planned"]:
                findings.append(("WARN", "W-PLANNED-SCRIPT", sorted(citers)[0],
                                 f"cited script marked planned, not yet in repo: {tok}"))
            else:
                findings.append(("FAIL", "F1-MISSING", sorted(citers)[0],
                                 f"cited script not found in repo: {tok}"))
            continue
        if p in checked or not p.endswith(".py"):
            continue
        checked.add(p)
        for lvl, code, detail in check_script(p, run=run):
            findings.append((lvl, code, rel(p), detail))
    findings += [f for f in check_prose(paperdir)
                 if not foreign(f[2], paper_id, all_ids)]
    if paper_id:
        findings += check_frontier(paper_id, paperdir)
    return findings

def find_paperdir(paper_id):
    pid = paper_id.lower()
    for root, dirs, files in os.walk(REPO):
        dirs[:] = [d for d in dirs if d != ".git"]
        for fn in files:
            if fn.lower().startswith(pid + "_") and fn.endswith(".tex"):
                return root
    return None

def discover_all():
    """Every dir containing a *-ID_*.tex paper file → {ID: dir} (first hit wins,
    archive/ excluded)."""
    found = {}
    idre = re.compile(r"^([A-Za-z]{1,4}-\d+[a-z]?)_.*\.tex$", re.I)
    for root, dirs, files in os.walk(REPO):
        dirs[:] = [d for d in dirs if d not in (".git", "archive")]
        for fn in files:
            m = idre.match(fn)
            if m:
                found.setdefault(m.group(1).upper(), root)
    return found

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--paper")
    ap.add_argument("--dir")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--run", action="store_true",
                    help="actually execute cited scripts (timeout 240 s each)")
    ap.add_argument("--report", help="write a Markdown report to this path")
    a = ap.parse_args()

    idx = build_basename_index()
    all_ids = set(discover_all().keys())
    jobs = []
    if a.all:
        jobs = sorted(discover_all().items())
    elif a.paper:
        d = find_paperdir(a.paper)
        if not d:
            print(f"ERROR: no {a.paper}_*.tex found in repo"); return 2
        jobs = [(a.paper.upper(), d)]
    elif a.dir:
        d = os.path.join(REPO, a.dir)
        if not os.path.isdir(d):
            print(f"ERROR: no such dir {a.dir}"); return 2
        jobs = [(None, d)]
    else:
        ap.print_help(); return 2

    any_fail = False
    collected = []
    lines = ["# Integrity audit report", ""]
    for pid, d in jobs:
        findings = audit_paper(pid, d, idx, run=a.run, all_ids=all_ids)
        collected.append((pid, d, findings))
        fails = [f for f in findings if f[0] == "FAIL"]
        warns = [f for f in findings if f[0] == "WARN"]
        verdict = "FAIL" if fails else ("WARN" if warns else "clean")
        any_fail |= bool(fails)
        hdr = f"{pid or rel(d)}  [{verdict}]  ({len(fails)} fail / {len(warns)} warn)  {rel(d)}"
        print("=" * 78); print(hdr)
        lines += [f"## {hdr}", ""]
        for lvl, code, where, detail in findings:
            row = f"  [{lvl}] {code:24s} {where}\n         {detail}"
            print(row)
            lines.append(f"- **{lvl}** `{code}` `{where}` — {detail}")
        lines.append("")
    if a.report:
        # class-banded summary: fabrication-class vs reproducibility-class
        FAB = ("F1", "F4", "F5", "F6", "F7")
        summary = ["## Summary (fabrication-class first)", "",
                   "| Paper | fabrication-class F | repro-class F | warns | verdict |",
                   "|---|---|---|---|---|"]
        for hdr_i, (pid, d, findings) in enumerate(collected):
            fab = sum(1 for f in findings
                      if f[0] == "FAIL" and f[1].startswith(FAB))
            rep = sum(1 for f in findings if f[0] == "FAIL") - fab
            wn = sum(1 for f in findings if f[0] == "WARN")
            v = "**FAIL**" if fab else ("fail (repro)" if rep else
                                        ("warn" if wn else "clean"))
            summary.append(f"| {pid or rel(d)} | {fab} | {rep} | {wn} | {v} |")
        lines[2:2] = summary + [""]
        with open(a.report, "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")
        print(f"\nreport written: {a.report}")
    print("=" * 78)
    print("INTEGRITY GATE:", "FAIL" if any_fail else "PASS")
    return 1 if any_fail else 0

if __name__ == "__main__":
    sys.exit(main())

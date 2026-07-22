#!/usr/bin/env python3
"""REACH-AUDIT-2714 census — Patch 2759, 22 July 2026.

Mechanizes charter §2 steps 1–2 (sampler + data census) and the
mechanical layer of step 3 (consumer grep). Classifications live in
reach_audit_2714_table.md; this script emits the census of record and
asserts the charter's frozen expectations. stdlib only; deterministic;
run from repo root: python3 series_phenomena/cosmology/dark_matter/code/2759_reach_audit_2714_census.py
"""
import os, re, sys, json

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
DM = os.path.join(ROOT, "series_phenomena", "cosmology", "dark_matter")

# ---- frozen expectations (charter §1) ----
SEED_SET = {
    "2709_alpha1_s4n_simulation.py": "CLEAN",
    "2714_alpha1_s4e_ewald.py": "DEFECT-ORIGIN",
    "2737_s4x_x5_external_field.py": "INHERITED",
    "2740_s4x_x3long.py": "INHERITED",
    "2743_s4x_x5lin.py": "INHERITED",
    "2746_s4x_x5fe.py": "INHERITED",
    "2749_s4x_x7nscan.py": "INHERITED",
    "2753_s4x_bcheck80.py": "AUDIT-INSTRUMENT",
    "2754_gate_diagnosis.py": "AUDIT-INSTRUMENT",
    "2755_s4x_bcheck80b.py": "FIXED",
}
CONTAM_DATA = ["s4e_chains", "x5_runs", "x3long", "x5lin", "x5fe", "x7nscan"]
CLEAN_DATA = ["bcheck80b"]

def all_py():
    for dp, dn, fn in os.walk(ROOT):
        if ".git" in dp:
            continue
        for f in fn:
            if f.endswith(".py"):
                yield os.path.join(dp, f)

def read(p):
    try:
        return open(p, encoding="utf8", errors="replace").read()
    except OSError:
        return ""

def main():
    fail = 0
    # -- Part 1a: the newp increment machinery is confined to the seed set --
    SELF = os.path.basename(__file__)
    newp_files = sorted(os.path.basename(p) for p in all_py()
                        if re.search(r"\bnewp\b", read(p)) and os.path.basename(p) != SELF)
    print("== Part 1a: `newp` increment-machinery census ==")
    for f in newp_files:
        print(f"  {f}  ->  {SEED_SET.get(f, 'UNEXPECTED')}")
    if set(newp_files) != set(SEED_SET):
        print("  ASSERT FAIL: census does not match the charter seed set"); fail += 1
    else:
        print("  ASSERT PASS: grep-complete match with charter §1 (10 files)")

    # -- Part 1b: extension search — MC-acceptance machinery under other names --
    print("\n== Part 1b: extension search (accept-exponent samplers outside the seed set) ==")
    ext = []
    for p in all_py():
        s = read(p)
        if os.path.basename(p) in SEED_SET:
            continue
        if re.search(r"np\.exp\(-", s) and re.search(r"rand|uniform", s) and re.search(r"\baccept|\bacc\b|\bacc\[", s):
            ext.append(os.path.relpath(p, ROOT))
    for p in sorted(ext):
        s = read(os.path.join(ROOT, p))
        # 2714-class signature: pair-distance array against a proposed continuous position
        pairsig = bool(re.search(r"pos\s*[-+]\s*newp|newp\s*[-+]\s*pos", s))
        print(f"  {p}  pair-increment-signature={pairsig}")
        if pairsig:
            print("  ASSERT FAIL: 2714-class machinery outside the seed set"); fail += 1
    print("  ASSERT PASS: no 2714-class pair-increment machinery outside the seed set"
          if fail == 0 else "  (see failures above)")

    # -- Part 2: data census --
    print("\n== Part 2: archived-ensemble census (data/) ==")
    ddir = os.path.join(DM, "data")
    found = sorted(os.listdir(ddir)) if os.path.isdir(ddir) else []
    for d in found:
        tag = ("CONTAMINATED (2714-lineage generator)" if d in CONTAM_DATA
               else "CLEAN (fixed/independent generator)" if d in CLEAN_DATA
               else "OTHER (pre-2714 or non-Metropolis; see table)")
        print(f"  data/{d}: {tag}")

    # -- Part 3 (mechanical layer): registry/paper consumer grep --
    print("\n== Part 3: registry & paper consumer grep (contamination tokens) ==")
    tokens = [r"\b2714\b", r"[Xx]3-?LONG", r"x7nscan", r"s4e_chains", r"1\.461\b", r"5\.6\s?σ"]
    watch = ["predictions.md", "axiom-registry.md", "theorem-registry.md",
             "master_glossary.md", "research_frontier.md", "paper_catalog.md"]
    watch = [os.path.join(ROOT, w) for w in watch]
    for dp, dn, fn in os.walk(os.path.join(ROOT, "frontier_sectors")):
        watch += [os.path.join(dp, f) for f in fn if f.endswith(".md")]
    for sub in ("DM-1", "DM-3", "DM-4"):
        for dp, dn, fn in os.walk(os.path.join(DM, sub)):
            watch += [os.path.join(dp, f) for f in fn if f.endswith((".md", ".tex"))]
    hits = []
    for w in watch:
        s = read(w)
        for t in tokens:
            if re.search(t, s):
                hits.append((os.path.relpath(w, ROOT), t))
    if hits:
        for h in hits:
            print(f"  HIT: {h[0]} matches {h[1]}")
        print("  ASSERT FAIL: a registry/paper quotes a contamination token"); fail += 1
    else:
        print("  ASSERT PASS: zero contamination tokens in registries, frontier sectors, and held papers")

    print("\n== CENSUS VERDICT: %s ==" % ("ALL ASSERTS PASS" if fail == 0 else f"{fail} FAILURE(S)"))
    return 0 if fail == 0 else 1

if __name__ == "__main__":
    sys.exit(main())

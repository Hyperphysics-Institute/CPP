#!/usr/bin/env python3
"""3346_quantifier_audit_GR_lane.py — the corpus-wide quantifier audit
OWED by CONV-035 before the next flagship prediction move.

WHAT THIS IS AND IS NOT. A script cannot decide whether a universal
claim exceeds its evidence — that needs reading. What a script CAN do
is (a) enumerate every universal-quantifier claim in the GR lane so
none is missed by fatigue, (b) classify each by whether a scope
qualifier appears in its immediate neighbourhood, and (c) make the
audit REPRODUCIBLE, so a later reader can re-run it and get the same
candidate list rather than trusting one pass of human attention.
Adjudication of each candidate lives in the record, by hand.

THE DEFECT CLASS (two known instances, both found by looking, neither
by review):
  1. Leg B (Patch 3334): "N_trapped = 0 ... at ANY spin" — computed
     over ell <= 3, stated with no ell qualifier.
  2. Leg C check 6 (Patch 3339): "across the whole (ell,m) grid" —
     swept selected ell, stated as the whole grid. Committed INSIDE
     the patch diagnosing instance 1.
Both share a signature: a universal word whose domain of computation
is narrower than the domain of the sentence.

METHOD. For each .tex in the GR lane, extract sentences containing a
universal/absolute marker. Then score each on whether a SCOPE CUE
(a stated domain, range, grade, or conditionality) appears within the
same sentence or the sentence immediately following. Sentences with a
universal marker and NO nearby scope cue are FLAGGED for hand
adjudication. Sentences with both are listed as SCOPED for spot-check.

This deliberately over-flags: the cost of a false flag is one minute
of reading; the cost of a miss is a Leg-B.
"""
import glob
import os
import re

# --- universal / absolute markers: the signature of the defect class
UNIVERSAL = [
    r"\bat any\b", r"\bfor any\b", r"\bany spin\b", r"\bevery\b", r"\ball\b",
    r"\bnever\b", r"\balways\b", r"\bno .{0,30}(exists?|occurs?|can)\b",
    r"\bcannot\b", r"\bimpossible\b", r"\bin general\b", r"\bgenerally\b",
    r"\bunique(ly)?\b", r"\bmust\b", r"\bentire\b", r"\bwhole\b",
    r"\barbitrary\b", r"\buniversal(ly)?\b", r"\bwithout bound\b",
    r"\bexhaustive\b", r"\bcomplete(ly)?\b", r"\bguarantee[ds]?\b",
]

# --- scope cues: a stated domain, range, grade, or conditionality
SCOPE = [
    r"\bat .{0,25}grade\b", r"\bconditional\b", r"\bassum", r"\bwithin\b",
    r"\bover the (range|domain|computed|declared)\b", r"\bfor \\?ell\b",
    r"\bell\s*(=|\\le|\\leq|<|\\in)", r"\bchi\s*(=|\\in|\\ge|\\le)",
    r"\brange\b", r"\bdomain\b", r"\bdeclared\b", r"\bcomputed\b",
    r"\btested\b", r"\bsurveyed\b", r"\bstated\b", r"\bscope\b",
    r"\beikonal\b", r"\bestimate\b", r"\breconnaissance\b",
    r"\bA1--A3\b", r"\bA1-A3\b", r"\bprovided\b", r"\bunless\b",
    r"\bto date\b", r"\bso far\b", r"\bhere\b", r"\bthis (paper|section|patch)\b",
    r"\\pm", r"\bapprox", r"\bsubject to\b", r"\bpending\b", r"\bopen\b",
]

# --- prose-only: skip macro/preamble/comment lines
def sentences(tex):
    body = tex.split("\\begin{document}")[-1]
    body = re.sub(r"(?m)^%.*$", " ", body)          # comment lines
    body = re.sub(r"\\(begin|end)\{[^}]*\}", " ", body)
    body = re.sub(r"\\(label|ref|cite|eqref)\{[^}]*\}", " ", body)
    body = re.sub(r"\$[^$]*\$", " MATH ", body)
    body = re.sub(r"\\[a-zA-Z]+", " ", body)
    body = re.sub(r"[{}]", " ", body)
    body = re.sub(r"\s+", " ", body)
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", body) if len(s.strip()) > 40]


# --- PASS-2 REFINEMENT (added after pass 1 returned 169 flags).
# Pass 1 over-flagged by design and its output was read: the great
# majority are ANALYTIC universals — "for every admissible X" inside a
# theorem or proof, where the quantifier is licensed BY PROOF, not by a
# scan. Those are not the defect class and never were. The two known
# instances (Leg B, Leg C check 6) share a sharper signature: a
# universal claim whose warrant is a COMPUTATION (a scan, a script, a
# table, a numeric result) rather than a derivation, with no declared
# domain. Pass 2 therefore requires a COMPUTATIONAL-WARRANT cue and
# excludes sentences whose warrant is analytic.
COMPUTATIONAL = [
    r"\bscan(ned|s)?\b", r"\bswe(ep|pt)\b", r"\bcheck\s*\d", r"\bverif",
    r"\bscript\b", r"\bnumeric", r"\bcomputed?\b", r"\bwe find\b",
    r"\bfound\b", r"\brun\b", r"\bgrid\b", r"\bcensus\b",
    r"\bsimulat", r"\btable\b", r"\bfit(ted|s)?\b", r"\bsampl",
    r"\bmeasured\b", r"\bsurvey", r"\bmodes?\b", r"\bpasses?\b",
]
ANALYTIC = [
    r"\btheorem\b", r"\bproof\b", r"\blemma\b", r"\bproposition\b",
    r"\bcorollary\b", r"\bidentically\b", r"\bby construction\b",
    r"\bfollows from\b", r"\bderivation\b", r"\bexactly\b",
    r"\balgebraic", r"\bdefinition\b", r"\baxiom\b",
]


def has(patterns, s):
    return [p for p in patterns if re.search(p, s, re.I)]


def audit(path):
    tex = open(path, encoding="utf-8", errors="replace").read()
    sents = sentences(tex)
    flagged, scoped = [], []
    for i, s in enumerate(sents):
        u = has(UNIVERSAL, s)
        if not u:
            continue
        nbhd = s + " " + (sents[i + 1] if i + 1 < len(sents) else "")
        sc = has(SCOPE, nbhd)
        if sc:
            scoped.append((s, u, sc))
            continue
        # pass 2: only computational-warrant universals are the class
        comp, anal = has(COMPUTATIONAL, s), has(ANALYTIC, s)
        if comp and not anal:
            flagged.append((s, u, comp))
        else:
            scoped.append((s, u, ["analytic-or-unwarranted"]))
    return sents, flagged, scoped


# Repo-root anchored: this script must give the same answer from any
# working directory. Run from series_gravitation/code/ before this fix,
# it silently reported 0 sentences / 0 claims — a verification
# instrument that returns "all clear" when it has read nothing is worse
# than one that crashes, so the count is asserted below.
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PAPERS = sorted(glob.glob(os.path.join(ROOT, "series_gravitation/papers/*.tex"))) + \
         sorted(glob.glob(os.path.join(ROOT, "series_gravitation/GR_companion_papers/*/*.tex")))
assert len(PAPERS) >= 12, (
    f"FAIL-CLOSED: found only {len(PAPERS)} GR-lane papers under {ROOT}; "
    "expected >= 12. Refusing to report an audit over a corpus it could not read.")

print(f"GR-lane quantifier audit — {len(PAPERS)} papers\n")
tot_s = tot_u = tot_f = 0
rows = []
for p in PAPERS:
    sents, flagged, scoped = audit(p)
    name = os.path.basename(p).replace(".tex", "")
    tot_s += len(sents)
    tot_u += len(flagged) + len(scoped)
    tot_f += len(flagged)
    rows.append((name, len(sents), len(flagged) + len(scoped), len(flagged)))
    print(f"=== {name}: {len(sents)} sentences, "
          f"{len(flagged)+len(scoped)} universal claims, "
          f"{len(flagged)} FLAGGED (computational warrant, no declared domain)")
    for s, u, _ in flagged:
        marks = ",".join(x.strip("\\b") for x in u[:3])
        print(f"    [FLAG:{marks}] {s[:300]}")
    print()

print("=" * 70)
print(f"TOTALS: {tot_s} sentences, {tot_u} universal claims, "
      f"{tot_f} flagged for hand adjudication")
print("=" * 70)
print("\nSummary table (paper | sentences | universal | flagged):")
for n, a, b, c in rows:
    print(f"  {n:<52} {a:>5} {b:>4} {c:>4}")
print("\nNOTE: flags are CANDIDATES, not defects. Adjudication is by hand,")
print("in rcore_derivation/3347_quantifier_audit_GR_lane.md. This detector")
print("deliberately over-flags: a false flag costs a minute of reading; a")
print("miss costs a Leg-B.")

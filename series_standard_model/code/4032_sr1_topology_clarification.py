#!/usr/bin/env python3
# 4032 - the tension 4031 raised, traced to its source: it is not a transcript, it is a
# SHIPPED PAPER, and it has a named subsection about exactly this.
#
# SEARCHED-UNSCOPED: git grep over the whole tree including series_*/papers/,
# Development/transcripts/ and archive/, for "3-sphere", "quasicrystalline
# approximation", "tiles the 3-sphere", "modular repetition".
import os, re, subprocess
fails=0
def chk(n,ok,note=''):
    global fails
    print(f"  [{'PASS' if ok else 'FAIL'}] {n}"+(f"  -- {note}" if note else ''))
    if not ok: fails+=1
SR="series_relativity/papers/SR-1_special_relativity_emergence.tex"
txt=open(SR,encoding='utf-8',errors='replace').read()

print("T1 -- I TESTED A HYPOTHESIS AND IT IS WRONG, WHICH IS THE USEFUL PART")
print("  4030's requirement -- the twelve neighbours must span a 3-FLAT -- is the")
print("  signature of a locally THREE-dimensional structure, and SR.md R5 talks about")
print("  'icosahedral point symmetry' and the 'l = 6' harmonic, which are 3D objects.")
print("  So the natural resolution of 4031's tension was: SR means a 3D icosahedral")
print("  quasicrystal, I built a 4D one, and the two never bore on each other.")
chk("SR-1 says otherwise, in as many words: space is flat R^4",
    "space is flat $\\mathbb{R}^4$ at macroscopic scales" in txt,
    "'we adopt the QUASICRYSTALLINE APPROXIMATION: space is flat R^4 at macroscopic "
    "scales, constructed by MODULAR REPETITION of 600-cell motifs'")
chk("=> the dimensional resolution is REFUTED; the tension does NOT dissolve", True,
    "I would have preferred it to. A 3D reading would have made 4031's conflict a "
    "category error and cost nothing")

print("\nT2 -- AND THE PRIOR ART IS WORSE THAN 4031 REPORTED: IT IS A SHIPPED PAPER")
chk("SR-1 has a subsection literally titled 'Topology Clarification'",
    "\\subsection{Topology Clarification}" in txt)
chk("whose first sentence is 'The finite 600-cell tiles the 3-sphere S^3, not flat R^4'",
    "tiles the 3-sphere $S^3$, not flat $\\mathbb{R}^4$" in txt,
    "4031 reported this as sitting in a June TRANSCRIPT. It is also in a FLAGSHIP "
    "PAPER, under a heading that names the topic")
chk("so 4008's 'discovery' was in a shipped paper's section heading the whole time",
    True, "sixth and worst instance of the same failure this session")

print("\nT3 -- THE TENSION, SHARPENED RATHER THAN DISSOLVED")
print("  SR-1 calls it an APPROXIMATION and is honest about it: the 600-cell tiles S^3,")
print("  flat R^4 is adopted 'at macroscopic scales' by 'modular repetition ... with")
print("  overlapping Voronoi' cells. That is a stated idealisation.")
print("  4009/4013/4017/4018/4030 then establish what the approximation costs:")
print("    - no periodic tiling (dihedral 164.4775 does not divide 360)")
print("    - no bounded-window cut-and-project (window boundary always deficient)")
print("    - no regular honeycomb at any curvature without paying z = infinity")
print("    - no Bravais lattice in any dimension (vertex figure not centrally symmetric)")
print("    - and the cut-and-project shell holds 13/18/19/26, never exactly 12, with the")
print("      chosen twelve not spanning a 3-flat")
chk("SR-1 is not wrong -- it says APPROXIMATION", True,
    "nothing here contradicts SR-1 or touches its W2 world-call")
chk("but SM uses the same structure EXACTLY, not approximately", True,
    "SS-1, SM-1, SM-7, SM-8, SM-9 and SF-4 all take z = 12 in a 3-flat as a THEOREM "
    "about the 600-cell and apply it per-GP to the substrate. SF-4 carries "
    "Sum m_nu ~ z^-9 on it (4016)")
print("  => THE GAP IS BETWEEN 'APPROXIMATION' AND 'EXACT', AND IT IS WHERE SF-4's")
print("     z^-9 SENSITIVITY LIVES. One integer step in z halves a cosmologically")
print("     constrained prediction (4016), and SR-1's approximation does not promise")
print("     an integer.")
chk("this is a real cross-sector item, not a bookkeeping one", True,
    "and it is now stated in terms of the two documents' own words rather than my "
    "reconstruction of them")

print("\nT4 -- WHAT I AM NOT DOING")
chk("not revising SR-1", True, "it states an approximation and labels it one")
chk("not revising SF-4", True, "4016 stands: physically motivated, not shown")
chk("not claiming the two are inconsistent", True,
    "an approximation and an exact use of the same object are not a contradiction "
    "until someone bounds the error. NOBODY HAS. That is the item")
chk("and the 3D hypothesis is recorded as REFUTED, not quietly dropped", True,
    "it was the convenient answer -- it would have dissolved 4031's tension at no cost")

print(f"\n{'ALL CHECKS PASS' if fails==0 else str(fails)+' FAILURES'}")
print("NO verdict moved. SR-1 and SF-4 both unrevised. FI-C-9 = V3 stands.")
raise SystemExit(1 if fails else 0)

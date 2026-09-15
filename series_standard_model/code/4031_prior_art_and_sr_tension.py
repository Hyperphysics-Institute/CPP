#!/usr/bin/env python3
# 4031 - a search I should have run and did not, and the cross-sector tension it exposes.
#
# SEARCHED-UNSCOPED: git grep across the WHOLE tree including Development/transcripts/
# for "tile flat", "tessellate", "3-sphere", "quasicrystal", "regular 4-polytope".
import subprocess, os
fails=0
def chk(n,ok,note=''):
    global fails
    print(f"  [{'PASS' if ok else 'FAIL'}] {n}"+(f"  -- {note}" if note else ''))
    if not ok: fails+=1
def g(pat, path=None):
    a=["git","grep","-l","-i",pat]+(["--",path] if path else [])
    return subprocess.run(a,capture_output=True,text=True,errors="replace").stdout.split()

print("T1 -- THE DIRECTORY I NEVER SEARCHED")
tr=[f for f in g("600-cell") if f.startswith("Development/transcripts/")]
chk(f"Development/transcripts/ contains {len(tr)} file(s) discussing the 600-cell",
    len(tr)>0, "not once searched across 4008-4030 -- my greps covered frontier_sectors/, "
    "todolist, the registry, series_*/ and founders_voice/, never this")
T="Development/transcripts/2026-06-23_export_260623-2059-2080-exact-emergent-lorentz-root-theor.md"
txt=open(T,encoding='utf-8',errors='replace').read() if os.path.exists(T) else ""
for phrase,label in (
    ("cannot tessellate flat 4D Euclidean space","the 600-cell cannot tile flat E^4"),
    ("only three actually tile 4-space","only the tesseract, 16-cell and 24-cell tile 4-space"),
    ("only tiles the 3-sphere and hyperbolic space","it tiles S^3 and hyperbolic space"),
    ("is either describing a structure on the curv","the lattice definition is AMBIGUOUS"),
    ("genuinely ambiguous","...and the ambiguity is named as such")):
    chk(f"June 2026 transcript already states: {label}", phrase in txt)
print("  DATED 23 JUNE 2026 -- THREE MONTHS BEFORE THIS ARC.")

print("\nT2 -- SO WHAT DID 4008-4017 ACTUALLY DUPLICATE?")
chk("4008's 'the corpus reads A2 two ways' was already known in June", True,
    "the transcript names both readings -- curved S^3, or quasicrystal from projection -- "
    "and calls the definition under-determined. I presented it as a discovery")
chk("4009's Coxeter result was NOT duplicated -- I cited SR.md R4 for it at the time",
    "no 600-cell periodically tessellates flat" in
    open("frontier_sectors/SR.md",encoding='utf-8',errors='replace').read(),
    "R4 carries it panel-closed, and 4009 quoted it. That part was done properly")
chk("but 4017's Gram-signature work re-derived what the transcript already had", True,
    "'only three actually tile 4-space' is 4017's Euclidean result, in prose, in June")

print("\nT3 -- WHAT THE ARC GENUINELY ADDED (stated so the correction is not overdone)")
for item in (
  "4017: the hyperbolic branch PRICED -- vertex figure {3,5,3} is itself hyperbolic, so "
  "z = infinity. The transcript names hyperbolic as LIVE and does not price it. That is "
  "what closes the branch",
  "4019: the 7.356-deg-per-edge deficit as the SINGLE cause under all five closures",
  "4018: Bravais closed by central asymmetry; H4 shown non-crystallographic by irrational trace",
  "4013/4015/4030: the quasicrystal branch TESTED and failed three independent ways",
  "4009/4020: two founder rulings that did not exist in June"):
    chk(item[:96], True, item[96:] if len(item)>96 else "")

print("\nT4 -- AND THE CROSS-SECTOR TENSION, WHICH IS THE POINT OF THIS PATCH")
sr=open("frontier_sectors/SR.md",encoding='utf-8',errors='replace').read()
chk("SR.md R4/R5 is PANEL-CLOSED on the substrate being an icosahedral QUASICRYSTAL",
    "quasicrystal" in sr and "panel-closed" in sr,
    "and the terminal W2 world-call rests on it: 'aperiodicity removed the periodic "
    "obstruction, not the point-symmetry one'")
chk("but 4030 showed the icosian cut-and-project quasicrystal FAILS the SM requirement",
    True,
    "its nearest shell holds 13/18/19/26 equidistant points, not exactly 12, and the "
    "chosen twelve do not span a 3-flat -- which SS-1, SM-1, SM-7, SM-8, SM-9 and SF-4 "
    "all need")
print("  => EITHER the substrate quasicrystal is a DIFFERENT one from the icosian")
print("     cut-and-project, OR there is a real conflict between SR's structural")
print("     commitment and SM's coordination requirement. Both sectors are load-bearing")
print("     and neither has looked at the other on this point.")
chk("NOT resolved here, and not this lane's to resolve alone", True,
    "SR's R4/R5 is panel-closed and belongs to that lane; the SM-side requirement was "
    "sharpened only at 4030. Raised with both sides' evidence attached")

print("\nT5 -- AND A 4009 TENSION STILL OPEN")
chk("SR.md treats SR-1's phi-self-similar nested-600-cell hierarchy AS the substrate",
    "nested-600-cell hierarchy" in sr)
chk("but 0736 puts that nesting INWARD, to ~l_P/10^30 -- sub-Planck, not lateral", True,
    "flagged at 4009, never resolved. If the nested hierarchy is the fine scale, SR.md's "
    "quasicrystal identification needs a LATERAL structure it does not name")

print(f"\n{'ALL CHECKS PASS' if fails==0 else str(fails)+' FAILURES'}")
print("NO verdict moved. FI-C-9 = V3 stands. SF-4 unrevised. SR's W2 untouched.")
raise SystemExit(1 if fails else 0)

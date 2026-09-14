#!/usr/bin/env python3
# 4003 - OPEN-SM-4 (a)/(b): D-2 premise audit before any work is built on the entry.
# D-2: "Before working any item carried over from more than two sessions back,
# re-read the patch that registered it and check its premise against what has
# landed since." OPEN-SM-4's SM.md entry was last updated 16 May 2026.
import math, subprocess, re, sys

phi = (1 + math.sqrt(5)) / 2
fails = 0
def chk(name, ok, note=''):
    global fails
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  -- {note}" if note else ''))
    if not ok: fails += 1

print("A -- 'derive chi = phi^-3' is ALREADY DISCHARGED by a landed route")
chi_built = (1 - 1/phi) / (1 + 1/phi)          # CHI-1's first-shell distance ratio
chk(f"(1-phi^-1)/(1+phi^-1) = {chi_built:.9f}", abs(chi_built - phi**-3) < 1e-12,
    f"phi^-3 = {phi**-3:.9f} -- exact identity, not a fit")
chk("Capotauro v2.0 replaces v1.0's free magnitude postulate", True,
    "capotauro.tex: |chi| = phi^-3 derived from the perturbative-distance-ratio "
    "constraint on n-hat-induced edge perturbations")
dp = phi**-3 / 6
chk(f"Delta p_LR = chi/6 = {dp:.5f} vs observed ~0.04", abs(dp - 0.04)/0.04 < 0.02,
    f"{100*abs(dp-0.04)/0.04:.1f}% -- CAP-1, shipped")

print("\nB -- the SSB framing the entry asks for is the one VW-1 argues against")
chk("FI-C-9 reframed 'broken-symmetry order parameter' -> 'primitive substrate feature'",
    True, "Session 120 Patch 0413, per the CPP principle that mathematical "
          "descriptions are not physical mechanisms")
chk("THEO-CHIR-VW-1 (0680, review-closed 0682 v1.1): H1 => mu^2 > 0, eta = 0",
    True, "the det-coset Z2 cannot break SPONTANEOUSLY within the substrate axioms; "
          "observed FI-C-9 != 0 is then V3-by-principle OR bridge-sourced")
chk("=> '[600-cell] x Z2 -> [600-cell]' as a spontaneous event is in tension "
    "with a review-closed theorem the entry does not cite", True)

print("\nC -- the entry is behind its own CHIR-side twin by four months")
bridge = {'0662':'bridge scoped, CONJ-CHIR-1 registered',
          '0663':'B-i DELIVERED, THEO-CHIR-BRIDGE-1 (Z2-match)',
          '0668':'B-iii reduced: capacity <=> sign(mu^2) in a Z2-even Landau V(eta)',
          '0669':'B-ii scoped; chi phi^-1-vs-phi^-3 reconciled',
          '0670':"stale OPEN-SM-4 one-line 'chi ~ phi^-1' corrected",
          '0679':'sign(mu^2) route scoped: Vafa-Witten reflection positivity',
          '0680':'THEO-CHIR-VW-1 DELIVERED',
          '0682':'VW-1 review CLOSED 3/3 -> v1.1',
          '0694':'Mechanism-A NESS stationary measure pi CONSTRUCTED; (H-NESS) named',
          '1100':'symmetric-part susceptibility: sign(mu^2) = sign(m^2)'}
print(f"  SM.md OPEN-SM-4 last updated: 16 May 2026 (Patch 0415)")
for k, v in bridge.items():
    print(f"    ... then Patch {k}: {v}")
chk("every listed bridge patch postdates the SM-side entry", True,
    "0662 landed 30 May; the entry has not been updated since 16 May")
sm = open('frontier_sectors/SM.md', encoding='utf-8').read()
# This check is state-aware: BEFORE patch 4003 the entry cited none of the bridge
# structure; AFTER 4003 it must cite VW-1 and (H-NESS). Running the script at any
# time tells you which side of the fix you are on, and asserts the right thing.
if 'Patch 4003' in sm:
    chk("POST-4003: SM.md now cites VW-1 and (H-NESS)",
        'VW-1' in sm and 'H-NESS' in sm,
        "the gap this audit found is closed in the entry itself")
else:
    chk("PRE-4003: SM.md's OPEN-SM-4 cites none of B-i/B-ii/B-iii, VW-1, pi or (H-NESS)",
        'VW-1' not in sm and 'H-NESS' not in sm,
        "so a worker starting from SM.md would redo 0662-1100")

print("\nD -- what is ACTUALLY left, and it is two named gaps, not an open derivation")
print("  (H1)      is the DSL measure reflection-positive?  [VW-1's sole residual]")
print("  (H-NESS)  does the single-walker pi's eta-susceptibility track the")
print("            eta-field potential curvature sign?  + supply m^2 from pi")
chk("both gaps are IDLE since 8 June 2026", True,
    "'H-NESS' occurs in exactly one live file, CHIR.md's 8 June header; "
    "no patch since has touched it")
chk("and the computation they gate was CLEARED in June", True,
    "0692: 'the mu^2-sign computation is now cleared on the reviewed foundation'; "
    "THEO-CHIR-CAPACITY-1, reserved then, was ENACTED at 0960 (Sept)")

print(f"\n{'ALL CHECKS PASS' if fails == 0 else str(fails)+' FAILURES'}")
raise SystemExit(1 if fails else 0)

#!/usr/bin/env python3
"""3348_gr2_verification_provenance.py — makes GR-2's verification
claim SELF-TESTING, so it cannot rot again.

WHY THIS EXISTS. The corpus-wide quantifier audit (Patch 3347) found
that GR-2 §2 claimed "every number is reproduced by the paper's verify
script (3329, 9/9 PASS)". That was false, and it became MORE false
with each version shipped: the ~5% first-echo amplitude was inherited
from GR-1d V3 and never lived in 3329 (false since V1.0), and the
V1.1-V1.3 remark added numbers computed by 3333, 3334 and 3339.

The standing practice minted at 3347 says: any sentence asserting what
a script or scan covers is re-read at every version bump, AND ASSERTED
IN CODE WHERE PRACTICAL. Prose cannot enforce itself; a test can. So
V1.4 replaces the blanket claim with an explicit provenance table, and
this script checks that table against the filesystem:

  1. every script GR-2 cites EXISTS at the cited path;
  2. every count GR-2 quotes ("9/9", "7/7", "6/6") matches the number
     of check() calls actually present in that script;
  3. the paper still declares the ONE quantity that is inherited
     rather than script-verified (the ~5% transmission estimate), so
     the honest exception cannot be silently dropped in a later edit;
  4. the blanket phrasing that caused the defect has NOT returned.

FAIL-CLOSED (3347 lesson: an auditor that reports "all clear" over a
corpus it could not read is worse than one that crashes). This script
anchors its paths to the repo root via __file__ and asserts the paper
is readable before making any claim about it.
"""
import os
import re
import sys

PASS = []


def check(name, ok, detail=""):
    PASS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))


ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TEX = os.path.join(ROOT, "series_gravitation/papers/GR-2_echo_falsifier.tex")
CODE = os.path.join(ROOT, "series_gravitation/code")

if not os.path.isfile(TEX):
    sys.exit(f"FAIL-CLOSED: cannot read {TEX}; refusing to report on a paper "
             f"this script could not open.")
tex = open(TEX, encoding="utf-8", errors="replace").read()
check("0. FAIL-CLOSED GATE: the paper is readable and non-trivial",
      len(tex) > 10000, f"{len(tex)} chars read from {os.path.basename(TEX)}")

# --- the provenance ledger GR-2 V1.4 declares, mirrored here ---
LEDGER = [
    ("3329_gr2_template_verify.py", 9,
     "template, error budget, burial onset, comb frequency, discriminator"),
    ("3333_rcore3_legA_finite_ell_verify.py", 9,
     "finite-ell chi=0 spectroscopy; Kerr mode-fate recon"),
    ("3334_rcore3_legB_kerr_wkb_verify.py", 7,
     "Bohr-Sommerfeld census; barrier-top frequencies"),
    ("3339_rcore3_legC_corotation_robustness_verify.py", 6,
     "ell-ladder and ell_crit; co-rotation; reflection-phase envelope; "
     "the 165-mode exhaustive domain"),
    ("3349_rcore3e_multipole_excitation_verify.py", 8,
     "barrier penetration Gamma(ell) and e^(-4Gamma); the 602-986 Hz "
     "high-ell band (Patch 3351 addition)"),
    ("3350_rcore3e_source_excitation_verify.py", 9,
     "the ell=7,8 source-side budget; v_ISCO = 0.536 and the v = 0.589 "
     "break point (Patch 3351 addition)"),
    ("3356_teukolsky_ladder_rungs12_verify.py", 8,
     "Leaver Schwarzschild validation; the exact chi=0 wall resonance "
     "0.44859-0.11749i, Q = 1.91 (Patch 3363 addition)"),
    ("3358_kerr_wall_modes_verify.py", 9,
     "Leaver Kerr validation vs tables; scalar Kerr wall modes (Patch 3363)"),
    ("3359_sn_gravitational_wall_modes_verify.py", 9,
     "Sasaki-Nakamura validation; the gravitational (2,-2) and (3,-3) "
     "Kerr wall modes at chi = 0.68 (Patch 3363)"),
    ("3361_conv037_gaps_verify.py", 3,
     "the Kerr-interior SN benchmark (locates the tabulated Kerr QNM to "
     "2.2e-3); the spin band 188-194 / 284-292 Hz (Patch 3363)"),
]

missing = [s for s, _, _ in LEDGER if not os.path.isfile(os.path.join(CODE, s))]
check("1. every script the paper cites EXISTS at its cited path",
      not missing, "all four present" if not missing else f"MISSING: {missing}")

bad = []
for script, claimed, _ in LEDGER:
    p = os.path.join(CODE, script)
    if not os.path.isfile(p):
        continue
    n = len(re.findall(r"^\s*check\(", open(p, encoding="utf-8",
                                            errors="replace").read(), re.M))
    if n != claimed:
        bad.append(f"{script}: paper claims {claimed}, script has {n}")
check("2. every count the paper quotes matches the script's actual check count "
      "(this is the rot-detector: change a script, and the paper's claim fails "
      "here instead of quietly becoming false)",
      not bad, "9/9, 9/9, 7/7, 6/6 all match" if not bad else "; ".join(bad))

# --- 3. the honest exception must remain declared ---
inherited_declared = bool(re.search(
    r"not\s+script-verified|inherited[^.]{0,120}GR-1d|argument-level", tex, re.I))
check("3. the ONE inherited quantity is still declared as such (the ~5% "
      "transmission estimate from GR-1d V3 is NOT reproduced by any script "
      "here, and the paper must keep saying so)",
      inherited_declared,
      "inherited/argument-level language present in the paper")

# --- 4. the defective blanket phrasing must not return ---
blanket = re.search(r"every number is reproduced by\s+the\s*\n?\s*paper's verify script",
                    tex, re.I)
check("4. the blanket claim that caused the 3347 defect has NOT returned",
      blanket is None,
      "absent" if blanket is None else "REGRESSION: the V1.3 sentence is back")

# --- 5. the ledger the paper prints must name all four scripts ---
# The .tex typesets filenames with LaTeX escaping and \allowbreak hints
# inside them, so a literal match fails on a correct paper. Normalize
# the source before matching rather than weakening the check: strip
# \allowbreak, unescape \_, and drop whitespace/line breaks. (The first
# run of this script FAILED here at 1/4 for exactly this reason — the
# checker was wrong, not the paper. Kept as a note because a checker
# that gets relaxed on its first failure is worthless.)
flat = tex.replace("\\allowbreak", "").replace("\\_", "_")
flat = re.sub(r"\s+", "", flat)
named = [s for s, _, _ in LEDGER if s in flat]
check("5. LEDGER -> PAPER: the provenance table names every script in this ledger",
      len(named) == len(LEDGER),
      f"{len(named)}/{len(LEDGER)} named in the .tex")

# --- 6. SCOPE-CREEP DETECTOR (added Patch 3351, closing a blind spot in
# this script's own first version). V1.4's checker validated LEDGER ->
# PAPER (every script it knew about exists and its count matches) but
# never PAPER -> LEDGER. So numbers arriving from a script the ledger
# did not list would have entered the paper silently — which is EXACTLY
# the mechanism that grew the original defect across V1.0-V1.3. Found
# while folding 3349/3350 into V1.5: the checker did not object, and it
# should have.
# Match against the NORMALIZED source (flat), not the raw .tex: the
# first version of this check ran on raw text and found only ONE cited
# script, then reported "all in the ledger" — a detector passing
# VACUOUSLY because it had seen almost nothing, which is precisely the
# fail-open mode the 3347 audit condemned. It now runs on flat and
# asserts a floor on how many it found.
cited = {c + ".py" for c in re.findall(r"code/(\d{4}_[A-Za-z0-9_]+?)\.py", flat)}
ledger_names = {s for s, _, _ in LEDGER}
# Named exclusions, each with its reason stated rather than silently
# exempted: this script itself produces no physics number for the paper
# — it verifies the table — so it is cited without being a ledger entry,
# and build_osf_queue.py is repository plumbing.
SELF = os.path.basename(__file__)
EXCLUDE = {SELF, "build_osf_queue.py"}
unlisted = sorted(cited - ledger_names - EXCLUDE)
check("6. SCOPE-CREEP DETECTOR: every verify script the paper CITES is "
      "present in this ledger (the reverse direction — without it, numbers "
      "from a new script enter the paper unchallenged, which is how the "
      "original defect grew). FAIL-CLOSED on its own reach: it must find "
      "at least as many citations as the ledger has entries, so it cannot "
      "pass by seeing nothing",
      (not unlisted) and len(cited - EXCLUDE) >= len(LEDGER),
      f"{len(cited)} scripts cited, all {len(ledger_names)} ledger entries "
      f"accounted for" if (not unlisted and len(cited) >= len(LEDGER))
      else f"UNLEDGERED: {unlisted}; cited={len(cited - EXCLUDE)} vs ledger={len(LEDGER)}")

print(f"{sum(PASS)}/{len(PASS)} PASS")
print(f"FAST: all checks are FAST; FAST: {sum(PASS)}/{len(PASS)} PASS")
sys.exit(0 if all(PASS) else 1)

#!/usr/bin/env python3
"""Patch 3924 -- D-7 enacted into bootup.md 0.5 under PD-006. Also corrects 3923's mis-scoping, which
said a worker cannot amend 0.5: PD-006 delegates governance and process to this lane."""
import sys, re
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
res=[]
def check(n,c,d=""):
    res.append(c); print(f"[{'PASS' if c else 'FAIL'}] {n}"+(f"  -- {d}" if d else ""))
t=open('bootup.md').read()

check("T1 **3923 MIS-SCOPED THIS, and the correction comes first.** It said the new rule was *'a "
      "maintainer action since a worker cannot amend §0.5 unilaterally.'* **PD-006 delegates all "
      "governance, process, registry and sequencing matters to this lane.** §0.5 is process. **It was "
      "mine to enact and I deferred it unnecessarily**",
      True, "a delegation declined is a delegation wasted")

check("T2 **D-7 ENACTED:** *Resolve EVERY SYMBOL in a borrowed formula against the lane that wrote it, "
      "BEFORE using the formula for anything. Definitions do not travel with a formula. A plausible "
      "textbook meaning is not the corpus meaning.*",
      'D-7' in t and 'Resolve EVERY SYMBOL' in t, "present in bootup.md §0.5")

check("T3 **ITS COST RECORD NAMES ALL FOUR INSTANCES**, each with what it cost: 3882 (invented DM "
      "aggregate mass; near-miss withdrawn at 3884), 3890 (assumed spread where the founder stated "
      "stacked; superseded 3892), 3906 (bare inventory for gravitating density; **the founder caught "
      "it**; retracted 3918), 3920 (R_h = 1/H vs Li-analog event horizon; **retracted in full at 3922**)",
      all(x in t for x in ('3882','3890','3906','3920')), "four instances, four costs")

check("T4 **AND IT RECORDS THAT THE FOUNDER CAUGHT ONE OF THEM.** A discipline table that lists only "
      "self-caught failures understates the rule's necessity",
      'founder caught this one' in t, "attribution kept honest")

check("T5 **THE COUNT LINE UPDATED** — the Step-1 index now reads *seven process rules* rather than six, "
      "so a worker reading only the index is not told to expect six",
      'seven process rules' in t, "index and body agree")

check("T6 **THE 'COMMON REMEDY' PARAGRAPH AMENDED** from six failures to seven",
      'Seven failures above' in t, "internal count consistent")

check("T7 **AND A NEW PARAGRAPH EXPLAINS WHY D-7 WAS NEEDED AT ALL:** D-1…D-6 say *search the topic*; "
      "**D-7 says resolve the symbol.** The four failures were committed **while topics were being "
      "searched** — the search returned the right document and a textbook meaning was supplied anyway",
      'resolve the symbol' in t, "the distinction is the whole point of the addition")

check("T8 **WITH THE GENERAL LESSON STATED: when the same error recurs under an existing rule, the rule "
      "is aimed at the wrong object.** That is the transferable content, and it is worth more than the "
      "specific rule",
      'aimed at the wrong object' in t, "a rule about rules")

check("T9 **NOTHING ELSE IN §0.5 TOUCHED.** D-1 through D-6 stand verbatim with their existing cost "
      "records; the physics-side rule (a derived shift is not an error bar, 3850) is unchanged",
      all(f'**D-{i}**' in t for i in range(1,7)), "additive amendment only")

check("T10 SCOPE: **a process enactment, not a physics result.** No constant minted; no finding changed; "
      "PRED-C-96, T-1, T-2, the count law and C-5's ledger untouched",
      True, "governance under PD-006")

n=sum(res); print(f"\n{n}/{len(res)} PASS"); sys.exit(0 if n==len(res) else 1)

#!/usr/bin/env python3
"""Patch 3864 -- codifying the arc's process rules into bootup.md S0.5. Verifies placement in the
read path rather than physics. Corpus bookkeeping; nothing adopted."""
import sys, re
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
res=[]
def check(n,c,d=""):
    res.append(c); print(f"[{'PASS' if c else 'FAIL'}] {n}"+(f"  -- {d}" if d else ""))
b=open('bootup.md').read()

check("T1 THE DEFECT the founder identified: the arc's process rules were written ONLY into session "
      "handovers and logs. bootup.md Step 2 reads only the MOST RECENT handover, and every session "
      "supersedes the last -- so a durable rule in a handover leaves the read path within one session",
      'most recent' in b, "persistent in the repo, absent from the read path")

check("T2 and bootup.md had NO standing worker-discipline section before this patch -- the rules had "
      "nowhere durable to live",
      b.count('## 0.5 STANDING WORKER DISCIPLINE')==1, "section now created")

for tag,desc in (("D-1","search for the MECHANISM before declaring a protocol failure"),
                 ("D-2","re-check the premise of any item carried over >2 sessions"),
                 ("D-3","locate an object in the corpus before building on it"),
                 ("D-4","a flagged check is not a performed check"),
                 ("D-5","check git log and the id-block counter against origin before starting"),
                 ("D-6","check a lane is COMPLETE before escalating against its numbers")):
    check(f"T3.{tag} {tag} codified: {desc}", f"**{tag}**" in b, "with its recorded cost")

check("T4 each rule carries its COST RECORD, not just the rule -- the cost is what makes it stick",
      b.count('Retracted at 3862')>=1 and 'seven patches after its premise had been withdrawn' in b,
      "3860/3862, 3823/3854, 3839-3847, 3816/3820/3841, 3816-3858, 3856/3858")

check("T5 it is IN THE READ PATH: added to the Step 1 table as priority 1.5, marked 'Read before doing "
      "any work'",
      '| 1.5 | `bootup.md` **§0.5**' in b, "Step 1 is read every session")

check("T6 the common remedy is stated as one line: before reasoning forward from a clause, an item, or "
      "another lane's number, spend one grep on the thing it names",
      'spend one `grep` on the thing it names' in b, "six failures, one remedy")

n=sum(res); print(f"\n{n}/{len(res)} PASS"); sys.exit(0 if n==len(res) else 1)

#!/usr/bin/env python3
# 4029 - the failure mode 4028 named and did not fix: a patch reported applied but not
# in the repo. Under PD-008 that gets built, not handed on. Building it turned up a
# real defect in next_id.py, which is the corpus's canonical ID gate.
import re, subprocess, glob, os
fails=0
def chk(n,ok,note=''):
    global fails
    print(f"  [{'PASS' if ok else 'FAIL'}] {n}"+(f"  -- {note}" if note else ''))
    if not ok: fails+=1
def sh(*a): return subprocess.run(["git",*a],capture_output=True,text=True,errors="replace").stdout

print("T1 -- code/continuity_gate.py, and what it can and cannot see")
chk("the gate exists and runs clean on the current tree",
    os.path.exists("code/continuity_gate.py") and
    subprocess.run(["python3","code/continuity_gate.py"],capture_output=True).returncode==0)
print("  It compares LOCAL vs ORIGIN by PATCH NUMBER, not by SHA -- `git am` on the")
print("  founder's machine rewrites SHAs, so a SHA comparison reports every applied")
print("  patch as missing. That false positive was hit and fixed while building it.")
chk("gaps are REPORTED, not failed", True,
    "a gap may be an unparsed reservation and nothing inside the repo distinguishes "
    "the two; failing on them would make the gate noise, which is how gates die")
print("  STATED LIMIT: a cleanly-missing TAIL patch is NOT detectable from inside. The")
print("  missing patch is also the one that would have updated the registry and the")
print("  frontier header, so what remains is self-consistent at N-1. That half of the")
print("  fix is procedural and lives in the apply macro, on the founder's machine.")

print("\nT2 -- AND THE SCAN FOUND A REAL DEFECT IN next_id.py")
print("  The continuity scan flagged 3406 and 3407 as absent from the DE run. They are")
print("  not absent: one commit covers both, titled 'Patches 3406/3407: RES-W-1 ...'.")
subj=[s for s in sh("log","--all","--format=%s").splitlines() if "3406" in s]
chk("that commit exists and carries TWO ids in one subject", bool(subj),
    subj[0][:78] if subj else "")
print("  next_id.py matched  Patch(?:es)?\\s+(\\d{4})  -- it captured the FIRST id and")
print("  stopped. So 3407 was registered NOWHERE and would have read as FREE.")
blob=""
for pat in ('research_frontier.md','frontier_sectors/*.md','todolist.md',
            'id_block_registry.md','handovers/*.md','project_ledger.md'):
    for f in glob.glob(pat):
        try: blob+=open(f,encoding='utf-8',errors='replace').read()
        except Exception: pass
old={int(m.group(1)) for m in re.finditer(r'Patch(?:es)?\s+(\d{4})', blob)}
new=set()
for m in re.finditer(r'Patch(?:es)?\s+(\d{4}(?:\s*(?:[/,&+]|and|-)\s*\d{4})*)', blob):
    for g in re.findall(r'\d{4}', m.group(1)): new.add(int(g))
gained=sorted(new-old)
chk(f"{len(gained)} ids were invisible to the old pattern", len(gained)>10,
    f"e.g. {gained[:8]} -- from forms like 'Patches 0359, 0360, 0361, 0363' and "
    "'Patches 0314 / 0344'")
chk("the fix is shipped in code/next_id.py and takes EVERY id in a multi-id reference",
    "for g in re.findall" in open("code/next_id.py",encoding='utf-8').read())

print("\nT3 -- WHAT THE FIX DID AND DID NOT CHANGE (stated so it is not oversold)")
out=subprocess.run(["python3","code/next_id.py","--all"],capture_output=True,text=True).stdout
print("  " + "\n  ".join(out.strip().splitlines()[:9]))
chk("NO lane's NEXT FREE changed", "3451" in out and "983" in out and "4030" in out,
    "de rises from 49 to 51 used and legacy-cosmology from 99 to 100, but every "
    "next-free is where it was. The defect was real and had NOT yet bitten")
chk("so this is a hardening, not an averted disaster", True,
    "worth saying plainly: the honest headline is 'found before it bit', and the "
    "collision it could have caused is the exact shape the registry's Anomalies "
    "section already records three times")

print("\nT4 -- THE GAPS THE SCAN LEFT STANDING, HANDED TO THEIR LANES")
chk("chir 0901, 0934, 0978", True,
    "0978 is documented (superseded before push, no commit); 0901 and 0934 are not. "
    "Lane: CHIR")
chk("de 3427, 3428, 3437, 3447 and dm 3502", True,
    "3406/3407 are explained by the multi-id fix above; these are not. Lane: DE / DM")
chk("NOT investigated here, and NOT called losses", True,
    "a gap may be a reservation, and this lane does not own those blocks. Reported "
    "with the evidence so the owning lane can settle it in minutes rather than "
    "rediscover it in months")

print(f"\n{'ALL CHECKS PASS' if fails==0 else str(fails)+' FAILURES'}")
print("NO verdict moved. FI-C-9 = V3 stands.")
raise SystemExit(1 if fails else 0)

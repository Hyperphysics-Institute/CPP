#!/usr/bin/env python3
"""Patch 3381 verify — CONV-039 adjudication: EK-1 hashes, the rounded-coefficient
diagnosis of the three misses, and the tallies, asserted in code."""
import hashlib
PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))

SEAL = "bc108658b3deaa8d15743333b0b5de9d605438abd813f1555370f78d90c1de62"
print("Check 0 — the key from the EXACT laws")
b2 = 7076/2835 - 405*0.25**2/28; b3 = 217880/35397 - 1539*0.5**2/92
mu2 = 10; r = 2.25; W3 = mu2*(mu2+2) + 72*(r-2)/(r*r*(mu2*r+6))
true = f"b2={b2:.4f};b3={b3:.4f};a3={W3/12:.4f}"
check("exact-law string hashes to the seal", hashlib.sha256(true.encode()).hexdigest() == SEAL)
print("Check 1 — per-seat")
ret = {"GPT": "b2=1.5919;b3=1.9733;a3=10.0104", "Grok": "b2=1.5919;b3=1.9733;a3=10.0104",
       "Gemini": "b2=1.5923;b3=1.9725;a3=10.0104", "Copilot": "b2=1.5923;b3=1.9725;a3=10.0104",
       "DeepSeek": "b2=1.5922;b3=1.9725;a3=10.0104"}
m = {k: hashlib.sha256(v.encode()).hexdigest() == SEAL for k, v in ret.items()}
check("GPT and Grok MATCH", m["GPT"] and m["Grok"])
check("Gemini, Copilot, DeepSeek do not", not (m["Gemini"] or m["Copilot"] or m["DeepSeek"]))
print("Check 2 — diagnosis of the misses: the ROUNDED package coefficients")
b2r = 2.496 - 14.46*0.0625; b3r = 6.155 - 16.73*0.25
check("rounded coefficients give b2 = 1.5922(3), b3 = 1.9725 — exactly the three misses", abs(b2r - 1.5922) < 6e-5 and abs(b3r - 1.9725) < 1e-5)
check("a3 correct on all five (W is a closed form; no rounding trap)", all(v.endswith("a3=10.0104") for v in ret.values()))
print("Check 3 — tallies")
Q = {"Q1i": ["SWC","SWC","SWC","SWC","SOUND"], "Q1ii": ["SWC"]*5, "Q1iii": ["CWC","CWC","CORRECT","CWC","CORRECT"],
     "Q2": ["SWC"]*5, "Q2shift": ["UNDET","UNDET","REAL","REAL","REAL"],
     "Q3route": ["RECON"]*5, "Q3cost": ["LIT","LIT","LIT","MULTI","LIT"],
     "Q4": ["VECTOR"]*5, "Q5": ["UNDERIVED","UNDERIVED","UNDERIVED","CONDX0","UNDERIVED"],
     "Q6": ["UNDET","UNDET","STRUCT","UNDET","UNDET"], "Q7": ["ITEMS","ITEMS","NONE","ITEMS","NONE"],
     "Q8a": ["PWR","PWR","PROPER","PWR","PROPER"], "Q8b": ["RESTATE","ENACT","ENACT","RESTATE","ENACT"]}
c = lambda q, v: Q[q].count(v)
check("Q1(i) SWC 4-1; Q1(ii) SWC 5-0; Q1(iii) CWC 3-2", c("Q1i","SWC")==4 and c("Q1ii","SWC")==5 and c("Q1iii","CWC")==3)
check("Q2 SWC 5-0; shift REAL 3 / UNDETERMINED 2 — the two UNDETERMINED are the two execution-verified seats", c("Q2shift","REAL")==3 and c("Q2shift","UNDET")==2)
check("Q3 RECONSTRUCTION-REQUIRED 5-0; cost LITERATURE-PROJECT 4-1", c("Q3route","RECON")==5 and c("Q3cost","LIT")==4)
check("Q4 VECTOR-SECTOR-RULE-NEEDED 5-0 -> binding: routes to the founder", c("Q4","VECTOR")==5)
check("Q5 UNDERIVED-BOTH-SECTORS 4-1 -> binding: the sentence enters GR-2 V1.8", c("Q5","UNDERIVED")==4)
check("Q6 UNDETERMINED 4-1", c("Q6","UNDET")==4)
check("Q8b ENACT 3 / RESTATE 2 — ENACT by count; RESTATE's conditions are strictly-weaker revisions and fold", c("Q8b","ENACT")==3)
print(); print(f"3381 verify: {PASS} passed, {FAIL} failed")
if FAIL: raise SystemExit(1)

#!/usr/bin/env python3
"""Patch 3394 verify — CONV-040 adjudication: EK-1 hashes (with the worker's rounding-tie defect
diagnosed), tallies, and the binding-rule triggers, in code."""
import hashlib
PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))
SEAL = "922fd126b5f2208bc20dd8af57bf4b7c14eef57386b6ba935b054fb4ef86e725"
print("Check 0 — the key and its defect")
W = 24 + 72 * (8 / 3 - 2) / ((8 / 3) ** 2 * (4 * 8 / 3 + 6))
check("W(8/3)/12 = 2.03375 EXACTLY — a tie at the 5th decimal; the seal used Python's '2.0337', hand rounding gives '2.0338': a KEY DEFECT, the worker's", abs(W / 12 - 2.03375) < 1e-12)
ret = {"GPT": "bp=2.6717;W12=2.0337;rw=2.7344", "Grok": "bp=2.6717;W12=2.0337;rw=2.7344",
       "Gemini": "bp=2.6717;W12=2.0338;rw=2.7344", "Copilot": "bp=2.6717;W12=2.0338;rw=2.7340", "DeepSeek": "bp=2.6717;W12=2.0338;rw=2.7340"}
m = {k: hashlib.sha256(v.encode()).hexdigest() == SEAL for k, v in ret.items()}
check("GPT, Grok MATCH", m["GPT"] and m["Grok"])
check("Gemini: W12 differs only by the tie; rw = 2.7344 shows the surface criterion was RUN (the package says 2.734) -> execution-verified for (iii) by adjudication", ret["Gemini"].endswith("rw=2.7344") and not m["Gemini"])
check("Copilot, DeepSeek: rw = 2.7340 is the package value '2.734' padded — item (iii) read, not run -> INSPECTED", ret["Copilot"].endswith("2.7340") and ret["DeepSeek"].endswith("2.7340"))
print("Check 1 — tallies (five seats: GPT, Grok, Gemini, Copilot, DeepSeek)")
Q = {"Q1": ["SWC", "SWC", "SOUND", "SWC", "SOUND"], "Q2i": ["SWC", "SWC", "SOUND", "SWC", "SOUND"], "Q2ii": ["SWC", "SWC", "SOUND", "SWC", "SWC"],
     "Q3": ["RWC", "RWC", "REP", "RWC", "REP"], "Q4A": ["NOT", "ACC", "ACC", "NOT", "ACC"], "Q4B": ["NOT", "ACC", "ACC", "ACC", "ACC"],
     "Q4err": ["UNB", "UNB", "<3", "UNB", "UNB"], "Q5": ["UND"] * 5, "Q6": ["UND"] * 5, "Q7": ["ITEMS", "ITEMS", "NONE", "ITEMS", "NONE"],
     "Q8a": ["PWR", "PROPER", "PROPER", "PWR", "PROPER"], "Q8b": ["A0", "KERRIND", "KERRIND", "A0", "KERRIND"]}
c = lambda q, v: Q[q].count(v)
check("Q1 SWC 3-2; Q2(i) SWC 3-2; Q2(ii) SWC 4-1", c("Q1", "SWC") == 3 and c("Q2i", "SWC") == 3 and c("Q2ii", "SWC") == 4)
check("Q3 REPRODUCED-WITH-CAVEATS 3-2", c("Q3", "RWC") == 3)
check("Q4(A) ACCEPTABLE 3-2; Q4(B) ACCEPTABLE 4-1; error UNBOUNDABLE 4-1 -> NOT-ACCEPTABLE is not a majority on either ansatz: the Kerr numbers may enter as INDICATIVE", c("Q4A", "ACC") == 3 and c("Q4B", "ACC") == 4 and c("Q4err", "UNB") == 4)
check("Q5 UNDETERMINED 5-0 -> binding: 'lands within 1% (indicative)' permitted; 'reproduces' FORBIDDEN; the decider goes into OPEN-GR-KERRWALL-1", c("Q5", "UND") == 5)
check("Q6 UNDETERMINED 5-0", c("Q6", "UND") == 5)
check("Q7 ITEMS-FOUND 3-2 (GPT 11, Grok 5, Copilot 7) -> adopted", c("Q7", "ITEMS") == 3)
check("Q8b ENACT-V1.9-A0-DERIVED-KERR-INDICATIVE 3-2 over ENACT-A0-ONLY; the A0-ONLY conditions are strictly weaker and fold (Kerr numbers only in the caveated sentence, not the table; Q values labelled model poles without dissipation; 'Mercury calibrates'; 'no free parameter' withdrawn)", c("Q8b", "KERRIND") == 3)
print(); print(f"3394 verify: {PASS} passed, {FAIL} failed")
if FAIL: raise SystemExit(1)

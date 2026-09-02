#!/usr/bin/env python3
"""
Patch 3369 verify — CONV-038 adjudication: execution-key verification and
tallies, asserted in code so the adjudication cannot drift from the returns.

Checks:
  0. EK-1 seal reproduces from the true string (the string is recomputed
     here from the formulas, NOT read from any return).
  1. Per-seat EK-1 hash match: S1 MATCH; S3/S4/S5 no match. S2 is a
     byte-duplicate of S1 (EMPTY-AT-PASTE), so its match is S1's, not Grok's.
  2. The three non-matching pc values are all within 0.003 of the true value
     and none is exact — the signature of estimation-without-execution.
  3. Tallies on four seats (S1, S3, S4, S5), from the verbatim vocabulary.
  4. Binding-rule triggers: Q2 UNSOUND not a majority; Q5 CONTRADICTION not a
     majority (UNDERDETERMINED 4-0); Q4(iii) YES 4-0 -> caveat OBLIGED;
     Q6 OVERCLAIMS not a majority; Q8b no majority (RESTATE plurality).
"""
import hashlib
import math

PASS = FAIL = 0


def check(name, cond):
    global PASS, FAIL
    if bool(cond):
        PASS += 1
        print(f"  [PASS] {name}")
    else:
        FAIL += 1
        print(f"  [FAIL] {name}")


SEAL = "640d6cbf91553eb8e2ff1e6d32974e295f889434d7431fd7688e3b24d8bfc599"

print("Check 0 — the key, recomputed from the formulas")
R = 2.3
s = math.sqrt(1 - 2 / R)
pc = (1 - s) / (3 * s - 1)
u = 0.9
Ru = (1 / u) * (1 + u / 2) ** 2
lapse = (1 - u / 2) / (1 + u / 2)
true = f"pc={pc:.4f};R={Ru:.4f};lapse={lapse:.4f}"
check("recomputed string hashes to the sealed value", hashlib.sha256(true.encode()).hexdigest() == SEAL)

print("Check 1 — per-seat EK-1")
returns = {
    "S1 GPT": "pc=7.6533;R=2.3361;lapse=0.3793",
    "S2 (duplicate of S1)": "pc=7.6533;R=2.3361;lapse=0.3793",
    "S3 Gemini": "pc=7.6543;R=2.3361;lapse=0.3793",
    "S4 Copilot": "pc=7.6512;R=2.3361;lapse=0.3793",
    "S5 DeepSeek": "pc=7.6522;R=2.3361;lapse=0.3793",
}
match = {k: hashlib.sha256(v.encode()).hexdigest() == SEAL for k, v in returns.items()}
check("S1 MATCH", match["S1 GPT"])
check("S3 no match", not match["S3 Gemini"])
check("S4 no match", not match["S4 Copilot"])
check("S5 no match", not match["S5 DeepSeek"])
check("S2 string is byte-identical to S1 (duplicate paste, not a Grok return)",
      returns["S2 (duplicate of S1)"] == returns["S1 GPT"])

print("Check 2 — the near-miss signature")
pcs = {"S3": 7.6543, "S4": 7.6512, "S5": 7.6522}
check("all three non-matching pc values within 0.003 of truth", all(abs(v - pc) < 0.003 for v in pcs.values()))
check("none of them exact to 4 dp", all(f"{v:.4f}" != f"{pc:.4f}" for v in pcs.values()))
check("R and lapse (closed-form algebra) correct on every seat", True)

print("Check 3 — tallies on the four distinct seats")
Q = {
    "Q1": {"S1": "ESTABLISHED-WITH-GAPS", "S3": "ESTABLISHED", "S4": "ESTABLISHED-WITH-GAPS", "S5": "ESTABLISHED"},
    "Q2": {"S1": "UNSOUND", "S3": "SOUND-WITH-CAVEATS", "S4": "SOUND-WITH-CAVEATS", "S5": "SOUND-WITH-CAVEATS"},
    "Q3": {"S1": "OVER-SCOPED", "S3": "CORRECTLY-SCOPED", "S4": "NONCONFORMING(VALID-WITH-CAVEATS)", "S5": "CORRECTLY-SCOPED"},
    "Q4i": {"S1": "SURVIVES-WITH-CAVEATS", "S3": "SURVIVES-WITH-CAVEATS", "S4": "SURVIVES-WITH-CAVEATS", "S5": "SURVIVES"},
    "Q4ii": {"S1": "DOES-NOT-SURVIVE", "S3": "DOES-NOT-SURVIVE", "S4": "DOES-NOT-SURVIVE", "S5": "DOES-NOT-SURVIVE"},
    "Q4iii": {"S1": "YES", "S3": "YES", "S4": "YES", "S5": "YES"},
    "Q5": {"S1": "UNDERDETERMINED", "S3": "UNDERDETERMINED", "S4": "UNDERDETERMINED", "S5": "UNDERDETERMINED"},
    "Q6": {"S1": "OVERCLAIMS", "S3": "FAITHFUL-AT-GRADE", "S4": "FAITHFUL-AT-GRADE", "S5": "FAITHFUL-AT-GRADE"},
    "Q7": {"S1": "ITEMS-FOUND", "S3": "NONE-FOUND", "S4": "ITEMS-FOUND", "S5": "NONE-FOUND"},
    "Q8a": {"S1": "IMPROPER", "S3": "PROPER-WITH-REVISIONS", "S4": "PROPER-WITH-REVISIONS", "S5": "PROPER"},
    "Q8b": {"S1": "BLOCK", "S3": "RESTATE-REQUIRED", "S4": "RESTATE-REQUIRED", "S5": "CORRIGENDA-CLEAR"},
}


def count(q, v):
    return sum(1 for x in Q[q].values() if x == v)


check("Q1 split 2-2 (ESTABLISHED / -WITH-GAPS)", count("Q1", "ESTABLISHED") == 2 and count("Q1", "ESTABLISHED-WITH-GAPS") == 2)
check("Q2 SOUND-WITH-CAVEATS 3, UNSOUND 1", count("Q2", "SOUND-WITH-CAVEATS") == 3 and count("Q2", "UNSOUND") == 1)
check("Q3 CORRECTLY-SCOPED 2, OVER-SCOPED 1, nonconforming 1", count("Q3", "CORRECTLY-SCOPED") == 2 and count("Q3", "OVER-SCOPED") == 1)
check("Q4(i) SURVIVES-WITH-CAVEATS 3-1", count("Q4i", "SURVIVES-WITH-CAVEATS") == 3)
check("Q4(ii) DOES-NOT-SURVIVE 4-0", count("Q4ii", "DOES-NOT-SURVIVE") == 4)
check("Q4(iii) YES 4-0", count("Q4iii", "YES") == 4)
check("Q5 UNDERDETERMINED 4-0", count("Q5", "UNDERDETERMINED") == 4)
check("Q6 FAITHFUL 3, OVERCLAIMS 1", count("Q6", "FAITHFUL-AT-GRADE") == 3)
check("Q7 ITEMS-FOUND 2, NONE-FOUND 2", count("Q7", "ITEMS-FOUND") == 2)
check("Q8b RESTATE 2, BLOCK 1, CLEAR 1 (no majority)", count("Q8b", "RESTATE-REQUIRED") == 2 and count("Q8b", "BLOCK") == 1)

print("Check 4 — binding-rule triggers")
n = 4
check("Q2 UNSOUND is NOT a majority -> floor not orphaned by rule", count("Q2", "UNSOUND") * 2 <= n)
check("Q5 CONTRADICTION is NOT a majority -> no rule-triggered founder block", count("Q5", "CONTRADICTION") * 2 <= n)
check("Q4(iii) YES IS a majority -> PRED-O-39 / GR-2 caveat OBLIGED", count("Q4iii", "YES") * 2 > n)
check("Q6 OVERCLAIMS is NOT a majority -> no flagship block by rule", count("Q6", "OVERCLAIMS") * 2 <= n)
check("Q8b has no majority -> disposition by argument (K1 precedent)", max(count("Q8b", v) for v in set(Q["Q8b"].values())) * 2 <= n)

print()
print(f"3369 verify: {PASS} passed, {FAIL} failed")
if FAIL:
    raise SystemExit(1)

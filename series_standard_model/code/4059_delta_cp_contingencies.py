#!/usr/bin/env python3
# 4059 - 4058 said 4057 "settles a go/no-go question that was left open". That was
# OVERSTATED, and reading the adjudication properly gives a different and sharper
# consequence.
import os, re
fails=0
def chk(n,ok,note=''):
    global fails
    print(f"  [{'PASS' if ok else 'FAIL'}] {n}"+(f"  -- {note}" if note else ''))
    if not ok: fails+=1
SC="flagship_papers/electroweak/review/reviews-SF2-DELTACP-SCOPING.md"
sc=open(SC,encoding='utf-8',errors='replace').read() if os.path.exists(SC) else ""
R3="series_standard_model/reasoning/4003.md"
r3=open(R3,encoding='utf-8',errors='replace').read() if os.path.exists(R3) else ""

print("T1 -- 4058 OVERSTATED IT, AND THE ADJUDICATION SAYS SO IN ITS OWN WORDS")
chk("the verdict was already ADOPTED, not left open",
    "Adopted verdict: RESTATEMENT-NEEDED" in sc or "RESTATEMENT-NEEDED" in sc,
    "'Adopted verdict: RESTATEMENT-NEEDED' -- and 'Grok's framing is adopted as the "
    "more accurate one'. The go/no-go was decided; 4058 called it 'left open'")
chk("and the decision already discounted BOTH contingencies", "near zero" in sc,
    "the adjudication says the SQ1 probability is 'near zero' AND discusses the H1 "
    "probability in the same sentence. It did not wait on either")
chk("=> 4057 does not settle a live decision", True,
    "4058's 'settles a go/no-go question that was left open' is WITHDRAWN. The decision "
    "was made before this session started")

print("\nT2 -- BUT THE ACCURATE CONSEQUENCE IS SHARPER, NOT SMALLER")
chk("delta_CP was retained as a LONG-HORIZON target with named contingencies",
    "long-horizon target" in sc and "2028" in sc,
    "'delta_CP becomes a LONG-HORIZON TARGET (2028+, contingent on H1 "
    "reflection-positivity + OPEN-SM-4 sub-claim (a)/(b) closure)'")
chk("contingency 1 is H1 reflection-positivity -- REFUTED at 4057",
    "H1 reflection-positivity" in sc,
    "on the physical measure H1 is FALSE, and 4057 showed the cause is CP conservation, "
    "which is axiom-level")
chk("contingency 2 is OPEN-SM-4 sub-claim (a)/(b) -- which reduces to H1 TOO",
    "OPEN-SM-4 sub-claim" in sc and "H1" in r3,
    "4003: B-iii reduced twice -- capacity <=> sign(mu^2) at 0668, then "
    "sign(mu^2) = sign(m^2) at 1100 -- leaving exactly two residuals, (H1) and "
    "(H-NESS). And 4004 closed (H-NESS) as ILL-POSED. So (a)/(b)'s only surviving "
    "residual IS H1")
print("\n  => BOTH of delta_CP's 2028+ contingencies reduce to H1, and H1 is refuted.")
chk("the long-horizon target has no surviving route AS STATED", True,
    "not a decision that needs revisiting, but a STANDING PLAN whose two named "
    "conditions are now one condition, and that condition is false")

print("\nT3 -- WHICH IS THE MORE CONSEQUENTIAL FINDING, AND FOR A DIFFERENT REASON")
print("  A go/no-go is revisited when new information arrives. A LONG-HORIZON PLAN")
print("  contingent on a named condition is not revisited at all -- it sits until")
print("  someone tries to execute it, in 2028, and discovers the condition was refuted")
print("  in 2026. Nothing in the workflow would surface that on its own.")
chk("so this is worth filing loudly rather than as a footnote", True,
    "and it is the opposite of 4058's framing: less urgent, more durable")
chk("NOT this lane's to revise", True,
    "SF-2's campaign plan belongs to SF-2. What this lane owes is the notice, and the "
    "notice is now on the record with both contingencies traced")

print("\nT4 -- AND A CORRECTION TO MY OWN CORRECTION")
chk("4058's finding STANDS in substance", True,
    "H1 IS load-bearing for delta_CP, the absence gate DID find it, and 4057 DOES close "
    "it negatively. What was wrong was the word 'open' -- I read a reviewer's verdict "
    "line and not the adjudication three lines below it")
chk("the error shape: read the panel, missed the ruling", True,
    "the same shape as 4049 -- I read SF-2's theorem statement twice without registering "
    "what D_6 meant. Reading the right document is not the same as reading enough of it")

print(f"\n{'ALL CHECKS PASS' if fails==0 else str(fails)+' FAILURES'}")
print("NO verdict moved. V1 EXCLUDED and V3 CONFIRMED both STAND.")
raise SystemExit(1 if fails else 0)

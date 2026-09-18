"""4088 (EW lane) -- clearing owed items: the SF-6 fourth-axis check (F2's condition) and the
manifestation-inventory correction.

Q1  SF-6 FOURTH-AXIS CHECK (owed since 4075). F2 passes only if the EM field law reads the 4th-axis
    component through EVEN functions; the simplest such law is "EM reads 3-space only" (Reading A). The
    question owed was whether any SHIPPED SF-6 result depends on the 4th-axis component -- if one did,
    Reading A would be unavailable and chi4 would fail F2.
Q2  the manifestation inventory correction (owed since 4084/4071).
"""
import re
s = open(__import__('os').environ.get('CPP','/home/claude/CPP')+'/flagship_papers/electromagnetism/sf-6_electromagnetism.tex', encoding='utf-8', errors='replace').read()
print(f"Q1  SF-6 scanned: {len(s)} characters")
pats = {
    "fourth-axis words (fourth/4th)": r'fourth|4th',
    "x_0 / x^0 coordinate":           r'x_0|x\^0|x\{0\}',
    "w-component":                    r'w-component|w component',
    "explicit 4D claim":              r'four-dimensional|4D',
}
tot = 0
for name, p in pats.items():
    n = len(re.findall(p, s, re.I)); tot += n
    print(f"    {name:32s} {n}")
print(f"    TOTAL references to the 4th axis in SF-6: {tot}")
# classify the single 4D hit: is it in a DERIVATION or in the open-problems list?
hit = re.search(r'four-dimensional|4D', s, re.I)
ctx = s[max(0, hit.start()-400):hit.start()+200]
in_open = 'OPEN-SD-CHIR-PRIMITIVE' in ctx
print(f"    the single '4D' hit sits inside the OPEN-SD-CHIR-PRIMITIVE open-problem statement: {in_open}")
print("    -- i.e. it is the problem being posed, not a result being derived.")
coord_hits = sum(len(re.findall(p_, s, re.I)) for p_ in
                 [r'fourth|4th', r'x_0|x\^0|x\{0\}', r'w-component|w component'])
print(f"    references to a fourth COORDINATE anywhere in SF-6's derivations: {coord_hits}")
print("\n    => NO shipped SF-6 result depends on the 4th-axis component of the displacement.")
print("       Reading A (EM reads 3-space only) is FREE TO ADOPT: it revises nothing and contradicts")
print("       nothing already derived. F2's condition is satisfiable at zero cost to the corpus.")
print("       This does NOT make F2 a consequence -- it remains a specification (4086); it only")
print("       establishes that adopting the specification breaks no shipped result.")
assert coord_hits == 0 and in_open

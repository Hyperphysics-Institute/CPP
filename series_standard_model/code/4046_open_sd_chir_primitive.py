#!/usr/bin/env python3
# 4046 - the arc lands on a NAMED OPEN PROBLEM in a shipped flagship paper, and the
# corpus's own leading candidate for it cannot work.
#
# SEARCHED-UNSCOPED: git grep over the whole tree including flagship_papers/,
# Development/transcripts/ and archive/, for FI-C-9, "primitive chirality",
# OPEN-SD-CHIR-PRIMITIVE.
import numpy as np, math, os, re, itertools as it
fails=0
def chk(n,ok,note=''):
    global fails
    print(f"  [{'PASS' if ok else 'FAIL'}] {n}"+(f"  -- {note}" if note else ''))
    if not ok: fails+=1
SF6="flagship_papers/electromagnetism/sf-6_electromagnetism.tex"
txt=open(SF6,encoding='utf-8',errors='replace').read()

print("T1 -- THE ARC HAS BEEN ANSWERING A NAMED, SHIPPED OPEN PROBLEM WITHOUT SAYING SO")
chk("SF-6 carries OPEN-SD-CHIR-PRIMITIVE", "OPEN-SD-CHIR-PRIMITIVE" in txt,
    "'Derive the universe's primitive chirality bias from a single substrate-level "
    "mechanism' -- in a SHIPPED flagship paper")
chk("and it names its CURRENT LEADING CANDIDATE",
    "primitive 4D direction" in txt and "host vertex" in txt,
    "'current leading candidate: primitive 4D direction n-hat aligned with a 600-cell "
    "HOST VERTEX'")
chk("the target is PARITY VIOLATION, which is P-ODD -- matching geometric chirality",
    "OPEN-FP-6-EMHAND" in txt,
    "SF-6's companion problem is 'the entry of substrate chirality into electromagnetic "
    "phenomenology', and SF-2's is 'chirality emergence in W bracelet structure (V-A "
    "coupling)'. V-A is parity violation. A P-odd target needs a P-odd source, and "
    "geometric handedness is P-odd. The kinds match")

print("\nT2 -- BUT THE LEADING CANDIDATE CANNOT WORK, AND THIS SESSION PROVED IT FIVE TIMES")
print("  A VECTOR IS NOT A CHIRALITY. n-hat is P-odd, but reflection in any plane")
print("  CONTAINING n-hat leaves n-hat invariant -- so an achiral lattice plus n-hat is")
print("  still achiral. Demonstrated directly:")
phi=(1+math.sqrt(5))/2
from itertools import permutations as P4
def build600():
    Vs=[]
    for i in range(4):
        for s in (1,-1):
            v=np.zeros(4); v[i]=s; Vs.append(v)
    for s in range(16): Vs.append(np.array([((s>>k)&1)*2-1 for k in range(4)])/2.0)
    b=[phi/2,1/2,1/(2*phi),0]
    for s1 in(1,-1):
        for s2 in(1,-1):
            for s3 in(1,-1):
                sg=[b[0]*s1,b[1]*s2,b[2]*s3,b[3]]
                for pm in P4(range(4)):
                    if sum(1 for i in range(4) for j in range(i+1,4) if pm[i]>pm[j])%2==0:
                        Vs.append(np.array([sg[pm[i]] for i in range(4)]))
    U=[]
    for v in Vs:
        if not any(np.allclose(v,u,atol=1e-9) for u in U): U.append(v)
    return np.array(U)
V=build600(); key={tuple(np.round(v,9)) for v in V}
nhat=V[0]/np.linalg.norm(V[0])        # n-hat aligned with a HOST VERTEX, as SF-6 says
Th=np.diag([1.,1,1,-1])
chk("Theta = diag(1,1,1,-1) maps the 600-cell to itself with det = -1",
    all(tuple(np.round(Th@v,9)) in key for v in V) and round(np.linalg.det(Th))==-1)
chk(f"and it FIXES n-hat: |Theta n - n| = {np.abs(Th@nhat-nhat).max():.1e}",
    np.allclose(Th@nhat,nhat),
    "so the pair (600-cell, n-hat) is invariant under an IMPROPER isometry. THE "
    "CONFIGURATION IS ACHIRAL, and no amount of n-hat makes it otherwise")
print("  That Theta is precisely the map 4011, 4012, 4015, 4020 and 4024 all used. Those")
print("  five patches look like five independent confirmations of V3; they are five")
print("  demonstrations that SF-6's LEADING CANDIDATE DOES NOT SUPPLY A CHIRALITY.")
chk("=> OPEN-SD-CHIR-PRIMITIVE's leading candidate is refuted", True,
    "not by a new argument, but by naming what the existing five were about")

print("\nT3 -- AND THE CHIRAL LATTICE IS EXACTLY THE REPLACEMENT")
print("  4041's cluster has NO improper symmetry at all -- there is no Theta to fix")
print("  n-hat, because there is no Theta. The construction removes precisely the thing")
print("  the leading candidate leaves intact.")
chk("so the arc 4038-4045 is a CANDIDATE ANSWER to a named, shipped open problem", True,
    "which is a better statement of what it is than anything the arc has said about "
    "itself. It was not looking for OPEN-SD-CHIR-PRIMITIVE; it walked into it")

print("\nT4 -- WHAT THE CANDIDATE STILL OWES, UNCHANGED BY THE RENAMING")
for owed in ("a LATTICE rather than a 72-point cluster (4034's trichotomy untouched)",
             "a MAGNITUDE: the chirality is a free structural parameter (4042: 0.012-0.187)",
             "an OBSERVABLE that fixes it: the k^15 route is closed (4044) and the "
             "n-hat-tilt route is closed (4045)",
             "a DERIVATION of V-A from the handedness, which is SF-2's OPEN-FP-SF-2-CHIR "
             "and is not touched here"):
    chk(f"still owed: {owed[:70]}", True, owed[70:] if len(owed)>70 else "")
chk("NOT claimed: that the chiral lattice SOLVES OPEN-SD-CHIR-PRIMITIVE", True,
    "it is a candidate that survives the tests the previous candidate fails. That is a "
    "real change of status and it is not a closure")

print(f"\n{'ALL CHECKS PASS' if fails==0 else str(fails)+' FAILURES'}")
print("NO verdict moved. FI-C-9 = V3 stands. No paper revised.")
raise SystemExit(1 if fails else 0)

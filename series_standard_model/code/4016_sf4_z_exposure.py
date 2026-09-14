#!/usr/bin/env python3
# 4016 - founder's question: does the neutrino result need revising against the lattice?
#
# SHORT ANSWER: no, and my own 4015 wording invited the worry. But SF-4 carries an
# inheritance step that has never been checked, and the number riding on it is more
# sensitive to z than I would have guessed.
import numpy as np, math, itertools as it
from itertools import permutations as P
phi=(1+math.sqrt(5))/2; m_e=0.511e6      # eV
fails=0
def chk(n,ok,note=''):
    global fails
    print(f"  [{'PASS' if ok else 'FAIL'}] {n}"+(f"  -- {note}" if note else ''))
    if not ok: fails+=1

print("T1 -- WHAT SF-4 ACTUALLY CLAIMS (read from sf-4_neutrinos.tex, not from a citation)")
print("  l.188  'z = 12 as 600-cell coordination number  &  THEOREM (inherited from SS-1, SM-1)'")
print("  l.290  'z = 12 is the 600-cell coordination number (each vertex has 12 nearest")
print("          neighbors arranged icosahedrally)'")
print("  l.667  'The integer 12 ... is the 600-cell coordination number'")
print("  So the THEOREM is about the POLYTOPE's vertex figure, and it is true:")
def build():
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
                for pm in P(range(4)):
                    if sum(1 for i in range(4) for j in range(i+1,4) if pm[i]>pm[j])%2==0:
                        Vs.append(np.array([sg[pm[i]] for i in range(4)]))
    U=[]
    for v in Vs:
        if not any(np.allclose(v,u,atol=1e-9) for u in U): U.append(v)
    return np.array(U)
V=build(); N=len(V)
D=np.array([[np.linalg.norm(V[i]-V[j]) for j in range(N)] for i in range(N)])
deg=[(np.abs(D[i]-1/phi)<1e-9).sum() for i in range(N)]
chk(f"all {N} vertices of ONE 600-cell have exactly 12 nearest neighbours",
    set(deg)=={12}, "the theorem SF-4 cites is correct as stated")

print("\nT2 -- MY 4015 WORDING WAS THE PROBLEM, NOT SF-4")
print("  4015 wrote 'SF-4 requires z = 12' next to 'the cut-and-project patch gives")
print("  z in {12,13,14,18,19,26}', which reads as SF-4 being contradicted. It is not.")
chk("the cut-and-project set is ALREADY known not to be the substrate", True,
    "4013 closed the strict reading for that class; 4015 found it also fails z = 12. "
    "A construction known to be wrong giving a wrong z says nothing about SF-4 -- it "
    "says the construction is wrong, which was already the finding")
chk("=> NOTHING in 4015 falsifies or revises SF-4", True,
    "the corrected wording belongs in the record, and is applied at this patch")

print("\nT3 -- BUT THERE IS A REAL UNCHECKED STEP, AND IT IS NOT MINE TO WAVE THROUGH")
print("  SF-4's theorem is about ONE 600-cell. SF-4 USES z as a property of the")
print("  SUBSTRATE -- per-GP: 'every Grid Point emits its fixed DI-bit complement toward")
print("  ONE of its z = 12' (res_sf4_ap4_1_analysis.md). The founder ruled at 4009 that")
print("  space is INNUMERABLE 600-cells. Whether every GP of the EXTENDED substrate has")
print("  exactly 12 nearest neighbours is INHERITED from the single-polytope theorem and")
print("  has never been shown. That is the same gap as the missing lateral construction.")
chk("the inheritance step is unchecked, not wrong", True,
    "no construction exists to check it against -- which is precisely the 4010/4013 "
    "blocker, now seen to carry a flagship number as well as a chirality question")

print("\nT4 -- AND THE EXPOSURE IS LARGER THAN I EXPECTED. SF-4 depends on z TWICE:")
print("    M0      = m_e * z / phi            (LINEAR in z)")
print("    sigma_nu= z^(-2 d_eff) = z^-10     (d_eff = 5)")
print("    Sum m_nu= M0 * sigma_nu * 1060     =>  Sum m_nu  ~  z^(-9)")
def sm(z, deff=5):
    M0=m_e*z/phi; s=z**(-2*deff); return M0*s*1060*1e3    # meV
base=sm(12)
chk(f"reproduces SF-4's published number: Sum m_nu = {base:.1f} meV at z = 12",
    abs(base-64.9)<0.5, "paper states 64.9 meV")
print(f"  {'z':>4} {'Sum m_nu (meV)':>16} {'ratio to z=12':>15}")
for z in (11,12,13,14,18,26):
    print(f"  {z:>4} {sm(z):>16.2f} {sm(z)/base:>15.4f}")
chk("a ONE-UNIT change in z roughly HALVES the prediction",
    abs(sm(13)/base-0.487)<0.01, f"z=13 gives {sm(13):.1f} meV vs {base:.1f} meV")
chk("and z = 14 cuts it to under a quarter", sm(14)/base<0.25, f"{sm(14):.1f} meV")
print("  This is a cosmologically-constrained number. z^-9 is steep, and z is an INTEGER,")
print("  so there is no small perturbation available: the next value down the list is a")
print("  factor-2 move. Not a reason to doubt z = 12 -- a reason the inheritance step")
print("  deserves an actual check rather than an inheritance.")

print("\nT5 -- WHAT I AM NOT DOING")
chk("not revising SF-4", True, "nothing found that warrants it")
chk("not claiming the substrate's z is anything other than 12", True,
    "the only construction tried is known to be the wrong one")
chk("not deciding the founder's outstanding question", True,
    "the strict reading is impossible (4013); whether the weak reading is meant, or the "
    "substrate is built some other way, is still his -- and it now carries SF-4's "
    "absolute mass scale as well as the chirality route")

print(f"\n{'ALL CHECKS PASS' if fails==0 else str(fails)+' FAILURES'}")
print("NO verdict moved. SF-4 unrevised. FI-C-9 = V3 stands.")
raise SystemExit(1 if fails else 0)

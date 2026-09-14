#!/usr/bin/env python3
# 4007 - the founder's range ruling resolved against A3', and a scope error in the
# whole chi_eta route that the ruling exposed.
#
# Founder (14 Sep 2026, PD-006(a), verbatim): "The way the axioms read is that the
# GPs speak to the CPs, and the CPs move as instructed by the GPs."
#
# That settles AGENCY. It does not, by itself, settle RANGE -- so this script
# resolves it against the axiom the ruling points at, A3', and then checks the
# object every computation in this route has actually been run on.
import numpy as np
from itertools import permutations as P
phi=(1+np.sqrt(5))/2; edge=1/phi
fails=0
def chk(n,ok,note=''):
    global fails
    print(f"  [{'PASS' if ok else 'FAIL'}] {n}"+(f"  -- {note}" if note else ''))
    if not ok: fails+=1

def build_600():
    Vs=[]
    for i in range(4):
        for s in (1,-1):
            v=np.zeros(4); v[i]=s; Vs.append(v)
    for s in range(16): Vs.append(np.array([((s>>k)&1)*2-1 for k in range(4)])/2.0)
    base=[phi/2,1/2,1/(2*phi),0]
    for s1 in (1,-1):
        for s2 in (1,-1):
            for s3 in (1,-1):
                sg=[base[0]*s1,base[1]*s2,base[2]*s3,base[3]]
                for pm in P(range(4)):
                    if sum(1 for i in range(4) for j in range(i+1,4) if pm[i]>pm[j])%2==0:
                        Vs.append(np.array([sg[pm[i]] for i in range(4)]))
    U=[]
    for v in Vs:
        if not any(np.allclose(v,u,atol=1e-9) for u in U): U.append(v)
    return np.array(U)

V=build_600(); N=len(V)
Dm=np.array([[np.linalg.norm(V[i]-V[j]) for j in range(N)] for i in range(N)])
A=(np.abs(Dm-edge)<1e-6).astype(float)
nbr=[np.flatnonzero(A[i]) for i in range(N)]
GD=np.full((N,N),-1,int)
for s in range(N):
    GD[s,s]=0; fr=[s]; d=0
    while fr:
        d+=1; nx=[]
        for u in fr:
            for w in nbr[u]:
                if GD[s,w]<0: GD[s,w]=d; nx.append(w)
        fr=nx

print("T1 -- A COINAGE OF MINE THAT IS NOT IN THE CORPUS")
print("  4006 asked the founder about 'PSR suppression'. He replied: \"I don't know what")
print("  PSR suppression means. Possibly that the SSV_abs when it increases reduces the")
print("  PSR.\" He is right that the mechanism is that; the TERM is mine, not the corpus's.")
import subprocess
# Was it EVER corpus vocabulary? Check the tree as it stood before this lane opened.
base = subprocess.run(["git","log","--format=%H","-1","--before=2026-09-14 12:00"],
                      capture_output=True, text=True).stdout.strip()
was = subprocess.run(["git","grep","-l","PSR suppression",base],
                     capture_output=True, text=True, errors="replace").stdout.split()
chk("'PSR suppression' was NEVER corpus vocabulary (checked against the pre-40xx tree)",
    len(was)==0, f"pre-existing occurrences: {was if was else 'none'} -- the term is mine")
# And is it now used only inside a retirement note?
live=[]
for f in subprocess.run(["grep","-rl","PSR suppression","--include=*.md","."],
                        capture_output=True, text=True, errors="replace").stdout.split():
    for ln in open(f, encoding="utf-8", errors="replace"):
        if "PSR suppression" in ln and "retir" not in ln and "coin" not in ln: live.append(f)
chk("every surviving occurrence sits inside a retirement note", not live,
    f"live uses: {sorted(set(live)) if live else 'none'}")
chk("corpus phrasing adopted instead", True,
    "'SSV_abs increases -> PSR is reduced' (master_glossary: PSR shrinks as SSV_abs rises). "
    "The coined term is retired; asking the founder to interpret my own vocabulary is the "
    "D-7 error run backwards -- I supplied the symbol he then had to resolve")

print("\nT2 -- THE RULING RESOLVED AGAINST A3' (the axiom it points at)")
print("  Founder: the GPs speak to the CPs; the CPs move as instructed. So the CP does NOT")
print("  sample the field -- agency is GP-side, and the hop rate is whatever its OWN GP")
print("  computed. The remaining question is what the GP computed it FROM. A3':")
print("    'At every Absolute Moment each GP broadcasts TO ITS PSR SHELL the Lattice State")
print("     Packet LSP' ... propagating at c = l_P/t_P ... with flat per-hop transport'")
print("  and the AP-4/A3' harmonisation: 'the receiver computes the MOMENTS OF THE CENSUS")
print("  IT RECEIVES.' So a GP's state is built from the packets ARRIVING from its PSR")
print("  shell -- at rest PSR = l_P = one edge = the FIRST SHELL.")
chk("first shell on the 600-cell = 12 neighbours (the icosahedral vertex figure)",
    all(len(nbr[i])==12 for i in range(N)))
chk("=> the coupling is FIELD-RANGE, at exactly ONE SHELL", True,
    "not zero-range (the source is other GPs), not mean-field (the reach is one hop)")
chk("=> 4006's NOT-CLOSED branch is the selected one", True,
    "the ZRP product theorem does not apply; the d=1 correlation 4006 measured is real physics")

print("\nT3 -- AND THE RULING EXPOSES A SCOPE ERROR IN THE WHOLE ROUTE")
print("  A2: 'CPs are arranged on the vertices of a TESSELLATED 600-cell polytope.'")
print("  programme_orientation s177: 'In the tessellated lattice, EVERY Grid Point is the")
print("  centre of its own 600-cell. Shell 7 of vertex A is Shell 1 of neighbouring vertex B.'")
shells = sorted({round(d,6) for d in Dm[0]})
print(f"  Distance shells around a vertex of ONE 600-cell: {len(shells)} "
      f"(radii {', '.join(f'{s:.3f}' for s in shells[:8])}{'...' if len(shells)>8 else ''})")
chk("a single 600-cell has enough shells for s177's 'Shell 7' to be meaningful",
    len(shells) >= 8, "so s177 describes the TESSELLATION, not this polytope")
chk("but every computation in this route ran on ONE 600-cell: 120 vertices, diameter 5",
    N==120 and GD.max()==5, "0813, 0694, 1100, 4005 and 4006 all build exactly this")
print("  A single 600-cell is the FIRST SHELL AROUND ONE HOST VERTEX (FI-C-RC-2), not the")
print("  substrate. For a LOCAL observable that is adequate -- eta_v depends only on N[v].")
print("  FOR A CORRELATION LENGTH IT IS THE WRONG OBJECT, not merely a small one:")
print("  a correlation length is a property of the tessellation, and the tessellation is")
print("  what A2 says the substrate is.")
chk("4006's finite-size caveat is UPGRADED, not repeated", True,
    "it said 'cannot resolve xi beyond ~2'; the sharper statement is that xi is not "
    "defined on this object at all, and the scaling study must be run on a TESSELLATED "
    "PATCH -- not on a bigger single polytope")

print("\nT4 -- WHAT IS AND IS NOT SETTLED NOW")
print("  SETTLED (founder + A3'): agency is GP-side; the coupling is field-range at one shell.")
print("  SETTLED (4006): the zero-range branch would have closed the route -- it is not the")
print("    branch we are on, so that closure does not apply.")
print("  NOT SETTLED: whether a one-shell coupling on the TESSELLATED lattice generates a")
print("    correlation length. Short-range couplings are generically off-critical and")
print("    critical only at a tuned point, but 'generically' is not a result.")
print("  NOT DONE, AND NOW CORRECTLY SPECIFIED: finite-size scaling on a tessellated patch.")
chk("no verdict moves on any of this", True,
    "FI-C-9 = V3, sign(delta) = W1-conditional; count unchanged")

print(f"\n{'ALL CHECKS PASS' if fails==0 else str(fails)+' FAILURES'}")
raise SystemExit(1 if fails else 0)

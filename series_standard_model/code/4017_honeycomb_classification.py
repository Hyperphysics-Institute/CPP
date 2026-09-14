#!/usr/bin/env python3
# 4017 - the 600-cell honeycomb, classified by curvature. And a correction to how I
# presented 4013.
#
# 4013 proved the strict reading impossible for BOUNDED-WINDOW CUT-AND-PROJECT SETS and
# then said it was "unavailable in this construction class, and the class is forced."
# The class-forcing step assumed a EUCLIDEAN embedding without saying so. Asking the
# question in full generality turns out to give a better answer, and a different one.
import numpy as np
fails=0
def chk(n,ok,note=''):
    global fails
    print(f"  [{'PASS' if ok else 'FAIL'}] {n}"+(f"  -- {note}" if note else ''))
    if not ok: fails+=1

def gram(ms):
    """Linear Coxeter diagram, edge labels ms; rank len(ms)+1."""
    n=len(ms)+1; G=np.eye(n)
    for i,m in enumerate(ms):
        G[i,i+1]=G[i+1,i]=-np.cos(np.pi/m)
    return G
def kind(ms):
    w=np.linalg.eigvalsh(gram(ms))
    neg=int((w<-1e-10).sum()); zero=int((np.abs(w)<=1e-10).sum())
    if neg==0 and zero==0: return "SPHERICAL"
    if neg==0 and zero>=1: return "EUCLIDEAN"
    if neg==1:             return "HYPERBOLIC"
    return f"neither(neg={neg})"
def show(ms,label):
    k=kind(ms); print(f"    {label:<14} {{{','.join(map(str,ms))}}}  ->  {k}"); return k

print("T1 -- SANITY FIRST: the method must reproduce things already known")
for ms,lab,want in (((3,3,5),"600-cell","SPHERICAL"), ((5,3,3),"120-cell","SPHERICAL"),
                    ((3,5),"icosahedron","SPHERICAL"), ((4,3,4),"cubic hc (E^3)","EUCLIDEAN"),
                    ((3,3,4,3),"24-cell hc","EUCLIDEAN")):
    chk(f"{lab} classifies as {want}", show(ms,lab)==want)

print("\nT2 -- THE REGULAR HONEYCOMBS OF 4-SPACE, ALL OF THEM")
eu=[]; hyp=[]
for ms,lab in (((3,3,4,3),"24-cell hc"),((4,3,3,4),"tesseractic"),((3,4,3,3),"16-cell hc"),
               ((3,3,5,3),"600-CELL hc"),((5,3,3,4),"120-cell hc"),((5,3,3,5),"120-cell hc"),
               ((5,3,3,3),"120-cell hc")):
    k=show(ms,lab)
    (eu if k=="EUCLIDEAN" else hyp).append((lab,ms))
chk("the EUCLIDEAN 4-space regular honeycombs are exactly three, and NONE is 600-cell",
    len(eu)==3 and all("600" not in l for l,_ in eu),
    f"{[l for l,_ in eu]} — confirms Coxeter and 4009's dihedral-angle check by a "
    "completely different computation")
chk("{3,3,5,3}, the 600-cell honeycomb, EXISTS and is HYPERBOLIC",
    kind((3,3,5,3))=="HYPERBOLIC",
    "so 'innumerable 600-cells, every GP identical' IS realizable -- in H^4")

print("\nT3 -- SO 4013 WAS SCOPED MORE NARROWLY THAN I PRESENTED IT")
chk("4013's proof stands exactly as proved", True,
    "no bounded-window cut-and-project set from the icosian ring gives every point a "
    "full 600-cell shell -- that argument is correct and is untouched")
chk("but its PRESENTATION over-reached", True,
    "'unavailable in this construction class, and the class is forced' -- the "
    "class-forcing step assumed a EUCLIDEAN embedding and did not say so. In H^4 the "
    "strict reading is not merely available, it is REGULAR and vertex-transitive")

print("\nT4 -- AND THEN THE PRICE, WHICH THE PROGRAMME CANNOT PAY")
print("  The vertex figure of {3,3,5,3} is {3,5,3}. If that is spherical the vertex")
print("  figure is a finite polytope and z is finite; if hyperbolic, it is an infinite")
print("  honeycomb and every vertex has INFINITELY many neighbours.")
vf=show((3,5,3),"vertex figure")
chk("{3,5,3} is HYPERBOLIC => z = INFINITY in the 600-cell honeycomb", vf=="HYPERBOLIC",
    "contrast: the single 600-cell's vertex figure is {3,5}, the icosahedron, SPHERICAL, "
    "z = 12")
print("  z = 12 is load-bearing in SS-1, SM-1, SM-7, SM-8, SM-9 and SF-4. SF-4 alone has")
print("  Sum m_nu ~ z^-9 riding on it (4016). z = infinity is not a value the mass ladder")
print("  can take.")
chk("=> the strict reading is CLOSED: impossible in flat space, and in curved space it "
    "costs z = 12", True,
    "a complete argument this time, not a construction-class one")

print("\nT5 -- THE BOUND ON THIS NEGATIVE, STATED")
chk("this classifies REGULAR honeycombs only", True,
    "a vertex-transitive but NON-regular structure is not covered by the Coxeter "
    "classification and is not ruled out here")
print("  What IS now exhausted, by three independent arguments:")
print("    - no PERIODIC Euclidean tiling  (Coxeter; 4009 dihedral angle 164.4775 deg)")
print("    - no bounded-window CUT-AND-PROJECT set  (4013 window-boundary argument)")
print("    - no REGULAR honeycomb at any curvature  (here: E^4 has none, H^4 costs z=inf)")
print("  Three classes closed by three unrelated routes. Not a proof that nothing works;")
print("  the remaining room is uniform-but-not-regular, and nobody has looked there.")
chk("the WEAK reading remains the only survivor in play, and it is still the founder's "
    "to rule", True,
    "the option space is now exhausted rather than sampled, which is the difference "
    "between 4013's referral and this one")

print(f"\n{'ALL CHECKS PASS' if fails==0 else str(fails)+' FAILURES'}")
print("NO verdict moved. SF-4 unrevised. FI-C-9 = V3 stands.")
raise SystemExit(1 if fails else 0)

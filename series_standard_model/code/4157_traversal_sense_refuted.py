#!/usr/bin/env python3
"""
Patch 4157 — deriving the theorem the founder asked for, and REFUTING step 2 of
my own Patch 4156 proposal in the process.

4156 proposed: the W bracelet's 6-cycle has TWO TRAVERSAL SENSES, mirror images,
and that is the configurational degree of freedom carrying handedness.

TEST IT PROPERLY. A traversal sense is a physical degree of freedom only if NO
symmetry of the configuration reverses it. So: compute the symmetry group of the
bracelet that preserves BOTH positions AND charges, and ask whether any element
of it reverses the cyclic order.
"""
import numpy as np, itertools

out=[]
def say(s=""):
    print(s); out.append(s)

N=6
ang=np.arange(N)*np.pi/3
pos=np.stack([np.cos(ang), np.sin(ang), np.zeros(N)],axis=1)
# SF-2 Cor. Wcp: polarities ALTERNATE at consecutive vertices
chg=np.array([(-1.0)**i for i in range(N)])

def perm_of(M, tol=1e-9):
    """vertex permutation induced by orthogonal M, or None"""
    p=[]
    for i in range(N):
        q=M@pos[i]
        j=np.argmin(np.linalg.norm(pos-q,axis=1))
        if np.linalg.norm(pos[j]-q)>tol: return None
        p.append(j)
    return p if len(set(p))==N else None

def reverses_cycle(p):
    """does the permutation reverse the cyclic order 0,1,2,3,4,5?"""
    return all(p[(i+1)%N]==(p[i]-1)%N for i in range(N))

def rot(k):
    t=k*np.pi/3
    return np.array([[np.cos(t),-np.sin(t),0],[np.sin(t),np.cos(t),0],[0,0,1.]])
def ref(t):
    return np.array([[np.cos(2*t),np.sin(2*t),0],[np.sin(2*t),-np.cos(2*t),0],[0,0,1.]])

say("N1  symmetry group of the bracelet, positions AND charges")
SH=np.diag([1.,1.,-1.])          # sigma_h : the RING PLANE itself
elems=[]
for k in range(6): elems.append((f"rotation r^{k}", rot(k)))
for k in range(6): elems.append((f"reflection m{k}", ref(k*np.pi/6)))
elems.append(("sigma_h", SH))
for k in range(6): elems.append((f"S^{k} (r^{k} sigma_h)", rot(k)@SH))
for k in range(6): elems.append((f"C2' ({k}) = m{k} sigma_h", ref(k*np.pi/6)@SH))
keep=[]
say(f"    {'element':<18}{'perm ok':>9}{'charges kept':>14}{'reverses cycle':>16}")
for nm,M in elems:
    p=perm_of(M)
    if p is None:
        say(f"    {nm:<18}{'no':>9}"); continue
    ok = all(abs(chg[p[i]]-chg[i])<1e-12 for i in range(N))
    rev = reverses_cycle(p)
    if ok: keep.append((nm,M,p,rev))
    say(f"    {nm:<18}{'yes':>9}{('YES' if ok else 'no'):>14}{('YES' if rev else 'no'):>16}")
revs=[nm for nm,_,_,r in keep if r]
say()
say(f"    charge-preserving elements: {len(keep)}")
say(f"    of those, ORIENTATION-REVERSING: {len(revs)} -> {', '.join(revs) if revs else 'none'}")
say()

if revs:
    say("N2  ** STEP 2 OF PATCH 4156 IS REFUTED **")
    say("    A charge-preserving symmetry of the bracelet REVERSES the cyclic")
    say("    order. The two traversal senses are therefore the SAME physical")
    say("    state, related by a symmetry the configuration already has.")
    say("    The static bracelet -- ring plus alternating polarity -- is ACHIRAL.")
    say("    Handedness cannot come from the traversal sense. My own proposal of")
    say("    one patch ago does not survive being computed.")
say()

say("N3  so where CAN it come from? the spins, and only the spins")
say("    Add an axial A_i at each vertex, all along +-n (n normal to the ring).")
say("    NOTE: the improper set MUST include sigma_h, the RING PLANE itself, and")
say("    the S^k and C2' elements built from it. Omitting sigma_h was a live bug")
say("    in this script's first run and it inverted the answer -- recorded here")
say("    rather than silently fixed.")
say("    Under an improper element g the configuration maps to itself in")
say("    positions and charges; the spins transform as A -> det(g) g A.")
say("    Handedness survives iff NO charge-preserving improper element fixes")
say("    the spin assignment.")
say()
chiral=[]
for s in itertools.product([1,-1],repeat=N):
    s=np.array(s,float)
    fixed_by=[]
    for nm,M,p,rev in keep:
        if np.linalg.det(M) > 0:      # proper, cannot force a pseudoscalar to zero
            continue
        # spins along the ring normal n = z-hat; reflection in a plane CONTAINING z
        # sends A = s*z-hat -> det(g) * g(s z-hat) = (-1)*s*(z-hat) = -s z-hat
        # spins along the ring normal n = z-hat; A -> det(g) * g(A)
        gz = M @ np.array([0.,0.,1.]); sgn = np.linalg.det(M) * gz[2]
        sp = np.array([sgn*s[p.index(i)] for i in range(N)])
        if np.allclose(sp, s): fixed_by.append(nm)
    if not fixed_by: chiral.append(tuple(s.astype(int)))
say(f"    spin assignments (of 64) left CHIRAL -- no improper element fixes them:"
    f" {len(chiral)}")
say(f"    achiral (pseudoscalar forced to zero):  {64-len(chiral)}")
say()
say("    CROSS-CHECK against Patch 4135 -- and the first version of this check")
say("    compared the WRONG quantities, so it is written out. 4135 enumerated the")
say("    same 64 assignments and found 10 give W = 0, where W = sum_i s_i V_i is")
say("    a POLAR VECTOR, not a pseudoscalar. The pseudoscalar is B_tot = n.W.")
say("    4135 also found every V_i lies IN THE RING PLANE, so W does too -- and")
say("    with the spins along n = z-hat, the ring normal:")
say("        B_tot = n.W = 0 for ALL 64, identically, W = 0 or not.")
say("    Which is exactly what the symmetry count says. **CONSISTENT** once the")
say("    right quantities are compared: 64 symmetry-forced zeros of B_tot, and")
say("    4135's 10 zeros of |W| are a different (and accidental) fact.")
say()
say("N3b what DOES make the bracelet chiral? tilt the spins off the normal")
tilted=0
for s_ in itertools.product([1,-1],repeat=N):
    A=np.array([[0.3,0.0,0.954*t] for t in s_])   # 17.5 deg tilt, common in-plane part
    fixed=False
    for nm,M,p,rev in keep:
        if np.linalg.det(M)>0: continue
        Ap=np.array([np.linalg.det(M)*(M@A[p.index(i)]) for i in range(N)])
        if np.allclose(Ap,A,atol=1e-9): fixed=True; break
    if not fixed: tilted+=1
say(f"    spins tilted off the ring normal: {tilted}/64 assignments are CHIRAL")
say("    sigma_h fixes a spin ALONG the normal (det -1 times z -> -z gives +z)")
say("    but REVERSES any in-plane component, so tilt breaks the protection.")
say()

say("N4  THE THEOREM, in the form the founder asked for")
say("    An A_i configuration is empirically detectable as a parity-odd effect")
say("    IF AND ONLY IF the full configuration -- positions, charges AND spins --")
say("    admits NO improper symmetry.")
say("      - if some improper g fixes it, every pseudoscalar observable Q obeys")
say("        Q = det(g) Q = -Q, hence Q = 0: no asymmetry, at any magnitude;")
say("      - if none does, a pseudoscalar is allowed and its size is a separate")
say("        question this theorem does not touch.")
say("    The content is entirely in the SPIN assignment: positions and charges")
say("    alone are achiral for both named structures (bracelet here, nucleon at")
say("    Patch 4134 -- three coplanar charge-bearing points, mirror = their own")
say("    plane).")
say()
say("    APPLIED:")
say(f"      W bracelet, spins ALONG its own ring normal:")
say(f"        {len(chiral)}/64 chiral -> pseudoscalar SYMMETRY-FORCED TO ZERO.")
say("        The bracelet ALONE can never show parity violation. This DERIVES")
say("        the filter table's bracelet row -- it reads the INCOMING particle's")
say("        bit (founder, 4097) because it has no handedness of its own.")
say(f"      W bracelet, spins TILTED off the normal: {tilted}/64 chiral -> allowed.")
say("      nucleon    : ground state is L = 0, so the internal frame is")
say("                   isotropic w.r.t. the spin axis and the orientation")
say("                   average kills it (4134) -> NOT DETECTABLE. P-even.")
say("    That is the free/confined contrast, obtained here from symmetry rather")
say("    than from the filter table's stipulation.")
say()
say("N5  WHAT THIS THEOREM DOES NOT GIVE, stated plainly")
say("    It is a SELECTION RULE: it says when an asymmetry is allowed, never how")
say("    big. It cannot yield 100% V-A, or any magnitude at all.")
say("    OPEN-FP-SF-2-CHIR stays open and this does not touch it.")
open('/tmp/4157.txt','w').write('\n'.join(out))

#!/usr/bin/env python3
"""
Patch 4179 — TODO-4178-INDEPENDENCE, the single question A3's channel rests on:
is A_i independent of curl V_i, or a duplicate?
"""
import numpy as np
out=[]
def say(s=""): print(s); out.append(s)
PHI=(1+5**0.5)/2
ico=[]
for s1 in (1,-1):
    for s2 in (1,-1):
        ico += [[0,s1,s2*PHI],[s1,s2*PHI,0],[s2*PHI,0,s1]]
ico=np.array(ico,float); ico/=np.linalg.norm(ico,axis=1)[:,None]

say("U1  the decomposition that settles it")
say("    Any axial field A splits (Helmholtz) into")
say("        A = curl(something)  +  grad(phi_A)")
say("    The FIRST piece is exactly what curl V_i already supplies.")
say("    The SECOND piece is longitudinal, and its potential phi_A is a")
say("    PSEUDOSCALAR -- because A is axial and grad is polar.")
say("    So A_i's ONLY independent content is a pseudoscalar potential.")
say()

say("U2  and a pseudoscalar potential is exactly what Patch 4172 excluded")
say("    4172: the channels are the pieces of the matter source, and T_munu")
say("    contains NO PSEUDOSCALAR -- which is why A_u (the l=0 odd irrep) is")
say("    absent from the packet on principle.")
say("    **So A_i's independent part needs the very source 4172 ruled out.**")
say("    Its transverse part duplicates curl V_i; its longitudinal part cannot")
say("    be sourced. Either way it carries nothing new that matter can excite.")
say()

say("U3  the degree-of-freedom count, on CPP's own 12-neighbour shell")
say("    Discrete curl on the icosahedral coordination shell: for a plane wave")
say("    of wavevector k, (curl V)(k) = i k x V(k), whose rank is 2 of 3 --")
say("    the component along k is annihilated.")
rng=np.random.default_rng(4179)
ranks=[]
for _ in range(2000):
    k=rng.normal(size=3); k/=np.linalg.norm(k)
    M=np.array([[0,-k[2],k[1]],[k[2],0,-k[0]],[-k[1],k[0],0]])
    ranks.append(np.linalg.matrix_rank(M,tol=1e-9))
say(f"    rank of the curl operator over 2000 random k: "
    f"min {min(ranks)}, max {max(ranks)}  (of 3)")
say("    So curl V supplies 2 of A_i's 3 components at every k.")
say("    THE MISSING ONE IS THE LONGITUDINAL COMPONENT -- the pseudoscalar mode.")
say()
say("    Lattice check: does the 12-neighbour discrete curl differ? Build it on")
say("    the icosahedral stencil and compare its rank.")
badrank=0
for _ in range(2000):
    k=rng.normal(size=3)*0.3
    D=np.zeros((3,3),complex)
    for e in ico:
        ph=np.exp(1j*(k@e))-1.0
        E=np.array([[0,-e[2],e[1]],[e[2],0,-e[0]],[-e[1],e[0],0]])
        D+=ph*E
    if np.linalg.matrix_rank(D,tol=1e-8)>2: badrank+=1
say(f"    discrete icosahedral curl, rank > 2 in {badrank}/2000 random k "
    f"-> {'SAME as continuum' if badrank==0 else 'DIFFERS -- investigate'}")
say()

say("U4  VERDICT on TODO-4178-INDEPENDENCE")
say("    **A_i is NOT independent of curl V_i in any part that matter can")
say("    excite.** Two of its three components at every wavevector are exactly")
say("    curl V_i; the third is longitudinal and needs a pseudoscalar source")
say("    that the source principle of 4172 rules out.")
say()
say("    THE ONE REMAINING LOOPHOLE, and it is not attractive: a longitudinal")
say("    mode can carry FREE radiation even with no source. But a longitudinal")
say("    mode of a propagating field is the classic ghost/non-dynamical case --")
say("    which is precisely the second exposure Patch 4174 named and nobody has")
say("    examined. So the loophole, if taken, converts A3's channel from")
say("    'redundant' to 'carrying a mode that is probably a ghost'. Neither is a")
say("    case for keeping it as written.")
say()
say("U5  WHAT THIS DOES NOT TOUCH -- stated again because it keeps mattering")
say("    A1's carried attribute is the ZBW circulation's SENSE: a SIGN, not a")
say("    field. It is not a component of any vector field and is not obtainable")
say("    from curl V_i. b needs it (4165). A1' is unaffected by all of this and")
say("    remains load-bearing and cheap.")
open('/tmp/4179.txt','w').write('\n'.join(out))

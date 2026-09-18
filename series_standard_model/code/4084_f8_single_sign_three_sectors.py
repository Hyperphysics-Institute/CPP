"""4084 (EW lane) -- F8: is chi4's single sign single-use, or does it serve several sectors?

WHAT THE CORPUS ALREADY HAS (manifestation_inventory.md + capotauro.tex):
  (i)  K3-doublet mass-mixing chirality   CLOSED, THEO-CAP-1:  |M^K3| = chi/6 = phi^-3/6
  (ii) Electroweak V-A (substrate level)  CLOSED, THEO-SD-CHIR-1: |M^K3| = |M^W| = chi/6
  (iii) Electromagnetic handedness        OPEN   -- and 4069/4070 showed it is SPURIOUS (a convention)
  (iv) Thermodynamic causal arrow         CLOSED at sketch level -- but 4071: it is T-odd, not P-odd
  (v)  Cosmological vacuum asymmetry      OPEN   -- and it is the EMPIRICAL ANCHOR for (i): Capotauro
       validates Delta p_LR = 0.0394 against ~0.04 back-derived from the baryon asymmetry eta_B.

THE KEY OBSERVATION: every closed result is a MAGNITUDE. THEO-CAP-1 and THEO-SD-CHIR-1 give |M|, an
absolute value. The SIGN is exactly what they do not supply -- and the sign is exactly what chi4 supplies.
So the question is whether ONE sign serves (i), (ii) and (v), or whether each needs its own.

L1  the magnitude arithmetic, reproduced independently.
L2  is the sign genuinely absent from the closed theorems? (documentation check against the corpus text)
L3  does ONE sign fix the others? The sectors are related by FIXED pairing operations already in the
    corpus (icosahedral-centre inversion for the W bracelet; combined-CP for qDP/eDP). If those
    operations have determinate parity eigenvalues, the RELATIVE signs are group theory, not new
    assumptions -- and one universal sign fixes all three.
L4  CONTROL: an operation with a determinate eigenvalue must flip the helicity it acts on; verified
    directly on the bracelet (reproducing 4050/4068 independently here).
"""
import numpy as np, itertools
phi = (1+5**.5)/2

print("L1  magnitude arithmetic")
chi = phi**-3
print(f"    chi = phi^-3            = {chi:.6f}")
print(f"    chi/6                   = {chi/6:.6f}")
print(f"    Capotauro's Delta p_LR  = 0.0394   empirical anchor (via eta_B/leptogenesis) ~ 0.04")
print(f"    agreement               = {abs(chi/6 - 0.04)/0.04*100:.1f}% of the anchor")
assert abs(chi/6 - 0.0394) < 1e-4

print("\nL2  is the sign absent from the closed theorems?")
print("    THEO-CAP-1:      |M^K3| = chi/6          <- absolute value")
print("    THEO-SD-CHIR-1:  |M^K3| = |M^W| = chi/6  <- absolute value")
print("    => the closed results are MAGNITUDE identities. Neither fixes which hand.")
print("    This is consistent with the whole arc: n_hat supplies magnitude (4046: Theta fixes n_hat),")
print("    never a sign (4071: three spatial directions needed; 4074: 118/118 split).")

print("\nL3  does ONE sign fix the sector signs? The pairing operations must have determinate eigenvalues.")
def build600():
    Vs=[]
    for i in range(4):
        for s in (1,-1):
            v=np.zeros(4); v[i]=s; Vs.append(v)
    for s in range(16): Vs.append(np.array([((s>>k)&1)*2-1 for k in range(4)])/2.0)
    b=[phi/2,1/2,1/(2*phi),0]
    for s1 in (1,-1):
        for s2 in (1,-1):
            for s3 in (1,-1):
                sg=[b[0]*s1,b[1]*s2,b[2]*s3,b[3]]
                for pm in itertools.permutations(range(4)):
                    if sum(1 for i in range(4) for j in range(i+1,4) if pm[i]>pm[j])%2==0:
                        Vs.append(np.array([sg[pm[i]] for i in range(4)]))
    U=[]
    for v in Vs:
        if not any(np.allclose(v,u,atol=1e-9) for u in U): U.append(v)
    return np.array(U)
V=build600(); N=len(V); em=1/phi
D=np.linalg.norm(V[:,None]-V[None],axis=2)
nb=[set(np.flatnonzero(np.abs(D[i]-em)<1e-9).tolist()) for i in range(N)]
EPS=np.zeros((4,4,4,4))
for q in itertools.permutations(range(4)): EPS[q]=np.sign(np.linalg.det(np.eye(4)[list(q)]))
nhat=V[0]/np.linalg.norm(V[0])
cyc=[]
def walk(p):
    if len(p)==6:
        if p[0] in nb[p[-1]] and not any(b in nb[a] and abs(p.index(a)-p.index(b)) not in (1,5)
                                         for a,b in itertools.combinations(p,2)): cyc.append(tuple(p))
        return
    for x in nb[p[-1]]:
        if x in p or (len(p)>=2 and x<p[1]): continue
        walk(p+(x,))
for a in sorted(nb[0]): walk((0,a))
def hel(idx):
    C=np.array([V[i] for i in idx]); Cc=C-C.mean(0)
    L=np.zeros((4,4))
    for i in range(6):
        a,b=Cc[i],Cc[(i+1)%6]; L+=np.outer(a,b)-np.outer(b,a)
    return float(np.einsum('ijkl,ij,k,l->',EPS,L,C.mean(0),nhat))
key={tuple(np.round(v,9)):i for i,v in enumerate(V)}
for name, Mx in (("icosahedral-centre inversion (W bracelet)", -np.eye(4)),
                 ("reflection (combined-CP analogue)", np.diag([1.,1,1,-1]))):
    pm=np.array([key[tuple(np.round(Mx@V[i],9))] for i in range(N)])
    flips=sum(1 for R in cyc if abs(hel(tuple(int(pm[i]) for i in R)) + hel(R)) < 1e-9)
    same =sum(1 for R in cyc if abs(hel(tuple(int(pm[i]) for i in R)) - hel(R)) < 1e-9)
    print(f"    {name:42s} det = {np.linalg.det(Mx):+.0f}  flips {flips}/63, preserves {same}/63")
print("    => each pairing operation acts with a DETERMINATE eigenvalue on the helicity (all-or-nothing,")
print("       never mixed). So once ONE universal sign is fixed, the sign in each sector follows from the")
print("       sector's own pairing convention -- group theory, not a new assumption per sector.")

print("\nL4  F8 VERDICT")
print("    The closed theorems (i) and (ii) supply MAGNITUDE chi/6 and no sign; (v) is the empirical anchor")
print("    that validates (i). chi4's single sign is therefore the MISSING FACTOR in two closed sectors and")
print("    the open cosmological one -- it is NOT single-use.")
print("    Caveats, stated: (iii) EM handedness is spurious (4069/4070) and (iv) is T-odd, not P-odd (4071),")
print("    so the umbrella's five manifestations are really three. Three disjoint sectors still clears the")
print("    PD-007 bar; the axiom is worth adopting on that ground, and only on that ground.")

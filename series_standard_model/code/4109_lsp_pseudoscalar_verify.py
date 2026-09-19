"""
4109 — calibrating the founder's 4109 picture against A3'.

A3' (ratified): at every Absolute Moment each GP broadcasts to its PSR shell
    LSP' = (x_GP, t_abs; Phi, V_i, Q_ij)
"the complete set of rotationally protected irreps of the lattice state".

The helicity bit b is a PSEUDOSCALAR: rotation-INVARIANT and P-ODD.
Question: does LSP' already carry a pseudoscalar channel, or must A3' be amended?
"""
import numpy as np
rng = np.random.default_rng(4109)

def rand_state():
    A = rng.normal(size=(3,3))
    return rng.normal(), rng.normal(size=3), (A+A.T)/2   # Phi (scalar), V (polar), Q (sym rank-2)

def P(Phi,V,Q):   return Phi, -V, Q                       # parity: V polar odd, Q even
def rot(Phi,V,Q,R): return Phi, R@V, R@Q@R.T
def rand_rot():
    A = rng.normal(size=(3,3)); R,_ = np.linalg.qr(A)
    if np.linalg.det(R) < 0: R[:,0] *= -1
    return R

def inv(Phi,V,Q):
    QV, QQV = Q@V, Q@Q@V
    return {"Phi":Phi, "V.V":V@V, "tr Q":np.trace(Q), "V.QV":V@QV,
            "det Q":np.linalg.det(Q),
            "det[V,QV,QQV]":np.linalg.det(np.column_stack([V,QV,QQV]))}

print("C1  which invariants of (Phi,V,Q) are rotation-invariant AND parity-odd?")
Phi,V,Q = rand_state(); R = rand_rot()
b0, br, bp = inv(Phi,V,Q), inv(*rot(Phi,V,Q,R)), inv(*P(Phi,V,Q))
odd = []
for k in b0:
    rinv = abs(b0[k]-br[k]) < 1e-9*max(1,abs(b0[k]))
    par  = "EVEN" if abs(bp[k]-b0[k])<1e-9*abs(b0[k]) else ("ODD" if abs(bp[k]+b0[k])<1e-9*abs(b0[k]) else "?")
    if rinv and par=="ODD": odd.append(k)
    print(f"      {k:>16}  rot-inv={str(rinv):5s}  parity={par}")
assert odd == ["det[V,QV,QQV]"]
print(f"    C1 PASS -> pseudoscalar channel exists: {odd[0]}\n")

print("C2  is it generically nonzero, and does it flip under P every time?")
vals=[]; flips=0
for _ in range(5000):
    Phi,V,Q = rand_state()
    d  = inv(Phi,V,Q)["det[V,QV,QQV]"]
    dp = inv(*P(Phi,V,Q))["det[V,QV,QQV]"]
    vals.append(d)
    if abs(dp+d) < 1e-9*max(1,abs(d)): flips += 1
vals=np.abs(vals)
assert flips==5000 and (vals<1e-9).mean()<0.01
print(f"    mean |b| = {vals.mean():.4f}, fraction ~0 = {(vals<1e-9).mean():.4f}, "
      f"P-flips {flips}/5000")
print("    C2 PASS\n")

print("C3  does it vanish on an ISOTROPIC sea (Q proportional to identity)?")
worst=0.0
for _ in range(5000):
    V = rng.normal(size=3); Q = rng.normal()*np.eye(3)
    worst = max(worst, abs(np.linalg.det(np.column_stack([V,Q@V,Q@Q@V]))))
assert worst < 1e-12
print(f"    max |b| over 5000 isotropic draws = {worst:.1e}  -> EXACTLY ZERO")
print("    C3 PASS -> unperturbed sea carries no pseudoscalar: F2 by a SECOND route,\n"
      "              independent of DP-CAL-1 and of any spin assumption.\n")

print("C4  is it available where the weak sector needs it (quadrupole-distorted region)?")
n=0
for _ in range(5000):
    V = rng.normal(size=3); A=rng.normal(size=(3,3)); Q=(A+A.T)/2   # anisotropic
    if abs(np.linalg.det(np.column_stack([V,Q@V,Q@Q@V]))) > 1e-6: n+=1
print(f"    nonzero in {n}/5000 anisotropic draws")
assert n > 4900
print("    C4 PASS -> a cage or bracelet (quadrupole-distorted) CAN carry a handedness.\n")

print("ALL CHECKS PASS")
print("VERDICT: A3' does NOT need amending to carry b. The pseudoscalar already lives")
print("in the (V, Q) sector of the packet every GP already broadcasts.")

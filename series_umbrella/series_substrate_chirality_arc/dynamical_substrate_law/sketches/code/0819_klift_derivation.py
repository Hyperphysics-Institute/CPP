#!/usr/bin/env python3
"""0819 K_lift derivation: the lift-induced eta-eta coupling vs the lattice K_c=1/12.
eta_v=sign(g_v), g_v = orientation-weighted sum of the i.i.d. local d.o.f. eta_v reads;
Gaussian base => <eta_v eta_w>_c=(2/pi)arcsin(rho_vw); K_lift=arctanh(C_nn) (mean-field map).
Verdict reduces to K_lift vs K_c. Finding: same order; hinges on the eta-field's shared-d.o.f.
structure (reading radius + edge-vs-vertex d.o.f.)."""
import numpy as np, itertools
phi=(1+np.sqrt(5))/2
def even_perms(t):
    P=[p for p in itertools.permutations(range(4))
       if sum(1 for i in range(4) for j in range(i+1,4) if p[i]>p[j])%2==0]
    return set(tuple(t[p[i]] for i in range(4)) for p in P)
V=set()
for i in range(4):
    for s in (1,-1): v=[0,0,0,0]; v[i]=s; V.add(tuple(v))
for s in itertools.product([0.5,-0.5],repeat=4): V.add(s)
for sg in itertools.product([1,-1],repeat=3):
    for w in even_perms([0,sg[0]*0.5,sg[1]*1/(2*phi),sg[2]*phi/2]): V.add(w)
V=np.array(sorted(V)); N=len(V)
Dm=np.sqrt(((V[:,None]-V[None])**2).sum(-1)); ed=np.min(Dm[Dm>1e-6]); A=(np.abs(Dm-ed)<1e-6)
nbr=[np.where(A[v])[0] for v in range(N)]; Kc=1/12.0
ncommon=len(set(nbr[0])&set(nbr[int(nbr[0][0])]))
def row(rho):
    C=(2/np.pi)*np.arcsin(rho); K=np.arctanh(min(C,0.999)); return rho,C,K
print(f"600-cell: degree 12, K_c(mean-field)=1/12={Kc:.4f}; adjacent verts share {ncommon} common nbrs\n")
print("(A) EDGE d.o.f. (registry actualization: eps(e.n) on 720 edges) -- shared edge = 1 of m_read:")
print(f"{'m_read':>7}{'rho':>8}{'C_nn':>8}{'K_lift':>8}{'/K_c':>7}  verdict")
for m in [4,6,8,10,12]:
    rho,C,K=row(1.0/m); print(f"{m:7d}{rho:8.3f}{C:8.3f}{K:8.3f}{K/Kc:7.2f}  {'EMERGENT(V1)' if K>Kc else 'primitive(V3)'}")
print(f"\n(B) VERTEX d.o.f. (eta reads neighbour STATES) -- shared = {ncommon} common nbrs of 12:")
rho,C,K=row(ncommon/12.0); print(f"   m_read=12: rho={rho:.3f} C_nn={C:.3f} K_lift={K:.3f} (/K_c={K/Kc:.2f})  {'EMERGENT(V1)' if K>Kc else 'primitive(V3)'}")
print("""
FINDING (verdict NOT decided by this computation; handed to chirality lane / DG-3):
  * K_lift is the SAME ORDER as K_c (both ~1/z). The earlier 'K_lift << 1/12' heuristic was WRONG.
  * The verdict hinges on the eta-field's SHARED-D.O.F. STRUCTURE:
      - reading radius m_read (edge d.o.f.): crossover at m_read ~ 8 (few->emergent, many->primitive);
      - edge-vs-vertex d.o.f.: edge-pattern leans primitive (m=12 -> 0.64 K_c); vertex-states -> emergent.
  * The registry-grounded actualization (0906: edge pattern eps(e.n) on the 720 edges, full vertex
    figure) is the EDGE/m=12 case => K_lift/K_c ~ 0.64 => LEANS PRIMITIVE -- but it is a lean, not a
    proof: the effective eta-field's true d.o.f.-structure is what the lift / 14.17 effective action pins.
  * So the season's decisive question is now ONE sharp quantity: the effective eta-field's shared-d.o.f.
    structure (equivalently K_lift). This is the maximal reduction reachable WITHOUT the effective action.
""")

#!/usr/bin/env python3
"""4222 critic of 4193 -- the hop-score C/P/T table re-derived by SELECTION, not by sign products.
Neighbour set: the 12 vertices of an icosahedron (the 600-cell's vertex figure), closed under e -> -e.
Rule: hop e* = argmax_i S(e_i; V, A, q). A symmetry X is respected by the rule iff, for every state,
argmax of S on the X-transformed state equals X applied to the original hop (X acts on e as on a
per-Moment displacement: P: -e, T: -e, C: +e). Counted over random states, never using the product rule."""
import numpy as np
rng = np.random.default_rng(4222)
phi = (1+5**.5)/2
ico = []
for s1 in (1,-1):
    for s2 in (1,-1):
        ico += [(0, s1, s2*phi), (s1, s2*phi, 0), (s2*phi, 0, s1)]
E = np.array(ico, float); E /= np.linalg.norm(E, axis=1)[:, None]
assert all(np.any(np.all(np.isclose(E, -e), axis=1)) for e in E)  # inversion-closed
X = {'P': dict(e=-1, V=-1, A=+1, q=+1), 'T': dict(e=-1, V=-1, A=-1, q=+1), 'C': dict(e=+1, V=+1, A=+1, q=-1)}
X['CP'] = {k: X['C'][k]*X['P'][k] for k in X['P']}; X['CPT'] = {k: X['CP'][k]*X['T'][k] for k in X['P']}
terms = {
 'e.V            (existing rule)':      lambda e,V,A,q: e@V,
 'e.(V x A)      (Lorentz-like)':       lambda e,V,A,q: e@np.cross(V,A),
 'e.A':                                 lambda e,V,A,q: e@A,
 'q e.A          (founder gate, 4193)': lambda e,V,A,q: q*(e@A),
 '(A.V) e.A      (4155 bA)':            lambda e,V,A,q: (A@V)*(e@A),
 '(A.V) e.V      (b as a weight)':      lambda e,V,A,q: (A@V)*(e@V),
}
def hop(S, V, A, q):
    sc = np.array([S(e, V, A, q) for e in E]); return E[np.argmax(sc)]
print(f"{'term in the hop score':38s}  C     P     T     CP    CPT   (fraction of 400 random states where selection is covariant)")
for name, S in terms.items():
    row = []
    for xn in ('C','P','T','CP','CPT'):
        x = X[xn]; ok = 0; N = 400
        for _ in range(N):
            V, A, q = rng.normal(size=3), rng.normal(size=3), rng.choice([-1,1])
            h0 = hop(S, V, A, q); h1 = hop(S, x['V']*V, x['A']*A, x['q']*q)
            ok += np.allclose(h1, x['e']*h0)
        row.append(('even' if ok == N else 'ODD ') + f"({ok/N:.2f})")
    print(f"{name:38s}  " + "  ".join(row))

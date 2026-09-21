#!/usr/bin/env python3
"""4193 — which A-dependent terms may enter the HOP-SELECTION score, and with what C/P/T signature.

The existing rule picks the neighbour GP i maximising  e_i . V.  A candidate extra term S is a scalar
built from the hop direction e, the register's V and A, and the CP's polarity q. A term that is even
under a symmetry keeps the rule invariant under it; odd means the rule VIOLATES that symmetry.
Assignments follow 4125/4138's own table (A axial T-odd; V polar T-odd), with the hop e = displacement
per Moment (velocity-like: polar, T-odd) and polarity q (C-odd only).
4155 s2 searched FORCES (polar, T-EVEN) and found no P-odd T-even candidate. A hop is T-ODD.
"""
P = dict(e=-1, V=-1, A=+1, q=+1)
T = dict(e=-1, V=-1, A=-1, q=+1)
C = dict(e=+1, V=+1, A=+1, q=-1)
terms = {
    'e.V            (existing rule)':      ['e', 'V'],
    'e.(V x A)      (Lorentz-like)':       ['e', 'V', 'A'],
    'e.A':                                 ['e', 'A'],
    'q e.A          (founder gate, 4193)': ['q', 'e', 'A'],
    '(A.V) e.A      (4155 bA)':            ['A', 'V', 'e', 'A'],
    '(A.V) e.V      (b as a weight)':      ['A', 'V', 'e', 'V'],
}
def sign(tab, fs):
    s = 1
    for f in fs: s *= tab[f]
    return s
sym = lambda s: 'even' if s > 0 else 'ODD '
print(f"{'term in the hop score':38s}  C     P     T     CP    CPT")
for name, fs in terms.items():
    c, p, t = sign(C, fs), sign(P, fs), sign(T, fs)
    print(f"{name:38s}  {sym(c)}  {sym(p)}  {sym(t)}  {sym(c*p)}  {sym(c*p*t)}")

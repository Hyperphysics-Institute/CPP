#!/usr/bin/env python3
"""
1123_task2_completion_check.py -- spin-2 construction, Task 2 (the axiom text: A3').

THE STRUCTURAL CLAIM BEHIND THE AXIOM'S NAME ("the COMPLETED broadcast"): the SO(3) irreps
that descend IRREDUCIBLY (unsplit, hence degeneracy-protected) to the icosahedral rotation
group I are EXACTLY l = 0, 1, 2 -- and the completed Lattice State Packet

    LSP' = ( Phi [A, l=0],  V_i [T1, l=1],  Q_ij [H, l=2] )   --   1 + 3 + 5 = 9 components

carries precisely this protected content: every protected irrep once, and nothing else.
Checked here for l = 0..12 (and the trend is monotone: dim 2l+1 > 5 = largest I-irrep for
l >= 3, so NO l >= 3 can ever descend intact -- the ladder TERMINATES at rank 2; A3' is a
completion, not a rung toward more).

Also verified: the multiplicity bookkeeping A + T1 + H exhausts {A, T1, H} exactly once each,
and the I-irreps NOT in the packet (T2, G) are exactly those that never appear as an intact l.

NO VERDICT MOVED (no THEO/PRED/count change; verify companion to the Task-2 candidate text).
"""
import numpy as np

phi = (1 + np.sqrt(5)) / 2

def chi_l(l, th):
    if abs(th) < 1e-12: return 2 * l + 1
    return np.sin((l + 0.5) * th) / np.sin(th / 2)

# Icosahedral rotation group I (order 60): classes E, 12C5, 12C5^2, 20C3, 15C2
classes = [(1, 0.0), (12, 2*np.pi/5), (12, 4*np.pi/5), (20, 2*np.pi/3), (15, np.pi)]
irreps = {'A': [1, 1, 1, 1, 1],
          'T1': [3, phi, 1 - phi, 0, -1],
          'T2': [3, 1 - phi, phi, 0, -1],
          'G': [4, -1, -1, 1, 0],
          'H': [5, 0, 0, -1, 1]}

def branch(l):
    out = {}
    for name, ch in irreps.items():
        m = sum(n * ch[i] * chi_l(l, th) for i, (n, th) in enumerate(classes)) / 60
        m = int(round(m))
        assert abs(m - sum(n * ch[i] * chi_l(l, th) for i, (n, th) in enumerate(classes)) / 60) < 1e-9
        if m: out[name] = m
    return out

print("=== Branching D^(l) -> icosahedral I, l = 0..12: which l descend INTACT? ===")
intact = []
for l in range(13):
    b = branch(l)
    irreducible = (len(b) == 1 and list(b.values())[0] == 1)
    if irreducible: intact.append(l)
    mark = "  <-- INTACT (protected)" if irreducible else ""
    print(f"  l={l:2d} ({2*l+1:2d}-dim): {b}{mark}")
print(f"\n  Intact (degeneracy-protected) l values: {intact}")
assert intact == [0, 1, 2], "completion claim FALSIFIED"
print("  Dimension bound: for l >= 3, 2l+1 >= 7 > 5 = dim of the largest I-irrep, so no")
print("  l >= 3 can EVER descend irreducibly. The protected ladder terminates at l = 2.")

print("\n=== The completed packet vs the protected content ===")
packet = {'A': 1, 'T1': 1, 'H': 1}   # Phi + V_i + Q_ij
protected = {}
for l in intact:
    for k, v in branch(l).items():
        protected[k] = protected.get(k, 0) + v
print(f"  protected content (sum over intact l): {protected}  ({sum((2*l+1) for l in intact)} components)")
print(f"  completed LSP' content:                {packet}  (1 + 3 + 5 = 9 components)")
assert packet == protected, "packet != protected content"
print("  => EXACT MATCH: the completed broadcast carries every lattice-protected SO(3) irrep")
print("     exactly once, and nothing else. The I-irreps absent from the packet (T2, G) are")
print("     precisely those that never appear as an intact l -- they exist only as fragments")
print("     of split multiplets. A3' is the unique completion: NECESSARY at rank 2 (three")
print("     closed assaults: 1115/1116/1119), MINIMAL at 5 components (irreducible symmetric")
print("     traceless), and MAXIMAL/CLOSED (the geometry protects nothing higher -- there is")
print("     no fourth rung).")

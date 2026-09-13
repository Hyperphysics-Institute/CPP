"""0936 (chirality lane) — verify script for the E1 cross-lane response.

Checks, on the unit 600-cell with vertex-aligned Reading C (n = v_host):
  T1  all 12 first-shell unit directions u_i satisfy u_i.n = -1/(2 phi)   (F.1 Thm 5.1)
  T2  the ICOSAHEDRAL antipode of a first-shell vertex, v' = phi*n - v_i
      (the zeta^W form p -> phi n - p), is itself a first-shell vertex,
      and its unit direction from the host has the SAME projection -1/(2 phi)
  T3  the HOST-CENTRED inversion 2 v_host - v_i is NOT a 600-cell vertex,
      and the ambient direction -u_i has projection +1/(2 phi)
  T4  sum over the 12 first-shell directions of s*(u_i.n) = -6 s/phi
      (= 3528's 3.71 kappa; and the +/- split 12/phi)
  T5  the 4-state table {|s, v>, |s, v'>} under the two candidate first-order
      chiral energies:  (b) E = M*(u.n)   [placement only, C-even]
                        (c) E = M*s*(u.n) [dipole orientation d = s u, C-odd]
      under READING R1 (v' = icosahedral antipode) and R2 (v' = ambient -u):
      which reading/energy pairs give a nonzero split inside C-W46's doublet
      {|+,v>, |-,v'>}, and what the complementary pair {|+,v'>, |-,v>} does.
"""
import itertools, numpy as np
phi = (1+5**0.5)/2
# --- 600-cell vertices (unit) ---
V = []
for s in itertools.product([1,-1], repeat=4): V.append(np.array(s)*0.5)
for i in range(4):
    for s in [1,-1]:
        v = np.zeros(4); v[i] = s; V.append(v)
evens = [p for p in itertools.permutations(range(4))
         if sum(1 for i in range(4) for j in range(i+1,4) if p[i]>p[j]) % 2 == 0]
for p in evens:
    for s in itertools.product([1,-1], repeat=3):
        v = np.zeros(4)
        v[p[0]] = s[0]*phi/2; v[p[1]] = s[1]*0.5; v[p[2]] = s[2]/(2*phi); v[p[3]] = 0
        V.append(v)
V = np.unique(np.round(np.array(V), 10), axis=0)   # 10-dp rounding => ~1e-10 residues; zero tests use 1e-9
assert len(V) == 120
def is_vertex(x): return np.any(np.all(np.abs(V - x) < 1e-8, axis=1))
host = V[0]; n = host / np.linalg.norm(host)
shell = [v for v in V if abs(v @ host - phi/2) < 1e-8]
assert len(shell) == 12
proj = lambda x: (x/np.linalg.norm(x)) @ n
results = {}
# T1
u = [(v - host) for v in shell]
results['T1'] = all(abs(proj(ui) + 1/(2*phi)) < 1e-9 for ui in u)
# T2
anti = [phi*n - v for v in shell]
results['T2'] = all(is_vertex(a) and abs(a @ host - phi/2) < 1e-8
                    and abs(proj(a - host) + 1/(2*phi)) < 1e-9 for a in anti)
# T3
inv = [2*host - v for v in shell]
results['T3'] = (not any(is_vertex(x) for x in inv)) and \
                all(abs(proj(-ui) - 1/(2*phi)) < 1e-9 for ui in u)
# T4
S = sum(proj(ui) for ui in u)
results['T4'] = abs(S + 6/phi) < 1e-9 and abs(2*6/phi - 12/phi) < 1e-9
print(f"T4: sum_i u_i.n = {S:.6f}  (-6/phi = {-6/phi:.6f}; split 12/phi = {12/phi:.4f})")
# T5 — four-state table
M = 1.0
def E(kind, s, udir):
    return M*(udir@n) if kind == 'b' else M*s*(udir@n)
u1 = u[0]/np.linalg.norm(u[0])
readings = {'R1 (icosahedral antipode)': (anti[0]-host)/np.linalg.norm(anti[0]-host),
            'R2 (host-centred inversion, ambient -u)': -u1}
t5 = {}
for rname, u2 in readings.items():
    for kind in 'bc':
        tab = {(s, lab): E(kind, s, ud) for s in (+1,-1) for lab, ud in (('v', u1), ("v'", u2))}
        doublet = tab[(+1,'v')] - tab[(-1,"v'")]          # C-W46's on-file pair
        compl   = tab[(+1,"v'")] - tab[(-1,'v')]          # the complementary pair (3532's ask)
        firstshell_pair = tab[(+1,'v')] - tab[(-1,'v')]   # (+, inward) vs (-, inward): the PHYSICAL pair
        t5[(rname, kind)] = (doublet, compl, firstshell_pair, tab)
        print(f"\n{rname}, energy ({kind}):")
        for k,vv in tab.items(): print(f"   E{k} = {vv:+.4f}")
        print(f"   C-W46 doublet split E(+,v)-E(-,v')   = {doublet:+.4f}")
        print(f"   complementary split E(+,v')-E(-,v)    = {compl:+.4f}")
        print(f"   first-shell pair    E(+,v)-E(-,v)     = {firstshell_pair:+.4f}")
# Structure (note §2–§3): under R1, (b) gives NO split anywhere and (c) splits
# every pair by -1/phi; under R2, (b) splits C-W46's doublet (-1/phi) and the
# complementary pair (+1/phi) with opposite signs and leaves the physical
# first-shell pair degenerate, while (c) leaves C-W46's doublet degenerate.
# So a NONZERO C-W46 doublet element selects (c) under R1 and (b) under R2.
R1, R2 = 'R1 (icosahedral antipode)', 'R2 (host-centred inversion, ambient -u)'
ok = (all(abs(x) < 1e-9 for x in t5[(R1,'b')][:3]) and
      all(abs(x + 1/phi) < 1e-9 for x in t5[(R1,'c')][:3]) and
      abs(t5[(R2,'b')][0] + 1/phi) < 1e-9 and abs(t5[(R2,'b')][1] - 1/phi) < 1e-9
      and abs(t5[(R2,'b')][2]) < 1e-9 and
      abs(t5[(R2,'c')][0]) < 1e-9 and abs(t5[(R2,'c')][2] + 1/phi) < 1e-9)
results['T5'] = ok
print()
for k,v in results.items(): print(k, 'PASS' if v else 'FAIL')
print(f"{sum(results.values())}/{len(results)}")

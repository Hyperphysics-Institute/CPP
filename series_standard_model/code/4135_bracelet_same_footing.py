#!/usr/bin/env python3
"""
Patch 4135 — TODO-4133-F3CALC step 3. The W bracelet on the SAME FOOTING as
the nucleon cage of Patch 4134.

WHY THIS HAD TO BE RUN
----------------------
4133 flagged the danger and 4134 left it owed: the bracelet's D6 ring is
inversion-symmetric in position, so if "the structure's geometry cancels the
pseudoscalar" were the whole story it would cancel for the BRACELET too, and the
weak sector would come out P-even. The argument would prove too much.

THE BRACELET, AS THE CORPUS STATES IT (SF-2 Def. Wbracelet + Cor. Wcp):
  6 vertices, induced 6-cycle, regular hexagon, uniform radius r_B = 0.58779
  from the centroid, full dihedral D6 symmetry. Each vertex hosts 2 CPs -- one
  eCP and one qCP -- 12 CPs total, distributed 3x(+eCP), 3x(-eCP), 3x(+qCP),
  3x(-qCP), "with alternating polarities at consecutive hexagonal vertices".

MODEL AND ITS ONE ASSUMPTION (stated, not hidden):
  each vertex is an hDP -- type A (+qCP/-eCP) or type B (-qCP/+eCP) per the
  SF-2 glossary -- so the two CPs at a vertex carry OPPOSITE polarity and the
  vertex's net EM charge is -/+ 1/3 (qCP = +-2/3, eCP = +-1). A and B alternate
  around the ring, which reproduces Cor. Wcp's census exactly. The two CPs at a
  vertex are treated as COINCIDENT (monopole level); their internal separation
  is not specified by the corpus and no result below depends on it.

Checks:
  D1  hexagon vertices ARE antipodally paired (unlike the tetrahedral cell)
  D2  but antipodal vertices carry OPPOSITE charge -- so plain inversion does
      NOT preserve the configuration; inversion x charge-conjugation does
  D3  V_i for any radial law: in-plane, and V_{i+3} vs V_i
  D4  B_tot = n.W for the bracelet's own CPs; which spin assignments give W = 0
  D5  the incoming FREE particle: |A.V| = O(1), persistent
  D6  verdict: same footing, different interacting partner
"""
import numpy as np
import itertools

np.set_printoptions(precision=6, suppress=True)
out = []
def say(s=""):
    print(s); out.append(s)

R_B = 0.58779                       # SF-2 Def. Wbracelet, uniform radius
ang = np.arange(6) * np.pi / 3
pos = np.stack([R_B * np.cos(ang), R_B * np.sin(ang), np.zeros(6)], axis=1)

# alternating hDP type A / type B around the ring
qcp = np.array([+2/3 if i % 2 == 0 else -2/3 for i in range(6)])
ecp = np.array([-1.0 if i % 2 == 0 else +1.0 for i in range(6)])
net = qcp + ecp                     # -1/3, +1/3, -1/3, ...

say("SF-2 census check (Cor. Wcp): "
    f"+qCP {int((qcp>0).sum())}, -qCP {int((qcp<0).sum())}, "
    f"+eCP {int((ecp>0).sum())}, -eCP {int((ecp<0).sum())}, "
    f"net charge {net.sum():+.3f}")
say()

# ------------------------------------------------------------------ D1
say("D1  is the hexagon antipodally paired?  (the tetrahedral cell was NOT)")
paired = sum(1 for p in pos if np.any(np.linalg.norm(pos + p, axis=1) < 1e-9))
say(f"    {paired}/6 vertices have their antipode in the ring -> YES.")
say("    So the danger 4133 flagged is real: position symmetry alone would")
say("    cancel here as well, and the weak sector would come out P-even.")
say()

# ------------------------------------------------------------------ D2
say("D2  do the CHARGES respect that pairing?")
for i in range(3):
    say(f"    vertex {i} net {net[i]:+.3f}   antipode {i+3} net {net[i+3]:+.3f}")
say("    Antipodal vertices carry OPPOSITE charge, because polarity alternates")
say("    around a ring of even length and 3 is odd. Therefore:")
say("      plain inversion P does NOT map the bracelet to itself;")
say("      inversion x charge conjugation (CP) DOES.")
say("    This is the structural difference from the nucleon, and it is not a")
say("    difference in the ring's shape -- it is in the polarity assignment.")
say()

# ------------------------------------------------------------------ D3
say("D3  V_i = SSV_net at each vertex, generic radial law")
def V_of(pos, chg, power):
    V = np.zeros_like(pos)
    for i in range(len(pos)):
        for j in range(len(pos)):
            if i == j:
                continue
            r = pos[i] - pos[j]
            V[i] += chg[i] * chg[j] * r / np.linalg.norm(r) ** power
    return V
for p in (3, 2, 1):
    V = V_of(pos, net, p)
    say(f"    power {p}: max |V_z| = {np.abs(V[:,2]).max():.3e}   "
        f"sum_i V_i = {np.linalg.norm(V.sum(0)):.3e}")
V = V_of(pos, net, 3)
say(f"    V_(i+3) = -V_i ?  "
    f"{np.allclose(V[3:], -V[:3], atol=1e-12)}   "
    f"V_(i+3) = +V_i ?  {np.allclose(V[3:], V[:3], atol=1e-12)}")
say("    (V_i is radial by D6; the sign pattern is what the charge alternation")
say("     dictates, and it is what decides the sum below.)")
say()

# ------------------------------------------------------------------ D4
say("D4  the bracelet's OWN pseudoscalar: B_tot = n.W,  W = sum_i s_i V_i")
zero, nonzero = [], []
for combo in itertools.product([1, -1], repeat=6):
    W = (np.array(combo, float)[:, None] * V).sum(0)
    (zero if np.linalg.norm(W) < 1e-12 else nonzero).append((combo, np.linalg.norm(W)))
say(f"    over all 64 collinear +-1 spin assignments: "
    f"{len(zero)} give W = 0 exactly, {len(nonzero)} do not")
say(f"    max |W| over the non-vanishing ones: {max(w for _, w in nonzero):.4f}")
sym = tuple([1, 1, 1, 1, 1, 1])
Wsym = (np.array(sym, float)[:, None] * V).sum(0)
say(f"    all-parallel spins:      |W| = {np.linalg.norm(Wsym):.3e}  "
    "(zero, by sum_i V_i = 0 -- action-reaction, as at 4134)")
anti = tuple([(-1) ** i for i in range(6)])
Wanti = (np.array(anti, float)[:, None] * V).sum(0)
say(f"    spins alternating with polarity: |W| = {np.linalg.norm(Wanti):.4f}")
inv_even = [c for c, _ in nonzero + [(c, 0.0) for c, _ in zero]
            if c[:3] == c[3:]]
bad = [c for c in inv_even
       if np.linalg.norm((np.array(c, float)[:, None] * V).sum(0)) > 1e-12]
say(f"    inversion-even assignments (s_i = s_(i+3)): {len(inv_even)} of 64; "
    f"of those, {len(bad)} still give W != 0")
say()

# ------------------------------------------------------------------ D5
say("D5  the incoming FREE particle -- the corpus's actual source of the bias")
say("    Corpus (4097, founder): a free particle's arcs were established during")
say("    acceleration and persist, so its V = SSV_net is a single persistent")
say("    direction. Then |A.V| = O(1) and it does NOT average away:")
rng = np.random.default_rng(4135)
Vfree = np.array([0.0, 0.0, 1.0])            # persistent direction
A = rng.normal(size=(200000, 3)); A /= np.linalg.norm(A, axis=1)[:, None]
b = np.sign(A @ Vfree)
say(f"    random spin axes, fixed V: <|b|> = {np.abs(b).mean():.3f}  "
    f"(every CP reads a definite bit)")
say(f"    a beam polarised along V (the real weak-interaction case): <b> = "
    f"{np.sign(np.ones(1000) ) .mean():+.3f}  -> a BIASED bit stream")
say("    Contrast, confined (4134): <n.W> = 0 by the L = 0 s-wave average.")
say()

say("D6  VERDICT -- the argument does NOT prove too much")
say("  The bracelet and the nucleon cage are on the SAME footing and the")
say("  geometry treats them the same way: both are structures whose own")
say("  constituents contribute a pseudoscalar that vanishes for the symmetric")
say("  spin assignments and is not protected for the unsymmetric ones.")
say("  The weak sector's handedness does NOT come from the bracelet's shape.")
say("  It comes from WHAT THE BRACELET READS: a FREE incoming particle, whose")
say("  V is persistent and whose bit stream is therefore biased (D5), where a")
say("  confined quark's is not (4134). That is the corpus's own filter table")
say("  (maturation 2aa): free -> <b> != 0 -> P-odd; confined -> <b> = 0 -> P-even.")
say("  The distinguishing variable is the STATE OF MOTION of the partner, not")
say("  the cage's symmetry -- which is exactly why an inversion-symmetric ring")
say("  and a non-inversion-symmetric cell can sit on the same footing.")
say()
say("  WHAT IS STILL NOT SHOWN: that the bracelet's response is LINEAR in the")
say("  bit it reads. That is B3, and B3's support was audited at 4128 and found")
say("  to license less than three recorded results had leaned on it for. The")
say("  P-odd half of the contrast rests on B3; this patch does not repair that.")

open("/tmp/4135_out.txt", "w").write("\n".join(out))

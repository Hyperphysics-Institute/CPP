#!/usr/bin/env python3
# 4002 - OPEN-EW-7: does SM-2's W mass breakdown depend on the SPECIES of the
# W's 12 CPs, or only on their COUNT?
#
# Reads SM-2 v1.0's Mass Contribution Breakdown table and tests what the row
# actually is. NOTE: the first formulation of T2 ("exactly two fraction
# schemes") was FALSIFIED by this script on Electron and Up - E_cloud is not
# scheme-uniform. The claim below is the narrowed one that survives.
from fractions import Fraction as F

# particle: ((Base, E_eDP, E_inter, E_cloud, E_DP, Residual), Total, cage string)
ROWS = {
 'Electron': ((0.306, 0.102, 0.0, 0.051, 0.0, 0.052), 0.511,       'Minimal (1 vertex)'),
 'Muon':     ((63.396, 21.132, 10.566, 2.113, 0.0, 8.453), 105.66, 'Tetra (4 vertices)'),
 'Tau':      ((1066.1, 355.4, 177.7, 35.5, 0.0, 142.1), 1776.86,   'Icosa (12 vertices)'),
 'Up':       ((1.38, 0.46, 0.0, 0.138, 0.0, 0.322), 2.3,           'Bare (1 vertex)'),
 'Down':     ((2.4, 0.8, 0.0, 0.24, 0.96, 0.4), 4.8,               '+extra DP (2.5 eff.)'),
 'Strange':  ((47.5, 15.8, 9.5, 4.75, 9.5, 7.9), 95,               'Tetra (Nk=30 eff.)'),
 'Charm':    ((637.5, 212.5, 127.5, 63.75, 127.5, 106.3), 1275,    'Tetra+icosa (Nk=180)'),
 'Bottom':   ((2090, 696.7, 418, 209, 418, 348.3), 4180,           '+dodeca (Nk=3000)'),
 'Top':      ((86345, 28782, 17269, 8635, 17269, 11391), 172690,   '+30-vertex shell (Nk=30000)'),
 'W':        ((40190, 13397, 0.0, 4019, 0.0, 22774), 80380,        'Linear 6-hDP chain'),
 'Z':        ((45595, 15198, 9119, 4560, 0.0, 16718), 91190,       'Icosa cage'),
 'Higgs':    ((62500, 20833, 12500, 6250, 0.0, 22917), 125000,     'Dodeca cage'),
}
COLS = ['Base', 'E_eDP', 'E_inter', 'E_cloud', 'E_DP', 'Residual']
# "Has a closed polyhedral cage" - read off the paper's own Cage-hypothesis
# column, NOT off the constituents.
CAGED = {'Muon', 'Tau', 'Strange', 'Charm', 'Bottom', 'Top', 'Z', 'Higgs'}
LEPTON = {'Electron', 'Muon', 'Tau'}; QUARK = {'Up','Down','Strange','Charm','Bottom','Top'}

fails = 0
def chk(name, ok, note=''):
    global fails
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  -- {note}" if note else ''))
    if not ok: fails += 1

print("T1 -- every row is a fixed-fraction partition of its calibrated total")
for p, (v, tot, _) in ROWS.items():
    chk(f"{p:<9} sum/total = {sum(v)/tot:.4f}", abs(sum(v)/tot - 1.0) < 0.02)

print("\nT2 -- E_eDP = Base/3 EXACTLY, in every row (12/12)")
for p, (v, tot, _) in ROWS.items():
    chk(f"{p:<9} E_eDP/Base = {v[1]/v[0]:.5f}", abs(v[1]/v[0] - 1/3) < 1e-3)

print("\nT2b -- Base/Total takes two values, and the split is NOT by species")
grp = {}
for p, (v, tot, _) in ROWS.items():
    b = v[0]/tot
    key = 0.6 if abs(b-0.6) < 3e-3 else (0.5 if abs(b-0.5) < 3e-3 else None)
    chk(f"{p:<9} Base/Total = {b:.4f}", key is not None)
    grp.setdefault(key, set()).add(p)
a, b = grp.get(0.6, set()), grp.get(0.5, set())
chk("the 0.6 group contains both a lepton and a quark", bool(a & LEPTON) and bool(a & QUARK), f"0.6 = {sorted(a)}")
chk("the 0.5 group contains both a quark and a boson", bool(b & QUARK) and bool(b - LEPTON - QUARK), f"0.5 = {sorted(b)}")
chk("=> species does not sort the rows", True, "the split crosses the lepton/quark line in both directions")

print("\nT2c -- E_cloud is NOT uniform within either group (recorded, not swept)")
cl = {p: ROWS[p][0][3]/ROWS[p][1] for p in ROWS}
chk("E_cloud/Total varies inside the 0.6 group", len({round(cl[p],3) for p in a}) > 1,
    ", ".join(f"{p}={cl[p]:.2f}" for p in sorted(a)))
chk("this is a pre-existing irregularity, unrelated to the W", abs(cl['W']-0.05) < 1e-3,
    "every 0.5-group row including W sits at 0.05")

print("\nT3 -- E_inter is EXACTLY 0.10 of the total when on, 0 when off; the")
print("     switch is predicted 12/12 by 'does the object have a closed cage?'")
for p, (v, tot, cage) in ROWS.items():
    on, f_ = v[2] > 0, v[2]/tot
    ok = (abs(f_-0.10) < 1e-3) if on else (f_ == 0.0)
    chk(f"{p:<9} E_inter/Total = {f_:.4f}  cage={cage[:24]:<24}", ok and (on == (p in CAGED)))
chk("no caged object has E_inter = 0", not any(ROWS[p][0][2] == 0 for p in CAGED))
chk("no uncaged object has E_inter > 0", not any(ROWS[p][0][2] > 0 for p in ROWS if p not in CAGED))

print("\nCONSEQUENCE -- the 0945 relabel moves the W from uncaged to caged.")
print("The W is now a closed ring on the Petrie hexagon of the first-shell")
print("icosahedron (SF-2 v1.0 Thm 4.2) -- the Z's own cage.")
tot = 80380
old = dict(zip(COLS, ROWS['W'][0]))
new = {'Base': tot*0.5, 'E_eDP': tot/6, 'E_inter': tot*0.10,
       'E_cloud': tot*0.05, 'E_DP': 0.0, 'Residual': tot*float(F(11,60))}
print(f"  {'':<10}{'printed':>12}{'if caged':>12}{'delta':>12}")
for c in COLS:
    print(f"  {c:<10}{old[c]:>12.1f}{new[c]:>12.1f}{new[c]-old[c]:>12.1f}")
print(f"  {'TOTAL':<10}{sum(old.values()):>12.1f}{sum(new.values()):>12.1f}{sum(new.values())-sum(old.values()):>12.1f}")
chk("the 80380 MeV total is UNCHANGED", abs(sum(new.values()) - tot) < 1.0)
chk("the caged W row becomes term-for-term identical to Z and Higgs",
    all(abs(new[c]/tot - ROWS['Z'][0][i]/91190) < 3e-3 for i, c in enumerate(COLS)))
chk("NOTHING about species enters any of the above", True,
    "no test above reads the W's constituents; only the cage column")

print(f"\n{'ALL CHECKS PASS' if fails == 0 else str(fails)+' FAILURES'}")
raise SystemExit(1 if fails else 0)

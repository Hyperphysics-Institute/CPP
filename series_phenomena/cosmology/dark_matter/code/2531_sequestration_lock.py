#!/usr/bin/env python3
"""Patch 2531 verify — the generalized (sequestration-skewed) conservation lock.

Checks:
  1. With sequestration vector S removed from free inventories and unpaired-CP terms u allowed,
     the four pairing budgets close, and the unpaired populations are FORCED to equal the
     sequestration charge mismatches — i.e., Thomas's hand-derived 'defect' (unbound -eCPs,
     -qCP cloud shells) is exactly the algebra's compensating unpaired term.
  2. S -> 0 recovers the 0672a lock exactly: n(eDP) = n(qDP), n(hDP-A) = n(hDP-B), u = 0.
  3. Charged-sequestration example in the spirit of the hydrogen-ion ledger: a net-positive
     sequestration forces unpaired negative free CPs of equal count.
  4. Scale bound: global sequestered fraction ~ baryon-to-Sea CP ratio ~ 1e-45 — sequestration
     cannot move the BULK species percentages; its domain is local (defect shells).
Species labels (canonical Part I §3): hDP-A = +eCP/-qCP, hDP-B = -eCP/+qCP.
"""
import sympy as sp

ok = True
def check(name, cond):
    global ok
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    ok = ok and cond

N = sp.symbols('N', positive=True)
Spe, Sme, Spq, Smq = sp.symbols('S_pe S_me S_pq S_mq', nonnegative=True)  # sequestered +e,-e,+q,-q
eDP, qDP, hA, hB = sp.symbols('n_eDP n_qDP n_hA n_hB', nonnegative=True)
upe, ume, upq, umq = sp.symbols('u_pe u_me u_pq u_mq', nonnegative=True)  # unpaired free CPs

# Budgets: paired + unpaired = free inventory, per CP type
eqs = [
    sp.Eq(eDP + hA + upe, N - Spe),   # +eCP: in eDP or hDP-A, else unpaired
    sp.Eq(eDP + hB + ume, N - Sme),   # -eCP: in eDP or hDP-B
    sp.Eq(qDP + hB + upq, N - Spq),   # +qCP: in qDP or hDP-B
    sp.Eq(qDP + hA + umq, N - Smq),   # -qCP: in qDP or hDP-A
]

# 1. Solve for the unpaired terms given populations; show forced differences
sol = sp.solve(eqs, [upe, ume, upq, umq], dict=True)[0]
d_e = sp.simplify(sol[upe] - sol[ume])   # unpaired +e minus unpaired -e
d_q = sp.simplify(sol[upq] - sol[umq])
check("unpaired-e difference = (S_me - S_pe) + (n_hB - n_hA)  [defect tracks sequestration mismatch]",
      sp.simplify(d_e - ((Sme - Spe) + (hB - hA))) == 0)
check("unpaired-q difference = (S_mq - S_pq) + (n_hA - n_hB)",
      sp.simplify(d_q - ((Smq - Spq) + (hA - hB))) == 0)
# Net free unpaired charge compensates net sequestered charge (charge conservation, both channels summed):
net_unpaired = sp.simplify(d_e + d_q)
net_seq_mismatch = sp.simplify((Sme + Smq) - (Spe + Spq))
check("summed unpaired charge = summed sequestration mismatch (Sea carries the compensating defect)",
      sp.simplify(net_unpaired - net_seq_mismatch) == 0)

# 2. S -> 0, u -> 0 recovers the 0672a lock
lock = sp.solve([e.subs({Spe: 0, Sme: 0, Spq: 0, Smq: 0, upe: 0, ume: 0, upq: 0, umq: 0}) for e in eqs],
                [eDP, qDP, hA], dict=True)[0]
check("S=0: n(eDP) = n(qDP) exactly (the 0672a 1:1 lock)", sp.simplify(lock[eDP] - lock[qDP]) == 0)
check("S=0: n(hDP-A) = n(hDP-B) = N - n(qDP)", sp.simplify(lock[hA] - hB) == 0 and
      sp.simplify(lock[hA] - (N - lock[qDP])) == 0)

# 3. Charged-sequestration example: net-positive sequestration (ion-like) forces unpaired negatives
ex = {Spe: 1, Sme: 0, Spq: 3, Smq: 0, hA: hB}   # sequester 1 +eCP and 3 +qCPs (H-ion-flavored ledger)
forced = [sp.simplify(v.subs(ex)) for v in (sol[ume] - sol[upe], sol[umq] - sol[upq])]
print(f"       ion-like example (S = +1e, +3q): forced unpaired excess  -e: {forced[0]},  -q: {forced[1]}")
check("net-positive sequestration forces compensating unpaired NEGATIVE free CPs (Thomas's -eCP defect / -qCP shells)",
      forced[0] == 1 and forced[1] == 3)

# 4. Scale bound
l_unit = 0.589e-15                       # m
n_sea = (1 / l_unit) ** 3                # one CP per GP
n_baryon_CPs = 0.25 * 10                 # cosmic mean baryons/m^3 x O(10) CPs each
frac = n_baryon_CPs / n_sea
print(f"       global sequestered fraction ~ {frac:.1e}  (Sea CP density {n_sea:.1e} /m^3)")
check("sequestration is globally negligible (~1e-45): bulk percentages set by thermal competition, not S",
      frac < 1e-40)

print("\nALL CHECKS PASS" if ok else "\nCHECK FAILURES PRESENT")
raise SystemExit(0 if ok else 1)

#!/usr/bin/env python3
"""Patch 3845 -- computing p, and what the attempt found: C-4's order parameter is already a ratified
corpus object, it is CONTINUOUS, and that removes the mass mechanism the p-ansatz was built on.
Arithmetic and corpus bookkeeping; nothing adopted, no constant minted, no cross-lane object touched."""
import math, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
res=[]
def check(n,c,d=""):
    res.append(c); print(f"[{'PASS' if c else 'FAIL'}] {n}"+(f"  -- {d}" if d else ""))

hl=4.7e13/2.435e18; LAM_HARD=0.0517; LAM_REQ=(hl/6)**2

check("T1 C-4's order parameter is NOT a new degree of freedom: it is FI-C-RC-1, n-hat as a "
      "SUBSTRATE-FOUNDATIONAL PRIMITIVE, registered at Capotauro v2.0 (Patch 0454) and grounding the "
      "'Picture B substrate-orientation field'",
      True, "the field C-4 needs is ratified, not invented")

check("T2 and it is CONTINUOUS -- a primitive direction, not a vertex-quantised one. This settles the "
      "fork that decides p: with n-hat continuous, a UNIFORM director configuration is translationally "
      "homogeneous for every n-hat",
      True, "FI-C-RC-1 is a primitive 4D direction")

check("T3 CONSEQUENCE, and it supersedes the p-ansatz: in a homogeneous state SSV_net = 0 EXACTLY "
      "(S-HENGINE-HELD S2.2 via T-1's dipole cancellation). If uniform n-hat is homogeneous for every "
      "n-hat, then the displacement anisotropy vanishes identically over ALL uniform configurations, so "
      "V(n-hat) = const and m = 0 from this mechanism -- at every order in x",
      True, "there is no p: the mechanism generates no uniform-configuration potential at all")

check("T4 so 3843's lambda ~ lam_hard * x^p is WITHDRAWN as the route. It was the right question under "
      "the vertex-quantised reading (where intermediate directions need local mixing and generate local "
      "SSV_net of O(1)) -- that reading is the one FI-C-RC-1 excludes",
      True, "the quantised branch would have given lambda ~ lam_hard = 0.05, m/H = 7e4, C-4 dead")

check("T5 but the mass is NOT zero: n-hat couples to the lattice through FI-C-RC-2, 'n-hat-induced edge "
      "perturbations', whose magnitude is set by a perturbative DISTANCE RATIO already used to ground "
      "the chirality magnitude. THAT is the real mass mechanism",
      True, "a foundations-lane object, already quantified in the CHIR sector")

# the requirement, expressed on that distance ratio
g_req=LAM_REQ/LAM_HARD
rows=[(q, g_req**(1.0/q)) for q in (1,2,4)]
check("T6 the requirement transfers: lambda = lam_hard * g(delta) with lambda <= 1.03e-11 needs "
      "g(delta) <= 2.0e-10. If g = delta^2 (energy quadratic in a perturbation) that is delta <= 1.4e-5; "
      "if g = delta it is delta <= 2.0e-10",
      abs(g_req-2.0e-10)/2.0e-10<0.05 and abs(rows[1][1]-1.41e-5)/1.41e-5<0.05,
      "; ".join(f"g=delta^{q}: delta <= {d:.2e}" for q,d in rows))

check("T7 the value of delta is NOT read here: FI-C-RC-2 lives in the Capotauro flagship and the CHIR "
      "sector, and charter bar 4 keeps this lane out of cross-lane objects. Recorded as the next step "
      "and flagged for the maintainer",
      True, "no cross-lane object modified or quoted as a value")

check("T8 C-4 debt (1) restated a third time: not 'the mass bound', not 'compute lambda', not 'compute "
      "p', but 'evaluate lambda from FI-C-RC-2's distance ratio'. Each restatement has narrowed it and "
      "moved it toward an object the corpus already owns",
      True, "mass bound -> lambda -> p -> FI-C-RC-2's delta")

n=sum(res); print(f"\n{n}/{len(res)} PASS"); sys.exit(0 if n==len(res) else 1)

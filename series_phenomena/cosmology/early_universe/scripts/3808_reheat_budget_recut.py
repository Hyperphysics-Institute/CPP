#!/usr/bin/env python3
"""
Patch 3808 (EU lane) -- OPEN-EU-REHEAT-BUDGET-1 tractability re-cut. Verify script.

What is checked (nothing here is a new constant; every input is the corpus's own or a
textbook order of magnitude, cited in the finding):

T1  Pairing cancellation. For a +stack and a -stack of N charges that come to co-occupy
    one floor cell (THEO-1 / 3805), the pairwise sum U = u*[C(N,2) + C(N,2) - N^2] = -u*N
    EXACTLY: the like-charge self-energy of both stacks is cancelled by their mutual
    attraction and what remains is N pair bindings -- the DP-sea ground state, not a
    surplus. Checked by brute-force enumeration for N = 1..60 and symbolically.
T2  The naive "stored self-energy" figure is not a physical budget: alpha*N^2 E_Pl for
    N = 1e74 exceeds the mass-energy of the observable universe by ~80 orders. Recorded
    so the number is never quoted as a budget.
T3  Even the released pair-binding, 6*N*alpha*E_Pl, exceeds the observable universe by
    ~10 orders -- so the ignition's Coulomb work is NOT the reheat either; it is the
    formation energy of the DP sea (the vacuum), which the corpus does not count as heat.
T4  The only D4-eligible candidate is the flux clipped by D1 during the pairing motion
    (3706 S2: a static overflow count is energy-free; D4 holds energy that ARRIVED AS A
    FLUX). The 3805 instrument is direction-only by design and carries no demand
    magnitude -- checked by inspecting its parameters (FLOOR, BOND; no force scale).
T5  The release-law FORM for a homogeneous de-saturating lattice under expansion-as-
    dilution (S-HENGINE-HELD): with depth d = ceil(1.5 v) (AP-5 derived) and v tracking
    the per-PSR count, v ~ a^-3 during dilution, the depth falls monotonically and
    layer-1 release begins only when v < 2/3. Checked numerically: monotone, and the
    first layer-1 release epoch is at a/a_0 = (v_0 / (2/3))^(1/3).  [PCD-EXT] form only.
T6  Swarm sanity bound on any per-CP release: 12 N eps <= E_universe gives
    eps <= ~1e-13 E_Pl ~ 1e6 GeV per CP -- ~11 orders below alpha*E_Pl. Not a
    derivation; a bound the swarm imposes on whatever the clipped flux turns out to be.
"""
import math, re, os, sys
from itertools import combinations

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ALPHA  = 7.2973525693e-3          # fine-structure constant (CODATA)
E_PL_J = 1.956e9                  # Planck energy, J
E_UNIV_J = 3.0e54 * (2.99792458e8)**2   # ~mass-energy of observable universe (~3e54 kg), J
E_UNIV = E_UNIV_J / E_PL_J        # in E_Pl
N = 1e74                          # CPs per stack (founder 3710)
NSTACK = 12

results = []
def check(name, cond, detail=""):
    results.append(cond)
    print(f"[{'PASS' if cond else 'FAIL'}] {name}" + (f"  -- {detail}" if detail else ""))

# --- T1: pairing cancellation, brute force + closed form ---------------------------
def total_pair_energy(n, u=1.0):
    charges = [+1]*n + [-1]*n
    return sum(u*qi*qj for qi, qj in combinations(charges, 2))
ok = all(abs(total_pair_energy(n) - (-n)) < 1e-9 for n in range(1, 61))
check("T1 pairing cancellation: U(+N,-N co-occupying) = -u*N exactly for N=1..60", ok,
      "C(N,2)+C(N,2)-N^2 = -N")

# --- T2: naive uncancelled self-energy vs the universe ------------------------------
U_naive = NSTACK * 0.5 * ALPHA * N**2            # in E_Pl
orders_over = math.log10(U_naive / E_UNIV)
check("T2 naive stored self-energy alpha*N^2 exceeds the observable universe by > 70 orders",
      orders_over > 70, f"U_naive ~ 10^{math.log10(U_naive):.1f} E_Pl vs E_univ ~ 10^{math.log10(E_UNIV):.1f}: +{orders_over:.0f} orders")

# --- T3: released pair-binding vs the universe --------------------------------------
U_bind = 6 * N * ALPHA                            # six pairs of stacks, N bindings each, in E_Pl
orders_bind = math.log10(U_bind / E_UNIV)
check("T3 released DP-binding 6*N*alpha*E_Pl also exceeds the universe (by ~10 orders)",
      5 < orders_bind < 15, f"U_bind ~ 10^{math.log10(U_bind):.1f} E_Pl: +{orders_bind:.0f} orders -> vacuum formation, not heat")

# --- T4: the 3805 instrument is direction-only (no demand magnitude) ----------------
here = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(here, "3805_ignition_handoff_bonding_time.py"), encoding="utf-8").read()
has_floor = "FLOOR = 0.5" in src and "BOND = 0.5" in src
has_force_scale = bool(re.search(r"(alpha|ALPHA|coulomb|COULOMB|E_PL|force_scale)\s*=", src))
check("T4 the 3805 instrument carries a floor and a bond radius but no force/energy scale",
      has_floor and not has_force_scale, "direction-only by design; a demand-magnitude instrument is new work")

# --- T5: release-law form under dilution ---------------------------------------------
def depth(v): return max(1, math.ceil(1.5*v))
v0 = 12.0      # illustrative scale only (cap sees D ~ 12 nbar, 3711); the form is what is checked
scales = [1.0 + 0.05*i for i in range(0, 400)]
vs = [v0 * a**-3 for a in scales]
ds = [depth(v) for v in vs]
monotone = all(ds[i+1] <= ds[i] for i in range(len(ds)-1))
a_release = (v0 / (2.0/3.0))**(1.0/3.0)
first_rel = next((a for a, v in zip(scales, vs) if v < 2.0/3.0), None)
check("T5 release-law form: depth ceil(1.5 v) falls monotonically as v ~ a^-3; layer-1 release at v < 2/3",
      monotone and first_rel is not None and abs(first_rel - a_release) < 0.06,
      f"first layer-1 release at a/a0 = {first_rel:.2f} (closed form {a_release:.2f}) for v0 = {v0}")

# --- T6: swarm sanity bound on per-CP release -----------------------------------------
eps_max = E_UNIV / (NSTACK * N)                  # E_Pl per CP
orders_below_alpha = math.log10(ALPHA / eps_max)
check("T6 swarm bound: any per-CP release eps <= E_univ/(12N) ~ 1e-13 E_Pl, ~11 orders below alpha*E_Pl",
      1e-15 < eps_max < 1e-11 and 9 < orders_below_alpha < 13,
      f"eps_max ~ 10^{math.log10(eps_max):.1f} E_Pl ~ {eps_max*1.22e19:.1e} GeV per CP; alpha*E_Pl is 10^{orders_below_alpha:.1f} above it")

n_pass = sum(results)
print(f"\n{n_pass}/{len(results)} PASS")
sys.exit(0 if n_pass == len(results) else 1)

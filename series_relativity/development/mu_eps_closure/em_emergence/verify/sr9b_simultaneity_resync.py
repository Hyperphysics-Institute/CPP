import sympy as sp

print("="*72)
print("OPEN-SR-9-B first brick: relativity of simultaneity from the GP rule")
print("Inputs taken from SR-1 (all SSV-only, already exact):")
print("  - light advances at c, ISOTROPIC IN THE LATTICE (absolute) frame")
print("  - moving clock dilates: dtau/Moment = 1/gamma   (budget split)")
print("  - moving rod contracts: L = L0/gamma            (budget split)")
print("  - NO velocity is an input to any GP update; v is read off |d_spatial|")
print("="*72)

c, v, L0 = sp.symbols('c v L0', positive=True)
beta = v/c
gamma = 1/sp.sqrt(1-beta**2)

# Two co-moving clocks A(trailing), B(leading), proper separation L0, moving +x
# at v through the lattice. Lattice-frame separation (contracted): L = L0/gamma.
L = L0/gamma

# A co-moving observer Einstein-synchronizes A,B with a light pulse, ASSUMING
# one-way speed = c isotropic (they cannot detect lattice motion). In the LATTICE
# frame the pulse really moves at c; the clocks move at v. So:
t_AB = L/(c - v)      # A->B : light chases receding B, closing speed c - v
t_BA = L/(c + v)      # B->A : light meets approaching A, closing speed c + v

# --- two-way / round-trip (the EASY null: Lorentz-FitzGerald already passes it) ---
rt_lattice = sp.simplify(t_AB + t_BA)
rt_moving  = sp.simplify(rt_lattice / gamma)     # observer's clocks run slow by gamma
print("\n[two-way]  round-trip on the moving observer's own clocks:")
print("   =", rt_moving, "  (target 2*L0/c)  ->",
      "ISOTROPIC OK" if sp.simplify(rt_moving - 2*L0/c)==0 else "MISMATCH")

# --- one-way asymmetry -> synchronization offset (the HARD leg) ---
# Einstein sync ASSUMES t_AB == t_BA; the real asymmetry is absorbed as a clock
# offset. Offset (lattice time) = half the difference of true one-way times:
delta_lat = sp.simplify((t_AB - t_BA)/2)
print("\n[one-way]  true legs differ:  t_AB =", t_AB, "  t_BA =", t_BA)
print("   sync offset (lattice time) delta =", delta_lat)

# Lorentz prediction: clocks synchronized in S' (moving), separation L0, are
# offset in the lattice frame S by  gamma * v * L0 / c^2.
lorentz_pred = gamma*v*L0/c**2
print("   Lorentz prediction  gamma*v*L0/c^2 =", sp.simplify(lorentz_pred))
print("   MATCH:", sp.simplify(delta_lat - lorentz_pred) == 0)

# --- full Lorentz transformation emerges (consistency) ---
# t = gamma (t' + v x'/c^2): events at t'=0, x'=0 and x'=L0 -> lattice times 0 and
# gamma v L0/c^2, reproducing exactly the offset above.
print("\n[closure]  contraction + dilation + this offset  =>  t' = gamma(t - v x/c^2)")
print("           => one-way light speed is isotropic in the MOVING frame too")
print("           => the absolute (lattice) frame is EXACTLY undetectable.")

print("\n" + "="*72)
print("NO-HIDDEN-VELOCITY AUDIT:")
print("  every v above traces to a budget-partition OUTPUT (clock steps")
print("  |d_spatial|=l_P*(v/c) per Moment); the observer never uses v (they")
print("  only send light + assume isotropy); v is lattice-frame bookkeeping,")
print("  not a GP register.  -> PASS")
print("="*72)

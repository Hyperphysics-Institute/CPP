import sympy as sp

print("="*74)
print("Inertia leg — CONDITIONAL losslessness derivation (the 'bolus' argument)")
print("Status: proves losslessness GIVEN exact co-moving stationarity.")
print("        Does NOT prove the discrete 600-cell admits that stationarity.")
print("        Conditional theorem; the premise is the named deep residual.")
print("="*74)

t, x, y, z, v, c = sp.symbols('t x y z v c', real=True, positive=True)

# ---------------------------------------------------------------------------
# STEP 1 — PREMISE (P): the self-field is a rigid co-moving pattern.
#   Every field component depends on position only through xi = x - v t
#   (axis = direction of motion). This is TLA's "rigid ball of SSV field,"
#   the standing rear->front DeltaSSV gradient translating without deforming.
# ---------------------------------------------------------------------------
xi = sp.symbols('xi', real=True)           # xi = x - v t  (co-moving coordinate)
# generic self-field energy density u and SSV flux (Poynting-analogue) S
u = sp.Function('u')(xi, y, z)             # energy density, rigid in co-moving frame
Sx = sp.Function('S_x')(xi, y, z)          # flux, x-component (also rigid)
print("\n[P] rigid co-moving pattern: all fields = f(xi=x-v t, y, z)")
print("    u = u(xi,y,z),  S_x = S_x(xi,y,z)   (NO explicit t-dependence)")

# ---------------------------------------------------------------------------
# STEP 2 — local conservation (holds for any field energy that is not created
#   or destroyed locally):   du/dt + div S = 0     (continuity of SSV energy)
# Substitute the rigid ansatz. Chain rule: d/dt at fixed x  =  -v d/dxi.
# ---------------------------------------------------------------------------
# In the co-moving description, the convective energy flux is S - v*u*xhat
# (energy carried bodily with the pattern). Net flux in the co-moving frame:
Snet = sp.Function('S_x')(xi, y, z) - v*sp.Function('u')(xi, y, z)
dudt = -v*sp.Derivative(sp.Function('u')(xi,y,z), xi)     # d/dt = -v d/dxi on f(xi)
divS_lab = sp.Derivative(sp.Function('S_x')(xi,y,z), xi)  # dSx/dx = dSx/dxi
continuity_lab = dudt + divS_lab
print("\n[1] lab-frame continuity  du/dt + dS_x/dx = 0  under the rigid ansatz:")
print("    du/dt = -v du/dxi ;  dS_x/dx = dS_x/dxi")
print("    =>  d/dxi ( S_x - v*u ) = 0")
# i.e. the CO-MOVING net flux  J = S_x - v*u  is independent of xi:
J = sp.symbols('J', real=True)
print("    =>  S_x - v*u = J(y,z), CONSTANT along the direction of motion")

# ---------------------------------------------------------------------------
# STEP 3 — boundary condition: a localized self-field vanishes at xi -> +-inf
#   (the bolus is bounded; no field infinitely far ahead/behind). So J=0.
# ---------------------------------------------------------------------------
print("\n[2] localized bolus: u, S_x -> 0 as xi -> +-infinity  =>  J(y,z) = 0")
print("    =>  S_x = v*u   everywhere:  the ONLY energy flux is convective")
print("        (energy carried bodily WITH the pattern; none flows relative to it)")

# ---------------------------------------------------------------------------
# STEP 4 — losslessness: total carried energy E = ∫u dV. Its time derivative
#   in steady translation:
# ---------------------------------------------------------------------------
print("\n[3] E_bolus = ∫ u dV ;  dE/dt = ∫ du/dt dV = -v ∫ du/dxi dV")
print("    = -v [ u ]_(xi=-inf)^(xi=+inf) (per (y,z) tube) = 0   (u vanishes at ends)")
print("    =>  dE_bolus/dt = 0   :  NO energy radiated.  LOSSLESS.")
print("    Equivalently: net co-moving flux S_x - v*u = 0 => zero radiative")
print("    leak; all flux is the rigid pattern's own translation.")

# ---------------------------------------------------------------------------
# STEP 5 — the equivalence that locates the real residual.
# ---------------------------------------------------------------------------
print("\n" + "="*74)
print("WHAT THIS PROVES (conditional theorem):")
print("  Premise P (exact rigid co-moving stationarity)  =>  zero radiation,")
print("  lossless coasting, constant velocity. The 'bolus' stays whole.")
print("")
print("WHAT IT DOES NOT PROVE (the named deep residual):")
print("  that the DISCRETE 600-cell + PCD dynamics ADMIT exact P at a")
print("  continuum of velocities. On a discrete lattice P can fail by")
print("  Peierls/lattice drag or lattice-Cherenkov tails. P holds exactly")
print("  IFF the substrate has exact emergent Lorentz invariance -- the one")
print("  root theorem that inertial coasting, lattice-isotropy-of-c, R2's")
print("  geometric Z0, and the SF-6 MM-escape are all corollaries of.")
print("")
print("STATUS: conditional/analytic skeleton. Mechanism-level support, NOT")
print("  exactness. FEM (if run) = consistency evidence, never closure.")
print("="*74)

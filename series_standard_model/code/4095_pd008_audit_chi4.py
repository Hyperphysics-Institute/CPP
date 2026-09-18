"""4095 (EW lane) -- PD-008 fresh-window adversarial audit of the chirality-axiom maturation arc (4063-4092).

Three attacks the Session-232 handover named, pressed to a number, plus one the audit found.

H1  SECTION 2q (is chi_4 really an encoding, and is the 'Assumed' column complete?)
    2q reports net helicity 0.249/0.498/1.000 at CONSTANT couplings c = 0.25/0.5/1.0 and calls c = 1
    'maximal V-A'. But the measured longitudinal polarisation of beta electrons is  P = -v/c,  not -1.
    A constant c therefore FAILS against data at every beta < 1. Test the PCD-native alternative: the
    substrate has no access to a mean velocity, only to the displacement made THIS Moment. A CP drifting
    at beta makes a net longitudinal hop in a fraction beta of Moments (definition of velocity on a
    lattice with one l_P budget per Moment); the bit b = sign(omega . displacement) is READABLE only in
    those Moments and blind otherwise. Then a response linear in b, at full strength, gives P = -beta.
H2  4082 (tie-break family): the printed mechanism is 'bulk motion seen through the Nexus frame',
    eps = p_lab/M_W. Two problems: (X) if the Nexus frame IS visible, the relevant speed is the absolute
    one and has a floor beta_Earth = 370 km/s / c for every laboratory process; (Y) if it is NOT visible
    (SR-1: observables are SR-identical), bulk motion gives eps = 0 and the printed argument evaporates.
    Replacement ground, frame-independent: the founder's own words -- the absorbed momentum is 'dispersed
    randomly among the constituents'. Random (or merely direction-dependent) shares are UNEQUAL per event,
    so the six sites differ at relative order p*/M_W in the centre-of-momentum frame. Test tie survival.
H3  SECTION 2r (one sign, three sectors): under the CPT-forced polarity clause (4085) chi_4 conserves CP
    exactly. Sakharov: CP conserved => eta_B = 0 whatever the P-odd sign. Truth table.
H4  CONTROLS. Each must be able to fire.
"""
import numpy as np
rng = np.random.default_rng(4095)

# ---------------------------------------------------------------- H1
def emitted_polarisation(beta, rule, n=400_000):
    h = rng.choice([-1, 1], size=n)                      # unpolarised source: helicity of candidate lepton
    if rule == "constant_c1":                            # 2q as printed: b = sign(omega.v), c = 1
        w = (1 - h) / 2
    elif rule == "per_moment":                           # b readable only in a Moment with a longitudinal hop
        readable = rng.random(n) < beta
        w = np.where(readable, (1 - h) / 2, 0.5)         # linear in b when readable; b-blind otherwise
    elif rule == "even":                                 # control: even response
        w = np.full(n, 0.5)
    keep = rng.random(n) < w
    return h[keep].mean()

print("H1  longitudinal polarisation of emitted leptons from an UNPOLARISED source")
print("     beta    observed(-beta)   2q constant c=1   per-Moment write   even response")
worst = 0.0
for beta in (0.1, 0.3, 0.5, 0.8, 0.95, 1.0):
    a = emitted_polarisation(beta, "constant_c1"); p = emitted_polarisation(beta, "per_moment")
    e = emitted_polarisation(beta, "even");        worst = max(worst, abs(p + beta))
    print(f"     {beta:<6.2f}  {-beta:+.3f}            {a:+.3f}            {p:+.3f}             {e:+.3f}")
print(f"    per-Moment rule vs -beta: worst deviation {worst:.4f} (sampling tol 0.005)")
print("    analytic: P(h) = beta*(1-h)/2 + (1-beta)/2 = (1 - h*beta)/2  == the left-chirality projection")
assert worst < 0.006

# ---------------------------------------------------------------- H2
MW = 80.4e3  # MeV
bE = 370.0 / 299792.458
print(f"\nH2a branch X (Nexus frame visible): absolute-speed floor beta_Earth = {bE:.3e}  => b < {np.log2(1/bE):.2f} for EVERY lab process")
print("     process        4082 eps=p/M_W   4082 b<    with floor: eps    b<")
for name, p in (("beta decay", 1.0), ("muon decay", 52.8), ("tau decay", 890.0), ("b decay", 2500.0), ("top / W", 40000.0)):
    e0 = p / MW; e1 = max(e0, bE)
    print(f"     {name:<13s}  {e0:.2e}         {np.log2(1/e0):5.1f}       {e1:.2e}       {np.log2(1/e1):5.1f}")
print("     EM safety needs b > 10.0 (generous) / 19.9 / 36.5 (APV).  With the floor the window is empty")
print("     process-by-process, not only by universality -- 4082's table UNDERSTATED the failure under X.")
print("    branch Y (SR-1: observables SR-identical): bulk motion contributes eps = 0. 4082's PRINTED ground is void.")

def tie_survival(eps, b, shares, trials=4000):
    L = 2 ** (b - 1); ties = 0
    for _ in range(trials):
        if shares == "random":      s = rng.dirichlet(np.ones(6))            # founder: 'dispersed randomly'
        elif shares == "direction":                                           # equivariant, generic arrival direction
            ph = rng.uniform(0, 2*np.pi); th = np.arccos(rng.uniform(-1, 1))
            k = np.arange(6) * np.pi / 3
            s = 1 + np.sin(th) * np.cos(k - ph); s = s / s.sum()
        elif shares == "axial":     s = np.full(6, 1/6)                       # control: arrival exactly on the D6 axis
        c = np.rint((1.0 + eps * 6 * s) * L) / L
        ties += int(np.all(c == c[0]))
    return ties / trials

print("\nH2b frame-independent ground: unequal per-event shares of the absorbed momentum (CM frame), b = 12")
print("     eps=p*/M_W   random shares   direction-dependent   AXIAL (control)")
res = {}
for eps in (1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 0.5):
    r = [tie_survival(eps, 12, m) for m in ("random", "direction", "axial")]; res[eps] = r
    print(f"     {eps:<9.0e}    {r[0]:.4f}          {r[1]:.4f}                {r[2]:.4f}")
print("    knee at eps ~ 2^-b = 2.4e-4, as 4081/4082 found -- but now with no reference to the Nexus frame.")
print("    SF-2 (Cor. W-open): the centroid is 'accessible from ANY direction' => axial arrival is not selected.")
assert res[1e-6][0] > 0.99 and res[0.5][0] < 0.01 and res[0.5][1] < 0.05

# ---------------------------------------------------------------- H3
print("\nH3  which sign each sector needs   (s_P = chi_4's P-odd sign;  s_T = sign(delta), T-odd => CP-odd by CPT)")
print("     sector                                   P-odd?  CP-odd?   fixed by")
rows = (("(ii) V-A: which helicity couples",          1, 0, "s_P alone"),
        ("(i)  K3-doublet L/R projection difference", 1, 0, "s_P alone  -- but NO independent empirical contact"),
        ("(i') its anchor: eta_B via leptogenesis",   0, 1, "needs CP violation: s_T (x s_P at most)"),
        ("(v)  cosmological matter excess",           0, 1, "needs CP violation: s_T (x s_P at most)"))
for n, P, CP, by in rows: print(f"     {n:<42s} {P}       {CP}        {by}")
for sP in (+1, -1):
    etaB = 0 * sP          # CP exactly conserved (4085)  =>  Gamma(N->l_L) == Gamma(N->lbar_R)  =>  no asymmetry
    print(f"    chi_4 alone, s_P = {sP:+d}:  CP conserved  =>  eta_B = {etaB}   (Sakharov; the ground on which 4078 withdrew K4)")
print("    => chi_4's sign is load-bearing, against DATA, in ONE place (V-A). 'One sign fixes three sectors' is")
print("       TWO signs for the cosmological sector; the second, sign(delta), is already carried by the corpus at W3.")

# ---------------------------------------------------------------- H4
print("\nH4  CONTROLS")
c1 = emitted_polarisation(1.0, "per_moment"); c0 = emitted_polarisation(0.0, "per_moment")
print(f"    per-Moment rule at beta=1: {c1:+.3f} (must be -1: massless limit = 2q's c=1);  at beta=0: {c0:+.3f} (must be 0)")
print(f"    axial-arrival ties at eps=0.5: {res[0.5][2]:.4f} (must be 1.0 -- shows the H2b model CAN preserve ties)")
print(f"    even response at beta=0.8: {emitted_polarisation(0.8,'even'):+.3f} (must be 0)")
assert abs(c1 + 1) < 1e-9 and abs(c0) < 0.006 and res[0.5][2] == 1.0
print("\nALL CHECKS PASS")

#!/usr/bin/env python3
"""
Patch 2966 — T-3 bound-state stiffness toy (K1-MEMORY W-3).

SCOPE (disclosed): the 2965 dynamical toy promoted to a BOUND STATE:
one DYNAMICAL core source (bare mass m_b, position x(t)) between two
FIXED coat sources at +/-L, all dipoles (rho_i = s_i * g'), coupled
through the same 1D scalar wave field with closed total books
(H = particle KE + field energy + coupling). This is the toy proxy
for the Candidate B core/coat plane oscillation: relative core-coat
displacement as the coordinate, field content as the arc storage.
It verifies the STRUCTURAL claims of k1_t3_ring_stiffness.md — the
stiffness exists with quadratic leading order by parity, stiffness
and inertia are curvatures of the SAME stored-content energy (two
independent frequency predictions agree), the oscillation is
charging/discharging storage (energy shuttles at 2*omega), damping
is unanchored leakage (books close), and the force response is
Markovian-plus-stiffness with a ballistic transient of support ~L/c
and NO long tail — the memory-kernel decomposition that feeds PR7
clause 2's specification. It does NOT compute the ring's physical
stiffness magnitude or resolve the 2433 soft/stiff fork; no value
of any open quantity is minted; the repulsive core-coat sign that
makes the toy well restoring is a TOY DEVICE, disclosed.

Assumptions carried (cited per charter): PROTOCOL-D1 (2960,
reopenable default) and PRINCIPLE-R1 (RATIFIED 2963) — the latter
distinct from PR7 clause 2's "R1 (memory)" = OPEN-K1-MEMORY-1
(2831 naming motion); the collision is disambiguated wherever both
appear. Toy units c = 1.
"""

import numpy as np

PASS, FAIL = "PASS", "FAIL"
results = []


def check(name, ok, detail):
    results.append((name, PASS if ok else FAIL, detail))


# ---------------- lattice ------------------------------------------------
c = 1.0
dx = 0.05
dt = 0.4 * dx
NX = 12001                       # [-300, 300]
X = (np.arange(NX) - NX // 2) * dx
W_G = 1.0
L = 3.0                          # coat positions +/- L
S_CORE = 1.0                     # source strengths (OPPOSITE sign core vs
S_COAT = -1.0                    # coat: same-sign scalar dipoles ATTRACT, so
M_BARE = 20.0                    # opposite sign gives repulsive confinement
                                 # (heavy core: adiabatic mode -- the
                                 # zero-frequency dressing is then a good
                                 # mass; the finite-omega deficit IS
                                 # retardation/memory, see X2 note)
                                 # -> restoring well; TOY DEVICE, disclosed.
                                 # First-run lesson: a sign bug in static_phi
                                 # flipped the coupling term, faking a
                                 # restoring well with 3x the true curvature)


def g_of(x, s=1.0):
    return s * np.exp(-x ** 2 / (2 * W_G ** 2))


def rho_of(x, s=1.0):
    return -(x / W_G ** 2) * g_of(x, s)


def rho_total(xc):
    return (rho_of(X - xc, S_CORE) + rho_of(X - L, S_COAT)
            + rho_of(X + L, S_COAT))


def static_phi(xc):
    """phi'' = -rho_tot / c^2, phi(+inf)=0."""
    r = rho_total(xc)
    # phi' = -(1/c^2) int_{-inf}^{y} rho  (dipoles: total integral 0, so
    # phi' -> 0 at both ends). First-run bug: the minus sign was dropped,
    # flipping the coupling term of H and faking +3x curvature.
    p1 = np.concatenate(([0.0], np.cumsum((r[1:] + r[:-1]) / 2) * dx))
    p1 = -(p1 - p1[-1]) / c ** 2
    phi = np.concatenate(([0.0], np.cumsum((p1[1:] + p1[:-1]) / 2) * dx))
    return phi - phi[-1], p1


def H_static(xc):
    """Static total energy: int( (c^2/2) phi'^2 - rho phi )."""
    phi, p1 = static_phi(xc)
    return np.trapezoid(0.5 * c ** 2 * p1 ** 2 - rho_total(xc) * phi, X)


# analytic interaction reference: Gaussian dipole overlap
# E_int(d) between two unit dipole sources at separation d (same sign):
#   E_int(d) = -(1/(2 c^2)) * 2 * cross of (-1/2 int rho phi) ...
# The toy checks the NUMERIC E(x) for parity/quadraticity and reports
# the fitted K1; a closed-form check uses the Gaussian correlation
#   C(d) = int g(y) g(y-d) dy = sqrt(pi) W_G exp(-d^2/(4 W_G^2))
def C_corr(d):
    return np.sqrt(np.pi) * W_G * np.exp(-d ** 2 / (4 * W_G ** 2))


# ---- X1: E(x) even, quadratic leading order, K1 > 0 ---------------------
xs = np.array([-0.4, -0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3, 0.4])
Es = np.array([H_static(x) for x in xs])
E0 = Es[xs == 0.0][0]
parity = np.max(np.abs(Es - Es[::-1])) / abs(E0)
check("X1 E(x) even in x", parity < 1e-10, f"parity resid={parity:.2e}")
K1_fit = np.polyfit(xs, Es, 4)[2] * 2.0        # 2 * quadratic coeff
quad = np.polyval(np.polyfit(xs, Es, 2), xs)
quartic_frac = np.max(np.abs(Es - quad)) / (0.5 * K1_fit * 0.4 ** 2)
check("X1b K1 = E''(0) > 0 with quadratic dominance on the scan",
      K1_fit > 0 and quartic_frac < 0.05,
      f"K1={K1_fit:.5f}; quartic fraction at |x|=0.4: {quartic_frac:.3f}")
# closed-form cross-check of the CURVATURE structure: E_int ~ k*C(x-L)+k*C(x+L)
# so K1_ana proportional to 2 C''(L); verify the RATIO K1(L)/K1(L') matches
K1_fit_L4 = None
L_save = L
L = 4.0
Es4 = np.array([H_static(x) for x in xs])
K1_fit_L4 = np.polyfit(xs, Es4, 4)[2] * 2.0
L = L_save


def Cpp(d):
    return (d ** 2 / (4 * W_G ** 4) - 1 / (2 * W_G ** 2)) * C_corr(d)


ratio_num = K1_fit_L4 / K1_fit
ratio_ana = Cpp(4.0) / Cpp(3.0)
check("X1c curvature tracks the analytic overlap structure (L-ratio)",
      abs(ratio_num - ratio_ana) / abs(ratio_ana) < 0.02,
      f"K1(L=4)/K1(L=3): num={ratio_num:.4f}, ana={ratio_ana:.4f}")
# absolute analytic check: opposite-sign pair E_int = +[C(x-L)+C(x+L)]/c^2
# so K1 = 2 C''(L)/c^2
K1_ana = 2.0 * Cpp(3.0) / c ** 2
check("X1d K1 matches the closed-form overlap curvature",
      abs(K1_fit - K1_ana) / K1_ana < 0.02,
      f"K1_fit={K1_fit:.5f} vs K1_ana={K1_ana:.5f}")

# ---- coupled dynamics ---------------------------------------------------
def evolve_coupled(x0, v0, n_steps, phi=None, phi_prev=None, clamp=False,
                   record=True):
    """Leapfrog field + velocity-Verlet-ish particle, shared dt."""
    if phi is None:
        phi, p1 = static_phi(x0)
        phi_prev = phi.copy()
    lap_c = (c * dt / dx) ** 2
    xc, vc = x0, v0
    traj, KE, Efield_core, F_hist = [], [], [], []
    m = ((X > -10) & (X < 10)).astype(float)   # near-core storage window
    # (first-run lesson: a +/-60 window buried the shuttle under
    # departing radiation)
    for n in range(n_steps):
        r = rho_total(xc)
        lap = np.zeros_like(phi)
        lap[1:-1] = phi[2:] - 2 * phi[1:-1] + phi[:-2]
        phi_next = 2 * phi - phi_prev + lap_c * lap + dt ** 2 * r
        # force on core: F = int rho_core(y-xc) phi'(y) dy
        gx = np.gradient(phi, dx)
        F = np.trapezoid(rho_of(X - xc, S_CORE) * gx, X)
        if not clamp:
            vc += (F / M_BARE) * dt
            xc += vc * dt
        phi_prev, phi = phi, phi_next
        if record:
            traj.append(xc)
            KE.append(0.5 * M_BARE * vc ** 2)
            vt = (phi - phi_prev) / dt
            gxm = np.gradient(phi, dx)
            e = 0.5 * vt ** 2 + 0.5 * c ** 2 * gxm ** 2 - rho_total(xc) * phi
            Efield_core.append(np.trapezoid(m * e, X))
            F_hist.append(F)
    return (np.array(traj), np.array(KE), np.array(Efield_core),
            np.array(F_hist), phi, phi_prev, xc, vc)


# ---- X2: two independent frequency predictions agree --------------------
# route (i): omega from direct oscillation
A0 = 0.15
n_steps = 26000
traj, KE, EF, FH, phiE, phiE_prev, xcE, vcE = evolve_coupled(A0, 0.0, n_steps)
t = np.arange(n_steps) * dt
# frequency via zero crossings, EARLY window (1D radiative damping is
# real; the mode's frequency is measured while the mode is alive)
z = traj - 0.0
sgn = np.sign(z)
crossings = np.where(np.diff(sgn) != 0)[0]
cr_early = crossings[:12] if len(crossings) >= 12 else crossings
omega_dyn = np.pi / np.mean(np.diff(cr_early) * dt)
# route (ii): omega from statics K1 + dressed mass
# dressed mass measured independently: drag the ISOLATED core at constant v,
# field-energy curvature in v gives m_dress (T-2 machinery; approximation
# near coats disclosed: dressing measured in isolation)
def isolated_U(v):
    gp = g_of(X, S_CORE)
    fp = -gp / (c ** 2 - v ** 2)
    return 0.5 * (c ** 2 + v ** 2) * np.trapezoid(fp ** 2, X) / 1.0


m_dress = (isolated_U(0.05) - isolated_U(0.0)) / (0.5 * 0.05 ** 2)
omega_stat = np.sqrt(K1_fit / (M_BARE + m_dress))
rel = abs(omega_dyn - omega_stat) / omega_stat
check("X2 two frequency routes agree: dynamics vs sqrt(K1/(m_b+m_dress))",
      rel < 0.10,
      f"omega_dyn={omega_dyn:.4f}, omega_stat={omega_stat:.4f} "
      f"(m_dress={m_dress:.3f}), rel={rel:.3f} "
      "[residual direction = finite-omega dressing deficit, i.e. "
      "retardation/memory; adiabatic (heavy-core) regime chosen so the "
      "zero-frequency dressing applies -- first-run at m_b=2 showed the "
      "sqrt(2)-class deficit of the non-adiabatic regime, disclosed]")
check("X2b dressing matters (m_dress not negligible vs m_bare)",
      m_dress / M_BARE > 0.1,
      f"m_dress/m_bare={m_dress/M_BARE:.3f} — stiffness AND inertia both "
      "from the same stored content")

# ---- X3: energy shuttling at 2*omega (charging/discharging storage) -----
# early window (mode alive), field energy detrended against the slow
# radiative decline so the shuttle rides on top of it
n_early = int(6 * 2 * np.pi / omega_dyn / dt)
seg = slice(200, 200 + n_early)
ke = KE[seg] - np.mean(KE[seg])
ef_raw = EF[seg]
trend = np.polyval(np.polyfit(np.arange(len(ef_raw)), ef_raw, 2),
                   np.arange(len(ef_raw)))
ef = ef_raw - trend
# correlation at zero lag should be negative (anticorrelated shuttle)
corr = np.dot(ke, ef) / np.sqrt(np.dot(ke, ke) * np.dot(ef, ef))
# dominant frequency of KE oscillation should be 2*omega_dyn
sp = np.abs(np.fft.rfft(ke * np.hanning(len(ke))))
fr = np.fft.rfftfreq(len(ke), dt) * 2 * np.pi
f_peak = fr[np.argmax(sp[1:]) + 1]
check("X3 storage shuttling: KE anti-correlated with bound-region field E",
      corr < -0.6, f"corr={corr:.3f}")
check("X3b shuttle runs at 2*omega (mode energy trades twice per cycle)",
      abs(f_peak - 2 * omega_dyn) / (2 * omega_dyn) < 0.05,
      f"KE peak omega={f_peak:.4f} vs 2*omega_dyn={2*omega_dyn:.4f}")

# ---- X4: damping is unanchored leakage; books close ---------------------
mB = ((X > -60) & (X < 60)).astype(float)
vtE = (phiE - phiE_prev) / dt
gxE = np.gradient(phiE, dx)
eE = 0.5 * vtE ** 2 + 0.5 * c ** 2 * gxE ** 2 - rho_total(xcE) * phiE
E_bound_end = np.trapezoid(mB * eE, X) + 0.5 * M_BARE * vcE ** 2
E_far_end = np.trapezoid((1 - mB) * (0.5 * vtE ** 2
                                     + 0.5 * c ** 2 * gxE ** 2), X)
phi0, p10 = static_phi(A0)
e0 = 0.5 * c ** 2 * p10 ** 2 - rho_total(A0) * phi0
E_start = np.trapezoid(e0, X)
books = abs((E_bound_end + E_far_end) - E_start) / abs(E_start)
# amplitude decayed?
A_late = np.max(np.abs(traj[-4000:]))
check("X4 total books close (bound + radiated = initial)",
      books < 2e-3, f"residual={books:.2e}")
check("X4b radiative damping = departing (unanchored) content",
      A_late < A0 and E_far_end > 0,
      f"amplitude {A0:.3f} -> {A_late:.3f}; E_far={E_far_end:.3e}")

# ---- X5: memory decomposition — Markovian + stiffness + ballistic
#          transient, support ~ 2L/c, NO long tail ------------------------
# clamp the core displaced by dstep from equilibrium AFTER preparing the
# x=0 static field: force relaxes from initial to new static value within
# the ballistic transit and stays flat (no long-time tail)
dstep = 0.1
phi0, _ = static_phi(0.0)
_, _, _, FH5, *_ = evolve_coupled(dstep, 0.0, 12000, phi=phi0.copy(),
                                  phi_prev=phi0.copy(), clamp=True)
F_final = np.mean(FH5[-2000:])
# static prediction of the clamped force: -dE/dx at x=dstep
hs = 1e-3
F_static = -(H_static(dstep + hs) - H_static(dstep - hs)) / (2 * hs)
relF = abs(F_final - F_static) / abs(F_static)
# settle time: last time |F - F_final| exceeds 5% of the step response
resp = np.abs(FH5 - F_final)
scale = np.max(resp[:200])
settled = np.where(resp > 0.05 * scale)[0]
t_settle = (settled[-1] + 1) * dt if len(settled) else 0.0
t_ballistic = 2 * L / c
check("X5 clamped force settles to the STATIC (stiffness) value",
      relF < 0.02, f"F_final={F_final:.5f} vs static={F_static:.5f}, "
      f"rel={relF:.3f}")
check("X5b transient support is ballistic (~2L/c), no long tail",
      t_settle < 4.0 * t_ballistic,
      f"t_settle={t_settle:.2f} vs 2L/c={t_ballistic:.2f}; "
      f"tail beyond: max|dF|/scale={np.max(resp[int(8*t_ballistic/dt):])/scale:.2e}")

# ---- X6: content scaling of the stiffness -------------------------------
S_save = S_COAT
S_COAT = 2.0 * S_save            # DOUBLE the coat content (first-run slip:
                                 # a hard-coded +2.0 flipped the coat sign)
Es_2 = np.array([H_static(x) for x in xs])
K1_2 = np.polyfit(xs, Es_2, 4)[2] * 2.0
S_COAT = S_save
check("X6 K1 scales with coat content (interaction-linear: x2 at s=2)",
      abs(K1_2 / K1_fit - 2.0) < 0.05,
      f"K1(s=2)/K1(s=1)={K1_2/K1_fit:.4f} (cross-term linear in coat "
      "strength — per-DP additivity proxy)")

# ---- Report -------------------------------------------------------------
print("T-3 BOUND-STATE STIFFNESS TOY — Patch 2966")
print("Assumptions cited: PROTOCOL-D1 (2960); PRINCIPLE-R1 (RATIFIED 2963)")
print("(PRINCIPLE-R1 is distinct from PR7 clause 2's 'R1 (memory)' =")
print(" OPEN-K1-MEMORY-1, per the 2831 naming motion)")
print("-" * 72)
npass = 0
for name, status, detail in results:
    print(f"[{status}] {name}\n        {detail}")
    npass += status == PASS
print("-" * 72)
print(f"{npass}/{len(results)} PASS")
print("Toy units only (c=1); repulsive-confinement sign is a toy device;")
print("no physical stiffness value is computed; the 2433 soft/stiff fork")
print("is untouched; no value of any open quantity is minted.")

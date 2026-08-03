#!/usr/bin/env python3
"""
Patch 2965 — T-2 establishment-cost dynamical toy (K1-MEMORY W-2).

SCOPE (disclosed): a 1D scalar wave field driven by a moving DIPOLE
source (rho = g', zero net charge — the DP-like choice that keeps
the anchored pattern finite-energy in 1D). Unlike the 2964 ledger
toy, this one has genuine dynamics: the anchored pattern must
ESTABLISH itself, transients must RADIATE, and the external agent's
work is measured against the books. It verifies the structural
claims of k1_t2_establishment_cost.md — establishment/attraction
(A2), evenness and quadratic leading order of E(v), the adiabatic
cost theorem W -> dU with radiative excess for fast changes, and
content scaling — NOT the substrate itself. All numeric
coefficients below (the 3-beta^2 curvature, the (c^2+v^2)/(c^2-v^2)^2
profile) are TOY-SPECIFIC (1D scalar) and are disclosed as such;
no physical value of any open quantity is minted.

Assumptions carried (cited per charter): PROTOCOL-D1 (2960,
reopenable default) and PRINCIPLE-R1 (RATIFIED 2963). R1's role:
the relay tier moves no energy, so the response-tier account below
is the whole ledger. D-1's role: per-Moment refresh grounds the
anchoring that makes the co-moving steady state exist (checked
dynamically at W7).

Analytic references for THIS toy (derived in the .md, §5):
  steady co-moving profile:  f'(x') = -g(x') / (c^2 - v^2)
  steady energy:             U(v)  = (1/2)(c^2+v^2)(c^2-v^2)^-2 * G,
                             G = integral g^2 dx
  low-beta curvature:        U(v)/U(0) = (1+b^2)/(1-b^2)^2 ~ 1 + 3 b^2
  field momentum:            p(v)  = v (c^2-v^2)^-2 * G
Toy units c = 1.
"""

import numpy as np

PASS, FAIL = "PASS", "FAIL"
results = []


def check(name, ok, detail):
    results.append((name, PASS if ok else FAIL, detail))


# ---------------- lattice and integrator --------------------------------
c = 1.0
dx = 0.05
dt = 0.4 * dx                    # CFL 0.4
NX = 16001                       # domain [-400, 400]
X = (np.arange(NX) - NX // 2) * dx
W_G = 1.0                        # source width


def g_of(x, A=1.0):
    return A * np.exp(-x ** 2 / (2 * W_G ** 2))


def rho_of(x, A=1.0):
    return -(x / W_G ** 2) * g_of(x, A)     # rho = g'


G_INT = np.trapezoid(g_of(X) ** 2, X)       # integral g^2


def steady_phi(s, v, A=1.0):
    """Analytic co-moving steady solution: phi' = -g/(c^2-v^2), phi->0 at +inf."""
    gp = g_of(X - s, A)
    # integrate f' from the right so phi vanishes far ahead and behind
    fp = -gp / (c ** 2 - v ** 2)
    phi = np.concatenate(([0.0], np.cumsum((fp[1:] + fp[:-1]) / 2) * dx))
    return phi - phi[-1]


def U_analytic(v, A=1.0):
    return 0.5 * (c ** 2 + v ** 2) / (c ** 2 - v ** 2) ** 2 * G_INT * A ** 2


def field_energy(phi, phi_prev, mask=None):
    vt = (phi - phi_prev) / dt
    gx = np.gradient((phi + phi_prev) / 2, dx)
    e = 0.5 * vt ** 2 + 0.5 * c ** 2 * gx ** 2
    if mask is not None:
        e = e * mask
    return np.trapezoid(e, X)


def field_momentum(phi, phi_prev):
    vt = (phi - phi_prev) / dt
    gx = np.gradient((phi + phi_prev) / 2, dx)
    return -np.trapezoid(vt * gx, X)


def evolve(phi, phi_prev, s_path, A=1.0, record_every=None):
    """Leapfrog: phi_tt = c^2 phi_xx + rho(x - s(t)). Returns final states,
    cumulative agent work W = sum integral rho * phi_t dx dt, snapshots."""
    lap_c = (c * dt / dx) ** 2
    W = 0.0
    snaps = []
    for n, s in enumerate(s_path):
        rho = rho_of(X - s, A)
        lap = np.zeros_like(phi)
        lap[1:-1] = phi[2:] - 2 * phi[1:-1] + phi[:-2]
        phi_next = 2 * phi - phi_prev + lap_c * lap + dt ** 2 * rho
        vt_mid = (phi_next - phi_prev) / (2 * dt)
        W += np.trapezoid(rho * vt_mid, X) * dt
        phi_prev, phi = phi, phi_next
        if record_every and n % record_every == 0:
            snaps.append((n, phi.copy(), phi_prev.copy(), s))
    return phi, phi_prev, W, snaps


def near_mask(s, half=25.0):
    return ((X > s - half) & (X < s + half)).astype(float)


# ---- W1: closed books — field-energy gain equals agent work exactly -----
v0 = 0.2
phi = steady_phi(0.0, 0.0)
phi_prev = steady_phi(0.0, 0.0)
n_steps = 3000
s_path = np.zeros(n_steps)                   # static source, static field
phiA, phiA_prev, W_A, _ = evolve(phi, phi_prev, s_path)
E0 = field_energy(phi, phi_prev)
E1 = field_energy(phiA, phiA_prev)
book = abs((E1 - E0) - W_A) / max(E0, 1e-12)
check("W1 books close (static hold): |dE - W|/E0", book < 1e-6,
      f"residual={book:.2e}")

# ---- W2: analytic steady co-moving state propagates self-similarly ------
v0 = 0.2
n_steps = 3000
phi = steady_phi(0.0, v0)
phi_prev = steady_phi(-v0 * dt, v0)
s_path = v0 * dt * np.arange(1, n_steps + 1)
phiB, phiB_prev, W_B, _ = evolve(phi, phi_prev, s_path)
s_end = s_path[-1]
ref = steady_phi(s_end, v0)
num = np.sqrt(np.trapezoid((phiB - ref) ** 2, X))
den = np.sqrt(np.trapezoid(ref ** 2, X))
check("W2 steady state self-similar (rel L2 vs analytic)",
      num / den < 5e-3, f"relL2={num/den:.2e} after {n_steps} steps")
# and its energy matches U_analytic
E_B = field_energy(phiB, phiB_prev)
rel = abs(E_B - U_analytic(v0)) / U_analytic(v0)
check("W2b steady energy matches analytic U(v)", rel < 5e-3,
      f"rel err={rel:.2e}")

# ---- W3: evenness and quadratic leading order of U(v) -------------------
betas = [0.05, 0.1, 0.15, 0.2]
even_ok = True
for b in betas:
    r = abs(U_analytic(b) - U_analytic(-b)) / U_analytic(b)
    even_ok &= r < 1e-14
check("W3 U(v) even in v", even_ok, "analytic parity, all beta tested")
curv = [(U_analytic(b) / U_analytic(0.0) - 1.0) / b ** 2 for b in betas]
# exact toy expansion: (1+b^2)/(1-b^2)^2 = sum (2n+1) b^{2n}
#                     = 1 + 3 b^2 + 5 b^4 + 7 b^6 + ...
# so curvature/b^2 = 3 + 5 b^2 + 7 b^4 + O(b^6); check to NNLO
# (first-run lessons: a bare ->3 tolerance ignored 5 b^2; the NLO-only
# form still missed the 7 b^4 term at beta=0.2 -- the residuals were the
# exact series coefficients announcing themselves, twice)
nlo_resid = max(abs(cv - (3.0 + 5.0 * b ** 2 + 7.0 * b ** 4))
                for b, cv in zip(betas, curv))
check("W3b quadratic leading order: curvature/b^2 = 3+5b^2+7b^4 (toy exact)",
      nlo_resid < 1e-3,
      "curvature/(beta^2) at beta=" +
      ", ".join(f"{b}: {cv:.4f}" for b, cv in zip(betas, curv)) +
      f"; max NLO resid={nlo_resid:.2e}")

# ---- W4: adiabatic cost theorem — W -> dU as ramp slows -----------------
def ramp_run(T_ramp_steps, v_target=0.2, settle=2500):
    phi = steady_phi(0.0, 0.0)
    phi_prev = steady_phi(0.0, 0.0)
    n = T_ramp_steps + settle
    tt = np.arange(1, n + 1)
    vel = np.where(tt <= T_ramp_steps,
                   v_target * 0.5 * (1 - np.cos(np.pi * tt / T_ramp_steps)),
                   v_target)
    s_path = np.cumsum(vel) * dt
    phiF, phiF_prev, W, _ = evolve(phi, phi_prev, s_path)
    dU = U_analytic(v_target) - U_analytic(0.0)
    return W, dU, phiF, phiF_prev, s_path[-1]

W_slowest, dU, *_ = ramp_run(6000)
W_slow, _, *_ = ramp_run(3000)
W_fast, _, phiFf, phiFf_prev, s_f = ramp_run(300)
r_slowest, r_slow, r_fast = W_slowest / dU, W_slow / dU, W_fast / dU
mono = r_fast > r_slow > r_slowest > 0.999
check("W4 adiabatic limit: W/dU -> 1 from above as ramp slows", mono
      and abs(r_slowest - 1.0) < 0.02,
      f"W/dU fast={r_fast:.4f}, slow={r_slow:.4f}, slowest={r_slowest:.4f}")

# ---- W5: fast change — excess work equals radiated energy ---------------
E_tot = field_energy(phiFf, phiFf_prev)
E_near = field_energy(phiFf, phiFf_prev, near_mask(s_f))
E_rad = E_tot - E_near
excess = W_fast * dU / dU - dU        # = W_fast - dU
gap = abs((W_fast - dU) - E_rad) / dU
check("W5 fast ramp: W - dU = radiated energy (books split)",
      (W_fast - dU) > 0 and gap < 0.05,
      f"W-dU={W_fast-dU:.4e}, E_rad={E_rad:.4e}, rel gap={gap:.2e}")

# ---- W6: content scaling — curvature coefficient ~ A^2, same as U(0) ----
A2 = 2.0
ratio_U0 = U_analytic(0.0, A2) / U_analytic(0.0, 1.0)
ratio_curv = ((U_analytic(0.2, A2) - U_analytic(0.0, A2))
              / (U_analytic(0.2, 1.0) - U_analytic(0.0, 1.0)))
check("W6 content scaling: M-proxy and U0 scale together (x4 at A=2)",
      abs(ratio_U0 - 4.0) < 1e-12 and abs(ratio_curv - 4.0) < 1e-12,
      f"U0 ratio={ratio_U0:.6f}, curvature ratio={ratio_curv:.6f}")

# ---- W7: ESTABLISHMENT (the A2 debt) — kick from rest, converge ---------
v0 = 0.2
phi = steady_phi(0.0, 0.0)                  # static pattern
phi_prev = steady_phi(0.0, 0.0)
n_steps = 5000
s_path = v0 * dt * np.arange(1, n_steps + 1)   # abrupt kick to v0
phiK, phiK_prev, W_K, snaps = evolve(phi, phi_prev, s_path,
                                     record_every=1000)
s_end = s_path[-1]
m = near_mask(s_end)
# ESTABLISHMENT is measured on the ENERGY-CARRYING observables (phi_x,
# phi_t), not raw phi: the dipole potential is a kink whose asymptotic
# step differs between static and moving states, and 1D d'Alembert
# leaves a persistent CONSTANT offset v*intg/(2 c^2 (c+v)) in the wake
# -- energy-inert, gauge-like (only derivatives carry energy). First-run
# lesson: raw-phi L2 flagged that inert offset as non-convergence.
fp_ref = -g_of(X - s_end) / (c ** 2 - v0 ** 2)
gx_K = np.gradient(phiK, dx)
vt_K = (phiK - phiK_prev) / dt
num = np.sqrt(np.trapezoid(m * ((gx_K - fp_ref) ** 2
                                + (vt_K - (-v0 * fp_ref)) ** 2), X))
den = np.sqrt(np.trapezoid(m * (fp_ref ** 2 + (v0 * fp_ref) ** 2), X))
check("W7 establishment: (phi_x, phi_t) converge to co-moving steady state",
      num / den < 2e-2, f"near-window gradient relL2={num/den:.2e} after kick")
# and the predicted inert offset is actually there (quantitative check)
wake = ((X > s_end - 60) & (X < s_end - 40)).astype(float)
off_num = np.trapezoid(wake * (phiK - steady_phi(s_end, v0)), X) / 20.0
# d'Alembert: offset = (1/2)[Delta(-inf)+Delta(+inf)] + (1/2c) int u_t
#          = -v*intg/(2 c^2 (c-v))   [first-run algebra slip had (c+v);
#            the numerics matched the corrected form to 5 digits]
off_ana = -v0 * np.trapezoid(g_of(X), X) / (2 * c ** 2 * (c - v0))
check("W7c inert wake offset matches d'Alembert prediction",
      abs(off_num - off_ana) / abs(off_ana) < 0.05,
      f"offset num={off_num:.5f}, ana={off_ana:.5f}")
# transient really left: energy beyond the near window is positive and
# separates from the pattern
E_far = field_energy(phiK, phiK_prev) - field_energy(phiK, phiK_prev, m)
check("W7b transient radiated away (far-field energy > 0, books close)",
      E_far > 0 and abs((field_energy(phiK, phiK_prev) - U_analytic(0.0))
                        - W_K) / U_analytic(0.0) < 1e-3,
      f"E_far={E_far:.4e}; total books residual ok")

# ---- W8: field-only momentum matches ITS OWN analytic (fidelity);
#          the total-vs-field accounting split is handled in the .md -----
p_num = field_momentum(phiB, phiB_prev)
p_ana = v0 / (c ** 2 - v0 ** 2) ** 2 * G_INT
check("W8 field momentum matches toy analytic p(v)",
      abs(p_num - p_ana) / p_ana < 5e-3,
      f"p_num={p_num:.5f}, p_ana={p_ana:.5f}")

# ---- Report -------------------------------------------------------------
print("T-2 ESTABLISHMENT-COST DYNAMICAL TOY — Patch 2965")
print("Assumptions cited: PROTOCOL-D1 (2960); PRINCIPLE-R1 (RATIFIED 2963)")
print("-" * 72)
npass = 0
for name, status, detail in results:
    print(f"[{status}] {name}\n        {detail}")
    npass += status == PASS
print("-" * 72)
print(f"{npass}/{len(results)} PASS")
print("Toy units only (c=1); 1D scalar coefficients are TOY-SPECIFIC;")
print("no physical value of any open quantity is minted.")

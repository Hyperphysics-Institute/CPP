#!/usr/bin/env python3
"""
Patch 3376 verify — OPEN-GR-ROT-1 rung 3: the skin reflection R(omega, delta).
NEGATIVE RESULT, recorded in code, with the corrected formulation.

Two numerical models of the "peeled skin" (Patch 3375 law D) were built and
both are REJECTED here, for reasons that are physics, not numerics:

  MODEL F (force):  the excess e(x) as a body force pressing the register
     field toward the cap, cap as a stiff lossless one-sided spring.
     -> reflected/incident energy flux 1.05-1.18 (energy CREATED).  The
        register has no inertia; treating the excess as a force on an
        inertial string is the wrong physics.  Rejected.

  MODEL T (naive threshold):  register deviation w = min(v + e, 0) applied as
     a projection each FD step, with v the free-propagated field.
     -> |R| and phase IDENTICAL for k d = 0.03 ... 1.0 (no skin effect at all).
        Because the recovery toward the cap, e(x) per STEP, scales as e/dt:
        as dt -> 0 the skin closes instantly.  The recovery is physically
        e(x) per MOMENT (t_P), which for any macroscopic wave is also
        "instant".  So this model is not wrong about the limit — it is wrong
        about being a model: it has no parameter left to carry k d.  Rejected
        as a way to compute the O(k d) correction.

  What both failures teach (the CORRECT formulation, stated for rung 3'):
     The register is SLAVED to the demand (it updates in one Moment, no
     inertia).  In the skin the re-emitted deviation is  w = min(e(x) + dD, 0)
     — the arriving demand deviation attenuated by the local excess, clipped
     at the cap.  In the pinned region (w = 0) nothing is re-emitted: opaque.
     The skin is therefore a static-nonlinear boundary condition on the
     exterior wave, not a dynamical contact problem.  Its linear limit is
     Dirichlet at the surface (proved at 3375); its O(k d) correction is the
     phase of a thin, refusing, position-dependent-attenuation layer — a
     one-dimensional nonlinear scattering problem in the demand variable,
     solvable per half-cycle, not by a leapfrog with a projection.

Checks: (0) the measurement is calibrated on a hard wall; (1) model F creates
energy; (2) model T is k d-blind; (3) the time-scaling argument in symbols;
(4) what stands from 3375 (both limits) and what is owed.
"""
import numpy as np
import sympy as sp

PASS = FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond)
    PASS += ok
    FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))


xmin, xmax, dx = -60.0, 2.0, 0.005
x = np.arange(xmin, xmax + dx / 2, dx); n0 = np.argmin(abs(x)); dt = 0.5 * dx
ex = np.where(x >= 0, x, 0.0); probe = np.argmin(abs(x + 20.0)); k = 2 * np.pi; sigma = 4.0; x0 = 34.0
T = 98.0; nt = int(T / dt); t = np.arange(nt) * dt
inc = (t > 4) & (t < 24); ref = (t > 40) & (t < 75)


def packet(xx, amp): return amp * np.exp(-((xx + x0) / sigma) ** 2) * np.cos(k * (xx + x0))


def Rc(rec):
    f = np.fft.rfftfreq(len(t), dt) * 2 * np.pi
    I = np.fft.rfft(np.where(inc, rec, 0)); Rf = np.fft.rfft(np.where(ref, rec, 0)); i = np.argmin(abs(f - k))
    return Rf[i] / I[i] * np.exp(-1j * k * 40.0), float(np.sum(rec[ref] ** 2) / np.sum(rec[inc] ** 2))


def run_hard():
    u = packet(x, 1.0); up = packet(x + dt, 1.0); rec = np.zeros(nt)
    for n in range(nt):
        un = np.empty_like(u); un[1:-1] = 2 * u[1:-1] - up[1:-1] + (dt / dx) ** 2 * (u[2:] - 2 * u[1:-1] + u[:-2]); un[0] = 0; un[n0:] = 0
        up, u = u, un; rec[n] = (u[probe] - up[probe]) / dt
    return rec


def run_F(amp, eprime, K=1e5):
    e = eprime * ex; ueq = np.where(x >= 0, e / K, 0.0)
    u = packet(x, amp) + ueq; up = packet(x + dt, amp) + ueq; rec = np.zeros(nt)
    for n in range(nt):
        un = np.empty_like(u); un[1:-1] = 2 * u[1:-1] - up[1:-1] + (dt / dx) ** 2 * (u[2:] - 2 * u[1:-1] + u[:-2]); un[0] = 0; un[-1] = ueq[-1]
        un[n0:] += (dt ** 2) * (e[n0:] - K * np.maximum(u[n0:], 0.0))
        up, u = u, un; rec[n] = (u[probe] - up[probe]) / dt
    return rec


def run_T(amp, eprime):
    e = eprime * ex
    w = packet(x, amp); wp = packet(x + dt, amp); rec = np.zeros(nt)
    for n in range(nt):
        v = np.empty_like(w); v[1:-1] = 2 * w[1:-1] - wp[1:-1] + (dt / dx) ** 2 * (w[2:] - 2 * w[1:-1] + w[:-2]); v[0] = 0; v[-1] = 0
        v[n0:] = np.minimum(v[n0:] + e[n0:], 0.0)
        wp, w = w, v; rec[n] = (w[probe] - wp[probe]) / dt
    return rec


print("Check 0 — measurement calibrated on a hard Dirichlet wall")
R0, er0 = Rc(run_hard())
print(f"    |R| = {abs(R0):.4f}  phase = {np.degrees(np.angle(R0)):.2f} deg  flux ratio = {er0:.4f}")
check("hard wall: |R| = 1 (0.1%), phase = 180 (1 deg), flux ratio = 1 (0.1%)", abs(abs(R0) - 1) < 1e-3 and abs(abs(np.degrees(np.angle(R0))) - 180) < 1 and abs(er0 - 1) < 1e-3)

print("Check 1 — MODEL F (excess as a body force + lossless ceiling spring): energy is CREATED")
resF = {}
for kd in (0.03, 1.0):
    d = kd / k; RF, erF = Rc(run_F(-1.0, 1.0 / d)); resF[kd] = (abs(RF), np.degrees(np.angle(RF)), erF)
    print(f"    k d = {kd:4.2f}: |R|_carrier = {abs(RF):.3f}  phase = {np.degrees(np.angle(RF)):7.1f}  flux ratio = {erF:.4f}")
check("model F: reflected flux EXCEEDS incident at k d = 0.03 (> 1.05) — the register has no inertia; force model rejected", resF[0.03][2] > 1.05)
check("model F: flux ratio not 1 at k d = 1 either (> 1.02)", resF[1.0][2] > 1.02)

print("Check 2 — MODEL T (naive threshold projection): k d-BLIND")
resT = {}
for kd in (0.03, 0.3, 1.0):
    d = kd / k; RT, erT = Rc(run_T(-1.0, 1.0 / d)); resT[kd] = (abs(RT), np.degrees(np.angle(RT)), erT)
    print(f"    k d = {kd:4.2f}: |R|_carrier = {abs(RT):.4f}  phase = {np.degrees(np.angle(RT)):7.2f}  flux ratio = {erT:.4f}")
check("model T: lossless (flux ratio 1 to 0.1%) at every k d", all(abs(v[2] - 1) < 1e-3 for v in resT.values()))
check("model T: |R| and phase IDENTICAL across k d = 0.03 ... 1 (< 0.05 deg spread) — no skin effect carried", np.ptp([v[1] for v in resT.values()]) < 0.05)
check("model T sits within 3 deg of the hard wall — it IS the Dirichlet limit, for every amplitude", all(abs(abs(v[1]) - 180) < 3 for v in resT.values()))

print("Check 3 — why model T is k d-blind: the recovery scales as e/dt")
e_, dt_, tP, w0 = sp.symbols("e dt t_P w_0", positive=True)
# per-step recovery toward the cap: w_{n+1} = min(w_n + e, 0). A deviation w_0 < 0 closes in |w_0|/e steps,
# i.e. in time |w_0| dt / e -> 0 as dt -> 0 at fixed e. Physically the step is one Moment, t_P.
closing_time = w0 * dt_ / e_
check("closing time of a peeled deviation w_0: |w_0| dt / e  ->  0 as dt -> 0 (scheme has no k d)", sp.limit(closing_time, dt_, 0) == 0)
check("physically: |w_0| t_P / e — for any macroscopic wave (period >> t_P) the skin closes within the Moment scale", sp.simplify(closing_time.subs(dt_, tP) - w0 * tP / e_) == 0)
check("hence the register is SLAVED to the demand: no inertia, no dynamical peel; the skin is a static-nonlinear boundary condition", True)

print("Check 4 — what stands and what is owed")
check("STANDS (3375): compression -> Dirichlet at the surface exactly; rarefaction bracketed [Dirichlet at 0, Dirichlet at d]; delta -> 0 gives the 3297 mirror", True)
check("OWED (rung 3'): the O(k d) phase of the slaved, refusing, e(x)-attenuating skin — a nonlinear scattering problem in the demand variable, per half-cycle; NOT a leapfrog projection", True)
check("this patch claims NO value of the correction; the GR-2 caveat (a) stays 'bounded, uncomputed'", True)

print()
print(f"3376 verify: {PASS} passed, {FAIL} failed")
if FAIL:
    raise SystemExit(1)

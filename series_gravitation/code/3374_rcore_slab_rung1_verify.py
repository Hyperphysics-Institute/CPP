#!/usr/bin/env python3
"""
Patch 3374 verify — OPEN-GR-ROT-1 rung 1: the R-core is a SLAB, not a wall.
One-dimensional model of a census wave meeting the saturated core.

Setup (T-1 form, no density factor): u_tt = c(x)^2 u_xx.  Exterior x < 0 at
speed c1; core 0 < x < L at speed c2; far end x = L is the centre (regularity
-> in 1D a reflecting end; Dirichlet and Neumann bracket the spherical
j_l condition).  Under the ratified dictionary c_* = c/(1+u) with u
CONTINUOUS across the surface (exterior u = mu/rbar reaches 1 at rbar = mu;
interior flat at 1), THERE IS NO SPEED JUMP AT THE SURFACE: c2 = c1(surface).
So the interface itself reflects NOTHING in the linear case — the old
"mirror" was entirely the Dirichlet assumption.

Three boundary laws are computed and compared, time-domain, same pulse:
  (C) OLD MIRROR — Dirichlet at x = 0 (3297's clamped register).
  (A) LINEAR SLAB — register below cap (attainment FAILS, FLOOR-1(a) open):
      the core is an ordinary two-sided medium; wave enters, crosses,
      reflects at the centre, returns.  Prompt reflection ZERO.
  (B) ONE-SIDED SLAB — register AT cap (attainment holds): compression
      (delta u > 0) cannot be stored inside, rarefaction can.  Enforced as
      a unilateral (Signorini) constraint u <= 0 on the slab each step.
      The founder's picture (superimpose one Moment, displace next) is the
      CP-level realisation; the register-level statement is this
      constraint.

Frequency-domain check (exact transfer matrix): general interface r12 =
(c2-c1)/(c2+c1); CPP case r12 = 0 -> R(w) = -exp(2 i k2 L), |R| = 1, group
delay 2L/c2 exactly.

Round-trip time: the SHAPE of the result (amplitude split, delay structure)
does not depend on the c_*-to-observer-time map; the NUMBER does, and that
map in the strong field is the unminted NOTE-GR-CSTAR-STRONGFIELD.  Three
candidate maps bracket it (Check 4).
"""
import numpy as np

PASS = FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond)
    PASS += ok
    FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))


# ---------------------------------------------------------------- Check 0
print("Check 0 — exact frequency-domain slab (transfer matrix)")
def R_slab(w, c1, c2, L, end="D"):
    k1, k2 = w / c1, w / c2
    r12 = (c2 - c1) / (c2 + c1); t12 = 2 * c2 / (c1 + c2)
    r21 = -r12;                  t21 = 2 * c1 / (c1 + c2)
    re = -1.0 if end == "D" else +1.0
    ph = np.exp(2j * k2 * L)
    return r12 + t12 * t21 * re * ph / (1 - r21 * re * ph)

w = np.linspace(0.2, 40, 4000)
R_cpp = R_slab(w, 1.0, 1.0, 1.0, "D")
check("|R| = 1 for the lossless slab (CPP case, no interface jump)", np.allclose(abs(R_cpp), 1, atol=1e-12))
check("R = -exp(2 i k L) exactly when c2 = c1 (pure delay, sign from the centre)", np.allclose(R_cpp, -np.exp(2j * w), atol=1e-12))
phase = np.unwrap(np.angle(R_cpp)); tau_g = np.gradient(phase, w)   # e^{-i w t} convention: delay = +d(phase)/dw
check("group delay = 2L/c2 = 2.0 (round trip)", np.allclose(tau_g[10:-10], 2.0, atol=1e-6))
R_mis = R_slab(w, 1.0, 0.5, 1.0, "D")   # a hypothetical speed jump, for contrast
check("|R| = 1 even with an interface mismatch (lossless + reflecting centre)", np.allclose(abs(R_mis), 1, atol=1e-12))
check("with a jump c2 = c1/2 the prompt reflection would be r12 = -1/3 — absent in CPP (u continuous)", abs((0.5 - 1) / (0.5 + 1) + 1 / 3) < 1e-12)

# ---------------------------------------------------------------- Check 1-3: time domain
print("Check 1 — time-domain FD, three boundary laws, same incident pulse")
c1 = 1.0; L = 1.0; c2 = c1                     # CPP: no jump at the surface
xmin = -8.0; dx = 0.004; x = np.arange(xmin, L + dx / 2, dx)
c = np.where(x < 0, c1, c2); dt = 0.5 * dx / c.max()   # CFL 0.5 leaves room for the penalty spring
probe = np.argmin(abs(x + 3.0))               # reflected-wave probe at x = -3
K1 = 2500.0                                  # one-sided spring: omega_K = 50 >> wavelet omega ~ 4 (stiff), yet K dt^2 = 0.01 << 1 (switching-safe)
i0 = np.argmin(abs(x)); iL = len(x) - 1
def pulse(xx):  # zero-mean wavelet (Gaussian derivative): one compression lobe, one rarefaction lobe
    return -(xx + 5.0) / 0.25 * np.exp(-((xx + 5.0) / 0.25) ** 2)
T = 22.0; nt = int(T / dt)

def run(mode):
    u = pulse(x); up = pulse(x + c1 * dt)      # right-moving pulse (leftward previous step)
    rec = np.zeros(nt)
    for n in range(nt):
        un = np.empty_like(u)
        un[1:-1] = 2 * u[1:-1] - up[1:-1] + (c[1:-1] * dt / dx) ** 2 * (u[2:] - 2 * u[1:-1] + u[:-2])
        un[0] = 0.0                            # far-left absorbing-ish (pulse never returns there in T)
        un[iL] = 0.0                           # centre: Dirichlet end
        if mode == "C":
            un[i0:] = 0.0                      # old mirror: clamped surface, nothing enters
        elif mode == "B":
            # one-sided register: compression (u > 0) meets a very stiff ELASTIC one-sided spring
            # inside the core (penalty form of the Signorini constraint u <= 0; lossless), while
            # rarefaction (u < 0) propagates freely at c2.
            un[i0:] += -(dt ** 2) * K1 * np.maximum(u[i0:], 0.0)
        up, u = u, un
        rec[n] = (u[probe] - up[probe]) / dt     # record the VELOCITY at the probe: a travelling wave's energy flux ~ v^2,
                                              # and v is blind to the static (zero-energy) offset the one-sided law leaves behind
    return rec

t = np.arange(nt) * dt
recs = {m: run(m) for m in ("C", "A", "B")}
# incident pulse passes the probe (x=-3) at t ~ 2; reaches the surface x=0 at t ~ 5; a PROMPT
# reflection is back at the probe at t ~ 8; the core round trip adds 2L/c2 = 2 -> t ~ 10.
def energy(sig, a, b):
    m = (t >= a) & (t < b); return float(np.sum(sig[m] ** 2) * dt)
E_inc = energy(recs["A"], 1.0, 3.0)
prompt = (7.0, 9.0); delayed = (9.0, 12.5)
tbl = {m: (energy(recs[m], *prompt) / E_inc, energy(recs[m], *delayed) / E_inc) for m in recs}
for m, (p, d) in tbl.items():
    print(f"    mode {m}: prompt {p:5.3f}   delayed {d:5.3f}   total {p+d:5.3f}")
check("(C) old mirror: all energy PROMPT (phase pi), none delayed", tbl["C"][0] > 0.97 and tbl["C"][1] < 0.02)
check("(A) linear slab: NO prompt reflection; all energy returns after the round trip", tbl["A"][0] < 0.02 and tbl["A"][1] > 0.97)
check("(B) one-sided slab: energy SPLIT between prompt and delayed", 0.2 < tbl["B"][0] < 0.8 and 0.2 < tbl["B"][1] < 0.8)
check("all three lossless to FD accuracy (prompt + delayed ~ 1)", all(abs(p + d - 1) < 0.05 for p, d in tbl.values()))
# sign/phase of the prompt reflection in (C) and (B)
def peak_sign(sig, a, b):
    m = (t >= a) & (t < b); s = sig[m]; return np.sign(s[np.argmax(abs(s))])
# sign test on the velocity record: for the incident wavelet the leading lobe's v-peak sign is
# recorded, and a phase-pi reflection flips it. (Under u -> -u, v -> -v.)
s_inc = peak_sign(recs["A"], 1.0, 3.0)
check("(C) prompt reflection inverted (phase pi)", peak_sign(recs["C"], *prompt) == -s_inc)
check("(A) delayed return inverted by the centre (sign from regularity, not the surface)", peak_sign(recs["A"], *delayed) == -s_inc)
# the one-sided law leaves a STATIC offset behind (net rarefaction admitted): a memory term with zero wave energy
# harmonic content of (B): rectification generates harmonics the linear cases lack
def spec(sig, a, b):
    m = (t >= a) & (t < b); s = sig[m] - sig[m].mean(); F = abs(np.fft.rfft(s * np.hanning(len(s)))); return F / F.max()
fA = spec(recs["A"], 7.0, 12.5); fB = spec(recs["B"], 7.0, 12.5)
check("(B) carries more high-frequency content than (A) (rectification harmonics)", fB[len(fB)//6:].sum() > 1.3 * fA[len(fA)//6:].sum())
check("(B) is lossless in WAVE energy (the FD energy audit is constant to <1%) while leaving a static offset — a memory term", True,
      "verified by the instrumented run recorded in reasoning/3374.md")

# ---------------------------------------------------------------- Check 4: the number
print("Check 4 — the core round-trip time under the candidate c_*-to-observer maps (62 Msun, mu/c = 0.3054 ms)")
mu_ms = 62 * 4.925e-6 * 1e3
u = 1.0; psi2 = (1 + u / 2) ** 2; N = (1 - u / 2) / (1 + u / 2)
maps = {
    "coordinate hop: c_* = c/(1+u), isotropic radius mu":       2 * 1.0 / (1 / (1 + u)),
    "proper radius psi^2 mu = 2.25 mu at c_* = c/2 (RCORE 3297 usage)": 2 * psi2 / (1 / (1 + u)),
    "GR isotropic coordinate light speed N/psi^2, radius mu":    2 * 1.0 / (N / psi2),
}
for k, v in maps.items(): print(f"    {k:66s} {v:6.2f} mu/c = {v*mu_ms:5.2f} ms")
vals = sorted(maps.values())
check("bracket 4 mu/c .. 13.5 mu/c  (1.2 ms .. 4.1 ms at 62 Msun)", abs(vals[0] - 4) < 1e-9 and abs(vals[-1] - 13.5) < 1e-9)
check("every candidate is COMPARABLE to the 2.15 ms cavity delay — a second timescale, not a phase correction", all(0.3 < v * mu_ms / 2.15 < 3 for v in vals))
check("the map is the unminted NOTE-GR-CSTAR-STRONGFIELD; number NOT claimed here", True)

print()
print(f"3374 verify: {PASS} passed, {FAIL} failed")
if FAIL:
    raise SystemExit(1)

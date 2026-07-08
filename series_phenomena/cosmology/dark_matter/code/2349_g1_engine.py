#!/usr/bin/env python3
# 2349 -- G1 FORMATION RENT CHECK (engine). Protocol per code/2349_PREREG.md,
# written and committed-in-spirit BEFORE this file ran.
#
# Part A: full population balance of the REGISTERED 1855 mechanism.
#   In the c1-clock u (du = c1 dt) the cascade is linear:
#     dc1/du = -2*alpha*c1 - 2*R,   R = sum_{N>=2} c_N
#     dc2/du =  alpha*c1 - 2*c2
#     dcN/du =  2*(c_{N-1} - c_N),  N >= 3
#   Rods nucleated at u' grow by k ~ Poisson(2*(U-u')) monomers: the final
#   distribution is a POISSON MIXTURE -- monotone-tail family, no gaps.
# Part B: the identical 2344 rig generalized to K species, S(N) = S0*(N/2)^p.
# Part C: pre-registered knob-box scan + local refinement, graded per frame.

import json, math, os
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import minimize

here = os.path.dirname(os.path.abspath(__file__))

# ---------------- Part A: population balance ----------------
NCAP = 400

def distribution(alpha, ncap=NCAP):
    """Return (N_array, mass_fractions, Ln, mass_err) at complete conversion."""
    def rhs(u, y):
        c1 = y[0]; c = y[1:]
        R = c.sum()
        d = np.empty_like(y)
        d[0] = -2.0*alpha*c1 - 2.0*R
        d[1] = alpha*c1 - 2.0*c1*0 - 2.0*c[0]  # dc2/du = alpha*c1 - 2*c2
        d[2:] = 2.0*(c[:-1] - c[1:])
        return d
    def done(u, y): return y[0] - 1e-13
    done.terminal, done.direction = True, -1
    y0 = np.zeros(ncap); y0[0] = 1.0
    # generous u-span; event terminates
    s = solve_ivp(rhs, (0.0, 5000.0), y0, method="LSODA",
                  rtol=1e-10, atol=1e-13, events=done, dense_output=False)
    y = s.y[:, -1]
    c1 = max(y[0], 0.0); c = np.clip(y[1:], 0.0, None)
    N = np.arange(2, ncap + 1, dtype=float)
    mass = c1 + (N * c).sum()
    f = (N * c) / (N * c).sum()          # mass fractions over rods (c1 -> 0)
    Ln = (N * c).sum() / c.sum()
    return N, f, Ln, abs(mass - 1.0), c1

def moment_Ln(alpha, tmax=None):
    """1855's own moment model, verbatim (validator target)."""
    if tmax is None: tmax = 50.0/alpha + 500.0
    def rhs(t, y):
        c1, R = y
        return [-2*alpha*c1*c1 - 2*c1*R, alpha*c1*c1]
    s = solve_ivp(rhs, (0, tmax), [1.0, 0.0], method="Radau",
                  rtol=1e-10, atol=1e-12, t_eval=[tmax])
    c1, R = s.y[0, -1], s.y[1, -1]
    return (1 - c1)/R

# ---------------- Part B: the 2344 rig, K species ----------------
t = json.load(open(os.path.join(here, "2344_F_table.json")))
lnE, lnF = np.array(t["lnE"]), np.array(t["lnF"])
EPS_LO, EPS_HI = 1.1e-2, 9.9e3

def F_of_eps(eps):
    e = np.clip(np.asarray(eps, dtype=float), EPS_LO, None)
    out = np.exp(np.interp(np.log(e), lnE, lnF))
    hi = e > EPS_HI
    if np.any(hi):
        out[hi] = np.exp(lnF[-1] + 0.17*(np.log(e[hi]) - lnE[-1]))
    return out

M_EL, CONV0 = 1408.0, 1e-26/1.783e-27
FL = {30: 0.11, 50: 0.09, 200: 0.05, 1500: 0.04}
C = 2.998e5
VELS = (30.0, 50.0, 200.0, 1500.0)

FR = json.load(open(os.path.join(here, "2345_l4_results.json")))["frames"]
FRAMES = {k: {int(a): tuple(b) for a, b in v.items()} for k, v in FR.items()}

def totals_K(Narr, warr, S0, p, Rs):
    """sigma_T/m totals at the four velocities for a K-species population."""
    M = Narr * M_EL
    S = S0 * (Narr / 2.0) ** p
    K = len(Narr)
    i, j = np.triu_indices(K)                     # pairs incl. self
    Sij = np.sqrt(S[i] * S[j])
    mu = M[i] * M[j] / (M[i] + M[j])
    wfac = np.where(i == j, warr[i]*warr[j]/M[i],
                    warr[i]*warr[j]*(1.0/M[i] + 1.0/M[j]))
    out = {}
    for v in VELS:
        b = (v / C) ** 2
        eps = Sij / (0.5 * mu * b * Rs)
        sig = Rs * Rs * F_of_eps(eps)
        out[int(v)] = float((wfac * sig).sum() * CONV0 + FL[int(v)])
    return out

def violation(tot, frame):
    v = 1.0
    for vel, (lo, hi) in frame.items():
        x = tot[vel]
        if x < lo: v = max(v, lo / x)
        if x > hi: v = max(v, x / hi)
    return v

# validator V2: reproduce the stored 2344 two-delta totals through this code path
ext = json.load(open(os.path.join(here, "2344_extended_anneal.json")))
NA, NB, gA2, gB2, w, Rs0 = ext["params"]
# two-delta: cannot use S(N) law (2344 species are free-coupled); feed directly
def totals_two_delta(NA, NB, gA2, gB2, w, Rs):
    Narr = np.array([NA, NB]); warr = np.array([w, 1 - w])
    M = Narr * M_EL
    S = np.array([gA2, gB2])
    i, j = np.triu_indices(2)
    Sij = np.sqrt(S[i] * S[j]); mu = M[i]*M[j]/(M[i]+M[j])
    wfac = np.where(i == j, warr[i]*warr[j]/M[i],
                    warr[i]*warr[j]*(1.0/M[i] + 1.0/M[j]))
    out = {}
    for v in VELS:
        b = (v/C)**2
        eps = Sij / (0.5*mu*b*Rs)
        sig = Rs*Rs*F_of_eps(eps)
        out[int(v)] = float((wfac*sig).sum()*CONV0 + FL[int(v)])
    return out

# ---------------- Part C: scan ----------------
def run():
    res = {}

    # V1: population balance vs 1855 moment model
    v1 = []
    for a in (1.0, 0.1, 0.01):
        N, f, Ln, merr, c1f = distribution(a)
        v1.append({"alpha": a, "Ln_pb": Ln, "Ln_moment": moment_Ln(a),
                   "mass_err": merr, "c1_final": c1f})
    res["V1"] = v1

    # V2: rig reproduces stored 2344 totals
    td = totals_two_delta(NA, NB, gA2, gB2, w, Rs0)
    res["V2"] = {"reproduced": td, "stored": ext["totals"],
                 "max_rel_err": max(abs(td[k] - ext["totals"][str(k)]) /
                                    ext["totals"][str(k)] for k in td)}

    # dimer-dominance curve f2(alpha) + tail structure
    curve = []
    for la in np.linspace(-2, 6, 33):
        a = 10.0 ** la
        N, f, Ln, merr, _ = distribution(a)
        d = {"alpha": a, "f2": float(f[0]), "f3": float(f[1]), "f4": float(f[2]),
             "f5": float(f[3]), "Ln": Ln, "mass_err": merr,
             "tail_monotone": bool(np.all(np.diff(f[1:60]) <= 1e-12))}
        curve.append(d)
    res["f2_curve"] = curve
    # alpha for f2 = 0.99 (log-interp)
    f2s = np.array([c["f2"] for c in curve]); las = np.linspace(-2, 6, 33)
    if f2s.max() >= 0.99:
        res["alpha_f2_99"] = float(10 ** np.interp(0.99, f2s, las))
    else:
        res["alpha_f2_99"] = None

    # coarse scan on the pre-registered box
    la_grid = np.linspace(-2, 6, 17)
    dists = {}
    for la in la_grid:
        N, f, Ln, merr, _ = distribution(10.0 ** la)
        keep = f >= 1e-6
        dists[la] = (N[keep], f[keep] / f[keep].sum())
    ls_grid = np.linspace(-6, 2, 33)
    p_grid = np.linspace(0, 16, 17)
    rs_grid = np.array([20.0, 25.42, 30.0, 40.0, 60.0, 90.0, 120.0])

    best = {k: {"viol": np.inf} for k in FRAMES}
    nev = 0
    for la in la_grid:
        Narr, warr = dists[la]
        for ls in ls_grid:
            for p in p_grid:
                for rs in rs_grid:
                    tot = totals_K(Narr, warr, 10.0**ls, p, rs)
                    nev += 1
                    for fk, fr in FRAMES.items():
                        v = violation(tot, fr)
                        if v < best[fk]["viol"]:
                            best[fk] = {"viol": v, "la": float(la), "ls": float(ls),
                                        "p": float(p), "rs": float(rs),
                                        "tot": tot}
    res["coarse_n_evals"] = nev
    res["coarse_best"] = best

    # local refinement per frame: finer alpha around the coarse best,
    # Nelder-Mead over (ls, p, rs) at each
    refined = {}
    for fk, fr in FRAMES.items():
        b = best[fk]
        cands = []
        for la in np.linspace(b["la"] - 0.75, b["la"] + 0.75, 7):
            la = float(np.clip(la, -2, 6))
            N, f, Ln, merr, _ = distribution(10.0 ** la)
            keep = f >= 1e-6
            Narr, warr = N[keep], f[keep] / f[keep].sum()
            def obj(x):
                ls, p, rs = x
                if not (-6 <= ls <= 2 and 0 <= p <= 16 and 20 <= rs <= 120):
                    return 50.0
                return math.log(violation(totals_K(Narr, warr, 10.0**ls, p, rs), fr))
            r = minimize(obj, [b["ls"], b["p"], b["rs"]], method="Nelder-Mead",
                         options={"maxiter": 400, "xatol": 1e-4, "fatol": 1e-7})
            v = math.exp(r.fun)
            tot = totals_K(Narr, warr, 10.0**r.x[0], r.x[1], r.x[2])
            cands.append({"viol": v, "la": la, "ls": float(r.x[0]),
                          "p": float(r.x[1]), "rs": float(r.x[2]), "tot": tot})
        refined[fk] = min(cands, key=lambda c: c["viol"])
    res["refined_best"] = refined

    # binding-window report + kinetic structure at each refined best
    for fk, b in refined.items():
        fr = FRAMES[fk]; binds = {}
        for vel, (lo, hi) in fr.items():
            x = b["tot"][vel]
            binds[vel] = {"tot": x, "lo": lo, "hi": hi,
                          "factor": max(lo/x, x/hi, 1.0)}
        b["binding"] = binds
        N, f, Ln, merr, _ = distribution(10.0 ** b["la"])
        b["f2345"] = [float(f[0]), float(f[1]), float(f[2]), float(f[3])]

    json.dump(res, open(os.path.join(here, "2349_results.json"), "w"), indent=1)
    print("V1 (Ln pb vs moment):", [(d["alpha"], round(d["Ln_pb"], 3),
                                     round(d["Ln_moment"], 3)) for d in v1])
    print("V2 max rel err:", res["V2"]["max_rel_err"])
    print("alpha for f2=0.99:", res["alpha_f2_99"])
    print("coarse evals:", nev)
    for fk in FRAMES:
        print(fk, "coarse", round(best[fk]["viol"], 4),
              "refined", round(refined[fk]["viol"], 4),
              "at alpha=1e%.2f p=%.2f S0=1e%.2f Rs=%.1f"
              % (refined[fk]["la"], refined[fk]["p"],
                 refined[fk]["ls"], refined[fk]["rs"]))

if __name__ == "__main__":
    run()

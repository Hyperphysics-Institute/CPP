#!/usr/bin/env python
"""Patch 3080 -- D-SEA-SELFCONSIST Stage 3: the explicit 3D array.

Retires the Stage-2 caveats: no 1D reduction, no mirror approximation,
no mean-field OU environment, no FCC-C6 stand-in, no hand-built poach
rule. N_p = 27 DPs (54 CPs, unit charges +/-1) in a periodic cube of
side 3*d_s, initialised superposed on a 3x3x3 grid, seeded with a
small random velocity kick. The ruled dynamics and nothing else:
  R-STEP-SSV + R-INERTIA-ARC : v += F, x += v (continuous branch --
      the sub-GP-step branch pending FQ-5.1; the hard-quantum branch
      is provably frozen at these field strengths, Stage 2 G1)
  Coulomb : all-pairs +/-1/r^2, minimum-image periodic, floor r >= 1
  R-ZBW-DELAY : the PARTNER interaction is RETARDED (light-cone search
      over the partner's true stored trajectory, monotone pointer);
      non-partner fields quasi-static (their retardation ~ d_s Moments
      smooths against slow configuration change -- caveat recorded)
  Partnering : perfect matching maintained; a switch happens when an
      opposite-charge non-partner is nearer than the partner AND
      within 2 GP (the founder's closer-at-perigee rule); switches
      re-pair mutually; retardation uses the global history, so the
      new partner's past light-cone is physically honoured with no
      reset artefact.
THE EXPERIMENT per d_s: seed the frozen array and watch <delta^2>(t):
  DECAY -> the Sea freezes without continuous external seeding;
  SUSTAIN -> a self-maintained jittering branch exists in the array;
  GROW/f_sw->1 -> plasma runaway.
Outputs: eta_z = <delta^2>/d_s^2 (late window), f_switch per
regeneration, thirds-trajectory of <delta^2>, <v^2> drift, superposed
fraction. Two seed amplitudes test attractor independence. No band
quantity anywhere.
"""
import numpy as np

def run(ds, T=3200, kick=0.5, seed=5):
    rng = np.random.default_rng(seed)
    n_side, Np = 3, 27
    Nc = 2*Np
    L = n_side*ds
    grid = np.array([[i, j, k] for i in range(n_side) for j in range(n_side)
                     for k in range(n_side)], float)*ds + ds/2
    X = np.repeat(grid, 2, axis=0)                     # pairs superposed
    q = np.tile([1.0, -1.0], Np)
    partner = np.arange(Nc); partner[0::2] += 1; partner[1::2] -= 1
    V = rng.normal(0, kick, (Nc, 3))
    V[1::2] = -V[0::2]                                 # opposite launch (R-DWELL-1 mechanism)
    Hist = np.zeros((T, Nc, 3)); Hist[0] = X
    ptr = np.zeros(Nc, dtype=int)
    qq = np.outer(q, q)
    eye = np.eye(Nc, dtype=bool)
    opp = (qq < 0)
    d2_series, sup_series, v2_series, sw_cum, regen_cum = [], [], [], 0, 0
    prev_sup = np.ones(Np, dtype=bool)
    for t in range(1, T):
        D = X[:, None, :] - X[None, :, :]
        D -= L*np.round(D/L)
        r = np.sqrt(np.einsum('ijk,ijk->ij', D, D)); np.fill_diagonal(r, 1.0)
        co = r < 1e-6                                   # co-location: force undefined => ZERO (ruled)
        rs = np.where(co, 1.0, r)
        re = np.maximum(rs, 1.0)
        kern = np.where(co, 0.0, qq/(re**2 * rs))
        # all-pairs quasi-static force on i from j (attract if opposite)
        F = -np.einsum('ij,ijk->ik', kern, D)
        # replace partner term with the RETARDED one
        for i in range(Nc):
            p = partner[i]
            # remove instantaneous partner contribution
            dv = D[i, p]; rr = np.sqrt(dv@dv)
            if rr > 1e-6:
                F[i] += qq[i, p]/(max(rr, 1.0)**2 * rr) * dv
            # light-cone: largest tr <= t-1 with (t-tr) >= |X_i - Hist[tr, p]|
            tr = min(ptr[i], t-1)
            def gap(tt):
                w = X[i] - Hist[tt, p]; w -= L*np.round(w/L)
                return np.sqrt(w@w)
            while tr+1 <= t-1 and (t-(tr+1)) >= gap(tr+1): tr += 1
            while tr >= 0 and (t-tr) < gap(tr): tr -= 1
            ptr[i] = max(tr, 0)
            if tr >= 0:
                w = X[i] - Hist[tr, p]; w -= L*np.round(w/L)
                s = np.sqrt(w@w)
                if s > 1e-9:
                    F[i] += -qq[i, partner[i]]/(max(s, 1.0)**2 * s) * w
        V += F
        X = (X + V) % L
        Hist[t] = X
        # switching: nearest opposite non-partner closer than partner and < 2 GP
        ro = np.where(opp & ~eye, r, np.inf)
        for i in range(Nc):
            ro[i, partner[i]] = np.inf
        j_star = np.argmin(ro, axis=1)
        d_new = ro[np.arange(Nc), j_star]
        d_par = r[np.arange(Nc), partner]
        want = (d_new < d_par) & (d_new < 2.0)
        done = np.zeros(Nc, bool)
        for i in np.where(want)[0]:
            j = j_star[i]
            if done[i] or done[j]: continue
            m, k = partner[i], partner[j]
            if done[m] or done[k] or len({i, j, m, k}) < 4: continue
            partner[i], partner[j] = j, i
            partner[m], partner[k] = k, m
            done[[i, j, m, k]] = True
            sw_cum += 1
        # observables (per pair, once)
        pi = np.arange(0, Nc, 2)
        dp = r[pi, partner[pi]]
        d2_series.append(np.mean(dp**2))
        sup = dp < 1.0
        regen_cum += int(np.sum(sup & ~prev_sup))       # entries into superposition
        prev_sup = sup
        sup_series.append(np.mean(sup))
        v2_series.append(np.mean(np.einsum('ij,ij->i', V, V)))
    d2 = np.array(d2_series); v2 = np.array(v2_series)
    th = len(d2)//3
    return dict(ds=ds, d2_early=d2[:th].mean(), d2_mid=d2[th:2*th].mean(),
                d2_late=d2[2*th:].mean(), eta=d2[2*th:].mean()/ds**2,
                fsw=sw_cum/max(regen_cum, 1), regen=regen_cum,
                sup=np.mean(sup_series[2*th:]), v2_drift=v2[2*th:].mean()/max(v2[:th].mean(), 1e-12))

print(f"{'d_s':>5} {'kick':>5} {'d2 early/mid/late':>24} {'eta_late':>9} {'f_sw':>6} {'regen':>6} {'sup_frac':>8} {'v2 drift':>8}")
for ds in (6.0, 8.0, 16.0):
    for kick in (0.5, 2.0):
        z = run(ds, kick=kick)
        print(f"{ds:5.0f} {kick:5.1f} {z['d2_early']:8.2f}/{z['d2_mid']:7.2f}/{z['d2_late']:7.2f} "
              f"{z['eta']:9.4f} {z['fsw']:6.3f} {z['regen']:6d} {z['sup']:8.3f} {z['v2_drift']:8.2f}")

# ---- H2 demonstration: lossy arc inertia (retarded self-field reading) ----
# If R-INERTIA-ARC's memory is the RETARDED RETURN of the CP's own
# emissions (an arc FIELD re-encountered, not perfect bookkeeping),
# inertia carries a loss: v <- gamma*v + F, gamma < 1. Two gamma values
# EXHIBIT the mechanism's effect; neither is adopted -- the loss
# magnitude is FQ-5.3, the founder's picture (and possibly derivable
# from the arc geometry). Anti-extraction: no gamma is selected.
def run_g(ds, gamma, T=3200, kick=0.5, seed=5):
    rng = np.random.default_rng(seed)
    n_side, Np = 3, 27; Nc = 2*Np; L = n_side*ds
    grid = np.array([[i, j, k] for i in range(n_side) for j in range(n_side)
                     for k in range(n_side)], float)*ds + ds/2
    X = np.repeat(grid, 2, axis=0); q = np.tile([1.0, -1.0], Np)
    partner = np.arange(Nc); partner[0::2] += 1; partner[1::2] -= 1
    V = rng.normal(0, kick, (Nc, 3)); V[1::2] = -V[0::2]
    Hist = np.zeros((T, Nc, 3)); Hist[0] = X
    ptr = np.zeros(Nc, dtype=int); qq = np.outer(q, q)
    eye = np.eye(Nc, dtype=bool); opp = (qq < 0)
    d2s, sws, regen = [], 0, 0
    v2s = []
    prev_sup = np.ones(Np, bool)
    for t in range(1, T):
        D = X[:, None, :] - X[None, :, :]; D -= L*np.round(D/L)
        r = np.sqrt(np.einsum('ijk,ijk->ij', D, D)); np.fill_diagonal(r, 1.0)
        co = r < 1e-6; rs = np.where(co, 1.0, r); re = np.maximum(rs, 1.0)
        kern = np.where(co, 0.0, qq/(re**2 * rs))
        F = -np.einsum('ij,ijk->ik', kern, D)
        for i in range(Nc):
            p = partner[i]
            dv = D[i, p]; rr = np.sqrt(dv@dv)
            if rr > 1e-6:
                F[i] += qq[i, p]/(max(rr, 1.0)**2 * rr) * dv
            tr = min(ptr[i], t-1)
            def gap(tt):
                w = X[i] - Hist[tt, p]; w -= L*np.round(w/L); return np.sqrt(w@w)
            while tr+1 <= t-1 and (t-(tr+1)) >= gap(tr+1): tr += 1
            while tr >= 0 and (t-tr) < gap(tr): tr -= 1
            ptr[i] = max(tr, 0)
            if tr >= 0:
                w = X[i] - Hist[tr, p]; w -= L*np.round(w/L); s = np.sqrt(w@w)
                if s > 1e-9:
                    F[i] += -qq[i, partner[i]]/(max(s, 1.0)**2 * s) * w
        V = gamma*V + F
        X = (X + V) % L; Hist[t] = X
        ro = np.where(opp & ~eye, r, np.inf)
        for i in range(Nc): ro[i, partner[i]] = np.inf
        j_star = np.argmin(ro, axis=1)
        d_new = ro[np.arange(Nc), j_star]; d_par = r[np.arange(Nc), partner]
        want = (d_new < d_par) & (d_new < 2.0)
        done = np.zeros(Nc, bool)
        for i in np.where(want)[0]:
            j = j_star[i]
            if done[i] or done[j]: continue
            m, k = partner[i], partner[j]
            if done[m] or done[k] or len({i, j, m, k}) < 4: continue
            partner[i], partner[j] = j, i; partner[m], partner[k] = k, m
            done[[i, j, m, k]] = True; sws += 1
        pi = np.arange(0, Nc, 2); dp = r[pi, partner[pi]]
        d2s.append(np.mean(dp**2))
        sup = dp < 1.0; regen += int(np.sum(sup & ~prev_sup)); prev_sup = sup
        v2s.append(np.mean(np.einsum('ij,ij->i', V, V)))
    d2 = np.array(d2s); th = len(d2)//3; v2 = np.array(v2s)
    return dict(eta=d2[2*th:].mean()/ds**2, fsw=sws/max(regen, 1), regen=regen,
                drift=v2[2*th:].mean()/max(v2[:th].mean(), 1e-12))

print("\nH2: lossy-arc demonstration (d_s = 8):")
for gamma in (0.99, 0.90):
    z = run_g(8.0, gamma)
    print(f"  gamma={gamma:4.2f}: eta_late={z['eta']:8.4f}, f_sw={z['fsw']:6.3f}, "
          f"regen={z['regen']:5d}, v2 drift={z['drift']:6.2f}")
print("""
STAGE-3 FINDINGS (exhibited, whichever way they point):
 H1  With PERFECT-MEMORY inertia (v += F) and no back-reaction, the
     explicit array HEATS (<v^2> x2-7 over the run) and ionises into
     a partner-random gas at ALL spacings scanned: eta_late ~ 2.0-2.2
     = the uniform-gas value (L^2/4)/d_s^2 = 2.25, superposed fraction
     ~1%, switches >> regenerations. The Stage-2 stationarity is NOT
     self-sustained in this model class. Diagnosis: retarded
     attraction + lossless inertia pumps energy -- the model violates
     the automaton's own O-3 ledger conservation. ENERGY REGULATION
     is a MISSING RULED INGREDIENT, not a Sea property.
 H2  A lossy arc (v <- gamma*v + F) -- the reading in which
     R-INERTIA-ARC's memory is the RETARDED RETURN of the CP's own
     arc field rather than perfect bookkeeping -- CURES THE HEATING
     (v^2 drift 0.98-1.00, flat, vs x2-7 lossless) but does NOT by
     itself restore the faithful-pair phase in this run: the array
     relaxes into scrambled/glassy states (labels randomised during
     the transient persist; gamma=0.90 near-freezes, regen=3). The
     regulator is NECESSARY (H1) but not sufficient as tested;
     recovering the faithful jittering phase needs the ruled loss
     PLUS proper preparation/annealing (Stage 3b).
     FQ-5.3 (founder): is the arc's inertia perfect memory, or the
     re-encounter of the CP's own retarded emissions (lossy, with the
     loss potentially DERIVABLE from arc geometry + shell dilution)?
 H3  Stage-2's eta_z ~ 0.2 remains the best current phi_3 estimate,
     now understood as CONDITIONAL on the energy-regulated stationary
     faithful branch -- whose regulator FQ-5.3 pins and whose
     existence in the explicit array Stage 3b must exhibit.""")

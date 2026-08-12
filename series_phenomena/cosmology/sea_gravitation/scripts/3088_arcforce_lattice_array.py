#!/usr/bin/env python
"""Patch 3088 -- D-ARC-FORCE: the arc-force lattice array (the decisive
CC computation), with the electric-sector sign audit that preceded it.

SIGN AUDIT (found during the port, before any run):
  (1) The 3080/3083 3D arrays compute F = -sum(kern*D) with
  kern = qq/(re^2 rs), i.e. the NEGATIVE of standard Coulomb
  (F_std = +qq*D/r^3): unlike charges REPEL, like charges ATTRACT,
  and the retarded partner term is likewise inverted (repulsion from
  the retarded position, where the ruled mechanism -- R-ZBW-DELAY,
  "retarded restoring dominance" -- requires attraction). Stage 2's
  1D model (3079) has the correct restoring sign, so the
  shape-universal eta_z ~ 0.2 is NOT contaminated; the 3D phase
  tables (Stage 3 heating, 3b GLASS, 3c fidelity failure) ARE.
  (2) The 3086 two-body code's MAGNETIC term is inverted relative to
  its own docstring: B_at1 = (-1)*cross(v2, -rhat) = +cross(v2, rhat)
  is magnetic REPULSION for parallel currents; the docstring's
  analytic derivation (textbook, attraction) is the ruled one (SF-6
  Maxwell limit). 3086's bounded run therefore validated the BORIS
  PUSHER (rotation preserves |v| for either sign), not the sign; its
  orbit also stayed bounded partly because the sign/launch mismatch
  kept it away from close range. With textbook signs, well-resolved
  orbits (a = 4/6/10; 97/181/392 steps per orbit) are bounded with
  energy drift 1.6e-5 / 8.8e-6 / 8.0e-7, improving with resolution;
  the a = 2 orbit (33 steps/orbit) decays into sub-unit passages
  that a unit-Moment step cannot resolve -- the 3086 close-range
  flag reproduced, and structurally ABSENT on the lattice, where
  distinct addresses are never closer than 1 GP and co-location is
  ruled (zero force + one-Moment dwell + coupled-field relaunch).
  This script therefore runs BOTH: (a) the sign-corrected no-arc
  CONTROL (does the 3084 table survive correction?), and (b) the
  arc-force run (D-ARC-FORCE proper). The pre-stated criterion
  (3083) is UNCHANGED: recurrent superposition + eta << 2.25 +
  small f_sw + flat v^2.

FORCES (all matched to the validated 3086 conventions, generalised):
  Electric  F_i = sum_j qq_ij * D_ij / (re^2 rs)   [attraction for
            unlike], co-located pairs -> ZERO (superposition,
            zero-force release). Partner term replaced by the
            retarded one (R-ZBW-DELAY pump): attraction toward the
            partner's retarded position.
  Magnetic  B_i = sum_j q_j * (v_j x rhat_{j->i}) / re^2 at c = 1
            (SF-6: E and B locked components of one dipole
            displacement, Maxwell the macroscopic limit => the
            CP-level arc force is the standard magnetic interaction
            of moving charges, ZERO new constants). Source
            velocities saturated at the substrate signal speed
            (|v_eff| <= 1: a bound, not a dial -- arc fields are
            made of DI-bits at c = 1). Quasi-static for
            non-partners; retarded for the partner. Does no work;
            opposite members excursing oppositely = parallel
            currents => v^2-proportional BINDING (the ruled
            fidelity agent, 3084 par.2 / 3085 grounding).
  Pusher    BORIS (3086-validated, parameter-free): half electric
            kick, exact rotation for the magnetic part (|v|
            preserved by construction), half kick; the brake gamma
            applied after as a separate factor. gamma is SCANNED
            (D-ARC-GAMMA has not yet pinned it; the question put to
            the array is INSENSITIVITY).
  Noise     R-JITTER-SOURCE floor sigma_n, SCANNED; charge-coupled
            as a FIELD: co-located partners feel the SAME vector and
            respond OPPOSITELY -- the R-DWELL-1 relaunch (one-Moment
            superposition; next Moment's summation moves opposite
            members oppositely).
  Lattice   GP-address jumps X += round(V) (R-STEP-SSV). On the
            lattice distinct addresses have r >= 1, so the r >= 1
            floor of the continuum runs is INERT; close range is
            handled by the ruled co-location behaviour (zero force +
            coupled-field relaunch), resolving the 3086 flag.
  R-GP-REZERO honoured by construction: fields rebuilt fresh each
            Moment, no carryover.

VALIDATION GATE: check_twobody() reduces this file's own force
assembly + Boris to the 3086 two-body setting (2 CPs, free space,
retardation off) and must reproduce the bounded analytic orbit
(|energy drift| < 0.01 over 20,000 Moments) BEFORE any array run is
reported. A failed gate voids the tables below it.

Phase classification per run (late third), unchanged from 3083:
  GAS         eta within 25% of the uniform-gas value 2.25
  COLLAPSED   <v^2> < 1e-6 and eta < 1e-3 (pump lost to brake)
  FROZEN-SUP  eta < 1e-3 with regen = 0 (held superposed, no cycle)
  GLASS       regenerations ~ 0 with eta order-1 (stuck)
  FAITHFUL    bound (eta << gas), regenerating, stationary (v^2 flat)
No band quantity appears anywhere. Fixed seeds; one repeat seed line.
"""
import sys
import numpy as np


def clip_rows(V):
    """Saturate row vectors at the substrate signal speed |v| <= 1."""
    n = np.sqrt(np.einsum('ij,ij->i', V, V))
    return V / np.maximum(n, 1.0)[:, None]


def run(ds, gamma, T=3000, kick=0.05, seed=5, sig_n=0.0, lattice=True,
        arc=False, retard=True, n_side=3, L_override=None):
    rng = np.random.default_rng(seed)
    Np = n_side**3; Nc = 2*Np
    L = L_override if L_override is not None else n_side*ds
    grid = np.array([[i, j, k] for i in range(n_side) for j in range(n_side)
                     for k in range(n_side)], float)*ds + ds/2
    X = np.repeat(grid, 2, axis=0)
    q = np.tile([1.0, -1.0], Np)
    partner = np.arange(Nc); partner[0::2] += 1; partner[1::2] -= 1
    orig = partner.copy()      # exploratory diagnostic: original pairing
    V = rng.normal(0, kick, (Nc, 3)); V[1::2] = -V[0::2]
    Hist = np.zeros((T, Nc, 3)); Hist[0] = X
    VHist = np.zeros((T, Nc, 3))
    ptr = np.zeros(Nc, dtype=int)
    qq = np.outer(q, q)
    eye = np.eye(Nc, dtype=bool); opp = (qq < 0)
    d2s, v2s, sws, regen, regen_orig = [], [], 0, 0, 0
    prev_sup = np.ones(Np, bool)
    idx = np.arange(Nc)
    for t in range(1, T):
        D = X[:, None, :] - X[None, :, :]; D -= L*np.round(D/L)
        r = np.sqrt(np.einsum('ijk,ijk->ij', D, D)); np.fill_diagonal(r, 1.0)
        co = r < 1e-6                       # superposition: zero force
        rs = np.where(co, 1.0, r); re = np.maximum(rs, 1.0)
        kern = np.where(co, 0.0, qq/(re**2 * rs))
        # ELECTRIC, standard Coulomb sign (3086 convention):
        # F_i = +sum_j qq_ij D_ij / (re^2 rs) -- unlike attracts.
        E = np.einsum('ij,ijk->ik', kern, D)
        B = np.zeros((Nc, 3))
        if arc:
            Vc = clip_rows(V)
            rhat = D / rs[:, :, None]       # unit vector j -> i (= D_ij/r)
            # B at i from source j: q_j (v_j x rhat_{j->i}) / re^2
            Bk = np.where(co, 0.0, 1.0/re**2)[:, :, None] * \
                 np.cross(Vc[None, :, :] * q[None, :, None], rhat)
            np.einsum('iik->ik', Bk)[:] = 0.0
            B = Bk.sum(axis=1)
        for i in range(Nc):
            p = partner[i]
            if not retard:
                continue
            # replace the instantaneous partner terms with retarded ones
            dv = D[i, p]; rr = r[i, p]
            if not co[i, p]:
                E[i] -= qq[i, p]/(max(rr, 1.0)**2 * rr) * dv
                if arc:
                    B[i] -= q[p]*np.cross(clip_rows(V[p][None])[0],
                                          dv/rr)/max(rr, 1.0)**2
            tr = min(ptr[i], t-1)
            def gap(tt):
                w = X[i] - Hist[tt, p]; w -= L*np.round(w/L)
                return np.sqrt(w@w)
            while tr+1 <= t-1 and (t-(tr+1)) >= gap(tr+1):
                tr += 1
            while tr >= 0 and (t-tr) < gap(tr):
                tr -= 1
            ptr[i] = max(tr, 0)
            if tr >= 0:
                w = X[i] - Hist[tr, p]; w -= L*np.round(w/L)
                s = np.sqrt(w@w)
                if s > 1e-9:
                    # attraction toward the retarded partner position
                    # (R-ZBW-DELAY: "retarded restoring dominance")
                    E[i] += qq[i, p]/(max(s, 1.0)**2 * s) * w
                    if arc:
                        # retarded partner B: source velocity at emission
                        vp_ret = clip_rows(VHist[tr, p][None])[0]
                        B[i] += q[p]*np.cross(vp_ret, w/s)/max(s, 1.0)**2
        if sig_n > 0:
            # R-JITTER-SOURCE as a FIELD; co-located partners share the
            # vector -> opposite response = the R-DWELL-1 relaunch.
            fld = rng.normal(0, sig_n, (Nc, 3))
            near = r[idx, partner] < 1.0
            for i in np.where(near)[0]:
                if i < partner[i]:
                    fld[partner[i]] = fld[i]
            E = E + q[:, None]*fld
        # BORIS pusher (3086-validated): half kick, exact rotation, half
        # kick; |v| preserved by the magnetic part by construction.
        vm = V + 0.5*E
        if arc:
            tvec = 0.5*q[:, None]*B
            t2 = np.einsum('ij,ij->i', tvec, tvec)[:, None]
            vp = vm + np.cross(vm + np.cross(vm, tvec), 2*tvec/(1.0+t2))
        else:
            vp = vm
        V = gamma*(vp + 0.5*E)              # brake as a separate factor
        if not np.all(np.isfinite(V)) or np.max(np.abs(V)) > 1e6:
            return dict(ds=ds, g=gamma, eta=np.nan, fsw=np.nan,
                        regen=regen, v2=np.nan, drift=np.nan,
                        phase=f"OVERFLOW@{t}")
        VHist[t-1] = V
        X = (X + (np.round(V) if lattice else V)) % L
        Hist[t] = X
        ro = np.where(opp & ~eye, r, np.inf)
        for i in range(Nc):
            ro[i, partner[i]] = np.inf
        j_star = np.argmin(ro, axis=1)
        d_new = ro[idx, j_star]; d_par = r[idx, partner]
        want = (d_new < d_par) & (d_new < ds/2.0)   # founder perigee rule
        done = np.zeros(Nc, bool)
        for i in np.where(want)[0]:
            j = j_star[i]
            if done[i] or done[j]:
                continue
            m, k = partner[i], partner[j]
            if done[m] or done[k] or len({i, j, m, k}) < 4:
                continue
            partner[i], partner[j] = j, i
            partner[m], partner[k] = k, m
            done[[i, j, m, k]] = True; sws += 1
        pi = np.arange(0, Nc, 2); dp = r[pi, partner[pi]]
        d2s.append(np.mean(dp**2))
        sup = dp < 1.0
        new = sup & ~prev_sup
        regen += int(np.sum(new))
        regen_orig += int(np.sum(new & (partner[pi] == orig[pi])))
        prev_sup = sup
        v2s.append(np.mean(np.einsum('ij,ij->i', V, V)))
    d2 = np.array(d2s); v2 = np.array(v2s); th = len(d2)//3
    eta = d2[2*th:].mean()/ds**2
    drift = v2[2*th:].mean()/max(v2[th:2*th].mean(), 1e-30)
    v2l = v2[2*th:].mean()
    gas = abs(eta - 2.25) < 0.6
    if v2l < 1e-6 and eta < 1e-3:
        phase = "COLLAPSED"
    elif eta < 1e-3 and regen == 0:
        phase = "FROZEN-SUP"
    elif gas:
        phase = "GAS"
    elif regen < 5:
        phase = "GLASS"
    elif eta < 1.2 and 0.3 < drift < 3.0:
        phase = "FAITHFUL"
    else:
        phase = "OTHER"
    return dict(ds=ds, g=gamma, eta=eta, fsw=sws/max(regen, 1),
                regen=regen, forig=regen_orig/max(regen, 1),
                v2=v2l, drift=drift, phase=phase)


def _pair_eb(X, V, q):
    """This file's two-body force assembly (textbook signs, floor)."""
    d = X[0] - X[1]; s = np.linalg.norm(d)
    se = max(s, 1.0); rhat = d/s
    E = np.zeros((2, 3))
    E[0] = q[0]*q[1]*d/(se**2*s)            # standard Coulomb: attraction
    E[1] = -E[0]
    Vc = clip_rows(V)
    B = np.zeros((2, 3))
    B[0] = q[1]*np.cross(Vc[1],  rhat)/se**2   # source 2 -> point 1
    B[1] = q[0]*np.cross(Vc[0], -rhat)/se**2   # source 1 -> point 2
    return E, B


def check_signs():
    """Gate part 1 (exact): parallel-current magnetic force must BIND
    with magnitude v^2/s^2 (SF-6 Maxwell limit, 3086 docstring)."""
    X = np.array([[2., 0., 0.], [-2., 0., 0.]])
    V = np.array([[0., 0.2, 0.], [0., -0.2, 0.]])
    q = np.array([1.0, -1.0])
    E, B = _pair_eb(X, V, q)
    Fm = q[0]*np.cross(V[0], B[0])
    want = np.array([-0.04/16.0, 0.0, 0.0])   # inward, v^2/s^2
    return dict(Fmag=Fm.tolist(), analytic=want.tolist(),
                ok=bool(np.allclose(Fm, want)))


def check_orbit(a=6.0, T=60000):
    """Gate part 2: well-resolved analytic orbit v^2 = 1/(4a-1) must be
    bounded with tiny energy drift under this file's forces + Boris.
    (a = 2 is deliberately NOT the gate: at 33 steps/orbit the discrete
    map decays into sub-unit passages -- the 3086 close-range flag,
    absent on the lattice.)"""
    v = np.sqrt(1.0/(4*a - 1.0))
    X = np.array([[a, 0., 0.], [-a, 0., 0.]])
    V = np.array([[0., v, 0.], [0., -v, 0.]])
    q = np.array([1.0, -1.0])
    rads, encs = [], []
    for t in range(T):
        E, B = _pair_eb(X, V, q)
        vm = V + 0.5*E
        tvec = 0.5*q[:, None]*B
        t2 = np.einsum('ij,ij->i', tvec, tvec)[:, None]
        vp = vm + np.cross(vm + np.cross(vm, tvec), 2*tvec/(1.0+t2))
        V = vp + 0.5*E
        X = X + V
        sep = np.linalg.norm(X[0] - X[1])
        rads.append(sep/2)
        encs.append(0.5*np.einsum('ij,ij->', V, V) - 1.0/max(sep, 1.0))
    r = np.array(rads); e = np.array(encs)
    return dict(rad0=float(r[:100].mean()), radN=float(r[-100:].mean()),
                rmin=float(r.min()),
                edrift=float(e[-100:].mean() - e[:100].mean()))


if __name__ == "__main__":
    print("VALIDATION GATE 1 (one-step analytic sign/magnitude, exact):")
    z1 = check_signs()
    print("  ", z1, "->", "PASS" if z1['ok'] else "FAIL")
    print("VALIDATION GATE 2 (resolved orbit a=6, bounded, |edrift| < 1e-4):")
    z2 = check_orbit()
    ok2 = abs(z2['edrift']) < 1e-4 and abs(z2['radN'] - z2['rad0']) < 0.5
    print("  ", z2, "->", "PASS" if ok2 else "FAIL")
    if not (z1['ok'] and ok2):
        sys.exit("GATE FAILED: no array run is reported.")
    hdr = (f"{'arc':>4} {'d_s':>4} {'gamma':>6} {'sig_n':>6} {'seed':>5} "
           f"{'phase':>11} {'eta3D':>8} {'eta/3':>7} {'f_sw':>7} "
           f"{'f_orig':>7} {'regen':>6} {'v2_late':>9} {'drift':>6}")
    if len(sys.argv) > 1:
        cfgs = eval(sys.argv[1])
    else:
        cfgs = (
            # (arc, ds, gamma, sig_n, seed) -- sign-corrected CONTROL
            # (arc off), mirroring the 3084 table for direct comparison:
            [(False, 8, 0.90, 0.03, 5), (False, 8, 0.90, 0.30, 5),
             (False, 8, 0.90, 0.50, 5), (False, 8, 0.80, 0.50, 5),
             (False, 16, 0.90, 0.50, 5), (False, 8, 0.90, 1.00, 5)] +
            # D-ARC-FORCE proper (arc on): gamma scanned incl. the
            # weak-loss end D-ARC-GAMMA suggests; sigma_n scanned.
            [(True, 8, 0.90, 0.03, 5), (True, 8, 0.90, 0.30, 5),
             (True, 8, 0.90, 0.50, 5), (True, 8, 0.98, 0.30, 5),
             (True, 8, 0.98, 0.50, 5), (True, 8, 1.00, 0.30, 5),
             (True, 16, 0.90, 0.50, 5), (True, 8, 0.80, 0.50, 5),
             (True, 8, 0.90, 0.30, 11)] +
            # Finer sigma_n scan through the recurrence onset, both
            # sectors (the phase-boundary neighbourhood):
            [(False, 8, 0.90, 0.05, 5), (False, 8, 0.90, 0.10, 5),
             (False, 8, 0.90, 0.15, 5), (False, 8, 0.90, 0.20, 5),
             (True, 8, 0.90, 0.05, 5), (True, 8, 0.90, 0.08, 5),
             (True, 8, 0.90, 0.10, 5), (True, 8, 0.90, 0.12, 5),
             (True, 8, 0.90, 0.15, 5), (True, 8, 0.90, 0.20, 5)] +
            # Invariance block at the onset: d_s in {8,12,16}, seed
            # repeats (eta/3 = per-axis excursion statistic; compare
            # Stage 2's 1D shape-universal 0.19-0.25):
            [(True, 8, 0.90, 0.10, 11), (True, 12, 0.90, 0.10, 5),
             (True, 16, 0.90, 0.10, 5), (True, 16, 0.90, 0.10, 11),
             (False, 16, 0.90, 0.10, 5)]
        )
    print(hdr)
    for arc, ds, g, sn, sd in cfgs:
        z = run(ds, g, seed=sd, sig_n=sn, lattice=True, arc=arc)
        print(f"{str(arc)[0]:>4} {ds:4.0f} {g:6.2f} {sn:6.2f} {sd:5d} "
              f"{z['phase']:>11} {z['eta']:8.4f} {z['eta']/3:7.4f} "
              f"{z['fsw']:7.2f} {z['forig']:7.3f} {z['regen']:6d} "
              f"{z['v2']:9.2e} {z['drift']:6.2f}")

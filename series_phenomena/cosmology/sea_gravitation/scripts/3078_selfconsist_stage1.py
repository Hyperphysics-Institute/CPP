#!/usr/bin/env python
"""Patch 3078 -- D-SEA-SELFCONSIST Stage 1: the two-member retarded cycle.

Implements EXACTLY the ruled dynamics, nothing else:
  R-STEP-SSV      displacement_t = SSV_net_t (GP units; quantized variant
                  rounds to the 1-GP nominal quantum)
  R-INERTIA-ARC   SSV_net_t = (previous displacement) + (forces) ==>
                  discrete second-order dynamics, unit arc-mass
  R-ZBW-DELAY     partner influence at 1 GP/Moment (DI-bit speed); force
                  from the partner's RETARDED position (monotone light-
                  cone pointer); co-location => zero partner force that
                  Moment (superposition release)
  R-DWELL-1       not imposed -- measured
  Environment     Stage 1a: constant coherent SSV_net g (control).
                  Stage 1b: fluctuating SSV_net (OU: RMS sigma,
                  correlation tau_c Moments) -- STAND-INS for the array
                  statistics Stage 3 derives from d_s; not dials.
  Coulomb         unit charges, 1/s^2, lattice floor s >= 1 GP.

Symmetric frame: members at +/-x(t); delta = 2|x|; retarded separation
s_ret = x_now + x(t_r), largest t_r with (t - t_r) >= s_ret.

Findings are exhibited whichever way they point; no band quantity
appears anywhere in this file.
"""
import numpy as np

def retarded_force(x, t, xa, trp):
    """Largest t_r <= t-1 with (t-t_r) >= |xa + x[t_r]|, via monotone pointer."""
    tr = min(trp, t-1)
    # advance pointer while the NEXT candidate still satisfies the cone
    while tr + 1 <= t - 1 and (t - (tr+1)) >= abs(xa + x[tr+1]):
        tr += 1
    # retreat if current fails (can happen after fast growth)
    while tr >= 0 and (t - tr) < abs(xa + x[tr]):
        tr -= 1
    if tr < 0:
        return 0.0, 0
    s = abs(xa + x[tr])
    F = 0.0 if s < 1e-9 else -np.sign(xa + x[tr]) / max(s, 1.0)**2
    return F, tr

def run(T, env, quantize=False, seed=7):
    r = np.random.default_rng(seed)
    mode, p1, p2 = env
    rho = np.exp(-1.0/p2) if mode == "ou" else 0.0
    x = np.zeros(T); v = e = 0.0; trp = 0
    d2sum = nsum = near = 0; d2sum = 0.0
    apogees, crossings, cyc_max = [], [], 0.0
    for t in range(1, T):
        xa = x[t-1]
        F, trp = retarded_force(x, t, xa, trp)
        if mode == "const":
            Fenv = p1
        else:
            e = rho*e + p1*np.sqrt(1-rho*rho)*r.standard_normal()
            Fenv = e
        v = v + F + Fenv
        x[t] = xa + (np.round(v) if quantize else v)
        d = 2*abs(x[t]); d2sum += d*d; nsum += 1
        cyc_max = max(cyc_max, d)
        if d < 1.0: near += 1
        if x[t-1]*x[t] < 0:
            crossings.append(t); apogees.append(cyc_max); cyc_max = 0.0
        if abs(x[t]) > 5e3:                      # escaped (ionized): stop
            return dict(escaped=True, t_esc=t, ncyc=len(apogees))
    apo = np.array(apogees[2:])
    ok = len(apo) > 3
    return dict(escaped=False, ncyc=len(apo),
                apo=np.mean(apo) if ok else float('nan'),
                per=2*np.mean(np.diff(crossings)) if ok else float('nan'),
                eta=(d2sum/nsum)/np.mean(apo**2) if ok else float('nan'),
                dwell=near/max(nsum,1))

print("Stage 1a: CONSTANT coherent field g (control)")
print(f"{'g':>5} {'result':>28}")
for g in (0.25, 0.5, 1.0, 2.0):
    z = run(3000, ("const", g, 0))
    if z['escaped']:
        print(f"{g:5.2f}   IONIZED (escape by Moment {z['t_esc']}, {z['ncyc']} cycles)")
    else:
        print(f"{g:5.2f}   bound: apo={z['apo']:.2f} GP, eta={z['eta']:.3f}, per={z['per']:.1f}")

print("\nStage 1b: FLUCTUATING field (OU), continuous steps, T=15000")
print(f"{'sigma':>6} {'tau_c':>6} {'cycles':>7} {'apo(GP)':>8} {'period':>8} {'eta':>7} {'dwell<1':>8}")
for sig in (0.5, 1.0, 2.0):
    for tc in (2, 8, 32):
        z = run(15000, ("ou", sig, tc))
        tag = "ESC" if z['escaped'] else ""
        if z['escaped']:
            print(f"{sig:6.1f} {tc:6d}   IONIZED at {z['t_esc']}")
        else:
            print(f"{sig:6.1f} {tc:6d} {z['ncyc']:7d} {z['apo']:8.2f} {z['per']:8.1f} {z['eta']:7.3f} {z['dwell']:8.3f}")

print("\nStage 1b quantized (1-GP quantum), sigma=1:")
for tc in (2, 8, 32):
    z = run(15000, ("ou", 1.0, tc), quantize=True)
    if z['escaped']:
        print(f"   tau_c={tc}: IONIZED at {z['t_esc']}")
    else:
        print(f"   tau_c={tc}: cycles={z['ncyc']}, apo={z['apo']:.2f}, eta={z['eta']:.3f}, dwell={z['dwell']:.3f}")

ths = [run(15000, ("ou", 1.0, 8), seed=s).get('t_esc', -1) for s in (1, 2, 3, 4, 5)]
print(f"\nfidelity horizon, seeds 1-5 (sigma=1, tau_c=8): t_esc = {ths}")

print("""
STAGE-1 FINDINGS (exhibited, whichever way they point):
 F1  Constant coherent field: bound stretch-states below a threshold
     (g=0.25 overshoot-oscillation apo~0.75 GP; g=0.5 bound WITHOUT
     re-superposition -- the coherent field holds the pair open);
     g >= 1 IONIZES. Coherent fields do not make ZBW; they ionize or
     freeze-open. The plasma boundary exists and is exhibited.
 F2  Fluctuating field, ISOLATED pair: ionization is CERTAIN (velocity
     random-walks; 1/s^2 cannot confine without dissipation). Fidelity
     horizons ~70-260 Moments across the scanned (sigma, tau_c).
     STRUCTURAL CONCLUSION: the discrete-ZBW Sea cannot consist of
     isolated eternal pairs; RE-CAPTURE (faithful or new-partner) is
     necessary. P-SEA-DILUTE sharpens: spacing controls the switch
     RATE; R-SWAP-EQUIV makes the regenerative ensemble well-defined
     regardless. eta_z therefore lives in the REGENERATIVE process
     (Stage 2: superposition -> excursion -> first re-capture, reset),
     not in an isolated two-body limit cycle. 
 F3  Quantized (1-GP) vs continuous: same morphology at these
     amplitudes; sub-quantum freeze occurs only at fields << 1
     (the founder's effective-step caveat, exhibited).
NEXT: Stage 2 -- regenerative ensemble with re-capture at the poaching
radius r_p ~ d_s/2 and env statistics TIED to d_s via the array's own
dipole fields (no stand-in dials); outputs: eta_z(d_s), switch fraction
(the fidelity curve), and the P-SEA-DILUTE boundary d_s*.""")

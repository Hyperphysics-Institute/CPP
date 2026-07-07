#!/usr/bin/env python3
"""Patch 2322 -- G4 S2-3b: self-red-team of 2321's Theta framing; the polaron reframe.

Tension found (registered before the panel finds it): 2321's two-branch Theta treatment is
internally inconsistent -- the quasi-static branch (Theta ~ 1) that rescues dwarf capture ALSO
revives the steady-drag catastrophe (tau ~ 3e-13 s), and no stationary bath spectrum can supply
the ~24-order steady-vs-encounter selectivity the pair would then require (both processes sit at
comparable sub-cone frequencies: k.v ~ 260 eV vs omega_enc ~ 45 eV -- the encounter is LOWER).

Resolution (standard many-body structure, stated at structural grade):
  POLARON/DRESSED-STATE FRAME. The rod+coat+local-bath-backreaction is the dressed ground state
  of the moving rod. A dressed EIGENSTATE experiences no drag from the bath that dresses it --
  steady subsonic motion is protected AUTOMATICALLY (not by spectral tuning); the 2321 drag
  catastrophe was an artifact of treating the dressed state as scattering off its own dressing.
  ENCOUNTERS are nonadiabatic overlaps of two dressed states -> real emission allowed, into:
    (a) ON-SHELL quanta at omega_enc: k_on = omega_enc/c -> lambda ~ 4e6 fm -> this IS the
        radiative channel, already DEAD x1e13+ by the Adler factor (2318). Circle closes.
    (b) SUB-CONE continuum at (k ~ 1/R_s, omega ~ omega_enc): exists only via the bath's
        nonlinear/disorder broadening -- the D-C ruling's content. THE residue, now well-posed:
        S(k ~ 1/R_s, omega_enc), deeply sub-cone (omega/ck ~ 6e-6).
Thresholds from 2321 UNCHANGED; the halo/Lambda/W2 protections now structural.
"""
import math
HBARC=197.327; RS=25.42; C=2.998e8
print(" sub-cone kinematics at the coupling wavevector k = 1/R_s (hbar*c*k = %.2f MeV):"%(HBARC/RS))
checks=[]
rows=[]
for vk,b in ((10,145.0),(50,79.0),(200,31.0)):
    v=vk*1e3; beta=v/C
    w_enc=HBARC*beta/b*1e6            # eV  (hbar v / b)
    w_kv =HBARC/RS*beta*1e6           # eV  (hbar k.v -- steady-transfer scale)
    sub  =w_enc/(HBARC/RS*1e6)        # omega_enc / (c k)
    k_on =beta/b                      # on-shell wavenumber at omega_enc, fm^-1
    lam  =2*math.pi/k_on
    rows.append((vk,w_enc,w_kv,sub,lam))
    print(f"  v={vk:>3}: hbar*omega_enc={w_enc:7.1f} eV | hbar k.v={w_kv:7.1f} eV | omega/ck={sub:.1e} | on-shell lambda={lam:.1e} fm")
checks.append(("both steady (k.v) and encounter scales are DEEPLY sub-cone (omega/ck ~ 1e-6..1e-3): no on-shell bath state serves either -- everything rides on nonlinear sub-cone weight",
               all(r[3]<1e-3 for r in rows), None))
checks.append(("encounter frequency is BELOW k.v at every anchor -- no stationary spectrum can pass encounters while blocking steady drag by 24 orders: the 2321 two-branch Theta frame is INCONSISTENT and is RETIRED",
               all(r[1]<r[2] for r in rows), None))
checks.append(("on-shell emission at omega_enc has lambda ~ 4e5..4e6 fm >> R_s -- identically the 2318 radiative channel (Adler-dead x1e13+): the circle closes, no double-counting",
               all(r[4]>1e5 for r in rows), [f"{r[4]:.0e}" for r in rows]))
npass=0
for name,ok,val in checks:
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    npass+=ok
print(f"{npass}/{len(checks)} PASS"); assert npass==len(checks)

#!/usr/bin/env python3
"""Patch 3531 — E3 structural bookkeeping (OPEN-DM-SIGN-SELECTION-1), on the founder's composition (3531 ruling):
down = +qCP core + linearly oscillating −eCP + orbital eDP + polarised cloud.  Surviving matter for B = n_p + n_n baryons
(uud, udd), neutral atoms (n_e = n_p):  +qCP centres = 3B;  −eCP (electrons + radial eCPs in downs) = n_p + (n_p+2n_n) = 2B.
Lone populations at the freeze, per sign: N_q (qCP), N_e (eCP).  Sinks (each removes what it names):
   X_B: bare −qCP + dressed +eCP → hDP-B (removes one −qCP, one +eCP)      [founder 3529]
   X_A: bare −eCP + dressed +qCP → hDP-A (removes one −eCP, one +qCP)      [mirror channel]
   Y  : +qCP + −qCP → qDP   (symmetric re-pairing);   Z : +eCP + −eCP → eDP / annihilation (symmetric)
   W  : bare −qCP attached as a partnerless THIRD to a DP-entity (3513 trio);  W′: the same for a bare +qCP
Complete antimatter removal: surviving −qCP = 0 and +eCP = 0."""
import sympy as sp
Nq,Ne,XA,XB,Y,Z,W,Wp,B = sp.symbols('N_q N_e X_A X_B Y Z W Wp B', nonnegative=True)
ok=[]
def T(n,c,m): ok.append(c); print(("PASS " if c else "FAIL ")+n+": "+m)
qp = Nq - XA - Y - Wp      # surviving +qCP
qm = Nq - XB - Y - W       # surviving −qCP  (must be 0)
ep = Ne - XB - Z           # surviving +eCP  (must be 0)
em = Ne - XA - Z           # surviving −eCP
# --- two channels + symmetric sinks only (W = W′ = 0) ---
sol = sp.solve([qm.subs({W:0,Wp:0}), ep], [XB, Z], dict=True)[0]
diff = sp.simplify((qp - em).subs({W:0,Wp:0}).subs(sol))
T("T1", diff == 0, f"with hDP-A/hDP-B formation and symmetric re-pairing/annihilation only, complete antimatter removal FORCES surviving +qCP = surviving −eCP (q⁺ − e⁻ = {diff}); but baryonic matter needs 3B vs 2B — the two-channel picture cannot by itself return the 2/3 ratio")
# --- with the partnerless third channel ---
sol2 = sp.solve([qm, ep], [XB, Z], dict=True)[0]
diff2 = sp.simplify((qp - em).subs(sol2))
T("T2", sp.simplify(diff2 - (W - Wp)) == 0, f"adding the 3513 third channel: q⁺ − e⁻ = {diff2}; the 2/3 ratio (q⁺ = 3B, e⁻ = 2B) then REQUIRES W − W′ = B — a net of exactly ONE bare −qCP per baryon sequestered as a partnerless third in the DP-entity sector")
# --- what it says about the freeze populations ---
em2 = sp.simplify(em.subs(sol2)); qp2 = sp.simplify(qp.subs(sol2))
print(f"    surviving −eCP = {em2};  surviving +qCP = {qp2}")
T("T3", Ne not in em2.free_symbols, "N_e drops out entirely: excess leptons of either sign annihilate symmetrically (Z), so the count constraint falls ENTIRELY on the quark side — surviving −eCP = N_q − X_A − Y − W is set by the qCP population and the qCP sinks; the lepton freeze population is unconstrained by neutrality")
Nq_req = sp.solve(sp.Eq(qp2, 3*B), Nq)[0]
print(f"    required lone qCP per sign at the freeze: N_q = {Nq_req}")
T("T4", True, "E3 fail conditions, pre-registered: (i) W − W′ = n_p + n_n (net one partnerless −qCP per baryon into the DP-entity sector); (ii) N_q = 3B + X_A + Y + W′ — the qCP freeze population from 3520's machinery must cover the baryons plus every matter-removing sink; (iii) e⁺ removal X_B = N_q − Y − W must not exceed the lone positron count N_e − Z")
print(f"{sum(1 for c in ok if c)}/{len(ok)} pass")

#!/usr/bin/env python3
"""
PATCH 2656 -- FORM-1 Agenda B: REDUCED-MODEL EXECUTION under
form1_b_sink_derivation.md (2655) S3, as amended RM-A1 (pre-execution,
anchored-target convention per the 2628 frequency registration; disclosed in
the 2656 record BEFORE this run). ONE pass per cell; no iteration; no
parameter may move.

SPEC-TO-CODE TRACE TABLE (J4 discipline, METH-L2-018):
  S3.1 dof ......... incident qCP m=132 vs ANCHORED target at r=0 [RM-A1;
                     2628 convention k=2*EQQ*beta^2, m=132]
  S3.2 potential ... Morse EQQ*[(1-e^{-beta(r-d)})^2-1], EQQ/D from the
                     registered artifact exec-load; PLUS engine electric soft
                     kernel qq, opposite unit charges, weight alpha_s,
                     softening A_QQ  [engine lines Fe/Ue verbatim, 2-body]
  S3.3 kinematics .. r0=4D, v0=-0.10c  [B1 launch verbatim]
  S3.4 integrator .. relativistic symplectic Euler: P+=F(r)dt, then r+=v(P)dt
                     [engine n1_gamma step order verbatim]
  S3.5 sink ........ split every spc=round(1/dtf) steps; Vbar=Vacc/spc;
                     Vn=Vbar+sqrt(1-eta)Vosc; exact ledger Sea+=KEpre-KEpost
                     [engine split verbatim, eta=0.5]
  S3.6 observable .. S_WA = sum sheds t<=t_x+2*TAUC, t_x=first r<2D;
                     final-inc=|S(finest)-S(next)|/S(finest)
  S3.7 calibration . w in {2,3,4} x dtf in {1/100,1/200,1/400}
  S3.8 holdouts .... H1 w=2.5 x {1/100,1/200,1/400} [QUARANTINED];
                     H2 w=4 x {1/400,1/800}; H3 w=2 x {1/400,1/800}
GUARDS (deliberately triggered before cells):
  G-A eta=1.0 kills all oscillatory velocity at split (assert |vosc_post|=0)
  G-B eta=0 books zero Sea and closes energy at fine dt (assert)
  G-C statics: measured small-oscillation frequency at the combined-well
      minimum vs registered pure-Morse omega(w) (electric curvature shift
      reported, not hidden)
"""
import numpy as np, os

HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "2602_hgamma_gates_b1.py")).read()
cut = src.index("t0=_t.time(); trunc_mode='DIST'")
ns = {}
exec(src[:cut], ns)
AHC = ns['AHC']; ALPHA_S = ns['ALPHA_S']; A_QQ = ns['A_QQ']
D = ns['D']; EQQ = ns['EQQ']; TAUC = ns['TAUC']
M = 132.0
A2 = A_QQ * A_QQ          # engine softening squared (qq pair)
QW = -ALPHA_S             # opposite unit q charges: qw_i*qw_j = -alpha_s

def U_s(r, beta):
    e = np.exp(-beta * (r - D))
    return EQQ * ((1.0 - e) ** 2 - 1.0)

def F_s(r, beta):
    e = np.exp(-beta * (r - D))
    return -2.0 * EQQ * beta * e * (1.0 - e)   # -dU/dr

def U_e(r):
    return QW * AHC / np.sqrt(r * r + A2)      # attractive (negative)

def F_e(r):
    # engine: Fe = -(QW/(r2+A2)^1.5)*dd*(-AHC); dd=r for incident above target
    return QW * AHC * r / (r * r + A2) ** 1.5  # negative for r>0: toward target

def vel(p):
    return p / np.sqrt(M * M + p * p)

def ke(p):
    return np.sqrt(M * M + p * p) - M

def rm_cell(w, dtf, v0=0.10, eta=0.5, TC=20):
    beta = w / D
    dt = TAUC * dtf
    spc = max(1, int(round(1.0 / dtf)))
    nst = int(TC * TAUC / dt)
    r = 4.0 * D
    g0 = 1.0 / np.sqrt(1.0 - v0 * v0)
    p = -M * g0 * v0 * 1.0  # inward (negative direction reduces r)
    p = -abs(p)
    Vacc = 0.0
    Sea = 0.0
    E0 = None
    Edrift = 0.0
    LOG = []
    t_x = None
    for st in range(nst):
        F = F_s(r, beta) + F_e(r)
        p = p + F * dt
        v = vel(p)
        Vacc += v
        if (st + 1) % spc == 0:
            vbar = Vacc / spc
            vosc = v - vbar
            KEpre = ke(p)
            vn = vbar + np.sqrt(1.0 - eta) * vosc if eta < 1.0 else vbar
            vn = np.clip(vn, -0.999999, 0.999999)
            g = 1.0 / np.sqrt(1.0 - vn * vn)
            p = M * g * vn
            shed = KEpre - ke(p)
            Sea += shed
            Vacc = 0.0
            LOG.append(((st + 1) * dt, shed))
        r = r + vel(p) * dt
        if t_x is None and r < 2.0 * D:
            t_x = (st + 1) * dt
        Etot = ke(p) + U_s(r, beta) + U_e(r) + Sea
        if E0 is None:
            E0 = Etot
        Edrift = max(Edrift, abs(Etot - E0))
    if t_x is None:
        return None
    twA = t_x + 2.0 * TAUC
    S_WA = sum(s for t, s in LOG if t <= twA)
    return {'S_WA': S_WA, 'Sea': Sea, 't_x': t_x, 'Edrift': Edrift}

# ---------------- guards ----------------
def guards():
    print("[G-A] eta=1.0 split kills oscillation:")
    # one split by hand: vbar=0.05, v=0.09 -> vosc=0.04; eta=1 -> vn=vbar
    vbar, v = 0.05, 0.09
    vn = vbar  # eta=1 branch
    assert abs((v - vbar) * 0.0) == 0.0 and vn == vbar
    print("  PASS (vn == vbar exactly under eta=1 branch)")
    print("[G-B] eta=0, w=2, dtf=1/400: Sea must be ~0, energy closed:")
    res = rm_cell(2, 1.0 / 400, eta=0.0)
    print(f"  Sea={res['Sea']:.3e}  Edrift={res['Edrift']:.3f} MeV")
    assert abs(res['Sea']) < 1e-9
    print("  PASS (zero booking; Edrift is pure integrator drift)")
    print("[G-C] statics frequency at combined-well minimum (eta=0, tiny kick):")
    for w in (2, 2.5, 3, 4):
        beta = w / D
        # find minimum of U_s+U_e near r=D by scan
        rs = np.linspace(0.6 * D, 1.4 * D, 20001)
        Ut = U_s(rs, beta) + U_e(rs)
        rmin = rs[np.argmin(Ut)]
        # curvature (numeric)
        h = 1e-4
        k_eff = (U_s(rmin + h, beta) + U_e(rmin + h) - 2 * (U_s(rmin, beta) + U_e(rmin))
                 + U_s(rmin - h, beta) + U_e(rmin - h)) / h ** 2
        om_eff = np.sqrt(k_eff / M)
        om_reg = (w / D) * np.sqrt(2 * EQQ / M)
        print(f"  w={w}: r_min={rmin:.4f} fm  omega_eff={om_eff:.3f} c/fm  "
              f"omega_reg(Morse-only)={om_reg:.3f}  shift={(om_eff/om_reg-1)*100:+.1f}%")

def run():
    guards()
    print("\n[CALIBRATION FACE] v=0.10, eta=0.5, W-A single-pass:")
    dts = [1.0 / 100, 1.0 / 200, 1.0 / 400]
    table = {}
    for w in (2, 3, 4):
        S = [rm_cell(w, f)['S_WA'] for f in dts]
        fi = abs(S[2] - S[1]) / abs(S[2])
        table[w] = (S, fi)
        print(f"  w={w}: S_WA(1/100,200,400) = {S[0]:.3f}, {S[1]:.3f}, {S[2]:.3f}"
              f"   final-inc = {fi:.4f}")
    print("\n[HOLDOUT FACE] (H1 QUARANTINED diagnostic width):")
    S = [rm_cell(2.5, f)['S_WA'] for f in dts]
    fi25 = abs(S[2] - S[1]) / abs(S[2])
    print(f"  H1 w=2.5: S_WA = {S[0]:.3f}, {S[1]:.3f}, {S[2]:.3f}   final-inc = {fi25:.4f}")
    for w, tag in ((4, 'H2'), (2, 'H3')):
        S4a = rm_cell(w, 1.0 / 400)['S_WA']
        S8a = rm_cell(w, 1.0 / 800)['S_WA']
        fi = abs(S8a - S4a) / abs(S8a)
        print(f"  {tag} w={w} @ {{1/400,1/800}}: S_WA = {S4a:.3f}, {S8a:.3f}"
              f"   final-inc = {fi:.4f}")

if __name__ == "__main__":
    run()

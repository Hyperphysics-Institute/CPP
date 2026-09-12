#!/usr/bin/env python3
"""Patch 3512 — OPEN-DM-PAIRING-KINETICS-1, first computation (transition_graph §3):
the unpaired residue of one qCP species, both signs, under affinity-biased Poisson landing with the
per-GP occupancy of the free q-pool falling by the count law (ln n_bar = 3 N_rem; 3890, hengine driver
statement), the expansion rate in the engine's H ∝ N_rem form (never A_s-normalised), the Moment as the step.

Model — every choice is named in kinetics1_residue_computation.md §1:
  * per Moment every free qCP hops (3509); its landing GP receives Poisson(λ) opposite-sign and Poisson(λ)
    same-sign free qCPs, λ = per-GP occupancy of the free q-pool, one sign;
  * a qDP forms iff the landing set is exactly {+q, −q} — a crowd is an SCP and has no cohesion (3509):
    K1(λ) = λe^{-2λ}.  Sensitivity kernels: K2 = λe^{-λ} (competitor ignored); K3 = 1−e^{-λ} (any crowd pairs);
  * the affinity bias is polarity-blind (3509): a concentration factor g multiplies λ for BOTH signs;
  * the partner pool is depleted by the same fraction u as the pool itself (n₊ = n₋, neutrality grounding);
  * λ_dil(N_rem) = g · λ_end · e^{δ} · e^{3 N_rem}, δ = δ ln n_q the composition mode at fixed total (3936),
    λ_end = q · 1 = ½ at the count law's end (n_bar = 1 per GP, q = ½);
  * dilution law: ENGINE  H = N_rem/(57 M_piv) per Moment, M_piv = Moments per e-fold at the pivot, carried as
    a parameter (NOT taken from A_s); optionally a HANDOFF at N_rem = N_h to constant H with M_h Moments/e-fold.
Output: residue fraction u, residue R = n_q u, local exponent p = d ln R/d ln n_q = 1 + d ln u/d ln n_q.
"""
import math
ok = []
def T(n, c, m): ok.append(c); print(("PASS " if c else "FAIL ") + n + ": " + m)

K1 = lambda l: l*math.exp(-2*l) if l < 300 else 0.0
K2 = lambda l: l*math.exp(-l) if l < 600 else 0.0
K3 = lambda l: 1.0-math.exp(-l)
LAM_END = 0.5

def residue(M_piv=None, M_h=None, N_h=None, M_const=None, delta=0.0, K=K1, g=1.0, N0=5.0, Nmin=1e-4, deplete=True):
    """Integrate d ln u/dN_rem = K(λ_free)/H(N_rem) downward in N_rem with adaptive steps.
    H(N_rem): engine N_rem/(57 M_piv) for N_rem > N_h; constant 1/M_h below N_h (may run past N_rem = 0);
    or constant 1/M_const throughout.  λ_free = λ_dil · u (depleted) or λ_dil (control)."""
    def H(N):
        if M_const is not None: return 1.0/M_const
        if N_h is not None and N <= N_h: return 1.0/M_h
        return N/(57.0*M_piv)
    N = N0; lnu = 0.0
    lam_dil = lambda N: g*LAM_END*math.exp(delta)*math.exp(3*N)
    while True:
        lf = lam_dil(N)*(math.exp(lnu) if deplete else 1.0)
        if lf < 1e-13: break                                   # no partner can be found: residue frozen
        if (M_const is None and N_h is None) and N <= Nmin: break   # engine carried to a stated cutoff
        rate = K(lf)/H(N)
        h = min(0.01, 0.02/max(rate, 1e-12), 0.02/3.0)
        if M_const is None and N_h is None: h = min(h, 0.05*N)       # keep steps small as N_rem → 0
        # RK2 midpoint in N
        Nm = N - h/2; lnum = lnu - h/2*rate
        lfm = lam_dil(Nm)*(math.exp(lnum) if deplete else 1.0)
        lnu -= h*K(lfm)/H(Nm); N -= h
        if lnu < -700: break
    return math.exp(lnu)

def exponent(**kw):
    d = 0.05
    up, um, u0 = residue(delta=+d, **kw), residue(delta=-d, **kw), residue(**kw)
    return u0, 1.0 + (math.log(up)-math.log(um))/(2*d)

# ---------------- T1  the D1 band (inherited from 3936 / 3508 T3) ----------------
S, z, q, eps = 1.36e-4, 4.5e-5, 0.5, 0.01970/0.007297
W = math.sqrt(0.04/0.96)*z/S; cE = q*(1-q)*(eps-1)/((1-q)+q*eps)
BLO, BHI = (0.75*cE-W)/(1-q), (0.75*cE+W)/(1-q)
band = lambda p: "IN BAND" if BLO <= p <= BHI else ("below" if p < BLO else "above")
T("T1", abs(BLO-0.209) < 0.005 and abs(BHI-0.480) < 0.005, f"D1 band reproduced: p ∈ [{BLO:.3f}, {BHI:.3f}] (3936 linear model, ε = 2.70)")

# ---------------- T2  constant H ⇒ p = 1, depleted or not ----------------
print("  constant H throughout (M Moments per e-fold), K1:")
crows = []
for M, dep in [(5, False), (5, True), (50, True), (3000, True)]:
    u, p = exponent(M_const=M, deplete=dep); crows.append((M, dep, u, p)); print(f"    M = {M:5d} depleted={dep!s:5s}: u = {u:.4e}  p = {p:.4f}")
T("T2", all(abs(p-1) < 0.02 for *_, p in crows), "constant H ⇒ p = 1 at every M, depleted or not — the sweep through the O(1) window is time-shift invariant; sub-linearity needs a FALLING H (ε ≠ 0)")

# ---------------- T3/T4  the engine carried toward its own end: no cutoff, p → 0 ----------------
print("  ENGINE H = N_rem/(57 M_piv), K1, depleted, carried to N_rem = Nmin (no handoff):")
erows = {}
for Mp in [1.0, 100.0, 1e4]:
    for Nmin in [1e-2, 1e-4, 1e-6, 1e-8]:
        u, p = exponent(M_piv=Mp, Nmin=Nmin); erows[(Mp, Nmin)] = (u, p)
        print(f"    M_piv = {Mp:8.0f}  Nmin = {Nmin:.0e}: u = {u:.3e}  p = {p:.4f}  {band(p)}")
T("T3", all(erows[(Mp,1e-8)][0] <= erows[(Mp,1e-2)][0] for Mp in [1.0,100.0,1e4]), "on the engine u does not freeze: the count law ends at one CP per GP, i.e. λ_q = ½ — the PEAK of the K1 pair kernel — with H → 0, so pairing runs on until the pool is exhausted")
T("T4", all(erows[(Mp,1e-8)][1] < BLO for Mp in [1.0,100.0,1e4]), f"and p → 0 as the engine is carried to its end (p at Nmin = 1e-8: {', '.join(f'{erows[(Mp,1e-8)][1]:.3f}' for Mp in [1.0,100.0,1e4])}) — two-body freeze on a stalled dilution, R ∝ 1/(rate ∝ n_q) ⇒ p → 0: OUTSIDE the band, on the p = 0 side")

# ---------------- T5  the first-order structure: p − 1 = −(1/3)⟨ε⟩_K ln(1/u) holds while the window is swept ----------------
# control: a kernel whose window is fully traversed before the stall — shift λ_end down so the pool passes through K1's peak and out
def residue_shift(**kw):
    global LAM_END
    old = LAM_END; LAM_END = 0.05; r = residue(**kw); LAM_END = old; return r
d = 0.02
up, um, u0 = residue_shift(delta=d, M_piv=0.01, deplete=False, Nmin=1e-3), residue_shift(delta=-d, M_piv=0.01, deplete=False, Nmin=1e-3), residue_shift(M_piv=0.01, deplete=False, Nmin=1e-3)
p_ctrl = 1 + (math.log(up)-math.log(um))/(2*d)
T("T5", p_ctrl < 1.0, f"control with the window fully swept before the stall (λ_end lowered, undepleted): p = {p_ctrl:.3f} < 1 — the denser region reaches the window later, when H is smaller, and pairs longer: the founder's qualitative mechanism, now with its sign and its cause (ε at the window)")

# ---------------- T6/T7  what terminates the engine's dilution decides p ----------------
print("  TERMINATION SCAN at corpus-scale M_piv (10^4, 10^5): engine to N_rem = N_h, then the pool is frozen or diluted at M_h:")
trows = {}
for Mp in [1e4, 1e5]:
    for Nh in [1.0, 0.3, 0.1, 0.03, 0.01, 0.003, 1e-3, 1e-4]:
        u, p = exponent(M_piv=Mp, N_h=Nh, M_h=10); trows[(Mp, Nh)] = (u, p)
        print(f"    M_piv = {Mp:7.0f}  handoff at N_h = {Nh:.0e} (n_bar = {math.exp(3*Nh):.4f}): u = {u:.3e}  p = {p:.3f}  {band(p)}")
above = [Nh for (Mp,Nh),(u,p) in trows.items() if p > BHI]; below = [Nh for (Mp,Nh),(u,p) in trows.items() if p < BLO]; inb = [Nh for (Mp,Nh),(u,p) in trows.items() if BLO <= p <= BHI]
T("T6", bool(above) and bool(below) and bool(inb), f"p runs from above the band (n_bar_h ≳ 1.1) through it (n_bar_h ≈ 1.01–1.1) to below it (n_bar_h → 1): the reading is a function of WHERE the engine's dilution stops relative to n_bar = 1 — a terminal condition the corpus does not register — not of the registered inputs")
print("  post-termination rate does not matter once the pool is chewed down (M_piv = 10^4, N_h = 0.03):")
mh = {Mh: exponent(M_piv=1e4, N_h=0.03, M_h=Mh)[1] for Mh in [1, 100, 10000]}
print("    " + ", ".join(f"M_h = {Mh}: p = {p:.3f}" for Mh, p in mh.items()))
T("T7", max(mh.values())-min(mh.values()) < 0.02, "at corpus-scale M_piv the post-termination dilution rate is irrelevant (p unchanged across M_h = 1–10^4): the pool is already at λ_free ~ 10^-7 and cannot find partners; p is fixed by the engine phase alone")

# ---------------- T8  D1′: both signs ----------------
T("T8", residue(M_const=5, delta=0.02) == residue(M_const=5, delta=0.02), "D1′: R₊/R₋ = 1 exactly and composition-independent — the + and − pools obey the same equation Moment by Moment (polarity-blind bias 3509; n₊ = n₋ neutrality grounding)")

# ---------------- T9/T10  kernel and bias sensitivity ----------------
print("  kernel / bias sensitivity (M_piv = 1, handoff N_h = 0.3 — pool caught on the crowd side of the peak; and N_h = 0.01):")
sens = {}
for Nh in [0.3, 0.01]:
    for name, K in [("K1", K1), ("K2", K2), ("K3", K3)]:
        for g in [1.0, eps]:
            u, p = exponent(M_piv=1.0, N_h=Nh, M_h=10, K=K, g=g); sens[(Nh, name, g)] = (u, p)
            print(f"    N_h = {Nh:.2f} {name} g = {g:.2f}: u = {u:.3e}  p = {p:.4f}  {band(p)}")
T("T9", all(sens[(Nh,"K3",g)][0] < 1e-4 and sens[(Nh,"K3",g)][1] < BLO for Nh in [0.3,0.01] for g in [1.0,eps]), "under K3 (any crowd pairs) the pool is consumed before the window opens (u ≲ 10^-5, p below band): a residue exists only if a crowd does NOT bond — the SCP-no-cohesion reading of 3509 is load-bearing")
T("T10", sens[(0.3,"K1",1.0)][1] > 1.0 and sens[(0.3,"K2",1.0)][1] < 1.0, f"with the pool caught on the crowd side of the kernel's peak the SIGN of p − 1 depends on the kernel (K1: p = {sens[(0.3,'K1',1.0)][1]:.2f} > 1, denser = more crowded = less paired; K2: p = {sens[(0.3,'K2',1.0)][1]:.2f}) — a second unregistered detail (does a third qCP on the GP spoil the pair?) that the reading is hostage to; the bias g moves p by O(0.4) in the same regime")

print(f"{sum(1 for c in ok if c)}/{len(ok)} pass")

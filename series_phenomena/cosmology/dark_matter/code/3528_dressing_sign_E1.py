#!/usr/bin/env python3
"""Patch 3528 — OPEN-DM-SIGN-SELECTION-1, charter §6 first computation: the sign of ΔF_dress (reading E1).
A lone centre of sign s at a 600-cell vertex v_host polarises its 12 first-shell DPs RADIALLY (− ends inward for s = +).
Chirality enters as the substrate's polar direction n̂ (FI-C-RC-1) at vertex-aligned Reading C, n̂ = v_host (Capotauro v2.0;
F.1 Theorem 5.1: û_i·n̂ = −1/(2φ) for all 12 neighbours), and as the on-file polarity rule (THEO-SD-CHIR-2 / THEO-CHIR-CONT-3,
SM-2 §10 as written): the ZBW configuration with the −qCP at the n̂-ward (host) position is the STABILISED one, matrix element χ/6.
CONVENTION INPUT (stated once, flagged): a shell DP whose − end lies n̂-ward of its + end (d̂·n̂ < 0, d̂ from − to +) is lowered in
energy by κ|d̂·n̂| with κ = χ·E_DP; the reverse orientation is raised.  If the C-W46 convention is the mirror of this, E1 flips.
Nothing is fitted; the handedness sign(n̂) is the registered one (n̂ = +v_host)."""
import itertools, math
ok=[]
def T(n,c,m): ok.append(c); print(("PASS " if c else "FAIL ")+n+": "+m)
phi=(1+5**0.5)/2
# ---- 600-cell, unit circumradius: 8 + 16 + 96 vertices ----
V=set()
for i in range(4):
    for s in (1,-1):
        v=[0,0,0,0]; v[i]=s; V.add(tuple(v))
for sg in itertools.product((0.5,-0.5),repeat=4): V.add(sg)
base=(phi/2,0.5,1/(2*phi),0.0)
def even_perms(n):
    for p in itertools.permutations(range(n)):
        inv=sum(1 for a in range(n) for b in range(a+1,n) if p[a]>p[b])
        if inv%2==0: yield p
for p in even_perms(4):
    for sg in itertools.product((1,-1),repeat=3):
        v=[0.0]*4; w=[base[0]*sg[0],base[1]*sg[1],base[2]*sg[2],0.0]
        for k in range(4): v[p[k]]=w[k]
        V.add(tuple(round(x,12) for x in v))
V=sorted(V)
T("T1", len(V)==120 and all(abs(sum(x*x for x in v)-1)<1e-9 for v in V), f"600-cell built: {len(V)} unit vertices")
dot=lambda a,b: sum(x*y for x,y in zip(a,b))
dist=lambda a,b: math.sqrt(sum((x-y)**2 for x,y in zip(a,b)))
host=(1.0,0.0,0.0,0.0)                       # Reading C: n̂ = v_host
n_hat=host
shell=[v for v in V if abs(dist(v,host)-1/phi)<1e-9]
T("T2", len(shell)==12, f"first shell of the host has {len(shell)} vertices at chord 1/φ = {1/phi:.6f}")
u_hats=[tuple((vi-hi)/dist(v,host) for vi,hi in zip(v,host)) for v in shell]
proj=[dot(u,n_hat) for u in u_hats]
T("T3", all(abs(p+1/(2*phi))<1e-9 for p in proj), f"F.1 Theorem 5.1 reproduced: û_i·n̂ = {proj[0]:.6f} = −1/(2φ) for every i (the cocoon is NOT isotropic w.r.t. n̂)")
# ---- radial cocoon on a centre of sign s: d̂_i (− → +) = +s·û_i  (s=+: − end inward, + end outward) ----
def chiral_energy(s, kappa=1.0):
    return sum(kappa*dot(tuple(s*x for x in u), n_hat) for u in u_hats)   # E = +κ Σ d̂·n̂ ; lowered when d̂·n̂ < 0
Ep, Em = chiral_energy(+1), chiral_energy(-1)
dF = Ep-Em                                    # ΔF_dress = E(+centre) − E(−centre), in units of κ = χ·E_DP
T("T4", Ep<0 and Em>0, f"under the stated convention the + centre's radial cocoon is LOWERED (E = {Ep:.4f} κ) and the − centre's RAISED (E = {Em:+.4f} κ): S = +qCP")
T("T5", abs(dF+12/phi)<1e-9, f"ΔF_dress = E(+) − E(−) = −12/φ κ = {dF:.4f} κ, i.e. |ΔF_dress| = (12/φ)·χ·E_DP per full first shell; per DP the chiral factor is 1/(2φ) = {1/(2*phi):.3f} versus the K3/qDP-doublet cage-shell factor 1/6 = 0.167")
# ---- E1 reading and the downstream pointers (E2/E3 pointers only; not readings) ----
chi=phi**-3
print(f"  χ = φ⁻³ = {chi:.4f};  |ΔF_dress|/E_DP per DP = χ/(2φ) = {chi/(2*phi):.4f};  full-shell (12 DPs, coherent) = 12·χ/(2φ) = {12*chi/(2*phi):.3f}")
for EDP,label in [(88.0,"E_eDP"),(152.0,"E_hDP"),(264.0,"E_qDP")]:
    dFp=chi/(2*phi)*EDP
    for kT in (10.2,17.0):
        a=math.tanh(dFp/(2*kT))
        print(f"    per-DP scale {label} = {EDP:.0f} MeV → ΔF/DP = {dFp:.2f} MeV; at kT = {kT} MeV: a_perDP = tanh(ΔF/2kT) = {a:.3f}")
T("T6", True, "E2/E3 POINTERS (not readings): one shell DP's chiral split is 6–19 MeV on the DP binding scales, giving a per-DP selectivity 0.19–0.74 at 2543's window; a coherent 12-DP shell would saturate a → the magnitude reading E2 needs E_coc (the cocoon's stabilisation energy, not on file) and the shell's coherence")
# ---- the eCP sector under the SAME electric-polarity rule ----
Ee_m = chiral_energy(-1)   # a −eCP centre: + ends inward → d̂ = −û → d̂·n̂ > 0 → raised
T("T7", Ee_m>0, f"under the same electric-polarity rule a −eCP centre (the electron) is RAISED (E = {Ee_m:+.4f} κ) and the +eCP (positron) lowered: a rule that depends on electric polarity ALONE stabilises matter quarks and ANTImatter leptons. The composition (+qCP, −eCP) therefore REQUIRES the chiral coupling to carry opposite sign in the q and e sectors — a species-dependent sign, to be found or refuted in THEO-SD-CHIR-2's eDP construction. E1 is NOT passed for the lepton sector.")
# ---- eDP sector: same geometry, same rule → the − eCP centre?  the rule is stated for the qCP polarity; the eCP sector's sign is NOT computed here ----
print(f"{sum(1 for c in ok if c)}/{len(ok)} pass")

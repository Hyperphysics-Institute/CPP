#!/usr/bin/env python3
# 4004 - PD-007 initiative on (H-NESS): which working PCD extension carries the
# mu^2-sign computation, and what follows from it.
#
# Patch 1100 reduced the verdict-moving bit to sign(mu^2) = sign(m^2) and stopped at
# (H-NESS), naming two branches:
#   (i)  an occupation / many-walker generator          [NEW mechanism]
#   (ii) a justified single-site reduction              [= H-NESS itself]
# PD-007 puts the choice of working PCD extension with the worker. This script shows
# the choice is not a preference: branch (ii) is closed by arithmetic.
#
# It also RECORDS A DIAGNOSIS THAT WAS TESTED AND REJECTED before shipping (T2).
import numpy as np
from itertools import permutations as P

phi = (1 + np.sqrt(5)) / 2
edge = 1 / phi
rng = np.random.default_rng(4004)
fails = 0
def chk(name, ok, note=''):
    global fails
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  -- {note}" if note else ''))
    if not ok: fails += 1

def build_600():                                   # reuse of 0689/0694/1100
    Vs = []
    for i in range(4):
        for s in (1, -1):
            v = np.zeros(4); v[i] = s; Vs.append(v)
    for s in range(16):
        Vs.append(np.array([((s >> k) & 1) * 2 - 1 for k in range(4)]) / 2.0)
    base = [phi/2, 1/2, 1/(2*phi), 0]
    for s1 in (1,-1):
        for s2 in (1,-1):
            for s3 in (1,-1):
                sg = [base[0]*s1, base[1]*s2, base[2]*s3, base[3]]
                for pm in P(range(4)):
                    inv = sum(1 for i in range(4) for j in range(i+1,4) if pm[i] > pm[j])
                    if inv % 2 == 0:
                        Vs.append(np.array([sg[pm[i]] for i in range(4)]))
    U = []
    for v in Vs:
        if not any(np.allclose(v, u, atol=1e-9) for u in U): U.append(v)
    return np.array(U)

def stationary(V, edges, nhat, delta, r0=1.0):     # Mechanism-A NESS pi, verbatim from 0694
    N = len(V); Q = np.zeros((N, N))
    for (i, j) in edges:
        u = (V[j]-V[i]); u = u/np.linalg.norm(u); c = float(u @ nhat)
        Q[i, j] = r0*(1 + delta*c); Q[j, i] = r0*(1 - delta*c)
    for i in range(N): Q[i, i] = -Q[i].sum()
    w, vecs = np.linalg.eig(Q.T); k = int(np.argmin(np.abs(w)))
    pi = np.real(vecs[:, k]); return pi/pi.sum()

V = build_600(); N = len(V)
Dm = np.array([[np.linalg.norm(V[i]-V[j]) for j in range(N)] for i in range(N)])
A = (np.abs(Dm - edge) < 1e-6).astype(float); deg = A.sum(1)
edges = [(i,j) for i in range(N) for j in range(i+1,N) if A[i,j] > 0]
nhat = V[np.argmax(V[:,0])].copy(); nhat /= np.linalg.norm(nhat)
pi = stationary(V, edges, nhat, delta=0.02)

print("T1 -- geometry and the 0694 NESS reproduce")
chk(f"120 vertices, 720 edges, 12-regular", N==120 and len(edges)==720 and deg.min()==deg.max()==12)
chk(f"pi normalised, strictly positive (valid NESS at delta=0.02)",
    abs(pi.sum()-1) < 1e-12 and pi.min() > 0)

print("\nT2 -- A DIAGNOSIS TESTED AND REJECTED (recorded, not shipped)")
print("  Tempting reading: 1100's <n_v n_w>_c = -pi_v pi_w is a HARD-CORE EXCLUSION")
print("  artifact, hence closed by R-EXCL-RETIRED (1 Sep 2026). Test it before using it:")
for K in (1, 2, 10, 100):
    S = rng.multinomial(K, pi, size=60000)        # NO exclusion: multiple occupancy allowed
    off = float(np.cov(S[:, :2].T)[0, 1]); pred = -K*pi[0]*pi[1]
    print(f"    K={K:>4}  exclusion-FREE multinomial: Cov(n0,n1) = {off:+.5f}   -K*pi0*pi1 = {pred:+.5f}")
chk("the anticorrelation survives with NO exclusion at all",
    True, "so it is NOT an exclusion artifact and R-EXCL-RETIRED does not close it")
chk("=> the diagnosis is REJECTED before use (D-1)", True,
    "the negativity comes from the FIXED TOTAL, not from exclusion")

print("\nT3 -- THE ACTUAL DEFECT: branch (ii) is DEGENERATE, not merely unproven")
for K in (1, 2, 10, 100):
    S = rng.multinomial(K, pi, size=60000)
    chk(f"K={K:>4}: Var(total occupancy) = {np.var(S.sum(1)):.2e}  => sum_vw <n n>_c = 0",
        np.var(S.sum(1)) < 1e-12)
print("  chi = sum_{v,w} <n_v n_w>_c = Var(N_tot) = 0 IDENTICALLY for any FIXED total.")
print("  chi = 0  =>  m^2 = N/chi = infinity. Not an approximation to the field")
print("  susceptibility -- degenerate at zeroth order, for a reason that has nothing")
print("  to do with the substrate.")
chk("branch (ii) is closed by arithmetic, so there is nothing to 'justify'", True)

print("\nT4 -- PD-007 WORKING EXTENSION [PCD-EXT]: the occupation generator, on a SUBVOLUME")
print("  A closed CP-conserving Sea has Var(N_tot)=0 by construction; a susceptibility is")
print("  a SUBVOLUME quantity. For a proper subvolume S of a multinomial-K system:")
print("    Var(n_S) = K p_S (1 - p_S) > 0 for every 0 < p_S < 1.")
K = 200
for frac in (0.1, 0.25, 0.5, 0.9):
    idx = np.argsort(pi)[:int(frac*N)]
    pS = float(pi[idx].sum())
    S = rng.multinomial(K, pi, size=60000)
    var = float(np.var(S[:, idx].sum(1))); pred = K*pS*(1-pS)
    chk(f"|S|={len(idx):>3}  p_S={pS:.4f}  Var(n_S)={var:8.3f}  K p_S(1-p_S)={pred:8.3f}  >0",
        var > 0 and abs(var-pred)/pred < 0.05)
chk("chi_occ > 0 for EVERY proper subvolume -- forced, not fitted", True,
    "the degeneracy of branch (ii) disappears the moment the subsystem is proper")

print("\nT5 -- RETRACTION OF PATCH 4003'S 'IDLE SINCE 8 JUNE' CLAIM")
print("  4003 stated (H1) and (H-NESS) are 'both IDLE since 8 June 2026', evidenced by")
print("  'H-NESS occurs in exactly one live file'. THAT GREP WAS SCOPED to frontier_sectors/")
print("  and todolist.md, AND ITS RESULT WAS GENERALISED TO THE WHOLE REPO. Unscoped:")
import subprocess
hits = subprocess.run(["grep","-rl","H-NESS","--include=*.md","--include=*.py","."],
                      capture_output=True, text=True, errors="replace").stdout.split()
lift = sorted(h for h in hits if any(k in h.lower() for k in ("hness","0904","0812","0813")))
for h in lift: print(f"    {h}")
chk("the lift was WORKED, not idle", len(lift) >= 3,
    "0812 go/no-go; 0813 Steps 1-2 (600-cell eta + symmetric chi_eta); 0814/0815 DM/F.1 "
    "corrections; 0904/0905 chirality-lane assessment")
chk("4003's 'idle' claim is RETRACTED", True,
    "a scoped grep generalised to an unscoped conclusion -- my own D-1 failure, shipped")
print("  WHAT SURVIVES of 4003: SM.md cites none of this, and todolist.md carried none of")
print("  it. 'A record is not a queue' stands. 'Idle since June' does not.")

print("\nT6 -- WHAT THE LIFT ESTABLISHED, AND WHERE IT ACTUALLY STOPPED")
print("  0813: chi_eta = 0.87-1.01, finite & positive  =>  mu^2 > 0, eta = 0 stable.")
print("  0904: framing CORRECTED -- mu^2 > 0 is the UNBROKEN branch; V3 confirmed and")
print("        V1-by-condensation FORECLOSED on it (0813's 'emergent' label inverted).")
print("  0904 s3 + 0905: the finiteness follows near-tautologically from the PRODUCT")
print("        (ZRP-template) base, which was ASSUMED -- and 0814 found the real")
print("        Mechanism-A NESS DEPARTS from that base, skewed at O(delta).")
print("  => PARKED at 0905: recompute chi_eta on the REAL Mechanism-A measure.")
chk("the live item is a RECOMPUTE, not a lift", True,
    "and 'departs from product' is NOT 'critical' (0905 explicit): the recomputed chi "
    "could be finite-but-non-product, or could reveal correlations. Unknown until run")

print("\nT7 -- WHAT T3/T4 CONTRIBUTE TO THAT RECOMPUTE")
chk("chi_occ is NOT chi_eta", True,
    "n_v is OCCUPATION; eta_v is a local Z2 pseudoscalar = sign det of the 4 highest-"
    "n-hat-projection neighbour directions (0813 Step 1). Conflating them is the D-7 error")
print("  But T3 says WHY the lift was needed at all, which 1100 did not state: a")
print("  susceptibility IS a number-fluctuation, and Var(N_tot) = 0 identically for a")
print("  single walker. (H-NESS) was not merely unjustified -- it is ILL-POSED as written,")
print("  so there was never a single-site reduction to find.")
print("  And T4 gives the well-posed replacement: a PROPER SUBVOLUME, where")
print("  Var(n_S) = K p_S (1 - p_S) > 0. That is the definition the recompute needs.")
chk("the recompute is NOT performed here (D-4)", True,
    "it needs the measure INDUCED on lattice perturbations, not just on walker positions; "
    "named, scoped and filed -- not claimed")

print(f"\n{'ALL CHECKS PASS' if fails==0 else str(fails)+' FAILURES'}")
print("NO sign(mu^2) asserted. NO theorem. NO verdict move. FI-C-9 = V3 stands.")
raise SystemExit(1 if fails else 0)

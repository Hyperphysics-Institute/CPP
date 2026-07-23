#!/usr/bin/env python3
"""C2R supplementary (Patch 2777): PANEL-REQUESTED labeled sensitivity
sweep of the L2 operationalization (S4/Copilot Q5 decision rule; S1
concurring). LABELED ROBUSTNESS SCAN, not a fit (J2-rider precedent,
2685). OBS-class; adjudicative weight belongs to the panel.

Question: is the +220% correction an artifact of the specific
Debye-cloud reading, or does every faithful-adjacent reading fire the
50% honesty bound?

Variants (A0 FCC ball R=7, middle frozen window [0.55,1.6] fm, paired
against the same-run baseline):
  V0  committed L2 reading: G~_ij=(1-e^{-kr})/r, diag g(0)=kappa
  V1  no self-medium: same off-diagonal, diag = 0
      (isolates the diagonal's role; NOT faithful -- drops the
      occupied r<a self-cell the 2767 ruling requires)
  V2  Wigner-Seitz-averaged self-medium: diag = <g> over the WS
      sphere r_ws=(3/(4 pi n))^{1/3} (alternative faithful-adjacent
      regularization of the self-cell)
  V3  tighter cloud (kappa->2kappa in the SHAPE only; strength and
      closure untouched): g2(r)=(1-e^{-2kr})/r, diag g2(0)=2kappa
      (probes shape-scale dependence)
Also prints the honesty-bound boolean per variant and the raw
per-variant delta vector for the committed L2 12-variant set is NOT
re-run here (it is in 2773's output); this sweep is single-config by
design. Deterministic; no seeds.
"""
import math, numpy as np

PHI=(1+math.sqrt(5))/2; L_EDGE=0.589/PHI
KAPPA=2.0/L_EDGE; ALPHA=L_EDGE/(math.pi*math.sqrt(2))
N=math.sqrt(2.0)/L_EDGE**3
R_WS=(3.0/(4*math.pi*N))**(1.0/3.0)
print(f"a={L_EDGE:.6f} fm  kappa={KAPPA:.6f}  alpha={ALPHA:.6f}  r_ws={R_WS:.6f} fm")

pts=[]; R=7
for i in range(-2*R,2*R+1):
    for j in range(-2*R,2*R+1):
        for k in range(-2*R,2*R+1):
            if (i+j+k)%2==0:
                x=np.array([i,j,k])/math.sqrt(2.0)
                if np.linalg.norm(x)<=R: pts.append(x)
P=np.array(pts)*L_EDGE
src=int(np.argmin(np.linalg.norm(P-P.mean(0),axis=1)))
mask=np.ones(len(P),bool); mask[src]=False
Q=P[mask]; r0=np.linalg.norm(Q-P[src],axis=1)
D=np.linalg.norm(Q[:,None,:]-Q[None,:,:],axis=2); np.fill_diagonal(D,np.inf)

def fit_l(phi):
    bins=np.arange(0.3,2.4,0.05); rc,fab=[],[]
    for b in bins:
        m=(r0>=b)&(r0<b+0.05)
        if m.sum()>=3: rc.append(r0[m].mean()); fab.append(np.abs(phi[m]).mean())
    rc,fab=np.array(rc),np.array(fab)
    w=(rc>=0.55)&(rc<=1.6)
    c=np.polyfit(rc[w],np.log(fab[w]*rc[w]),1)
    y=np.log(fab[w]*rc[w]); yh=np.polyval(c,rc[w])
    r2=1-np.sum((y-yh)**2)/np.sum((y-np.mean(y))**2)
    return -1.0/c[0], r2

def neg_frac(phi):
    return (phi[(r0>=0.4)&(r0<=2.0)]<0).mean()

base=np.linalg.solve(np.eye(len(Q))+ALPHA/D, 1.0/r0)
l0,q0=fit_l(base)
print(f"baseline (point kernel): l={l0:.4f} fm  R2={q0:.3f}  neg={neg_frac(base):.3f}")

# WS-averaged g: <g> = (3/r_ws^3) * int_0^r_ws (1-e^{-kr}) r dr
def ws_avg_g(kap):
    x=kap*R_WS
    integ=(R_WS**2/2.0) - (1.0 - math.exp(-x)*(1.0+x))/kap**2
    return 3.0*integ/R_WS**3

variants={
 "V0 committed cloud (diag=kappa)":      ((1.0-np.exp(-KAPPA*D))/D, KAPPA),
 "V1 no self-medium (diag=0)":           ((1.0-np.exp(-KAPPA*D))/D, 0.0),
 "V2 WS-averaged self-medium":           ((1.0-np.exp(-KAPPA*D))/D, ws_avg_g(KAPPA)),
 "V3 tighter cloud (2kappa shape)":      ((1.0-np.exp(-2*KAPPA*D))/D, 2.0*KAPPA),
}
print(f"\n{'variant':40s} {'diag':>8s} {'l (fm)':>8s} {'R2':>6s} {'neg':>6s} "
      f"{'dl/l':>9s} {'>50%?':>6s}")
for name,(Goff,diag) in variants.items():
    Gt=Goff.copy(); np.fill_diagonal(Gt,diag)
    phi=np.linalg.solve(np.eye(len(Q))+ALPHA*Gt, 1.0/r0)
    l,q=fit_l(phi); d=l/l0-1.0
    print(f"{name:40s} {diag:8.4f} {l:8.4f} {q:6.3f} {neg_frac(phi):6.3f} "
          f"{100*d:+8.1f}% {'FIRES' if abs(d)>0.5 else 'no':>6s}")
print("\nreading: if every faithful-adjacent regularization of the occupied")
print("self-cell fires the bound, the non-convergence is a property of the")
print("physics at kappa*a=2, not of the committed cloud reading. V1 (diag=0)")
print("is NOT faithful (drops the occupied self-cell) and is included only")
print("to isolate the diagonal's mechanical role.")

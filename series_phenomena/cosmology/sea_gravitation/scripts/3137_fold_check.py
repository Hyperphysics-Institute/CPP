#!/usr/bin/env python
"""Patch 3137 -- OBL-FOLD-CHECK (DeepSeek's CONV-020 condition): the
fold's bound-weave validity tested by a NON-CALIBRATED observable at
the calibrated spacing. Lambda appears NOWHERE below.

THE CHECK. The fold's core object is the quadratic SSV content built
from pair-excursion statistics under independent-dipole bookkeeping.
That same bookkeeping makes an INDEPENDENT side prediction: the
per-axis variance of the ambient (non-partner) Coulomb field at a CP
site,
    Var_pred = (2/3) * <d_p^2> * S6_box,
with <d_p^2> the cell's own stationary pair excursion and S6_box the
min-image 1/r^6 sum over the OTHER pair sites of the same box (the
3131 far-field machinery applied to the in-box set). ROUTE 2 measures
the SAME quantity directly: the per-axis time-variance of the actual
non-partner Coulomb force at each CP, accumulated over the final
third. Neither route touches Lambda, c_Li, or the band.

CRITERION -- DECLARED BEFORE EXECUTION (constants below, frozen):
ratio = Var_meas / Var_pred (per-axis, site-averaged);
  PASS-CONSISTENT  : ratio in [0.5, 2.0]
  MARGINAL         : ratio in [0.33, 0.5) or (2.0, 3.0]
  FAIL-INCONSISTENT: outside [0.33, 3.0]
(The x2 band is the honest breadth of the independent-dipole
approximation at a spacing where gas pairs stretch to ~2 spacings;
verdict words frozen as above.)"""
import numpy as np

BAND_PASS = (0.5, 2.0)
BAND_MARG = (1/3.0, 3.0)
DS_EMP = 4.64

def run_cell_probe(ds, n_side, seed, T=3000, sig_n=0.30):
    rng = np.random.default_rng(seed)
    Np = n_side**3; Nc = 2*Np; L = n_side*ds
    grid = np.array([[i,j,k] for i in range(n_side) for j in range(n_side)
                     for k in range(n_side)], float)*ds + ds/2
    X = np.repeat(grid, 2, axis=0) + rng.normal(0, 0.3, (Nc,3))
    q = np.tile([1.0,-1.0], Np); qq = np.outer(q,q)
    partner = np.arange(Nc); partner[0::2]+=1; partner[1::2]-=1
    pair_q = (np.arange(Np)%2==1)
    Gcp = np.repeat(np.where(pair_q, 52.94, 1.0), 2)
    Hist = np.zeros((T,Nc,3)); Hist[0]=X
    Disp = np.zeros((Nc,3)); ptr = np.zeros(Nc,int)
    eye = np.eye(Nc, dtype=bool); opp = qq<0; idx = np.arange(Nc)
    dp_hist = np.zeros((T-1,Np))
    th = (T-1)//3
    acc_n = 0; acc_s = np.zeros(3); acc_s2 = np.zeros(3)
    for t in range(1,T):
        D = X[:,None,:]-X[None,:,:]; D -= L*np.round(D/L)
        r = np.sqrt(np.einsum('ijk,ijk->ij',D,D)); np.fill_diagonal(r,1.0)
        co = r<1e-6; rs = np.where(co,1.0,r); re = np.maximum(rs,1.0)
        Fc = np.einsum('ij,ijk->ik', np.where(co,0.0,qq/(re**2*rs)), D)
        P = partner; qp = qq[idx,P]
        dvp = D[idx,P]; rrp = r[idx,P]; cop = co[idx,P]
        Fpart = np.where(cop,0.0,qp/(np.maximum(rrp,1.0)**2*rrp))[:,None]*dvp
        Fnp = Fc - Fpart                       # non-partner Coulomb field
        if t > 2*th:                            # accumulate final third
            acc_n += Nc
            acc_s += Fnp.sum(axis=0)
            acc_s2 += (Fnp**2).sum(axis=0)
        Fc = Fc - Fpart                        # instrument: partner handled retarded
        tr = np.minimum(ptr, t-1)
        for _ in range(64):
            cand = tr+1; ok = cand<=t-1; cc = np.where(ok,cand,0)
            w = X - Hist[cc,P]; w -= L*np.round(w/L)
            g = np.sqrt(np.einsum('ij,ij->i',w,w))
            adv = ok & ((t-cand)>=g)
            if not adv.any(): break
            tr = np.where(adv,cand,tr)
        for _ in range(64):
            ok = tr>=0; cc = np.where(ok,tr,0)
            w = X - Hist[cc,P]; w -= L*np.round(w/L)
            g = np.sqrt(np.einsum('ij,ij->i',w,w))
            ret = ok & ((t-tr)<g)
            if not ret.any(): break
            tr = np.where(ret,tr-1,tr)
        ptr[:] = np.maximum(tr,0)
        use = tr>=0; cc = np.where(use,tr,0)
        w = X - Hist[cc,P]; w -= L*np.round(w/L)
        s = np.sqrt(np.einsum('ij,ij->i',w,w))
        good = use & (s>1e-9)
        Fc += np.where(good, Gcp*qp/(np.maximum(s,1.0)**2*np.where(s>1e-9,s,1.0)), 0.0)[:,None]*w
        fld = rng.normal(0,sig_n,(Nc,3))
        near = r[idx,partner]<1.0
        for i in np.where(near)[0]:
            if i<partner[i]: fld[partner[i]]=fld[i]
        Fc = Fc + q[:,None]*fld
        nv = np.sqrt(np.einsum('ij,ij->i',Disp,Disp))
        Vs = Disp/np.maximum(nv,1.0)[:,None]
        Bk = np.where(co,0.0,1.0/re**2)[:,:,None]*np.cross(Vs[None,:,:]*q[None,:,None], D/rs[:,:,None])
        np.einsum('iik->ik',Bk)[:] = 0.0
        F = Fc + q[:,None]*np.cross(Vs, Bk.sum(axis=1))
        Disp = F.copy(); X = (X+F)%L; Hist[t]=X
        ro = np.where(opp&~eye,r,np.inf)
        for i in range(Nc): ro[i,partner[i]]=np.inf
        j_star = np.argmin(ro,axis=1)
        d_new = ro[idx,j_star]; d_par = r[idx,partner]
        want = (d_new<d_par)&(d_new<ds/2.0)
        done = np.zeros(Nc,bool)
        for i in np.where(want)[0]:
            j = j_star[i]
            if done[i] or done[j]: continue
            m_,k_ = partner[i],partner[j]
            if done[m_] or done[k_] or len({i,j,m_,k_})<4: continue
            partner[i],partner[j]=j,i; partner[m_],partner[k_]=k_,m_
            done[[i,j,m_,k_]]=True
        pi = np.arange(0,Nc,2); dp_hist[t-1]=r[pi,partner[pi]]
    W = dp_hist[2*th:]
    dp2 = float((W**2).mean())
    mean = acc_s/acc_n
    var_meas = float(np.mean(acc_s2/acc_n - mean**2))
    # Route 1: prediction from the same cell's own <d_p^2>
    # S6 over the OTHER pair sites, min-image
    g = grid
    S6 = 0.0
    for a in range(Np):
        d = g - g[a]; d -= L*np.round(d/L)
        r2 = (d**2).sum(1); r2[a] = np.inf
        S6 += float(np.sum(r2**-3))
    S6 /= Np
    var_pred = (2.0/3.0)*dp2*S6
    return dp2, S6, var_pred, var_meas

if __name__ == "__main__":
    print(f"OBL-FOLD-CHECK at d_s^emp = {DS_EMP} (declared bands: "
          f"PASS [{BAND_PASS[0]}, {BAND_PASS[1]}], MARGINAL to [{BAND_MARG[0]:.2f}, {BAND_MARG[1]:.1f}])")
    ratios = []
    for seed in (5, 11):
        dp2, S6, vp, vm = run_cell_probe(DS_EMP, 5, seed)
        ratio = vm/vp
        ratios.append(ratio)
        print(f"  seed {seed}: <d_p^2> = {dp2:7.2f}  S6_box = {S6:.3e}  "
              f"Var_pred = {vp:.4e}  Var_meas = {vm:.4e}  ratio = {ratio:.3f}")
    rmean = float(np.mean(ratios))
    print(f"\n  site-and-seed mean ratio = {rmean:.3f}")
    if BAND_PASS[0] <= rmean <= BAND_PASS[1]:
        print("  VERDICT: OBL-FOLD-CHECK — PASS-CONSISTENT (in the declared words).")
    elif BAND_MARG[0] <= rmean <= BAND_MARG[1]:
        print("  VERDICT: OBL-FOLD-CHECK — MARGINAL (in the declared words).")
    else:
        print("  VERDICT: OBL-FOLD-CHECK — FAIL-INCONSISTENT (in the declared words).")

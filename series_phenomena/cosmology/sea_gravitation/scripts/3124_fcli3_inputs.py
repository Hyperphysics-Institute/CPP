#!/usr/bin/env python
"""Patch 3124 -- F-CLI-3: input measurement at the frozen spacing + the
point confrontation (prereg 3123, committed before this file existed).
run_cell = the 3122 scheme-test's certified function (v2 dynamics,
lagged arc scheme = the campaign scheme), 3104 S3 read-outs."""
import sys, json, os
import numpy as np

def run_cell(ds, n_side, seed, T=3000, sig_n=0.30):
    rng = np.random.default_rng(seed)
    Np = n_side**3; Nc = 2*Np; L = n_side*ds
    grid = np.array([[i,j,kk] for i in range(n_side) for j in range(n_side)
                     for kk in range(n_side)], float)*ds + ds/2
    X = np.repeat(grid, 2, axis=0) + rng.normal(0, 0.3, (Nc,3))
    q = np.tile([1.0,-1.0], Np); qq = np.outer(q,q)
    partner = np.arange(Nc); partner[0::2]+=1; partner[1::2]-=1
    pair_q = (np.arange(Np)%2==1)
    Gcp = np.repeat(np.where(pair_q, 52.94, 1.0), 2)
    Hist = np.zeros((T,Nc,3)); Hist[0]=X
    Disp = np.zeros((Nc,3)); ptr = np.zeros(Nc,int)
    eye = np.eye(Nc, dtype=bool); opp = qq<0; idx = np.arange(Nc)
    dp_hist = np.zeros((T-1,Np))
    for t in range(1,T):
        D = X[:,None,:]-X[None,:,:]; D -= L*np.round(D/L)
        r = np.sqrt(np.einsum('ijk,ijk->ij',D,D)); np.fill_diagonal(r,1.0)
        co = r<1e-6; rs = np.where(co,1.0,r); re = np.maximum(rs,1.0)
        Fc = np.einsum('ij,ijk->ik', np.where(co,0.0,qq/(re**2*rs)), D)
        P = partner; qp = qq[idx,P]
        dvp = D[idx,P]; rrp = r[idx,P]; cop = co[idx,P]
        Fc -= np.where(cop,0.0,qp/(np.maximum(rrp,1.0)**2*rrp))[:,None]*dvp
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
            m_,kk_ = partner[i],partner[j]
            if done[m_] or done[kk_] or len({i,j,m_,kk_})<4: continue
            partner[i],partner[j]=j,i; partner[m_],partner[kk_]=kk_,m_
            done[[i,j,m_,kk_]]=True
        pi = np.arange(0,Nc,2); dp_hist[t-1]=r[pi,partner[pi]]
    th=(T-1)//3; W=dp_hist[2*th:]
    eq=~pair_q; qm=pair_q
    We,Wq=W[:,eq],W[:,qm]
    ge=We>ds/2.0; gq=Wq>ds/2.0
    be=We[We<=ds/2.0]; bq=Wq[Wq<=ds/2.0]
    # threshold-variant aggregates (OBL-INV-SENS): 0.75*ds gas threshold
    ge2=We>0.75*ds; gq2=Wq>0.75*ds
    be2=We[We<=0.75*ds]; bq2=Wq[Wq<=0.75*ds]
    return dict(r_e=float(ge.mean()),
                x_q=float(gq.sum()/max(ge.sum()+gq.sum(),1)),
                eta_gas=float((We**2)[ge].mean()/ds**2) if ge.any() else np.nan,
                eta_e=float((be**2).mean()/ds**2) if be.size else np.nan,
                s=float((bq**2).mean()/(be**2).mean()) if bq.size and be.size else np.nan,
                r_e75=float(ge2.mean()),
                x_q75=float(gq2.sum()/max(ge2.sum()+gq2.sum(),1)),
                eta_gas75=float((We**2)[ge2].mean()/ds**2) if ge2.any() else np.nan,
                eta_e75=float((be2**2).mean()/ds**2) if be2.size else np.nan,
                s75=float((bq2**2).mean()/(be2**2).mean()) if bq2.size and be2.size else np.nan)

ALPHA = 1/137.035999
C_COH = 68.4841       # (1+k)^2, D-CHAN-ADD derived
BAND = (0.6, 0.9)
DS_STAR, DS_ERR = 2.450, 0.091

def phi(re, xq, ee, eg, s, C=C_COH):
    rq = min(re*xq/(1.0-xq), 1.0)
    return ((1-re)*ee + re*eg + C*((1-rq)*(s*ee) + rq*eg))/4.0

def cli(P, a, d):
    return np.sqrt((4.0/3.0)*25.338*a*ALPHA*P)/d

if __name__ == "__main__":
    st = {}
    for ds in (2.359, 2.450, 2.541):
        for sd in (5, 11):
            z = run_cell(ds, 5, sd)
            st[f"{ds}:{sd}"] = z
            print(f"  ds={ds} seed={sd}: " + " ".join(f"{k}={v:.4f}" for k,v in z.items()))
    json.dump(st, open("/tmp/3124_inputs.json","w"))
    # central inputs: seed mean at 2.450
    cen = {k: float(np.mean([st[f"2.45:{s}"][k] if f"2.45:{s}" in st else st[f"2.450:{s}"][k] for s in (5,11)]))
           for k in ("r_e","x_q","eta_gas","eta_e","s")}
    print("\nCENTRAL INPUTS (d_s = 2.450, seed mean):",
          " ".join(f"{k}={v:.4f}" for k,v in cen.items()))
    P_c = phi(cen["r_e"], cen["x_q"], cen["eta_e"], cen["eta_gas"], cen["s"])
    c_central = cli(P_c, 1.0, DS_STAR)
    print(f"Phi = {P_c:.3f};  CENTRAL c_Li = {c_central:.4f};  BAND [{BAND[0]}, {BAND[1]}]")
    # residual band: all cells x seeds x arrangement x alpha_s x arc-scheme x ds
    import itertools
    lo, hi = 1e9, -1.0
    ARC = 0.034
    for key, z in st.items():
        for a_ in (0.78, 1.35):
            for das in (0.9, 1.0, 1.1):                     # alpha_s +/-10% -> k^2 scaling
                Cv = (1 + np.sqrt(das)* (C_COH**0.5 - 1))**2
                for d_ in (DS_STAR-DS_ERR, DS_STAR, DS_STAR+DS_ERR):
                    for sgn in (-1, 0, 1):                  # arc-scheme shift, worst-case coherent
                        zz = {k: z[k] + sgn*ARC*(1 if k in ("r_e","x_q") else (z[k]*0.02 if k=="eta_gas" else 0.01))
                              for k in z}
                        P = phi(zz["r_e"], min(zz["x_q"],0.95), zz["eta_e"], zz["eta_gas"], zz["s"], Cv)
                        c = cli(P, a_, d_)
                        lo, hi = min(lo,c), max(hi,c)
    print(f"RESIDUAL BAND: [{lo:.3f}, {hi:.3f}]")
    print("="*68)
    if BAND[0] <= c_central <= BAND[1]:
        print("VERDICT: the central point falls INSIDE the band.")
        print("F-CLI-3: PASS (bracketed by the residual band, reported above).")
    elif c_central < BAND[0]:
        print(f"VERDICT: central below the band (shortfall x{(BAND[0]/c_central)**2:.2f} in rho).")
        print("F-CLI-3: FIRES (shortfall), in those words.")
    else:
        print(f"VERDICT: central above the band (overshoot x{(c_central/BAND[1])**2:.2f} in rho).")
        print("F-CLI-3: FIRES (overshoot), in those words.")
    print("="*68)

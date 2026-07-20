#!/usr/bin/env python3
"""
PATCH 2629 -- SINK-OBS-1 EXECUTION under sink_obs1_derivation_prereg.md (2628)
S3 ONLY. n1_disc2 verbatim from the 2626 artifact (pinned lineage). Widths w=3
is DIAGNOSTIC-QUARANTINED per prereg: no DM consumer may cite it.
The strengthened sink-ON/OFF single-transit discriminator + FUNNEL-1.
Engine import: exec-load of the registered artifact code/2602_hgamma_gates_b1.py
through the 2609 cut -- n1_gamma, rung, strong_FU, constants are the registered
objects. n1_disc is the VERBATIM n1_gamma body with LOGGING LINES ONLY added
(marked "# INSTR"); the state-update path is untouched. Verdicts are read from
the prereg against raw outputs (2579); this script prints observables only.
Stages: controls | m1 | m23 | m4 | m5   (foreground-chunked per prereg S5).
"""
import numpy as np, time, os, sys
from scipy.optimize import minimize_scalar

HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "2602_hgamma_gates_b1.py")).read()
cut = src.index("t0=_t.time(); trunc_mode='DIST'")
ns = {}
exec(src[:cut], ns)
n1_gamma = ns['n1_gamma']; rung = ns['rung']
AHC = ns['AHC']; ALPHA_S = ns['ALPHA_S']; A_QQ = ns['A_QQ']; D = ns['D']
EQQ = ns['EQQ']; TAUC = ns['TAUC']; FLOOR = ns['FLOOR']
amat = ns['amat']; qw_of = ns['qw_of']; strong_FU = ns['strong_FU']
M = 132.0
H4, C4, S4 = rung(1)

# ---------------- instrumented engine (verbatim path + "# INSTR" lines) --------
def n1_disc2(H0, C, SP, dtf, betad, eta, coupling=1.0, TC=120, V0=None):
    NS=len(H0); A=amat(SP); qw=qw_of(SP,C); QW=np.outer(qw,qw); A2=A*A
    isE=np.array([s=='e' for s in SP]); m=np.where(isE,ns['KE'],ns['KQ'])
    dt=TAUC*dtf; nst=int(TC*TAUC/dt); spc=max(1,int(round(1.0/dtf)))
    H=np.array(H0,float).copy()
    P=np.zeros((NS,3))
    if V0 is not None:
        v0=np.array(V0,float); g0=1.0/np.sqrt(1-(v0*v0).sum(axis=1))
        P=(m*g0)[:,None]*v0
    Vacc=np.zeros((NS,3)); Sea=0.0; PSea=np.zeros(3); E0=None; Edrift=0.0
    Rr=[]; Dm=[]; gmax=1.0
    LOG=[]; dmin=np.inf; t_ca=0.0; Msum=m.sum()          # INSTR
    t_x=None; t_m=None; dprev1=None; dprev2=None         # INSTR
    def vel(P):
        return P/np.sqrt(m*m+(P*P).sum(axis=1))[:,None]
    def rke(P):
        return (np.sqrt(m*m+(P*P).sum(axis=1))-m).sum()
    for st in range(nst):
        ddh=H[:,None,:]-H[None,:,:]; r2h=(ddh*ddh).sum(axis=2); np.fill_diagonal(r2h,np.inf)
        Fe=(-((QW/(r2h+A2)**1.5))[:,:,None]*ddh*(-AHC)).sum(axis=1)
        Fs,Us=strong_FU(H,SP,betad)
        Ue=(np.triu(QW/np.sqrt(r2h+A2),1)).sum()*AHC
        if coupling>0: P=P+(Fe+Fs)*dt
        V=vel(P); gmax=max(gmax,1.0/np.sqrt(1-min((V*V).sum(axis=1).max(),0.999999)))
        Vacc+=V
        if NS>=5:                                          # INSTR
            cen4=H[:4].mean(axis=0)                        # INSTR
            di=np.linalg.norm(H[NS-1]-cen4)                # INSTR
            if di<dmin: dmin=di; t_ca=(st+1)*dt            # INSTR
            if t_x is None and di<2*D: t_x=(st+1)*dt       # INSTR
            if t_m is None and dprev2 is not None and \
               dprev1<dprev2 and dprev1<di: t_m=st*dt      # INSTR
            dprev2=dprev1; dprev1=di                       # INSTR
        if (st+1)%spc==0 and coupling>0:
            Vbar=Vacc/spc; Vosc=V-Vbar
            KEpre=rke(P); Ppre=P.sum(axis=0)
            gb=1.0/np.sqrt(1-np.minimum((Vbar*Vbar).sum(axis=1),0.999999))   # INSTR
            ktA=((m*gb)-m).sum()                                             # INSTR
            ktB=np.sqrt(Msum*Msum+(Ppre*Ppre).sum())-Msum                    # INSTR
            Vn=Vbar+np.sqrt(1-eta)*Vosc if eta<1.0 else Vbar.copy()
            g=1.0/np.sqrt(1-np.minimum((Vn*Vn).sum(axis=1),0.999999))
            P=(m*g)[:,None]*Vn
            Sea+=KEpre-rke(P); PSea=PSea+(Ppre-P.sum(axis=0)); Vacc[:]=0.0
            KEpost=rke(P); Pt2=P.sum(axis=0)                                 # INSTR
            ktB2=np.sqrt(Msum*Msum+(Pt2*Pt2).sum())-Msum                     # INSTR
            LOG.append(((st+1)*dt, KEpre, ktA, KEpre-ktA, ktB,               # INSTR
                        KEpre-ktB, KEpost-ktB2, KEpre-KEpost))               # INSTR
        H=H+vel(P)*dt
        Etot=rke(P)+Us+Ue+Sea
        if E0 is None: E0=Etot
        Edrift=max(Edrift,abs(Etot-E0))
        cen=H.mean(axis=0); dc=np.linalg.norm(H-cen,axis=1)
        Rr.append(np.sqrt((dc*dc).mean())); Dm.append(dc.max())
    Rr=np.array(Rr); Dm=np.array(Dm); n=len(Rr); wsl=slice(int(0.75*n),n)
    return {'R0':Rr[0],'Dmax0':Dm[0],'Rw':Rr[wsl].mean(),'Dmaxw':Dm[wsl].max(),
            'hb_ok':True,'Edrift':Edrift,'Sea':Sea,'PSea':PSea,'gmax':gmax,
            'H':H,'V':vel(P),'m':m,'Rend':Rr[-1],
            'LOG':LOG,'t_ca':t_ca,'dmin':dmin,'t_x':t_x,'t_m':t_m}           # INSTR

# ---------------- shared helpers (B1 verbatim geometry / classifier) ----------
def launch(b, v):
    H0=np.vstack([H4,[b*D,0.0,4*D]]); C0=np.append(C4,-1.0); S0=S4+['q']
    V0=np.zeros((5,3)); V0[4]=[0,0,-v]
    return H0,C0,S0,V0

def classify(res):
    Hf=res['H']; Vf=res['V']; cen4=Hf[:4].mean(axis=0)
    d_inc=np.linalg.norm(Hf[4]-cen4)
    vr=np.dot(Vf[4]-Vf[:4].mean(axis=0),(Hf[4]-cen4)/max(d_inc,1e-9))
    d4=np.linalg.norm(Hf[:4]-cen4,axis=1); sq_ok=(d4.max()<3*D)
    if d_inc<3*D and sq_ok and res['Sea']>0: return 'CAP'
    if d_inc>4*D and vr>0 and sq_ok: return 'SCA'
    if not sq_ok: return 'FRG'
    return 'UNR'

def reads2(res):
    """S_WA, S_WB, D^B(W-A), S_cum, |dcen|; NO-CONTACT flag if t_x is None."""
    scum=res['Sea']; dcen=np.linalg.norm(res['H'][:4].mean(axis=0))
    if res['t_x'] is None:
        return None, None, None, scum, dcen
    twA=res['t_x']+2*TAUC
    sWA=sum(e[7] for e in res['LOG'] if e[0]<=twA)
    dB=sum(e[5]-e[6] for e in res['LOG'] if e[0]<=twA)
    if res['t_m'] is not None:
        twB=res['t_m']+2*TAUC
        sWB=sum(e[7] for e in res['LOG'] if e[0]<=twB)
    else:
        sWB=None
    return sWA, sWB, dB, scum, dcen

def cell(b,v,w,eta,dtf,disc=True,TC=120):
    H0,C0,S0,V0=launch(b,v)
    fn=n1_disc2 if disc else n1_gamma
    return fn(H0,C0,S0,dtf,w,eta,TC=TC,V0=V0)

stage=sys.argv[1] if len(sys.argv)>1 else 'p1'
t0=time.time()
print("="*78); print(f"PATCH 2629 -- SINK-OBS-1 (prereg 2628 S3; verdicts read there)  stage={stage}")
print("="*78)

def swa_of(v,w,dtf):
    r=cell(0.0,v,w,0.5,dtf)
    sWA,sWB,dB,sc,dc=reads2(r)
    return sWA,sc,r['Edrift'],classify(r)

if stage=='p1':
    print("[P1] stiffness monotonicity: single-pass final-inc vs width, v=0.10")
    FI={}
    for w in (2.0,3.0,4.0):
        S={}
        for dtf in (1/100,1/200,1/400):
            S[dtf],sc,ed,cl=swa_of(0.10,w,dtf)
            print(f"  w={w} dt=1/{int(1/dtf)}: S_WA={S[dtf]:.2f} (S_cum={sc:.1f}, Edrift={ed:.1f}, {cl})")
        fi=abs(S[1/400]-S[1/200])/max(S[1/400],1e-9)
        FI[w]=fi
        print(f"  w={w}: final-inc={fi:.4f}")
    mono=FI[2.0]<FI[3.0]<FI[4.0]
    print(f"  [P1 verdict-input] final-inc(2,3,4) = {FI[2.0]:.4f}, {FI[3.0]:.4f}, {FI[4.0]:.4f} "
          f"MONOTONE-INCREASING: {mono}")
    print(f"[{time.time()-t0:.0f}s]")

elif stage=='p2':
    print("[P2] endpoint order: S_cum at dt 1/200,1/400,1/800, both anchors, w=4")
    for v in (0.10,0.95):
        S={}; E={}
        for dtf in (1/200,1/400,1/800):
            sWA,sc,ed,cl=swa_of(v,4.0,dtf)
            S[dtf]=sc; E[dtf]=ed
            print(f"  v={v} dt=1/{int(1/dtf)}: S_cum={sc:.2f} Edrift={ed:.2f} ({cl})")
        d1=abs(S[1/800]-S[1/400]); d2=abs(S[1/400]-S[1/200])
        fin=d1/max(S[1/800],1e-9); bound=E[1/800]/max(S[1/800],1e-9)+0.01
        print(f"  v={v}: increments {d2:.2f} -> {d1:.2f} FALLING={d1<=d2}; "
              f"final-inc={fin:.4f} <= Edrift/S+1%={bound:.4f}: {fin<=bound}")
    print(f"[{time.time()-t0:.0f}s]")

elif stage=='p3':
    print("[P3] gentleness leg: w=4 single-pass final-inc, v=0.05 vs v=0.10")
    FI={}
    for v in (0.05,0.10):
        S={}
        for dtf in (1/100,1/200,1/400):
            S[dtf],sc,ed,cl=swa_of(v,4.0,dtf)
            print(f"  v={v} dt=1/{int(1/dtf)}: S_WA={S[dtf]:.2f} ({cl})")
        FI[v]=abs(S[1/400]-S[1/200])/max(S[1/400],1e-9)
        print(f"  v={v}: final-inc={FI[v]:.4f}")
    print(f"  [P3 verdict-input] final-inc(0.05)={FI[0.05]:.4f} < final-inc(0.10)={FI[0.10]:.4f}: "
          f"{FI[0.05]<FI[0.10]}")
    print(f"[{time.time()-t0:.0f}s]")

print("\nDone. Verdicts are read in sink_obs1_record.md against prereg S3.")

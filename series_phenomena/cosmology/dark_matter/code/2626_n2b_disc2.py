#!/usr/bin/env python3
"""
PATCH 2626 -- N2B-DISC-2 EXECUTION under n2b_disc2_prereg.md (2625) ONLY.
n1_disc2 = the 2624 n1_disc body + two tracked times (t_x first-crossing of
R_in=2D; t_m first local minimum of d_inc), LOGGING ONLY; state path verbatim.
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

stage=sys.argv[1] if len(sys.argv)>1 else 'controls'
t0=time.time()
print("="*78); print(f"PATCH 2626 -- N2B-DISC-2 (prereg 2625; verdicts read there)  stage={stage}")
print("="*78)

if stage=='controls':
    ra=cell(0.0,0.40,4.0,0.5,1/100,disc=False)
    rb=cell(0.0,0.40,4.0,0.5,1/100,disc=True)
    print(f"[C1] registered: {classify(ra)} Sea={ra['Sea']:.6f} gmax={ra['gmax']:.6f}")
    print(f"[C1] n1_disc2  : {classify(rb)} Sea={rb['Sea']:.6f} gmax={rb['gmax']:.6f}")
    print(f"[C1] match: cls={classify(ra)==classify(rb)} "
          f"dSea={abs(ra['Sea']-rb['Sea']):.2e} dg={abs(ra['gmax']-rb['gmax']):.2e}")
    r0=cell(0.0,0.10,4.0,0.0,1/200)
    print(f"[C2a] eta=0 v=0.10 dt=1/200: Sea={r0['Sea']:.3e} (|Sea|<1e-6: {abs(r0['Sea'])<1e-6})")
    Ed={}
    for dtf in (1/100,1/200,1/400):
        Ed[dtf]=cell(0.0,0.10,4.0,0.0,dtf)['Edrift']
    q1=Ed[1/100]/Ed[1/200]; q2=Ed[1/200]/Ed[1/400]
    print(f"[C2b] Edrift(eta=0) = {Ed[1/100]:.3f},{Ed[1/200]:.3f},{Ed[1/400]:.3f} "
          f"ratios {q1:.2f},{q2:.2f} (both>=1.5: {q1>=1.5 and q2>=1.5})")
    ri=n1_disc2(H4,C4,S4,1/100,4.0,0.5,TC=60)
    ktAmax=max(e[2] for e in ri['LOG']); ktBmax=max(e[4] for e in ri['LOG'])
    print(f"[C3] isolated square: max ktA={ktAmax:.4f} max ktB={ktBmax:.4f} "
          f"(both <1: {ktAmax<1 and ktBmax<1})")
    rs=cell(0.0,0.95,4.0,0.0,1/200)
    sWA,sWB,dB,sc,dc=reads2(rs)
    print(f"[C4] eta=0 v=0.95 (SCA cell): t_x={'%.2f'%rs['t_x'] if rs['t_x'] else 'NONE'} "
          f"S_WA={sWA:.3e} (machine-zero: {abs(sWA)<1e-6 if sWA is not None else False})")
    ra2=cell(0.0,0.10,4.0,0.5,1/200)
    print(f"[C4] ON low-gamma anchor: t_x={ra2['t_x']:.2f} t_m={ra2['t_m']:.2f} "
          f"(t_x<=t_m: {ra2['t_x']<=ra2['t_m']})")
    print(f"[{time.time()-t0:.0f}s]")

elif stage=='m1':
    print("[M1] gates at the anchors  eta=0.5  b=0 w=4")
    R={}
    for v in (0.10,0.95):
        for dtf in (1/100,1/200,1/400):
            r=cell(0.0,v,4.0,0.5,dtf)
            sWA,sWB,dB,sc,dc=reads2(r)
            R[(v,dtf)]=(sWA,sWB,dB,sc,r['Edrift'])
            exp='BASELINE-EXPOSED' if sWA<3*r['Edrift'] else 'clear'
            wb=f"{sWB:.2f}" if sWB is not None else "NONE"
            print(f"  v={v} dt=1/{int(1/dtf)}: S_WA={sWA:.2f} S_WB={wb} D^B={dB:.2f} "
                  f"S_cum={sc:.1f} Edrift={r['Edrift']:.1f} [{exp}] "
                  f"t_x={r['t_x']:.2f} t_m={r['t_m']:.2f} cls={classify(r)}")
        a=R[(v,1/100)][0]; b_=R[(v,1/200)][0]; c=R[(v,1/400)][0]
        d1=abs(c-b_); d2=abs(b_-a); fin=d1/max(c,1e-9)
        print(f"  [G1] v={v}: |400-200|={d1:.2f} |200-100|={d2:.2f} shrinking={d1<=d2} "
              f"final-inc={fin:.3f} (<=0.05: {fin<=0.05})")
        for dtf in (1/200,1/400):
            sWA,sWB,dB,_,_=R[(v,dtf)]
            g2=abs(dB-sWA)/max(sWA,1e-9); g3=abs(sWB-sWA)/max(sWA,1e-9)
            print(f"  [G2] v={v} dt=1/{int(1/dtf)}: |DB-SWA|/SWA={g2:.3f} (<=0.10: {g2<=0.10})")
            print(f"  [G3] v={v} dt=1/{int(1/dtf)}: |SWB-SWA|/SWA={g3:.3f} (<=0.10: {g3<=0.10})")
        b200=abs(R[(v,1/200)][2]-R[(v,1/200)][0])/max(R[(v,1/200)][0],1e-9)
        b400=abs(R[(v,1/400)][2]-R[(v,1/400)][0])/max(R[(v,1/400)][0],1e-9)
        print(f"  [G2-band] v={v}: beta(1/200)={b200:.3f} beta(1/400)={b400:.3f} "
              f"|dbeta|={abs(b200-b400):.3f} (band-STABLE <=0.05: {abs(b200-b400)<=0.05})")
        sc=[R[(v,d)][3] for d in (1/100,1/200,1/400)]
        d1=abs(sc[2]-sc[1]); d2=abs(sc[1]-sc[0]); fin=d1/max(sc[2],1e-9)
        print(f"  [G4] v={v}: S_cum {sc[0]:.1f},{sc[1]:.1f},{sc[2]:.1f} shrinking={d1<=d2} "
              f"final-inc={fin:.3f} (<=0.05: {fin<=0.05})")
    import json
    open('/tmp/disc2_R.json','w').write(json.dumps({f"{k[0]}_{k[1]}":vv for k,vv in R.items()}))
    print(f"[{time.time()-t0:.0f}s]")

elif stage=='m23':
    print("[M2] physical span v-grid at dt=1/200 (b=0 w=4) + [G5]")
    import json
    R={}
    try:
        raw=json.loads(open('/tmp/disc2_R.json').read())
        for k,vv in raw.items():
            v,dtf=k.split('_'); R[(float(v),float(dtf))]=vv
    except Exception:
        R=None
    phys={}
    for v in (0.10,0.40,0.95):
        r=cell(0.0,v,4.0,0.5,1/200)
        sWA,sWB,dB,sc,dc=reads2(r)
        phys[v]=sWA
        print(f"  v={v}: S_WA={sWA:.2f} S_WB={sWB:.2f} D^B={dB:.2f} Edrift={r['Edrift']:.1f}")
    ps=max(phys.values())-min(phys.values())
    if R:
        for v in (0.10,0.95):
            # impl members: S_WA across dt; S_WB at 1/200,1/400; D^B included unless band applies
            swa=[R[(v,d)][0] for d in (0.01,0.005,0.0025)]
            swb=[R[(v,d)][1] for d in (0.005,0.0025) if R[(v,d)][1] is not None]
            db=[R[(v,d)][2] for d in (0.005,0.0025)]
            g2fail=any(abs(R[(v,d)][2]-R[(v,d)][0])/max(R[(v,d)][0],1e-9)>0.10 for d in (0.005,0.0025))
            mem=swa+swb+([] if g2fail else db)
            isr=max(mem)-min(mem)
            note=" (method-B EXCLUDED per band clause)" if g2fail else ""
            print(f"  [G5] anchor v={v}: impl spread={isr:.2f} phys spread={ps:.2f} "
                  f"ratio={isr/max(ps,1e-9):.3f} (<=0.20: {isr/max(ps,1e-9)<=0.20}){note}")
    print("\n[M3] width confirmation w=2, low-gamma anchor (sentence-gating only)")
    W={}
    for dtf in (1/100,1/200):
        r=cell(0.0,0.10,2.0,0.5,dtf)
        sWA,sWB,dB,sc,dc=reads2(r)
        W[dtf]=(sWA,sWB)
        print(f"  dt=1/{int(1/dtf)}: S_WA={sWA:.2f} S_WB={sWB:.2f} S_cum={sc:.1f}")
    g3=abs(W[1/200][1]-W[1/200][0])/max(W[1/200][0],1e-9)
    print(f"  window agreement at 1/200: {g3:.3f} (<=0.10: {g3<=0.10}); "
          f"dS_WA(100->200)={abs(W[1/200][0]-W[1/100][0]):.2f}")
    print(f"[{time.time()-t0:.0f}s]")

print("\nDone. Verdicts are read in n2b_disc2_record.md against the prereg.")

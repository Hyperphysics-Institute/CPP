#!/usr/bin/env python3
"""
PATCH 2621 -- N2B-DISC-1 EXECUTION under n2b_disc1_prereg.md (2620) ONLY.
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
def n1_disc(H0, C, SP, dtf, betad, eta, coupling=1.0, TC=120, V0=None):
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
            'LOG':LOG,'t_ca':t_ca,'dmin':dmin}                               # INSTR

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

def reads(res):
    """S_1pass, S_cum, D^B over the 1-pass window, f_1pass, |dcen|."""
    tw=res['t_ca']+2*TAUC
    s1=sum(e[7] for e in res['LOG'] if e[0]<=tw)
    dB=sum(e[5]-e[6] for e in res['LOG'] if e[0]<=tw)
    scum=res['Sea']; f=s1/scum if scum>0 else 0.0
    dcen=np.linalg.norm(res['H'][:4].mean(axis=0))
    return s1,scum,dB,f,dcen

def cell(b,v,w,eta,dtf,disc=True,TC=120):
    H0,C0,S0,V0=launch(b,v)
    fn=n1_disc if disc else n1_gamma
    return fn(H0,C0,S0,dtf,w,eta,TC=TC,V0=V0)

stage=sys.argv[1] if len(sys.argv)>1 else 'controls'
t0=time.time()
print("="*78); print(f"PATCH 2621 -- N2B-DISC-1 (prereg 2620; verdicts read there)  stage={stage}")
print("="*78)

if stage=='controls':
    # C1 convention-pin (METH-L2-015): reproduce the registered 2609 timing cell
    ra=cell(0.0,0.40,4.0,0.5,1/100,disc=False)
    rb=cell(0.0,0.40,4.0,0.5,1/100,disc=True)
    print(f"[C1] registered: {classify(ra)} Sea={ra['Sea']:.6f} gmax={ra['gmax']:.6f}")
    print(f"[C1] n1_disc   : {classify(rb)} Sea={rb['Sea']:.6f} gmax={rb['gmax']:.6f}")
    print(f"[C1] match: cls={classify(ra)==classify(rb)} "
          f"dSea={abs(ra['Sea']-rb['Sea']):.2e} dg={abs(ra['gmax']-rb['gmax']):.2e}")
    # C2 sink-OFF null
    r0=cell(0.0,0.10,4.0,0.0,1/200)
    print(f"[C2] eta=0 v=0.10 dt=1/200: Sea={r0['Sea']:.3e} (|Sea|<1e-6: {abs(r0['Sea'])<1e-6}) "
          f"Edrift={r0['Edrift']:.3f} (<FLOOR {FLOOR}: {r0['Edrift']<FLOOR})")
    r9=cell(0.0,0.95,4.0,0.0,1/200)
    print(f"[C2r] eta=0 v=0.95 dt=1/200 (reported): Sea={r9['Sea']:.3e} Edrift={r9['Edrift']:.3f} "
          f"cls={classify(r9)}")
    # C3 decomposition sanity: isolated settled square
    ri=n1_disc(H4,C4,S4,1/100,4.0,0.5,TC=60)
    ktAmax=max(e[2] for e in ri['LOG']); ktBmax=max(e[4] for e in ri['LOG'])
    print(f"[C3] isolated square: max ktA={ktAmax:.4f} max ktB={ktBmax:.4f} MeV "
          f"(both <1: {ktAmax<1 and ktBmax<1})")
    print(f"[{time.time()-t0:.0f}s]")

elif stage=='m1':
    print("[M1] component tracking  eta=0.5 dt=1/100  (S1p, Scum, D^B, f_1pass, |dcen|)")
    for w in (2.0,4.0):
        for b in (0.0,1.0):
            row=[]
            for v in (0.10,0.40,0.95):
                r=cell(b,v,w,0.5,1/100)
                s1,sc,dB,f,dc=reads(r)
                row.append(f"v={v}:{classify(r)} S1p={s1:.1f} Sc={sc:.1f} "
                           f"DB={dB:.1f} f={f:.2f} dcen={dc:.2f}")
            print(f"  w={w} b={b}D: "+" | ".join(row))
    print(f"[{time.time()-t0:.0f}s]")

elif stage=='m23':
    print("[M2] dt-convergence x partition-independence on S_1pass; anchors b=0 w=4")
    A={}
    for v in (0.10,0.95):
        for dtf in (1/50,1/100,1/200,1/400):
            r=cell(0.0,v,4.0,0.5,dtf)
            s1,sc,dB,f,dc=reads(r)
            A[(v,dtf)]=(s1,dB)
            print(f"  v={v} dt=1/{int(1/dtf)}: S1p={s1:.2f} D^B={dB:.2f} "
                  f"|DB-S1p|/S1p={abs(dB-s1)/max(s1,1e-9):.3f} Scum={sc:.1f} cls={classify(r)}")
        d1=abs(A[(v,1/400)][0]-A[(v,1/200)][0]); d2=abs(A[(v,1/200)][0]-A[(v,1/100)][0])
        fin=d1/max(A[(v,1/400)][0],1e-9)
        print(f"  v={v}: increments |400-200|={d1:.2f} |200-100|={d2:.2f} "
              f"shrinking={d1<=d2}  final-inc={fin:.3f} (<=0.05: {fin<=0.05})")
        for dtf in (1/200,1/400):
            s1,dB=A[(v,dtf)]; ag=abs(dB-s1)/max(s1,1e-9)
            print(f"  v={v} dt=1/{int(1/dtf)}: method agreement {ag:.3f} (<=0.10: {ag<=0.10})")
    print("\n[M3] physical vs implementation spread (S_1pass)")
    phys=[]
    for v in (0.10,0.40,0.95):
        r=cell(0.0,v,4.0,0.5,1/200); s1,_,_,_,_=reads(r); phys.append(s1)
        print(f"  physical grid v={v} dt=1/200: S1p={s1:.2f}")
    ps=max(phys)-min(phys)
    for v in (0.10,0.95):
        vals=[A[(v,d)][0] for d in (1/100,1/200,1/400)]+[A[(v,1/200)][1],A[(v,1/400)][1]]
        isr=max(vals)-min(vals)
        print(f"  anchor v={v}: impl spread={isr:.2f}  phys spread={ps:.2f}  "
              f"ratio={isr/max(ps,1e-9):.3f} (<=0.20: {isr/max(ps,1e-9)<=0.20})")
    print(f"[{time.time()-t0:.0f}s]")

elif stage=='m4':
    print("[M4] split-ON/OFF trajectory comparison (identical launches)")
    cells=[(0.10,0.0,4.0),(0.10,1.0,4.0),(0.95,0.0,4.0),(0.95,1.0,4.0),(0.10,0.0,2.0)]
    for (v,b,w) in cells:
        pair={}
        for eta in (0.5,0.0):
            r=cell(b,v,w,eta,1/100)
            s1=reads(r)[0] if eta>0 else 0.0
            dinc=np.linalg.norm(r['H'][4]-r['H'][:4].mean(axis=0))
            pair[eta]=(classify(r),dinc,s1,r)
        c5,d5,s5,_=pair[0.5]; c0,d0,_,_=pair[0.0]
        line=(f"  v={v} b={b}D w={w}: ON={c5}(d={d5:.2f},S1p={s5:.1f})  "
              f"OFF={c0}(d={d0:.2f})")
        if c5!=c0 or True:
            r5=cell(b,v,w,0.5,1/200); r0=cell(b,v,w,0.0,1/200)
            line+=f"  dt=1/200: ON={classify(r5)} OFF={classify(r0)}"
        print(line)
    print(f"[{time.time()-t0:.0f}s]")

elif stage=='m5':
    print("[M5-i] analytic well W(b), registered forms verbatim (well ONLY)")
    def U_inc(z,b,w):
        pos=np.array([b*D,0.0,z]); Utot=0.0; beta=w/D
        for k in range(4):
            r=max(np.linalg.norm(pos-H4[k]),1e-9)
            e=np.exp(-beta*(r-D))
            Utot+=EQQ*((1-e)**2-1)
            Utot+=(-1.0)*C4[k]*ALPHA_S*AHC/np.sqrt(r*r+A_QQ*A_QQ)
        return Utot
    def W_of(b,w):
        res=minimize_scalar(lambda z: U_inc(z,b,w),bounds=(-2.0,4*D),
                            method='bounded',options={'xatol':1e-8})
        return max(-res.fun,0.0)
    KEinc=M*(1.0/np.sqrt(1-0.10**2)-1.0)
    print(f"  KE_inc(0.10c) = {KEinc:.4f} MeV")
    for w in (2.0,4.0):
        Ws=[(b,W_of(b,w)) for b in np.arange(0.0,10.01,0.5)]
        bW=max([b for b,W in Ws if W>=KEinc],default=-1.0)
        samp=", ".join(f"b={b:.0f}:W={W:.2f}" for b,W in Ws if b in (0.0,1.0,2.0,3.0,5.0,7.0,10.0))
        print(f"  w={w}: {samp}  ->  b_W = {bW:.1f}D")
    print("\n[M5-ii] numeric funnel scan v=0.10c dt=1/100 (dt-union 1/200 on brackets)")
    for w in (2.0,4.0):
        for eta in (0.5,0.0):
            cls={}
            row=[]
            for b in (1,2,3,4,5,6,7,8):
                r=cell(float(b),0.10,w,eta,1/100)
                cls[b]=classify(r)
                dc=np.linalg.norm(r['H'][:4].mean(axis=0))
                row.append(f"b={b}:{cls[b]}(dcen={dc:.2f})")
            caps=[b for b in cls if cls[b]=='CAP']
            print(f"  w={w} eta={eta}: "+" ".join(row))
            if caps:
                bc=max(caps); bn=min([b for b in cls if b>bc and cls[b]!='CAP'] or [None]) \
                    if any(b>bc and cls[b]!='CAP' for b in cls) else None
                c1=classify(cell(float(bc),0.10,w,eta,1/200))
                msg=f"    bracket: last-CAP b={bc} (dt=1/200: {c1})"
                if bn is not None:
                    c2=classify(cell(float(bn),0.10,w,eta,1/200))
                    msg+=f", first-non-CAP b={bn} (dt=1/200: {c2})"
                else:
                    msg+=", no non-CAP above on grid (reach >= 8D)"
                print(msg)
            else:
                print(f"    NO CAP on offset grid")
    print(f"[{time.time()-t0:.0f}s]")

print("\nDone. Verdicts are read in n2b_disc1_record.md against the prereg.")

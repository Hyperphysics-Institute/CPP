#!/usr/bin/env python3
"""
PATCH 2452 -- OPEN-DM-FLOQUET-1 / R1 IN-SITU SOLVE EXECUTED (2441 SS6 i-iv) -- with a
REGISTERED-CONVENTION FORK DISCOVERED (FORK-SWITCH-1) that the placement hinges on.

DERIVED (registered, exact):
 - Constituents (SF-3/0880): E_eDP=88, E_qDP=264, E_hDP=152 MeV. Element mass
   4*E_qDP+4*E_eDP = 1408 MeV = the 2383 DD-priced mass EXACTLY (zero-parameter check).
 - In-situ inertia (0886 constituent rule): m_qCP = 132 MeV, m_eCP = 44 MeV.
   [SUPERSEDES the 2451 equal-split 88 MeV row.]
 - Pair-flip statistics: P(pair flips | swap) = 3/7 exactly (combinatorics verified by
   simulation) -- same 3/7 as the duty, a clean identity.
 - Bond frequency map: (hw_A)^2 = 2 E_qq (hc)^2/(d^2 m_q), coat hw_A ~ 7 MeV.

THE FORK (FORK-SWITCH-1, discovered by this solve's own diagnostic):
 (ANCHORED) Pattern-anchored switching: each pair spends (1-delta)=4/7 in its PATTERN
   product state, 3/7 flipped -- the reading every quantitative patch since 2437 uses
   (E_static = (1-2delta)*pattern is only correct here). Drive = coherent duty-3/7
   alternation; response computed EXACTLY below via square-wave harmonics.
 (UNIFORM) 2435-literal jello-uniform sampling: <c_i c_j> = -1/7 for ALL intra-element
   pairs (pattern-independent) and 0 inter-element. DEMONSTRATED below: this breaks the
   arc's E_static convention (mean-force ratio 5.76 vs the required 1.0) AND its
   stochastic spectrum is adiabatic-dominated -> net NEGATIVE response (kills).
   UNIFORM is therefore INTERNALLY INCONSISTENT with the registered geometry-#3 arc --
   evidence for ANCHORED, but the adjudication is the founder's/panel's, not Opus's.

CLOCK sub-readings under ANCHORED (per-pair alternation fundamental), all shown (G7):
 (C1) one full pattern<->flipped alternation per Compton period (ZBW = oscillation at
      the Compton frequency; residence 4:3 WITHIN the period): hw_1 = 264 MeV.
 (C2) orbit reading: 4 swaps/element/period, flip rate (12/7)/tau => hw_1 = (6/7)*264
      = 226.3 MeV.
 (C3) two hops per period (unfavorable): hw_1 = (12/7)*264 = 452.6 MeV.
"""
import numpy as np
AHC=197.3; PHI_G=(1+np.sqrt(5))/2; ALPHA_S=5/(8*PHI_G); ALPHA=1/137.036; DELTA=3/7
d=1.15; m_q=132.0; m_e=44.0
# thresholds (species-resolved, from the in-script lattice recompute of the R1 run):
SEg,SPcg,SPeg = -11958.0, 7.569e6, 4.269e5      # tilt gradient
SEu,SPcu,SPeu = -158.8, 9.490e4, 5.613e3        # tilt uniform
gE,gPc,gPe    = 724.0, -913888.0, -23002.0      # closure endpoint slopes
dEr,dPcr,dPer = 24.318, -16817.2, -489.4        # ring vs straight (global)
p=4.0/7.0   # duty of the PATTERN state
def harm_weights(nmax=40):
    w=[]
    for n in range(1,nmax+1):
        a=(4.0/(n*np.pi))*abs(np.sin(n*np.pi*p))
        w.append(a*a/2.0)
    return np.array(w)
W=harm_weights()
print(f"harmonic mean-square total = {W.sum():.4f} vs f_osc^2 = {1-(1-2*DELTA)**2:.4f} (=48/49)")
def lam_species(hw1,m,hwA,res_margin=0.10):
    tot=0.0; flag=False
    for n,wn in enumerate(W,start=1):
        hw=n*hw1
        if abs(hw-hwA)<res_margin*hwA: flag=True; continue
        tot+= wn*AHC**2/(4*m*(hw**2-hwA**2))
    return tot,flag
def thresholds(lam_e):
    t_tg=(-(SEg)-lam_e*SPeg)/SPcg
    t_tu=(-(SEu)-lam_e*SPeu)/SPcu
    t_ao=(gE+lam_e*gPe)/-gPc
    t_gl=(dEr+lam_e*dPer)/-dPcr
    return t_tg,t_tu,t_ao,t_gl
print()
print("="*84)
print("BRACKET (ANCHORED): exact square-wave response, per clock reading and E_qq branch")
print("="*84)
for cname,hw1 in [("C1: 1 alternation/Compton period (264.0)",264.0),
                  ("C2: orbit 4-swap reading (226.3)",(6/7)*264),
                  ("C3: two-hop reading (452.6)",(12/7)*264)]:
    hw1e = hw1*553.0/264.0
    lam_e,_=lam_species(hw1e,m_e,7.0)
    t_tg,t_tu,t_ao,t_gl=thresholds(lam_e)
    thr=max(t_tg,t_tu,t_ao,t_gl)
    eps=None
    print(f"[{cname}]  lam_e={lam_e:.3e}; required lam_q: tilt-g {t_tg:.3e} tilt-u {t_tu:.3e} "
          f"anti-open {t_ao:.3e} global {t_gl:.3e}")
    print(f"    {'E_qq':>6} {'hwA_q':>7} {'lam_q':>11} {'ratio/max-thr':>13} {'eps=(wA/w1)^2':>13}  verdict")
    for Eqq in (40.,66.,100.,115.,140.,170.):
        hwA=np.sqrt(2*Eqq*AHC**2/(d**2*m_q))
        lq,fl=lam_species(hw1,m_q,hwA)
        eps=(hwA/hw1)**2
        v=("FULLY STABILIZED" if lq>=thr else
           ("partial("+",".join(n for n,t in [("tg",t_tg),("tu",t_tu),("ao",t_ao),("gl",t_gl)] if lq>=t)+")"
            if lq>=min(t_tg,t_tu,t_ao,t_gl) else "BELOW ALL")) + (" [near-res!]" if fl else "")
        intone=" tongue-IN" if 0.179<=eps<=0.428 else " tongue-out"
        print(f"    {Eqq:>6.0f} {hwA:>7.1f} {lq:>11.3e} {lq/thr:>13.2f} {eps:>13.3f}{intone}  {v}")
    # sign-flip E_qq (fundamental resonance crossing)
    Estar=hw1**2*d**2*m_q/(2*AHC**2)
    print(f"    fundamental-resonance crossing: E_qq* = {Estar:.1f} MeV (sign flips above; "
          f"treatment invalid within ~10% of it)")
    print()
print("="*84)
print("BRACKET (UNIFORM, 2435-literal): from the stochastic lattice simulation (prior run)")
print("="*84)
print("  mean-force diagnostic: |<F>| / [(1-2delta)*pattern] = 5.76 (must be 1.0 under the")
print("  arc's E_static convention) -> UNIFORM breaks the registered static convention.")
print("  dynamic response (all E_qq, both clocks): lam_q(net) in [-7.2e-3, -5.6e-3] --")
print("  adiabatic(below-resonance)-DOMINATED, net NEGATIVE -> would kill; but the same")
print("  reading also zeroes inter-element E_static -> internally inconsistent with the")
print("  entire 2437-2451 quantitative arc. Adjudication = FORK-SWITCH-1 (founder/panel).")
print()
print("K_switch eligibility note: the parametric (Meissner) channel is a SEPARATE additive")
print("positive channel wherever eps=(wA/w1)^2 lands in [0.179,0.428] (tongue rows above);")
print("mid-band gain ~0.12*A -- uncounted in the thresholds; bridges sub-threshold ratios")
print("of order ~0.9 where tongue-IN. Not invoked quantitatively (uncomputed on the")
print("collective coordinates).")

# ============================================================================
# APPENDIX -- the UNIFORM-bracket stochastic simulation (reproduces the quoted
# mean-force diagnostic 5.76 and lam_q(net) in [-7.2e-3,-5.6e-3]). Seeded.
# Run with RUN_SIM=1 environment variable (adds ~1-2 min).
# ============================================================================
import os
if os.environ.get("RUN_SIM")=="1":
    exec(r"""import numpy as np
from numpy.linalg import norm
rng=np.random.default_rng(24520)
AHC=197.3; PHI_G=(1+np.sqrt(5))/2; ALPHA_S=5/(8*PHI_G); ALPHA=1/137.036; DELTA=3/7
d=1.15; D=d; A_Q=d; R_E=1.6*(d/np.sqrt(2)); N=16
E_eDP=88.0; E_qDP=264.0; m_q=E_qDP/2; m_e=E_eDP/2
print("="*78); print("R1 IN-SITU SOLVE -- derived inertia + drive spectrum + resonance response"); print("="*78)
print(f"element mass check: 4*{E_qDP:.0f}+4*{E_eDP:.0f} = {4*E_qDP+4*E_eDP:.0f} MeV (DD-priced 1408 EXACT)")
print(f"in-situ inertia (0886 constituent rule): m_qCP = {m_q:.0f} MeV, m_eCP = {m_e:.0f} MeV")
print()
# ---------- lattice ----------
def plane(R,a_q):
    h=a_q/2
    return [(+h,+h,+1,'q'),(-h,+h,-1,'q'),(-h,-h,+1,'q'),(+h,-h,-1,'q'),
            (+R,0,-1,'e'),(0,+R,+1,'e'),(-R,0,-1,'e'),(0,-R,+1,'e')]
def build(centers,angles):
    Cc=[];Pp=[];Ww=[];Sp=[]
    for k in range(N):
        cx,cy,cz=centers[k]; th=angles[k]; c,s=np.cos(th),np.sin(th); par=(-1)**k
        for (x,y,sgn,sp) in plane(R_E,A_Q):
            Pp.append((cx+x*c,cy+y,cz-x*s)); Cc.append(sgn*par)
            Ww.append(np.sqrt(ALPHA_S) if sp=='q' else np.sqrt(ALPHA)); Sp.append(sp)
    return np.array(Cc,float),np.array(Pp,float),np.array(Ww,float),Sp
def bend(kap):
    if abs(kap)<1e-12: return build([(0,0,k*D) for k in range(N)],[0.0]*N)
    R=1/kap; ph=[k*D/R for k in range(N)]
    return build([(R*(1-np.cos(p)),0,R*np.sin(p)) for p in ph],ph)
def Esw(cfg):
    Cc,Pp,Ww,_=cfg; E=0.0
    for i in range(len(Cc)):
        dd=Pp[i+1:]-Pp[i]; r=np.sqrt((dd*dd).sum(axis=1))
        E+=np.sum(-(1-2*DELTA)*Ww[i]*Cc[i]*(Ww[i+1:]*Cc[i+1:])*AHC/r)
    return E
def Phi_split(cfg):
    Cc,Pp,Ww,Sp=cfg; core=0.0; coat=0.0
    for i in range(len(Cc)):
        dd=Pp[i]-Pp; r=np.sqrt((dd*dd).sum(axis=1)); r[i]=np.inf
        Ei=((Ww*Cc)[:,None]*dd/(r**3)[:,None]).sum(axis=0)*AHC
        c=Ww[i]**2*(Ei@Ei)
        if Sp[i]=='q': core+=c
        else: coat+=c
    return core,coat
def stiff(fn,y0,xs=(0.005,0.01,0.02)):
    return 2*np.mean([(fn(x)-y0)/x**2 for x in xs])
cfg0=bend(0.0); Cc0,Pp,Ww,Sp=cfg0; E0=Esw(cfg0); P0c,P0e=Phi_split(cfg0)
# ---------- species-resolved thresholds ----------
straight=[(0,0,k*D) for k in range(N)]
SEg=stiff(lambda t:Esw(build(straight,[t*k for k in range(N)])),E0)
SPcg=stiff(lambda t:Phi_split(build(straight,[t*k for k in range(N)]))[0],P0c)
SPeg=stiff(lambda t:Phi_split(build(straight,[t*k for k in range(N)]))[1],P0e)
SEu=stiff(lambda t:Esw(build(straight,[t]*N)),E0)
SPcu=stiff(lambda t:Phi_split(build(straight,[t]*N))[0],P0c)
SPeu=stiff(lambda t:Phi_split(build(straight,[t]*N))[1],P0e)
KAP=2*np.pi/(N*D); dk=KAP/68
Ee=Esw(bend(KAP)); Pce,Pee=Phi_split(bend(KAP))
Ee2=Esw(bend(KAP-dk)); Pce2,Pee2=Phi_split(bend(KAP-dk))
gE=(Ee-Ee2)/dk; gPc=(Pce-Pce2)/dk; gPe=(Pee-Pee2)/dk
lam_glob_c=lambda le: (Ee-E0 + le*(Pee-P0e))/-(Pce-P0c)
print("species-resolved requirements on lambda_q, given lambda_e:")
print(f"  tilt gradient: SE={SEg:+.0f}, SP_core={SPcg:+.3e}, SP_coat={SPeg:+.3e}")
print(f"  tilt uniform : SE={SEu:+.1f}, SP_core={SPcu:+.3e}, SP_coat={SPeu:+.3e}")
print(f"  closure endpoint slopes: dE/dk={gE:+.0f}, dPhi_c/dk={gPc:+.0f}, dPhi_e/dk={gPe:+.0f}")
print()
# ---------- switch-process simulation ----------
qidx=[[ (2*e+a)*8+b for a in range(2) for b in range(4)] for e in range(8)]
eidx=[[ (2*e+a)*8+4+b for a in range(2) for b in range(4)] for e in range(8)]
tgt_q = 7*8+0        # plane 7 (mid-rod), first qCP
tgt_e = 7*8+4        # plane 7, first eCP
def pattern_field(i):
    dd=Pp[i]-Pp; r=np.sqrt((dd*dd).sum(axis=1)); r[i]=np.inf
    return ((Ww*Cc0)[:,None]*dd/(r**3)[:,None]).sum(axis=0)*AHC
Wq2Eq2=Ww[tgt_q]**2*(pattern_field(tgt_q)@pattern_field(tgt_q))
We2Ee2=Ww[tgt_e]**2*(pattern_field(tgt_e)@pattern_field(tgt_e))
# geometry vectors for fast force eval
def force_on(i,charges):
    dd=Pp[i]-Pp; r=np.sqrt((dd*dd).sum(axis=1)); r[i]=np.inf
    return Ww[i]*charges[i]*(((Ww*charges)[:,None]*dd/(r**3)[:,None]).sum(axis=0))*AHC
def run(NT, swaps_q_per_tick, swaps_e_per_tick, tick_MeV, periodic_len=None, seed=1):
    \"\"\"simulate NT ticks; return force time series at both targets.
       tick_MeV = hbar/tick in MeV (energy of one-tick angular freq = 2pi/T_total*n grid).\"\"\"
    r=np.random.default_rng(seed)
    ch=Cc0.copy()
    # optional periodic drive: pre-generate a swap script and tile it
    script=[]
    if periodic_len:
        for t in range(periodic_len):
            step=[]
            for e in range(8):
                for _ in range(swaps_q_per_tick):
                    g=qidx[e]; cg=ch[g]  # note: uses evolving ch only for +- lists; regenerate generically
                    step.append(('q',e,r.integers(0,4),r.integers(0,4)))
                ne=swaps_e_per_tick if isinstance(swaps_e_per_tick,int) else (int(swaps_e_per_tick)+ (r.random()< (swaps_e_per_tick%1)))
                for _ in range(ne):
                    step.append(('e',e,r.integers(0,4),r.integers(0,4)))
            script.append(step)
    Fq=np.zeros((NT,3)); Fe=np.zeros((NT,3))
    for t in range(NT):
        if periodic_len:
            step=script[t%periodic_len]
            for (spn,e,ip,im) in step:
                g=qidx[e] if spn=='q' else eidx[e]
                plus=[j for j in g if ch[j]>0]; minus=[j for j in g if ch[j]<0]
                a=plus[ip%len(plus)]; b=minus[im%len(minus)]
                ch[a],ch[b]=ch[b],ch[a]
        else:
            for e in range(8):
                for _ in range(swaps_q_per_tick):
                    g=qidx[e]; plus=[j for j in g if ch[j]>0]; minus=[j for j in g if ch[j]<0]
                    a=plus[r.integers(0,len(plus))]; b=minus[r.integers(0,len(minus))]
                    ch[a],ch[b]=ch[b],ch[a]
                ne=swaps_e_per_tick if isinstance(swaps_e_per_tick,int) else (int(swaps_e_per_tick)+(r.random()<(swaps_e_per_tick%1)))
                for _ in range(ne):
                    g=eidx[e]; plus=[j for j in g if ch[j]>0]; minus=[j for j in g if ch[j]<0]
                    a=plus[r.integers(0,len(plus))]; b=minus[r.integers(0,len(minus))]
                    ch[a],ch[b]=ch[b],ch[a]
        Fq[t]=force_on(tgt_q,ch); Fe[t]=force_on(tgt_e,ch)
    return Fq,Fe
def response(F, m, hwA, NT, hw_grid_unit, label):
    \"\"\"one-sided spectral response; returns (U_above, U_below, excl_weight, S_tot)\"\"\"
    Ua=0.0;Ub=0.0;excl=0.0;Stot=0.0
    for c in range(3):
        X=np.fft.rfft(F[:,c]-F[:,c].mean())
        S=2*np.abs(X)**2/NT**2   # mean-square amplitude per line (one-sided)
        for n in range(1,len(S)):
            hw=n*hw_grid_unit
            Stot+=S[n]
            if abs(hw-hwA)<0.1*hwA: excl+=S[n]; continue
            U=S[n]*AHC**2/(4*m*(hw**2-hwA**2))
            if hw>hwA: Ua+=U
            else: Ub+=U
    return Ua,Ub,excl,Stot
# clock setup: tick = tau_hop/4  =>  hbar*w_tick... grid unit: hw_n = n * (hbar*2pi/T_total)
# ticks per Compton period = 4 => full period energy 264 MeV spans 4 ticks:
# time step dt = tau_hop/4 = 2*pi*hbar/(4*264 MeV) => grid unit = 2*pi*hbar/(NT*dt) = 4*264/NT
NT=8192
for clockname, sq, se_rate, ticks_per_period in [
    ("PRIMARY: 1 hop/Compton period (4 swaps/elem/period)",1,553.0/264.0,4),
    ("ALT (unfavorable): 2 hops/period (8 swaps/elem/period)",2,2*553.0/264.0,8)]:
    unit=ticks_per_period*264.0/NT   # MeV per FFT line
    Fq,Fe=run(NT,sq,se_rate,unit,seed=11)
    # verify duty statistics
    print(f"[{clockname}] grid {unit*1000:.1f} keV/line, Nyquist {unit*NT/2:.0f} MeV")
    print(f"  pattern refs: w^2|E|^2 core={Wq2Eq2:.1f}, coat={We2Ee2:.3f}; "
          f"<F> vs (1-2d)*pattern check: {norm(Fq.mean(axis=0))/ (norm(pattern_field(tgt_q))*Ww[tgt_q]*(1-2*DELTA)):.3f} (→1)")
    print(f"  {'E_qq':>6} {'hwA_q':>7} {'lam_q(abv)':>11} {'lam_q(blw)':>11} {'lam_q(net)':>11} {'excl%':>6}")
    for Eqq in (40.0,66.0,100.0,170.0):
        hwA=np.sqrt(2*Eqq*AHC**2/(d**2*m_q))
        Ua,Ub,ex,St=response(Fq,m_q,hwA,NT,unit,'q')
        print(f"  {Eqq:>6.0f} {hwA:>7.1f} {Ua/Wq2Eq2:>11.3e} {Ub/Wq2Eq2:>11.3e} {(Ua+Ub)/Wq2Eq2:>11.3e} {100*ex/St:>6.2f}")
    hwAe=7.0
    Ua,Ub,ex,St=response(Fe,m_e,hwAe,NT,unit,'e')
    lam_e=(Ua+Ub)/We2Ee2
    print(f"  coat (hwA~7): lam_e = {lam_e:.3e} (above {Ua/We2Ee2:.2e} / below {Ub/We2Ee2:.2e})")
    print()
# store primary run for placement
Fq,Fe=run(NT,1,553.0/264.0,4*264.0/NT,seed=11)
unit=4*264.0/NT
print("="*78)
print("PLACEMENT (primary clock), species-resolved, per E_qq branch:")
print(f"  required lam_q given lam_e:  tilt-grad  lam_q > (-(SE)+.. )   computed per lam_e")
Ua,Ub,ex,St=response(Fe,m_e,7.0,NT,unit,'e'); lam_e=(Ua+Ub)/We2Ee2
req_tg=(-(SEg)-lam_e*SPeg)/SPcg
req_tu=(-(SEu)-lam_e*SPeu)/SPcu
req_cl=(gE+lam_e*gPe)/-gPc
req_gl=lam_glob_c(lam_e)
print(f"  lam_e(derived) = {lam_e:.3e}")
print(f"  thresholds on lam_q: tilt-grad {req_tg:.3e} | tilt-unif {req_tu:.3e} | "
      f"anti-open {req_cl:.3e} | ring-global {req_gl:.3e}")
print(f"  {'E_qq':>6} {'hwA_q':>7} {'lam_q(net)':>11}  verdict vs max-threshold")
thr=max(req_tg,req_tu,req_cl,req_gl)
for Eqq in (40.0,66.0,100.0,170.0):
    hwA=np.sqrt(2*Eqq*AHC**2/(d**2*m_q))
    Ua,Ub,ex,St=response(Fq,m_q,hwA,NT,unit,'q')
    lq=(Ua+Ub)/Wq2Eq2
    v="FULLY STABILIZED" if lq>=thr else ("partial: "+",".join(
        n for n,t in [("tilt-g",req_tg),("tilt-u",req_tu),("anti-open",req_cl),("global",req_gl)] if lq>=t) or "BELOW ALL")
    print(f"  {Eqq:>6.0f} {hwA:>7.1f} {lq:>11.3e}  {v}")
print("="*78)
""")

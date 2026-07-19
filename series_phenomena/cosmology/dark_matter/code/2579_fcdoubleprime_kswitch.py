#!/usr/bin/env python3
"""
PATCH 2579 -- F-c'' EXECUTION under fcdoubleprime_preregistration.md (2578) ONLY.
Every formula cites its registered source (2578 S2 discipline).
  [C1] static kernel + species: 2575 (code/2575_fc_statics_core.py, U-A/U-B verbatim)
  [C2] landscape form: 2578 S0(a) -- mean (1-2d)U + 4d(1-d)|F_unit|^2 (hbarc)^2/(4 mu (hw)^2)
  [C3] monodromy: 2440 (T_osc/T_hyp/monodromy, Meissner limit, verbatim transfer)
  [C4] clocks 264/553: 2451 registered inputs; delta sweep: 2440 G5 + 2435 upper bound
"""
import numpy as np
AHC=197.3; PHI_G=(1+np.sqrt(5))/2; ALPHA_S=5/(8*PHI_G); ALPHA=1/137.036
A_QQ=AHC/264.0; A_EE=AHC/553.0; A_QE=np.sqrt(A_QQ*A_EE)
D=1.15; A_Q=D; r_q=A_Q/np.sqrt(2); R_E=1.6*r_q; FLOOR=2.0
HW_Q=264.0; MU=264.0     # [C4]; mu c^2 = (4*132)/2 pinned (2578 S0a)
TWO_PI=2*np.pi

def soft_a(si,sj): return A_QQ if si==sj=='q' else (A_EE if si==sj=='e' else A_QE)
def w(s): return np.sqrt(ALPHA_S) if s=='q' else np.sqrt(ALPHA)
def unit(par,z,coated=False):                       # [C1]
    h=A_Q/2; q=[(+h,+h,+1),(-h,+h,-1),(-h,-h,+1),(+h,-h,-1)]
    P=[];C=[];S=[]
    for (x,y,sg) in q: P.append((x,y,z));C.append(sg*par);S.append('q')
    if coated:
        for (x,y,sg) in q:
            n=np.hypot(x,y); P.append((R_E*x/n,R_E*y/n,z));C.append(-sg*par);S.append('e')
    return np.array(P,float),np.array(C,float),S
def Ustat(sep,parB=-1,coated=False):                # [C1]
    PA,CA,SA=unit(+1,0,coated); PB,CB,SB=unit(parB,sep,coated)
    E=0.0
    for i in range(len(PA)):
        for j in range(len(PB)):
            a=soft_a(SA[i],SB[j]); r2=((PA[i]-PB[j])**2).sum()
            E+=w(SA[i])*CA[i]*w(SB[j])*CB[j]/np.sqrt(r2+a*a)
    return E*AHC

SEPS=np.linspace(0.05,2.6,120)*D
dse=SEPS[1]-SEPS[0]
def curves(coated=False):
    U=np.array([Ustat(s,-1,coated) for s in SEPS])
    Um=np.array([Ustat(s,+1,coated) for s in SEPS])
    return U,Um
U_A,Um_A=curves(False)
assert np.max(np.abs(U_A+Um_A))<1e-9, "mirror identity violated"   # 2578 S1 assert
print("="*78); print("PATCH 2579 -- F-c'' EXECUTION: the switched encounter"); print("="*78)
print(f"[mirror] U_rep == -U_att exactly (max dev {np.max(np.abs(U_A+Um_A)):.1e})")

def d1(U): return np.gradient(U,dse)
def d2(U): return np.gradient(np.gradient(U,dse),dse)

# [C3] 2440 machinery VERBATIM
def T_osc(alpha,t):
    wv=np.sqrt(alpha); c,s=np.cos(wv*t),np.sin(wv*t)
    return np.array([[c,s/wv],[-wv*s,c]])
def T_hyp(alpha,t):
    wv=np.sqrt(alpha); c,s=np.cosh(wv*t),np.sinh(wv*t)
    return np.array([[c,s/wv],[wv*s,c]])
def stable(eps_rep,eps_att,delta):
    """Square-wave period tau=2pi (in switching units): fraction delta at curvature
    +eps_rep-phase value, (1-delta) at eps_att-phase value; each phase value may be
    restoring (osc) or anti-restoring (hyp) BY ITS SIGN (2578: signs as computed)."""
    def phase(alpha,t):
        if abs(alpha)<1e-15: return np.array([[1.0,t],[0.0,1.0]])
        return T_osc(alpha,t) if alpha>0 else T_hyp(-alpha,t)
    M=phase(eps_att,(1-delta)*TWO_PI) @ phase(eps_rep,delta*TWO_PI)
    return abs(np.trace(M))<=2.0

CONV=(AHC**2)/(MU*HW_Q**2)          # eps = U'' * (hbarc)^2/(mu (hw)^2)  [C2/C3 units]
DELTAS=(0.10,0.20,1/3,3/7)
def analyze(U,label):
    F=-d1(U); K=d2(U)
    print(f"\n### {label}")
    print(f"{'delta':>6} | {'min U_eff':>10} {'@sep/D':>7} {'depth':>7} {'rise<':>6} {'mono@min':>8} {'core?':>6}")
    out={}
    for dlt in DELTAS:
        f2=4*dlt*(1-dlt)
        Ueff=(1-2*dlt)*U + f2*(F*F)*CONV/4.0     # [C2]
        i=int(np.argmin(Ueff)); interior=0<i<len(Ueff)-1
        depth=Ueff[-1]-Ueff[i]; rise=interior and Ueff[0]>Ueff[i]+2*FLOOR
        # monodromy at the landscape minimum: phase curvatures of the SWITCHED potential:
        # rep phase curvature = d2 of +U at i ; att phase = d2 of -U ... signs as computed:
        er=(+K[i])*CONV; ea=(-K[i])*CONV
        mono=stable(er,ea,dlt) if interior else False
        ok=interior and depth>2*FLOOR and rise and mono
        out[dlt]=(Ueff,i,ok,depth,mono)
        print(f"{dlt:6.3f} | {Ueff[i]:10.2f} {SEPS[i]/D:7.3f} {depth:7.2f} {str(rise):>6} {str(mono):>8} {'YES' if ok else 'no':>6}")
    return out

resA=analyze(U_A,"U-A bare squares (primary)")
U_B,_=curves(True)
resB=analyze(U_B,"U-B coated (union secondary)")

# Also: full monodromy stability BAND in sep (instrument (b) standalone), delta=3/7
print("\n[monodromy band, delta=3/7, U-A] sep/D where |tr M|<=2:")
K=d2(U_A); band=[SEPS[i]/D for i in range(len(SEPS)) if stable(K[i]*CONV,-K[i]*CONV,3/7)]
if band: print(f"  {len(band)} of {len(SEPS)} grid points; range [{min(band):.2f},{max(band):.2f}] D")
else: print("  none")

ok37=resA[3/7][2]; ok13=resA[1/3][2]
gen_any=any(resA[d][2] for d in DELTAS) or any(resB[d][2] for d in DELTAS)
print("\nREADING (per 2578 S2):")
if ok37 and ok13:
    i=resA[3/7][1]
    print(f"  R1'' FIRES: dynamic equilibrium at {SEPS[i]/D:.3f} D (delta=3/7), surviving the "
          f"stingy pair, monodromy-stable. F-c'' CONFIRMED at derivation strength.")
elif not gen_any:
    print("  R2'' FIRES: no qualifying minimum-with-stability at any swept delta under the "
          "generous members. F-b proceeds WITH EXHAUSTION -- every registered stabilization "
          "channel is now on the record as insufficient at the encounter scale.")
else:
    print("  R3'': split/partial verdicts -- recorded exactly; routed to founder.")

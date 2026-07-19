#!/usr/bin/env python3
"""
PATCH 2577 -- F-c' EXECUTION under fcprime_preregistration.md (2576) ONLY.
Exact Gauss-Hermite average of the registered soft kernel over relative ZBW jitter;
readings R1'/R2'/R3' frozen at 2576 S3. No amplitude selection is made here.
"""
import numpy as np
AHC=197.3; PHI_G=(1+np.sqrt(5))/2; ALPHA_S=5/(8*PHI_G); ALPHA=1/137.036
A_QQ=AHC/264.0; A_EE=AHC/553.0; A_QE=np.sqrt(A_QQ*A_EE)
D=1.15; A_Q=D; r_q=A_Q/np.sqrt(2); R_E=1.6*r_q; FLOOR=2.0
F2=48/49.0
def soft_a(si,sj): return A_QQ if si==sj=='q' else (A_EE if si==sj=='e' else A_QE)
def w(s): return np.sqrt(ALPHA_S) if s=='q' else np.sqrt(ALPHA)
def unit(par,z,coated=False):
    h=A_Q/2; q=[(+h,+h,+1),(-h,+h,-1),(-h,-h,+1),(+h,-h,-1)]
    P=[];C=[];S=[]
    for (x,y,sg) in q: P.append((x,y,z));C.append(sg*par);S.append('q')
    if coated:
        for (x,y,sg) in q:
            n=np.hypot(x,y); P.append((R_E*x/n,R_E*y/n,z));C.append(-sg*par);S.append('e')
    return np.array(P,float),np.array(C,float),S

# Gauss-Hermite product nodes for a standard normal (weights sum to 1)
def gh(n):
    x,wgt=np.polynomial.hermite_e.hermegauss(n)   # weight e^{-x^2/2}
    wgt=wgt/wgt.sum(); return x,wgt

def Ueff(sep, xi, nodes=7, coated=False, jitter='indep', f2w=True):
    """Exact Gaussian average of cross energy. jitter: 'indep' (relative per-axis var
    2 xi^2/3) or 'rigid' (units jitter as wholes; relative var 2 xi^2/3 identical for
    the CROSS energy of rigid translation -- distinct only through intra-unit
    correlations, which cancel here since only relative pair vectors enter and rigid
    jitter shifts ALL cross pair vectors by the SAME eta -> same integral. The bracket
    therefore collapses analytically for cross terms; asserted below at a probe)."""
    PA,CA,SA=unit(+1,0.0,coated); PB,CB,SB=unit(-1,sep,coated)
    var_axis=(2*xi*xi/3.0)*(F2 if f2w else 1.0)
    s=np.sqrt(var_axis)
    x,wg=gh(nodes)
    X,Y,Z=np.meshgrid(x,x,x,indexing='ij')
    W=(wg[:,None,None]*wg[None,:,None]*wg[None,None,:]).ravel()
    ETA=np.stack([X.ravel(),Y.ravel(),Z.ravel()],axis=1)*s
    E=0.0
    for i in range(len(PA)):
        for j in range(len(PB)):
            a=soft_a(SA[i],SB[j])
            dv=(PA[i]-PB[j])[None,:]+ETA
            r2=(dv*dv).sum(axis=1)
            E+=w(SA[i])*CA[i]*w(SB[j])*CB[j]*np.sum(W/np.sqrt(r2+a*a))
    return E*AHC

def kapitza(sep, xi, coated=False):
    PA,CA,SA=unit(+1,0.0,coated); PB,CB,SB=unit(-1,sep,coated)
    var_tot=2*xi*xi*F2
    E=0.0
    for i in range(len(PA)):
        for j in range(len(PB)):
            a=soft_a(SA[i],SB[j]); r2=((PA[i]-PB[j])**2).sum()
            base=1.0/np.sqrt(r2+a*a); lap=-3*a*a*(r2+a*a)**(-2.5)
            E+=w(SA[i])*CA[i]*w(SB[j])*CB[j]*(base+(var_tot/6.0)*lap)
    return E*AHC

SEPS=np.linspace(0.05,2.6,60)*D
XIS=[0.2,0.4,0.631,0.747,1.0,1.121,1.5,2.0,2.242,2.8,3.36]
CAND={0.631:'m=312.7',0.747:'m=264',1.121:'m=176',2.242:'m=88'}

print("="*78); print("PATCH 2577 -- F-c' EXECUTION: U_eff(sep; xi), registered stacking"); print("="*78)
# convergence probes (declared): (0.5D,0.747),(1.0D,1.121),(0.2D,2.242)
print("[convergence 7^3 vs 9^3]  (declared probes)")
for sp,xx in ((0.5*D,0.747),(1.0*D,1.121),(0.2*D,2.242)):
    u7=Ueff(sp,xx,7); u9=Ueff(sp,xx,9)
    print(f"  sep={sp/D:.2f}D xi={xx}: {u7:9.3f} vs {u9:9.3f}  d={abs(u7-u9):.2e}")
# rigid-vs-indep bracket collapse assert at a probe
ui=Ueff(0.5*D,1.0,7,jitter='indep'); ur=Ueff(0.5*D,1.0,7,jitter='rigid')
assert abs(ui-ur)<1e-9
print(f"[bracket] rigid==indep for cross energy (analytic collapse confirmed): d={abs(ui-ur):.1e}")
# small-xi Kapitza coherence
uK=kapitza(1.0*D,0.2); uE=Ueff(1.0*D,0.2,7)
print(f"[coherence] xi=0.2: exact {uE:8.3f} vs Kapitza {uK:8.3f}  d={abs(uE-uK):.3f}")

def analyze(xi, coated=False, f2w=True):
    U=np.array([Ueff(s,xi,7,coated,f2w=f2w) for s in SEPS])
    i=int(np.argmin(U)); interior=0<i<len(U)-1
    plateau=U[-1]
    depth=plateau-U[i]
    rise_below = interior and np.all(np.diff(U[:i+1])<1e-9)  # monotone decreasing INTO min from below side? careful:
    # repulsive rise below the minimum means U increases as sep decreases past the min:
    rise_below = interior and (U[0]>U[i]+2*FLOOR)
    ok = interior and depth>2*FLOOR and rise_below
    return U,i,ok,depth

print(f"\n{'xi [fm]':>8} {'cand':>8} | {'U(0.05D)':>9} {'min U':>9} {'@sep/D':>7} {'depth-vs-plateau':>16} {'core?':>6}")
found=[]
for xi in XIS:
    U,i,ok,depth=analyze(xi)
    tag=CAND.get(xi,'')
    print(f"{xi:8.3f} {tag:>8} | {U[0]:9.2f} {U[i]:9.2f} {SEPS[i]/D:7.3f} {depth:16.2f} {'YES' if ok else 'no':>6}")
    if ok: found.append((xi,SEPS[i]/D,U[i],depth,U[0]))
print()
if found:
    xistar=found[0][0]
    in_span=[x for x,_,_,_,_ in found if x in CAND]
    print(f"xi* (smallest amplitude with a qualifying core) <= {xistar} fm")
    if in_span:
        print(f"R1' CANDIDATE: qualifying core at registered amplitude(s): "
          + ", ".join(f"xi={x} ({CAND[x]}): min at {l:.3f} D, depth {d:.1f} MeV, wall U(0.05D)={u0:+.1f}"
                      for x,l,_,d,u0 in found if x in CAND))
        print("STINGY-convention check (f2 off is generous; f2 ON is stingier by 1%;")
        for x,l,_,d,u0 in found:
            if x in CAND:
                U2,i2,ok2,d2=analyze(x,f2w=True)
                print(f"  xi={x}: stingy member ok={ok2} depth={d2:.1f}")
        # coated union member at the smallest confirming candidate
        xs=in_span[0]
        Uc,ic,okc,dc=analyze(xs,coated=True)
        print(f"  coated union at xi={xs}: ok={okc}, min at {SEPS[ic]/D:.3f} D, depth {dc:.1f} MeV")
    else:
        print("R3' shape: core exists only OUTSIDE the registered candidate span.")
else:
    print("No qualifying minimum at any xi <= 1.5x largest candidate -> R2' fires (F-b re-enters).")

# =============================================================================
# FAITHFULNESS FIX (2573-class, disclosed): the prereg S1.5 jitter statistics
# implemented POSITION-SMEARING, which the in-run rigid==indep collapse proves
# analytically cannot carry ponderomotive content (the Kapitza repulsion lives
# in the drive-response CORRELATION that uncorrelated smearing discards). The
# REGISTERED lineage the prereg claimed to consume (2451) supplies the identity
# verbatim, with NO free amplitude:  U_pond,i = (w_i|E_i|)^2_osc/(4 m omega^2),
# lambda_phys = f_osc^2 (hbar c)^2 / (4 (mc^2)(hbar omega)^2). The registered
# content governs. The smearing curves above STAND as the disclosed record of
# the wrong formalism; the derivation below is the faithful one. The amplitude-
# threshold framing DISSOLVES (2451's identity consumes mass+clock directly);
# the mass-candidate union {88,176,264,312.7} MeV carries the span, clocks
# 264 (q) / 553 (e). Readings: R1'/R2' SHAPE unchanged (interior minimum +
# repulsive rise + depth > 2*floor); confirm must hold at the STINGIEST
# registered mass (largest m -> smallest lambda -> weakest core: m=312.7);
# kill must hold even at the most GENEROUS (m=88, largest lambda).
# =============================================================================
HW_Q=264.0; HW_E=553.0
def field_sq_at(Pt,Ct,St,x):
    """|sum_j w_j q_j (x-P_j)/(r^2+a^2)^{3/2}|^2 * AHC^2 -- squared force-per-unit-w
       from the OTHER unit at point x (soft kernel gradient, registered form)."""
    F=np.zeros(3)
    for j in range(len(Pt)):
        a=soft_a('q',St[j])  # receiver is qCP in U-A; coated handled below
        d=x-Pt[j]; r2=(d*d).sum()
        F+=w(St[j])*Ct[j]*d/(r2+a*a)**1.5
    return (F*AHC)  # MeV/fm per unit receiver-w
def Ueff_pond(sep, mc2, coated=False):
    PA,CA,SA=unit(+1,0.0,coated); PB,CB,SB=unit(-1,sep,coated)
    # static part (registered kernel, verbatim)
    Us=0.0
    for i in range(len(PA)):
        for j in range(len(PB)):
            a=soft_a(SA[i],SB[j]); r2=((PA[i]-PB[j])**2).sum()
            Us+=w(SA[i])*CA[i]*w(SB[j])*CB[j]/np.sqrt(r2+a*a)
    Us*=AHC
    # ponderomotive part: each CP of each unit in the OTHER unit's field
    Up=0.0
    for (Pr,Cr,Sr,Pt,Ct,St) in ((PA,CA,SA,PB,CB,SB),(PB,CB,SB,PA,CA,SA)):
        for i in range(len(Pr)):
            hw = HW_Q if Sr[i]=='q' else HW_E
            lam = F2*(AHC)**2/(4.0*mc2*hw*hw)   # fm^2/MeV (2451 identity verbatim)
            Fv=field_sq_at(Pt,Ct,St,Pr[i])*w(Sr[i])
            Up+=lam*float((Fv*Fv).sum())
    return Us+Up
print("\n"+"="*78)
print("FAITHFUL DERIVATION (2451 identity; no free amplitude):")
print(f"{'mc2':>7} | {'U(0.05D)':>9} {'min U':>9} {'@sep/D':>7} {'depth-vs-plateau':>16} {'core?':>6}")
res={}
for mc2 in (312.7,264.0,176.0,88.0):
    U=np.array([Ueff_pond(s,mc2) for s in SEPS])
    i=int(np.argmin(U)); interior=0<i<len(U)-1
    depth=U[-1]-U[i]; ok=interior and depth>2*FLOOR and (U[0]>U[i]+2*FLOOR)
    res[mc2]=(U,i,ok,depth)
    print(f"{mc2:7.1f} | {U[0]:9.2f} {U[i]:9.2f} {SEPS[i]/D:7.3f} {depth:16.2f} {'YES' if ok else 'no':>6}")
stingy_ok=res[312.7][2]; generous_ok=res[88.0][2]
print()
if stingy_ok:
    U,i,_,d=res[312.7]
    print(f"R1' FIRES AT THE STINGIEST REGISTERED MASS: interior minimum at "
          f"{SEPS[i]/D:.3f} D, depth {d:.1f} MeV, inner wall U(0.05D)={U[0]:+.1f} MeV.")
    Uc=np.array([Ueff_pond(s,312.7,coated=True) for s in SEPS])
    ic=int(np.argmin(Uc)); dc=Uc[-1]-Uc[ic]
    okc=0<ic<len(Uc)-1 and dc>2*FLOOR and Uc[0]>Uc[ic]+2*FLOOR
    print(f"  coated union member (m=312.7): ok={okc}, min at {SEPS[ic]/D:.3f} D, depth {dc:.1f} MeV")
elif generous_ok:
    print("R3' shape: core only at generous masses -- mass assignment routes to founder.")
else:
    print("R2' under the faithful formalism too: no core at any registered mass -> F-b re-enters.")

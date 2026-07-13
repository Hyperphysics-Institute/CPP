#!/usr/bin/env python3
"""
PATCH 2443 -- OPEN-DM-FLOQUET-1 / R1 self-consistent solve, FINITE-ANGLE flexure for
the N_planes=16 ring make-or-break. At theta = 2pi/16 = 22.5 deg/hinge the bonds
strain ~20-30%, outside the harmonic (V'') regime, so the full bond potential is used
-- which also DERIVES the R6 branch (which bond fragments) from the strain.

KINEMATICS: R_ring = d/(2 sin(theta/2)); bond at offset x has L(x)=d+2 x sin(theta/2).
  (2 sin(theta/2)=0.390 vs theta=0.393 -> kinematic nonlinearity <1%; the potential
   nonlinearity over a 20-30% strain is what matters.)
BOND: V(r)=-A_eff/r+K/r^2, A_eff=(1-2 delta)A, delta=3/7 (net attractive 1/7). Outer
  bonds stretch (bounded by depth=dissociation); inner compress (steep K/r^2). Soft-
  stretch/stiff-compress asymmetry = founder-flagged "resistance changes with bending."
CROSS-SECTION: per junction 4 core (qCP square r_q)+4 coat (eCP square R_e). Lever=x.
GUARDRAILS G1/G3/G5/G6/G7. Layer C. NOT R5-netted. Not survival.
"""
import numpy as np
AHC=197.3; ALPHA=1/137.036; PHI=(1+np.sqrt(5))/2; ALPHA_S=5/(8*PHI)
DELTA=3/7; NPL=16; THETA=2*np.pi/NPL; THRESH_LO=0.43; d_target=1.15; CEIL=NPL/(2*np.pi**2)
print("="*74)
print(f"R1 FINITE-ANGLE FLEXURE -- geometry #3, N_planes={NPL}, theta={np.degrees(THETA):.1f} deg/hinge")
print("="*74)
print(f"alpha_s={ALPHA_S:.4f} alpha={ALPHA:.5f} ratio={ALPHA_S/ALPHA:.1f} delta=3/7={DELTA:.4f}")
print(f"kinematic 2sin(theta/2)={2*np.sin(THETA/2):.4f} vs theta={THETA:.4f}  window=[{THRESH_LO},{CEIL:.3f}]")
print()
def bond(A,K,delta=DELTA):
    A_eff=(1-2*delta)*A; dstar=2*K/A_eff
    V=lambda r:-A_eff/r+K/r**2
    depth=-V(dstar); kax=-2*A_eff/dstar**3+6*K/dstar**4; force=A_eff/dstar**2-2*K/dstar**3
    return dict(A_eff=A_eff,K=K,dstar=dstar,depth=depth,kax=kax,force=force,V=V)
A_core=ALPHA_S*AHC; K_core=(1-2*DELTA)*A_core*d_target/2; C=bond(A_core,K_core)
print(f"CORE d*={C['dstar']:.4f}fm |F|={abs(C['force']):.1e}(G3) depth={C['depth']*1000:.0f}keV kax={C['kax']:.3f}")
print(f"G1: delta=0->+1 attractive well; delta=1->-1 no well; 3/7->{1-2*DELTA:+.3f} attractive. OK.")
print()
def finite_bend(Re_over_rq,coat_depth_frac,rq_over_d=1/np.sqrt(2),orient_deg=45,delta=DELTA,Ccore=None):
    d=d_target; r_q=rq_over_d*d; R_e=Re_over_rq*r_q
    Cc=Ccore if Ccore else C
    A_coat=ALPHA*AHC; K_coat=(1-2*delta)*A_coat*d/2; Co=bond(A_coat,K_coat,delta)
    coat_scale=coat_depth_frac*Cc['depth']/Co['depth']
    Vcore=Cc['V']; Vcoat=lambda r:(-Co['A_eff']/r+Co['K']/r**2)*coat_scale
    ang=np.radians(orient_deg)+np.array([0,np.pi/2,np.pi,3*np.pi/2])
    xs_core=r_q*np.cos(ang); xs_coat=R_e*np.cos(ang); s=np.sin(THETA/2)
    depth_core=Cc['depth']; depth_coat=Co['depth']*coat_scale; U=0.0; pb=[]
    for x in xs_core:
        L=d+2*x*s; dV=Vcore(L)-Vcore(d); U+=dV; pb.append(('core',x,L,dV,dV/depth_core))
    for x in xs_coat:
        L=d+2*x*s; dV=Vcoat(L)-Vcoat(d); U+=dV; pb.append(('coat',x,L,dV,dV/depth_coat))
    kappa_eff=2*U/THETA**2
    kappa_lin=Cc['kax']*np.sum(xs_core**2)+Co['kax']*coat_scale*np.sum(xs_coat**2)
    return dict(U=U,kappa_eff=kappa_eff,kappa_lin=kappa_lin,E_total=4*depth_core+4*depth_coat,
                E_coat=depth_coat,depth_core=depth_core,depth_coat=depth_coat,perbond=pb,r_q=r_q,R_e=R_e)
print("="*74); print("FINITE-ANGLE (baseline r_q=d/sqrt2, R_e/r_q=1.6, coat depth 10% of core)"); print("="*74)
b=finite_bend(1.6,0.10)
print(f"U(theta)/hinge={b['U']*1000:.1f}keV  kappa_eff=2U/theta^2={b['kappa_eff']*1000:.1f}keV")
print(f"kappa_linear(harmonic)={b['kappa_lin']*1000:.1f}keV -> finite/linear={b['kappa_eff']/b['kappa_lin']:.2f}x (nonlin)")
print(f"E_bond total={b['E_total']*1000:.0f}keV  coat-only(shallow)={b['E_coat']*1000:.0f}keV")
print()
print("per-bond strain (R6: fragmentation is TENSION-side = stretch toward dissociation;")
print(" compression climbs the K/r^2 wall -> costs energy but does NOT break the bond):")
print(f"  {'rail':>5} {'x[fm]':>7} {'L[fm]':>7} {'mode':>6} {'dV[keV]':>9} {'frac_depth':>11}")
for r,x,L,dV,frac in sorted(b['perbond'],key=lambda t:-t[4]):
    mode='stretch' if x>0 else 'compr'
    print(f"  {r:>5} {x:>7.3f} {L:>7.3f} {mode:>6} {dV*1000:>9.1f} {frac:>11.3f}")
tens=[t for t in b['perbond'] if t[1]>0]
fm=max(tens,key=lambda t:t[4])
print(f"  -> nearest dissociation (TENSION): {fm[0]} bond, frac={fm[4]:.3f} of depth."
      f"  {'FRAGMENTS' if fm[4]>=1 else 'no fragmentation at 22.5deg'} => formation "
      f"{'blocked' if fm[4]>=1 else 'feasible'}; R6 branch (weakest tension bond) = "
      f"{'SHALLOW/coat' if fm[0]=='coat' else 'DEEP/core'}")
print()
print("ratios vs window:")
for lab,E in [('E_total',b['E_total']),('E_coat(shallow)',b['E_coat'])]:
    r=b['kappa_eff']/E; v="IN-WINDOW" if THRESH_LO<=r<CEIL else ("too soft" if r<THRESH_LO else "springs open")
    print(f"  kappa_eff/{lab:16s}={r:8.3f}  -> {v}")
print(f"  spring-open: 16*U={16*b['U']*1000:.0f}keV vs E_total={b['E_total']*1000:.0f}keV -> "
      f"{'SPRINGS OPEN' if 16*b['U']>b['E_total'] else 'holds closed'}")
print()
print("="*74); print("SENSITIVITY: r_q/d and R_e/r_q"); print("="*74)
print(f"{'r_q/d':>7} {'R_e/rq':>7} {'kappa[keV]':>11} {'ratio(Etot)':>12} {'ratio(coat)':>12} {'frag':>6}")
for rqd in [0.5,1/np.sqrt(2),0.9]:
    for Re in [1.0,1.6,2.5]:
        bb=finite_bend(Re,0.10,rq_over_d=rqd); fr=max(bb['perbond'],key=lambda t:t[4])[0]
        print(f"{rqd:>7.3f} {Re:>7.2f} {bb['kappa_eff']*1000:>11.1f} {bb['kappa_eff']/bb['E_total']:>12.3f} "
              f"{bb['kappa_eff']/bb['E_coat']:>12.2f} {fr:>6}")
print()
print("delta-invariance (G5): ratio(E_total) vs delta, baseline geom")
for dl in [0.30,0.357,3/7,0.45]:
    if (1-2*dl)<=0: print(f"  delta={dl}: no well"); continue
    Cd=bond(ALPHA_S*AHC,(1-2*dl)*ALPHA_S*AHC*d_target/2,dl)
    b2=finite_bend(1.6,0.10,delta=dl,Ccore=Cd)
    print(f"  delta={dl:.3f}: kappa_eff={b2['kappa_eff']*1000:6.1f}keV ratio(Etot)={b2['kappa_eff']/b2['E_total']:.3f}")
print()
print("="*74)
print("HONEST READ (G7): reported where it lands. R1 (equil+finite-angle flexure), Layer C.")
print("NOT R5-netted (transverse ponderomotive, sign negative from 2430, magnitude on")
print("geom #3 un-recomputed). Not survival, not falsification.")
print("="*74)

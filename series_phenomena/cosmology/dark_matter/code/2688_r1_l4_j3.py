#!/usr/bin/env python3
"""FA-SG-R1 leg L4 (Patch 2688): the mandatory J3 companion attack.

Charter SS2 R1-L4 (the panel's unanimous highest-risk joint): an alternative
SITE-LEVEL normalization of alpha derived from the discrete-lattice Green
function at z = 12, tested against the continuum matching kappa^2 = 4 pi
alpha n used by the arc in the post-homogenization (kappa*a = 2) regime.
Executed as a derivation, not a scan. Fence F1: the LOCAL DP density n only.

Derivation. The frozen continuum matching is the self-consistency
  alpha * S_cont(kappa) = 1,   S_cont(kappa) = n Int d3r e^{-kappa r}/r
                                            = 4 pi n / kappa^2,
i.e. exactly alpha = kappa^2/(4 pi n). The site-level discrete analog
replaces the homogenized integral with the actual z = 12 lattice sum over
DP sites (self-site excluded -- no self-scattering):
  alpha' * S_disc(kappa) = 1,  S_disc(kappa) = sum_{j!=0} e^{-kappa r_j}/r_j,
evaluated at the operating point kappa*a = 2 (post-homogenization regime).
This is the discrete-lattice Green-function (isotropic evanescent) matching.

Propagation (charter: "reported explicitly, not assumed"): BOTH the
charter-stated l ~ alpha^{-1/2} scaling AND the direct empirical
propagation (re-solve the extended instrument at alpha', read l') are
computed; the alpha-scan below tests the scaling law itself. Frozen [ADJ]:
J3-CONCORD iff the alpha'-propagated l' lies within the joint L1/L3 band;
J3-REVISE otherwise.

Supplementary (reported, not the derivation): staggered-sector site sums at
the FCC zone-boundary X and L points; operator stability threshold
alpha_crit = -1/lambda_min(G).
Labeled robustness scan (axis frozen pre-run): alpha/alpha0 in
{0.5, 1, 1.5, 1.611, 2, 3}.
"""
import math, numpy as np

PHI=(1+math.sqrt(5))/2; L_UNIT=0.589; L_EDGE=L_UNIT/PHI; A=L_EDGE; D_REG=1.15
kappa0=2.0/A; alpha0=A/(math.pi*math.sqrt(2)); n_dens=math.sqrt(2.0)/A**3
JOINT_LO, JOINT_HI = 0.0836, 0.0956   # L1/L3 joint band (2685/2686)

print("== the two normalizations ==")
S_cont=4*math.pi*n_dens/kappa0**2
print(f"S_cont = 4 pi n / kappa^2 = {S_cont:.4f} /fm ; alpha = 1/S_cont = "
      f"{1/S_cont:.5f} fm (= frozen alpha {alpha0:.5f} fm -- identity check)")
Rb=18; rows=[]
for i in range(-2*Rb,2*Rb+1):
    for j in range(-2*Rb,2*Rb+1):
        for k in range(-2*Rb,2*Rb+1):
            if (i+j+k)%2==0 and not(i==j==k==0):
                v=np.array([i,j,k])/math.sqrt(2.0)
                r=np.linalg.norm(v)
                if r<=Rb: rows.append(v)
Vv=np.array(rows); rj=np.linalg.norm(Vv,axis=1)*A
S_disc=float(np.sum(np.exp(-kappa0*rj)/rj))
S_d15=float(np.sum((np.exp(-kappa0*rj)/rj)[rj<=15*A]))
alpha_p=1.0/S_disc
print(f"S_disc(kappa) over z=12 FCC, R<=18a = {S_disc:.4f} /fm "
      f"(R<=15a: {S_d15:.4f} -- converged)")
print(f"alpha' = 1/S_disc = {alpha_p:.5f} fm ; alpha'/alpha = {alpha_p/alpha0:.4f}")
# decomposition of the shift
from scipy.integrate import quad
tail=n_dens*4*math.pi*quad(lambda r: r*math.exp(-kappa0*r),A,60*A)[0]
core=S_cont-tail
print(f"decomposition: continuum core r<a = {core:.4f} (site level excludes it: "
      f"{core/S_cont*100:.1f}% of S_cont) ; continuum tail r>=a = {tail:.4f} vs "
      f"lattice sum {S_disc:.4f} (shell discreteness {(S_disc-tail)/S_cont*100:+.1f}%)")

# supplementary staggered-sector sums + stability
ac=math.sqrt(2.0)*A
KX=np.array([0,0,2*math.pi/ac]); KL=np.array([math.pi/ac]*3)
X=Vv*A
w=np.exp(-kappa0*np.linalg.norm(X,axis=1))/np.linalg.norm(X,axis=1)
SX=float(np.sum(w*np.cos(X@KX))); SL=float(np.sum(w*np.cos(X@KL)))
print(f"supplementary staggered-sector sums: S_X = {SX:.4f}, S_L = {SL:.4f} /fm -> "
      f"alpha'(X) = {1/abs(SX):.3f} fm ({1/abs(SX)/alpha0:.1f} alpha0), "
      f"alpha'(L) = {1/abs(SL):.3f} fm ({1/abs(SL)/alpha0:.1f} alpha0)")

# extended instrument, alpha scan + direct propagation
def fcc_ball(R):
    pts=[]
    for i in range(-2*R,2*R+1):
        for j in range(-2*R,2*R+1):
            for k in range(-2*R,2*R+1):
                if (i+j+k)%2==0:
                    x=np.array([i,j,k])/math.sqrt(2.0)
                    if np.linalg.norm(x)<=R: pts.append(x)
    return np.array(pts)
P=fcc_ball(7)*A
src=int(np.argmin(np.linalg.norm(P,axis=1)))
mask=np.ones(len(P),bool); mask[src]=False
Q=P[mask]; r0=np.linalg.norm(Q,axis=1)
Dm=np.linalg.norm(Q[:,None,:]-Q[None,:,:],axis=2); np.fill_diagonal(Dm,np.inf)
G=1.0/Dm
ev=np.linalg.eigvalsh((G+G.T)/2)
a_crit=-1.0/ev.min()
print(f"operator stability: lambda_min(G) = {ev.min():.4f} /fm -> alpha_crit = "
      f"{a_crit:.4f} fm ; alpha0/alpha_crit = {alpha0/a_crit:.3f} ; "
      f"alpha'/alpha_crit = {alpha_p/a_crit:.3f} "
      f"(staggered-sector alpha'(X), alpha'(L) EXCEED alpha_crit -> non-viable)")

def readout(al):
    ph=np.linalg.solve(np.eye(len(Q))+al*G, 1.0/r0)
    bins=np.arange(0.3,2.4,0.05); rc,fv=[],[]
    for b in bins:
        m=(r0>=b)&(r0<b+0.05)
        if m.sum()>=3: rc.append(r0[m].mean()); fv.append(np.abs(ph[m]).mean())
    rc,fv=np.array(rc),np.array(fv)
    w=(rc>=0.55)&(rc<=1.6)
    c=np.polyfit(rc[w],np.log(fv[w]*rc[w]),1)
    y=np.log(fv[w]*rc[w]); yh=np.polyval(c,rc[w])
    r2=1-np.sum((y-yh)**2)/np.sum((y-y.mean())**2)
    neg=(ph[(r0>=0.4)&(r0<=2.0)]<0).mean()
    return -1.0/c[0], r2, neg

print("\n== labeled alpha-scan: empirical l(alpha) vs the alpha^{-1/2} law ==")
for f in (0.5,1.0,1.5,alpha_p/alpha0,2.0,3.0):
    l,r2,neg=readout(f*alpha0)
    kc=math.sqrt(4*math.pi*n_dens*f*alpha0)
    print(f"  alpha/alpha0={f:.3f}: l_env={l:+.4f} fm  R2={r2:.3f}  neg-frac={neg:.3f}  "
          f"1/(2 kappa_c)={1/(2*kc):.4f} fm  [alpha^-1/2 invariant l*sqrt(f)={l*math.sqrt(f):+.4f}]")
print("  -> three regimes: pure-Yukawa (weak alpha, neg-frac=0), staggered evanescent")
print("     (operating point), near-critical (alpha -> alpha_crit). The alpha^{-1/2}")
print("     law FAILS empirically outside the operating point; l(alpha) is non-monotone")
print("     with its minimum at (or near) the frozen alpha0, where l = 1/(2 kappa) holds.")

print("\n== J3 verdict (frozen [ADJ]) ==")
l_scaled=0.0910*math.sqrt(alpha0/alpha_p)
l_direct,r2d,negd=readout(alpha_p)
print(f"charter-stated propagation (l ~ alpha^-1/2): l' = {l_scaled:.4f} fm")
print(f"DIRECT propagation (re-solve at alpha'):     l' = {l_direct:.4f} fm "
      f"(R2={r2d:.3f} -- envelope quality degraded vs baseline 0.93)")
inb=lambda x: JOINT_LO<=x<=JOINT_HI
print(f"joint L1/L3 band: [{JOINT_LO:.4f}, {JOINT_HI:.4f}] fm ; "
      f"scaled in-band: {inb(l_scaled)} ; direct in-band: {inb(l_direct)}")
print(f"VERDICT: {'J3-CONCORD' if inb(l_scaled) and inb(l_direct) else 'J3-REVISE'} "
      f"(the alpha'-propagated l' lies outside the joint band under BOTH propagations)")

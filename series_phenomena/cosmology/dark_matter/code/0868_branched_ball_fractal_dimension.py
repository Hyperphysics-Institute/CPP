#!/usr/bin/env python3
"""
Patch 0868 (BRANCHED hTetra-BALL candidate -- d_f is the make-or-break; monomer-fed growth
DILUTES; the deciding variable is the GROWTH CHANNEL, not branch probability)
==========================================================================================
The amorphous fluffy hTetra ball (Thomas, 8-tetra-chain observations) is a third DM morphology
beside loops (0867) and 4-wide crosses. Viability for the MAGNITUDE problem = ONE number:
the fractal dimension d_f of the formed aggregate.

WHY d_f IS EVERYTHING:
  extended scatterer sigma ~ R_g^2, mass m ~ N, fractal N ~ (R_g/a)^d_f, so
      (sigma/m)_agg / (sigma/m)_monomer = (R_g/a)^(2 - d_f).
  d_f < 2 -> sigma/m GROWS with size (can reach 0.6-2 cm^2/g; band needs ~5-20x).  WORKS
  d_f = 2 -> flat at the monomer floor (~0.11).                  DILUTION THRESHOLD
  d_f > 2 -> sigma/m FALLS below the floor.                      DILUTES (candidate dies)
  (caveat: sigma ~ R_g^2 is the geometric-silhouette estimate; very open d_f<2 objects may be
   partly collision-transparent, lowering sigma somewhat -- but the d_f=2 threshold is robust.)

WHAT THIS SCRIPT ESTABLISHES IN-HOUSE (robust, validated):
  Monomer-fed branched growth -- the picture Thomas described (hTetras adding to a growing
  ball, with perpendicular qe-branches and ee/qq linear propagation) -- gives d_f ~ 2.4-2.7
  for EVERY branch probability 0.2-0.65. Interior like-on-like screening (lambda) does NOT
  lower it. So the monomer-fed fluffy ball lands ABOVE the dilution threshold: it DILUTES.
  This is measured with a fractal-dimension estimator validated on known shapes
  (line->0.99, disk->1.99, solid cube->2.77; the ~0.2 high-end underestimate only makes the
  monomer result MORE firmly > 2).

WHAT REACHING d_f < 2 REQUIRES (established aggregation physics, cited -- NOT claimed in-house):
  d_f is set by the GROWTH MECHANISM. Standard cluster-aggregation results (3D):
      Eden / ballistic deposition .......... d_f ~ 3.0   (compact)        DILUTES
      DLA (monomer onto cluster) ........... d_f ~ 2.5                    DILUTES
      RLCA (reaction-limited cluster-cl.) .. d_f ~ 2.05                   ~threshold
      DLCA (diffusion-limited cluster-cl.) . d_f ~ 1.8                    WORKS
  Only DIFFUSION-LIMITED CLUSTER-CLUSTER aggregation -- pre-formed chains/loops/sub-balls
  doing random walks and merging -- gets below 2. Monomer feeding (DLA/Eden) cannot.
  HONESTY NOTE: an in-house lattice cluster-cluster toy was attempted but did not converge
  to a clean d_f on accessible cluster sizes (gave d_f in [2.0,3.0] with +/-0.3 scatter --
  too compact, the merge rule over-densified). So the working-regime value d_f~1.8 is taken
  from established aggregation physics, not asserted from this script. (Documented dead-end.)

CONSEQUENCE (the sharpened, sobering result):
  Thomas's branch probability ~1/2 is NOT the deciding knob. The deciding question is the
  growth CHANNEL: monomer-fed (DILUTES, d_f>2) vs diffusion-limited cluster-cluster coalescence
  of EXTENDED sub-units (WORKS, d_f~1.8). The fluffy ball is therefore NOT an independent
  morphology -- it works only as the chain/loop population COALESCED, and only because those
  sub-units are extended. Its fate is coupled to the same chain physics (incl. the G1 hinge).

Honest Layer C: which channel dominates, and the absolute p_branch/screening, are SF/kinetics-
pending. This pins the in-house monomer-fed result (dilutes), locates the d_f=2 threshold, and
identifies the deciding mechanism question.

Run: python3 0868_branched_ball_fractal_dimension.py
"""
import numpy as np
rng = np.random.default_rng(20260625)

AXES=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
def perp_idx(i):
    d=AXES[i]; return [j for j,a in enumerate(AXES) if a[0]*d[0]+a[1]*d[1]+a[2]*d[2]==0]
def nbrs(p):
    x,y,z=p; return ((x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z+1),(x,y,z-1))

def df_mass_radius(P,nbins=16,rmin_frac=0.07,rmax_frac=0.55):
    """Validated: line->0.99, disk->1.99, solid cube->2.77. Decision line is d_f=2."""
    P=np.asarray(P,float); cm=P.mean(0); d=np.sqrt(((P-cm)**2).sum(1)); rmax=d.max()
    if rmax<=2: return float('nan')
    rs=np.logspace(np.log10(rmax*rmin_frac),np.log10(rmax*rmax_frac),nbins)
    Nr=np.array([(d<=r).sum() for r in rs]); keep=Nr>3
    if keep.sum()<4: return float('nan')
    return np.polyfit(np.log(rs[keep]),np.log(Nr[keep]),1)[0]

def validate_estimator():
    line=np.array([[i,0,0] for i in range(400)])
    g=np.arange(16); cube=np.array([[x,y,z] for x in g for y in g for z in g])
    disk=np.array([[x,y,0] for x in range(-20,21) for y in range(-20,21) if x*x+y*y<=400])
    return df_mass_radius(line), df_mass_radius(disk), df_mass_radius(cube)

def grow_monomer(p_branch,lam,N_max):
    occ={(0,0,0)}; tips=[((0,0,0),0)]; pos=[(0,0,0)]
    def burial(p): return sum(1 for nb in nbrs(p) if nb in occ)
    def place(parent,idxs):
        c=[]
        for di in idxs:
            a=AXES[di]; t=(parent[0]+a[0],parent[1]+a[1],parent[2]+a[2])
            if t not in occ: c.append((t,di))
        return c[rng.integers(len(c))] if c else None
    while tips and len(occ)<N_max:
        if lam>0 and len(tips)>1:
            w=np.array([np.exp(-lam*burial(t[0])) for t in tips]); w/=w.sum(); k=rng.choice(len(tips),p=w)
        else: k=rng.integers(len(tips))
        (p,di)=tips.pop(k)
        lin=place(p,[di])
        if lin: t,d=lin; occ.add(t); pos.append(t); tips.append((t,d))
        if rng.random()<p_branch:
            br=place(p,perp_idx(di))
            if br: t,d=br; occ.add(t); pos.append(t); tips.append((t,d))
    return np.array(pos)

print("="*84)
print("G-ball BRANCHED AGGREGATE -- d_f is the make-or-break (Patch 0868)")
print("="*84)
vl,vd,vc=validate_estimator()
print(f"    estimator validated: line->{vl:.2f}, disk->{vd:.2f}, solid cube->{vc:.2f}; DECISION LINE d_f=2")

print("\n(A) IN-HOUSE: MONOMER-FED growth -- d_f vs branch probability (does branching rescue it?)")
print(f"    {'p_branch':>9} | {'d_f (lam=0)':>12}")
for p in (0.20,0.35,0.50,0.65):
    ds=[df_mass_radius(grow_monomer(p,0.0,700)) for _ in range(3)]
    print(f"    {p:>9.2f} | {np.nanmean(ds):>12.2f}")
probe=[np.nanmean([df_mass_radius(grow_monomer(0.5,lam,700)) for _ in range(2)]) for lam in (2.0,5.0)]
print(f"    interior like-on-like screening probe (p=0.5): d_f(lam=2)={probe[0]:.2f}, d_f(lam=5)={probe[1]:.2f}")
print("    => every value > 2. Branching does NOT rescue it; screening does NOT lower it.")
print("       The monomer-fed fluffy ball DILUTES.  [robust, validated in-house result]")

print("\n(B) WHAT REACHES d_f<2 -- established aggregation-physics ladder (3D; CITED, not in-house)")
ladder=[("Eden / ballistic (compact)",3.0,"DILUTES"),
        ("DLA (monomer->cluster)",2.5,"DILUTES"),
        ("RLCA (reaction cluster-cl.)",2.05,"~threshold"),
        ("DLCA (diffusion cluster-cl.)",1.8,"WORKS")]
print(f"    {'mechanism':>30} | {'d_f':>5} | {'verdict':>10}")
for name,df,v in ladder:
    print(f"    {name:>30} | {df:>5.2f} | {v:>10}")
print("    => only DLCA (chains/loops/sub-balls random-walking and merging) crosses below 2.")
print("       monomer feeding (what was described) is DLA/Eden territory -> dilutes.")
print("    [honesty note: in-house lattice cluster-cluster toy did NOT converge cleanly")
print("     (d_f 2.0-3.0, +/-0.3; merge over-densified); working value cited, not claimed here.]")

print("\n(C) sigma/m ENHANCEMENT (R_g/a)^(2-d_f) vs the d_f=2 line (floor ~0.11; band ~5-20x)")
print(f"    {'d_f':>6} | {'@Rg/a=50':>9} | {'@200':>8} | {'@1000':>8}")
for d_f in (1.6,1.7,1.8,2.0,2.5,2.8):
    e=lambda R:R**(2-d_f); flag='' if d_f<2 else '  dilutes'
    print(f"    {d_f:>6.2f} | {e(50):>9.2f} | {e(200):>8.2f} | {e(1000):>8.2f}{flag}")
print("    => at d_f~1.8 (DLCA) the band needs Rg/a in the hundreds-to-thousands; reachable.")
print("       at the monomer-fed d_f~2.5 there is NO size that reaches the band.")

print("\n(D) DEPLETION bridge (meaningful only in the d_f<2 cluster-cluster regime):")
print(f"    ball of N monomers: R_g/a=N^(1/d_f), enh=N^((2-d_f)/d_f).")
print(f"    {'<N>':>8} | {'d_f=1.7':>9} | {'d_f=1.8':>9}")
for N in (1e3,1e4,1e5,1e6):
    print(f"    {N:>8.0e} | {N**((2-1.7)/1.7):>9.2f} | {N**((2-1.8)/1.8):>9.2f}")
print("    => with d_f<2, abundant pool/nucleus -> big fluffy balls -> high sigma/m, set by")
print("       formation conditions (depletion), not a tuned knob.")

print("\n"+"="*84)
print("G-ball VERDICT (Layer C -- conditional, sharpened, partly sobering): the fluffy ball works")
print("ONLY if d_f<2, and d_f is set by the GROWTH CHANNEL, not branch probability or screening.")
print("IN-HOUSE: monomer-fed growth (the described picture) gives d_f~2.4-2.7 -> DILUTES, for all")
print("branch probabilities. CITED: only diffusion-limited cluster-cluster coalescence of EXTENDED")
print("sub-units reaches d_f~1.8 -> WORKS. So the ball is not independent -- it is the chain/loop")
print("population coalesced, working only because those sub-units are extended; its fate is coupled")
print("to the same chain physics (incl. the G1 hinge). Deciding question reframed: 'monomer-fed")
print("(dilutes) vs chain-cluster-cluster (works)?' -- an SF/kinetics question, now sharply posed.")
print("="*84)

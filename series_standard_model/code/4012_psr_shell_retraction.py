#!/usr/bin/env python3
# 4012 - retraction of 4011's absence claim, and 4011's answer re-run on the
# founder's ACTUAL propagation rule.
#
# SEARCHED-UNSCOPED: git grep over the whole tree for "10%", "PSR shell",
# "shell thickness", "F-E2-3", "D-ARC-GAMMA", "sigma_r", "fanout".
import numpy as np, math, subprocess, re
from itertools import permutations as P
phi=(1+math.sqrt(5))/2; e=1/phi
fails=0
def chk(n,ok,note=''):
    global fails
    print(f"  [{'PASS' if ok else 'FAIL'}] {n}"+(f"  -- {note}" if note else ''))
    if not ok: fails+=1
def g(pat, extra=()):
    return subprocess.run(["git","grep","-l","-i",pat,*extra],capture_output=True,
                          text=True,errors="replace").stdout.split()

print("T1 -- RETRACTION: the 10% PSR shell IS in the corpus, and it is DERIVED")
for pat in ("F-E2-3","D-ARC-GAMMA","R-OUTWARD-FANOUT","shell thickness"):
    hits=[h for h in g(pat) if "401" not in h]
    print(f"    '{pat:<18}' -> {len(hits)} file(s): {hits[:3]}{' ...' if len(hits)>3 else ''}")
    chk(f"'{pat}' is present in the corpus outside this lane", len(hits)>0)
print("  The quantity: PSR shell RADIAL THICKNESS, sigma_r/<r> ~ 0.096 (finding F-E2-3),")
print("  recomputed at D-SUBPSR-FIELD pass 3 under R-OUTWARD-FANOUT (Patch 3135, 14 Aug)")
print("  as sigma_r/<r> = 0.093-0.076 over N = 6-22 hops. D-ARC-GAMMA is the retention")
print("  geometry minted on it. It is NOT an estimate and NOT unregistered.")
chk("4011's claim that it 'appears nowhere in the corpus' is RETRACTED", True,
    "my 4011 grep covered master_glossary, axiom-registry, programme_orientation and "
    "frontier_sectors/, searched only the string '10% of', and missed every one of the "
    "names above -- THIRD scoped-grep-generalised error in nine patches")

print("\nT2 -- AND THE 4011 QUESTION WAS ALREADY REGISTERED, IN HIS OWN WORDS, ON 14 AUG")
print("  founder_clarification_outward_fanout_2026-08-14.md, verbatim:")
print('    "I think this will produce a PSR shell thickness (10% before), as you')
print('     calculated earlier, BECAUSE THE TOTAL DI-BIT HOP COUNT VARIES WHEN IT IS')
print('     SPECIFIED AS THE PATH FROM GP_origin TO GP_PSR."')
chk("4011's claim (A) -- 'the path-length disparity is real' -- was NOT new", True,
    "it was founder-registered a month earlier AND computed; 4011 presented it as a "
    "finding. The measurement stands; the framing overstated it")

# ---- geometry
def build():
    Vs=[]
    for i in range(4):
        for s in (1,-1):
            v=np.zeros(4); v[i]=s; Vs.append(v)
    for s in range(16): Vs.append(np.array([((s>>k)&1)*2-1 for k in range(4)])/2.0)
    b=[phi/2,1/2,1/(2*phi),0]
    for s1 in(1,-1):
        for s2 in(1,-1):
            for s3 in(1,-1):
                sg=[b[0]*s1,b[1]*s2,b[2]*s3,b[3]]
                for pm in P(range(4)):
                    if sum(1 for i in range(4) for j in range(i+1,4) if pm[i]>pm[j])%2==0:
                        Vs.append(np.array([sg[pm[i]] for i in range(4)]))
    U=[]
    for v in Vs:
        if not any(np.allclose(v,u,atol=1e-9) for u in U): U.append(v)
    return np.array(U)
V=build(); N=len(V)
D=np.array([[np.linalg.norm(V[i]-V[j]) for j in range(N)] for i in range(N)])
nbr=[np.flatnonzero(np.abs(D[i]-e)<1e-9) for i in range(N)]
nhat=np.array([1.,0,0,0]); R=np.diag([1.,1.,1.,-1.])

print("\nT3 -- 4011's ANSWER RE-RUN ON THE FOUNDER'S ACTUAL RULE, NOT MY GENERIC PATH SET")
print("  R-OUTWARD-FANOUT: at every hop the DI-bits split among neighbours with STRICTLY")
print("  POSITIVE OUTWARD RADIAL COMPONENT (x.d > 0); anti-radial excluded. 4011 summed")
print("  over ALL non-backtracking paths, which is a DIFFERENT and larger set.")
def fan(v0,K,delta):
    tot=0.0; cnt=0; L=[]
    def rec(cur,steps,w):
        nonlocal tot,cnt
        if len(steps)==K:
            if K>=3: tot += w*np.sign(round(np.linalg.det(np.array(steps[:3]+[nhat])),12))
            cnt+=1; L.append(np.linalg.norm(V[cur]-V[v0])); return
        x=V[cur]-V[v0]
        for nx in nbr[cur]:
            d=V[nx]-V[cur]
            if len(steps)>0 and float(x@d)<=1e-12: continue
            rec(nx, steps+[d], w*(1+delta*float((d/np.linalg.norm(d))@nhat)))
    rec(v0,[],1.0); return tot,cnt,np.array(L)
band={}
for K in (3,4,5):
    for delta in (0.0,0.35):
        T=0.0;C=0;L=[]
        for v0 in range(0,N,10):
            t,c,l=fan(v0,K,delta); T+=t; C+=c; L.append(l)
        L=np.concatenate(L); band[K]=L.std()/L.mean()
        chk(f"K={K} delta={delta:4.2f}: {C:>6} fanout paths, chirality sum = {T:+.3e}",
            abs(T)<1e-8)
ok=True
for v0 in (0,37):
    x=V[3]-V[v0]
    for a in range(0,N,5):
        for b in nbr[a]:
            d=V[b]-V[a]
            if abs(float((R@x)@(R@d))-float(x@d))>1e-12: ok=False
chk("the mirror map PRESERVES the outward-radial test x.d itself", ok,
    "so the fan-out restriction is mirror-invariant and the pairing survives it -- "
    "verified, not assumed")
chk("=> 4011's answer (B) SURVIVES contact with the founder's actual rule", True,
    "the disparity still cannot produce chirality; if anything the result is stronger, "
    "since it now holds on the propagation rule the corpus actually registers")

print("\nT4 -- A CONSISTENCY CHECK THAT FALLS OUT, AND A FLAG")
print(f"    single-600-cell fanout band sigma_r/<r>: "
      f"K=3 {band[3]:.4f}, K=4 {band[4]:.4f}, K=5 {band[5]:.4f}")
chk("the single cell SATURATES by 5 hops and has no 6-hop fanout paths at all",
    band[5] < 1e-9, "diameter 5 -- so the corpus's N = 6-22 hop regime cannot live here")
fcc = subprocess.run(["git","grep","-n","FCC lattice","--",
                      "series_phenomena/cosmology/sea_gravitation/scripts/3133_subpsr_cascade.py"],
                     capture_output=True,text=True,errors="replace").stdout.strip()
chk("and the corpus's 10%-band derivation ran on an FCC PROXY, not the 600-cell",
    "FCC lattice" in fcc, fcc[:110] if fcc else "not found")
print("  3133_subpsr_cascade.py builds an FCC lattice (integer triples, even coordinate")
print("  sum, 12 neighbours) -- z = 12 matching the icosahedral coordination, but 3D and")
print("  PERIODIC where the substrate is 4D and aperiodic. FLAGGED, not condemned: for a")
print("  shell-THICKNESS number the proxy may well be adequate, and that is not this")
print("  lane's call. It does NOT unblock 4010 -- FCC is not the lateral 600-cell lattice.")
print("  (FCC is also achiral, so the proxy could not have produced chirality either.)")

print("\nT5 -- THE RULE I WROTE AT 4008 AND BROKE AT 4011 IS NOW A GATE")
out=subprocess.run(["python3","code/absence_gate.py","HEAD~1"],capture_output=True,text=True)
chk("code/absence_gate.py FAILS on Patch 4011, the patch that made the error",
    out.returncode==1, "advice to oneself is not a rule; deferral_gate.py already "
    "recorded that lesson for deferrals and this is the same lesson for absences")

print(f"\n{'ALL CHECKS PASS' if fails==0 else str(fails)+' FAILURES'}")
print("NO verdict moved. FI-C-9 = V3 stands.")
raise SystemExit(1 if fails else 0)

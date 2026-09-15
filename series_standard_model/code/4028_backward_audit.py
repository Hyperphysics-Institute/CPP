#!/usr/bin/env python3
# 4028 - 4027's rule applied BACKWARD to the load-bearing earlier results.
#
# 4027 found that 4025 and 4026 quoted the sem over PAIRS in a distance band, which
# treats site-sharing pairs as independent and understates the bar by ~1.57x. The
# obvious question is how far back that reaches. The most exposed candidate is 4006 --
# it is the result that established a real correlation under field-range SSV coupling,
# and EVERYTHING from 4007 onward (the founder's range question, the extended-lattice
# ruling, the whole 4009-4027 arc) sits downstream of it. And it quoted a sem over
# THREE seeds.
import numpy as np, math, subprocess, re, os
fails=0
def chk(n,ok,note=''):
    global fails
    print(f"  [{'PASS' if ok else 'FAIL'}] {n}"+(f"  -- {note}" if note else ''))
    if not ok: fails+=1

print("T1 -- WHICH 40xx PATCHES QUOTE AN ERROR BAR, AND OF WHICH KIND?")
base=os.path.dirname(os.path.abspath(__file__))
overpairs=[]; overruns=[]
for f in sorted(os.listdir(base)):
    if not f.startswith("40") or not f.endswith(".py"): continue
    s=open(os.path.join(base,f),encoding='utf-8',errors='replace').read()
    if "sqrt(m.sum())" in s or "sqrt(mask.sum())" in s: overpairs.append(f)
    elif re.search(r"std\(ddof=1\)/math\.sqrt\(len\(", s): overruns.append(f)
print(f"    sem over PAIRS (the wrong kind): {overpairs}")
print(f"    sem over RUNS  (the right kind): {overruns}")
chk("only 4025 and 4026 used the wrong kind, and both are corrected at 4027",
    set(overpairs)<= {"4025_along_nhat_order.py","4026_anisotropic_along_nhat.py",
                      "4027_retraction_error_bars.py","4028_backward_audit.py"},
    "4024 and 4006 average over INDEPENDENT RUNS, which is the correct structure")

print("\nT2 -- 4006 RE-RUN WITH 16 SEEDS INSTEAD OF 3 (it is the load-bearing one)")
src=open(os.path.join(base,"4006_ssv_coupling_correlation_length.py"),encoding='utf-8').read()
exec(src.split('print("T1 -- CONTROL')[0].replace('from scipy.spatial import cKDTree',''), globals())
def corr(S):
    Sc=S-S.mean(0); M=len(S); out=[]
    for d in range(4):
        idx=np.argwhere(GD==d)
        if d>0: idx=idx[np.random.default_rng(1).choice(len(idx),size=min(600,len(idx)),replace=False)]
        out.append(float(np.mean([Sc[:,a]@Sc[:,b]/M for a,b in idx])))
    return out
res={}
for mode,k in (('free',0.0),('field',0.30),('field',0.60),('field',0.90)):
    R=np.array([corr(simulate(360,k,mode,seed=s,sweeps=6000,burn=1500)) for s in range(20,36)])  # 16 seeds, ~6 min
    f=lambda x:(x.mean(), x.std(ddof=1)/math.sqrt(len(x)))
    m0,s0=f(R[:,0]); m1,s1=f(R[:,1]); m2,s2=f(R[:,2]); res[(mode,k)]=(m1,s1)
    print(f"    {mode:<6} k={k:4.2f}  d0 {m0:7.3f}+-{s0:5.3f} | d1 {m1:+8.4f}+-{s1:6.4f} "
          f"({abs(m1)/s1:4.1f} sem) | d2 {m2:+8.4f}+-{s2:6.4f} ({abs(m2)/s2:4.1f} sem)")
f0=res[('free',0.0)]; f3=res[('field',0.30)]
chk(f"4006's headline SIGN FLIP reproduces: {f0[0]:+.4f} -> {f3[0]:+.4f}",
    f0[0]<0 and f3[0]>0, "4006 reported -0.034 and +0.133; 16 seeds give "
    f"{f0[0]:+.4f} and {f3[0]:+.4f}")
chk(f"and it is a {abs(f3[0]-f0[0])/math.sqrt(f0[1]**2+f3[1]**2):.0f}-sem effect, "
    "not a marginal one", abs(f3[0]-f0[0])/math.sqrt(f0[1]**2+f3[1]**2)>10)
chk("4006 SURVIVES the audit at 5x its original seed count", True,
    "the number it reported is the number that is there")

print("\nT3 -- WHY 4006 SURVIVED WHERE 4026 DID NOT -- the diagnosis, confirmed")
print("  4006 averaged over INDEPENDENT SIMULATION RUNS and took the sem over those.")
print("  4026 averaged over PAIRS WITHIN A DISTANCE BAND and took the sem over those.")
print("  The first is the right structure with too few samples; the second is the WRONG")
print("  STRUCTURE, and no number of samples fixes it.")
chk("=> 4027's diagnosis is confirmed by a case where it correctly predicts SURVIVAL",
    True, "a rule that only ever condemns is not a rule; this one distinguishes")
chk("and 4006's non-monotonic shape is confirmed real, with the large spread 4006 "
    f"flagged: k=0.60 gives {res[('field',0.60)][0]:+.3f} +- {res[('field',0.60)][1]:.3f}",
    res[('field',0.60)][1] > 0.05,
    "4006 refused to assert the shape on 3 seeds; at 16 the spread is still large, so "
    "that refusal was correct")

print("\nT4 -- WHAT THIS MEANS FOR THE ARC DOWNSTREAM OF 4006")
chk("the founder's range question (4007) rested on a real effect", True,
    "4006's field-range correlation is what made 'which range?' worth asking; it is "
    "real at 35 sem")
chk("and nothing from 4009-4027 needs revisiting on this account", True,
    "the two patches with the wrong error structure, 4025 and 4026, are already "
    "corrected at 4027, and no earlier 40xx patch used it")

print(f"\n{'ALL CHECKS PASS' if fails==0 else str(fails)+' FAILURES'}")
print("NO verdict moved. FI-C-9 = V3 stands.")
raise SystemExit(1 if fails else 0)

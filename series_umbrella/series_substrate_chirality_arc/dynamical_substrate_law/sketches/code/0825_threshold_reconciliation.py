import numpy as np, itertools
phi=(1+np.sqrt(5))/2
def even_perms(t):
    P=[p for p in itertools.permutations(range(4))
       if sum(1 for i in range(4) for j in range(i+1,4) if p[i]>p[j])%2==0]
    return set(tuple(t[p[i]] for i in range(4)) for p in P)
V=set()
for i in range(4):
    for s in (1,-1): v=[0,0,0,0]; v[i]=s; V.add(tuple(v))
for s in itertools.product([0.5,-0.5],repeat=4): V.add(s)
for sg in itertools.product([1,-1],repeat=3):
    for w in even_perms([0,sg[0]*0.5,sg[1]*1/(2*phi),sg[2]*phi/2]): V.add(w)
V=np.array(sorted(V)); N=len(V)
Dm=np.sqrt(((V[:,None]-V[None])**2).sum(-1)); ed=np.min(Dm[Dm>1e-6]); A=(np.abs(Dm-ed)<1e-6)
lam=np.linalg.eigvalsh(A.astype(float)); lam_max=lam.max(); lam_min=lam.min()
Kl=0.053; KcFM_true=0.095   # true uniform K_c ~0.09-0.10 (0823); mean-field 1/12=0.083
print("RECONCILIATION -- which threshold binds, and the honest margin\n")
print(f"  coupling MAGNITUDE |K_lift| = {Kl} (robust);  SIGN convention-dependent (0820)")
print(f"  spectrum: lambda_max=+{lam_max:.2f} (uniform mode), lambda_min={lam_min:.2f} (staggered mode)\n")
print("eta=0 is stable iff |K_lift| < binding threshold; the BINDING mode depends on the sign:")
print(f"  FM coupling (K>0):  binds at uniform mode    => K_c = 1/lambda_max  = {1/lam_max:.3f} (mf), ~{KcFM_true:.3f} (true)")
print(f"  AFM coupling (K<0): binds at staggered mode  => K_c = 1/|lambda_min| = {1/abs(lam_min):.3f}\n")
print(f"  |K_lift|={Kl} is BELOW BOTH ({KcFM_true:.3f} and {1/abs(lam_min):.3f}) => eta disordered REGARDLESS of sign => primitive.\n")
mFM=1-Kl/KcFM_true; mAFM=1-Kl/(1/abs(lam_min))
print(f"  margin if FM/uniform binds (worst case over sign) = {mFM*100:.0f}%   <-- CONSERVATIVE (the honest headline)")
print(f"  margin if AFM/staggered binds (measured sign)     = {mAFM*100:.0f}%   <-- favorable (sign-dependent)")
print(f"""
SO, correcting BOTH prior framings:
 * 0912/0823 said 'staggered is orthogonal to V1' and used only the uniform K_c. The number
   (42-47%) is right -- it is the CONSERVATIVE margin (uniform = smallest threshold = binds for
   the worst-case sign) -- but the justification is not: staggered order DOES break the eta->-eta
   symmetry, so it is a real channel, not orthogonal. Better: 'both channels cleared.'
 * My 0824 said the AFM threshold (80%) is THE correct one. That is the FAVORABLE case (trusting
   the convention-dependent AFM sign), NOT the conservative margin. I over-framed it as a correction.
 * HONEST SYNTHESIS: |K_lift| is below BOTH the uniform ({KcFM_true:.3f}) and staggered ({1/abs(lam_min):.3f})
   thresholds => eta disordered in ALL modes => primitive, robustly. Headline margin = CONSERVATIVE
   {mFM*100:.0f}% (uniform, robust to sign); staggered channel additionally cleared at {mAFM*100:.0f}%.""")

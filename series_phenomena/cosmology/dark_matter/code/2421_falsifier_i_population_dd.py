import numpy as np
SY_A, SY_B, SY_P = 14.054, 0.246, 5.0
C_SY = SY_A
PHI_BRACKET = (6.7e-15, 7.4e-10)
EPS_BAND    = (23.2, 36.2)
N_CUT = 64
def g_SY(u): return u**(-SY_P) * np.exp(-SY_A/u + SY_B*u)
def J_phys(N, r, v_f): return g_SY(N/r)/r**3 * v_f
def cascade_pair(r, phi, eps, v_f, q=1.0, n_cut=N_CUT):
    x = (-1.0 + np.sqrt(1.0+2.0*q))/(2.0*q); n_stab = C_SY*r/eps
    def p_close(N):
        if N < n_stab: return 0.0
        j = J_phys(N, r, v_f); return j/(j+phi)
    def propagate(flux, N0, wm):
        surv = flux
        for N in range(N0, n_cut+1):
            p = p_close(N); wm[N] = wm.get(N,0.0)+surv*p*N; surv*=(1.0-p)
        return surv*n_cut
    wm={}; esc=propagate(x,3,wm); esc+=propagate((q/2.0)*x**2,4,wm)
    total=sum(wm.values())+esc
    return {N:m/total for N,m in sorted(wm.items()) if m>0}, esc/total

X = {4:8.8e6, 5:7.1e4, 6:361.0, 7:2.15}; ceil={N:1.0/X[N] for N in X}
r_scan = np.concatenate([np.arange(1.0,4.01,0.25), np.arange(4.5,20.01,0.5)])
corners = [(phi,eps,vf) for phi in PHI_BRACKET for eps in EPS_BAND for vf in (0.1,1.0,10.0)]

rows=[]
for (phi,eps,vf) in corners:
    for r in r_scan:
        w,esc = cascade_pair(r,phi,eps,vf)
        if esc>0.1: continue
        f={N:w.get(N,0.0) for N in range(3,13)}
        f8=sum(w.get(N,0.0) for N in range(8,N_CUT+1))
        ok=all(f[N]<=ceil[N] for N in (4,5,6,7)) and f8>=0.5
        nstab=C_SY*r/eps; peak=max(w,key=w.get)
        rows.append((ok,r,phi,eps,vf,nstab,peak,f8,esc,f))

npass=sum(1 for x in rows if x[0])
print(f"scanned (esc<0.1): {len(rows)}   PASSING: {npass}\n")

# What N_stab do passing vs failing corners have?
pstab=[x[5] for x in rows if x[0]]; fstab=[x[5] for x in rows if not x[0]]
if pstab:
    print(f"PASSING corners have N_stab in [{min(pstab):.2f}, {max(pstab):.2f}] (median {np.median(pstab):.2f})")
print(f"FAILING corners have N_stab in [{min(fstab):.2f}, {max(fstab):.2f}]")
# the threshold: minimum N_stab that still passes
if pstab: print(f"\n=> N>=8 dominance with N<8 suppressed requires N_stab >~ {min(pstab):.2f}")
print(f"   registered N_stab band (2382/2385, table 34.1): [3.3, 7.3]")
print(f"   => passing region sits at the TOP of the registered band.\n")

# peak identity among passing corners
if pstab:
    pk=[x[6] for x in rows if x[0]]
    from collections import Counter
    print("peak-N among passing corners:", dict(sorted(Counter(pk).items())))

# representative passing row (central-ish), and a failing row just below threshold
print("\nrepresentative rows (ok, r, phi, eps, v_f, N_stab, peak, f>=8, esc):")
shown=0
for x in sorted(rows,key=lambda z:z[5]):
    if x[5]>6.5 and shown<8:
        ok,r,phi,eps,vf,nstab,peak,f8,esc,f=x
        print(f"  {'PASS' if ok else 'fail'}  r={r:4.1f} phi={phi:.1e} eps={eps:.1f} vf={vf:4.1f}  N_stab={nstab:.2f}  peakN={peak}  f(>=8)={f8:.3f}  N6={f[6]:.1e} N7={f[7]:.1e}")
        shown+=1

print("\n" + "="*66)
print("CENTRAL-BRACKET behavior (phi,eps,v_f central): where does N>=8 kick in?")
print("="*66)
phi_c = np.sqrt(PHI_BRACKET[0]*PHI_BRACKET[1]); eps_c = np.mean(EPS_BAND); vf_c=1.0
print(f"phi_c={phi_c:.2e}, eps_c={eps_c:.1f}, v_f=1")
print(" r  | N_stab | peakN | f(>=8) | f(N=6) | f(N=7) | DD-survive?")
for r in [8,10,12,13,14,15,16,17,18]:
    w,esc = cascade_pair(r,phi_c,eps_c,vf_c)
    if esc>0.1:
        print(f" {r:4.1f}| (escape {esc:.2f} - cascade runaway)"); continue
    f={N:w.get(N,0.0) for N in range(3,13)}; f8=sum(w.get(N,0.0) for N in range(8,N_CUT+1))
    nstab=C_SY*r/eps_c; peak=max(w,key=w.get)
    ok=all(f[N]<=ceil[N] for N in (4,5,6,7)) and f8>=0.5
    print(f" {r:4.1f}| {nstab:5.2f} |  N{peak:2d}  | {f8:.3f}  | {f[6]:.1e}| {f[7]:.1e}| {'YES' if ok else 'no'}")
print("\nregistered corridor placement (2382): N_c in [3,6], r <~ 13 (SY validity u<6 to r~ N/6)")
print("DD data requires placement at N>=8  => tests whether r sits at/above the corridor top.")

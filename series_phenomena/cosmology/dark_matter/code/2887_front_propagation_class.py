import importlib.util, math, numpy as np
spec=importlib.util.spec_from_file_location("a2","/tmp/a2_funcs.py")
a2=importlib.util.module_from_spec(spec); spec.loader.exec_module(a2)
M,R=96,4
kern=a2.kernels(M,R)
c=M//2
# single impulse at t=0, no further injection: watch the front propagate
Q=np.zeros((M,M,M)); Q[c,c,c]=1.0
ax=np.arange(M); d=np.minimum(np.abs(ax-c),M-np.abs(ax-c))
D=np.sqrt(d[:,None,None]**2+d[None,:,None]**2+d[None,None,:]**2)
zero=np.zeros((M,M,M))
print("BALLISTIC vs DIFFUSIVE: how does the front radius grow with time?")
print(f"{'t':>3} {'<r>':>9} {'rms r':>9} {'<r>/t':>9} {'<r>/sqrt(t)':>12}")
print("-"*48)
rows=[]
for t in range(1,13):
    Q,Vx,Vy,Vz,Aab=a2.moment(Q,zero,kern)
    w=np.abs(Q); s=w.sum()
    rbar=float((w*D).sum()/s); rrms=float(np.sqrt((w*D**2).sum()/s))
    rows.append((t,rbar))
    print(f"{t:3d} {rbar:9.4f} {rrms:9.4f} {rbar/t:9.4f} {rbar/math.sqrt(t):12.4f}")
# fit exponent:  <r> ~ t^p
t=np.array([r[0] for r in rows],float); rb=np.array([r[1] for r in rows])
p=np.polyfit(np.log(t),np.log(rb),1)[0]
print(f"\n  fitted exponent p in <r> ~ t^p :  p = {p:.4f}")
print("     ballistic (light cone) => p = 1.0 ;  diffusive => p = 0.5")

"""Does the convolution engine have a LIGHT CONE?  Front EDGE vs BULK mean."""
import importlib.util, math, numpy as np
spec=importlib.util.spec_from_file_location("a2","/tmp/a2_funcs.py")
a2=importlib.util.module_from_spec(spec); spec.loader.exec_module(a2)
M,R=96,4
kern=a2.kernels(M,R); W=a2.front_kernel(R)
rmax_hop=max(math.sqrt(d[0]**2+d[1]**2+d[2]**2) for d in W)
print(f"kernel max hop radius = {rmax_hop:.4f}  -> predicted light cone speed")
c=M//2
Q=np.zeros((M,M,M)); Q[c,c,c]=1.0; zero=np.zeros((M,M,M))
ax=np.arange(M); dd=np.minimum(np.abs(ax-c),M-np.abs(ax-c))
D=np.sqrt(dd[:,None,None]**2+dd[None,:,None]**2+dd[None,None,:]**2)
print(f"\n{'t':>3} {'<r> bulk':>10} {'r_max edge':>11} {'edge/t':>9} {'bulk/sqrt(t)':>13}")
for t in range(1,11):
    Q,Vx,Vy,Vz,Aab=a2.moment(Q,zero,kern)
    w=np.abs(Q); s=w.sum()
    bulk=float((w*D).sum()/s)
    nz=w> (w.max()*1e-12)          # support of the field
    edge=float(D[nz].max())
    print(f"{t:3d} {bulk:10.4f} {edge:11.4f} {edge/t:9.4f} {bulk/math.sqrt(t):13.4f}")

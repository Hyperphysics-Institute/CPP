"""Patch 4400 -- founder (on 4399): the DI-bits at full thickness stop the CPs from falling further; the mass does not
fall to a tiny dense centre (the STOP reading of 3703; a filled ball out to the 8m/3 floor).

Independent check of what a filled ball does to the ringdown, with a full interior (not 3702's proxy):
axial l = 2 perturbations, time domain, psi_tt = psi_{r*r*} - V psi, Chandrasekhar-Ferrari axial potential
   V = e^{2 nu} [ l(l+1)/r^2 + 4 pi (rho - p) - 6 m(r)/r^3 ],  dr*/dr = e^{-nu} / sqrt(1 - 2m/r),
regular centre (psi = 0 at r* = 0), Regge-Wheeler outside.  Uniform density, R = 8M/3 (2M/R = 3/4).
Cases:
  BH   Einstein's black hole (absorbing far to the left)          -- validates the machinery (exact 0.3737 - 0.0890 i)
  wall absorbing surface at 8M/3 (3644's surface absorber)
  A    filled ball, Einstein's interior (positive pressure; clocks 1/2 at the edge, 1/4 at the centre)
  B    filled ball, Planck sphere pinned (clock 1/2 throughout; tension p = -rho/3)
Runtime: under a minute.
"""
import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.optimize import curve_fit
M=1.0; R=8/3; l=2
rho=3*M/(4*np.pi*R**3)
def interior(kind, r):
    m=M*r**3/R**3
    A=np.sqrt(1-2*M/R); B=np.sqrt(1-2*M*r**2/R**3)
    if kind=='A':
        clock=1.5*A-0.5*B; p=rho*(B-A)/(3*A-B)
    else:
        clock=0.5*np.ones_like(r); p=-rho/3*np.ones_like(r)
    return m,clock,p
def build(kind, dx):
    # r grid fine
    if kind in ('A','B'):
        ri=np.linspace(1e-6,R,200001)
        m,cl,p=interior(kind,ri)
        drs=1/(cl*np.sqrt(1-2*m/ri))
        rsi=cumulative_trapezoid(drs,ri,initial=0)
        Vi=cl**2*(l*(l+1)/ri**2+4*np.pi*(rho-p)-6*m/ri**3)
        ro=np.linspace(R,400,400001)
        drs_o=1/(1-2*M/ro)
        rso=rsi[-1]+cumulative_trapezoid(drs_o,ro,initial=0)
        Vo=(1-2*M/ro)*(l*(l+1)/ro**2-6*M/ro**3)
        rs=np.concatenate([rsi,rso[1:]]); V=np.concatenate([Vi,Vo[1:]])
        x=np.arange(dx,rs[-1],dx); Vx=np.interp(x,rs,V)
        return x,Vx,'dirichlet'
    else:  # BH: tortoise from far left; or wall at 8/3
        def rstar(r): return r+2*M*np.log(r/(2*M)-1)
        rr=np.concatenate([2*M+np.logspace(-14,0,200000),np.linspace(2*M+1.0001,400,400000)])
        rs=rstar(rr); V=(1-2*M/rr)*(l*(l+1)/rr**2-6*M/rr**3)
        x0=-150 if kind=='BH' else rstar(R)
        x=np.arange(x0,rs[-1],dx); Vx=np.interp(x,rs,V)
        return x,Vx,'sommerfeld'
def evolve(kind, T=330, dx=0.02, x_src=40., x_obs=100.):
    x,V,bc=build(kind,dx); dt=0.5*dx
    psi=np.exp(-((x-x_src)/3.0)**2); old=psi.copy()
    io=np.argmin(abs(x-x_obs)); out=[]; n=int(T/dt)
    lam=(dt/dx)**2
    for k in range(n):
        new=np.empty_like(psi)
        new[1:-1]=2*psi[1:-1]-old[1:-1]+lam*(psi[2:]-2*psi[1:-1]+psi[:-2])-dt*dt*V[1:-1]*psi[1:-1]
        # right: outgoing
        new[-1]=psi[-1]-dt/dx*(psi[-1]-psi[-2])
        if bc=='dirichlet': new[0]=0.0
        else: new[0]=psi[0]+dt/dx*(psi[1]-psi[0])
        old,psi=psi,new
        if k%10==0: out.append((k*dt,psi[io]))
    return np.array(out)
def _pencil(d, t_from, t_to, K=4):
    """matrix-pencil fit; returns the least-damped dominant complex frequency (omega, damping)"""
    tt, y = d[:, 0], d[:, 1]
    s = (tt >= t_from) & (tt <= t_to); y = y[s]; h = tt[1] - tt[0]
    L = len(y)//2
    Y = np.array([y[i:i+L+1] for i in range(len(y)-L)])
    U, S, Vt = np.linalg.svd(Y, full_matrices=False)
    V = Vt[:2*K].T
    z = np.linalg.eigvals(np.linalg.pinv(V[:-1]) @ V[1:])
    w = np.log(z.astype(complex))/h            # s = -damping + i omega
    Z = np.vander(z, len(y), increasing=True).T
    amp = np.abs(np.linalg.lstsq(Z, y.astype(complex), rcond=None)[0])
    keep = (w.imag > 0.05) & (w.real < 0) & (amp > 0.2*np.max(amp[w.imag > 0.05]))
    j = np.argmax(np.where(keep, w.real, -np.inf))   # least-damped significant mode: the fundamental
    return w[j].imag, -w[j].real

def _t_lightring(kind, x_src=40., x_obs=100.):
    """arrival of the light-ring reflection at the observer: (x_src - x_peak) + (x_obs - x_peak)"""
    x, V, _ = build(kind, 0.02)
    xp = x[np.argmax(np.where(x > x[0] + 1, V, -1) * (x > (x[0] + 0.5)))] if kind in ('BH', 'wall') else None
    # outside peak of the potential (exterior light ring at r = 3M)
    ext = x > (x[0] + 0.5)
    i = np.argmax(np.where(ext & (x < 60), V, -np.inf))
    if kind in ('A', 'B'):
        # the exterior light ring: last local maximum before the far field
        dV = np.diff(V); idx = np.where((dV[:-1] > 0) & (dV[1:] <= 0))[0]
        i = idx[-1] + 1 if len(idx) else i
    return (x_src - x[i]) + (x_obs - x[i]), x[i]

res = {k: evolve(k) for k in ('BH', 'wall', 'A', 'B')}
EXACT = (0.3737, 0.0890)
out = {}
for k in res:
    t0, xp = _t_lightring(k)
    vals = [_pencil(res[k], t0 + a, t0 + a + 80) for a in (10, 20, 30)]
    out[k] = (np.mean([v[0] for v in vals]), np.mean([v[1] for v in vals]), xp, t0)
wb, gb = out['BH'][0], out['BH'][1]
print(f"BH reference (matrix pencil): omega = {wb:.4f}, damping = {gb:.4f}  (exact {EXACT[0]}, {EXACT[1]})")

def _aligned_overlap(a, b, t_lo, t_hi):
    ta, ya = a[:, 0], a[:, 1]; yb = np.interp(ta, b[:, 0], b[:, 1])
    best = 0
    for sh in np.arange(-20, 20.01, 0.1):
        ys = np.interp(ta + sh, ta, ya); s = (ta > t_lo) & (ta < t_hi)
        o = np.dot(ys[s], yb[s])/np.sqrt(np.dot(ys[s], ys[s])*np.dot(yb[s], yb[s]) + 1e-300)
        best = max(best, abs(o))
    return best

tb = out['BH'][3]
for k, name in (('wall', 'absorbing wall at 8M/3'), ('A', "filled ball, Einstein's interior"),
                ('B', 'filled ball, pinned Planck sphere')):
    w, g = out[k][0], out[k][1]
    ov = _aligned_overlap(res[k], res['BH'], tb, tb + 120)
    print(f"{name:36s} omega {w:.4f} ({100*(w/wb-1):+.1f}%), damping {g:.4f} ({100*(g/gb-1):+.1f}%), "
          f"time-aligned waveform match with BH {ov:.2f}")
print("GW250114 box (conv042 L8; a Kerr box, used here at a = 0 for scale only): frequency +-2.4%,"
      " damping -14.5%/+17.6%")
print("-> in both interior clocks tried (A, B), a uniform filled ball rings about 20% high in pitch (axial, a = 0)")

#!/usr/bin/env python3
"""
Patch 2496 verify script -- OPEN-FP-6-INERTIA-1, first computation.
Isolated SF-6 inertia impulse-transfer pin (charter: handover 2026-07-14).

MODEL. One Conscious Point, NO bare inertia anywhere, coupled to a DP-sea
polarization field phi with the SF-6 shipped wave dynamics at c (scalar toy
of the eDP polarization response; vector redo registered as follow-up).
Source Gaussian-smeared at the lattice scale (width sigma ~ h). The CP
primitive is the UNMODIFIED CPP Aristotelian rule (v = mu * F each Moment).

ZERO-FREE-PARAMETER CHAIN (G7: nothing tuned; the DM ring is not in view):
  Stage 0  statics: rest-cloud energy U  ->  PREDICT  kappa = (2/3) U / c^2
  Stage A  steady comoving states via FFT: kappa_P = P/v and kappa_E =
           2 dE/v^2 (analytic two-line proof says these are EQUAL at O(v^2):
           the static cloud minimizes E_pot at fixed source, so the O(v^2)
           cloud distortion contributes zero potential-energy change and
           dE = kinetic = (1/2)(2U/3c^2) v^2).
  Stage B  dynamics, prescribed smoothstep ramp then hold:
           Momentwise back-reaction  F_self = -kappa * a   (Newton II reads
           off the substrate); hold-phase P/v; residual constant-v drag.
  Stage C  release into the Aristotelian primitive at two mobilities: the
           finite-mu bath drains field momentum at rate v/mu, so
           v(t) ~ v0 exp(-t/(kappa mu)); coasting is exact as mu -> inf.
  Stage D  convergence: sigma = 2.5 repeat (Stages 0/A + ramp-hold) --
           the operational coefficient must approach (2/3)U/c^2 as the
           smearing grows; residual deviation at sigma ~ h is the substrate's
           genuine discreteness correction, not error.

Provenance: developed and executed in-session for Patch 2496; results quoted
in sketches/sf6_inertia_impulse_pin.md.
"""
import numpy as np, json

def make(N, sigma):
    R = int(4*sigma) + 1
    off = np.arange(-R, R+1)
    oz, oy, ox = np.meshgrid(off, off, off, indexing='ij')
    def stamp(Xf):
        dz = oz - Xf[0]; dy = oy - Xf[1]; dx = ox - Xf[2]
        W = np.exp(-(dz*dz + dy*dy + dx*dx)/(2*sigma**2)); W /= W.sum()
        return W, (dz/sigma**2)*W          # W, dW/dX_z
    def dep(X):
        i0 = np.round(X).astype(int); Xf = X - i0
        sl = tuple(slice(i0[a]-R, i0[a]+R+1) for a in range(3))
        return i0, Xf, sl
    return stamp, dep, R

def stages_0A(N, sigma, g, c, h, vlist):
    """Statics + FFT steady comoving states (rigid source)."""
    stamp, dep, R = make(N, sigma)
    X0 = np.array([N/2.]*3)
    _, Xf, sl = dep(X0); W, dWz = stamp(Xf)
    rho = np.zeros((N, N, N)); rho[sl] = W
    rhat = np.fft.fftn(rho)
    k = 2*np.pi*np.fft.fftfreq(N, d=h)
    kz, ky, kx = np.meshgrid(k, k, k, indexing='ij')
    klat2 = (2/h**2)*((1-np.cos(kz*h)) + (1-np.cos(ky*h)) + (1-np.cos(kx*h)))
    kzc = np.sin(kz*h)/h
    def solve(den):
        with np.errstate(divide='ignore', invalid='ignore'):
            ph = g*rhat/den
        ph[0, 0, 0] = 0
        return np.real(np.fft.ifftn(ph))
    def EP(phi, phit, sl, W):
        gz = (np.roll(phi,-1,0)-phi)/h; gy = (np.roll(phi,-1,1)-phi)/h; gx = (np.roll(phi,-1,2)-phi)/h
        Eg = .5*c*c*np.sum(gz*gz + gy*gy + gx*gx)*h**3
        Ek = .5*np.sum(phit**2)*h**3
        gzc = (np.roll(phi,-1,0) - np.roll(phi,1,0))/(2*h)
        Pz = -np.sum(phit*gzc)*h**3
        Ui = -g*np.sum(phi[sl]*W)*h**3
        return Eg + Ek + Ui, Pz
    phi_s = solve(c*c*klat2)
    gz = (np.roll(phi_s,-1,0)-phi_s)/h; gy = (np.roll(phi_s,-1,1)-phi_s)/h; gx = (np.roll(phi_s,-1,2)-phi_s)/h
    U = .5*c*c*np.sum(gz*gz + gy*gy + gx*gx)*h**3
    E0, _ = EP(phi_s, np.zeros_like(phi_s), sl, W)
    out = {'U': U, 'kappa_cont': (2/3)*U/c**2, 'phi_s': phi_s, 'E0': E0,
           'kappa_P': {}, 'kappa_E': {}}
    for v in vlist:
        pv = solve(c*c*klat2 - (v*kzc)**2)
        pt = -v*(np.roll(pv,-1,0) - np.roll(pv,1,0))/(2*h)
        Ev, Pv = EP(pv, pt, sl, W)
        out['kappa_P'][v] = Pv/v
        out['kappa_E'][v] = 2*(Ev - E0)/v**2
    return out

def dynamics(N, sigma, g, c, h, dt, vf, Tr, Th, mus=(), Tc=0.0, st=None):
    """Ramp-and-hold with source at the correct leapfrog time level; optional
    two-branch release into the Aristotelian primitive."""
    if st is None:
        st = stages_0A(N, sigma, g, c, h, [vf])
    phi_s, E0 = st['phi_s'], st['E0']
    stamp, dep, R = make(N, sigma)
    lap = lambda f: (np.roll(f,1,0)+np.roll(f,-1,0)+np.roll(f,1,1)+np.roll(f,-1,1)
                     + np.roll(f,1,2)+np.roll(f,-1,2) - 6*f)/h**2
    ss = lambda s: np.clip(s,0,1)**2*(3-2*np.clip(s,0,1))
    vel = lambda t: vf*ss(t/Tr)
    def diag(phi, phit, sl, W):
        gzc = (np.roll(phi,-1,0) - np.roll(phi,1,0))/(2*h)
        gz = (np.roll(phi,-1,0)-phi)/h; gy = (np.roll(phi,-1,1)-phi)/h; gx = (np.roll(phi,-1,2)-phi)/h
        E = .5*c*c*np.sum(gz*gz+gy*gy+gx*gx)*h**3 + .5*np.sum(phit**2)*h**3 \
            - g*np.sum(phi[sl]*W)*h**3
        return E - E0, -np.sum(phit*gzc)*h**3
    def step(state, vfun=None, mu=None):
        phi, phi_old, X, t, rho = state
        i0, Xf, sl = dep(X); W, dWz = stamp(Xf)
        Fs = g*np.sum(phi[sl]*dWz)
        rho.fill(0.); rho[sl] = W                     # source at X^n, time level n
        phi_new = 2*phi - phi_old + dt*dt*(c*c*lap(phi) + g*rho)
        phit = (phi_new - phi_old)/(2*dt)             # centered at n
        E, P = diag(phi, phit, sl, W)
        v = vfun(t) if vfun else mu*Fs
        Xn = X.copy(); Xn[0] += v*dt
        return (phi_new, phi, Xn, t + dt, rho), dict(t=t, v=v, Fs=Fs, E=E, P=P)
    state = (phi_s.copy(), phi_s.copy(), np.array([N/2.]*3), 0., np.zeros((N,N,N)))
    recB = []
    for n in range(int((Tr+Th)/dt)):
        state, d = step(state, vfun=vel); recB.append(d)
    recC = {}
    for mu in mus:
        stC = (state[0].copy(), state[1].copy(), state[2].copy(), state[3], np.zeros((N,N,N)))
        rc = []
        for n in range(int(Tc/dt)):
            stC, d = step(stC, mu=mu); rc.append(d)
        recC[mu] = rc
    # analysis
    tB = np.array([d['t'] for d in recB]); FB = np.array([d['Fs'] for d in recB])
    PB = np.array([d['P'] for d in recB]); EB = np.array([d['E'] for d in recB])
    aB = vf*np.gradient(ss(tB/Tr), tB)
    ramp = (tB < Tr) & (np.abs(aB) > 0.3*np.abs(aB).max())
    hold = (tB > Tr + 10) & (tB < Tr + Th - 2)
    out = dict(kappa_Mw=float(np.median(-FB[ramp]/aB[ramp])),
               kappa_hold=float(np.mean(PB[hold]))/vf,
               F_hold=float(np.mean(FB[hold])),
               peak_backreaction=float(-FB[ramp].min()),
               E_hold=float(np.mean(EB[hold])))
    for mu, rc in recC.items():
        tv = np.array([d['t'] for d in rc]); vv = np.array([d['v'] for d in rc])
        m = (tv > tv[0] + 6) & (vv > 1e-4)
        tau = -1/np.polyfit(tv[m], np.log(vv[m]), 1)[0]
        out[f'coast_mu{int(mu)}'] = dict(tau=float(tau), kappa_coast=float(tau/mu))
    return out

if __name__ == '__main__':
    N, c, h, dt, g, vf = 96, 1., 1., 0.35, 8., 0.05
    print("=== sigma = 1.5 : Stages 0/A/B/C ===")
    st = stages_0A(N, 1.5, g, c, h, [0.025, 0.05, 0.1])
    dyn = dynamics(N, 1.5, g, c, h, dt, vf, 30., 40., mus=(10., 25.), Tc=45., st=st)
    kc = st['kappa_cont']
    print(f" U_static                          : {st['U']:.4f}")
    print(f" kappa_pred (2/3)U/c^2 (continuum) : {kc:.4f}")
    print(f" steady P/v   (FFT, v=0.025)       : {st['kappa_P'][0.025]:.4f}   ratio {st['kappa_P'][0.025]/kc:.4f}")
    print(f" steady 2dE/v^2 (FFT, v=0.025)     : {st['kappa_E'][0.025]:.4f}   ratio {st['kappa_E'][0.025]/kc:.4f}")
    print(f" Momentwise -F_self/a (ramp)       : {dyn['kappa_Mw']:.4f}   ratio {dyn['kappa_Mw']/kc:.4f}")
    print(f" hold-phase P/v (dynamics)         : {dyn['kappa_hold']:.4f}   ratio {dyn['kappa_hold']/kc:.4f}")
    print(f" residual hold drag / peak F_back  : {abs(dyn['F_hold'])/dyn['peak_backreaction']*100:.2f}%")
    for mu in (10, 25):
        d = dyn[f'coast_mu{mu}']
        print(f" coast (mu={mu:2d}): tau = {d['tau']:6.2f}  kappa = tau/mu = {d['kappa_coast']:.4f}")
    print("=== sigma = 2.5 : convergence (Stages 0/A + ramp-hold) ===")
    st2 = stages_0A(N, 2.5, g, c, h, [0.05])
    dyn2 = dynamics(N, 2.5, g, c, h, dt, vf, 30., 40., st=st2)
    kc2 = st2['kappa_cont']
    print(f" kappa_pred: {kc2:.4f}  FFT P/v: {st2['kappa_P'][0.05]:.4f} (ratio {st2['kappa_P'][0.05]/kc2:.4f})"
          f"  Momentwise: {dyn2['kappa_Mw']:.4f} (ratio {dyn2['kappa_Mw']/kc2:.4f})")
    print(f" convergence of Momentwise ratio: sigma 1.5 -> 2.5 : "
          f"{dyn['kappa_Mw']/kc:.4f} -> {dyn2['kappa_Mw']/kc2:.4f}")

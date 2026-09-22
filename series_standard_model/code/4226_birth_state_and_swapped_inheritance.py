#!/usr/bin/env python3
"""4226 -- what the mixing can and cannot do, and which birth state reproduces V-A.
(1) Any rotationally invariant coupling between the two departing DPs is a function of sigma_e.sigma_nu;
    it commutes with the pair's total spin, so the singlet/triplet CONTENT of the pair is fixed at birth.
    Numerically: evolve product states under exp(-i theta sigma.sigma); the S-vs-T weights never move.
(2) Birth states, evaluated with the ejection rule (4223 machinery) and compared with the full V-A amplitude:
    (a) inheritance as drawn: electron keeps the quark's orbital sense s; core refills with r = +/-s;
        antineutrino = -r; amplitudes 1 and g for r = +s / -s.
    (b) swapped: the antineutrino carries the quark's orbital angular momentum s; the proton and the
        electron are born as one counter-spinning pair (singlet).
    (c) the measured pair state (4223), and its decomposition as (b) + delta x (sigma-written triplet)."""
import numpy as np
sx, sy, sz = np.array([[0,1],[1,0]],complex), np.array([[0,-1j],[1j,0]]), np.array([[1,0],[0,-1]],complex); sig=[sx,sy,sz]
up, dn = np.array([1,0],complex), np.array([0,1],complex)
k = np.kron
S=(k(up,dn)-k(dn,up))/np.sqrt(2); T0=(k(up,dn)+k(dn,up))/np.sqrt(2); Tp=k(up,up); Tm=k(dn,dn)
# (1)
ss = sum(k(s,s) for s in sig)
for th in (0.3, 1.0, 2.5):
    U = np.cos(th)*np.eye(4) - 1j*np.sin(th)*ss/ (1) if False else None
    w, v = np.linalg.eigh(ss); U = v @ np.diag(np.exp(-1j*th*w)) @ v.conj().T
    psi = k(up,dn); out = U@psi
    print(f"(1) theta={th}: |<S|psi>|^2 = {abs(S.conj()@psi)**2:.3f} -> {abs(S.conj()@out)**2:.3f};   |<T0|psi>|^2 = {abs(T0.conj()@psi)**2:.3f} -> {abs(T0.conj()@out)**2:.3f}")
# (2) machinery: state = dict proton-spin -> pair vector (e (x) nubar); W = sum_p Tr[rho_p Pe Pn]
def fit(comps, beta=0.999, n=1500):
    rho = sum(np.outer(v, v.conj()) for v in comps.values())
    rng=np.random.default_rng(3); X=[]; y=[]
    for _ in range(n):
        e=rng.normal(size=3); e/=np.linalg.norm(e); v=rng.normal(size=3); v/=np.linalg.norm(v)
        Pe=np.eye(2)-beta*sum(c*s for c,s in zip(e,sig)); Pn=np.eye(2)+sum(c*s for c,s in zip(v,sig))
        X.append([1,beta*(e@v),beta*e[2],v[2]]); y.append(np.real(np.trace(rho@k(Pe,Pn))))
    c,*_=np.linalg.lstsq(np.array(X),np.array(y),rcond=None); return c[1:]/c[0]
def jtw(l): D=1+3*l*l; return np.array([(1-l*l)/D, -2*l*(l+1)/D, 2*l*(l-1)/D])
print(f"\n{'birth state':64s} {'a':>7s} {'A':>7s} {'B':>7s}")
for g in (1.0, -np.sqrt(2), 3.0):
    # (a): p+ with e+ nubar-  (r=+s, nubar=-s);  p- with e+ nubar+ (r=-s)
    a,A,B = fit({'p+': k(up,dn), 'p-': g*k(up,up)})
    print(f"{'(a) e keeps s; nubar = -refill; g(r=-s)/g(r=+s) = %+.3f' % g:64s} {a:+7.3f} {A:+7.3f} {B:+7.3f}")
# (b): nubar = |s>; (p,e) singlet: p+ e- - p- e+
a,A,B = fit({'p+': k(dn,up), 'p-': -k(up,up)})
print(f"{'(b) nubar carries s; proton and electron born as a singlet':64s} {a:+7.3f} {A:+7.3f} {B:+7.3f}")
print(f"{'    JTW at lambda = -1 (quark-level V-A, g_A = g_V)':64s} {jtw(-1)[0]:+7.3f} {jtw(-1)[1]:+7.3f} {jtw(-1)[2]:+7.3f}")
lam=-1.2754; d=lam+1
a,A,B = fit({'p+': S+lam*T0, 'p-': -np.sqrt(2)*lam*Tp})
print(f"{'(c) measured pair state (4223), lambda = -1.2754':64s} {a:+7.3f} {A:+7.3f} {B:+7.3f}")
a,A,B = fit({'p+': -np.sqrt(2)*k(dn,up) + d*T0, 'p-': np.sqrt(2)*k(up,up) - np.sqrt(2)*d*Tp})   # S+lam T0 with lam=-1+delta, exactly
print(f"{'    = -sqrt2 x (b)  +  delta x (sigma-written triplet), delta = lambda+1 = %.3f' % d:64s} {a:+7.3f} {A:+7.3f} {B:+7.3f}")
print(f"{'    JTW at lambda = -1.2754':64s} {jtw(lam)[0]:+7.3f} {jtw(lam)[1]:+7.3f} {jtw(lam)[2]:+7.3f}")
print(f"\nweight of the delta admixture: delta^2 x 3 / (2 + 3 delta^2) = {3*d*d/(2+3*d*d):.3f} of events; (b) alone carries {2/(2+3*d*d):.3f}")

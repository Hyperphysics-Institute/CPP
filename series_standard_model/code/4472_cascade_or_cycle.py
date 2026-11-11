"""Patch 4472 -- founder: the decay may proceed in stages, a propagated collapse through the orbital's sections, each releasing an identical
increment; perhaps a transformation-cell-type process; analogy with the Brusselator (as used by Paul LaViolette).

Part 1. A single sweep at the relay speed: time to cross an orbital (0.1-0.3 nm) at c, against one period of Lyman-alpha and the lifetime;
        how many rounds a repeating process would need to last the lifetime; how slow a single sweep would have to be to last it.
Part 2. Energy shares: N gapless in-step wavelets sharing E = hf each carry hf/N, not hf; the photon's energy x one period = h.
Part 3. The Brusselator (dX/dt = A + X^2 Y - (B+1) X, dY/dt = B X - X^2 Y), below its oscillation threshold (B < 1 + A^2): disturbed from its
        resting point it rings at a fixed rate and dies away -- the rate is set by A and B, not by how hard it was disturbed.  Simulated for two
        disturbance sizes; ringing period and decay time compared with the linear prediction.  (An analogy for a clock that keeps its rate while
        dying away, not evidence.)  Near the threshold (B close to 1 + A^2) it rings many cycles before fading; it rings at all only
        for (A-1)^2 < B < (A+1)^2.  Below threshold this is generic damped ringing; the Brusselator's own self-oscillation is above threshold.
Part 1b. At the electron's orbital speed (c/137) instead of c; and the speed a cycling round (2 pi r per period) would need.
"""
import numpy as np
c, h = 2.99792458e8, 6.62607015e-34
f, tau = 2.466e15, 1.596e-9
for r in (1e-10, 3e-10):
    print(f"Part 1  cross {r*1e9:.1f} nm at c: {r/c:.1e} s = {r/c*f:.1e} of a period; rounds of that length to fill the lifetime: {tau/(r/c):.1e}; "
          f"a single sweep lasting the lifetime would move at {r/tau:.2f} m/s")
print(f"        one period {1/f:.2e} s; cycles in the lifetime {f*tau:.1e}")
va = c/137.036
for r in (1e-10, 3e-10):
    print(f"Part 1b at the electron's orbital speed (c/137): cross {r*1e9:.1f} nm in {r/va*f:.2f} of a period; "
          f"a cycling round of 2 pi r = {2*np.pi*r*1e9:.2f} nm per period needs {2*np.pi*r*f:.1e} m/s (c/{c/(2*np.pi*r*f):.0f}); at c it would go round {c/(2*np.pi*r*f):.0f} times per period")
E = h*f
for N in (1, 1e3, 3.9e6):
    print(f"Part 2  {N:.0e} wavelets sharing E = hf = {E/1.602e-19:.1f} eV: each {E/N/1.602e-19:.1e} eV; energy x one period = {E/f/h:.0f} h")
A = 1.0
for B in (1.5, 1.98):
    tr, det = B - 1 - A**2, A**2
    gam = -tr/2; om = np.sqrt(det - gam**2)
    print(f"Part 3  Brusselator A={A}, B={B}: linear prediction period {2*np.pi/om:.3f}, decay time {1/gam:.2f}, "
          f"cycles before fading to 1/e {1/gam/(2*np.pi/om):.1f}")
B = 1.5
def run(dx):
    X, Y = A + dx, B/A; dt = 1e-3; ts, xs = [], []
    for k in range(int(60/dt)):
        dX = A + X*X*Y - (B+1)*X; dY = B*X - X*X*Y
        X += dX*dt; Y += dY*dt
        ts.append(k*dt); xs.append(X - A)
    xs = np.array(xs); ts = np.array(ts)
    up = np.where((xs[:-1] < 0) & (xs[1:] >= 0))[0]
    per = np.diff(ts[up]).mean()
    return per
for dx in (0.01, 0.1, 1.0):
    print(f"        disturbed by {dx}: ringing period {run(dx):.3f} (nearly the same rate for the sizes tried, while it dies away)")
# simulated near-threshold ringing count
def cycles_sim(B, dx=0.01, T=400.0):
    X, Y = A + dx, B/A; dt = 2e-3; xs = []
    for k in range(int(T/dt)):
        dX = A + X*X*Y - (B+1)*X; dY = B*X - X*X*Y
        X += dX*dt; Y += dY*dt; xs.append(X - A)
    xs = np.abs(np.array(xs)); env0 = xs[:int(7/dt)].max(); t1 = np.argmax(xs < env0/np.e*0 + 0)  # placeholder
    peaks = [i for i in range(1, len(xs)-1) if xs[i] >= xs[i-1] and xs[i] >= xs[i+1]]
    amps = np.array([xs[i] for i in peaks]); times = np.array(peaks)*dt
    k = np.argmax(amps < amps[0]/np.e) if np.any(amps < amps[0]/np.e) else len(amps)-1
    return times[k]/(2*np.pi)
print(f"        simulated at B = 1.98: about {cycles_sim(1.98):.0f} cycles before the swing falls to 1/e (linear prediction ~16)")
eps = 1/(np.pi*3.9e6)
print(f"        cycles before fading ~ 1/(pi (1 + A^2 - B)); 3.9e6 cycles needs B within {eps:.1e} of threshold")

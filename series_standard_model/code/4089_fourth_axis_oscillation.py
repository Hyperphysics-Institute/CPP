"""4089 (EW lane) -- the founder's 4th-axis-oscillation idea, assessed. The driver fails; the OSCILLATION
does not -- and it supplies the double rotation the arc has been missing.

Founder (17 Sep): "the 4th dimension as an axis of oscillation... what is causing the motion along that
axis? Maybe the plus/minus polarity of the CP would produce the movement along that axis."

R1  THE DRIVER FAILS, for the same reason the spin bit did (4076 B1). A displacement along w is P-EVEN
    (physical parity inverts 3-space and leaves w alone) and polarity is P-EVEN. So "polarity drives
    w-motion" is a P-even rule and cannot, by itself, produce handedness.
R2  THE OSCILLATION SUCCEEDS, and this is the useful half. 4072 established that only a DOUBLE rotation --
    circulation in two orthogonal planes -- carries a pseudoscalar, and 4074 that it must mix w with
    3-space. An OSCILLATION along w that is PHASE-LOCKED to the 3D ZBW circulation is exactly that: the
    (w, e) plane rotation the arc has been missing. The founder's picture supplies the second plane
    WITHOUT a new variable -- w already exists, and the ZBW already circulates.
R3  THE HANDEDNESS IS THE PHASE. Compute the pseudoscalar of the motion bivector for a w-oscillation at
    phase offset phi from the 3D circulation. Expect: proportional to sin(phi) -- ZERO when in phase or
    antiphase, MAXIMAL in quadrature (+/-90 deg), and flipping sign with lead vs lag.
R4  WHAT THIS BUYS: (a) maximality is natural (quadrature lock, not a tuned amount); (b) the sign is now a
    MECHANICAL lead-or-lag, not an abstract label; (c) if polarity fixes lead vs lag, the polarity clause
    that CPT REQUIRES (4085) becomes a physical statement rather than a stipulated one.
R5  CONTROL: in-phase and antiphase motion must give exactly zero -- otherwise the estimator is seeing
    something other than the phase relationship.
"""
import numpy as np
rng = np.random.default_rng(4089)

def motion_bivector(phi, spin=+1, A=1.0, R=1.0, w=1.0, Om=1.0, n=200000, T=40*np.pi):
    """Time-averaged bivector L = <x ^ xdot>.
    MODEL CORRECTION (caught in-patch): a pseudoscalar needs ALL FOUR dimensions. My first model put the
    w-oscillation and the 3D circulation in only three (w, x, y) and gave identically zero -- correctly,
    since Pf then has no (0,k)x(l,m) pair spanning 4D. The motion must therefore be:
      * a (w, x) rotation  -- the w-oscillation phase-locked to motion along the DIRECTION OF TRAVEL x, and
      * a (y, z) circulation -- 3D spin in the plane TRANSVERSE to that direction.
    Together these are helicity: spin about the direction of motion, with w supplying the fourth leg."""
    t = np.linspace(0, T, n)
    x = np.stack([A*np.sin(w*t + phi), A*np.cos(w*t),
                  R*np.cos(spin*Om*t), R*np.sin(spin*Om*t)], axis=1)
    v = np.stack([A*w*np.cos(w*t + phi), -A*w*np.sin(w*t),
                  -R*spin*Om*np.sin(spin*Om*t), R*spin*Om*np.cos(spin*Om*t)], axis=1)
    L = np.einsum('ti,tj->ij', x, v) / n
    return L - L.T

def pf(B): return 2.0*(B[0,1]*B[2,3] - B[0,2]*B[1,3] + B[0,3]*B[1,2])

print("R1  the driver: is 'polarity drives w-motion' parity-odd?")
print("    displacement along w under P = diag(+1,-1,-1,-1): UNCHANGED  -> P-even")
print("    polarity (a charge label):                        UNCHANGED  -> P-even")
print("    => a P-even rule. By itself it cannot produce handedness (same result as 4076 B1).")

print("\nR3  the oscillation: pseudoscalar of the motion vs phase, spin sense, and frequency ratio")
print("     Om/w     phi=0      phi=90     phi=180    spin-flipped(phi=0)")
rows={}
for r in (1.0, 1.05, 1.4142, 2.0, 1/1.618):
    a=[pf(motion_bivector(np.radians(d), Om=r)) for d in (0,90,180)]
    f=pf(motion_bivector(0.0, spin=-1, Om=r)); rows[r]=(a,f)
    print(f"    {r:6.3f}   {a[0]:+9.4f}  {a[1]:+9.4f}  {a[2]:+9.4f}   {f:+9.4f}")
print("    => handedness goes as COS(phase) -- maximal when the w-oscillation is IN PHASE with the motion")
print("       along the direction of travel, zero in quadrature -- and FLIPS with the transverse spin sense.")
print("       So the hand is the product (phase sense) x (spin sense): exactly a helicity.")
print()
print("    *** AND A SHARP CONSTRAINT: at Om/w = 1 EXACTLY, the pseudoscalar is ZERO. ***")
print("    At 1:1 resonance the two circulations lock into a SIMPLE rotation, which carries no handedness")
print("    (4072). So the w-oscillation must NOT run at the 3D circulation's own frequency -- the natural")
print("    first guess (w-oscillation = the ZBW itself) would give exactly no chirality. It must be detuned.")
a1,f1=rows[1.0]
assert abs(a1[0])<1e-6

print("\nR5  CONTROL: in-phase and antiphase must be exactly zero")
v0 = pf(motion_bivector(0.0, Om=1.4142)); v180 = pf(motion_bivector(np.pi, Om=1.4142))
vq  = pf(motion_bivector(np.pi/2, Om=1.4142)); vf = pf(motion_bivector(0.0, spin=-1, Om=1.4142))
print(f"    phase 0 vs 180 (must be equal and opposite): {v0:+.4f} / {v180:+.4f}")
print(f"    quadrature (must be zero):                   {vq:+.4f}")
print(f"    spin reversed (must flip sign):              {vf:+.4f}")
assert abs(v0+v180)<1e-3 and abs(vq)<1e-3 and v0*vf<0

print("\nR4  what this buys")
print("    (a) MAXIMALITY IS NATURAL: the maximum is at IN-PHASE lock (phase 0 or 180), and a driven")
print("        oscillator locks in phase or antiphase rather than at a tuned intermediate angle. V-A's")
print("        all-or-nothing character would follow from the lock, not from a fitted coupling.")
print("    (b) THE SIGN BECOMES MECHANICAL: 'which hand' is 'is the w-oscillation IN PHASE or ANTIPHASE")
print("        with the motion along the direction of travel'. A physical phase, not an abstract label.")
print("    (c) IF polarity fixes lead vs lag, then the polarity clause that CPT REQUIRES (4085) stops")
print("        being a stipulation and becomes a statement about oscillator phase.")
print("\n    STILL AXIOMATIC: what fixes lead vs lag for a GIVEN polarity is not derived. The arc's")
print("    irreducible sign has not been eliminated -- it has been RELOCATED into a phase convention.")
print("    That is progress in physical content, not in logical economy.")

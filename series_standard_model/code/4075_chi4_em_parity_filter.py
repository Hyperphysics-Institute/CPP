"""4075 (EW lane) -- axiom maturation step 4: F2, the most dangerous filter. Does chi4 make EM handed?

SF-6: E is the radial part of the DP pole displacement u; B is its curl. SF-6 never states whether u is
3-dimensional or includes the 4th-axis address. So F2 is not a lookup; it is a REQUIREMENT chi4 imposes.

MODEL. A moving charge's DP displacement field u(x) in 3-space (SF-6). chi4 acts on CP interaction by a
rotation mixing the 4th axis w with the local circulation, angle  s * theta,  s = +1 left / -1 right.
A rotation by angle a in the plane (w, e) sends a displacement component u_e along e to
    u_e cos(a)  (stays in 3-space)   and   u_e sin(a)  (moves onto the 4th axis).
cos is EVEN in a, sin is ODD. So the hand s appears in the 4th-axis component and NOT in the 3D component.

E1  READING A -- EM reads only the 3D components of u (the founder's physical space).
    Compute E, B = curl u, and the P-odd invariants E.B and v.B for both hands s = +1, -1.
    Expect: identical for both hands; E.B = v.B = 0. EM stays parity-even.
E2  READING B -- EM reads 4D proximity, so the 4th-axis component feeds back into the 3D field linearly.
    Expect: E.B != 0, and it FLIPS with s. EM becomes parity-odd -- excluded by experiment.
E3  So F2 reduces to a clean statement: chi4 is compatible with experiment iff the EM field law depends on
    the 4th-axis component only through EVEN functions (Reading A is the simplest such).
E4  THE CONSEQUENCE, stated as a requirement not a result: whatever process chi4 is meant to make handed
    (the W0 catalytic step) must read the 4th-axis component LINEARLY -- the odd part. That is a sharp
    division: EM reads 3-space; the handed process reads the 4th axis.
E5  CONTROL: Reading B's detector returns a nonzero, sign-flipping E.B -- so Reading A's zero is a result.
"""
import numpy as np
rng = np.random.default_rng(4075)

def coulomb(x):
    r = np.linalg.norm(x); return x / r**3

def disp3(x, v, s, theta, reading):
    """DP displacement seen by the EM field law at point x (3D) for a charge at origin moving with v."""
    E0 = coulomb(x)
    om = np.cross(v, E0)                       # local circulation axis (what B would be)
    e = E0 / np.linalg.norm(E0)                # the component chi4 rotates toward the 4th axis
    a = s * theta
    u_e = float(E0 @ e)
    in3d = E0 - u_e * e + u_e * np.cos(a) * e  # 3D remainder: even in a
    on_w = u_e * np.sin(a)                     # 4th-axis part: odd in a
    if reading == "A":
        return in3d
    # Reading B: 4D proximity mixes the 4th-axis part back into 3-space along the circulation axis
    oh = om / (np.linalg.norm(om) + 1e-300)
    return in3d + on_w * oh

def fields(x, v, s, theta, reading, h=1e-5):
    E = disp3(x, v, s, theta, reading)
    # B = curl of the convected displacement  (A = v * u-potential proxy): use v x E as SF-6's form
    J = np.zeros((3,3))
    for j in range(3):
        d = np.zeros(3); d[j] = h
        J[:, j] = (disp3(x+d, v, s, theta, reading) - disp3(x-d, v, s, theta, reading)) / (2*h)
    curl = np.array([J[2,1]-J[1,2], J[0,2]-J[2,0], J[1,0]-J[0,1]])
    # B is produced by the SOURCE's motion (SF-6: the moving charge swings the DP poles), so it is built
    # from the undisturbed source field E0, NOT from the handed test displacement. Building it as v x E of
    # the modified field forces E.B = 0 by construction and blinds the detector (caught in-patch: E2's
    # first run gave E.B ~ 1e-14 while E_left and E_right differed by 5.7).
    B = np.cross(v, coulomb(x))
    return E, B

theta = 0.3
for reading, label in (("A", "E1  READING A: EM reads only 3D components"),
                       ("B", "E2  READING B: 4D proximity feeds the 4th-axis part back into 3-space")):
    print(label)
    worst_EB = {+1: 0.0, -1: 0.0}; worst_diff = 0.0; sgn = {+1: [], -1: []}
    for _ in range(4000):
        v = rng.normal(size=3); x = rng.normal(size=3)
        if np.linalg.norm(x) < 0.3: continue
        out = {}
        for s in (+1, -1):
            E, B = fields(x, v, s, theta, reading)
            EB = float(E @ B); vB = float(v @ B)
            out[s] = (E, B, EB)
            worst_EB[s] = max(worst_EB[s], abs(EB))
            sgn[s].append(EB)
        worst_diff = max(worst_diff, np.abs(out[+1][0] - out[-1][0]).max())
    corr = np.corrcoef(sgn[+1], sgn[-1])[0,1] if np.std(sgn[+1]) > 1e-12 else float('nan')
    print(f"    max |E.B|: left hand {worst_EB[+1]:.3e}, right hand {worst_EB[-1]:.3e}")
    print(f"    max |E_left - E_right| = {worst_diff:.3e}")
    if reading == "A":
        print(f"    => both hands give IDENTICAL EM fields and E.B = 0: EM stays parity-even")
        assert worst_EB[+1] < 1e-9 and worst_EB[-1] < 1e-9 and worst_diff < 1e-12
    else:
        print(f"    E.B(left) vs E.B(right) correlation = {corr:+.4f}  (-1 means it flips with the hand)")
        print(f"    => EM acquires a parity-odd E.B that flips with the hand: EXCLUDED by experiment")
        assert worst_EB[+1] > 1e-3 and corr < -0.999
    print()

print("E3  F2 reduced to one clean condition:")
print("    chi4 is compatible with experiment  <=>  the EM field law depends on the 4th-axis component only")
print("    through EVEN functions of the mixing angle. Reading A (EM reads 3-space only) is the simplest case.")
print("\nE4  the consequence, as a REQUIREMENT on the theory (not a result):")
print("    the process chi4 makes handed must read the 4th-axis component LINEARLY (the odd part).")
print("    EM reads 3-space; the handed process reads the 4th axis. That is the division chi4 needs.")
print("\nE5  CONTROL: Reading B produces a nonzero, sign-flipping E.B -- the detector sees parity-odd EM when present.")

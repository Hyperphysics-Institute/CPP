#!/usr/bin/env python3
"""
1121_task1_source_configurational.py -- spin-2 construction, Task 1 (the flow choice: B).

Three computational demonstrations supporting the flow-B decision (Q_ij lives in the GP->GP
Lattice State Packet broadcast), each killing one alternative or fixing one design constraint:

  D1. AGAINST option A (CP State Register attribute): the mass quadrupole is IRREDUCIBLY
      CONFIGURATIONAL -- a single point mass has identically zero quadrupole about its own
      location, for any mass, always. No per-CP rank-2 attribute could ever be the source;
      the quadrupole exists only as a property of EXTENDED configurations (consistent with
      1120: matter-side l=2 lives in configuration space).
  D2. THE SOURCE NEEDS NO NEW REPORT: the mass quadrupole of any configuration is assembled
      purely from per-CP positions and masses -- content the CP->GP register ALREADY carries
      (GP address; mass via the eDP polarization energy E_pol = mc^2 of c07). Demonstrated:
      Q_ij of a binary computed from positions alone. The Perceive/Compute steps can assemble
      the source from existing reports; the only missing piece is the broadcast CHANNEL.
  D3. THE NO-STATIC-DOUBLE-COUNTING CONSTRAINT (design input for Task 3): a STATIC
      configuration has a time-CONSTANT quadrupole -> d^2Q/dt^2 = 0 -> radiates nothing; an
      ORBITING binary has an oscillating TT quadrupole at TWICE the orbital frequency (the GW
      signature). Sourcing the broadcast Q_ij by the TIME-VARYING (TT-projected) quadrupole
      leaves the static sector untouched -- the scalar keeps statics (Schwarzschild, recovered
      exactly in c07/c08); the tensor carries radiation. The labor division is clean.

NO VERDICT MOVED (no THEO/PRED/count change; this is the Task-1 decision record's verify).
"""
import numpy as np

def quadrupole(masses, positions):
    """Mass quadrupole Q_ij = sum m (3 x_i x_j - r^2 delta_ij) about the origin."""
    Q = np.zeros((3, 3))
    for m, x in zip(masses, positions):
        Q += m * (3 * np.outer(x, x) - np.dot(x, x) * np.eye(3))
    return Q

print("=== D1. AGAINST OPTION A: the quadrupole is irreducibly configurational ===")
for m in [1.0, 264.0, 1e30]:
    Q = quadrupole([m], [np.zeros(3)])
    print(f"  single point mass m={m:.3g} about its own location: |Q| = {np.abs(Q).max():.1f}")
print("  => identically zero, for any mass. A rank-2 'shape' attribute on a single CP has")
print("     nothing physical to report: the source quadrupole is a property of EXTENDED")
print("     configurations only (cf. 1120 P2: l=2 lives in the relative-coordinate function")
print("     space). Option A puts the bit where the physics is not.")

print("\n=== D2. THE SOURCE ASSEMBLES FROM EXISTING REPORTS (positions + masses) ===")
# equal-mass binary, separation 2a, about its center of mass
a, m = 1.0, 0.5
for name, x1 in [("binary along x", np.array([a, 0, 0])),
                 ("binary along (1,1,0)/sqrt2", np.array([a, a, 0]) / np.sqrt(2))]:
    Q = quadrupole([m, m], [x1, -x1])
    print(f"  {name}: Q_ij (from positions alone) =")
    print("    " + str(np.round(Q, 3)).replace("\n", "\n    "))
print("  => computed using ONLY per-CP data the CP->GP register already carries (GP address;")
print("     mass = E_pol/c^2 per c07). No new CP-side report is required. The missing piece")
print("     is not the SOURCE -- it is the broadcast CHANNEL to radiate it into (1114).")

print("\n=== D3. NO-STATIC-DOUBLE-COUNTING: only the TIME-VARYING quadrupole radiates ===")
omega, steps = 1.0, 720
ts = np.linspace(0, 4 * np.pi / omega, steps)
# static pair vs circularly orbiting pair (same masses, same separation)
amp_static, Qxx_t, Qxy_t = [], [], []
for t in ts:
    Qs = quadrupole([m, m], [np.array([a, 0, 0]), np.array([-a, 0, 0])])
    x1 = a * np.array([np.cos(omega * t), np.sin(omega * t), 0])
    Qo = quadrupole([m, m], [x1, -x1])
    amp_static.append(Qs[0, 0]); Qxx_t.append(Qo[0, 0]); Qxy_t.append(Qo[0, 1])
amp_static, Qxx_t, Qxy_t = map(np.array, (amp_static, Qxx_t, Qxy_t))
d2_static = np.gradient(np.gradient(amp_static, ts), ts)
print(f"  static pair:   d^2 Q_xx / dt^2  max |.| = {np.abs(d2_static).max():.2e}  (zero -> NO radiation)")
# dominant frequency of the orbiting pair's quadrupole:
f = np.fft.rfftfreq(steps, ts[1] - ts[0]) * 2 * np.pi
spec = np.abs(np.fft.rfft(Qxx_t - Qxx_t.mean()))
print(f"  orbiting pair: Q_xx oscillates at omega_GW = {f[np.argmax(spec)]:.3f}"
      f"  = 2 x omega_orbit ({omega})  [the GW double-frequency signature]")
print(f"                 Q_xy oscillation amplitude = {np.ptp(Qxy_t)/2:.3f} (the 'x' polarization channel)")
print("  => DESIGN CONSTRAINT for Task 3 (the coupling): source the broadcast Q_ij by the")
print("     TIME-VARYING (TT-projected) part of the matter quadrupole. Statics stay with the")
print("     scalar |SSV|_abs (Schwarzschild already exact, c07/c08); radiation goes to the")
print("     tensor. No double-counting of the Newtonian sector; no disturbance of recovered")
print("     results. (Sibling constraint: no-ZBW-double-counting -- Q_ij is the radiative")
print("     FIELD, distinct from emergent orbital spin-1/2 and from matter's configurational")
print("     l=2, per 1120.)")

print("\n================== TASK 1 VERIFY SUMMARY ==================")
print("A: wrong home (single CP has no quadrupole -- the source is configurational).")
print("C: the readout, not the carrier (the GP->CP instruction is the Compute step's OUTPUT;")
print("   once the broadcast carries Q_ij, extending the displacement map is a theorem).")
print("B: the irreducible core -- the missing piece is the broadcast channel, the source")
print("   assembles from existing reports, propagation is native (1113), carriage is")
print("   absolute-frame massless (1119), and the 5 components sit in the protected H_g")
print("   irrep (1120). The LSP has been extended ONCE BEFORE for exactly this kind of")
print("   reason (DI-bit -> LSP: 'adding the vector component needed for general relativity',")
print("   c07 glossary). The tensor extension is the third rung of an existing ladder.")

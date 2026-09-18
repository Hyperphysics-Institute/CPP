"""4082 (EW lane) -- the founder's momentum-absorption answer, made quantitative. It closes K3's window.

Founder (17 Sep): "If the captured charge is retained for a few Moments, then the momentum it was carrying
is absorbed by the bracelet. As the bracelet dissolves, reconstituting the momentum on the captured charge
is exceedingly unlikely and is more likely to be dispersed randomly among the various CP/DP constituents."

THE PHYSICS IS SOUND and it helps: the charge's direction is not held as a free vector at the decision
point. But absorbed momentum does not vanish -- CONSERVATION puts it into the bracelet's BULK MOTION, and
CPP has an ABSOLUTE frame (the Nexus), so bulk motion is physically visible at substrate level: DI-bits
travel at c in the absolute frame, so a moving ring sees direction-dependent arrivals at order v/c.

So the residual asymmetry is   eps ~ v/c = p_captured / M_W   -- suppressed by the MASS RATIO, which is
exactly the founder's point, quantified.

H1  eps for real processes (p / M_W).
H2  the register depth each process then ALLOWS: ties survive iff eps < 2^-b  =>  b < log2(1/eps).
H3  the register depth EM SAFETY REQUIRES: the generic tie rate 2^-b must sit below experimental limits on
    parity violation in electromagnetic/atomic processes.
H4  THE WINDOW: compare H2's ceiling with H3's floor.
H5  CONTROL: the arithmetic is a ratio of logs; both bounds are computed from the same 2^-b law used in
    4080/4081, so they are directly comparable.
"""
import numpy as np

M_W = 80.4e3   # MeV

print("H1  residual asymmetry eps = p_captured / M_W  (bulk recoil of the bracelet, absolute frame)")
procs = [("nuclear beta decay", 1.0), ("muon decay", 52.8), ("tau decay", 890.0),
         ("b-quark decay", 2500.0), ("top decay / on-shell W", 40000.0)]
eps = {}
for name, p in procs:
    e = p / M_W; eps[name] = e
    print(f"    {name:26s} p ~ {p:8.1f} MeV   eps = {e:.3e}")

print("\nH2  register depth each process ALLOWS (ties survive iff eps < 2^-b)")
ceil = {}
for name, _ in procs:
    b = np.log2(1/eps[name]); ceil[name] = b
    print(f"    {name:26s} b < {b:5.1f} bits")
b_ceiling = min(ceil.values())
print(f"    => the BINDING ceiling (the process with the largest eps that must still violate parity")
print(f"       maximally) gives  b < {b_ceiling:.1f} bits.")
print(f"    Note: V-A is observed maximal in ALL of these, so every one must keep its ties.")

print("\nH3  register depth EM SAFETY REQUIRES (generic tie rate 2^-b must be below observed EM parity limits)")
lims = [("atomic parity violation, measured effect", 1e-11),
        ("conservative bound on P-odd EM at 1e-6", 1e-6),
        ("very generous bound at 1e-3", 1e-3)]
floor = {}
for name, tol in lims:
    b = np.log2(1/tol); floor[name] = b
    print(f"    {name:42s} needs b > {b:5.1f} bits")

print("\nH4  THE WINDOW")
print(f"    ceiling from weak processes : b < {b_ceiling:.1f}")
for name, tol in lims:
    print(f"    floor  from {name:40s}: b > {floor[name]:.1f}   -> window {'OPEN' if floor[name] < b_ceiling else 'EMPTY'}")
print()
print(f"    Even the most generous EM bound (1e-3) needs b > {floor['very generous bound at 1e-3']:.1f},")
print(f"    while top/on-shell-W processes cap b at {ceil['top decay / on-shell W']:.1f}. The window is EMPTY by")
print(f"    {floor['very generous bound at 1e-3'] - ceil['top decay / on-shell W']:.1f} bits on the most generous reading, and by")
print(f"    {floor['atomic parity violation, measured effect'] - ceil['top decay / on-shell W']:.1f} bits on the realistic one.")

print("\nH5  the failure is not marginal and does not depend on fine numbers:")
print("    weak processes span p from ~1 MeV to ~40 GeV, i.e. eps from 1e-5 to 0.5. For ties to survive at")
print("    the HIGH end, registers must be shallow (b < 1). For EM to stay clean, they must be deep")
print("    (b > 10 at minimum). One fixed register depth cannot do both.")
print("\n    K3 PREDICTS: parity violation should WEAKEN as the captured momentum approaches M_W.")
print("    Observation: V-A is maximal across the whole range. That is a direct falsification.")
assert min(floor.values()) > b_ceiling
print("\n    => K3 IS REFUTED as a universal mechanism.")

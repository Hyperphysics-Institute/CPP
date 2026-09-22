#!/usr/bin/env python3
"""4206 -- the inheritance model's a, A, B with the channel weights and ejection statistics made explicit.
Model (G-EW-INHERIT-4205): neutron spin +z; departed d-quark sense s = +z with probability P, -z with 1-P;
electron spin = s; refill sense = -s (GT) with probability g, = +s (Fermi) with 1-g; antineutrino spin =
-(refill sense) = +s (GT) or -s (Fermi). Ejection: each lepton is emitted with the maximal linear bias
allowed by its measured helicity, W ~ 1 + h cos(angle to q*spin), h = 1 (electron helicity -v/c, nubar +1).
Coefficients from W ~ 1 + a (pe.pn) + A (sigma_n.pe) + B (sigma_n.pn):  X = 3 <cos>.
SM for comparison: lam = -1.2754."""
def coeffs(P, g):
    pol = 2 * P - 1                          # <s.z>
    # electron along -s (h=1): <cos to z> = -(1/3) pol.  Independent of channel (spin inherited).
    A = 3 * (-(1/3) * pol)
    # antineutrino along +(its spin): GT spin = +s, Fermi spin = -s
    B = 3 * ((1/3) * pol * (g - (1 - g)))
    # a: <cos(e,nu)> = <cos_e><cos_nu> about the common axis s
    a = 3 * ((-1/3) * (g * (1/3) + (1 - g) * (-1/3)))
    return a, A, B
l = -1.2754; D = 1 + 3*l*l
print(f"{'':44s} {'a':>7s} {'A':>7s} {'B':>7s}")
print(f"{'SM, measured lambda':44s} {(1-l*l)/D:+7.3f} {-2*l*(l+1)/D:+7.3f} {2*l*(l-1)/D:+7.3f}")
print(f"{'SM, pure GT limit':44s} {-1/3:+7.3f} {-2/3:+7.3f} {+2/3:+7.3f}")
print(f"{'SM, pure Fermi limit':44s} {+1:+7.3f} {0:+7.3f} {0:+7.3f}")
for name, P, g in (('model, SU(6) P=5/6, pure GT (g=1)', 5/6, 1.0), ('model, SU(6) P=5/6, pure Fermi (g=0)', 5/6, 0.0),
                   ('model, SU(6) P=5/6, g=0.83 (measured GT fraction)', 5/6, 0.83), ('model, P=0.71, g=0.83', 0.71, 0.83)):
    a, A, B = coeffs(P, g); print(f"{name:44s} {a:+7.3f} {A:+7.3f} {B:+7.3f}")
print("\nPure-GT limit: model = SM exactly, all three coefficients, with the SU(6) d-quark polarisation 5/6.")
print("Pure-Fermi limit: model a=+1/3, A=-2/3, B=-2/3 vs SM a=+1, A=0, B=0 -- the model assigns each lepton")
print("a definite spin along s inside what must be a singlet; and the measured A needs the Fermi-GT")
print("INTERFERENCE term (+0.434 of the SM's -0.119), which classical channel probabilities cannot produce.")

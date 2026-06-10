import numpy as np
hbarc=197.327; alpha=1/137.036; E_qDP=264.0; m_qDP=264.0; mu=m_qDP/4.0; lamC=hbarc/E_qDP
# Residual between color-SINGLET qDPs: no long-range color field (SS-1 vertex mechanism) -> light-DP-exchange
# Yukawa (range ~hbar c/E_hDP ~1.3 fm) + London dispersion floor. f = depth/E_qDP via qDP color polarizability.
def f_disp(alpha_c,a):
    gc2=alpha_c*hbarc; a_pol=gc2/(mu*(E_qDP/hbarc)**2); C6=0.75*E_qDP*a_pol**2
    return (C6/a**6)/E_qDP, a_pol
print(f"qDP Compton size lambda={lamC:.2f} fm, internal reduced mass mu={mu:.0f} MeV")
for name,ac in [("weak 3*alpha",3*alpha),("strong alpha_s~0.3",0.3),("strong alpha_s~0.6",0.6)]:
    for a in [1.0,1.3]:
        f,ap=f_disp(ac,a); print(f"  {name:18s} a={a} fm: alpha_pol={ap:.3f} fm^3, f={f:.2e}")
print(f"  geometric (lambda/a)^6: a=1.0->{(lamC/1.0)**6:.3f}, a=1.3->{(lamC/1.3)**6:.3f}")
print("=> f bounded ~1e-4 (weak/dispersion) to ~0.15 (strong/contact), all <1. Open vertex: which coupling")
print("   (3*alpha DP-binding vs alpha_s confinement) mediates the neutral qDP-qDP residual. Arc robust for all f<1.")

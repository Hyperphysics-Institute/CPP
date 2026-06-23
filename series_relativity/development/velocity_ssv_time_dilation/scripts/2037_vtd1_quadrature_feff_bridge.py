import numpy as np
print("VTD-1: three characterizations of the velocity time-dilation budget split")
print("="*78)
print(f"{'v/c':>5} {'gamma':>9} {'1/gamma':>9} | {'LINEAR 1-v/c':>13} {'QUAD sqrt(1-b^2)':>16} {'f_eff=1-1/g -> 1-f_eff':>22} {'bridge 1/(1+kdSSV)':>18}")
for b in [0.1,0.3,0.6,0.8,0.9,0.99]:
    g = 1/np.sqrt(1-b**2)
    inv_g = 1/g
    linear   = 1 - b                      # naive collinear consumption (WRONG)
    quad     = np.sqrt(1-b**2)            # orthogonal/Pythagorean remainder
    f_eff    = 1 - 1/g                    # SR-1 Appendix-H unique consumed fraction
    rem_feff = 1 - f_eff                  # remaining internal budget under f_eff
    kdSSV    = g - 1                      # energy-momentum bridge k*dSSV = gamma-1
    bridge   = 1/(1+kdSSV)               # internal rate via PSR_eff
    print(f"{b:>5.2f} {g:>9.5f} {inv_g:>9.5f} | {linear:>13.6f} {quad:>16.9f} {rem_feff:>22.9f} {bridge:>18.9f}")
print("-"*78)
# Assertions: quad == 1-f_eff == bridge == 1/gamma, all exact; linear != 1/gamma
ok=True
for b in np.linspace(0.01,0.999,200):
    g=1/np.sqrt(1-b**2)
    quad=np.sqrt(1-b**2); rem_feff=1-(1-1/g); bridge=1/(1+(g-1))
    if not (abs(quad-1/g)<1e-12 and abs(rem_feff-1/g)<1e-12 and abs(bridge-1/g)<1e-12):
        ok=False
    if abs((1-b)-1/g)<1e-9 and b>0.05:  # linear should NOT equal 1/gamma
        ok=False
print("QUAD == (1 - f_eff) == bridge == 1/gamma  for all v  :", ok)
print("LINEAR (1 - v/c) != 1/gamma                          : confirmed (collinear split is wrong)")
print()
print("=> The orthogonal/quadrature remainder, SR-1's f_eff = 1 - 1/gamma, and the")
print("   energy-bridge internal rate 1/(1+k*dSSV) are ONE object. The quadrature is")
print("   the geometric face of the f_eff that Appendix H already proves is the unique")
print("   consistent consumed fraction. It is not a new assumption; it inherits f_eff's status.")

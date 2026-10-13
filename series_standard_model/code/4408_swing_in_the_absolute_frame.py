"""Patch 4408 -- founder (on 4407): yes, all motion is relative to the absolute frame; a CP swinging forward has a greater
absolute speed than the bulk, backward a smaller one; going backward its PSR is slightly larger and its time passes
slightly faster.  The hot ball pulls harder; every CP drifting with a mass generates increased SSV_abs; mass is the
fraction of partially exposed (unpaired) CPs producing DP-arcs and separation.

Check of his swing picture: each leg's clock runs at sqrt(1 - u^2) of the absolute rate, u its absolute speed (his
'PSR smaller when faster'; the corpus's energy bridge PSR_eff = l_P/gamma, kDeltaSSV = gamma - 1, VTD-1).  A CP swings at
speed w over length L in the body's own frame; the body moves at v.  Lab leg speeds by relativistic addition.
  (a) with the swing length contracted, L/gamma (his 4395 'Lorentz contraction' phrase points toward it; longitudinal only): cycle proper time unchanged, lab
      period gamma times longer -> the moving clock runs slow by exactly gamma, whatever the swing speed or direction;
  (b) without contraction: the longitudinal period is gamma^2 T0 (an extra gamma) while a transverse swing gives
      gamma T0 -> clocks would depend on their orientation and the absolute frame would show up (Michelson-Morley).
"""
import numpy as np

def cycle(v, w, L=1.0, contract=True):
    g = 1/np.sqrt(1 - v*v)
    Lp = L/g if contract else L
    up = (v + w)/(1 + v*w); um = (v - w)/(1 - v*w)
    tp = Lp/(up - v); tm = Lp/(v - um)
    T = tp + tm
    tau = tp*np.sqrt(1 - up*up) + tm*np.sqrt(1 - um*um)
    return T, tau, up, um

print("   v     w    forward u    backward u (signed)  lab period/(gamma T0)   proper time/tau0   [no contraction: period/(gamma T0)]")
for v in (0.3, 0.6, 0.9):
    for w in (0.2, 0.9, 0.999):
        T0 = 2/w; tau0 = T0*np.sqrt(1 - w*w); g = 1/np.sqrt(1 - v*v)
        T, tau, up, um = cycle(v, w)
        Tn, _, _, _ = cycle(v, w, contract=False)
        print(f"  {v:.1f}  {w:5.3f}   {up:7.4f}    {um:+8.4f}         {T/(g*T0):.6f}             {tau/tau0:.6f}"
              f"            [{Tn/(g*T0):.4f}]")
print("\n -> his picture (faster leg: smaller PSR, slower clock; slower leg: larger PSR, faster clock) gives exactly")
print("    gamma, with no CP exceeding light speed, provided the swing length contracts by gamma along the motion.")
print("    Without contraction a longitudinal swing runs slow by gamma^2 (bracketed column = gamma), a transverse one")
print("    by gamma: orientation-dependent clocks, which Michelson-Morley-type experiments exclude.")

print("\nNon-circular case: a CP swinging AT its cap (w = 1, one Planck sphere per Moment): both legs at light speed in")
print("any frame, so no velocity addition is used.")
for v in (0.3, 0.6, 0.9):
    g = 1/np.sqrt(1 - v*v); T0 = 2.0
    Tc = (1/g)/(1 - v) + (1/g)/(1 + v)          # contracted length L/g
    Tn = 1/(1 - v) + 1/(1 + v)                  # uncontracted
    Ttr = 2*np.sqrt(1/(1 - v*v))                # transverse swing, length 1 (path sqrt(1 + (v t)^2) at speed 1)
    Ttr_c = Ttr/g                               # transverse with transverse contraction too
    print(f"  v = {v}: longitudinal, contracted: {Tc/(g*T0):.6f} gamma T0; uncontracted: {Tn/(g*T0):.4f} gamma T0;"
          f" transverse: {Ttr/(g*T0):.6f} gamma T0; transverse also contracted: {Ttr_c/(g*T0):.4f} gamma T0")
print("  -> clocks of every orientation agree (gamma T0) only if lengths contract along the motion and not across it.")
print("\nCheck of circularity for w < 1: Galilean addition with L/gamma gives T/(gamma T0) = 1 - v^2 (0.91 at v = 0.3):")
print("  the exact gamma for slower swings comes from relativistic velocity addition, i.e. from SR kinematics.")

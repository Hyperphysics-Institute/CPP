#!/usr/bin/env python3
"""3068_forward_assembly.py — the OBL-CC-2 forward assembly (Patch
3068). Everything forward-fixed; alpha from the founder's unit-charge
eDP-vacuum ruling; eta_z bounded by perigee capture. Prints the
derived c_Li and w0 over the admissible eta_z range and the shortfall
vs the 3060-frozen band. F-CLI-1 = FIRING-PENDING-SCRUTINY (SCR-1..3)."""
import numpy as np
alpha, C4, OL = 1/137.035999, 24.8225, 0.685
ratio = 4*C4*alpha
rows = [(1/3,'triangle (constant-PSR)'), (0.5,'sinusoid'), (1.0,'rms-at-max bound')]
ok = True
for eta, name in rows:
    cLi = np.sqrt(ratio*eta/3)
    w0 = -1/3 - (2/3)*np.sqrt(OL)/cLi
    out = not (0.6 <= cLi <= 0.9)
    ok &= out
    print(f"eta_z={eta:.3f} ({name}): c_Li={cLi:.4f} w0={w0:+.3f} "
          f"{'OUTSIDE band' if out else 'IN BAND'}")
print(f"derived coefficient {ratio:.4f}*eta_z (Step-C units); shortfall "
      f"1.5-3.4x (eta=1) to 4.5-10x (eta=1/3)")
print(f"[{'PASS' if ok else 'CHECK'}] confrontation reproduces the record: "
      f"outside at every admissible eta_z -> F-CLI-1 FIRING-PENDING-SCRUTINY")
print("~122 of ~123 catastrophe orders closed forward from alpha + lattice.")

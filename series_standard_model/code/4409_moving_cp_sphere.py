"""Patch 4409 -- founder (on 4408): yes, the shrinking is not uniform; oblate compression along the motion only, no
side-to-side change; the moving CP's sphere is compressed at the front and elongated at the rear; the swing's average
velocity equals the bulk velocity; a backward-moving CP moves slower than the bulk's forward motion.

Part 1  the light sphere seen from a CP moving at v through the absolute frame: emitted from where the CP was, radius
        one PSR; after one Moment the CP has moved v forward: front 1 - v, rear 1 + v, across sqrt(1 - v^2).
        That is his 'compressed at the front, elongated at the rear', and it is 4397's shifted sphere with beta = v.
Part 2  round trips: along the motion 2L/(1 - v^2) (harmonic mean of front and rear), across 2L/sqrt(1 - v^2).  They
        agree only if lengths along the motion contract by sqrt(1 - v^2): his oblate compression, axial only.
Part 3  signed velocity vs speed in the swing: the backward leg's velocity is always below the bulk's (his point), but
        its speed (magnitude) can exceed the bulk's when the swing is fast; clocks depend on speed.
"""
import numpy as np
print("Part 1: reaches per Moment from a CP moving at v (absolute frame)")
for v in (0.1, 0.5, 0.9):
    print(f"  v = {v}: front {1-v:.3f}, rear {1+v:.3f}, across {np.sqrt(1-v*v):.3f}")

print("\nPart 2: light round trips over a rod of rest length 1")
for v in (0.1, 0.5, 0.9):
    along = 2/(1 - v*v); across = 2/np.sqrt(1 - v*v)
    along_c = 2*np.sqrt(1 - v*v)/(1 - v*v)
    print(f"  v = {v}: along {along:.4f}, across {across:.4f}; along with the rod contracted by sqrt(1-v^2): {along_c:.4f}")
print("  -> equal only with the contraction along the motion (and none across): his oblate compression")

print("\nPart 3: a swing of speed w (body frame) in a body moving at v; lab velocities by relativistic addition")
for v, w in ((0.3, 0.2), (0.3, 0.999), (0.01, 0.999)):
    up = (v + w)/(1 + v*w); um = (v - w)/(1 - v*w)
    print(f"  v = {v}, w = {w}: forward velocity {up:+.4f}, backward velocity {um:+.4f} (signed: below the bulk's {v});"
          f" backward speed {abs(um):.4f} {'<' if abs(um) < v else '>'} bulk speed")
print("  -> for a fast swing (the ZBW, near the cap) both legs move at nearly light speed in magnitude; the forward")
print("     leg lasts longer; the clock slowing is set by speeds, and comes out as gamma overall (4408).")

print("\nAverages (v = 0.3, w = 0.2): simple mean of the leg velocities vs time-weighted mean")
v, w = 0.3, 0.2
g = 1/np.sqrt(1 - v*v); L = 1/g
up = (v + w)/(1 + v*w); um = (v - w)/(1 - v*w)
tp = L/(up - v); tm = L/(v - um)
print(f"  simple mean {(up + um)/2:.4f}; time-weighted mean {(up*tp + um*tm)/(tp + tm):.4f}  (bulk {v})")
print("  -> 'averages to the bulk velocity' holds time-weighted exactly; the simple mean only non-relativistically")

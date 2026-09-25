#!/usr/bin/env python3
"""4291 -- founders_voice/4291: outer -eCP on a circle of radius R at angular rate w_o; inner +eCP on a spirograph
through the core, reaching the circle, its tangent (petal-tip) point advancing the SAME way.  Model: the inner
swings along a line through the core, r(t) = R cos(w_r t), while the line turns at W (a rose curve, r = R cos((w_r/W) theta)).
Moment per CP mu = (q/2)<r x v>, angular momentum L = m <r x v> (4288: m = moving inertia).  Units R = 1, e = 1."""
import numpy as np
print("(1) exact sweep of a rose through the centre: r x v = r^2 dtheta/dt = r^2 W, so <r x v> = W <r^2> = W R^2/2")
for wr,W in ((1.0,0.5),(3.0,1.0),(1.0,2.0),(5.0,0.3)):
    t=np.linspace(0,2*np.pi*200/min(wr,W),4_000_001); r=np.cos(wr*t); th=W*t
    x,y=r*np.cos(th),r*np.sin(th); vx,vy=np.gradient(x,t),np.gradient(y,t)
    print(f"  w_r = {wr}, W = {W}:  <r x v> traced = {np.mean(x*vy-y*vx):.5f}   W/2 = {W/2:.5f}")
print("  -> the pass through the core carries nothing; all of the inner's spin and magnet come from the turning of its line.")

print("\n(2) a line through the core cannot turn under the core's pull alone: a central force keeps L = 0, so the swing")
print("    stays on one fixed line (W = 0). The turning must come from the partner: the orbiting outer -eCP pulls the inner")
print("    +eCP around. L is exchanged within the pair; only the total is conserved.")

print("\n(3) both circulating the same way: spins ADD, magnets OPPOSE (4290 rows 1).  With x = W/w_o:")
print("    S  = R^2 (m_o w_o + m_i W/2)        mu = (e/2) R^2 (-w_o + W/2)")
print("    g  = m_e (1 - x/2) / (m_o + m_i x/2)     [measured g = 2]")
for x in (0.0,0.5,1.0,2.0):
    for mo,mi in ((0.5,0.5),(1/6,1/6)):
        g=(1-x/2)/(mo+mi*x/2)
        print(f"  tips advance at W = {x:.1f} w_o, m_o = {mo:.3f}, m_i = {mi:.3f} m_e:  g = {g:.3f}"
              + ("   <- the inner's magnet cancels the outer's exactly" if x==2.0 and mo==0.5 else ""))
print("  g = 2 needs  m_o + m_i x/2 = m_e (1 - x/2)/2;  impossible for x >= 2 (no magnet left).")

print("\n(4) if the inner meets its partner at every petal tip (tips alternate sides, one swing out-through-out per w_r):")
print("    tip n at angle W n pi/w_r + n pi must equal the outer's w_o n pi/w_r  ->  W = w_o + (2j - 1) w_r")
for wr in (1.0,):
    print(f"  w_r = w_o:  j = 0 -> W = {1-wr:.1f} w_o (fixed diameter)   j = 1 -> W = {1+wr:.1f} w_o (tips at TWICE the outer's rate: g = 0)")
print("\n(4b) numeric check: angle between each petal tip and the outer -eCP at that moment (0 = they meet)")
wo=1.0
for wr,W,lab in ((1.0,0.0,"j=0, w_r=w_o"),(1.0,2.0,"j=1, w_r=w_o"),(0.5,0.5,"j=0, w_r=w_o/2"),(0.5,1.5,"j=1, w_r=w_o/2"),(1.0,1.0,"W=w_o (not a solution)")):
    gaps=[]
    for n in range(1,9):
        t=n*np.pi/wr; r=np.cos(wr*t); tip=np.angle(np.exp(1j*W*t)*np.sign(r)); out=np.angle(np.exp(1j*wo*t))
        gaps.append(abs(np.angle(np.exp(1j*(tip-out)))))
    print(f"  {lab:24s} W = {W:.1f}: max tip-to-partner angle over 8 tips = {max(gaps):.2e} rad")

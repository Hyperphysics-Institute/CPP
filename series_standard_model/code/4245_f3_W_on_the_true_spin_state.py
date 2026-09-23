#!/usr/bin/env python3
"""4245 -- TODO-4240-F3STATE: 4134's W = sum_i s_i V_i and 4136's bounds used the product state s = (+1,+1,-1).
The proton's J = 1/2 state (4240 Part A) has <2 s_i> = (+2/3, +2/3, -1/3). Same V_i as 4134 (SS-2 triangle, 1/r^2 law)."""
import numpy as np
duu,dud=1.071,0.620; h=np.sqrt(dud**2-(duu/2)**2)
pos=np.array([[-duu/2,0,0],[duu/2,0,0],[0,h,0]]); chg=np.array([2/3,2/3,-1/3])
V=np.zeros_like(pos)
for i in range(3):
    for j in range(3):
        if i!=j: r=pos[i]-pos[j]; V[i]+=chg[i]*chg[j]*r/np.linalg.norm(r)**3
Wp=(np.array([1,1,-1.])[:,None]*V).sum(0); Wt=(np.array([2/3,2/3,-1/3])[:,None]*V).sum(0)
print(f"sum_i V_i = {np.linalg.norm(V.sum(0)):.1e} (action-reaction)")
print(f"|W| product state (4134) = {np.linalg.norm(Wp):.4f}   |W| true J=1/2 state = {np.linalg.norm(Wt):.4f}   ratio = {np.linalg.norm(Wt)/np.linalg.norm(Wp):.4f}")
print("identity: with sum V = 0, W = sum s_i V_i = (s_d - s_u) V_d: product (-1-1) = -2 V_d, true (-1/3-2/3) = -1 V_d -> exactly half")
rms_p=0.67; print(f"rms <n.W> per nucleon: 4134 {rms_p:.2f} -> {rms_p*np.linalg.norm(Wt)/np.linalg.norm(Wp):.2f} (expectation value; operator fluctuations not included)")
Wb=1.1654; eps_p=1e-7/Wb; eps_t=1e-7/(Wb/2)
print(f"4136 E1 bound: eps <= {eps_p:.1e} -> {eps_t:.1e};  g <= {3*eps_p:.1e} -> {3*eps_t:.1e}  (Langevin, eps = g/3)")
print("-> isotropy result <n.W> = 0 unchanged (independent of the spin state); bounds loosen by exactly 2; the 'excluded by seven orders' reading unchanged.")

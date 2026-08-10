#!/usr/bin/env python3
"""3067_stage3_measurement_calibration.py — OBL-CC-2 Stage 3 verify
(Patch 3067): (1) M-q^2 instrument reading through the committed
engine (envelope = 1/4pi); (2) C4(FCC, nn=1) = 24.8225 (z=12
corpus-forced); (3) the assembled structure ratio 4*C4 = 99.29
multiplying alpha_q (the one named open input; its demanded value is
deliberately NOT computed — anti-extraction)."""
import importlib.util, os, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
ENG = os.path.normpath(os.path.join(HERE,
  '../../../../flagship_papers/electromagnetism/code/2902_mobile_sea_engine.py'))
spec = importlib.util.spec_from_file_location('eng', ENG)
eng = importlib.util.module_from_spec(spec); spec.loader.exec_module(eng)
a, D0 = 2.5, eng.D0
xs = a*np.arange(-3,4)
cent = np.array([[x,y,z] for x in xs for y in xs for z in xs if (x,y,z)!=(0,0,0)],float)
d = np.zeros_like(cent); d[:,2] = 1.0
pos = np.concatenate([[[0.,0.,0.]], cent+0.5*D0*d, cent-0.5*D0*d])
q = np.concatenate([[1.0], np.ones(len(cent)), -np.ones(len(cent))])
hist = eng.History(pos, 0.0, 62, 4)
radii = np.linspace(5,15,11)
dirs = np.array([[1,0,0],[0,1,0],[0,0,1],[1,1,1]/np.sqrt(3)])
recv = np.array([r*u for r in radii for u in dirs])
ridx = np.full(len(recv), -1)
tr, amp, uvec = eng.field_at(recv, ridx, hist, 0, 60.0)
A = float(np.mean(amp[:,0]*np.repeat(radii,len(dirs))**2))
ok1 = abs(A - 1/(4*np.pi)) < 1e-4
n = np.arange(-40,41)
P = np.stack(np.meshgrid(n,n,n,indexing='ij'),-1).reshape(-1,3).astype(float)
P = P[(P.sum(1)%2)==0]; P = P[np.any(P!=0,1)]
C4 = 4*float(np.sum(1.0/np.sum(P**2,1)**2))
ok2 = abs(C4 - 24.8225) < 0.01
print(f"[{'PASS' if ok1 else 'FAIL'}] M-q^2 envelope = {A:.6f} (1/4pi = {1/(4*np.pi):.6f})")
print(f"[{'PASS' if ok2 else 'FAIL'}] C4(FCC, nn=1) = {C4:.4f}")
print(f"assembled: rho_L = (C4 alpha_q / 2pi) hbar c / (l_P^2 R_h^2); "
      f"derived/StepC = 4*C4*alpha_q = {4*C4:.2f}*alpha_q")
print("alpha_q: OPEN (FQ-2); demanded value NOT computed (anti-extraction).")
print(f"{int(ok1)+int(ok2)}/2 PASS")

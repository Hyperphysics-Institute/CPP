#!/usr/bin/env python3
"""
Patch 2968 — K-MEM-MEAS-1 execution driver, under the FROZEN 2967 prereg
(`kmem_meas1_prereg.md`). The prereg is authoritative; this driver only
sequences the committed 2902 engine's step and records the source force.

Usage: python3 2968_kmem_step_driver.py {L1|L2|L3} [budget_seconds]
Checkpoints to /tmp/kmem_{leg}.npz (exact-state resume: History array,
positions, t, force record). Verdict-relevant outputs are archived by
the analysis step into series_phenomena/cosmology/dark_matter/data/.
"""
import importlib.util
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, '../../../../flagship_papers/electromagnetism/code/'
                         '2902_mobile_sea_engine.py')
spec = importlib.util.spec_from_file_location('eng', os.path.normpath(SRC))
eng = importlib.util.module_from_spec(spec)
spec.loader.exec_module(eng)

# ---- frozen leg definitions (2967 §3) -----------------------------------
LEGS = {
    'L1': dict(rho=(1.0, 8.0), x_half=16.0, t_step=24, beta_f=0.10,
               T_ball=36, t_end=240, x_src0=-10.8),
    'L2': dict(rho=(1.0, 8.0), x_half=16.0, t_step=None, beta_f=0.0,
               T_ball=36, t_end=144, x_src0=0.0),
    'L3': dict(rho=(1.0, 6.0), x_half=12.0, t_step=24, beta_f=0.10,
               T_ball=27, t_end=186, x_src0=-8.1),
}


def init_state(leg):
    L = LEGS[leg]
    sea, qs, _ = eng.build_sea(L['rho'][0], L['rho'][1],
                               -L['x_half'], L['x_half'], 2.5)
    pos = np.concatenate([[[L['x_src0'], 0.0, 0.0]], sea])
    q = np.concatenate([[1.0], qs])
    T_max = np.sqrt((2 * L['x_half'] + 20) ** 2 + (2 * L['rho'][1]) ** 2) + 5
    hist = eng.History(pos, 0.0, int(np.ceil(T_max)) + 2, L['t_end'])
    return pos, q, hist, T_max


def save_ck(path, pos, q, hist, t, F, AB):
    np.savez(path, pos=pos, q=q, H=hist.H, t_now=hist.t_now,
             T_pre=hist.T_pre, t=t, F=np.array(F), AB=np.array(AB))


def load_ck(path, leg):
    z = np.load(path)
    L = LEGS[leg]
    pos, q = z['pos'], z['q']
    T_max = np.sqrt((2 * L['x_half'] + 20) ** 2 + (2 * L['rho'][1]) ** 2) + 5
    hist = eng.History(pos, 0.0, int(z['T_pre']), L['t_end'])
    hist.H = z['H']
    hist.t_now = int(z['t_now'])
    return pos, q, hist, T_max, int(z['t']), list(z['F']), list(z['AB'])


def main():
    leg = sys.argv[1]
    budget = float(sys.argv[2]) if len(sys.argv) > 2 else 170.0
    L = LEGS[leg]
    ck = f"/tmp/kmem_{leg}.npz"
    if os.path.exists(ck):
        pos, q, hist, T_max, t, F, AB = load_ck(ck, leg)
        print(f"[{leg}] resume at t={t}")
    else:
        pos, q, hist, T_max = init_state(leg)
        t, F, AB = 0, [], []
        print(f"[{leg}] fresh start; N={len(pos)} CPs; t_end={L['t_end']}")
    tr = None
    t0 = time.time()
    while t < L['t_end']:
        beta = (L['beta_f'] if (L['t_step'] is not None and t >= L['t_step'])
                else 0.0)
        pos, src_net, src_ab, tr = eng.moment_step(
            pos, q, hist, t, T_max, beta, mobile_sea=True, tr_guess=tr)
        hist.append(pos)
        F.append(float(src_net[0]))
        AB.append(float(src_ab))
        t += 1
        if time.time() - t0 > budget:
            save_ck(ck, pos, q, hist, t, F, AB)
            print(f"[{leg}] checkpoint at t={t}/{L['t_end']} "
                  f"({time.time()-t0:.0f}s)")
            return 1
    save_ck(ck, pos, q, hist, t, F, AB)
    out = {'leg': leg, 'F': F, 'AB': AB, **{k: v for k, v in L.items()
                                            if k != 'rho'},
           'rho': list(L['rho'])}
    with open(f"/tmp/kmem_{leg}_done.json", 'w') as fh:
        json.dump(out, fh)
    print(f"[{leg}] COMPLETE t={t} ({time.time()-t0:.0f}s)")
    return 0


if __name__ == '__main__':
    sys.exit(main())

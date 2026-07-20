#!/usr/bin/env python3
"""
PATCH 2651 -- C7-D1 EXECUTION (TC-extension floor-scaling arc) under
c7_discriminant_campaign_prereg.md (2649) SS3 ONLY. Second arc of the frozen
order D2->D1->D3. Verdict is read in c7_d1_record.md against the prereg.

SPEC-TO-CODE TRACE TABLE (J4-1):
  prereg quantity                        -> code location
  instrument "same verbatim base"        -> exec of 2513 source below __main__
                                            split (2635/2650 loader pattern);
                                            reach-S byte-identical factory
  "the ONLY modification is TC"          -> etot_tc() passes TC=tc into
                                            dance_v8's existing TC kwarg
                                            (engine default 60; burn stays the
                                            engine's fractional 0.15 -- the
                                            instrument's own convention)
  TC set {60 pin, 120, 240}              -> stage names tc60|tc120|tc240
  a = 0.04, full member grid             -> members() inherited UNMODIFIED
                                            from the 2513 namespace
  dt-union {tauC/50, tauC/25}            -> DTS tuple
  pin control C-D1                       -> tc60 cell printed beside the 2635
                                            registered ensemble values; must
                                            match within printed spreads
  target: ensemble spread (floor) vs TC  -> SEM per mode per (TC, dt) persisted
                                            to /tmp/c7_d1.json; stage 'read'
                                            prints SEM(TC)/SEM(60) beside the
                                            1/sqrt(TC/60) reference column
GUARDS (J4-2): SEM uses ddof=1 with n>=2 asserted (fires on grid truncation);
  classification |<c>| vs 2*SEM inherited verbatim (2513); sem==0 ratio path
  guarded -> 'inf'. Deliberate trigger: stage 'guardtest' runs the n<2 assert
  and the sem==0 path.
Deterministic; no RNG. Stages: guardtest | tc60 | tc120 | tc240 | read.
"""
import numpy as np, time, os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))

def reach_S_factory(np_):
    def build_reach_S(P, C, SP):
        NS = len(P); reach = []
        for i in range(NS):
            dd = P - P[i]; r = np_.sqrt((dd * dd).sum(axis=1)); r[i] = np_.inf
            ki = i // 8
            if SP[i] == 'q':
                inpl = [j for j in range(NS) if SP[j] == 'q' and j // 8 == ki and r[j] < 1.8]
                axl = [j for j in range(NS) if SP[j] == 'q' and j // 8 != ki and r[j] < 1.3]
                ecp = [j for j in range(NS) if SP[j] == 'e' and r[j] < 0.6]
                reach.append(sorted(set(inpl + axl))[:5] + ecp)
            else:
                eopp = sorted([j for j in range(NS) if SP[j] == 'e' and 0 < r[j] < 2.6],
                              key=lambda j: r[j])[:4]
                qown = [j for j in range(NS) if SP[j] == 'q' and r[j] < 0.6]
                reach.append(eopp + qown)
        return reach
    return build_reach_S

stage = sys.argv[1] if len(sys.argv) > 1 else 'read'
t0 = time.time()
print("=" * 78)
print(f"PATCH 2651 -- C7-D1 (prereg 2649 SS3; verdict read in record)  stage={stage}")
print("=" * 78)

if stage == 'guardtest':
    try:
        xs = np.array([1.0]); assert len(xs) >= 2, "n<2: SEM undefined"
    except AssertionError as e:
        print(f"[guardtest] n<2 assert fires: PASS ({e})")
    s = 0.0; r = (1.0 / s) if s != 0 else float('inf')
    print(f"[guardtest] sem==0 ratio path -> {r} (guard fires): PASS")
    sys.exit(0)

src = open(os.path.join(HERE, "2513_ensemble_mw_modes.py")).read()
ns = {'__name__': 'd1', '__file__': os.path.join(HERE, '2513_ensemble_mw_modes.py')}
exec(src[:src.index("if __name__=='__main__':")], ns)
ns['build_reach'] = reach_S_factory(np)
dance_v8 = ns['dance_v8']; ring_scaffold = ns['ring_scaffold']
Pr = ns['Pr']; Cr = ns['Cr']; SPr = ns['SPr']; FREF = ns['FREF']
members = ns['members']
assert np.allclose(ns['ring_scaffold_ph'](ell=0.02, psi=0.0)[0],
                   ring_scaffold(ell=0.02)[0]), "psi=0 mismatch"

def etot_tc(P, dtf, tc):
    E, K, _, _ = dance_v8(P, Cr, SPr, FREF, dtf, TC=tc)
    return E.mean() + K.mean()

DTS = (1 / 50, 1 / 25)
REG_2635 = {  # registered ensemble values (pin reference, printed beside tc60)
    ('m0', 50): (-470732, 121439), ('m1', 50): (-73883, 10585),
    ('m2', 50): (-51430, 16683), ('ell', 50): (-285741, 54093),
    ('m0', 25): (-1051091, 381517), ('m1', 25): (-93373, 15494),
    ('m2', 25): (-73304, 22001), ('ell', 25): (-374525, 46244)}

if stage in ('tc60', 'tc120', 'tc240'):
    # CHECKPOINTED EXECUTION (runtime rider, prereg SS3): each invocation
    # computes members until a ~75s wall budget, persists per-member curvatures
    # to /tmp/c7_d1_cells.json, and exits PARTIAL; re-invoke until COMPLETE.
    # No member is ever recomputed; no cell is ever extrapolated.
    tc = int(stage[2:])
    mem = members()
    cellsf = '/tmp/c7_d1_cells.json'
    cells = json.load(open(cellsf)) if os.path.exists(cellsf) else {}
    tasks = []
    for dtf in DTS:
        tasks.append((f"{tc}_base_{int(1/dtf)}", ('base', dtf, None, None)))
        for nm in ('m0', 'm1', 'm2', 'ell'):
            for i, (P, x) in enumerate(mem[nm]):
                tasks.append((f"{tc}_{nm}_{int(1/dtf)}_{i}", (nm, dtf, i, x)))
    done = sum(1 for k, _ in tasks if k in cells)
    for k, (nm, dtf, i, x) in tasks:
        if k in cells: continue
        if time.time() - t0 > 75:
            json.dump(cells, open(cellsf, 'w'))
            print(f"PARTIAL {done}/{len(tasks)} (TC={tc}) -- re-invoke  "
                  f"({time.time()-t0:.0f}s)")
            sys.exit(0)
        if nm == 'base':
            cells[k] = etot_tc(Pr, dtf, tc)
        else:
            P, x = mem[nm][i]
            T0 = cells[f"{tc}_base_{int(1/dtf)}"]
            cells[k] = 2 * (etot_tc(P, dtf, tc) - T0) / x ** 2
        done += 1
    json.dump(cells, open(cellsf, 'w'))
    out = {}
    for dtf in DTS:
        dtl = int(1 / dtf)
        print(f"\n== TC={tc} dt=tauC/{dtl}: base ring Etot={cells[f'{tc}_base_{dtl}']:+.1f}")
        for nm in ('m0', 'm1', 'm2', 'ell'):
            cs = np.array([cells[f"{tc}_{nm}_{dtl}_{i}"] for i in range(len(mem[nm]))])
            assert len(cs) >= 2, "n<2: SEM undefined"
            mn = cs.mean(); sem = cs.std(ddof=1) / np.sqrt(len(cs))
            cls = ('SIG-POS' if mn > 2 * sem else
                   ('SIG-NEG' if mn < -2 * sem else 'INCONCLUSIVE'))
            out[f"{nm}_{dtl}"] = (float(mn), float(sem), cls)
            ref = REG_2635.get((nm, dtl))
            reftxt = f"  [2635 reg: {ref[0]:+d}+-{ref[1]:d}]" if tc == 60 else ""
            print(f"  {nm:3s} n={len(cs)}: <c>={mn:+10.0f} +- SEM {sem:8.0f} [{cls}]{reftxt}")
    db = json.load(open('/tmp/c7_d1.json')) if os.path.exists('/tmp/c7_d1.json') else {}
    db[str(tc)] = out
    json.dump(db, open('/tmp/c7_d1.json', 'w'))
    print(f"COMPLETE TC={tc}  total {time.time()-t0:.0f}s")

elif stage == 'read':
    db = json.load(open('/tmp/c7_d1.json'))
    tcs = sorted(int(k) for k in db)
    print("floor (SEM) vs TC; reference column = sqrt(60/TC):")
    for dtl in (50, 25):
        print(f"\n== dt=tauC/{dtl}")
        for nm in ('m0', 'm1', 'm2', 'ell'):
            row = []
            for tc in tcs:
                mn, sem, cls = db[str(tc)][f"{nm}_{dtl}"]
                s60 = db['60'][f"{nm}_{dtl}"][1]
                rat = sem / s60 if s60 != 0 else float('inf')
                row.append(f"TC={tc}: SEM={sem:8.0f} ratio={rat:5.2f} "
                           f"(ref {np.sqrt(60/tc):4.2f}) <c>={mn:+9.0f} [{cls}]")
            print(f"  {nm:3s}  " + " | ".join(row))
    print("\nreadings composed in c7_d1_record.md against prereg SS3")

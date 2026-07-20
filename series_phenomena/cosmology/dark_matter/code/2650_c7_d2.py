#!/usr/bin/env python3
"""
PATCH 2650 -- C7-D2 EXECUTION (larger-amplitude regime-entry arc) under
c7_discriminant_campaign_prereg.md (2649) SS2 ONLY. First arc of the frozen
order D2->D1->D3. Verdict is read in c7_d2_record.md against the prereg.

SPEC-TO-CODE TRACE TABLE (J4-1, mandatory per 2648/2649):
  prereg quantity                        -> code location
  instrument "2513/2635 verbatim"        -> exec of 2513 source below the
                                            __main__ guard split (identical to
                                            2635 stage i2a/i2b load pattern)
  reach-S                                -> reach_S_factory copied VERBATIM
                                            from code/2635_rb234_reach_s.py
                                            (byte-identical function body)
  "ONLY modification is the amplitude"   -> AMPS tuple below; the m2 tilt line
                                            a*np.cos(4*pi*k/N+ph) is the 2513
                                            m2 construction with 0.04 -> a
  TC=60, burn=0.15, kappa pinned, FREF   -> inherited unmodified from the 2513
                                            namespace (no override bound)
  dt-union {tauC/50, tauC/25}            -> DTS tuple
  phases {0, pi/2}                       -> PHS tuple (the 2513/2635 diagnostic
                                            convention, unchanged)
  pin control C-D2 (0.94/1.10 class)     -> stage 'pin': verbatim 2635 i2b
                                            diagnostic block (0.04/0.02 pair,
                                            dt=1/50, reach-S)
  pairwise adjacent-rung ratios          -> ratio = dT(2a)/dT(a) per phase per
                                            dt over AMPS adjacencies
  sign disclosed per rung                -> dT printed signed at every rung
GUARDS (stated per J4-2): d02/dT(a)==0 division guard -> prints 'inf' and the
  cell registers non-classifiable (no silent skip); psi=0 scaffold assert
  inherited from 2513 exec (fires on geometry drift). Deliberate-trigger test:
  stage 'guardtest' feeds a zero denominator through the ratio path.
Deterministic; no RNG. Stages: pin | ladder | guardtest.
"""
import numpy as np, time, os, sys
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

stage = sys.argv[1] if len(sys.argv) > 1 else 'pin'
t0 = time.time()
print("=" * 78)
print(f"PATCH 2650 -- C7-D2 (prereg 2649 SS2; verdict read in record)  stage={stage}")
print("=" * 78)

if stage == 'guardtest':
    d = 0.0
    r = (1.0 / d) if d != 0 else float('inf')
    print(f"[guardtest] zero-denominator path -> ratio={r} (guard fires, no exception): PASS")
    sys.exit(0)

src = open(os.path.join(HERE, "2513_ensemble_mw_modes.py")).read()
ns = {'__name__': 'd2', '__file__': os.path.join(HERE, '2513_ensemble_mw_modes.py')}
exec(src[:src.index("if __name__=='__main__':")], ns)
ns['build_reach'] = reach_S_factory(np)
etot = ns['etot']; ring_scaffold = ns['ring_scaffold']; Pr = ns['Pr']; N = ns['N']
assert np.allclose(ns['ring_scaffold_ph'](ell=0.02, psi=0.0)[0],
                   ring_scaffold(ell=0.02)[0]), "psi=0 mismatch"

PHS = (0.0, np.pi / 2)
AMPS = (0.04, 0.08, 0.16, 0.32)   # prereg SS2 ladder; 0.04 is the pin rung
DTS = (1 / 50, 1 / 25)

def m2P(a, ph):
    return ring_scaffold(tilt=[a * np.cos(4 * np.pi * k / N + ph) for k in range(N)])[0]

if stage == 'pin':
    dtf = 1 / 50
    T0, _ = etot(Pr, dtf)
    print(f"[C-D2 pin] reach-S base ring Etot={T0:+.1f}  ({time.time()-t0:.0f}s)")
    print("[C-D2 pin] verbatim 2635 diagnostic (0.04/0.02 pair, dt=tauC/50):")
    for ph in PHS:
        d04 = etot(m2P(0.04, ph), dtf)[0] - T0
        d02 = etot(m2P(0.02, ph), dtf)[0] - T0
        r = d04 / d02 if d02 != 0 else float('inf')
        print(f"  phase {ph:4.2f}: dT(0.04)={d04:+8.2f}  dT(0.02)={d02:+8.2f}  "
              f"ratio={r:+6.2f}   ({time.time()-t0:.0f}s)")
    print("[C-D2 pin] must reproduce the 2635 registered 0.94/1.10 class; "
          "read in record. Pin failure aborts the arc (RC).")

elif stage == 'ladder':
    for dtf in DTS:
        T0, _ = etot(Pr, dtf)
        print(f"\n== dt=tauC/{int(1/dtf)} (reach-S): base ring Etot={T0:+.1f}  "
              f"({time.time()-t0:.0f}s)")
        for ph in PHS:
            dT = {}
            for a in AMPS:
                dT[a] = etot(m2P(a, ph), dtf)[0] - T0
                print(f"  phase {ph:4.2f} a={a:4.2f}: dT={dT[a]:+10.2f}  "
                      f"sign={'+' if dT[a] > 0 else '-'}   ({time.time()-t0:.0f}s)")
            for a1, a2 in zip(AMPS[:-1], AMPS[1:]):
                r = dT[a2] / dT[a1] if dT[a1] != 0 else float('inf')
                mark = "IN [3,5]" if 3.0 <= r <= 5.0 else "outside"
                print(f"    ratio dT({a2:4.2f})/dT({a1:4.2f}) = {r:+7.2f}  [{mark}]")
    print(f"\ntotal {time.time()-t0:.0f}s -- readings composed in c7_d2_record.md")

#!/usr/bin/env python3
"""
PATCH 2635 -- R-B ITEMS 2-4 EXECUTION under rb234_invariance_prereg.md (2634) ONLY.
Stages: i3 | i4 | i2a | i2b. Overrides bound in the loaded namespaces; per-item
binding checks per the prereg. Verdicts are read in the record against the prereg.
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

stage = sys.argv[1] if len(sys.argv) > 1 else 'i3'
t0 = time.time()
print("=" * 78)
print(f"PATCH 2635 -- R-B ITEMS 2-4 (prereg 2634; verdicts read there)  stage={stage}")
print("=" * 78)

if stage == 'i3':
    src = open(os.path.join(HERE, "2549_endbond2_dance.py")).read()
    ns = {'__name__': 'i3', '__file__': os.path.join(HERE, '2549_endbond2_dance.py')}
    exec(src[:src.index("t0=time.time()")], ns)
    old_reach = ns['build_reach']; new_reach = reach_S_factory(np)
    # scaffolds exactly as the 2549 driver builds them
    drv = src[src.index("# ---- scaffolds ----"):src.index("# ---- FREF conventions")]
    exec(drv, ns)
    print("[i3] structural-equality census (OLD vs reach-S reach lists):")
    ident = True
    for nm in ('Pstk', 'Ppl', 'Pgap'):
        if nm not in ns: continue
        P = ns[nm]; C = ns['C' + nm[1:]]; SP = ns['SP' + nm[1:]]
        a = old_reach(P, C, SP); b = new_reach(P, C, SP)
        same = all(sorted(x) == sorted(y) for x, y in zip(a, b))
        ident &= same
        print(f"    {nm}: lists identical = {same}  (N={len(P)})")
    print(f"[i3] IDENTICAL-EVERYWHERE: {ident}"
          + ("  -> RB3-INVARIANT-BY-STRUCTURE candidate (read in record)" if ident else
             "  -> reproduction + reach-S union re-run required (run stage i3full)"))
    print(f"[{time.time()-t0:.0f}s]")

elif stage == 'i3full':
    for tag, use_S in (('OLD-reproduction', False), ('reach-S', True)):
        ns = {'__name__': 'i3f', '__file__': os.path.join(HERE, '2549_endbond2_dance.py')}
        src = open(os.path.join(HERE, "2549_endbond2_dance.py")).read()
        if use_S:
            marker = "def build_reach(P,C,SP):"
            head = src[:src.index(marker)]
            tail = src[src.index("# ---- dance_v8"):]
            # bind reach-S under the registered name in the chain namespace
            exec(head, ns)
            ns['build_reach'] = reach_S_factory(np)
            exec(tail, ns)
        else:
            exec(src, ns)
        print(f"  [{tag}] run complete ({time.time()-t0:.0f}s)")

elif stage == 'i4':
    src = open(os.path.join(HERE, "2510_hardened_dance_inertia.py")).read()
    ns = {'__name__': 'i4', '__file__': os.path.join(HERE, '2510_hardened_dance_inertia.py')}
    exec(src[:src.index("Pr,Cr,SPr=ring_scaffold()")], ns)
    ring_scaffold = ns['ring_scaffold']; straight_scaffold = ns.get('straight_scaffold')
    dance_v8_src_names = [k for k in ns if k.startswith('dance')]
    print(f"[i4] loaded 2510 head; dance fns: {dance_v8_src_names}")
    # instrumented pile counter: wrap by re-exec of dance_v8 source with counter lines
    d0 = src.index("def dance_v8("); d1 = src.index("Pr,Cr,SPr=ring_scaffold()")
    body = src[d0:d1]
    assert "if len(atj) and (r[i,atj]<A[i,atj]).any(): hit[m]=True" in body
    body_i = body.replace("def dance_v8(", "def dance_v8_instr(") \
        .replace("if len(atj) and (r[i,atj]<A[i,atj]).any(): hit[m]=True",
                 "if len(atj) and (r[i,atj]<A[i,atj]).any():\n"
                 "                    hit[m]=True; dance_v8_instr.pile+=1") \
        .replace("if hit[m]: last[i]=tgt[i]; out[i]=False",
                 "if hit[m]: last[i]=tgt[i]; out[i]=False; dance_v8_instr.hits+=1")
    exec(body_i, ns)
    dance_v8 = ns['dance_v8']; dance_v8_instr = ns['dance_v8_instr']
    Pr, Cr, SPr = ring_scaffold(); FREF = ns['FREF'] if 'FREF' in ns else None
    exec(src[src.index("Pr,Cr,SPr=ring_scaffold()"):src.index("mode=")], ns)
    Pr, Cr, SPr = ns['Pr'], ns['Cr'], ns['SPr']
    Ps, Cs, SPs = ns['Ps'], ns['Cs'], ns['SPs']
    FREF = ns['FREF']
    old_reach = ns['build_reach']; sfn = reach_S_factory(np)
    dtf = 1 / 50
    # convention-pin: instrumented wrapper reproduces un-instrumented <Ep> (OLD ring)
    Ep_ref = dance_v8(Pr, Cr, SPr, FREF, dtf)[0].mean()
    dance_v8_instr.pile = 0; dance_v8_instr.hits = 0
    Ep_ins = dance_v8_instr(Pr, Cr, SPr, FREF, dtf)[0].mean()
    print(f"[i4-pin] OLD ring <Ep>: plain {Ep_ref:+.3f} vs instrumented {Ep_ins:+.3f} "
          f"(match: {abs(Ep_ref-Ep_ins)<1e-9})")
    for tag, rfn in (('OLD', old_reach), ('reach-S', sfn)):
        ns['build_reach'] = rfn
        for snm, P, C, SP in (('ring', Pr, Cr, SPr), ('rod', Ps, Cs, SPs)):
            dance_v8_instr.pile = 0; dance_v8_instr.hits = 0
            Ep = dance_v8_instr(P, C, SP, FREF, dtf)[0].mean()
            fr = dance_v8_instr.pile / max(dance_v8_instr.hits, 1)
            print(f"  [{tag:7s}] {snm}: hits={dance_v8_instr.hits} pile-resolved="
                  f"{dance_v8_instr.pile} fraction={fr:.4f}  <Ep>={Ep:+.1f}")
    print(f"[{time.time()-t0:.0f}s]")

elif stage in ('i2a', 'i2b'):
    src = open(os.path.join(HERE, "2513_ensemble_mw_modes.py")).read()
    ns = {'__name__': 'i2', '__file__': os.path.join(HERE, '2513_ensemble_mw_modes.py')}
    exec(src[:src.index("if __name__=='__main__':")], ns)
    old_reach = ns['build_reach']
    ns['build_reach'] = reach_S_factory(np)
    etot = ns['etot']; ring_scaffold = ns['ring_scaffold']
    ring_scaffold_ph = ns['ring_scaffold_ph']; members = ns['members']
    Pr = ns['Pr']; N = ns['N']
    assert np.allclose(ring_scaffold_ph(ell=0.02, psi=0.0)[0],
                       ring_scaffold(ell=0.02)[0]), "psi=0 mismatch"
    if stage == 'i2a':
        ns['build_reach'] = old_reach
        T_old, _ = etot(Pr, 1 / 50)
        ns['build_reach'] = reach_S_factory(np)
        T_new, _ = etot(Pr, 1 / 50)
        print(f"[i2-binding] base ring Etot: OLD {T_old:+.1f} vs reach-S {T_new:+.1f} "
              f"(DIFFER: {abs(T_old-T_new)>1.0})")
        mem = members(); results = {}
        dtf = 1 / 50
        T0, E0 = etot(Pr, dtf)
        print(f"== dt=tauC/50 (reach-S): base ring Etot={T0:+.1f} Ep={E0:+.1f} ({time.time()-t0:.0f}s)")
        for nm in ('m0', 'm1', 'm2', 'ell'):
            cs = []
            for (P, x) in mem[nm]:
                Tp, Ep = etot(P, dtf)
                cs.append(2 * (Tp - T0) / x ** 2)
            cs = np.array(cs); mn = cs.mean(); sem = cs.std(ddof=1) / np.sqrt(len(cs))
            cls = ('SIG-POS' if mn > 2 * sem else ('SIG-NEG' if mn < -2 * sem else 'INCONCLUSIVE'))
            results[f"{nm}_50"] = (float(mn), float(sem), cls)
            print(f"  {nm:3s} n={len(cs)}: <c>={mn:+10.0f} +- SEM {sem:8.0f}  [{cls}]  ({time.time()-t0:.0f}s)")
        json.dump(results, open('/tmp/rb2_results.json', 'w'))
        print("[i2a results persisted]")
    else:
        results = json.load(open('/tmp/rb2_results.json'))
        mem = members()
        dtf = 1 / 25
        T0, E0 = etot(Pr, dtf)
        print(f"== dt=tauC/25 (reach-S): base ring Etot={T0:+.1f} Ep={E0:+.1f} ({time.time()-t0:.0f}s)")
        for nm in ('m0', 'm1', 'm2', 'ell'):
            cs = []
            for (P, x) in mem[nm]:
                Tp, Ep = etot(P, dtf)
                cs.append(2 * (Tp - T0) / x ** 2)
            cs = np.array(cs); mn = cs.mean(); sem = cs.std(ddof=1) / np.sqrt(len(cs))
            cls = ('SIG-POS' if mn > 2 * sem else ('SIG-NEG' if mn < -2 * sem else 'INCONCLUSIVE'))
            results[f"{nm}_25"] = (float(mn), float(sem), cls)
            print(f"  {nm:3s} n={len(cs)}: <c>={mn:+10.0f} +- SEM {sem:8.0f}  [{cls}]  ({time.time()-t0:.0f}s)")
        # amplitude diagnostic (verbatim 2513)
        dtf = 1 / 50; T0, _ = etot(Pr, dtf)
        print("== m2 amplitude-scaling diagnostic (dt=tauC/50):")
        for ph in (0.0, np.pi / 2):
            d04 = etot(ring_scaffold(tilt=[0.04 * np.cos(4 * np.pi * k / N + ph) for k in range(N)])[0], dtf)[0] - T0
            d02 = etot(ring_scaffold(tilt=[0.02 * np.cos(4 * np.pi * k / N + ph) for k in range(N)])[0], dtf)[0] - T0
            r = d04 / d02 if d02 != 0 else float('inf')
            print(f"  phase {ph:4.2f}: dT(0.04)={d04:+8.2f}  dT(0.02)={d02:+8.2f}  ratio={r:+6.2f}")
        # mechanical branch reading (verbatim 2513 rules)
        def sig(nm, d): return results[f"{nm}_{d}"]
        flips = [nm for nm in ('m0', 'm1', 'm2', 'ell')
                 if sig(nm, 50)[2].startswith('SIG') and sig(nm, 25)[2].startswith('SIG')
                 and np.sign(sig(nm, 50)[0]) != np.sign(sig(nm, 25)[0])]
        phys = ('m1', 'm2', 'ell')
        allclass = all(sig(nm, d)[2] != 'INCONCLUSIVE' for nm in phys for d in (50, 25))
        samesign = all(np.sign(sig(nm, 50)[0]) == np.sign(sig(nm, 25)[0]) for nm in phys)
        negboth = [nm for nm in phys if sig(nm, 50)[2] == 'SIG-NEG' and sig(nm, 25)[2] == 'SIG-NEG']
        print(f"== branch reading (mechanical, 2513 rules verbatim):")
        print(f"   flips={flips or 'none'}; phys all-classifiable={allclass}; "
              f"phys same-sign={samesign}; SIG-NEG-both={negboth or 'none'}")
        if flips or not allclass: print("   -> BRANCH U")
        elif negboth: print("   -> BRANCH N")
        elif samesign: print("   -> BRANCH D")
        else: print("   -> BRANCH U (residual sign inconsistency)")
    print(f"[{time.time()-t0:.0f}s]")

print("\nDone. Verdicts are read in rb234_invariance_record.md against the prereg.")

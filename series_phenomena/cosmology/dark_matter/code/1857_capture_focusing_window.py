#!/usr/bin/env python3
"""
1857 -- capture-focusing (no-threshold) sigma/m(v) and its viable (sigma_floor, v_sat) window.
Thomas's 1/r^2-locked-lattice picture: no delta* crossover, no v_thr. Fusion is 1/r^2 gravitational-
focusing capture (=> parameter-free 1/v^2 tail). Curve:  sigma/m(v) = s_floor + s_cap/(1+(v/v_sat)^2)
  s_floor = elastic rod-bounce (1856 sigma_T, velocity-indep) = the CLUSTER floor (short N -> low).
  s_cap/(1+(v/vsat)^2) = the capture tail (dwarf coring), saturating below v_sat.
Verdict wanted: is the (s_floor, v_sat) window that threads dwarf->Bullet FAT (robust) or a sliver (tuned)?
"""
import numpy as np

def curve(v, sf, vs, scap):
    return sf + scap/(1.0+(v/vs)**2)

def scap_for_dwarf(sf, vs, target=1.6):
    return (target - sf)*(1.0+(50.0/vs)**2)

# hard anchor windows (km/s): vd-SIDM, literature-consistent
ANCHORS = [("dwarf",50,1.0,2.0), ("LSB",200,0.7,2.5), ("group",1000,0.2,1.2),
           ("cluster",1500,0.0,1.0), ("Bullet",3500,0.0,0.7)]
CLU_PREF = (0.1, 0.5)  # Kaplinghat central

if __name__ == "__main__":
    sfs = np.linspace(0.05, 1.0, 40); vss = np.linspace(100, 600, 51)
    ok=[]; okp=[]
    for sf in sfs:
        for vs in vss:
            sc = scap_for_dwarf(sf, vs)
            if sc <= 0: continue
            if all(lo <= curve(v,sf,vs,sc) <= hi for _,v,lo,hi in ANCHORS):
                ok.append((sf,vs))
                if CLU_PREF[0] <= curve(1500,sf,vs,sc) <= CLU_PREF[1]: okp.append((sf,vs))
    if ok:
        sfa=np.array([o[0] for o in ok]); vsa=np.array([o[1] for o in ok])
        print(f"VIABLE window (threads dwarf->Bullet): "
              f"s_floor in [{sfa.min():.2f},{sfa.max():.2f}], v_sat in [{vsa.min():.0f},{vsa.max():.0f}] km/s")
        print(f"  fraction of grid viable: {100*len(ok)/(len(sfs)*len(vss)):.0f}%  (FAT => robust/non-tuned)")
    if okp:
        sfp=np.array([o[0] for o in okp]); vsp=np.array([o[1] for o in okp])
        print(f"  Kaplinghat cluster (0.1-0.5): s_floor<={sfp.max():.2f}, v_sat in [{vsp.min():.0f},{vsp.max():.0f}]")
    print("\nrepresentative viable curve (s_floor=0.20, v_sat=250):")
    sc = scap_for_dwarf(0.20, 250.0)
    for name,v,lo,hi in ANCHORS:
        print(f"  {name:>7} v={v:>4}: sigma/m={curve(v,0.20,250.0,sc):.2f}  (window {lo}-{hi})")

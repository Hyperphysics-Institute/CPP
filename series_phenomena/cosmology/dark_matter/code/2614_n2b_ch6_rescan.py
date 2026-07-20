#!/usr/bin/env python3
"""
PATCH 2614 -- N2-B-CH6-2 EXECUTION under n2b_ch6_2_prereg.md (2613) ONLY.
Controls: verbatim absolute-aim stage 7 (C-A' soft must MISS, C-B' steep must CAP).
Scan: the 22 declared centroid-relative soft cells, dt-union unconditional.
Reuses the 2611/2612 artifact functions by exec-load (registered engine verbatim).
"""
import numpy as np, time, os, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
def load(name, fn):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fn))
    m = importlib.util.module_from_spec(spec)
    return m, spec
# exec-load the scan module's namespace (engine + scan_cell + regen6, verbatim)
src = open(os.path.join(HERE, "2611_n2b_ch6_scan.py")).read()
cut = src.index('print("=" * 78)')
ns = {'__name__': 'ch6', '__file__': os.path.join(HERE, '2611_n2b_ch6_scan.py')}
exec(src[:cut], ns)
regen6 = ns['regen6']; scan_cell = ns['scan_cell']; stage_capture = ns['stage_capture']
AXES = {'-z': (0,0,-1), '+z': (0,0,1), '-x': (-1,0,0), '+x': (1,0,0), '-y': (0,-1,0), '+y': (0,1,0)}
D = ns['D']
print("="*78); print("PATCH 2614 -- N2-B-CH6-2 (prereg 2613; verdicts read there)"); print("="*78)
t0 = time.time()
H6s,V6s,C6s,S6s,log_s = regen6(2.0)
H6t,V6t,C6t,S6t,log_t = regen6(4.0)
print(f"[regen] soft {log_s} steep {log_t}")
print("[controls: verbatim ABSOLUTE-AIM stage 7]")
ctrl_ok = True
for wname,bd,(Hc,Vc,Cc,Sc),want in (('soft',2.0,(H6s,V6s,C6s,S6s),'MISS'),
                                     ('steep',4.0,(H6t,V6t,C6t,S6t),'CAP')):
    verd = []
    for dtf in (1/100, 1/200):
        ok,res,_,_,_ = stage_capture(Hc,Vc,np.array(Cc),list(Sc),-1.0,bd,dtf)
        verd.append('CAP' if ok else 'MISS')
        print(f"  {wname} dt=1/{int(1/dtf)}: {'BOUND' if ok else 'UNBOUND'} Sea={res['Sea']:.1f}")
    ok_ctrl = all(v == want for v in verd)
    ctrl_ok &= ok_ctrl
    print(f"  {wname}: want {want}, got {verd} -> {'PASS' if ok_ctrl else 'FAIL'}")
if not ctrl_ok:
    print("RC4': CONTROL FAILURE -- STOP"); raise SystemExit
print("\n[scan: 22 centroid-relative soft cells, dt-union]")
cells = []
for ax in ('-z','+z','-x','+x','-y','+y'):
    for b in (0.0,0.5,1.0): cells.append((ax,b,0,-1.0))
for phi in (45,90,135): cells.append(('-z',0.5,phi,-1.0))
cells.append(('-z',0.5,0,+1.0))
ncap = nuns = 0
for (ax,b,phi,q) in cells:
    r = {}
    for dtf in (1/100, 1/200):
        cl,res,d_inc = scan_cell(H6s,V6s,C6s,S6s,AXES[ax],b,phi,q,2.0,dtf)
        r[dtf] = (cl,res['Sea'])
    c1,c2 = r[1/100][0], r[1/200][0]
    stab = c1 == c2
    if stab and c1 == 'CAP': ncap += 1
    if not stab: nuns += 1
    print(f"  start={ax:2s} b={b}D phi={phi:3d} q={q:+.0f}: 1/100={c1}(S={r[1/100][1]:.0f}) 1/200={c2}(S={r[1/200][1]:.0f}) {'dt-STABLE' if stab else 'dt-UNSTABLE'}")
print(f"\n[{time.time()-t0:.0f}s] dt-stable CAP: {ncap}/22 ; dt-unstable: {nuns}")
print("Done. Verdicts read in n2b_ch6_2_record.md against the prereg.")

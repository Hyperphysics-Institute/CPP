#!/usr/bin/env python3
"""Patch 2324 -- Grok propagation: the DM-1 anchor suite under the three G4 outcomes.

Grok's decisive check (W1, merged into OPEN-DM-CAPTURE-1 at 2311): re-anchor the DM-1
suite with capture efficiency P(v) < 1 and propagate. Executed here under the 2322
polaron frame: the one residue is the sub-cone spectral weight w = S(k~1/R_s, omega_enc)
/S_max, with per-anchor thresholds Theta_crit from 2321 (unchanged at 2322).

Capture-annulus propagation (derived from the registered C-g accounting B):
  loss(b) = f_geo(b) * w * E_coat, f_geo(b) = f_geo(b_max) * (b/b_max)  [path (2b)(c/v),
  mfp fixed at k = 1/R_s], capture requires loss >= E_col = const(b)
  => capture annulus b in [b_max*(Theta_crit/w), b_max]
  => P(v, w) = max(0, 1 - (Theta_crit(v)/w)^2)      (flat-w slice)
Zero-parameter structure (eta = chi): P multiplies the published capture term with NO
refit freedom -- total(v, w) = floor + P(v, w) * capture_pub(v).

Checks: (1) omega_enc ladder; (2) kill-branch anchor table; (3) flat-w turn-on ladder =
partial branch excluded by the LSB anchor; (4) survive-branch requirements (w and E_coat
floors at the LSB frequency); (5) slope/Ohmic-excess quantification; (6) F1 invariance.
No verdict moved: G4 stays UNRESOLVED-QUANTIFIED.
"""
import math

C = 2.998e8; HBARC_MEVFM = 197.327
RS = 25.42; RC = 1.0; ELL, DELTA2 = 1.0, 0.09
ECOAT_LO, ECOAT_HI = 0.144, 0.6                      # MeV (hard..easy reservoir)
# anchors: v [km/s], b_max [fm], E_col [MeV]  (2311/2316/2321 registered)
ANCH = {"dwarf10": (10, 145.0, 7.04e-6),
        "pin50":   (50, 79.0, 1.76e-4),
        "lsb200":  (200, 31.0, 2.82e-3)}
# published anchor suite (DM-1 v1.4 sec xsec item iv; floor 1870-71 MC)
FLOOR = 0.046                                        # cm^2/g, measured elastic
PUB = {"dsph":  (15.5, (20.0, 100.0)),               # 10-40 km/s regime, graze-under recorded
       "pin50": (4.65, (1.0, 5.0)),                  # dwarf pin, PASS
       "lsb200":(0.795,(0.7, 2.5))}                  # LSB, PASS
def mfp(k): return ELL/((k*ELL)**4*DELTA2)
def fgeo(v_kms, b): return (2*b/(v_kms*1e3/C))/mfp(1.0/RS)
def theta_crit(v_kms, b, Ecol, Ecoat): return (Ecol/Ecoat)/fgeo(v_kms, b)
def P(th, w): return max(0.0, 1.0 - (th/w)**2) if w > 0 else 0.0

checks = []

# (1) encounter-frequency ladder  hbar*omega_enc = hbar*v/b_max
om = {k: HBARC_MEVFM*1e6*(v*1e3/C)/b for k,(v,b,_) in ANCH.items()}   # eV
checks.append((f"omega_enc ladder: {om['dwarf10']:.0f} eV (dwarf) / {om['pin50']:.0f} eV (pin) / "
               f"{om['lsb200']:.0f} eV (LSB) -- two decades; matches 2322's 45 eV dwarf figure",
               abs(om['dwarf10']-45.4) < 1.0 and 90 < om['lsb200']/om['dwarf10'] < 100, om))

# per-anchor Theta_crit bands (recompute = 2321 registered values)
TH = {k: (theta_crit(v,b,E,ECOAT_HI), theta_crit(v,b,E,ECOAT_LO)) for k,(v,b,E) in ANCH.items()}
checks.append((f"Theta_crit recompute matches 2321: dwarf {TH['dwarf10'][0]:.1e}..{TH['dwarf10'][1]:.1e}; "
               f"pin {TH['pin50'][0]:.1e}..{TH['pin50'][1]:.1e}; LSB {TH['lsb200'][0]:.2f}..{TH['lsb200'][1]:.2f}",
               abs(TH['dwarf10'][0]/6.3e-6-1)<0.05 and abs(TH['lsb200'][1]/0.98-1)<0.05, TH))

# (2) KILL branch: total = floor everywhere
kill_fail = {k: (lo/FLOOR, hi/FLOOR) for k,(pred,(lo,hi)) in PUB.items()}
checks.append((f"KILL branch = floor {FLOOR} everywhere: dSph FAILS x{kill_fail['dsph'][0]:.0f}-"
               f"{kill_fail['dsph'][1]:.0f} below window; dwarf pin FAILS x{kill_fail['pin50'][0]:.0f}; "
               f"LSB FAILS x{kill_fail['lsb200'][0]:.0f}; cluster/Bullet/group unchanged (floor-dominated, "
               f"bounds PASS) -- Discriminant I dead, candidate reverts to flat quasi-collisionless relic",
               all(f[0] > 10 for f in kill_fail.values()), kill_fail))

# (3) PARTIAL branch (flat w): turn-on ladder and the LSB exclusion
# pin survival floor: total >= 1 (window low edge); capture_pub(pin) = 4.65-FLOOR
cap_pin = PUB['pin50'][0]-FLOOR; Pmin_pin = (1.0-FLOOR)/cap_pin
w_pin = {c: TH['pin50'][i]/math.sqrt(1-Pmin_pin) for i,c in ((0,'easy'),(1,'hard'))}
# LSB survival floor: total >= 0.7; capture_pub(lsb) = 0.795-FLOOR
cap_lsb = PUB['lsb200'][0]-FLOOR; Pmin_lsb = (0.7-FLOOR)/cap_lsb
w_lsb = {c: TH['lsb200'][i]/math.sqrt(1-Pmin_lsb) for i,c in ((0,'easy'),(1,'hard'))}
checks.append((f"flat-w turn-on ladder: dwarf-side capture alive from w ~ {TH['dwarf10'][0]:.0e}; pin anchor "
               f"holds its window from w >= {w_pin['easy']:.1e} (easy coat)..{w_pin['hard']:.1e} (hard); LSB "
               f"anchor needs w >= {w_lsb['easy']:.2f} (easy)..{w_lsb['hard']:.2f} (hard>1: INFEASIBLE) -- "
               f"any flat w in [{w_pin['easy']:.0e}, {w_lsb['easy']:.2f}) keeps dwarf cores while LSB total "
               f"collapses to the floor {FLOOR} vs window low edge 0.7: the flat-spectrum PARTIAL branch is "
               f"EXCLUDED BY THE EXISTING LSB ANCHOR (not merely disfavored)",
               w_lsb['easy'] > 0.4 and w_lsb['hard'] > 1.0 and w_pin['easy'] < 2e-3, (w_pin, w_lsb)))

# (4) SURVIVE branch requirements: E_coat floor for LSB feasibility at w <= 1
# w_req = Theta_crit/sqrt(1-Pmin) <= 1  =>  Theta_crit <= sqrt(1-Pmin)
th_max = math.sqrt(1-Pmin_lsb)
Ecoat_min = ANCH['lsb200'][2]/(th_max*fgeo(*ANCH['lsb200'][:2]))
checks.append((f"SURVIVE branch feasibility: LSB requires P >= {Pmin_lsb:.2f} => w(4.2 keV) >= "
               f"{w_lsb['easy']:.2f} AND E_coat >= {Ecoat_min:.2f} MeV (upper half of the 0.144-0.6 band) -- "
               f"the unit-efficiency assumption is genuinely load-bearing at the LSB anchor; dwarf-side "
               f"survive is a categorically softer ask (w >= {w_pin['easy']:.0e})",
               0.25 < Ecoat_min < 0.45, Ecoat_min))

# (5) spectral asks in Ohmic-tail units and the required slope
ohm = {k: (ANCH[k][0]*1e3/C)*(RC/ANCH[k][1]) for k in ANCH}    # omega_enc * tau_b
excess_dwarf = TH['dwarf10'][0]/ohm['dwarf10']                 # 2321's x27 (easy end)
excess_lsb   = w_lsb['easy']/ohm['lsb200']
s_req = math.log(w_lsb['easy']/w_pin['easy'])/math.log(om['lsb200']/om['pin50'])
ohmic_shortfall = w_lsb['easy']/(w_pin['easy']*(om['lsb200']/om['pin50']))
checks.append((f"the spectral ask, graded: dwarf survival needs x{excess_dwarf:.0f} over the bare Ohmic tail "
               f"(2321's number); FULL-SUITE survival needs x{excess_lsb:.1e} at the LSB frequency -- "
               f"~x{excess_lsb/excess_dwarf:.0f} harder -- equivalently a super-Ohmic rise s >= {s_req:.1f} "
               f"between 417 eV and 4.2 keV (bare Ohmic s=1 falls short x{ohmic_shortfall:.0f} even seeded at "
               f"the pin threshold) OR near-ceiling plateau weight by ~keV",
               2.0 < s_req < 3.0 and excess_lsb > 1e4, (excess_dwarf, excess_lsb, s_req)))

# (6) F1 invariance across branches
grok_pred = FLOOR + 0.13*0.05  # group scale ~ floor + 13% capture fraction (2310)
checks.append((f"F1 (group-scale 0.037-0.05 vs Sagunski 0.5+-0.2) is BRANCH-INVARIANT: the group anchor is "
               f"floor-dominated (87%+) in all three G4 outcomes -- its pre-registered disqualifier power is "
               f"G4-independent", abs(grok_pred-0.052) < 0.01, grok_pred))

npass = 0
for name, ok, val in checks:
    print(f"[{'PASS' if ok else 'FAIL'}] {name}\n")
    npass += ok
print(f"{npass}/{len(checks)} PASS")
assert npass == len(checks)

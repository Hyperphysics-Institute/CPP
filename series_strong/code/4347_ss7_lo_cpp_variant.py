#!/usr/bin/env python3
"""4347 -- SS-7's alpha-chain predictions with the fully-CPP alpha binding (SS-5's 27.904 MeV) instead of the
measured 28.296 MeV. Each prediction shifts down by N_alpha * 0.392 MeV. Reads PRED-C-42..53 from predictions.md."""
import re, math
rows = [l for l in open('predictions.md') if re.match(r'\| PRED-C-(4[2-9]|5[0-3]) ', l)]
assert len(rows) == 12
e_exp, e_lo = [], []
for i, l in enumerate(rows):
    c = [x.strip().strip('*') for x in l.split('|')]
    pred = float(re.findall(r'[\d.]+', c[3])[0]); obs = float(re.findall(r'[\d.]+', c[4])[0]); Na = 3 + i
    e_exp.append(100 * (pred - obs) / obs); e_lo.append(100 * (pred - Na * 0.392 - obs) / obs)
    print(f"N_alpha={Na:2d}  measured-B_alpha {e_exp[-1]:+.2f}%   fully-CPP B_alpha {e_lo[-1]:+.2f}%")
rms = lambda e: math.sqrt(sum(x * x for x in e) / len(e))
print(f"RMS: measured input {rms(e_exp):.2f}%, fully-CPP {rms(e_lo):.2f}% (range {min(e_lo):+.2f}% to {max(e_lo):+.2f}%)")
assert abs(rms(e_lo) - 1.77) < 0.01

#!/usr/bin/env python3
"""claim_wording_sweep.py -- Patch 4339 (roadmap item 0/7: the corpus-wide wording sweep).

Scans every deposit candidate (osf_deposit_manifest.json, withheld papers skipped) for wording that can claim more than
the registries allow, and prints each hit with its line.  Categories:
  cosmo  : dark matter / dark energy / cosmological constant / vacuum energy
  const  : G, hbar, spin, alpha stated as derived / fixed / parameter-free
  zero   : "zero-parameter", "no free parameters", "parameter-free"
  toe    : "derives the Standard Model", "Theory of Everything"
Usage:  python3 code/claim_wording_sweep.py [category ...] [--counts]
The triage (what each hit should say) is recorded in wording_sweep_register.md, not here.
"""
import json, re, sys, collections
PATS = {
 'cosmo': r'dark[- ]matter|dark[- ]energy|cosmological constant|vacuum energy',
 'const': r'spin[^.\n]{0,40}\bderiv|deriv[^.\n]{0,40}spin[- ]?(?:1/2|½|\\frac\{1\}\{2\})|deriv[^.\n]{0,30}(?:\\hbar|Planck.s constant)'
          r'|(?:Newton|gravitational constant|\bG\b)[^.\n]{0,40}(?:deriv|no free|fixed by)|fine[- ]structure[^.\n]{0,40}deriv',
 'zero':  r'zero[- ](?:free[- ])?param|no free param|without (?:any )?free param|parameter[- ]free',
 'toe':   r'derives? the Standard Model|Theory of Everything',
}
args = [a for a in sys.argv[1:] if not a.startswith('--')]
cats = args or list(PATS)
m = json.load(open('osf_deposit_manifest.json'))
tot = collections.Counter()
for p in m['papers']:
    if p['withheld']:
        continue
    try:
        lines = open(p['rel']).read().splitlines()
    except OSError:
        continue
    for i, L in enumerate(lines, 1):
        if L.lstrip().startswith('%'):
            continue
        for c in cats:
            if re.search(PATS[c], L, flags=re.I):
                tot[(p['rel'], c)] += 1
                if '--counts' not in sys.argv:
                    print(f"{c:5s} {p['rel']}:{i}: {L.strip()[:220]}")
if '--counts' in sys.argv:
    for (r, c), n in sorted(tot.items(), key=lambda x: (x[0][1], -x[1])):
        print(f"{c:5s} {n:4d}  {r}")
print(f"# total hits: {sum(tot.values())} in {len({r for r, _ in tot})} papers", file=sys.stderr)

#!/usr/bin/env python3
"""
Patch 4168 — Patch 4167 is WRONG. The founder is right, and the corpus already
said so five years of patches ago.

MY ERROR: 4167 identified the 600-cell's nearest-neighbour distance with the
PSR, computed 12 GPs in the band, and concluded the founder's "vastly greater
than 12" needed a premise the corpus did not supply.

THE CORPUS'S CANONICAL POSITION, which I read past:
  c01, verbatim: "The true grid is sub-Planck (~ l_P / 10^30) by nesting."
  founders_vision, Patch 0733 correction, verbatim: "The 0732 scope note above
    MIS-READ l_P AS THE LATTICE SPACING. The corpus (c07 'sub-Planck spacing';
    glossary 'l_P = unstressed baseline' PSR; c01 '~10^30 GPs per Planck
    length') establishes that l_P is the BASELINE PSR -- a radius enclosing
    ~10^30 sub-Planck grid points."
  and: "Thomas pushed back -- across several rounds -- against the framing that
    the Planck length l_P is the Grid-Point lattice spacing."

A PRIOR OPUS MADE EXACTLY THIS ERROR AT PATCH 0732. The founder corrected it
across several rounds. It was recorded at 0733. I made it again at 4167.
"""
import numpy as np
out=[]
def say(s=""): print(s); out.append(s)
R=1e30                       # PSR / lattice spacing, from c01

say("W1  the recount")
lin=R
shell=4*np.pi*R**2*(0.1*R)
say(f"    GPs per Planck length (c01)                 ~ {lin:.0e}")
say(f"    GPs inside the PSR sphere  ~ (4/3) pi R^3   ~ {4/3*np.pi*R**3:.1e}")
say(f"    GPs in the +-10% PSR BAND  ~ 4 pi R^2 (0.1R)~ {shell:.1e}")
say()
say("    Not 12. About 1e90. The founder's 'vastly greater than 12 neighbors'")
say("    understates it by ninety orders of magnitude.")
say()

say("W2  what it does to Patch 4166's dilution number")
say("    corr(register, own spin) ~ 1 / sqrt(N):")
say(f"    {'N':>12}{'corr':>14}{'V-A would be':>16}")
for N,lab in ((12,'4167 (wrong)'),(1e30,''),(shell,'corrected')):
    c=1/np.sqrt(N)
    say(f"    {N:>12.0e}{c:>14.2e}{c*100:>15.1e}%  {lab}")
say()
say("    4166 reported corr = 0.154 and 'V-A would be ~15% of maximal'.")
say("    THE CORRECT FIGURE IS ~1e-45, i.e. V-A at 1e-43 percent of maximal.")
say("    **4166's number is wrong by forty-four orders. Its VERDICT is not.**")
say("    b cannot possibly read the A_i register -- the conclusion is now")
say("    overwhelming rather than merely forced, which is exactly what 4167")
say("    section 4 predicted would happen if the founder turned out to be right.")
say()

say("W3  and PSR is not a ceiling either -- TODO-4167-PSRSCALE answered")
say("    founders_vision, 0733: 'if l_P is the BASELINE PSR rather than a hard")
say("    ceiling, PSR CAN EXCEED IT (the variable-speed-of-light route), so")
say("    inflation is not ruled out by a PSR-cap.' And l_P is environment-")
say("    dependent -- smaller near a nucleus, larger in flat space.")
say("    So the answer to 'can the PSR exceed l_P' is YES, canonically, and the")
say("    question I filed at 4167 was already closed in the corpus.")
say()

say("W4  what else in this session assumed 12, and does it survive?")
rows=[("4159 Q2/Q3 staircase over 12 edges",
       "MOOT -- already withdrawn at 4161 for a different reason (b reads the"),
      ("", "  continuous V, not a quantised edge). The 12-count was a second"),
      ("", "  error underneath the first."),
      ("4160 anisotropy falsifier",
       "ALREADY WITHDRAWN at 4161. Would have been wrong twice over."),
      ("4161 'N = 12, the generic case'",
       "CONCLUSION STANDS, NUMBER WRONG. The isotropy of a sum over a spherical"),
      ("", "  5-design is exact at second order for ANY N >= the design's size;"),
      ("", "  N ~ 1e90 makes it more exact, not less."),
      ("4158 <b> = (v/c)cos(theta)",
       "UNAFFECTED -- it never used a neighbour count."),
      ("4167 entirely",
       "WITHDRAWN.")]
for a,b in rows:
    say(f"    {a:<38}{b}")
say()
say("W5  the pattern I should name")
say("    This is the THIRD time this session that a correction already recorded")
say("    in the corpus was read past: 4138 (a computed table whose prose")
say("    inverted it), 4161 (c03's own sentence, quoted in my own 4155), and now")
say("    4167 (a founder correction at 0733, argued across several rounds).")
say("    In each case the corpus contained the answer and the failure was in")
say("    SEARCH, not in reasoning. TODO-4138-TABLEPROSE was scoped too narrowly.")
open('/tmp/4168.txt','w').write('\n'.join(out))

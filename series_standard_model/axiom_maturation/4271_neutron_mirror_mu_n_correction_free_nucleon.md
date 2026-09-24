# The Neutron Is the Proton's Mirror; a Correction to μ_n Since 4244; Free Nucleon g_A 1.294–1.297

**Patch:** 4271. **Lane:** EW → strong (TODO-4234-DELTA; 4270 owed (a), (b)). **Session:** 239.
**Verify:** `series_standard_model/code/4271_neutron_own_frame_and_mu_n_correction.py`.

## 1. The neutron's frame

The founder's seat rules (4270: up 2 of 4, minus only; down 4 of 4) and the SU(3) story's account of beta decay
(*"its +qCP core migrates to the open minus eCP vertex — udd becomes uud"*) fix the neutron's frame:
- the u on the −qCP,
- the two d's on the two plus vertices (+qCP, +eCP),
- the −eCP open.

This is the proton's mirror. The like pair (dd) sits on the repulsive plus–plus edge, and the odd quark (u) is at the
apex. SS-2's force balance with d charges puts the dd edge 0.2% shorter than the uu edge. Under route (H) the widths do
not depend on binding strength (4262), so the neutron's like-pair and odd-quark R equal the proton's R_u and R_d, and
the d–d exchange equals the u–u exchange. **No separate neutron calculation is needed.** Owed item (b) is closed.

**SS-2 conflict (filed).** SS-2 writes the neutron as *V₁(−): d₁, V₂(−): d₂, V₃(+): u, V₄(−): open*. That puts
three minus vertices on an hTetra that has two, and it puts the u on a plus vertex, which the founder's 4270 rule
forbids. The assignment above replaces it.

## 2. A correction to μ_n in every script since 4244

The scripts from 4244 to 4269 computed μ_n = (4μ_d − μ_u)/3 with the d's spin factor taken from the proton's *odd*
quark and the u's from the proton's *like pair*. That assigns R by flavour. In the neutron's own frame the d's are
the like pair and the u is the odd quark, so R must be assigned by role. μ_p is unaffected.

| state | μ_n as scripted | μ_n, neutron's own frame |
|---|---|---|
| 4244, m_q = m_p/3 (boot-card checksum −1.829) | −1.829 (−4.4%) | −1.840 (−3.8%) |
| 4262 ruled state, m_q fitted to μ_p (4268's prediction) | −1.884 (−1.5%) | **−1.871 (−2.2%)** |

4268's "μ_n −1.5%" and 4270's provisional μ_n are corrected to −2.2%. Errata are appended to both. The earlier
scripts are left as records; this script supersedes their μ_n rows.

## 3. The free nucleon: the odd quark's diagonal mode

In a free proton the +eCP vertex is open (SS-2's nuclear binding site). By the 4270 rule, the d bonds to it as it
does to its own vertex, so the odd quark gains a **diagonal mode toward the open like-sign vertex**. This is the
mirror of the u's diagonal mode (4262). The free neutron's u gets the same mode toward the open −eCP.

The open vertex sits off the quark plane, and its position is not on file, so the mode's direction is scanned.

## 4. Rows verbatim (D-11)

```
(1) like-pair edge: proton uu 1.0710 fm, neutron dd 1.0692 fm (-0.17%) -- the mirror holds to 0.2%

(2) mu_n, as scripted since 4244 vs neutron's own frame:
  4244 (founder mode rule, before 4262)        m_q = m_p/3          m_q=312.8  mu_p=2.772  mu_n scripted -1.829 (-4.4%)  -> own frame -1.840 (-3.8%)  mu_n/mu_p -0.6639 (meas -0.6850)
  4244 (founder mode rule, before 4262)        m_q fitted to mu_p   m_q=310.4  mu_p=2.793  mu_n scripted -1.843 (-3.7%)  -> own frame -1.854 (-3.1%)  mu_n/mu_p -0.6639 (meas -0.6850)
  4262 ruled state, u-u exchange (= 4269 L1)   m_q = m_p/3          m_q=312.8  mu_p=2.675  mu_n scripted -1.805 (-5.7%)  -> own frame -1.792 (-6.3%)  mu_n/mu_p -0.6698 (meas -0.6850)
  4262 ruled state, u-u exchange (= 4269 L1)   m_q fitted to mu_p   m_q=299.6  mu_p=2.793  mu_n scripted -1.884 (-1.5%)  -> own frame -1.871 (-2.2%)  mu_n/mu_p -0.6698 (meas -0.6850)

(3) free nucleon: odd quark's diagonal mode toward the open like-sign vertex (like pair: 4262 state, u-u exchange)
    without it (4262/4269 L1): R_odd = 0.8162
    direction  0 deg from the plane normal: R_odd=0.7787  g_A=1.2970 (+1.7%)  m_q(mu_p)=298.9  mu_n=-1.862 (-2.7%)
    direction 30 deg from the plane normal: R_odd=0.7756  g_A=1.2960 (+1.6%)  m_q(mu_p)=298.8  mu_n=-1.861 (-2.7%)
    direction 60 deg from the plane normal: R_odd=0.7705  g_A=1.2943 (+1.5%)  m_q(mu_p)=298.7  mu_n=-1.860 (-2.8%)
    direction 90 deg from the plane normal: R_odd=0.7681  g_A=1.2935 (+1.4%)  m_q(mu_p)=298.7  mu_n=-1.860 (-2.8%)

-> The neutron's own frame is the proton's mirror, so d-d exchange = u-u exchange and no new calculation is needed
   beyond assigning S by role.  Corrected, the 4262 state predicts mu_n = -1.871 (-2.2%) at m_q fitted to mu_p;
   with the odd quark's diagonal mode (free nucleon, 4270) g_A = 1.294-1.297 (+1.4 to +1.7%), direction bracketed.
```

## 5. Result

For a free nucleon under every ruling so far (pass-through ZBW at ω = m_q c²/ħ; the founder's modes including both
diagonal modes; u–u exchange; seat rules):

- **g_A = 1.294–1.297 (+1.4% to +1.7%)**, the spread coming from the open vertex's unknown direction.
- **m_q ≈ 299 MeV** from μ_p.
- **μ_n ≈ −1.861 (−2.7%)**.

Neutron beta decay is a free-nucleon process, so this is the state to compare with the measured 1.2754. In a nucleus
the open vertex is bonded, and the odd quark's diagonal mode would then be lost (4270 (ii)).

**PD-008.** Adding the diagonal mode helps g_A, so it is a convenient branch. It is adopted because it follows
directly from the founder's 4270 rule and 4262's mode rule, both founder statements, not because of the improvement.
μ_n moves the other way (−2.2% to −2.7%), and that is recorded beside it.

## 6. Filed

- The open vertex's position, which would pin the direction and replace the 1.294–1.297 bracket with one number.
- SS-2's neutron assignment, to be corrected in the paper.
- **Free versus bound:** in a nucleus the odd quark loses its diagonal mode. With the like pair unchanged, g_A would
  return toward 1.310, which is higher, not lower. Nuclear g_A "quenching" runs the other way (g_A is smaller in
  nuclei), so this mechanism does not explain quenching. That is recorded as a negative.

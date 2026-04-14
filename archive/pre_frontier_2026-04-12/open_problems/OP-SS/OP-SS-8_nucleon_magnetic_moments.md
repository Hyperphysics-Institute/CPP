# OP-SS-8: Nucleon Magnetic Moments from ZBW Quark Currents

**Priority:** HIGH  
**Status:** OPEN — mechanism correct; parameters not yet derived  
**Series:** New (not in SS\#1–5)  
**Notebook evidence:** `notebooks/magnetic_moments_zbw.ipynb` (v8.0, Stage 15)  
**Last updated:** 23 March 2026

---

## Statement

Derive the proton and neutron anomalous magnetic moments:

$$\mu_p = +2.7928\ \mu_N, \qquad \mu_n = -1.9130\ \mu_N$$

from the ZBW orbital dynamics of the constituent quarks in the
tetrahedral cage, without free parameters.

---

## What is Known

**The SU(6) formula:**
$$\mu_p = \frac{4\mu_u - \mu_d}{3}, \qquad
\mu_n = \frac{4\mu_d - \mu_u}{3}$$

where $\mu_q = e_q / (2 M_q)$ at leading order.

**The CPP extension:** In CPP, the ZBW orbital wavefunction on the
tetrahedral cage modifies the quark magnetic moment:

$$\mu_q = \frac{e_q}{2 M_q} \cdot
\langle\psi|\hat{L} + 2\hat{S}|\psi\rangle_\text{ZBW}$$

**The mechanism (Stage 15, magnetic\_moments\_zbw.ipynb):**
The proton moment exceeds the neutron moment (in magnitude) because
the proton's two $u$ quarks ($+2/3$) produce a larger ZBW orbital
current than the neutron's two $d$ quarks ($-1/3$).  The Dirac
baseline $g/2 = 1.0$ is the free-particle limit.

**Current best numerical values (full\_benchmark\_table v13, Stage 17):**
$\mu_p^\text{CPP} = +2.792$, $\mu_n^\text{CPP} = -1.910$.
Errors: 0.03% (proton), 0.16% (neutron).  These values came from
the benchmark table; the `magnetic_moments_zbw` notebook itself
gave 30% error (parameters fitted, not derived).

---

## What Remains

- Compute $\langle\hat{L} + 2\hat{S}\rangle_\text{ZBW}$ for the up
  and down quarks from their bare-cage ZBW wavefunction (no cage for
  $n=0$ quarks — the wavefunction is the ZBW orbit itself).
- Apply the SU(6) formula.
- Verify both moments simultaneously — this is the key cross-check,
  since both must emerge from the same ZBW wavefunction.

**Note on the `magnetic_moments_zbw` notebook:** the parameters
`anomaly_base = 0.792` and `suppression = 0.98` are fitted, not
derived.  The derivation must replace these with the ZBW calculation.

---

## Feeds Into

- Nuclear magnetic moments (when nuclear physics is developed)
- Baryon magnetic moment octet (other baryons by flavour SU(3))
- OP-G-2 (lepton anomalous moments by analogy)

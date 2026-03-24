# OP-SS-3: Chiral Condensate $\langle\bar{q}q\rangle$ from ZBW Dynamics

**Priority:** MEDIUM  
**Status:** OPEN — GOR estimate 15% above lattice  
**Series:** SS\#5  
**Notebook evidence:** `notebooks/magnetic_moments_zbw.ipynb` (v8.0, Stage 15)  
**Last updated:** 23 March 2026

---

## Statement

Derive the chiral condensate magnitude from CPP ZBW dynamics:

$$|\langle\bar{q}q\rangle|^{1/3} \approx 240\text{–}250\ \text{MeV}$$

without calibrating to this value.

---

## What is Known

The Gell-Mann–Oakes–Renner relation gives an estimate:

$$|\langle\bar{q}q\rangle|^{1/3}
= \left(\frac{m_\pi^2 f_\pi^2}{m_u + m_d}\right)^{1/3}
\approx 289\ \text{MeV}$$

using tree-level current quark masses ($m_u = 2.2$~MeV, $m_d =
4.8$~MeV).  The lattice QCD value is 240–250~MeV — the 15% offset
is consistent with the known limitation of using tree-level masses
without RGE running.

In CPP, $\langle\bar{q}q\rangle$ is the vacuum expectation value of
ZBW phase coherence between quark and antiquark in the DP Sea.  The
up and down quarks have no cage (bare qCPs); their ZBW frequency goes
to zero as $m_{u,d} \to 0$, which is why $m_\pi \to 0$ in the chiral
limit (SS\#5 Theorem 2, exact).

---

## What Remains

- Compute $\langle\bar{q}q\rangle$ from the bare-quark ZBW phase
  coherence integral in the DP Sea.
- Verify the 15% offset is the RGE running correction (not a CPP
  structural error).
- The ZBW notebooks (`notebooks/magnetic_moments_zbw.ipynb`) contain
  the relevant ZBW orbital wavefunction; that wavefunction integrated
  over the DP Sea density gives $\langle\bar{q}q\rangle$.

---

## Feeds Into

- Pion mass and $f_\pi$ (full chiral perturbation theory from CPP)
- OP-SS-1 (light quark mass terms)

# OP-SS-10: Nuclear Binding Energy $V(r)$ from qDP Chain Insertion

**Priority:** HIGH  
**Status:** OPEN — mechanism identified; no quantitative derivation yet  
**Series:** New (not in SS\#1–5); companion to nuclear chart series  
**Notebook evidence:** `notebooks/nucleon_NBT_bonding.ipynb` (v8.0, Stage 21)  
**Last updated:** 23 March 2026

---

## Statement

Derive the nucleon–nucleon potential $V(r)$ as a function of
internucleonic separation $r$ from CPP qDP chain insertion dynamics.
Show that:

1. $V(r) < 0$ (attractive) for $r_\text{conf} < r < r_\text{nuclear}
   \approx 3$~fm
2. $V(r) > 0$ (repulsive) for $r < r_\text{conf} \approx 0.16$~fm
   (hard core)
3. $V(r) \to 0$ as $r \to \infty$
4. The binding energy per nucleon at saturation density is
   $\sim 7$–$9$~MeV

---

## What is Known

### 1. The NBT mechanism (`nucleon_NBT_bonding` v8, Stage 21)

When two nucleons approach, their qDP chains overlap.  The increased
SSV stress in the overlap region induces additional qDP chain
formation:

$$E_\text{bonding}(\text{stress}) = 1
+ \min(\text{stress}^2,\,1) \times 1.2
+ \max(\text{stress}^2 - 1,\,0) \times 0.8$$

This piecewise formula captures:
- Attractive regime: new qDP chains lower the total energy
- Saturation: cage geometry limits chain insertion → binding energy
  per nucleon peaks (analogous to Fe-56 maximum at 8.79~MeV/nucleon)
- The stress parameter is qualitatively correct but not yet connected
  to internucleonic separation $r$

### 2. Connection to confinement radius

The hard core at $r < r_\text{conf}$ follows from the cage geometry:
below $r_\text{conf} \approx 0.161$~fm, the two tetrahedral cages
cannot interpenetrate without collapsing both into a single cage
(which is a different hadron, not two nucleons).  This sets the
short-range repulsion.

### 3. The attraction range

For $r > r_\text{conf}$, the qDP chains of the two nucleons can
overlap without cage merger.  The SSV stress in the overlap region
scales as $\sim 1/r^4$; the induced chain formation energy scales
with the overlap volume $\sim r_\text{conf}^3 / r$.  This gives a
potential shape qualitatively like the Yukawa potential
$V(r) \sim e^{-r/r_\text{conf}} / r$ with range set by
$r_\text{conf}$.

---

## What Remains

### Step 1 — Connect stress to $r$

Define:
$$\text{stress}(r) = \frac{r_\text{conf}}{r} \times
\left(\frac{r_\text{nuclear}^2 - r^2}{r_\text{nuclear}^2}\right)$$

or a physically equivalent expression, and verify it reproduces the
known $V(r)$ shape (attractive well at $\sim 1$–3~fm, repulsive at
$< 0.5$~fm).

### Step 2 — Calibrate the overall scale

The $1.2$ and $0.8$ prefactors in the NBT formula must be derived
from the SSV chain insertion energy.  From OP-SS-5:
$$E_\text{chain} \sim \frac{\alpha_s \hbar c}{r_\text{conf}}
\approx \frac{0.118 \times 197\ \text{MeV·fm}}{0.161\ \text{fm}}
\approx 145\ \text{MeV}$$

This is the energy per qDP chain insertion.  Divided by the typical
nuclear kinetic energy per nucleon ($\sim 20$~MeV), the ratio $\sim 7$
is the source of the approximately-7~MeV binding energy scale.

### Step 3 — Reproduce nuclear saturation density

Nuclear saturation density $\rho_0 \approx 0.17\ \text{fm}^{-3}$
corresponds to internucleonic spacing $r_0 \approx 1.8$~fm.  At this
spacing, the CPP potential must have its minimum of $\sim -8$~MeV
per nucleon.  Verify that the derived $V(r)$ achieves this.

---

## Connection to Nuclear Chart Series

Solving OP-SS-10 gives $V(r)$, which when combined with the standard
many-body nuclear Hamiltonian gives:
- Binding energies across the nuclear chart
- Magic numbers (from closed shell structure of the cage potential)
- Alpha-particle special stability ($^4$He closed shell)

This is the starting point for the nuclear chart series that Thomas
and Grok developed separately.

---

## Prerequisites

- OP-SS-5 (string tension $\sigma$ and $r_\text{conf}$ from
  sea\_strength) — needed to set the absolute energy scale

---

## Feeds Into

- Nuclear chart series (`series_nuclear/`)
- OP-G-2 (full SM — nuclear physics as part of the CPP programme)
- $r$-process nucleosynthesis (future: neutron-rich nuclear binding)

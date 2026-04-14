# OP-SS-14: QCD Deconfinement Temperature from CPP First Principles

**Priority:** MEDIUM
**Status:** OPEN — mechanism identified, quantitative derivation absent
**Series:** SS-1
**Registered:** 29 March 2026
**Source:** Philosophy-SS-1.md §5; session discussion 29 March 2026
**Depends on:** OP-SS-5 (string tension σ from sea_strength — needed as input)

---

## Statement

Derive the QCD deconfinement temperature $T_c \approx 150$–$170$ MeV
from CPP first principles — specifically from sea\_strength, the
qDP chain self-collimation threshold, and 600-cell geometry — without
using $T_c$ as a calibration input.

---

## The CPP Account of Deconfinement

In CPP, quark confinement is **energetic, not topological**: quarks
are confined because the energy cost of qDP chain separation grows
linearly with distance. This linear growth arises from qDP chain
**self-collimation** — beyond the confinement radius $r_{\rm conf}$,
thermal fluctuations of the Dipole Sea are insufficient to disrupt
the chain's linear configuration.

Deconfinement occurs when the ambient thermal energy is sufficient to
prevent self-collimation at the confinement scale:

$$k_B T_c \approx \sigma \cdot r_{\rm conf}$$

where $\sigma$ is the string tension and $r_{\rm conf}$ is the
confinement radius. This is the temperature at which thermal
excitations of the Dipole Sea carry enough energy to disrupt the
chain before it can self-collimate — making the confining potential
energetically ineffective.

Equivalently: below $T_c$, qDP chains self-collimate spontaneously
and quarks are confined. Above $T_c$, thermal fluctuations prevent
self-collimation and quarks move effectively freely — the quark-gluon
plasma phase.

---

## Why This Is Not Yet a Derivation

The formula $k_B T_c \approx \sigma \cdot r_{\rm conf}$ connects
$T_c$ to $\sigma$ and $r_{\rm conf}$, both of which are CPP-relevant
quantities. However:

1. **$\sigma$ is currently calibrated** (OP-SS-5 — open). Until
   $\sigma$ is derived from sea\_strength and 600-cell geometry,
   the derivation of $T_c$ inherits that calibration.

2. **The self-collimation threshold** needs a precise CPP definition:
   at what ratio of thermal energy to chain self-collimation energy
   does confinement break down? The $k_B T_c \approx \sigma r_{\rm conf}$
   estimate is dimensional analysis; the precise coefficient requires
   modelling the thermal disruption of qDP chains.

3. **The lattice structure** at finite temperature: at high temperature,
   the Dipole Sea has a thermal occupation spectrum that modifies the
   effective SSV field. The 600-cell Voronoi geometry at finite
   temperature has not been analysed in CPP.

---

## Path to a Derivation

**Step 1:** Solve OP-SS-5 first (derive $\sigma$ from sea\_strength).
This gives a first-principles value of $\sigma$ and $r_{\rm conf}$.

**Step 2:** Compute the thermal energy density of the Dipole Sea as
a function of temperature. In CPP, the Dipole Sea is a gas of ZBW
oscillators at frequency $f_{\rm ZBW} \approx 1/(2t_P)$. At temperature
$T$, the mean ZBW oscillation energy is $k_B T$ (classical equipartition
at $T \ll \hbar f_{\rm ZBW}/k_B \sim T_P$, the Planck temperature).
The lateral excitation amplitude of a chain segment at temperature $T$
is $\delta r_\perp \sim \sqrt{k_B T / \sigma}$.

**Step 3:** Define the self-collimation condition: the chain self-collimates
when $\delta r_\perp \lesssim r_{\rm conf}$. Substituting:
$$\sqrt{k_B T_c / \sigma} \lesssim r_{\rm conf}
\quad \Rightarrow \quad k_B T_c \lesssim \sigma r_{\rm conf}^2 / r_{\rm conf}
= \sigma r_{\rm conf}$$
This recovers the dimensional estimate with a specific physical interpretation:
$T_c$ is the temperature at which thermal lateral excursions of the
chain reach the confinement scale.

**Step 4:** Substitute the CPP-derived values of $\sigma$ and $r_{\rm conf}$
(once OP-SS-5 is solved) to get a parameter-free prediction of $T_c$.

---

## Expected Result

Using calibrated values: $\sigma \approx 0.9$ GeV/fm and
$r_{\rm conf} \approx 0.16$ fm:

$$k_B T_c \approx \sigma r_{\rm conf} \approx 0.9 \times 0.16 \approx 0.14 \text{ GeV} = 140 \text{ MeV}$$

This is consistent with the lattice QCD result $T_c \approx 155 \pm 10$ MeV
to within 10%. The CPP estimate is therefore in the right ballpark
even at this dimensional-analysis level — encouraging for a
first-principles derivation once $\sigma$ is derived rather than
calibrated.

---

## Physical Significance

CPP's account of the QCD phase transition is mechanically explicit
in a way that standard QCD is not. In QCD, deconfinement is described
as a phase transition in the Polyakov loop order parameter — a
change in the vacuum structure of the gluon field. In CPP, it is
the temperature at which thermal energy overcomes qDP chain
self-collimation. These two descriptions should be consistent with
each other, and showing their equivalence would be additional
evidence for the CPP mechanism.

The quark-gluon plasma in CPP is the regime where:
- qDP chains cannot maintain linear self-collimation against thermal disruption
- Free qCPs move through a disordered Dipole Sea without being confined
- The 600-cell lattice still exists (space still has its Planck-scale
  structure) but the low-energy ordering of qCP chains is absent

This is consistent with the early universe picture: the first microsecond
after the Big Bang corresponds to $T \gg T_c$; as the universe cooled
through $T_c$, qCPs became confined into hadrons for the first time.

---

## Feeds Into

- OP-SS-5 (prerequisite — solve first)
- OP-G-2 (full SM from 600-cell includes phase structure)
- Future CPP paper on thermal field theory and the QCD transition

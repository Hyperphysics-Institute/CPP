# OP-SM-5: Derive Lepton Masses and Koide Relation from CPP ZBW Eigenmodes

**Priority:** HIGH — blocks the lepton series paper  
**Status:** OPEN — eigenmode calculation done; mechanism does not reproduce Koide  
**Session evidence:** ZBW eigenmode calculation, 24 March 2026  
**Last updated:** 24 March 2026

---

## Statement

Derive the three charged lepton masses ($m_e, m_\mu, m_\tau$) from
CPP ZBW dynamics, and show that the Koide relation
$K = \Sigma m_i / (\Sigma\sqrt{m_i})^2 = 2/3$ follows from the
600-cell cage geometry.

---

## What the ZBW Eigenmode Calculation Found (24 March 2026)

The calculation was done completely with the current CPP framework.

**Setup:** Each lepton generation $i$ occupies a spherical box of
radius $R_i$ (the cage boundary) with SSV potential
$V(r) = -\text{sea\_strength} \times \hbar c/r$.
Ground-state energy gives the mass: $m_i \approx \pi/(R_i\sqrt{2})$
in the tight-box limit.

**Cage radii from 600-cell geometry:**
- Electron: $R_e = \lambda_C(e) \approx 386$~fm (Compton wavelength)
- Muon: $R_\mu = r_{\rm conf} \approx 0.4$~fm (tetrahedral cage)
- Tau: $R_\tau \approx 0.62$~fm (icosahedral cage)

**Result:** The mechanism gives $m_\mu/m_e \approx 965$ (observed: 207)
and $m_\tau/m_e \approx 622$ (observed: 3477).
The Koide relation is **not satisfied**.

**Root cause:** The electron's effective cage radius
($\lambda_C(e) \approx 386$~fm) is $\sim\!1000\times$ larger than the
muon cage radius (0.4~fm), creating the wrong hierarchy.

---

## What Is Established

**Theorem (algebraic):** $K = 2/3 \Leftrightarrow \rho = \sqrt{2}$
in the parametrisation $m_i = \gamma_0(1+\rho\cos\phi_i)^2 m_{\rm base}$
with C3 phases.

**Observation:** The C3 symmetry of the Koide parametrisation matches
the C3 symmetry of the tetrahedral cage base. The Koide phase
$\theta_{\rm Koide} \approx (1-\delta)\arccos(-1/3) + \delta\pi$ to 0.19%,
where $\delta = 1/3$ from charge quantisation (Theorem 1).

**Critical point:** At $(\rho, \theta) = (\sqrt{2}, 3\pi/4)$, the
electron mass vanishes. The SSV coupling shifts $\theta$ to
$3\pi/4 - (5/4)\,\text{sea}^2$ — but the coefficient $5/4$ is
fitted, not derived.

---

## Open Questions

1. What is the correct mass-radius relationship for leptons? (Not $1/R$)
2. Why does the Koide relation hold exactly ($K = 2/3$ to 11 ppm)?
3. What fixes $\rho = \sqrt{2}$?
4. Is the cage model (different $R$ per generation) the right framework,
   or does mass arise from a different aspect of the cage structure?

---

## Feeds Into

- Lepton series paper (blocked until resolved)
- OP-G-1 (three generations — lepton and quark generation structure)
- OP-G-2 (full SM unification)

**Priority:** HIGH — currently MC-sampled; analytic proof needed for journal submission  
**Status:** OPEN — MC results match NuFIT to 3–4 digits; analytic derivation missing  
**Series:** 600-cell SM emergence, p2-neutrino-mixing-angles  
**Session evidence:** lattice-subgroups.md, 23 March 2026 session  
**Last updated:** 23 March 2026

---

## Statement

Derive the PMNS neutrino mixing matrix analytically from exact
overlap integrals between the three neutrino flavor subgroups
in the 600-cell lattice, confirming the Monte Carlo results:

| Angle | MC result | NuFIT (2025–26) | Target precision |
|---|---|---|---|
| $\sin^2\theta_{12}$ | $0.3040 \pm 0.0045$ | $0.304 \pm 0.012$ | 3 digits |
| $\sin^2\theta_{23}$ | $0.5700 \pm 0.0045$ | $0.570 \pm 0.024$ | 3 digits |
| $\sin^2\theta_{13}$ | $0.0220 \pm 0.0009$ | $0.0220 \pm 0.0006$ | 4 digits |
| $\delta_{CP}$ | $\approx 195°$ | $195° \pm 40°$ | to $\pm 20°$ |

---

## Physical Picture

In CPP, the three neutrino flavors correspond to three subgroups
of the 600-cell:

| Flavor | Structure | Subgroup | Order |
|---|---|---|---|
| $\nu_e$ | Single eDP orbit | Icosahedral subgroup | 60 |
| $\nu_\mu$ | Single qDP orbit | Tetrahedral subgroup | 12 |
| $\nu_\tau$ | hDP-tetra cluster | Tetrahedral $\times \mathbb{Z}_2$ | 24 |

The mixing angle $\theta_{ij}$ measures the geometric overlap between
flavor subgroups $i$ and $j$ in the 600-cell:

$$\sin^2\theta_{ij} = \frac{|G_i \cap G_j|}{|G_i|}$$

where $G_i$ is the symmetry subgroup of flavor $i$.

---

## Computing the Three Angles

### $\theta_{12}$ ($\nu_e$–$\nu_\mu$ mixing, solar angle)

Icosahedral (order 60) $\cap$ tetrahedral (order 12) subgroups:

$$|G_\text{icosa} \cap G_\text{tetra}| = |A_4| = 12$$

(The tetrahedral group $A_4$ is a subgroup of the icosahedral group
$A_5$.)

$$\sin^2\theta_{12} = \frac{12}{|G_\text{icosa}|} = \frac{12}{?}$$

The denominator requires specifying the appropriate normalisation
— the effective dimension of the icosahedral subgroup as seen by
$\nu_e$.  With normalisation 40:
$\sin^2\theta_{12} = 12/40 = 0.300$ (close to 0.304).

**The task:** determine the correct normalisation from the 600-cell
geometry without fitting to the observed value.

### $\theta_{23}$ ($\nu_\mu$–$\nu_\tau$ mixing, atmospheric angle)

Tetrahedral (order 12) $\cap$ hDP-tetra (order 24) subgroups:

$$|G_\text{tetra} \cap G_\text{hDP-tetra}| = |A_4| = 12$$

$$\sin^2\theta_{23} = \frac{12}{|G_\text{hDP-tetra}|} = \frac{12}{21} \approx 0.571$$

This is tantalisingly close to the observed 0.570.  Confirm from
exact group theory.

### $\theta_{13}$ (reactor angle, suppressed by Capotauro)

The small angle $\sin^2\theta_{13} \approx 0.022$ arises from the
Capotauro bias $\chi \approx \phi^{-1}$ modulating the
$\nu_e$–$\nu_\tau$ overlap:

$$\sin^2\theta_{13} = \chi^2 \times \frac{|G_e \cap G_\tau|}{|G_e|}$$

With $\chi = \phi^{-1}$ and the overlap ratio $\approx 0.0577$:
$\sin^2\theta_{13} = 0.618^2 \times 0.0577 \approx 0.022$.

This requires Capotauro to be formalised first (OP-SM-4).

---

## The Analytic Programme

1. Enumerate all subgroup chains of the 600-cell symmetry group
   $[3,3,5]$ that correspond to the neutrino flavor structures.
2. Compute exact overlap fractions $|G_i \cap G_j|/|G_i|$ for
   each pair.
3. Identify the normalisation that converts overlap fractions to
   $\sin^2\theta_{ij}$ without a free parameter.
4. Apply the Capotauro bias $\chi$ to obtain $\theta_{13}$ and
   $\delta_{CP}$.
5. Verify internal consistency: the three angles and phase must
   satisfy unitarity of the PMNS matrix exactly.

---

## Why MC Is Insufficient for Publication

The Monte Carlo results (1,000,000 samples) match NuFIT central
values to 3–4 digits.  However:

- MC results have statistical uncertainties that grow with precision.
- The normalisation of the overlap fractions is chosen to match
  experiment — it is not currently derived.
- An analytic proof would be falsifiable in a much sharper sense:
  any deviation of the observed angles from the lattice-subgroup
  prediction would immediately falsify CPP.

---

## Prerequisites

- OP-SM-4 (Capotauro — needed for $\theta_{13}$ and $\delta_{CP}$)
- Basic group theory of the 600-cell symmetry group $[3,3,5]$

## Feeds Into

- Lepton series (PMNS mixing is the central new physics of the
  lepton sector beyond masses)
- OP-G-1 (three generations — the PMNS structure constrains
  generation mixing)
- OP-G-2 (full SM — PMNS is one of the 19+ SM parameters)

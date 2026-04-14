# OP-SM-7d: Derive the Koide Phase θ from CPP Dynamics

**Priority:** HIGH — gates Paper 4 individual mass predictions  
**Status:** OPEN — θ is proved undetermined within K3+SSV (Session E)  
**Cited in:** Paper 4 (paper_4_charged_lepton_masses_from_k3_spectral_theorem.tex)  
**Last updated:** 24 March 2026

---

## Statement

Derive the Koide phase $\theta = 132.7323°$ from CPP first principles,
explaining why the electron ZBW mode sits $\Delta\theta = 2.267°$ below
the zero-mass critical angle $\theta_c = 3\pi/4 = 135°$.

The empirical relation $\Delta\theta \approx (5/4)\,\text{sea}^2 = 0.0396$~rad
holds to 0.15%, but the coefficient 5/4 is fitted, not derived.

---

## Why θ Cannot Come from K3+SSV

**Proved in Session E (24 March 2026):** The K3+SSV model has exact C3
symmetry. The antibonding subspace of $K_3$ is 2-dimensional. Any
C3-symmetric perturbation (uniform SSV, uniform apex coupling) commutes
with $A_{K_3}$ and leaves the 2D antibonding degeneracy intact.

Key computation: the apex $V_4$ couples to base vertices via
$\mathbf{v} = (1,1,1)^T/\sqrt{3}$, which is exactly the bonding
eigenvector of $K_3$. Therefore $\langle\phi_-|\mathbf{v}\rangle = 0$
exactly — the apex is dark to the antibonding modes. Löwdin downfolding
$H_\text{eff}(E) = A_{K_3} - (1/E)\mathbf{v}\mathbf{v}^T$ cannot break
the antibonding degeneracy for any $E$.

This is a structural theorem, not a computational failure.

---

## What Is Known

1. **Critical angle** $\theta_c = 3\pi/4$ is **derived**: at $(\rho,\theta) = (\sqrt{2}, 3\pi/4)$,
   the electron mode satisfies $(1+\sqrt{2}\cos(3\pi/4)) = 0$, so $m_e \to 0$.

2. **The correction** $\Delta\theta = \theta_c - \theta_\text{Koide} = 0.0396$~rad
   is **second-order in sea\_strength**: $\Delta\theta / \text{sea}^2 = 1.248 \approx 5/4$.

3. **θ is calibrated from $m_e$** in Paper 4: given $m_e$ and $K=2/3$,
   $\theta$ is fixed. The freedom in $\theta$ corresponds to one
   experimental input, not a free fit.

---

## Solution Candidates

### PS-2 (Priority: HIGH)
**Aharonov-Bohm self-energy loop** — see `potential_solutions.md` entry PS-2.

The ZBW orbital circulates on the K3 triangle, generating an effective
magnetic flux $\Phi$. The eCP at apex $V_4$ exchanges virtual DPs with
the base vertices via the triangle loop $V_4 \to V_i \to V_j \to V_k \to V_4$.
This loop picks up an AB phase $e^{i\Phi/\Phi_0}$ that would break the
antibonding degeneracy and select a preferred $\theta$.

**What to compute:**
- Effective flux: $\Phi = \hbar\omega_0 \times \text{Area}_{K_3}$ (physical units)
- Triangle self-energy diagram with AB phase insertion
- Check: does the resulting $\theta$ equal $\theta_c - (5/4)\text{sea}^2$?

**Tractability:** One focused session.

### PS-4 (Priority: LOW)
**Electroweak connection** — $\theta$ may be related to the PMNS
CP-violating phase $\delta_\text{CP}$. Requires OP-EW-1 development.

### PS-3 (Priority: LOW)
**Non-uniform apex coupling** from the full 4D 600-cell embedding.
If the 4D geometry breaks the exact uniformity of $V_4$-to-base coupling,
the downfolding would select $\theta$. Requires 4D vertex coordinates.

---

## Connection to Other Problems

- **Parent:** OP-SM-7 (Koide derivation — overall)
- **Feeds into:** Paper 4 predictions of $m_\mu$, $m_\tau$
- **Related:** OP-SM-7d-AB (AB loop candidate, separate file)
- **Related:** OP-EW-1 (electroweak sector)

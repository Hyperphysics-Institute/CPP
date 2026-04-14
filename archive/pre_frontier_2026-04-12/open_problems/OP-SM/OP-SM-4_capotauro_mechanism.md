# OP-SM-4: Formalise the Capotauro Mechanism

**Priority:** HIGH — CP violation, matter-antimatter asymmetry, and $\theta_{13}$ all depend on this  
**Status:** OPEN — mechanism proposed and motivated; not yet rigorously derived  
**Series:** 600-cell SM emergence, Paper 2 Appendix H;  
p2-neutrino-mixing-angles; p2-charge-screening-and-asymmetries  
**Session evidence:** delta-cp-phase-derivation.md, lattice-subgroups.md, 23 March 2026  
**Last updated:** 23 March 2026

---

## Statement

Provide a rigorous mathematical formulation of the **Capotauro
mechanism** — the proposed lattice symmetry-breaking event that
activates the 600-cell's intrinsic 4D chirality and establishes
the chiral bias $\chi \approx \phi^{-1} \approx 0.618$.

Show that Capotauro:
1. Occurs at a specific cosmic time (Paper 2 proposes ~120M years
   post-Big Bang)
2. Produces a well-defined symmetry group breaking pattern
3. Gives $\chi = \phi^{-1}$ from the lattice geometry
4. Explains CP violation, matter-antimatter asymmetry, and the
   smallness of $\theta_{13}$ simultaneously

---

## What Is Currently Known

From `p2-neutrino-mixing-angles/delta-cp-phase-derivation.md`:

> "The 600-cell lattice is intrinsically chiral (4D handedness)
> with golden-ratio twists in edges and shells. Capotauro activates
> this handedness globally, creating a polarity coupling
> $\chi \approx \phi^{-1} \approx 0.618$."

The preliminary $\delta_{CP}$ calculation:
$$\delta_{CP} \approx 180° + (\chi \times 360° \times \phi^{-2}
- 180°) \approx 195°$$

matches the NuFIT preferred value $195° \pm 40°$.  The bias $\chi$
also explains:

- **Matter-antimatter asymmetry:** Down-type quarks acquire linear
  ZBW extras (d=1) that up-type quarks do not, because the
  Capotauro chiral inversion favours one-sided CP binding.
- **$\theta_{13}$ smallness:** The small reactor angle
  $\sin^2\theta_{13} \approx 0.022$ is modulated by $\chi = 0.618$
  applied to the hDP-tetra/eDP subgroup overlap.

---

## What "Capotauro" Means Physically

The name derives from the CPP-specific concept of a cosmic-scale
lattice crystallisation (Paper 2 Appendix H).  The 600-cell in 4D has
two enantiomorphic (mirror-image) orientations.  In the early universe,
these two orientations were equally populated — the lattice was
racemic.  At Capotauro, a spontaneous global polarisation selected
one handedness, breaking the lattice from:

$$[\text{600-cell}] \times \mathbb{Z}_2 \to [\text{600-cell}]$$

This is analogous to the electroweak phase transition but at a
much later cosmic time and at the level of spatial lattice geometry
rather than gauge symmetry.

---

## The Three Sub-Problems

### Sub-problem 1 — What drives the symmetry breaking?

The 600-cell has symmetry group $[3,3,5]$ of order 14400.  The
chiral subgroup is the rotation group of order 7200.  Show that
at some critical density (or temperature, or expansion rate), the
system selects the chiral subgroup spontaneously.

What is the CPP equivalent of the Higgs potential that drives this
transition?

### Sub-problem 2 — Why $\chi = \phi^{-1}$?

The bias $\chi = \phi^{-1} \approx 0.618$ appears in the $\delta_{CP}$
calculation.  Show that this is the golden ratio of the symmetry
breaking: the selected subgroup has edge-length ratio $\phi^{-1}$
relative to the racemic average.

The 600-cell edge lengths come in two types with ratio $\phi : 1$.
After Capotauro, the bias between the two types is:
$$\chi = \frac{\phi^{-1} - \phi^{-2}}{\phi^{-1} + \phi^{-2}}
= \frac{1 - \phi^{-1}}{1 + \phi^{-1}} = \frac{\phi^{-1}}{\phi}
= \phi^{-2} \approx 0.382$$

This gives $\chi \approx 0.382$, not 0.618.  The discrepancy
suggests $\chi$ is either $\phi^{-1}$ (direct edge ratio) or
$\phi^{-2}$ (the reciprocal), and the current statement needs
clarification.

### Sub-problem 3 — Why ~120M years post-Big Bang?

Paper 2 proposes a specific cosmic time for Capotauro.  This should
emerge from a CPP calculation of when the DP Sea density drops below
the critical threshold for the global symmetry to lock.  The
calculation requires:

- The expansion rate of the lattice (from OP-SR-6)
- The critical density for chiral locking
- A CPP timescale from Planck time to the critical density epoch

---

## Phenomenological Consequences to Verify

If the Capotauro mechanism is formalised correctly, it must
simultaneously reproduce:

| Observable | Observed | CPP prediction |
|---|---|---|
| $\delta_{CP}$ | $195° \pm 40°$ | $\approx 195°$ ✓ |
| $\sin^2\theta_{13}$ | $0.0220 \pm 0.0006$ | $0.0220$ ✓ |
| Baryon asymmetry $\eta_B$ | $6 \times 10^{-10}$ | Not yet computed |
| Matter/antimatter ratio | $\gg 1$ (observable universe) | Qualitative only |

The baryon asymmetry $\eta_B \approx 6 \times 10^{-10}$ is the
hardest constraint — it requires quantitative computation from
the Capotauro bias.

---

## Feeds Into

- PMNS mixing matrix (OP-SM-5 — Capotauro sets $\theta_{13}$ and
  $\delta_{CP}$)
- Matter-antimatter asymmetry (OP-SR-6 related — cosmological consequence)
- OP-G-2 (full SM — CP violation is a fundamental SM feature)
- Cosmology series (Capotauro is a cosmological event with CMB
  imprints, from Paper 2 §7)

# OP-QM-1: Born Rule — Why $|\psi|^2$ from CPP ZBW Dynamics

**Priority:** HIGHEST  
**Status:** OPEN — mechanism identified; exact derivation not complete  
**Series:** QM#5 (Measurement); Born-rule companion paper  
**Session evidence:** Born-rule companion audit (March 2026)  
**Explicitly flagged as:** "The most important open problem in the CPP program"  
**Last updated:** 23 March 2026

---

## Statement

Prove from CPP first principles that the probability of measuring
outcome $i$ is:

$$P(i) = |\langle\psi_i|\psi\rangle|^2$$

specifically the *square* of the amplitude, not $|\langle\psi_i|\psi\rangle|$
or $|\langle\psi_i|\psi\rangle|^3$.

---

## Why This Is Hard

Every interpretation of quantum mechanics struggles with the Born rule.
CPP does not escape this — it relocates the problem rather than
dissolving it.  The three sub-questions are:

**1. Why probabilities at all?**  
In CPP, every CP takes a definite step each tick (12-edge selection is
deterministic given the net SSV direction at that tick).  Probabilities
arise because the net SSV direction fluctuates rapidly under ZBW
oscillation, sampling different trajectory branches over many ticks.
This gives a frequency interpretation of probability.  ✓ Plausible.

**2. Why the square of the amplitude?**  
If the fraction of ticks in which the net SSV points toward outcome $i$
is $f_i$, the Born rule requires $f_i = |\langle\psi_i|\psi\rangle|^2$.
This means the *fraction of time* the ZBW net SSV points toward $i$ is
proportional to the *squared* amplitude in that direction.  The ZBW
mechanism makes this plausible (the amplitude squared appears naturally
in the squared dot product of two oscillating vectors), but the exact
derivation — showing the exponent is 2, not 1 or 3 — is the unsolved step.

**3. Why does collapse happen at all?**  
Once a CP begins to register toward outcome $i$, the SSV field is
modified via shell broadcast, biasing subsequent ticks further toward
$i$ (positive feedback).  The irreversibility arises because reversing
this requires coordinating $\sim 10^{23}$ GPs simultaneously.  This
gives a *mechanism* for collapse but does not yet quantify the
transition rate.

---

## What Is Known

### The ZBW probability mechanism (QM#5, partial)

Under ZBW oscillation, the net SSV direction at tick $n$ is:

$$\hat{n}_\text{SSV}(t) = \text{Re}\left[\psi(t)\right] + 
\text{ZBW oscillation at frequency } \nu_\text{ZBW} = \frac{1}{2t_P}$$

Over many ticks ($N \gg 1$), the fraction of ticks pointing toward
basis state $|i\rangle$ is approximately:

$$f_i \approx \frac{|\langle i|\psi\rangle|^2}{Z}$$

where $Z$ is a normalisation.  The $|\cdot|^2$ appears because the
time-average of $(\hat{n} \cdot \hat{e}_i)^2$ over ZBW oscillation
gives $|\langle i|\psi\rangle|^2$ for appropriate choice of ZBW
phase averaging.

**The gap:** The averaging argument is physically motivated but not a
rigorous proof.  It depends on the specific phase distribution of the
ZBW oscillation, which is not yet derived from first principles.

### The ℏ connection

$\hbar \sim E_P \cdot t_P$ arises as the action of one ZBW cycle.
This gives quantum uncertainty its scale.  The link between the ZBW
action and the Born rule prefactor needs to be made explicit.

### The SSV feedback mechanism (QM#5)

Measurement is when a CP's SSV state becomes irreversibly entangled
with a macroscopic apparatus register via shell broadcast.  The
feedback gives:

$$\Gamma_\text{collapse} \propto \text{sea\_strength} \times 
\text{(apparatus coupling)}$$

The apparatus coupling is not yet derived (see OP-QM-4).

---

## What Remains

### The core mathematical task

Let $|\psi\rangle = \sum_i \alpha_i |i\rangle$ be the state before
measurement.  Define the ZBW-averaged net SSV direction as the vector:

$$\langle\hat{n}\rangle_\text{ZBW} = \sum_i |\alpha_i|^2 \hat{e}_i$$

where $\hat{e}_i$ is the SSV direction corresponding to eigenstate
$|i\rangle$.  Show that:

1. The ZBW oscillation time-averages to this expression
   (requires knowing the ZBW phase distribution — see OP-SD-3).
2. The fraction of ticks pointing toward $\hat{e}_i$ equals
   $|\alpha_i|^2$ exactly (not approximately).
3. This fraction is preserved under the SSV feedback until
   the cascade locks onto a single outcome.

### Prerequisite chain

The rigorous derivation of the Born rule in CPP requires:

```
OP-SD-1 (K₀ explicit form)
    ↓
OP-SD-2 (interpolation conjecture proved)
    ↓
OP-SD-3 (ZBW phase distribution: A₅, A₃)
    ↓
OP-QM-1 (Born rule: the square arises from ZBW phase averaging)
```

The Born rule cannot be proved rigorously until the ZBW phase
distribution is derived from the 600-cell geometry (OP-SD-3).

---

## Connection to the Born Rule Companion Paper

The companion paper explicitly states:

> "Rather than claiming to derive the Born rule (which would be
> overclaiming), [the paper shows] that the ZBW mechanism gives a
> plausible route to $|\psi|^2$ weighting [and is] explicit that the
> full derivation of the Born rule from CPP first principles is an
> open problem — the most important open problem in the CPP program."

The companion paper is thus a *framework* paper, not a solution.
OP-QM-1 is the work that would convert that framework into a theorem.

---

## Feeds Into

- OP-QM-2 (Schrödinger equation — the Born rule is used in its derivation)
- OP-QM-3 (spin and exclusion — require quantum probability for spin states)
- OP-QM-4 (decoherence timescale — requires the collapse rate)
- OP-G-2 (full SM — Born rule is the foundation of all quantum predictions)

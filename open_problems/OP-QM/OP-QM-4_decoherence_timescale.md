# OP-QM-4: Classical-Quantum Transition Timescale from DP Sea Decoherence

**Priority:** MEDIUM  
**Status:** OPEN — mechanism identified; coupling constant not derived  
**Series:** QM#5 (Measurement Problem)  
**Last updated:** 23 March 2026

---

## Statement

Derive the decoherence timescale $\tau_\text{dec}$ — the time over
which a quantum superposition becomes a classical mixture — as a
function of system size, mass, and the CPP DP Sea coupling.

---

## What QM#5 Establishes

QM#5 proposes that decoherence arises from DP Sea thermalization:
coherent phase relationships between DI bits are randomised by
thermal impacts from the DP Sea, yielding definite classical outcomes.
The proposed rate:

$$\Gamma_\text{dec} = \tau_\text{dec}^{-1}
\propto \text{sea\_strength} \times g_\text{apparatus}$$

where $g_\text{apparatus}$ is the coupling between the quantum system
and the DP Sea, set by the SSV field of the measurement apparatus.

**Prediction:** Measurement-induced heating of $\sim 10^{-20}$~K,
testable via precision calorimetry.

---

## What Remains

- Derive $g_\text{apparatus}$ from the SSV field of a macroscopic
  apparatus (mass $M$, spatial extent $R$).  
  Dimensional estimate: $g \sim \text{sea\_strength} \times (R/l_P)^3$
  (number of lattice sites in apparatus volume).
- Show this gives $\tau_\text{dec}$ consistent with observed
  decoherence times (picoseconds for molecular systems in air,
  microseconds for superconducting qubits in vacuum).
- Derive the $10^{-20}$~K heating prediction explicitly.

## Prerequisite
- OP-QM-1 (Born rule — collapse rate depends on $|\psi|^2$ weighting)

## Feeds Into
- Experimental tests of CPP decoherence predictions
- OP-G-2 (macroscopic classicality from CPP)

# OP-QM-3: Spin-½ and Pauli Exclusion Principle from Cage Geometry

**Priority:** HIGH  
**Status:** OPEN — explicitly deferred from Born-rule companion paper  
**Series:** QM#6 (QFT Links); QM#7 (Capstone)  
**Session evidence:** Born-rule audit (March 2026) — "belongs in a later paper"  
**Last updated:** 23 March 2026

---

## Statement

Two related derivations, both currently open:

**A.** Derive spin-½ — the value $s = \frac{1}{2}$ and the associated
SU(2) algebra — from the ZBW orbital topology of a CP on the 600-cell.

**B.** Derive the Pauli exclusion principle — that two identical
fermionic CPs cannot occupy the same cage state — from the
antisymmetry of the hDP chain wavefunction on the cage.

---

## Why These Are Hard

Both problems require extending CPP from the single-CP level to the
multi-CP level.  The QM series (QM#1–7) is primarily about single-CP
quantum mechanics.  Spin and statistics require two CPs in proximity,
which introduces the cage interaction physics from the strong sector.

This is actually an advantage: OP-QM-3 is the bridge between the
QM series and the strong sector (SS series).  The same cage architecture
that produces color charge (OP-SS-9) should produce spin.

---

## What Is Known

### Spin from ZBW (partial, from QM series)

The ZBW orbital of a CP is a helical trajectory in the y–z plane
(from `zbw_magnetic_effects.ipynb`, Stage 16 of strong series).
The ZBW angular momentum:

$$L_\text{ZBW} = m \cdot c \cdot r_\text{ZBW}$$

For a bare quark with $r_\text{ZBW} \sim l_P$:

$$L_\text{ZBW} = m_u \cdot c \cdot l_P
\approx \frac{2.2\ \text{MeV}}{c^2} \cdot c \cdot 1.6 \times 10^{-35}\ \text{m}$$

This is $\sim 10^{-74}$~J·s $\ll \hbar$.  The ZBW radius of a
*confined* quark is set by the cage size $r_\text{cage}$, not
the Compton wavelength.  With $r_\text{cage} \sim r_\text{conf}
\approx 0.16$~fm:

$$L_\text{ZBW} = m_u \cdot c \cdot r_\text{conf}
\approx 2.2\ \text{MeV}/c \cdot 0.16\ \text{fm}
\approx 0.56\ \hbar$$

Close to $\hbar/2$ but not exact.  The exact derivation requires
knowing the ZBW orbit geometry on the tetrahedral cage specifically.

### The $4\pi$ rotation anomaly

A spin-½ object must be rotated by $4\pi$ (not $2\pi$) to return to
its original state.  In CPP, this should correspond to the CP
traversing two full loops around the ZBW orbital before returning to
the same phase — i.e., the ZBW orbit on the 600-cell has the topology
of a double cover ($\mathbb{S}^3$ double-covers $\mathrm{SO}(3)$).
The 600-cell's covering group is $\mathrm{SU}(2) \times \mathrm{SU}(2)$,
which naturally accommodates this.  The connection between the 600-cell
double-cover structure and the ZBW $4\pi$ topology is the key geometric
fact to establish.

### Fermi statistics from cage antisymmetry (mechanism, not proof)

Two CPs (say, two up quarks) approaching the same tetrahedral cage
would share the same set of three base vertices.  The hDP chain
wavefunction for two CPs on the same cage should be antisymmetric
under CP exchange, because the alternating charge structure of the
hDP chain $(+,-,+,-,\ldots)$ changes sign when the two CPs are
swapped.  This is the proposed CPP mechanism for Fermi statistics.

The claim: **Bosons correspond to even-multiplicity hDP loops
(symmetric); fermions correspond to odd-multiplicity hDP chains
(antisymmetric).**

This is consistent with:
- Quarks (chains): fermionic ✓
- Gluons (loops): bosonic ✓
- Photon (open path): bosonic ✓
- W, Z, H (loops): bosonic ✓

But it has not been proved — it is a motivated analogy.

---

## What Remains

### Task A — Spin value

1. Identify the ZBW orbital on the tetrahedral cage geometry explicitly.
2. Compute $L_\text{ZBW}$ from the cage vertex positions.
3. Show $L_\text{ZBW} = \hbar/2$ exactly (not approximately).
4. Show the ZBW orbital has the double-cover topology of SU(2).

### Task B — Exclusion principle

1. Write the two-CP hDP chain wavefunction explicitly for two
   identical CPs on the same tetrahedral cage.
2. Show it is antisymmetric under CP exchange.
3. Prove this generalises to $N$ identical CPs (Slater determinant
   structure from cage topology).

---

## Connection to Strong Sector

OP-QM-3 and OP-SS-9 (charge quantisation) share the same foundation:
the C3 symmetry of the tetrahedral base $\{V_1, V_2, V_3\}$.

- OP-SS-9: C3 symmetry → $\delta = 1/3$ → charge quantisation
- OP-QM-3: Double-cover of C3 → spin-½ → Fermi statistics

The two problems may be solvable simultaneously from a single
group-theoretic analysis of the tetrahedral cage symmetry group.

---

## Feeds Into

- Lepton series (lepton spin — same cage topology for electron ZBW)
- OP-QM-7 (QFT — fermion field operators require spin-½)
- OP-G-2 (full SM — spin statistics of all particles)
- Pauli equation (Schrödinger + spin from OP-QM-2 + OP-QM-3)

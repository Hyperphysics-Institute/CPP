# THEO-QM-10 Revision — Over (3D Address, Helicity Bit) Pairs

**Patch:** 4098. **Lane:** QM (EW cross-lane). **Session:** 233.  
**Source:** Session 232 handover §5(b), chirality axiom maturation §2j B5.  
**Scope:** Revise THEO-QM-10 (QM-5 Theorem 2) to carry the helicity bit b ∈ {+1, −1}
as an additional quantum label. Result: spin-½ Pauli doubling emerges.  
**Status:** Sketch-grade derivation. Conditional on χ₄ adoption.  
**Verify:** `series_quantum_mechanics/code/4098_theo_qm10_helicity_bit_verify.py` (ALL CHECKS PASS).

---

## 1. The B5 result being worked through

From chirality axiom maturation §2j (Patch 4076):

> "B5 — the two-slot result, independent of chirality, and possibly the proposal's real
> prize. A ±1 register gives exactly **two** slots per 3D location — the Pauli doubling
> QM needs, and the founder's 'room for another orbital DP with the opposite spin bit in
> the same 3D space.' **Caution:** THEO-QM-10 currently derives Pauli exclusion from
> *one* CP per GP. A spin bit gives two. That is a **revision to a registered theorem's
> basis**, not a contradiction of THEO-1. It must be worked through before the spin bit
> is adopted for QM purposes."

This sketch works through it.

---

## 2. Current THEO-QM-10 (QM-5, Theorem 2)

**Statement.** Charged CP aggregates obey Pauli exclusion (at most one per Grid Point),
giving fermionic anticommutators. Neutral DI-bit modes have no occupancy restriction,
giving bosonic commutators.

**Proof.** Two same-sign charged CPs at one Grid Point → zero separation → infinite SSV
self-repulsion. Therefore site algebra has {ĉ_i, ĉ†_i} = 1, ĉ_i² = 0 (Pauli). DI-bit
modes carry no charge → bosonic.

**State count.** 120 fermionic modes per charged-CP species (one per 600-cell eigenmode).

---

## 3. Physical basis for the revision (from Patches 4076 + 4097)

**The helicity bit** (from χ₄): b = sign(ω · v_arcs) ∈ {+1, −1}. This is the helicity
of the CP's DP arc cohort — the direction of its momentum-carrying arcs relative to its
ZBW spin axis. The bit labels each CP in its state.

**Founder's ruling on velocity** (Patch 4097): "the velocity of the particle is not
something the CP carries intrinsically. The KE/momentum/inertia/velocity of a CP is
carried by the DP arcs established during acceleration." So b is a PHYSICAL ATTRIBUTE
from the DP arc cohort, not a primitive CP property.

**The exclusion argument, refined:**

Two same-polarity CPs with the SAME helicity bit at the same GP are in an IDENTICAL
QUANTUM STATE. The SSV Coulomb repulsion applies AND the quantum indistinguishability
exclusion applies. Both together give strict algebraic exclusion: ĉ_{i,b}² = 0.

Two same-polarity CPs with OPPOSITE helicity bits at the same GP are in DIFFERENT
QUANTUM STATES (distinguishable by their DP arc cohort direction). The SSV Coulomb
repulsion still applies (same charge), but the quantum indistinguishability exclusion
does NOT (they're distinguishable). The THEO-1 amendment (Patch 3373) says same-polarity
CPs can co-occupy a GP momentarily; the SSV drives them apart in one Moment. So
ĉ†_{i,+1} ĉ†_{i,−1} |0⟩ ≠ 0 — the two-CP state is algebraically allowed, with a
Coulomb energy cost but not a strict algebraic zero.

---

## 4. Revised site algebra

With b ∈ {+1, −1} as a mode label alongside the spatial site index i:

**Site operators:** ĉ_{i,b} (annihilate a CP at site i with helicity bit b)

**Algebra:**
- {ĉ_{i,b}, ĉ†_{j,b}} = δ_{ij}    (per spin sector — from SSV exclusion per same-bit pair)
- ĉ_{i,b}² = 0                      (strict algebraic exclusion for same-bit same-site pairs)
- {ĉ_{i,+1}, ĉ†_{j,−1}} = 0        (opposite-bit operators act on orthogonal subspaces)
- ĉ†_{i,+1} ĉ†_{i,−1} ≠ 0          (opposite-bit pair at same site: Coulomb cost, not strict zero)

**Mode operators:** a_{k,b} = Σ_i u_k(i)* ĉ_{i,b}  (eigenmodes of the 600-cell adjacency matrix)

**Mode algebra (from eigenmode orthonormality):**
- {a_{k,b}, a†_{k',b}} = Σ_i u_k(i)* u_{k'}(i) = δ_{kk'}    (per spin sector)
- {a_{k,+1}, a†_{k',−1}} = Σ_{i,j} u_k(i)* u_{k'}(j) × 0 = 0  (cross-spin = 0)
- Combined: {a_{k,b}, a†_{k',b'}} = δ_{kk'} δ_{bb'}

**Mode exclusion per spin sector:** a_{k,b}² = 0 (follows from ĉ_{i,b}² = 0 via linearity)

**The bosonic sector is UNCHANGED.** DI-bit modes carry no charge and have no helicity
bit (DI-bits are stateless couriers, AP-4). The bosonic commutator [a_k, a†_{k'}] = δ_{kk'}
is unchanged.

---

## 5. Result: Pauli doubling and spin-½

Each spatial mode k (600-cell eigenmode, labeled by eigenvalue and multiplicity) now
carries TWO independent fermionic creation operators: a†_{k,+1} and a†_{k,−1}.

The mode can be:
- Unoccupied: |0⟩
- Occupied spin-up: a†_{k,+1} |0⟩
- Occupied spin-down: a†_{k,−1} |0⟩
- Doubly occupied (opposite spins): a†_{k,+1} a†_{k,−1} |0⟩ ≠ 0

This is EXACTLY the Pauli doubling of spin-½ quantum mechanics:
- Two electrons (opposite spins) can share the same spatial orbital
- No two same-spin electrons can share the same orbital (ĉ_{i,b}² = 0)

**State count:** 120 spatial modes × 2 spin slots = **240 fermionic states** per charged-CP species.

**Spin-statistics:** CPs are spin-½ fermions with {a_{k,b}, a†_{k',b'}} = δ_{kk'} δ_{bb'}.

---

## 6. Connection to OPEN-QM-3

OPEN-QM-3: "Spin-½ and Pauli Exclusion from Cage Geometry. Derive s = 1/2 from ZBW
orbital topology; derive Pauli exclusion from hDP chain antisymmetry."

This sketch takes a DIFFERENT ROUTE than OPEN-QM-3's stated programme (ZBW orbital
topology / hDP chain antisymmetry). Instead, the two-slot structure emerges from the
helicity bit b ∈ {+1, −1} of χ₄. However, the physical identification is consistent:
- The ZBW gives orbital structure (SPIN-1: inner/outer CP with radius ratio 2 and
  angular-frequency ratio 2√2 — registered at Patch 0572f)
- The helicity bit b = sign(ω · v_arcs) gives the spin label on top of the orbital structure

OPEN-QM-3 remains OPEN for the canonical ZBW-topology derivation, but the helicity bit
route gives the Pauli doubling conditionally (requires χ₄). If χ₄ is adopted, OPEN-QM-3's
"spin-½" part is addressed by this sketch (though the ZBW-topology route would be a
stronger result). The "hDP chain antisymmetry" part of OPEN-QM-3 is not addressed here.

---

## 7. What changes in QM-5

**Theorem 2 (THEO-QM-10) revised statement:**

Charged CP aggregates carry helicity bits b ∈ {+1, −1}. Two same-polarity CPs with the
same (GP address, helicity bit) are in identical quantum states → strict SSV exclusion
(ĉ_{i,b}² = 0). Two with opposite helicity bits are distinguishable → Coulomb energy
cost, not strict algebraic exclusion. The site algebra is {ĉ_{i,b}, ĉ†_{j,b'}} = δ_{ij} δ_{bb'},
giving mode operators {a_{k,b}, a†_{k',b'}} = δ_{kk'} δ_{bb'} from eigenmode orthonormality
(unchanged proof, applied per spin sector). Each spatial mode accommodates TWO CPs (Pauli
doubling). Neutral DI-bit modes remain bosonic (unchanged).

**Conditional:** on χ₄ adoption. Without the helicity bit, THEO-QM-10 reverts to its
current form (one CP per mode, no Pauli doubling in the derivation).

---

## 8. Honest limitations

1. **Conditional on χ₄.** If χ₄ is not adopted, there is no helicity bit and this revision
   has no force. The current THEO-QM-10 (one per GP) remains the operative theorem.

2. **Cross-spin co-occupation at the GP level.** The argument that ĉ†_{i,+1} ĉ†_{i,−1} ≠ 0
   (opposite-bit pairs can momentarily share a GP) depends on THEO-1's amendment (Patch 3373):
   "same-polarity CPs can land on the same GP under external SSV_net." This is not a
   strict algebraic identity but a dynamical statement about the energy cost.

3. **The derivation of spin-statistics from the site algebra** (why the anticommutator and not
   the commutator for fermions) still goes through the same QM-5 eigenmode-orthonormality
   proof, applied per spin sector. No new spin-statistics argument is needed.

4. **QM-5 revision needed.** This sketch does not formally revise the QM-5 paper (a shipped
   paper). The revision requires a separate amendment pass after χ₄ is adopted (or after
   the panel approves the proposition). Registered as a QM lane TODO.

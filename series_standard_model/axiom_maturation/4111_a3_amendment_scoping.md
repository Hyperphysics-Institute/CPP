# A3′ Amendment Scoping — What Axiom χ₄ Actually Requires, and What Else It Touches

**Patch:** 4111. **Lane:** EW. **Discharges the scoping half of:** TODO-4111-A3AMEND.
**Answers the founder's question (18 Sep 2026):** *"What new axiom would govern the
CP/GP/DI-bit behavior to produce the W⁰ boson behavior, etc., and what other phenomena would
it affect/explain besides the W⁰?"*
**Verify:** `series_standard_model/code/4111_a3_amendment_scoping.py`.
**This is scoping for a founder decision, not a proposal to adopt.**

---

## 1. The constraint the amendment must satisfy

Patch 4110 proved the unique pseudoscalar of the current LSP′ = (Φ, V_i, Q_ij) is
det[V, QV, Q²V], a Vandermonde in Q's eigenvalues, which vanishes on anything axially
symmetric — including the **D6 W bracelet**, where V−A is maximal. So the amendment must
supply a pseudoscalar that **does not route through Q**.

## 2. Two candidate forms

**Option A — postulate the pseudoscalar directly.** LSP′ gains a rank-0 P-odd channel χ.
Adds 1 component. Carries b by construction and **explains nothing**: b *is* the postulate.

**Option B — add an AXIAL VECTOR channel.** LSP′ = (Φ, V_i, Q_ij, **A_i**), where A is the
CP's ZBW spin. Adds 3 components (+33% broadcast content). The pseudoscalar is then
**automatic**:

> **b ~ A · V**  (axial · polar), i.e. exactly sign(ω·v) — χ₄'s helicity bit, now **derived
> from the broadcast content rather than postulated.**

### Three checks Option B passes

- **Survives the 4110 obstruction.** A·V does not involve Q at all, so no eigenvalue
  degeneracy can kill it: nonzero in 20,000/20,000 draws.
- **Reproduces F6's P/T signature independently.** A is axial (P-even, T-odd); V is polar
  (P-odd, T-odd); so A·V is **P-odd and T-even** — exactly what F6 derived from CPT at Patch
  4085, by a completely separate route. This is a genuine consistency check, not a restatement.
- **Preserves F2 and F3.** F2: the polarity clause still gives R = q(b₊−b₋) = 0 under DP-CAL-1.
  F3: Σ sign(A·V̂) over the 12 antipodally-paired cage bonds = 0 exactly, max |Σ| = 0 over
  20,000 spins — Patch 4101's cancellation survives intact, still conditional on R-F3.

**Recommendation: Option B**, because it is the only one that converts b from an axiom into a
consequence, and because it supplies a CP spin attribute the corpus **currently lacks
entirely** — the founder's own words at 4107: *"we had not assigned a spin to any CP."*

## 3. The axiom, stated

Option B is not one amendment but a matched set across the three carriers:

| axiom | current | amended |
|---|---|---|
| **A1′** (CP existence) | CPs have type and polarity | CPs additionally carry an **axial-vector attribute** (ZBW spin) |
| **A3′** (Completed Broadcast) | LSP′ = (x, t; Φ, V_i, Q_ij) | LSP′ = (x, t; Φ, V_i, Q_ij, **A_i**) |
| **AP-4** (DI-bit content) | {origin, E, S} | {origin, E, S, **A**} |

All three are required together: a CP must carry it, a GP must broadcast it, a DI-bit must
transport it. Amending any one alone leaves the channel unreadable.

## 4. What else it affects or explains — the founder's second question

### Payoffs beyond W⁰

1. **Spin-½ and Pauli doubling (largest).** THEO-QM-10 currently derives *one* CP per mode.
   Patch 4098 showed the helicity bit gives *two* — 120 × 2 = 240 states, the Pauli doubling
   QM needs. Under Option B that spin is supplied by the axiom rather than assumed, which
   addresses **OPEN-QM-3**'s spin-½ half directly.
2. **THEO-SPIN-1 grounding.** SPIN-1 derives the captured-DP orbital geometry (radius ratio 2,
   frequency ratio 2√2) but has nothing that *is* the spin. A_i supplies the missing referent.
3. **Fermion/boson assignment.** Patch 4092 leaned on a SPIN-1 fermion/boson assignment that is
   currently stipulated. With an explicit CP spin it becomes derivable.
4. **Neutrino helicity (SF-4).** Neutrinos are purely left-handed; an axial channel is the
   natural carrier for a structural account rather than an input.
5. **DP-CAL-1 becomes checkable.** The 4107 calibration (antiparallel sea-DP spins) is
   currently an assumption about an attribute that does not formally exist. Option B gives it
   a referent, so it can be derived or refuted instead of calibrated.

### Costs and risks — stated, not resolved

1. **Magnetism double-counting (main risk).** SF-6 derives **B as the curl of a polar
   displacement** (Patches 4069/4070: *"B is axial because it is the curl of a polar
   displacement"*). Option B puts a *second*, independent axial object in the same packet.
   They are formally distinct — B = ∇×V is derived from the V channel, A is a per-CP attribute
   — but every SF-6 result reading "the axial part of the lattice state" would then have to
   say **which one**. This is not resolved here and is the first thing to settle before
   adoption.
2. **AP-5 saturation budget.** +33% broadcast content per GP per Moment. AP-5 governs what a
   GP does when arriving DI-bits exceed capacity; whether the budget absorbs a fourth channel
   is unchecked.
3. **Patch 4071 adjacency.** 4071 found ≥4 independent internal *directions* are needed for a
   pseudoscalar. A and V are two vectors — but of *different kinds* (axial vs polar), which is
   what makes A·V P-odd. 4071 presumably counted polar directions only. The relationship needs
   stating rather than assuming. (Patch 4110 already found the two agree from the LSP′ side.)
4. **It does not touch F5.** χ₄ still conserves CP exactly, so the CKM phase remains a missing
   mechanism (Patch 4103). **Option B does not move χ₄ toward panel-readiness on its own.**

## 5. Honest status

This is scoping, not a proposal. Nothing is adopted, no verdict moved. What it establishes:
the amendment χ₄ needs is **specific and modest in form** (one axial-vector channel, matched
across A1′/A3′/AP-4), it **pays for itself outside the weak sector** (spin-½, SPIN-1, the
fermion/boson assignment), and it carries **one substantial unresolved risk** (the magnetism
double-count) that should be settled before the axiom question is put formally.

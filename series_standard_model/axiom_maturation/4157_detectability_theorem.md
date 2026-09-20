# THEO-CHIR-1 — When an A_i Configuration Is Empirically Detectable

**Patch:** 4157. **Lane:** EW. **Session:** 234.
**Refutes:** step 2 of my own Patch 4156 proposal.
**Verify:** `series_standard_model/code/4157_traversal_sense_refuted.py`.

---

## 1. The 4156 traversal-sense proposal is refuted

4156 proposed that the W bracelet's 6-cycle carries handedness in its **traversal sense**. A
traversal sense is a physical degree of freedom only if **no symmetry of the configuration reverses
it**. Computed: of the bracelet's symmetry elements that preserve *both* positions and the
alternating polarity of Cor. Wcp, **six reverse the cyclic order** — the reflections m0, m2, m4 and
the C₂′ axes built from them.

**So the two traversal senses are the same physical state**, related by a symmetry the configuration
already has. The static bracelet — ring plus alternating polarity — is **achiral**. My own proposal
of one patch ago does not survive being computed.

## 2. A bug in this patch's first run, recorded rather than silently fixed

The first version of the script omitted **σ_h, the ring plane itself**, and the S^k and C₂′ elements
built from it. That omission **inverted the answer** — it reported 64/64 spin assignments chiral
where the truth is 0/64. Recorded here because this session has twice found claims written one notch
stronger than their checks, and a script whose first run said the opposite of its second is exactly
that failure caught early instead of late.

A second check in the same script fired **INCONSISTENT** on its first run: it compared this patch's
64 symmetry-forced zeros against Patch 4135's "10 of 64 give W = 0". **The check was comparing the
wrong quantities.** W = Σ s_i V_i is a *polar vector*; the pseudoscalar is **B_tot = n·W**. 4135 also
found every V_i lies in the ring plane, so W does too — and with spins along the ring normal,
**B_tot = n·W = 0 for all 64 identically**, whether or not W itself vanishes. The two patches agree.
4135's ten zeros of |W| are a separate and accidental fact.

## 3. THEO-CHIR-1 (proposed)

> **An A_i configuration is empirically detectable as a parity-odd effect if and only if the full
> configuration — positions, charges *and* spins — admits no improper symmetry.**
>
> If some improper g fixes it, every pseudoscalar observable Q obeys Q = det(g)·Q = −Q, hence
> **Q = 0** — no asymmetry at any magnitude. If none does, a pseudoscalar is allowed.

**The content is entirely in the spin assignment.** Positions and charges alone are achiral for both
named structures: the bracelet here, and the nucleon at Patch 4134 (three coplanar charge-bearing
points, whose mirror is their own plane).

### Applied

| structure | result |
|---|---|
| **W bracelet, spins along its own ring normal** | **0/64 chiral.** The pseudoscalar is **symmetry-forced to zero.** |
| W bracelet, spins tilted off the normal | 64/64 chiral — allowed |
| Nucleon ground state | L = 0, internal frame isotropic w.r.t. the spin axis, orientation average kills it (4134) — **P-even** |

## 4. The result worth keeping: the filter table's bracelet row is now derived

**The bracelet alone can never show parity violation.** σ_h fixes any spin along the ring normal —
det(−1) times ẑ → −ẑ gives +ẑ — so the whole spin sector is protected. Handedness therefore cannot
be the bracelet's own; it must be **imported**.

Which is exactly what the founder ruled at 4097 and what the filter table asserts: **the bracelet
reads the *incoming* particle's bit.** Patch 4137 leaned on that table and flagged it as a
CONDITIONAL worker proposal the founder had answered with *"I have no explanation."* **Its bracelet
row now has one** — not a stipulation but a symmetry theorem. The incoming particle supplies the
external axis that tilts the configuration out of σ_h invariance.

That also tightens TODO-4137-FILTERTABLE: one of the table's three rows is derived, two are not.

## 5. What the theorem does not give — and it is the important limitation

**It is a selection rule.** It says when an asymmetry is *allowed*, never how big. It cannot yield
100% V−A, or any magnitude at all. **OPEN-FP-SF-2-CHIR stays open and this does not touch it.**

The founder asked for "the derivations needed to complete the theorem on manifesting axial vector
effects as empirical detections." This completes the *allowed/forbidden* half. The *magnitude* half
is a different argument that nothing in this session has begun.

## 6. PD-008 — the convenient branch, marked

The convenient branch was to press the 4156 traversal picture, which is vivid, which the founder
engaged with, and which I had already put in writing. Computing it killed it in one step. The
recovery — that the refutation *derives* a row of the filter table — is a better result than the
proposal was, but it is worth being clear that it came from the proposal failing, not succeeding.
And §5 is the part that should not be glossed: a selection rule is not the theorem he asked for, it
is half of it.

## 7. Status

**THEO-CHIR-1 proposed**, not yet registered in `theorem-registry.md` — registration waits on a
review pass. TODO-4156-TRAVERSAL **closed as refuted**. No verdict moved. χ₄ provisionally adopted.
**F5 remains the blocker.**

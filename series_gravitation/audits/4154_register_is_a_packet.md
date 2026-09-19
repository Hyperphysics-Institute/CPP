# The GP Register Is a Packet — REGISTERIRREP Closed

**Patch:** 4154. **Lane:** GR/QM. **Session:** 234.
**Closes:** TODO-4153-REGISTERIRREP (founder ruling, `founders_voice/4154_ruling_register_is_a_packet.md`).
**Confirms:** Reading 2 of Patch 4153 §4 — one register **per irrep**.

---

## 1. The picture is right, and the corpus already says so

The GP holds a **structured packet**, one component per irrep of the full point group:

| component | irrep (I_h) | type | dim |
|---|---|---|---|
| Φ = \|SSV\|_abs | A_g | scalar | 1 |
| **V_i** | **T₁_u** | **polar vector** | 3 |
| Q_ij | H_g | symmetric-traceless tensor | 5 |
| **A_i** (amendment, 4120) | **T₁_g** | **axial vector** | 3 |

**The corpus already held more than one thing.** The glossary's Grid Point entry: *"the GP computes,
holds, and per-Moment refreshes **SSV_abs and** [the vector] from Perceive-stage arrivals."* Two
registers, named, since AP-3. So "one register" was never literally one number or one 3-vector; the
4152 ruling's "one vector" meant **one polar vector** — the one stamped on the CP.

**That reading preserves everything 4152 established.** The object stamped on the CP to direct its
displacement is still uniquely `V_i`; b = A·V_i is still well-posed with both factors present at the
CP at the moment of displacement; the retirement of `SSV_net` still stands for the rename reason.
And the amendment survives intact: A_i is a fourth packet component, so the GP broadcasting it
requires no second *polar* vector.

**Why it is not ad hoc.** Patch 4113's argument is exactly this: the original enumeration used the
**rotation** group I, under which polar and axial vectors are the same irrep T₁; under the full group
I_h they are inequivalent, T₁_u and T₁_g. One register per irrep of the full group gives four
components, not three. The amendment **completes** the packet rather than appending to it — which is
what 4120 claimed and what the founder's picture now supplies the storage model for.

## 2. One recommendation, and it is against the founder's own phrasing

> *"the vector stored in the GP register is a vector of scalars, tensors, and vectors"*

**Do not call the packet a vector.** In that sentence "vector" carries two meanings four words
apart — the container (a list of things) and the T₁ component (a physical 3-vector). **That is the
identical failure mode this session has spent twelve patches unwinding:** one token, two referents,
each locally clear, which nobody notices until a construction contracts them. `b = A·V` was that
construction; "a vector of vectors" would be the next one.

**Proposed terms, for the glossary:**

- the **GP state packet** — what the GP holds and refreshes each Moment; the content it imprints on
  outgoing DI-bits and stamps on its resident CP;
- its **components** or **registers** — Φ, V_i, Q_ij, A_i — one per irrep of I_h;
- **`V_i`** reserved for the T₁_u polar vector alone, never for the packet.

`LSP′` already names the *broadcast* of this packet; "GP state packet" names what is *held*. The two
are the same content at different points in the cycle, which is precisely the one-register insight
of 4152 and should be stated that way rather than left implicit.

## 3. One residual, and it is small but real

**Which A enters b = A·V_i — the CP's own, or the GP's A_i register?** They are different objects:
4120 calls A_i *"the CP's ZBW spin"* broadcast, so the GP's A_i register is the **summed** axial
field from arrivals, while the CP carries **its own** A as an A1′ attribute.

For a helicity bit, the CP's **own** spin is what must be contracted — otherwise b measures the
neighbourhood's average handedness rather than the particle's, and the free/confined contrast that
carries F3 (Patches 4134–4135) would not work. But the corpus does not say so, and the same ambiguity
that 4142 raised about V would then apply to A. **Filed as TODO-4154-WHICHA.** It is derivable from
the F3 argument's requirements, so it is mine under PD-008, not a founder question.

## 4. PD-008 — the convenient branch, marked

The convenient branch was to accept the founder's phrasing wholesale — it confirms Reading 2, which
is the reading I said I expected, and it saves the amendment. I have taken the substance and pushed
back on the wording, because "a vector of vectors" would reintroduce, in the very sentence that
resolves it, the defect the session was spent removing. And §3 notes that the ambiguity I raised
about V has an unexamined twin on A, which is not a comfortable thing to point out one patch after
claiming the V side was dissolved.

## 5. Status

TODO-4153-REGISTERIRREP **closed**. The amendment's storage model is consistent. A3G-2 passes. χ₄
provisionally adopted. TODO-4152-UNWIND and the edit pass are unblocked. **F5 remains the blocker.**

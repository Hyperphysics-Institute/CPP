# What Actually Settled the Spin Problem — and a New Constraint the Ruling Creates

**Patch:** 4153. **Lane:** EW/GR/QM. **Session:** 234.
**Answers the founder's question (19 Sep):** does the one-register framing still solve the problem
that precipitated the audit?

---

## 1. Short answer: the physics was settled at 4143, not by the audit

The alarm that started this was Patch 4139: b = A·V looked frame-dependent against the absolute
Nexus frame, ~10²³ over the comagnetometer bound. **It was answered at Patch 4143, and the answer
owes nothing to the SSV_net audit:**

> b does not need to be Lorentz-**invariant**; it needs to be **covariant**. Helicity is
> frame-dependent for a massive particle in any theory. What the comagnetometer forbids is an energy
> term κ(Ŝ · n̂_cosmic) with a **fixed cosmic direction**, and a covariant theory has none.

Nothing in that argument touches how many registers a GP holds or what SSV_net names. **4152 leaves
it completely intact. A3G-2 still passes, on the same footing as every SR-1-dependent CPP result.**

So the founder's read is right: **the concern that launched the rewrite was a misunderstanding of
mine** — I read his "no absolute-frame signature" ruling as "b is invariant," which is stronger and
false, and then spent four patches building machinery to guarantee it.

## 2. What the audit did contribute to the physics — one thing, and it is real but small

Patch 4142 raised a genuine worry: *"the corpus never says which object b contracts A with."* If
`SSV_net` had named two things, **b = A·V would have been ill-posed** — a sign-carrying pseudoscalar
with an ambiguous second factor, which is not a small defect in an axiom.

**The one-register ruling closes that.** There is exactly one vector to contract with, the GP's
register — `V_i`. And the ruling makes the contraction physically natural: the GP stamps the CP with
the register value to direct its displacement, while the CP carries its own axial attribute, so
**both factors of b are present at the CP at the moment of displacement.** b = A·V_i is well-posed
and locally constructible.

That is the audit's entire physics yield: **a worry raised and dissolved.** Everything else it
produced — the retirement, the inventory, the history — is corpus hygiene, which is worth having and
is not physics.

## 3. Does anything change for QM, SR or GR? No — except that QM-1 gets easier

- **QM-1/QM-4/QM-5/QM-6**: the phase identification (φ = the orientation of the GP's vector register,
  FI-QMRG-1) was the contested case. With one register it is unambiguous: φ is the orientation of
  **`V_i`**. **The papers' physics is unchanged; only the token changes.** QM-1's argument was never
  in doubt — my split was what made it look doubtful.
- **SR-1/SR-2**: untouched. SR-2 already wrote `V_i ≡ SSVnet`.
- **GR-1 series**: untouched. One register read two ways — directly for displacement, by its gradient
  for g_ij — is what those papers were already doing.

## 4. The new constraint — and it is on the amendment, not on the papers

**The ruling and the χ₄ amendment are in tension, and this was not visible before today.**

- Founder, 4152: *"each GP only stores **one** vector in its register."*
- A3′ as amended, 4120: *"LSP′ gains a fourth channel **A_i**, an axial vector."* LSP′ is what the GP
  **broadcasts**, and per AP-3 the GP imprints its register on outgoing DI-bits. **To broadcast A_i,
  the GP must hold A_i — a second stored vector.**

Two ways out, and they are not equivalent:

1. **A_i is never GP-stored.** A1′'s matched amendment says *"CPs carry the attribute"*; the CP could
   imprint its own A onto DI-bits at emission without the GP registering it. Then the one-register
   ruling holds as stated — but **A_i is not an LSP′ channel**, and the amendment's central claim
   that it *completes* A3′ over the full point group I_h weakens: it would be a CP/DI-bit attribute,
   not a broadcast irrep.
2. **The GP does hold a second vector**, and the ruling means "one *polar* vector" rather than one
   vector simpliciter. Then A3′'s amendment stands as written — but the ruling needs restating, and
   the natural restatement (one vector **per irrep**, T₁_u and T₁_g being inequivalent under I_h) is
   exactly Patch 4113's argument, which is encouraging rather than damaging.

**Reading 2 is the one I expect to be right**, since 4113's whole point is that T₁_u and T₁_g are
distinct irreps under the full group. But the ruling as given says "one vector," and I am not going
to read a qualifier into the founder's words to save the amendment. **Filed as
TODO-4153-REGISTERIRREP** — a physics question in a physical picture, PD-006(a) founder territory.

## 5. PD-008 — the convenient branch, marked

Overwhelmingly convenient to answer "yes, the framing still solves it" and stop at §1–§3, all of
which is true and all of which reflects well on the work. §4 is the inconvenient part: the ruling I
just spent a patch endorsing creates a fresh problem for the amendment I spent this session
defending, and the reading that saves the amendment requires the founder's words to carry a
qualifier they do not carry. Raised rather than smoothed.

## 6. Status

A3G-2 passes. χ₄ provisionally adopted. **F5 remains the blocker.** TODO-4153-REGISTERIRREP
registered. No verdict moved.

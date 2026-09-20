# The Mixing Loop Does Need A3′ — and What the Loop Then Costs

**Patch:** 4182. **Lane:** EW. **Session:** 234.
**Corrects:** Patch 4181 §1(a). **Reframes:** the retirement question.

---

## 1. The correction: 4181 §1(a) was too quick

I said the GP-must-hold-A argument *"establishes AP-4 (transport), not A3′."* **That was wrong.**
The founder's loop needs the **GP-held register**:

> GP computes a register → stamps outgoing DI-bits → they arrive at the next GP → that GP sums them
> into **its** register → stamps its resident CP → the CP hops carrying it → repeat.

**A DI-bit payload alone cannot close that loop.** Something must *compute and hold* the sum between
arrival and stamping, and that is exactly A3′'s GP state protocol applied to the A channel. **If the
mixing rule is part of the theory, A3′ is required machinery.**

## 2. But the loop's own conditional is where the weight sits

His first clause is *"**if** there is spin mixing."* Taking the loop at face value and asking what it
implies:

**The register is dominated by the environment, overwhelmingly.** The PSR band holds **N ≈ 1.3×10⁹⁰**
GPs (4168). Their axial contributions sum to ~√N = **1.1×10⁴⁵** against the resident CP's single unit.

> **If the CP were stamped with the raw register, the environmental share would be 1 − 10⁻⁴⁵. The
> CP's spin would be completely replaced by its neighbourhood's average in ONE Moment.**

That is excluded by observation at a colossal margin. The measured cap is **ε ≤ 5.4×10⁻⁴⁷** per
Moment (4170, from muon g−2). **Raw stamping exceeds it by ~2×10⁴⁶.**

## 3. So the loop can exist — at one setting only

For the loop to be consistent with spin conservation, the stamp must be weighted
**(1 − 5×10⁻⁴⁷) × the CP's own prior A + 5×10⁻⁴⁷ × the register.**

That is a real architecture, and it is the founder's, and **it is not "mixing" in any ordinary
sense** — it is *the CP's spin is conserved to forty-seven decimal places and the GP's contribution
is a rounding error.* The machinery is required; what it delivers is 10⁻⁴⁷.

## 4. Which reframes the retirement question, and improves it

**The question is no longer "is A3′ useless?"** It is:

> **Is the spin-mixing loop part of the theory?**
>
> - **If yes** — A3′ is **required machinery** and must stay. It supports one effect, bounded to
>   10⁻⁴⁷, and that is a legitimate reason to keep an axiom: theories may contain machinery whose
>   output is small.
> - **If no** — the GP computes an A register that nothing ever reads, and A3′ retires with nothing
>   lost.

**There is no third position.** A register that is computed and never read is idle by definition, so
either the loop exists or the channel does not.

**And this is the founder's call, not mine** — it is a question about what the theory asserts, in a
physical picture. **I withdraw the flat recommendation of 4181 §5**, which said "retire" without
conditioning on this.

## 5. What does not change

Everything in 4181 §2 (the six retirement requirements) stands **if** retirement is chosen, and
everything in 4179 stands regardless: **A_i is still not independent of ∇ × V_i in any part matter
can excite**, so the loop, if kept, transports axial information that the polar channel's curl
already determines. **Keeping A3′ for the loop is keeping it for the loop — not for the
completeness argument, which 4178 and 4179 refuted.**

## 6. PD-008 — the convenient branch, marked

I had a recommendation on the table and the founder pushed back on its weakest step. **The
convenient branch was to defend the recommendation** — and the defence was available: the mixing
rule is bounded to 10⁻⁴⁷, so "required machinery for a 10⁻⁴⁷ effect" can be made to sound like no
requirement at all. **It is a requirement.** Machinery that supports a small effect is still
machinery, and calling it useless would be a rhetorical move rather than an argument.

## 7. Status

4181 §1(a) **corrected**; 4181 §5's recommendation **withdrawn and replaced by the conditional in §4**.
Registered as **TODO-4182-LOOP**. No verdict moved. **F5 remains the blocker.**

# The Hop Gate — the Founder's Proposal Written Down, and Its Symmetry Signature

**Patch:** 4193. **Lane:** EW. **Session:** 236.
**Founder verbatim:** `founders_voice/4193_the_gp_to_gp_relationship_as_the_gate.md`.
**Verify:** `series_standard_model/code/4193_hop_selector_symmetries.py`.
**Corrects:** Patch 4155 §2 (*"there is no P-odd, T-even force available"* — true of forces, and CPP
does not move CPs by forces) and §3 (the tie-break *by b*). **Status: a candidate amendment, written
down and classified. NOT adopted, NOT tested against the filters. No verdict moved.**

---

## 1. "Does the CP only affect the GP that it is on?"

**Directly, yes.** A CP writes its attributes into the register of the one GP it occupies, and
nowhere else. Everything further is GP-to-GP: under the founder's 4184 ruling every GP receives,
integrates and rebroadcasts, so that content then travels outward by relay, thinning as a/r. **4192
summed the relayed part.** If the founder's intent is stronger — that a CP's axial content is *not*
relayed onward at all — then there is no axial field at a distance, 4192's sum is moot, and so is any
influence of the *environment's* chirality. Stated here so he can say which.

## 2. The proposal, written as a rule

The founder: edges are not actors; an edge is a **relationship between two GPs**; the amendment is
that **the A_i in the register is compared with the GP the CP is moving toward**. The existing rule
(c03) scores each of the twelve neighbour GPs by **e_i · V** and takes the largest. The comparison he
describes is **e_i · A** — how nearly the candidate GP lies along the register's axial vector. One
addition is mine, and is forced by filter F4/F9 (CP conserved; antiparticle = opposite polarity): the
comparison carries the CP's **polarity q**, so one polarity favours the GP *along* A and the other the
GP *against* it.

> **Candidate "hop gate":** among neighbour GPs, the score is e_i · V; the term **q (e_i · A)** enters
> either only when e_i · V does not decide (**tie-only**), or always, with some weight (**always-on**).

## 3. What kind of term it is — rows verbatim from the script (D-11)

```
term in the hop score                   C     P     T     CP    CPT
e.V            (existing rule)          even  even  even  even  even
e.(V x A)      (Lorentz-like)           even  even  ODD   even  ODD 
e.A                                     even  ODD   even  ODD   ODD 
q e.A          (founder gate, 4193)     ODD   ODD   even  even  even
(A.V) e.A      (4155 bA)                even  even  even  even  even
(A.V) e.V      (b as a weight)          even  ODD   even  ODD   ODD 
```

**q e·A is C-odd, P-odd, T-even, CP-even, CPT-even — the weak interaction's pattern, and it is the
only row that has it.**

**Why 4155 missed it.** 4155 §2 looked for a *force* — a polar, T-**even** vector — and correctly found
none: bA is T-odd. But 4156 §1 quotes the founder: *"no forces act on a CP to move it… movement is
purely rule-based."* **The rule delivers a hop, and a hop is a displacement per Moment: T-odd.** "Hop
toward A" pairs two T-odd objects and is T-even. The founder's insistence that the effect be a
*displacement* is what opens the door; in a force picture the door is shut.

**And 4155 §3's own tie-break does not work.** Breaking a tie *by b* must be one of the last two rows:
(A·V) e·A is **parity-EVEN** — it violates nothing — and (A·V) e·V cannot break a tie in e·V at all.
TODO-4155-EDGETIE is amended accordingly.

**Which A.** The founder says the register's A_i; 4192 §4 said the CP's own. **Numerically these are
the same object:** the resident CP dominates its GP's register by 10⁵⁰ against one neighbour (4184)
and still by ~10³⁷ beside a magnet (4192). And because the gate only **reads** the register to choose
a hop and never **stamps** it back into the CP, nothing accumulates — **4192's exclusion of mixing
does not touch it.** The cost: the *environment's* share in directing the hop is 10⁻³⁷ or less. It is
the CP's own handedness, held at its GP, that does the directing.

## 4. What could kill it — named before any computing

1. **Self-propulsion.** A free CP with V = 0 ties on all twelve neighbours, so the gate alone moves
   it along ±A. If that survives averaging over the ZBW cycle, a polarised particle at rest would
   drift — momentum is not conserved and the candidate is dead. **First test.**
2. **F2 — EM must stay P-even** to ~10⁻¹⁰. An always-on weight puts parity violation in every atom;
   tie-only may escape because bound motion rarely ties. Must be shown, not hoped.
3. **F4 — magnitude.** Does it give helicity polarisation −v/c, or only the right sign?
4. **F7 — no parameter.** Always-on needs a weight; tie-only does not. Tie-only is tested first.

## 5. PD-008

Not my convenient branch: this keeps A in the register doing real work, which I leaned against at
4191. It is, however, a result I *like*, which is its own hazard — the table is three lines of sign
arithmetic and should be re-derived by the next window before anything leans on it, in particular the
assignment **hop = T-odd**, on which everything in §3 rests.

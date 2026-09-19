# What A_i Acts Upon, and Where the Chiral Motive Force Is

**Patch:** 4155. **Lane:** EW. **Session:** 234.
**Answers the founder's questions (19 Sep):** what does the axial vector act upon; how does it show
up empirically; does it produce displacement if misoriented; what is the motive force for the
chiral effects. Plus a naming recommendation for the GP's held state.

---

## 1. What an axial vector can couple to — the complete short list

An axial vector has only three ways to enter a scalar or a force, and each has a fixed
parity/time signature. Everything A_i does must be one of them.

| construction | with | result | P | T | what it is |
|---|---|---|---|---|---|
| **A₁ · A₂** | another axial | scalar | + | + | **spin–spin alignment.** Ordinary magnetism. |
| **v × A** | a polar velocity | polar force | − | + | **Lorentz-type deflection.** A real force. |
| **A · V** | a polar vector | **pseudoscalar** | − | + | **the helicity bit b.** Chirality. |

That is the whole list. So the answers, in order:

**Does it act on other axial vectors?** Yes — A₁·A₂, and that is already in the corpus: Patch 4125
identified it as ordinary long-range magnetic dipole–dipole. **Nothing new; it is magnetism.**

**Does it produce displacement?** Yes — through **v × A**, a transverse deflection of a CP moving
through an A-field. That is a genuine motive force and it is **exactly what TEST-A3G-2 bounds**
(spin-dependent fifth force). Patch 4143 concluded A3G-2 passes, so the deflection exists in
principle and is unobserved in practice.

## 2. The hard part: where is the chiral motive force? Probably nowhere — and that is correct

The founder's instinct is that a parity effect needs a motive force behind it. **I think the
instinct is right about the need and wrong about the form**, and the corpus already says so.

Try to build a **force** from the chirality. The only polar object available from b and A is

  **F ∝ (A·V) A = b A**

— which is polar (pseudoscalar × axial), so it is a legal force under P. But under **T**: b is
T-even (F6) and A is T-odd, so **F is T-ODD.** A T-odd term in a fundamental force law is not a
small thing; it is CP violation in the substrate's kinematics.

Every other attempt fails on dimensional-analysis-of-parity grounds. b(A × V) is P-even, so not a
force at all. **There is no P-odd, T-even force available from these ingredients.**

**The resolution is that parity violation is not a force, and never was.** The weak interaction's
chirality shows up as **rate and selection asymmetries** — which decay channel, which final-state
helicity, how often — not as a push. Cobalt-60 does not feel a sideways force; its decay *products*
come out asymmetrically. This is exactly what the corpus's **B3** already asserts: parity violation
appears in observables *iff* the **response** R depends on b **linearly**. A response, not a force.

So: **there is no chiral motive force, and there should not be one.** Asking for one is asking
parity violation to be something it has never been in any theory.

## 3. Where b can act, concretely — a proposal

If b biases a selection rather than pushing, the corpus has one obvious place for it: **the 12-edge
selection rule.** c03 states it plainly —

> *"The 12-edge selection rule chooses the lattice edge i\* that maximizes **e_i · V**."*

**Ties are the opening.** When two of the twelve edges are degenerate in e_i·V — which happens
whenever V is symmetrically placed relative to the icosahedral shell — the rule as written does not
say which is taken. A degenerate pair related by reflection is precisely a left/right choice, and
**b is a sign. A tie-break by b is a parity-odd selection with no force anywhere in it.**

This has the right shape on every count: it is a **selection**, so it satisfies B3 without a T-odd
force; it is **local**, needing only the CP's own A and its GP's V; it costs **nothing when V is
generic**, since ties are measure-zero in a continuum but common on a lattice with an icosahedral
coordination shell; and it **vanishes for a confined quark** whose ⟨b⟩ = 0 (Patches 4134–4135),
which is the free/confined contrast F3 needs, arising here from the mechanism rather than being
imposed on it.

**This is my proposal, not corpus.** It needs: the degeneracy census on the 12-shell (how often do
ties occur, and are the tied pairs reflection-related?), and a check that the resulting bias
reproduces the weak sector's magnitude rather than merely its sign. Filed as **TODO-4155-EDGETIE**.

## 4. How A_i shows up empirically — and the uncomfortable answer

| channel | signature | status |
|---|---|---|
| A₁·A₂ | magnetic dipole–dipole | **already known.** Magnetism. |
| v × A | spin-dependent force | **bounded, unobserved** (A3G-2, passes) |
| A·V = b | weak parity violation | **already known.** V−A. |
| A₁·A₂ vacuum sum | vacuum magnetisation | **bounded, no fire** (A3G-1) |

**A_i currently has no independent empirical signature.** Everything it does is either magnetism we
already had or weak chirality we already had. It is a channel that explains the known and predicts
nothing new yet — which is a real weakness, not a neutral fact, and worth saying plainly after a
session spent defending it. The unrun suite items **A3G-4/5/6** are where a distinctive prediction
would have to come from, and they remain unrun.

## 5. Naming the GP's held state

The founder's candidates were *SSV Group*, *SSV parameters*, *SSV elements*; he had been saying
"SSV vector" or "GP vector".

**Reject "Group"** — CPP is saturated with genuine group theory (I_h, the binary icosahedral group
2I, SU(3) from the 600-cell). "SSV Group" would read as a symmetry group to every physicist who
opens the paper. This is the same one-token-two-referents trap in a worse neighbourhood.

**Reject "parameters"** — the programme's central claim is **zero free parameters**. A term called
"the SSV parameters" invites exactly the misreading the programme most needs to avoid.

**"Elements" is usable but second-best** — "element" is also group-element and lattice-element.

**Recommended: no new term at all.** The corpus already has one. **LSP′ — the Lattice State
Packet** — names this content; Patch 4152 established that what the GP *holds* and what it
*broadcasts* are the same content at two points in the cycle. So:

- **the GP's LSP′ register** (or **state register**) — what the GP computes, holds, refreshes,
  imprints on DI-bits, stamps on its CP;
- **its components**: Φ, V_i, Q_ij, A_i — one per irrep of I_h.

Coining a fifth name for a thing that already has one is how this session's twelve-patch detour
started. If a short informal term is wanted in prose, **"the GP's state packet"** reads naturally
and collides with nothing.

## 6. PD-008 — the convenient branch, marked

§2 declines the founder's framing: he asked what the chiral motive force is, and the answer is that
there is none and should be none. §4 is the uncomfortable one — having spent a session defending the
amendment, the honest summary is that A_i has no independent empirical signature yet. Both were
easier to leave unsaid, and §3's tie-break proposal (which is mine and is speculative) would have
read better without §4 beside it.

## 7. Status

No verdict moved. χ₄ provisionally adopted. **F5 remains the blocker**; A3G-4/5/6 unrun.

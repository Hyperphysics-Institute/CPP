# R2 Hardening — The Single-Response Structure Is Corpus-Derived, Not a Cartoon

**Patch:** 2007 (21 June 2026) · **Window:** 2000-band · **Work item:** OPEN-COSMO-DM-2 residual R2
**Status of result:** **R2 hardened. The 2002 PASS was "conditional on the single-oscillator structure,"
which 2002 flagged as a physical cartoon. This patch shows that the load-bearing half of that structure —
that B is a *functional of the polarization*, not an independent magnetic field with its own inertia — is
already entailed by the DERIVED field-strength math (c06 line 91, EW-5), not just the cartoon. The
residual narrows from "an un-derived single-oscillator picture" to ONE concrete substrate question: the
on-site-vs-inter-site stiffness question, posed sharply to the review panel (CONV-001 package, this patch).**
**Companion:** `R2-Z0-VIRIAL-CLOSURE.md` (2002), `dp_sea_mu_eps_symmetry.md` (0740).
**Discipline:** worker patch; owned path `mu_eps_closure/`; no shared-registry/c06/EW-5 edit.

---

## 1. What 2002 left conditional, and what the corpus actually contains

2002 proved: *if* the DP magnetic and electric responses are the two halves of one oscillator
(single-response), then the harmonic virial ⟨KE⟩=⟨PE⟩ makes the stiffness C cancel in Z₀=√(μ₀/ε₀)
(geometric → A=0 → PASS), while it survives in μ₀ε₀=1/c² (c varies = gravity). The alternative
(independent magnetic inertia, Reading B) gives Z₀∝C → A~O(1) → FAIL by ~6 orders. 2002 flagged the
single-response structure as "a physical cartoon, NOT in the corpus as a derivation," and that was the
honest status at the time.

On a closer reading of the EM sector, that status is too pessimistic. The b-field note's own corpus-status
line says: *"the mechanical picture is NOT in the corpus; only the curl/field-strength math is (EW-5,
c06)."* The **mechanical narration** (poles swinging) is the cartoon — but the **field-strength math** is
derived. And that derived math is exactly what R2 needs:

- **c06 (line 91, derived text):** *"The orthogonal magnetic component arises from the curl of the
  propagating SSV pattern."*
- **EW-5:** the field-strength tensor `F = ∂^μA^ν − ∂^νA^μ + …` emerges from SS-Vector curls.
- **c06 (line 185, the owed computation, with the prediction already stated):** Z₀=√(μ₀/ε₀) in lattice
  units is predicted to be *"a pure 600-cell geometric constant, independent of the SSV-variable stiffness
  C (because the magnetic component is the curl of the polarization pattern over the fixed, eternal GP
  network)."*

## 2. The hardening: derived math excludes the "independent magnetic field" horn

The structural content of "B = curl of the propagating polarization over the fixed GP network" is:

> **B is a *functional* of the one polarization (displacement) field, B = ∇×P, evaluated by a discrete
> curl over the fixed/eternal GP lattice.** There is no independent magnetic field carrying its own
> coordinate.

This is corpus-derived (c06/EW-5 field-strength math), not cartoon. It **excludes the strong form of
Reading B** — the scenario where the magnetic response is a genuinely independent oscillator/field with
its own degree of freedom. There is only the DP displacement field; B is a derived functional of it. So
the part of R2 that worried "maybe B is an independent thing with independent inertia" is closed by
existing derivation.

Combined with 2002: one polarization field, B a curl-functional of it ⇒ the magnetic and electric field
energies are two functionals of the *same* displacement field ⇒ the virial-type cancellation of 2002
applies ⇒ Z₀ geometric. The "cartoon" caveat on R2 is substantially discharged.

## 3. The honest residual — what is NOT yet closed (one concrete substrate question)

I will not overclaim a full closure. "B = ∇×P" excludes an independent magnetic *field*, but it does not
*by itself* prove that the magnetic energy carries the *same* stiffness-dependence as the electric energy.
The electric energy is on-site (the local polarization, governed by the DP on-site stiffness C, → ε₀∝nq²/C);
the magnetic energy is the *gradient/curl* of the displacement (→ governed by how the displacement is
coupled between neighboring GPs). The decidable residual:

> **Is the gradient/propagation stiffness that governs the magnetic (curl) energy the SAME C (or rigidly
> locked to it) as the on-site polarization stiffness that governs the electric energy — or is it an
> independent inter-site coupling K that could carry a different SSV-dependence?**
> - Same / locked → Z₀ geometric → A=0 → PASS (unconditional).
> - Independent K, SSV-split from C → Z₀∝(C/K)^p → A≠0 → FAIL.

The "fixed, eternal GP network" (GPs SSV-independent, Brick #2) is strong evidence the *geometric* curl
factor is C-free, which is why c06 line 185 predicts a geometric Z₀. But the *inter-site coupling
stiffness'* SSV-dependence has not been computed. That computation — the c06 owed "express μ₀, ε₀ in terms
of C and c" — is the concrete thing that converts this to an unconditional PASS or a kill.

## 4. R2 status after this patch

- **Was (2002):** PASS, conditional on an un-derived single-oscillator cartoon.
- **Now (2007):** PASS, with the single-response structure (B=∇×P, no independent magnetic field) shown to
  be corpus-derived (c06/EW-5). Residual narrowed to ONE concrete substrate question (on-site C vs
  inter-site K, §3), with the fixed/eternal GP network favoring the geometric (PASS) outcome.
- **Clean-kill exposure:** still formally open via the §3 residual, but narrowed and pointed toward PASS.
  Dispatched to the panel (this patch) and to the c06 owed computation.

## 5. Panel dispatch (CONV-001, this patch)

The §3 residual is now crisp and decidable, so it is dispatched to the default panel (ChatGPT / Grok /
Copilot) as a single-block package: `mu_eps_closure/R2_panel_dispatch.md`. The ask is adversarial: (a) does
"B = ∇×P over the fixed GP network" genuinely exclude an independent magnetic inertia, as argued in §2? and
(b) does the on-site/inter-site stiffness structure force Z₀ to be C-independent (PASS) or admit a C-split
(FAIL)? Reviewers are asked to attack the PASS, not confirm it.

## 6. Proposed cross-ref — FOR THE INTEGRATOR'S BATCHED PATCH (not edited here)

> **c06 owed-computation item (line 185):** annotate that R2 (Patch 2007) has shown the single-response
> structure (B=∇×P) is already entailed by the line-91 field-strength math, narrowing the owed Z₀(C,c)
> computation's open part to the on-site-C-vs-inter-site-K stiffness question; the prediction (geometric
> Z₀) stands and is the PASS criterion.

NO THEO (hardening of a conditional result + dispatch; no new axiom/term/counted prediction).

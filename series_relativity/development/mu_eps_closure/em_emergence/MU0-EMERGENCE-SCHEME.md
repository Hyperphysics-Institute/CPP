> **⚠ SUPERSEDED / RETRACTED by Patch 2021.** The proposed closure below does NOT survive the Q3 rigor upgrade. Dropping the μ₀∝α_B analogy and using Z₀=1/(ε₀c)=C/c with the corpus's grounded c∝√C gives Z₀∝√C — a ~6-order FAIL. The c∝C this argument needs was circular (derived from μ₀∝α_B). R2 is OPEN, leaning FAIL. See `Q3-Q2-HONEST-RESULT.md` (2021). The text below is kept for the record.

# OPEN-SR-9 Gate — The μ₀-Emergence Scheme From c06: A PROPOSED Closure (Under Adversarial Review)

**Patch:** 2017 (22 June 2026) · **Window:** 2000-band · **Work item:** OPEN-SR-9 / R2
**Status of result:** **PROPOSED closure — under adversarial (round-3) review, NOT an accepted result.** We argue the gate that left 2016 a conditional PASS *closes* in favour of PASS; whether the argument actually holds is exactly what the round-3 panel is being asked to decide. Every "PASS / closed" statement below is the PROPOSITION UNDER TEST, not an established fact. The
load-bearing assumption — that μ₀ emerges from the substrate as a *compliance* (μ₀∝1/C, giving geometric
Z₀) rather than a *kinetic inductance* (μ₀∝m∝C, giving Z₀∝C, FAIL) — is settled by two independent
c06-grounded arguments. The deepest honest statement: **R2 is no longer an independent falsifier — the FAIL
scheme is exactly the one that would also kill CPP's VSL horizon mechanism, so R2 passes iff VSL holds; they
are locked by one shared μ₀∝1/C scaling.** Remaining: a full dynamical derivation of μ₀ from the DI-bit
reconstruction (a rigor upgrade, not a gate) + round-3 panel review.
**Verify:** `scripts/2017_mu0_scheme.py`. **Anchors:** c06 lines 91, 103–104, 110.

---

## 1. The gate

2016 gave geometric Z₀ (PASS) + varying c (VSL) **conditional on the symmetric scheme** μ₀∝α_B (∝1/C). The
alternative — kinetic inductance, μ₀∝m∝C — gives Z₀∝C (FAIL). The three candidate schemes and their
signatures (script):

| scheme | μ₀(C) | c varies? (VSL) | Z₀ geometric? (R2) |
|---|---|---|---|
| **S1** configurational/compliance | **∝ 1/C** | **yes** | **yes — PASS** |
| S2 kinetic inductance | ∝ C | **no** (c fixed) | no — FAIL |
| S0 flat | const | yes | no — FAIL |

(ε₀∝1/C throughout, the solid radial-compliance result.) The gate = which scheme c06 forces.

## 2. Argument 1 — VSL-consistency excludes the kinetic FAIL scheme (S2)

CPP independently commits to the VSL horizon mechanism (EU-1 shipped: high early c_eff solves causal
contact without de Sitter). VSL requires c = 1/√(μ₀ε₀) to **vary** with the substrate stiffness. With ε₀∝1/C
fixed, the kinetic scheme S2 (μ₀∝C) gives μ₀ε₀ = const ⇒ **c fixed ⇒ no VSL**. So CPP's standing VSL
commitment **excludes S2** — the only scheme that would make Z₀ carry C. The scheme that would falsify R2 is
the same scheme that would kill the horizon mechanism CPP already relies on. (This argument alone leaves S0
vs S1 open — both give VSL; S0 still FAILs R2 — so Argument 2 is needed.)

## 3. Argument 2 — c06 forces the compliance scheme (S1 over S0)

Two corpus facts pick S1 (μ₀∝1/C) over S0 (μ₀ flat):
- **Reconstruction, not transport (c06 lines 103–104, 110; "frozen" config, lines 87/91).** The photon is
  *"not a discrete object in transit"*; it is *"reconstructed at each Absolute Moment by the vector
  summation of DI-bit strings,"* the displacement configuration *"frozen"* and advanced one shell per Moment.
  There is **no inertial transport of massive carriers** — so μ₀ is **not** a kinetic inductance (∝m). It is
  the **compliance** of the reconstructed displacement configuration: how much the Coulomb-bound poles
  displace (radially for E, in curl for B) per unit field. A compliance scales as 1/C.
- **"μ₀, ε₀ share one DP stiffness" (c06 line 91, explicit).** B is the curl and E the radial part of the
  *same* Coulomb-bound pole displacement, so both constants are functions of the *same* stiffness C in the
  *same* way: μ₀∝1/C and ε₀∝1/C. S0 (μ₀ independent of C) would mean μ₀ does **not** share the stiffness —
  contradicting line 91. So line 91 excludes S0.

Both arguments converge on **S1: μ₀∝1/C ⇒ Z₀ = √((1/C)/(1/C)) geometric ⇒ R2 PASS**, with c∝C (VSL ✓).

## 4. The lock (the deepest honest statement)

The kinetic-inductance FAIL scheme (S2) is excluded *twice over*: by VSL-consistency (§2) and by c06's
reconstruction mechanism (§3). And the scheme that survives is the *same* μ₀∝1/C that powers VSL. Therefore:

> **R2 is not an independent falsifier.** The impedance-drift kill requires μ₀∝C (S2); that scaling makes c
> constant, which destroys the VSL horizon mechanism. So R2 can only kill CPP by *also* killing VSL — and
> conversely, if VSL stands (as EU-1 commits), μ₀∝1/C and Z₀ is geometric and **R2 PASSES**. The falsifier
> and the mechanism are welded by one scaling.

## 5. Honest status and what remains

- **Gate: PROPOSED closed (pending round-3 panel review)** at the level of c06's stated mechanism (reconstruction + line 91) and CPP's VSL
  commitment. 2016's conditional-PASS → **proposed PASS** (pending review).
- **R2 overall:** from "open ~6-order independent falsifier" → "**PASS**, locked to VSL; the only way to
  fail it is to abandon the VSL horizon mechanism, which is independently motivated and shipped (EU-1)."
- **Not overclaimed — the rigor upgrade that remains:** §3's first bullet reads μ₀ off c06's *stated*
  reconstruction mechanism rather than deriving it from the DI-bit vector-summation *dynamics* explicitly;
  and line 91 is a corpus assertion this leans on. A from-scratch derivation of μ₀ from the reconstruction
  dynamics would convert "PASS at the mechanism level" to "PASS from first principles." That is the residual
  depth of OPEN-SR-9 — a rigor upgrade, **not** a gate, and the natural content of SF-6.
- **Recommended next:** round-3 adversarial panel review of this lock (the VSL-consistency lever + the
  reconstruction reading), since it is now a strong claim that should be attacked before the corpus leans on
  it.

## 6. Proposed (integrator) — NOT edited here
A one-line cross-ref in c06 (Open Problems / the line-91 note) that the μ₀-emergence scheme is fixed to the
compliance form (μ₀∝1/C) by the reconstruction mechanism + VSL-consistency (Patch 2017), closing the R2
impedance question to PASS-conditional-on-VSL. Deferred to the integrator (c06 is high-traffic).

NO THEO (conditional derivation + consistency lock; the fixed-ω₀ and VSL inputs are existing c02/EU-1).

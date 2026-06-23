# Review Package v1.0 — VTD-1 + R2-via-Lorentz (conditional-PASS), Patch 2039

**Programme:** Conscious Point Physics (CPP). **Window:** 2000-band. **Status of artifact:** conditional
verdict-move, frontier-tracked, **NO THEO** (no axiom/term/counted-prediction asserted). This package is the
immutable review request; responses aggregate in `reviews-VTD1-R2.md`.

---

## §0 — The ask (read first)

You are asked to adversarially review **two coupled conditional claims** and report whether each is (a) sound
as stated, (b) sound but mis-stated in strength, or (c) unsound. **Review from this document alone — fetch
nothing.** Be hostile where §4 directs you; we are trying to break these, not bless them. A FAIL is a useful
outcome. Do not infer unstated charity; if a step is "read off" rather than "derived," say so.

## §1 — Context (the thread, honestly)

The dark-matter arc (CONJ-COSMO-1) requires one CPP mechanism to make the uniform Dipole Sea inert (Λ
suppressed) while swirls gravitate (DM). The shared foundation is op:einstein (c08): gravity must source from
the SSV **excess** Δ|SSV|, not absolute |SSV|. A standing falsifier of that picture is **R2**: under an
SSV/density perturbation, does the fine-structure constant α drift? (Z₀ = √(μ₀/ε₀) = C/c_photon; α ∝ Z₀ at
fixed e, ℏ. If Z₀ moves with the local stiffness C, α drifts — a ~6-order local-position-invariance
violation.)

History of R2 (disclosed, no spin): **2016** PASS by analogy (circular, retracted). **2021** FAIL, concluding
Z₀ ∝ √C. **2024** the 2021 FAIL was found to use the DP-lattice **phonon** speed √(C/m)·a for the **photon**;
c06 says the photon advances one PSR/budget shell per Absolute Moment and Patch 2011 established photon ≠
phonon, so the FAIL's positive claim (c ∝ √C) used the wrong mode ⇒ R2 reopened to **OPEN**. **2025** a
grounded route to PASS was proposed (this package, claim P2). **2037/2038** VTD-1 (claim P1) was resolved and
founder-delegated-confirmed at SR-1 strength.

## §2 — The two claims under test

### P1 — VTD-1: the velocity time-dilation budget split is the quadrature (f_eff), not linear.

SR-1's displacement budget: total CP 4-displacement per Absolute Moment is bounded by l_P. A mass at speed v
spends a spatial bulk displacement v·t_P; internal processes (clocks) get the remainder. **Claim:** the
remainder is the **orthogonal/Pythagorean** part √(l_P²−(v t_P)²) = l_P/γ, giving internal clock rate exactly
1/γ ⇒ exact Lorentz γ. Equivalently the *consumed* fraction is f_eff = 1 − 1/γ.

**Grounding offered (not pure geometry):** SR-1's Appendix H (Geometric Insufficiency Theorem, A− externally
reviewed) proves no purely geometric model yields exact γ alone, and characterises **f_eff = 1 − 1/γ as the
unique consistent consumed fraction**, supplied by the energy-momentum bridge (ΔSSV ≡ relativistic KE
density). The quadrature is the *geometric face* of that already-validated f_eff. The competing **linear**
reading (consumed = v/c, internal = 1 − v/c) gives γ = 1/(1−v/c) — a different, **falsified** factor — so it
is excluded, and f_eff is unique (demand internal = 1/γ ⇒ consumed = 1 − 1/γ, no free parameter). See §3
code. **Asserted strength:** PASS *at SR-1 strength* — i.e. VTD-1 inherits exactly the status of SR-1's
energy-momentum bridge (a validated physical identification, App.-H-acknowledged as an identification, not a
geometric theorem). **Explicitly NOT asserted:** that the PCD/Absolute-Moment cycle *literally* allocates
displacement into orthogonal subspaces as a primitive fact (literal-vs-effective is carved out as a non-gating
refinement).

### P2 — R2-via-Lorentz: Z₀ geometric ⇒ R2 conditional-PASS, on P1 + medium-universality.

Steps: (a) c_light = c_photon (budget), not the phonon — corpus-confirmed (c06 line 89; Patch 2011). (b) For a
**moving** atom, α is a Lorentz scalar, hence invariant (Ives–Stilwell), **given P1** (exact Lorentz). The
moving atom sits in a medium whose local C is changed by the velocity strain; for α = e²/(4πε₀ℏ c_photon) with
ε₀ ∝ 1/C to stay invariant, the photon speed must compensate ⇒ **c_photon ∝ C** (slope +1.000), *read off*
α-invariance, not assumed. (c) **Universality transfer:** *if* c_photon(C) is a single-valued,
rotationally-symmetric property of the **local medium state** — the same function whether the SSV change was
velocity-sourced (anisotropic) or gravity-sourced (isotropic) — then c_photon ∝ C holds for gravity too ⇒
Z₀ = C/c_photon = constant ⇒ geometric ⇒ **k_α = d ln Z₀/d ln C = 0 ⇒ R2 PASS**. **Asserted strength:**
conditional-PASS on (i) P1 [now cleared at SR-1 strength] and (ii) **medium-universality** [grounded by the
scalar-SSV universality/locality/completeness arc, but the load-bearing assumption]. A *deeper* route —
deriving c_photon ∝ C from a first-principles lattice-EM action rather than reading it off Lorentz — is **NOT
claimed here** and remains open as **OPEN-SR-9** (a naive lattice action gives Z₀ ∝ C, an honest 2011
negative).

## §3 — Verify code (embedded in full; run it)

```python
# 2037 — quadrature == f_eff == energy-bridge == 1/gamma (exact); linear != 1/gamma
import numpy as np
for b in [0.1,0.3,0.6,0.8,0.9,0.99]:
    g=1/np.sqrt(1-b**2)
    linear=1-b; quad=np.sqrt(1-b**2); rem_feff=1-(1-1/g); bridge=1/(1+(g-1))
    print(f"v/c={b:.2f} 1/g={1/g:.6f} linear={linear:.6f} quad={quad:.6f} 1-f_eff={rem_feff:.6f} bridge={bridge:.6f}")
# Across v: quad == 1-f_eff == bridge == 1/g to 1e-12; linear (1-v/c) != 1/g.
```

```python
# 2038 — linear EXCLUDED, f_eff UNIQUE, against SR-1's externally-validated exact gamma
import numpy as np
for b in [0.1,0.3,0.6,0.8,0.9,0.99]:
    g=1/np.sqrt(1-b**2); need=1/g; linear=1-b; quad=np.sqrt(1-b**2)
    print(f"v/c={b:.2f} REQUIRED(1/g)={need:.5f} LINEAR={linear:.5f} QUAD/f_eff={quad:.5f}")
# LINEAR reproduces validated gamma? NO (gives 1/(1-v/c)). QUAD/f_eff? YES.
# Uniqueness: internal = 1 - f AND validated internal = 1/g  =>  f = 1 - 1/g = f_eff. No free parameter.
```

## §4 — Scrutiny directives (be hostile HERE)

1. **Condition (ii) medium-universality — the softest joint. Attack it.** P2(c) transfers c_photon ∝ C from
   the velocity frame (where α-invariance is *guaranteed* by Lorentz-scalar status, given P1) to the gravity
   frame (where there is *no* such protection). The velocity strain is **anisotropic** (a directional bulk
   displacement); a gravitational SSV gradient is **isotropic**. **Question:** what forbids c_photon from
   depending on the *anisotropy* or the *sourcing history* of the strain, not only on the scalar local C? If
   c_photon(C) is allowed to differ between anisotropic-velocity and isotropic-gravity strains at the same C,
   the transfer fails and R2 is not PASS. Is universality *derived*, or *assumed because it gives the wanted
   answer*? State which, and what would be required to derive it.
2. **The "read-off vs derive" gap (potential circularity).** P2(b) uses α-invariance to *extract* c_photon ∝
   C; P2(c) then uses c_photon ∝ C to conclude α is invariant under gravity. **Question:** is this a
   legitimate two-frame argument (invariance in the *velocity* frame is an independent experimental input;
   it is *transferred*, not reused, via universality) — or does it smuggle the gravitational conclusion
   through the universality step? Pin down exactly where the non-trivial physical content enters, and whether
   it is the universality assumption doing all the work.
3. **VTD-1 strength ceiling.** P1 is asserted only "at SR-1 strength," inheriting SR-1's energy-momentum
   bridge (an *identification*, not a geometric theorem, per App. H). **Question:** is "at SR-1 strength"
   sufficient to clear R2's condition (i), or does R2 specifically *need* the literal substrate derivation
   (the carved-out OPEN-SR-9 route)? I.e., does the effective γ(v) suffice for the impedance argument, or does
   the impedance result secretly require the literal orthogonal-allocation mechanism?
4. **The linear-exclusion logic.** P1 excludes the linear reading by appeal to SR-1's *validated* γ.
   **Question:** is that a fair exclusion (the linear reading makes a falsified empirical prediction), or does
   it merely assume the conclusion (that the budget split must reproduce SR γ)? Is there any third budget
   reading — neither linear nor quadrature — consistent with exact γ?

## §5 — Response format (per reviewer)

For **each** of P1, P2: verdict ∈ {SOUND / MIS-STATED-STRENGTH / UNSOUND}; the single strongest objection;
whether §4(1) universality is derivable or must be assumed; and the minimal additional work that would move
the claim from conditional-PASS to unconditional. Then an overall: does this package overclaim anywhere
relative to its own stated strengths? End with the one experiment or computation that would most cheaply
falsify P2.

## §6 — Reviewer steer (read your own row)

- **ChatGPT (rigor + hostile pass):** you are the designated breaker this round. Prioritise §4(1) and §4(2);
  do not accept "universality" without a derivation or an explicit "assumed." Press the anisotropic-vs-
  isotropic strain disanalogy hardest.
- **Grok:** independent-physics sanity. Is the photon≠phonon identification (P2a) actually load-bearing and
  correct? Is reading c_photon ∝ C off α-invariance a standard move or a sleight? Bring an outside-CPP
  analogue if one exists.
- **Copilot:** consistency/audit. Check the §3 code claims numerically; check P1's "at SR-1 strength" is used
  consistently and not silently upgraded; flag any place the text says "PASS" without its condition attached.

## §7 — Disclosure & provenance

Full history in §1 (2016 circular → 2021 phonon FAIL → 2024 reopen → 2025 Lorentz route → 2037/2038 VTD-1).
The 2021 FAIL was *self-reopened* on physics (wrong mode), not because OPEN is a nicer answer. Source files:
`VTD-1_RESOLUTION.md` (2037), `VTD-1_CONFIRMED.md` (2038), `mu_eps_closure/em_emergence/R2-RESOLUTION-VIA-LORENTZ.md` (2025),
`mu_eps_closure/R2-STATUS.md` (the ladder), OPEN-SR-9 scope. Blob/raw GitHub pointer provided in dispatch
(provenance only; **inline is authoritative — do not gate on fetching**).

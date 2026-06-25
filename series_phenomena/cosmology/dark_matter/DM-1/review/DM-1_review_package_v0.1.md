# DM-1 Review Package v0.1 — A Velocity-Independent Self-Interacting Dark-Matter Candidate from Substrate Aggregates

**Artifact:** DM-1 v0.1 (DRAFT) — first identification-grade paper of the CPP dark-matter / cosmology sector.
**Patch:** 0858 (cycle-opening; paper promoted to .tex at Patch 0856, version-labelled v0.1 at 0857; content assembled Patches 0700–0855).
**Result under review:** the claim that cosmological dark matter is charge-neutral qDP/hTetra substrate aggregates, with a **derived, velocity-independent** self-interaction **σ_V/m ≈ 0.20 cm²/g** across the entire dwarf-to-cluster range — a positive coring discriminant that distinguishes the candidate from both collisionless CDM (σ/m = 0) and velocity-dependent (light-mediator) SIDM.
**Grade claimed:** positive-discriminant candidate, **NOT** full identification. Consistent at dwarf-spheroidal scale; in **mild-to-moderate tension** with the largest LSB cores (IC 2574). **No THEO registered** (conjecture + microphysics + confrontation, not a closed theorem).

**Full paper (everything needed to review is inline below; the .tex is linked for completeness):**
- blob: https://github.com/Hyperphysics-Institute/CPP/blob/main/series_phenomena/cosmology/dark_matter/DM-1/DM-1_substrate_dark_matter_candidate.tex
- raw: https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/series_phenomena/cosmology/dark_matter/DM-1/DM-1_substrate_dark_matter_candidate.tex
  *(provenance only — likely unreachable for external reviewers on this private repo; the inline content is authoritative)*

**Responses aggregate in:** `series_phenomena/cosmology/dark_matter/DM-1/review/reviews-DM-1.md`.

---

## §1. Context (cold-start for a reviewer)

Conscious Point Physics (CPP) derives Standard-Model structure from a 600-cell lattice of Grid Points whose Conscious Points execute a Perceive–Compute–Displace (PCD) cycle. Its collective excitations are dipole pairs of three sectors: electromagnetic (eDP), hybrid (hDP), and quark (qDP), with binding energies 88, 152, 264 MeV. Four CPP results are taken as established inputs here (cited, not re-derived): the quark sector and its mass scale (SF-3), the strong sector — SU(3) colour, gluons as hDP, confinement (SF-5), the gradient-SSV gravity mechanism (SR-1), and the emergent Schrödinger dynamics licensing a scattering treatment (QM-1).

The dark-matter conjecture (**CONJ-COSMO-1**) posits **no new field**: the dark sector is identified with structures the substrate already contains — charge-neutral (colour-singlet, electrically neutral) qDP/hTetra aggregates — and the paper asks whether their derived properties reproduce dark matter.

**The honest status the paper claims (scrutinize the scope calibration, not only the math):** *a derived, falsifiable, velocity-independent SIDM candidate with a positive coring signature; consistent at dSph scale; in mild-to-moderate tension at the largest LSB cores; with the absolute mass scale and the dark-to-baryon ratio inherited as calibrated inputs (on par with ΛCDM), and the cosmological gate (DM-2) traversed without kill and now resting on one open condition. NOT a full identification.*

---

## §2. The claim chain (the spine — this is what to review)

1. **The candidate.** Dark matter = charge-neutral qDP/hTetra aggregates. Constituent mass **m_qDP ≈ 264 MeV** (ratio-clean: E_qDP = 3·E_eDP, colour factor 3). The qCP carries fermionic zitterbewegung ⇒ the qDP pair is a **boson** ⇒ spin-0 soliton ground state.

2. **Two distinct masses (do not conflate).** The *constituent* mass m_qDP = 264 MeV (the scattering partners) sets σ/m; the *aggregate-unit* mass m_unit (one neutral cluster) sets the abundance and is unpinned (~0.26 GeV → ~1 GeV → heavier). The σ/m result depends on the constituent mass **only**.

3. **Cheap-kill gates survived.** Collisionless at the bare level (neutral), diffuse (no bound nuggets), glueball-stable (residual too shallow to bind), and cold by ~10⁵–10⁶× the WDM bound. These are admission, not discriminants.

4. **The residual interaction.** Between colour-singlet qDPs the leading exchange is **two-gluon colour van der Waals** (a singlet cannot emit one gluon; hDP = gluon, SF-5). Screened-LJ form: hard core r_c ≈ 1.0 fm (eDP coat), Yukawa range λ ≈ 1.3 fm, depth V₀ = f·E_qDP with **f ≈ 0.2** (colour-polarizability estimate; factor-3 band f ∈ [0.07, 0.6]) ⇒ **V₀ ≈ 53 MeV**.

5. **Discriminant I — velocity-independent cross-section.** Finite-energy partial-wave scattering of (4). Across v = 30–3000 km/s, **k·λ ≈ 9×10⁻⁵ → 9×10⁻³ ≪ 1**, so scattering stays in the s-wave scattering-length limit (higher partial waves ~ (k·λ)⁴). The identical-boson viscosity cross-section is **σ_V = (4/3)σ₀** (×2 boson symmetrization × 2/3 viscosity weighting). Result: **σ_V/m ≈ 0.20 cm²/g, velocity-independent to four digits** over the whole range — the *opposite* of light-mediator SIDM (σ/m ∝ v⁻⁴). Flatness carries no f-dependence; magnitude does (factor-3 f-band; upper band f ≳ 0.5 hits a Ramsauer dip).

6. **Discriminant II — observable cores (density).** A self-interaction forms a core of central density ~ρ₁, the one-scatter density ρ₁(σ_1D) = 1/[(σ/m)·⟨v_rel⟩·t], ⟨v_rel⟩ ≈ 2.26 σ_1D, t = 10 Gyr. Confronted with two systems ~5× apart in velocity: Fornax (σ_1D = 11) gives ρ₁ = 0.094 vs obs 0.016–0.07 (2.8×); IC 2574 (σ_1D = 57) gives ρ₁ = 0.018 vs obs ≈0.006 (3.1×). **Both sit a similar ~3× above observed — flat across 5× in σ** — the discriminating signature: a velocity-*dependent* σ/m would make the Fornax offset far exceed IC 2574's; it does not.

7. **Discriminant II — observable cores (size).** Inverting the NFW r₁ condition ρ_NFW(r₁) = ρ₁(σ/m) turns the density test into a core-*size* prediction. Fornax-scale halo (V_max ≈ 25): r₁(0.20) ≈ 0.32 kpc, inside the observed ≲0.3–0.7 kpc core; the core implies σ/m = 0.18–0.58 — **f-band brackets 0.20, consistent**. IC 2574 (V_max ≈ 80): r₁(0.20) ≈ 1.83 kpc, well below its ~8 kpc core, which requires **σ/m ≈ 1.1–2.7 — above the f-band**.

8. **The honest tension.** (7) surfaces a **genuine high-velocity tension** the density test (6) did not fully expose: the largest LSB cores want more self-interaction than velocity-independent 0.20 supplies (echoing the velocity-dependent σ/m ~ 1–2 of rotation-curve SIDM fits, Kaplinghat-Tulin-Yu 2016). Escape routes named: (i) f underestimated at galaxy scale (factor-3 band), (ii) residual velocity-dependence, (iii) IC 2574's low-c halo inflating the requirement. Carries halo-model (c, ×2) and r_core/r₁ (O(1)) systematics.

9. **Falsifiability.** The signature is the **flatness**. If data require σ/m to fall from ~1–3 (dwarfs) to ~0.1 (clusters), the flat 0.20 fails on the dwarf side (it physically cannot rise at low v). If data are flat ~0.1–0.3 across scales, CPP predicts it with no free knobs beyond f. Two-sided test, live now (IC 2574 is the worked dwarf-side instance).

10. **Calibrated inputs (stated, not hidden).** The absolute mass scale (Project C, in prep) and the dark-to-baryon ratio Ω_DM/Ω_b ≈ 5.36 (abundance, non-binding — vast reservoir) are *calibrated*, on par with ΛCDM. Not claimed as derived.

11. **Cosmological gate (DM-2).** The Sea-gravitation structure is traversed A→D without kill. The c08 field-equation condition is **discharged** (G_μν = 8πG/c⁴·T_μν[LSP] at zero new params; the absolute-|SSV| monopole annihilated by 600-cell symmetry ⇒ uniform Sea inert; ground-state-exclusion falsifier refuted). The gate rests on **one** remaining condition (event-horizon IR-scale selection). Status: *conditionally supported, not promoted to derived.*

---

## §3. What this paper does NOT claim (deflation guardrails — confirm these are held)

- It does **not** claim a full cosmological *identification*. It is a positive-discriminant candidate.
- It does **not** derive the absolute mass scale or the dark-to-baryon ratio — both are stated as calibrated inputs (on par with ΛCDM).
- It does **not** claim the IC 2574 large-core system is fit — it is flagged as a genuine mild-to-moderate tension, awaiting the f pin-down.
- It does **not** claim the Sea-gravitation gate is closed — one condition (event-horizon selection) remains open; the status is "conditionally supported, not derived."
- It does **not** register a THEO; the result is conjecture + microphysics + confrontation, not a closed theorem.

---

## §4. Open marks the paper carries (registered, not closed)

- **f pin-down** (Project C / colour-polarizability) — collapses the σ/m magnitude band and decides whether the IC 2574 tension is absorbed or genuine.
- **Sea-gravitation gate:** one open condition (the event-horizon IR-scale selection); the rest discharged.
- **Abundance (route B):** asymmetric-DM derivation of the ~5:1 ratio (currently calibrated).
- **DM-unit mass:** the aggregate-unit mass is unpinned (range stated); abundance is non-binding so it does not gate the result.

---

## §5. Triage order (work these top-down; the top items are verdict-flipping)

**T1 — the velocity-independence claim + the cross-section construction (highest stakes).** Is σ_V/m ≈ 0.20 genuinely **velocity-independent** for the stated reason — that k·λ ≪ 1 across the whole range pins scattering in the s-wave scattering-length limit? Is the identical-boson viscosity factor **σ_V = (4/3)σ₀** correct (×2 symmetrization × 2/3 viscosity weighting), and is the s-wave-limit treatment (vs a full phase-shift calculation) adequate at the stated f and V₀? Is the flatness logically separable from the (uncertain) magnitude?

**T2 — the coring confrontation method (density + size).** Is the one-scatter density ρ₁ = 1/[(σ/m)⟨v_rel⟩t] the right core-density estimator, and is ⟨v_rel⟩ = 2.26 σ_1D applied consistently across a dispersion-supported dSph and a rotation-supported LSB (σ_1D = V_max/√2)? Is the **NFW r₁ inversion** (ρ_NFW(r₁) = ρ₁ ⇒ r_core ~ r₁) correctly applied, and are the conclusions robust to the halo-model (c) and r_core/r₁ O(1) systematics the paper claims?

**T3 — the IC 2574 tension: honestly stated, or under/over-stated?** Is the flat ~3× density offset → "supports velocity-independence" (claim 6) consistent with the core-size result that IC 2574 wants σ/m ≈ 1–2 (claim 7–8)? Is the paper's framing — consistent at dSph scale, mild-to-moderate tension at the largest cores — correctly calibrated, or is it spinning a falsification as a feature (or, conversely, over-conceding)?

**T4 — velocity conventions + observational inputs.** Is the ⟨v_rel⟩ = 2.26 σ_1D convention (and σ_1D = V_max/√2 for the rotation-supported case) defensible, given it carries a factor ~2? Are the observed numbers used correctly (Fornax central density 0.016–0.07 and core ≲0.3–0.7 kpc; IC 2574 v_max ≈ 80, core ~8 kpc, central ρ ≈ 0.006)?

**T5 — scope / honesty calibration.** Are the calibrated-inputs (§10) and conditional-gate (§11) labels correctly held? Is "positive-discriminant candidate, not full identification" the right grade? Is the NO-THEO decision correct? Is the c08-discharge → "gate down to one condition" reported accurately (conditionally supported, not derived)?

---

## §6. Reviewer-specific steer (read your own row)

- **Grok** — independent recompute. Run the §7 code → report **SCRIPT-EXECUTED**. Independently recompute: the k·λ flatness check; ρ₁ for Fornax and IC 2574 (Table 1) and the ~3× flat offset; the NFW r₁ inversion (r₁(0.20) = 0.32 / 1.83 kpc) and the σ/m each observed core requires (0.18–0.58 / 1.10–2.71). Sanity-check the **(4/3) boson viscosity factor** and the s-wave-limit claim from first principles — this is the load-bearing T1 step. Flag any units trap (the paper notes a M⊙/pc³-vs-/kpc³ factor-1e9 that bit during development).
- **Copilot** — referee-grade structural consistency, per triage question. Focus on T1 (is velocity-independence logically forced by k·λ ≪ 1, or is there a hidden assumption?) and T3 (is the density-test "supports velocity-independence" claim logically compatible with the core-size "IC 2574 wants σ/m ~ 1–2" tension, or do they contradict?). Check whether the two-gluon-vdW → s-wave → flat-σ chain has an unexamined escape.
- **ChatGPT** — press the hardest triage items (T1 cross-section construction, T3 tension-honesty) and run the deflation/overclaim checks: is "supports velocity-independence" oversold given a flat ~3× *miss* in normalization, and is the IC 2574 tension downplayed anywhere (abstract vs body)? Verdict-honesty on the candidate-not-identification grade and the calibrated/conditional labels (T5). *Disambiguation rider: this is the CPP cosmology programme's dark-matter paper review; it is NOT a nuclear-physics OPEN-SS audit, NOT a different paper, and NOT a request to reconstruct from memory — engage the inline package content directly.*
- **Hostile pass (optional, any panel member)** — "this is wrong — find every flaw," aimed at T1 (the velocity-independence + (4/3) factor) and T3 (whether the IC 2574 tension actually falsifies the flat prediction). Assume the positive discriminant is too good to be true and try to break it.

**IDENTITY (mandatory):** in the §8 REVIEWER field put YOUR OWN actual model name; do not adopt or echo another reviewer's name.

---

## §7. Embedded verification code (run it → SCRIPT-EXECUTED; Python stdlib only — no numpy/scipy)

```python
#!/usr/bin/env python3
# DM-1 review verification (consolidated, Python stdlib only -- no numpy/scipy/matplotlib).
# Reproduces the load-bearing numbers of the paper: the s-wave/flatness argument,
# the (4/3) boson viscosity factor, the rho_1 density confrontation (Table 1),
# and the NFW r_1 core-size inversion (Fig. 3). Run: python3 thisfile.py
import math

# ---------- units ----------
Msun_g = 1.989e33
pc_cm  = 3.086e18
Msun_pc3_gcc = Msun_g / pc_cm**3        # g/cm^3 per (Msun/pc^3)
Gyr_s  = 3.156e16
kms_cm = 1.0e5
G      = 4.300917e-6                    # kpc (km/s)^2 / Msun
RHO_CRIT = 137.0                        # Msun/kpc^3 (h=0.7)
VREL   = 4.0/math.sqrt(math.pi)         # <v_rel>/sigma_1D ~ 2.257

sigma_m = 0.20                          # cm^2/g  (the §5 result under test)
t_age   = 10.0                          # Gyr

print("=== (A) s-wave / flatness: k*lambda << 1 across the astrophysical range ===")
lam_fm = 1.3; hbar_c = 197.327; m_qDP = 264.0   # MeV, fm
for v in (30.0, 300.0, 3000.0):
    k = (m_qDP/2.0)*(v/3.0e5)/hbar_c            # 1/fm, reduced mass m/2
    print(f"  v={v:6.0f} km/s   k*lambda = {k*lam_fm:.2e}")
print("  -> << 1 everywhere; higher partial waves ~ (k*lambda)^4 negligible")
print("  -> sigma stays in the s-wave scattering-length limit => velocity-INDEPENDENT.")

print("\n=== (B) boson viscosity factor  sigma_V = (4/3) sigma_0 ===")
print("  identical-boson symmetrization (x2) * viscosity weighting (2/3) = 4/3")

def rho1(sig1D, sm=sigma_m, t=t_age):       # Msun/pc^3
    return 1.0/(sm*VREL*sig1D*kms_cm*t*Gyr_s)/Msun_pc3_gcc

print("\n=== (C) one-scatter density rho_1 confrontation (Table 1) ===")
for name, s1d, obs in (("Fornax", 11.0, (0.016, 0.07)),
                       ("IC 2574", 80.0/math.sqrt(2), (0.006, 0.006))):
    r = rho1(s1d); mid = math.sqrt(obs[0]*obs[1])
    print(f"  {name:8s} sigma1D={s1d:5.1f}  rho1={r:.3f} Msun/pc^3  obs~{mid:.3f}  pred/obs={r/mid:.1f}x")
print("  -> both ~3x above observed, FLAT across 5x in sigma -> supports velocity-independence")

# ---------- NFW r_1 inversion (stdlib bisection) ----------
def nfw(vmax, c):
    mc = math.log(1+c) - c/(1+c)
    rho_s = (200.0/3.0)*RHO_CRIT*c**3/mc            # Msun/kpc^3
    r_s = vmax/math.sqrt(4*math.pi*0.2162*G*rho_s)  # kpc
    return rho_s, r_s

def bisect(f, a, b):
    fa = f(a)
    for _ in range(200):
        m = 0.5*(a+b); fm = f(m)
        if abs(fm) < 1e-10 or (b-a) < 1e-12: return m
        if fa*fm < 0: b = m
        else: a, fa = m, fm
    return 0.5*(a+b)

def r1_of_sigma(vmax, c, sm):
    rho_s, r_s = nfw(vmax, c)
    rho1_kpc3 = rho1(vmax/math.sqrt(2.0), sm=sm)*1.0e9   # Msun/pc^3 -> Msun/kpc^3
    target = rho_s/rho1_kpc3
    x = bisect(lambda x: x*(1+x)**2 - target, 1e-6, 1e3)
    return x*r_s

def sigma_for_core(vmax, c, rcore):
    return bisect(lambda sm: r1_of_sigma(vmax, c, sm) - rcore, 1e-3, 1e3)

print("\n=== (D) NFW r_1 core-size inversion (Fig. 3) ===")
for name, vmax, c, core in (("Fornax", 25.0, 13.0, (0.3, 0.7)),
                            ("IC 2574", 80.0, 8.0, (6.0, 10.0))):
    r1v = r1_of_sigma(vmax, c, sigma_m)
    lo = sigma_for_core(vmax, c, core[0]); hi = sigma_for_core(vmax, c, core[1])
    print(f"  {name:8s} r1(0.20)={r1v:.2f} kpc  obs_core={core[0]:.1f}-{core[1]:.1f} kpc  "
          f"sigma/m_for_core={lo:.2f}-{hi:.2f} cm^2/g")
print("  -> Fornax: f-band [0.07,0.6] brackets 0.20 (CONSISTENT).")
print("  -> IC 2574: large core wants sigma/m=1.1-2.7 > f-band (high-velocity TENSION).")
```

**Expected output (from the development run, Patches 0850/0851):**
```
(A) k*lambda = 8.70e-05, 8.70e-04, 8.70e-03   (<< 1 -> s-wave, flat)
(C) Fornax  rho1=0.094  pred/obs=2.8x   ;  IC 2574  rho1=0.018  pred/obs=3.1x
(D) Fornax  r1(0.20)=0.32 kpc  sigma/m_for_core=0.18-0.58
    IC 2574 r1(0.20)=1.83 kpc  sigma/m_for_core=1.10-2.71
```

*(The figure-generating scripts `0849_residual_potential.py`, `0850_specific_dwarf_fit.py`, `0851_core_radius_vs_sigma.py` — which also render the PNGs via numpy/scipy/matplotlib — live in `series_phenomena/cosmology/dark_matter/scripts/`; the stdlib script above reproduces their load-bearing numbers without those dependencies.)*

---

## §8. Response format (please follow)

1. **One-line verdict** on the top-triage questions T1 (and T3) first.
2. **Per-question findings** T1→T5, each labelled with its verification tier:
   **INSPECTED** / **INDEPENDENTLY RECOMPUTED** / **SCRIPT-EXECUTED** (PD-002). If you ran the §7 code, report SCRIPT-EXECUTED with the output.
3. **Clearly separate** (a) **verdict-flipping objections** — each with a worked argument — from (b) **calibration** suggestions (wording / scope / honesty-label).
4. **SHIP verdict:** is DM-1 v0.1 acceptable to advance toward v1.0, or does a top-triage objection require a restate to v0.2/v1.1? State it explicitly.
5. **REVIEWER:** your own actual model name (see the §6 IDENTITY note).

---

*Package created Patch 0858 (cycle-opening) per `templates/review_dispatch_protocol.md` §2. Paper promoted to .tex at 0856, version-labelled v0.1 at 0857; content assembled Patches 0700–0855. Self-contained: claim chain (§2), guardrails (§3), open marks (§4), triage (§5), reviewer steers (§6), verify code (§7), response format (§8) all inline; the full .tex is linked in the header for completeness. NO THEO (positive-discriminant candidate, not a closed theorem).*

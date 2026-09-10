# Changelog — EU-1: The Primordial Scalar Spectral Index from Substrate Inflation

Version archaeology for EU-1 (canonical filename carries no version suffix; the
version lives here, per the version-archaeology architecture rule). Result:
n_s = 1 − 2/N_* = 1 − 2/57 ≈ 0.9649, α_s = −2/N_*² ≈ −0.0006, zero-new-axiom.
Registered: PRED-C-96 (n_s, §1 Confirmed/measured-and-consistent) + PRED-O-34 (α_s, §2). No THEO.

---

## v1.5 — 9 September 2026 (Session 169, Patch 3817) — the occupancy re-grounded (FORK-EU-OCCUPANCY-1 → Branch P)

- **3817** — one dated paragraph appended to §Problem Status recording Patch 3816 (founder ruling R-IGNITION-BALL-IN-ONE-PSR): the referent of "one address" in eq. Nstar is one rest-frame Planck sphere, not one grid point (the founder's twelve-per-GP ignition read per GP gives 0.8 e-folds; the programme re-grounded the referent rather than the number); the thirteen-GP seed superseded; N_* = ⅓ ln N_CP − ln(R_init/l_P) (61–65 across 10⁸⁰–10⁸⁴ at R_init = l_P; pivot 57 survives to R_init ≲ 10³ l_P); the §Background "large early PSR" causal-contact sentence re-grounded as the empty-register first Moment over a Planck-sized ball (no enlarged PSR assumed); OPEN-EU-PSR-EARLY-1 registered (PSR floor under saturated load; held vs perceived count; the pivot's survival as pass line); sub-Planck spacing ≳ 3×10²⁷ per l_P (linear) as a consistency condition. n_s unaffected; no equation, result, or section changed. Title block 1.4 → 1.5; date-block version line added. **Recompile owed (Isak).** Source: `eu1_derivation/occupancy_regrounding.md`.

## v1.4 — 9 September 2026 (Session 168, Patch 3809) — the saturation-protocol note (ledger B12)

- **3809** — one dated paragraph appended to §Problem Status recording what Session 167 (Patches 3801–3806, CONV-045 ADMISSIBLE 5–0) established for this paper under the ratified saturation protocol AP-5 and the founder's ruling R-STACK-SENDS-EACH: the n_s epoch is saturated (~74 orders); the tilt survives via **S-HENGINE-HELD** (the H-engine reads the held stack entropy μ = kT ln n̄, not the D1-clipped acted-on displacement; expansion is dilution on a fixed lattice); the count-driven framework leg restated as S-HENGINE-HELD, conditionality unchanged in number, the proposed "unsaturated epoch" gate void; the ignition pairs within 15 Moments and does not inflate (|ΔN| ≤ 0.45); the saturated bath's lag shifts the tilt by Δn_s ≤ 1.4×10⁻⁷. Title-block version reconciled with the catalog (the `.tex` still said 1.0 while the header and catalog said 1.3). **No claim, equation, number or section changed.** Compile gate: pdflatex ×2, 0 errors, 15 pp. Records: `../hengine_driver_statement.md`, `../ignition_handoff_bonding_time.md`, `../bath_depth_lag_bound.md`, `../review/reviews-CONV-045.md`.
- Versions 1.1–1.3 (17 Aug 2026, Patches 3212–3214) were corpus-wide sweeps (identifier appendix; five identifier families; How-we-review note) recorded in the `.tex` header only; no changelog entry was written at the time. Listed here for archaeology; content in the `.tex` header.

## v1.0 (SHIPPED) — 6 June 2026 (Session 155, Patches 0781–0783; Phase 7 0784+)

**First paper of the cosmology / early-universe sector to ship in the corpus.**

- **0781** — v0.1 DRAFT created. Full derivation chain (A1 indistinguishability → μ ∝ ln n̄ →
  p=2 → δN tilt n_s = 1 − 2/N_*), both legs, Debye closure, O(α) theory error. Compiles clean
  (13 pp). Bundled: verify script `scripts/0781_eu1_numerics.py` (ALL PASS), reasoning fragment
  `reasoning/0781_eu1_paper_draft.md`.
- **0782** — review cycle opened: self-contained package `review/EU-1_review_package_v1.0.md`.
- **0783** — review cycle CLOSED, **3/3 SHIP** (ChatGPT/Grok/Copilot), zero verdict-flipping
  objections; numerics independently reproduced + SCRIPT-EXECUTED. Calibration folded in
  (uniqueness softened to practical-uniqueness; p=2 stated as forced within the A1→ZRP→δN chain;
  derived total N_*≈60.5 separated from adopted pivot ≈57; ZRP framed as minimal leading-order
  reduction). Title block v0.1 DRAFT → **v1.0 SHIPPED**. Synthesis: `review/reviews-EU-1.md`.
- **0784 (Phase 7A-i)** — status wording softened *"confirmed at leading order"* →
  *"leading-order derived; consistent with Planck"* (maintainer decision; keeps the register's
  ✅ CONFIRMED = measured-and-consistent classification and the swarm count). This changelog,
  the `bibliography/cpp_references.bib` entry, `INDEX.md` rows, and the `series_phenomena/README.md`
  member row created.

**Honest status (panel-agreed, post-0784 wording):** leading-order derived and consistent with
Planck 2018 (central 0.9649 ± 0.0042), zero-new-axiom, conditional on standing CPP cosmology-sector
commitments (FRW/VSL homogeneity, DP-Sea neutrality, small-α SSV) — not yet fully derived from
A1–A11. O(α) theory uncertainty ~5×10⁻⁴ (~0.12 σ_Planck). Deeper residual registered OPEN-EU-1.

**Verification:** `series_phenomena/cosmology/early_universe/scripts/0781_eu1_numerics.py`
(stdlib-only; reproduces n_s, α_s, N_* bookkeeping, ideal-ZRP slope→p=2, O(α) correction table,
Debye Γ-reframing; ALL PASS).

- **0789 (Phase 7A-ii)** — full narrative documentation suite shipped: development, reviews, keywords, transcript (Pass 1) + mechanism, phenomena, philosophy, glossary, verification, osf-deposit (Pass 2); master_glossary EU-1 terms added (deferred 7B C4). 10 companion files in `documentation_suite/`.

## V1.6 (9 September 2026, Patch 3852) — SUBSTANTIVE: the quoted value moves

**First version in this arc to change the paper's headline number rather than its scaffolding.**

- **(a) T-2 delivered (Patch 3850).** The $O(\alpha)$ correction coefficient closes as **λ = α/κ** exactly (κ ≡ kT_bath/E_Pl), because a = l_P makes Γ = q²/(ℏc) = α at kT = E_Pl. The old 0.1α–10α bracket was a bracket on κ alone. Since the substrate bath cannot exceed the substrate scale, **κ ≤ 1 ⇒ λ ≥ α** and the bracket's lower half is excluded. At the bath clause (κ = 1): λ = α exactly, η = 1.43×10⁻², **Δn_s = +5.0×10⁻⁴**, and η > 0 — a **one-sided systematic shift, not a symmetric uncertainty**.
  - **Quoted value: 0.9649 ± 5×10⁻⁴ → n_s = 0.9654** (0.12σ_Planck). Abstract and title-block updated.
  - Two consequences recorded in the §Problem Status note: the relation run backwards gives an empirical bound **kT_bath ≳ 0.1 E_Pl**; and the residual uncertainty is κ, already a named conditionality leg (the bath clause), so **no new theory error is added** and the framework legs remain three.
- **(b) Amplitude closure (Patch 3847).** A dated note records that the asserted spectator prescription has no identified mechanism; all seven candidates closed; the structural obstruction registered. **The tilt is untouched** — this concerns the amplitude companion A_s only. Three exits recorded, none a further candidate search.
- **Unchanged:** the tilt derivation, Eq. Nstar, the count law, every section structure. Compiles clean in-container (pdflatex ×2, 16 pp, 0 errors, 0 undefined). **RECOMPILE OWED — Isak.**

### Pending (Phase 7 remainder)
- 7A-ii: DONE (Patch 0789).
- OSF deposit: metadata prepared (`documentation_suite/osf-deposit-EU-1.md`); awaiting Thomas's upload + DOI mint-back.
- 7B: programme-register propagation (paper_catalog.md, theory-overview, master_glossary, etc.;
  predictions.md prose status-line wording sync). predictions.md PRED-C-96/PRED-O-34 already stand.
- 7C: final commit + verification pass.

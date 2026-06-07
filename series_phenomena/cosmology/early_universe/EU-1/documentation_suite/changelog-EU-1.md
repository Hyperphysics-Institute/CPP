# Changelog — EU-1: The Primordial Scalar Spectral Index from Substrate Inflation

Version archaeology for EU-1 (canonical filename carries no version suffix; the
version lives here, per the version-archaeology architecture rule). Result:
n_s = 1 − 2/N_* = 1 − 2/57 ≈ 0.9649, α_s = −2/N_*² ≈ −0.0006, zero-new-axiom.
Registered: PRED-C-96 (n_s, §1 Confirmed/measured-and-consistent) + PRED-O-34 (α_s, §2). No THEO.

---

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

### Pending (Phase 7 remainder)
- 7A-ii: DONE (Patch 0789).
- OSF deposit: metadata prepared (`documentation_suite/osf-deposit-EU-1.md`); awaiting Thomas's upload + DOI mint-back.
- 7B: programme-register propagation (paper_catalog.md, theory-overview, master_glossary, etc.;
  predictions.md prose status-line wording sync). predictions.md PRED-C-96/PRED-O-34 already stand.
- 7C: final commit + verification pass.

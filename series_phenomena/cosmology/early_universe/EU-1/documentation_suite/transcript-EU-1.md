# Transcript — EU-1 (Tier-2 transaction pointer-map)

Transaction-indexed navigation index for the EU-1 development history (the n_s arc + paper +
review + Phase-7 publication). Each row: patch (transaction ID) · date · one-liner · pointer.
Tier-3 narrative texture is in `development-EU-1.md`; per-patch Tier-4 reasoning is in
`../reasoning/`. This file is the audit trail / canonical sequence of events.

## Arc — n_s derivation (Session 154, Patches ~0729–0778)

| Patch | Date | Transaction | Pointer |
|---|---|---|---|
| 0729 | ~31 May | Active-swirl generation barrier identified; inflation repurposed as spectrum generator | `../reasoning/` n_s-arc trail; `frontier_sectors/SR.md` |
| 0736–0742 | early Jun | Tilt reduced to $n_s = 1 - p/N_*$; $N_*$ fixed by CP count | `frontier_sectors/SR.md` |
| 0743–0746 | early Jun | Boost-law survey: power-law/packing excluded; entropic log selected → $p=2$ | `frontier_sectors/SR.md` |
| 0749 | early Jun | Log identified as A1 indistinguishability ($\mu \propto \ln\bar n$) | `frontier_sectors/SR.md` |
| 0764–0768 | early Jun | Long-range Debye residual closed (LEMMA-NS-BATH, $\Gamma$-reframing) | `bath_temperature_lemma.md` |
| 0770 | early Jun | Leg 2: DP-Sea pair neutrality → effective EoS | `neutrality_grounding.md` |
| 0772 | early Jun | LEMMA-NS-HTHEOREM: ZRP relaxation via KL Lyapunov | `bath_htheorem.md` |
| 0774–0775 | early Jun | LEMMA-NS-ZRP-DERIVE: PCD/ZBW → symmetric constant-rate ZRP (leading order) | `zrp_derivation.md` |
| 0776 | early Jun | FRW/VSL homogeneity grounded (symmetric kernel) | `inflationary_homogeneity_grounding.md` |
| 0751 | early Jun | CAND-AX-EU-1 drafted (ZBW stack thermalization), then split | `../reasoning/0752_emergence_track_assessment.md` |
| 0778 | 6 Jun | n_s PROMOTED to counted swarm contribution PRED-C-96 (3-AI consensus); 107→108 | `predictions.md`; `../reasoning/0778_ns_promotion.md` |

## Paper + review + Phase-7 (Session 155, Patches 0781–0787)

| Patch | Date | Transaction | Pointer |
|---|---|---|---|
| 0781 | 6 Jun | EU-1 v0.1 DRAFT created (paper + verify script + reasoning); compiles clean 13 pp | `../EU-1_primordial_spectral_index.tex`; `../scripts/0781_eu1_numerics.py`; `../reasoning/0781_eu1_paper_draft.md` |
| 0782 | 6 Jun | Review cycle OPENED — self-contained dispatch package | `../review/EU-1_review_package_v1.0.md` |
| 0783 | 6 Jun | Review cycle CLOSED 3/3 SHIP; calibration folded; v0.1 → v1.0 SHIPPED | `../review/reviews-EU-1.md`; `../reasoning/0783_eu1_review_close.md` |
| 0784 | 6 Jun | Phase 7A-i — status wording softened; changelog + bibliography + INDEX + series-README | `documentation_suite/changelog-EU-1.md`; `bibliography/cpp_references.bib`; `INDEX.md` |
| 0785 | 6 Jun | Phase 7B — programme-register sync (predictions §1 label, paper_catalog row, SR.md, future_projects, README, theory-overview) | `paper_catalog.md`; `predictions.md` |
| 0786 | 6 Jun | §15 Step-E count-provenance audit — Finding A (108 correct), Finding B (tier-vs-headline) flagged | `predictions.md` Count Provenance Ledger |
| 0787 | 6 Jun | Finding-B reconciliation (reading (i)): tier table 104→108; SS-8 ID-range cascade error corrected | `predictions.md` |
| 0789 | 6 Jun | Phase 7A-ii — doc-suite narrative files (this file, development, reviews, keywords; then mechanism/phenomena/philosophy/glossary + notebook + OSF) | `documentation_suite/` |

## Verification artifacts
- `../scripts/0781_eu1_numerics.py` — stdlib-only; ALL PASS (n_s, α_s, N_* bookkeeping, ideal-ZRP slope→p=2, O(α) correction table, Debye Γ-reframing).

## Key registry coordinates
- Predictions: **PRED-C-96** ($n_s$, §1 Confirmed), **PRED-O-34** ($\alpha_s$, §2). No THEO.
- Lemmas (finding-level): LEMMA-NS-HTHEOREM, LEMMA-NS-ZRP-DERIVE, LEMMA-NS-BATH.
- Open: **OPEN-EU-1** (A1–A11 homogeneity + ZRP-correction). Frontier home: `frontier_sectors/SR.md`.

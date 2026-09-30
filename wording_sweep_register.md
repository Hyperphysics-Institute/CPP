# Wording Sweep Register — pre-deposit (roadmap items 0 and 7)

**Registered:** Patch 4340, 29 September 2026. **Tool:** `code/claim_wording_sweep.py [cosmo|const|zero|toe] [--counts]`
lists every hit in the deposit candidates (withheld papers skipped). This file records the triage: what each hit was
judged to need, and where it was done. A hit that states its basis correctly needs nothing.

## cosmo — dark matter, dark energy, cosmological constant (DONE 4340)

| Paper | Hits | Verdict | Done |
|---|---|---|---|
| DP_sea_and_cage_composition (SD foundations) | 13 | overclaimed: "addresses the cosmological constant problem", "emerges directly from the postulates", DM cross-section unlabelled | v1.3 at 4340: Status note; Λ as a candidate mechanism, magnitude not derived; DM figure conditional on CONJ-COSMO-1 |
| EU-1 | 5 | the DM identification stated as fact | v1.6.1 at 4340: "conjectured (CONJ-COSMO-1)" |
| TN-SR-1 | 17 | already labelled "a conjecture (OP-SR-5), not a derived theorem" | none needed |
| GR-1b | 2 | already scoped at W-D (3294): candidate mechanism, magnitude not derivable | none needed |
| GR-1 | 2 | pointers to OPEN-EU-1 and the DE lane | none needed |
| SR-2 | 2 | describes the dependency of the CC and DM arcs on c08's premise | none needed |
| TP-1 | 1 | quotation from the cited paper | none needed |
| DM-2 | 14 | a dark-sector paper; not approved for deposit | deposit approval is the founder's; if approved, it needs the same scoping |

## const — G, ħ, spin, α as derived

| Paper | Verdict | Done |
|---|---|---|
| GR-1, GR-1a, GR-1c (+ GR doc suite) | "G fixed by the lattice, no free parameters" | 4339 (TODO-4300-HBARSWEEP) |
| SR-2 | "λ = 16πG/c⁴ derived" — derived from G-consistency; G itself is the Planck-unit identification | acceptable; no change |
| SS-1c, SS-6 | "gluon spin-1 derived", "J^P = 1⁺ derived in SS-5" | scoped claims about quantum numbers within the model; SS-6 is held with SS-5 |
| SPIN-3 | describes the spin programme's steps | SPIN-3 depends on SPIN-1/2's ħ/2 input — read with TODO-4289-SPINREV |
| QM-6 l.116 | capstone summary | read with TODO-4289-SPINSWEEP |

## zero — "zero-parameter", "no free parameters" (OPEN)

| Paper | Hits | Verdict | Done |
|---|---|---|---|
| SF-2 | 35 | wording correctly scoped (Weinberg angle and m_Z/m_W zero-param; masses stated calibrated) — **but an arithmetic error**: 3/(8φ) written as 0.23121 (the observed value), so m_Z/m_W given as 1.1405 / 0.54% instead of 1.1409 / 0.57%; the companion called the prediction "numerically coincident" with observation | SF-2 v1.08.1 and companion v1.06 at 4341 (erratum + on-shell/MS-bar scope note) |
| SF-4 | 29 | "zero free parameters" for absolute masses omitted the electron-mass calibration carried by M₀ (title already says "One Calibration"); cross-paper paragraph misquoted SM-9 ("top to 0.02%", which SM-9 calls a fortunate cancellation in a two-calibration fit) and SS-7 (measured B(⁴He) input) | SF-4 v3.5 at 4341 |
| SS-8 | 24 | explicitly "conditional-zero-parameter", defined once for the paper; the definition did not name the electron-mass calibration inside B_pair | v1.4 at 4342 (one clause) |
| Capotauro | 22 | "zero free parameters" for χ/6 is honest given FI-C-9/10 named as inputs; **the larger issue is status**: sub-claim (a)/Q7 superseded, δ_CP referral withdrawn, the hand not fixed, the EM leg a convention (4069/4070) | v2.4 at 4342: Status note + superseded banners (E4/E7 of the v2.1 revision plan) |

About 300 hits in some 45 papers. Most are scoped correctly ("zero free shape parameters, one calibration"). The
triage is owed paper by paper, largest first: SF-2 (35), SF-4 (29), SS-8 (24), Capotauro (22). Criterion: a
"zero-parameter" claim must either be literally true of that result or name its calibration or condition in the same
sentence. Tracked as TODO-4340-ZEROSWEEP.

## toe — "Theory of Everything", "derives the Standard Model"

DP_sea_and_cage_composition only (4 hits): scoped by the v1.3 Status note ("the programme's aim, not a result of this
paper"). README's tagline is the programme's description and is left as the founder wrote it.

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

## zero — "zero-parameter", "no free parameters" (DONE 4348)

| Paper | Hits | Verdict | Done |
|---|---|---|---|
| SF-2 | 35 | wording correctly scoped (Weinberg angle and m_Z/m_W zero-param; masses stated calibrated) — **but an arithmetic error**: 3/(8φ) written as 0.23121 (the observed value), so m_Z/m_W given as 1.1405 / 0.54% instead of 1.1409 / 0.57%; the companion called the prediction "numerically coincident" with observation | SF-2 v1.08.1 and companion v1.06 at 4341 (erratum + on-shell/MS-bar scope note) |
| SF-4 | 29 | "zero free parameters" for absolute masses omitted the electron-mass calibration carried by M₀ (title already says "One Calibration"); cross-paper paragraph misquoted SM-9 ("top to 0.02%", which SM-9 calls a fortunate cancellation in a two-calibration fit) and SS-7 (measured B(⁴He) input) | SF-4 v3.5 at 4341 |
| SS-8 | 24 | explicitly "conditional-zero-parameter", defined once for the paper; the definition did not name the electron-mass calibration inside B_pair | v1.4 at 4342 (one clause) |
| Capotauro | 22 | "zero free parameters" for χ/6 is honest given FI-C-9/10 named as inputs; **the larger issue is status**: sub-claim (a)/Q7 superseded, δ_CP referral withdrawn, the hand not fixed, the EM leg a convention (4069/4070) | v2.4 at 4342: Status note + superseded banners (E4/E7 of the v2.1 revision plan) |
| SS-7 | 17 | abstract said B_α comes "from SS-5's ⁴He prediction" but the table uses the measured 28.296 MeV; the body's fully-CPP variant misquoted (−4.0% at ⁴⁰Ca; actually −2.0%) | v1.7 at 4347: inputs stated; fully-CPP RMS 1.77% (verify `series_strong/code/4347_ss7_lo_cpp_variant.py`) |
| EU-1 | 8 | abstract/table/conclusion said the pivot N_* ≈ 57 is "fixed by the CP count", "derived, not assumed"; the body says the pivot placement is adopted | v1.6.2 at 4347: "no fitted parameter, one adopted input" |
| SS-2, SS-5, SS-6, SS-9 | 5/7/–/6 | held papers; SS-2's α_s(m_H) and constituent masses called zero-parameter | status notes at 4347 (held; frame superseded; α_s(m_H) calibrated in effect; m_q assigned; SS-9 calibrated on ⁵⁶Ni) |
| SM-8, SM-9, SF-3 | 14/11/14 | "zero free parameters" always displayed with M₀ = m_e z/φ, so the calibration is visible; SF-3 states the single m_e calibration throughout | none needed |
| SF-5, SF-6, SR-2, SS-1 | 9/5/5/8 | SF-5 names m_e; SF-6 carries its two-tier rigor labels; SR-2's λ is fixed by G; SS-1 scopes its claim to the algebra | none needed |
| GR-1d | 8 | "parameter-free echo" — the prediction itself is withdrawn | covered by the V4 status note (4345) |
| EW-1, EW-5 | 1/– | **the EW-series Monte-Carlo Weinberg angle (0.2312, "0.004%", "no free parameters") was calibrated** — the 1 Apr 2026 code audit found g′ set from the PDG target; the docs were corrected then, the papers never were | status notes at 4348; superseded by SM-6's 3/(8φ) |
| c02 | 2 | "fix the PSR formula without free parameters" — SR-1's k is a normalisation convention (2480) | scoped at 4348 |
| DP-Sea | 3 | one comparison bullet still said "zero free parameters beyond Planck units" | pointed to the v1.3 Status note at 4348 |
| GR-1a/1b/1c/1f/1g/1h/1j, GR-1, GR-2 | 1–3 each | "no free parameters" for metrics that depend only on G and M (the G identification scoped at 4339); GR-2's echo-era table rows are covered by its V2.11 withdrawals | none needed |
| SF-1, SR-1, SR-2, SS-1d, SM-2/3/5/6, SM-10, TP-1, dynamical_substrate_law, SS-6 | 1–3 each | scoped in the same sentence (single calibration, "given the ansatz", "aims to", "consistency, not parameter-free", inherited counts) or already covered by a status note | none needed |
| DM-2 | 4 | zero-parameter w(z) readings in a dark-sector paper not approved for deposit | none (not a deposit candidate until approved; scope with item 7 if it is) |

About 300 hits in some 45 papers — **all triaged by 4348**. Most are scoped correctly ("zero free shape parameters, one calibration"). The
triage is owed paper by paper, largest first: SF-2 (35), SF-4 (29), SS-8 (24), Capotauro (22). Criterion: a
"zero-parameter" claim must either be literally true of that result or name its calibration or condition in the same
sentence. Tracked as TODO-4340-ZEROSWEEP.

## toe — "Theory of Everything", "derives the Standard Model"

DP_sea_and_cage_composition only (4 hits): scoped by the v1.3 Status note ("the programme's aim, not a result of this
paper"). README's tagline is the programme's description and is left as the founder wrote it.

## Generated identifier appendices (4343)

Regenerated for 72 papers after the glossary generator was fixed (TODO-4342-GLOSSREGEN). The OPEN-SD-CHIR-PRIMITIVE gloss now states the current position (handedness a primitive; nucleation superseded; the EM right-hand rule a convention), and OPEN-GR-FE-1 reads as closed.

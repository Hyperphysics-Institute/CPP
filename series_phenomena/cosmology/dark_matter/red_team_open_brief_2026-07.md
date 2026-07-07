# RED-TEAM OPEN BRIEF — the CPP dark-matter arc (pre-release hostile round, July 2026)

**This is not a CONV-001 review.** There are no asks, no claim list, no ratification categories. The
three papers of the arc — DM-1 v1.4, DM-2 v1.0, DM-3 v1.0 — are in a pre-release cooling window
(deposit scheduled ≥ 20 July 2026). Your single instruction: **assume the arc is wrong somewhere, and
find where.** A confirmed KILL finding pauses the release — that is this round's purpose and its
success condition. Five of you receive this brief independently.

## Rules of engagement

1. **Everything is in scope**, including: the registered inputs the papers inherit (the capture
   criterion, the measured floor, E_c, the pitch, χ itself); the arithmetic (re-derive anything); the
   literature (hunt for a killing dataset we never confronted — a halo system, a direct-detection
   result, a cosmological bound, an isotope search, an astrophysical energy-loss argument); the
   statistics (the panel's own prior 5/5 verdicts are attackable — you may indict your own past
   ratifications); the governance (CONV-004 as applied — find a place where "measured coefficient"
   functioned as an escape in practice, not principle); the internal consistency ACROSS the three
   papers (a number used with different values, an assumption used with different strengths).
2. **Findings only — no praise.** The deliverable is a ranked findings list. If you find nothing,
   return exactly `NO FINDINGS` plus a list of what you checked and how (so the null is auditable).
3. **Severity scale:** **KILL** (if true, a paper's central claim fails or a falsifier already fired)
   / **WOUND** (a load-bearing number or statement needs correction; would break the stability cycle)
   / **SCRATCH** (wording, scope, or presentation; foldable without cycle impact).
4. **Every finding must carry:** (a) the exact claim attacked (paper + section/quote); (b) the failure
   mechanism, stated so it could be checked by computation or citation; (c) the decisive check — what
   specific computation, dataset, or derivation would confirm or dismiss it. Unverifiable suspicions
   rank below verifiable ones; state confidence.
5. **Suggested attack surfaces** (not exhaustive — surprise us): the J4 additivity chain everywhere it
   propagates; the 1871 measured-floor MC's geometry pins; the XQC exposure model's astrophysical
   inputs (halo density/velocity at Earth); overburden slowing physics (the Born-regime S_c² scaling
   used for shielding); cluster-bound heterogeneity (Andrade vs others); the dissipative-reach
   criterion's unit-efficiency assumption at the ANCHORS (not just the predictions); the Sea
   portrait's prior structure; DM-2's shell-sum scope; energy-loss/cooling arguments in stars or gas
   from rod capture; Big-Bang-nucleosynthesis or CMB bounds on a 25 GeV strongly-self-interacting
   relic; anything in `code/` that doesn't reproduce.

## Sources
- DM-1: https://github.com/Hyperphysics-Institute/CPP/blob/main/series_phenomena/cosmology/dark_matter/DM-1/DM-1_substrate_dark_matter_candidate.tex
- DM-2: https://github.com/Hyperphysics-Institute/CPP/blob/main/series_phenomena/cosmology/sea_gravitation/DM-2/DM-2_sea_gravitation_dark_sector.tex
- DM-3: https://github.com/Hyperphysics-Institute/CPP/blob/main/series_phenomena/cosmology/dark_matter/DM-3/DM-3_discriminating_predictions.tex
- Normative falsifier table: `DM-3/falsifier_protocols.md`; campaign records: `OPEN-SS-43_Rs_derivation.md`, `DM-3_discriminants_campaign.md`, `sea_gravitation/dm2_rod_era_rescoping.md`; all verify scripts under `dark_matter/code/`.

**Findings will be adjudicated openly:** every KILL/WOUND claim gets a written computation-level
response in the repo; confirmed findings pause or correct the release per the registered checklist.

# SF-5 Phase-7B Integration Content Pack

**Purpose.** Pre-staged content for the SF-5 v1.0 SHIP programme-level (Phase 7B) registry integration. Every edit below touches a **shared hot-list registry** that the other five live windows (DM 800, Chirality 900, Project C 1000, CC 1100, δ_CP 1200) append to — so per the lightweight multi-window protocol rule (E), this integration is ONE flagged patch applied **after a refresh against live HEAD**, NOT pushed autonomously and NOT pre-built against a HEAD that will be stale by morning. This pack lets the morning integration be a fast mechanical apply.

**Landing status: PENDING** (flip to `LANDED at Patch 15NN` when applied).
**Build instruction:** at apply time, `git fetch && git reset --hard origin/main`, then make each edit below with `str_replace` anchored on the stable substring shown, then `git format-patch` as ONE patch. If any anchor has drifted (another window edited that exact line), re-locate the nearest stable anchor and proceed — the inserts are append-style and order-independent.

---

## Key facts that constrain the integration (verified against source)

- **Swarm prediction count: UNCHANGED.** SF-5 introduces NO new counted predictions — every strong-sector correspondence it presents (α_s, the cascade, the binding quantum, SU(3)/gluons) is inherited from already-counted SS-line / SM-7 results. This mirrors SF-3, whose SHIP left the count at 108 for the same reason. **Do not increment the swarm headline.**
- **No new theorems.** SF-5 reframes SS-1b (SU(3) exact) and SS-3 (uniqueness); those THEO IDs stand. `theorem-registry.md` gets a paper-attribution note only, no new THEO.
- **No new axioms.** SF-5 uses the existing 600-cell topology / hopping-dynamics / propagation-efficiency / lattice-scale axioms. `axiom-registry.md` gets a prediction-attribution note only.
- **New open problems:** OPEN-FP-5-GLUEBALL (NEW); OPEN-FP-5-GLUON (RESERVED for four-vertex closure attempts). OPEN-SS-19 (deuteron NLO) and the SS-9 sub-conditions are already registered in the SS sector — inherited, not newly registered.

---

## C7 — `paper_catalog.md` (MANDATORY)

**Anchor:** the SF-Line Flagship Papers table; add the SF-5 row after the SF-3 row (created at Patch 1506). Also prepend a dated entry to the "Last updated:" log.

**SF-5 table row (insert in the SF-Line flagship table):**
```
| SF-5 | Strong-Sector Unification from 600-Cell Geometry | flagship_papers/strong/sf-5_strong.tex | v1.0 SHIPPED 15 Jun 2026 | 4/4 panel SHIP (ChatGPT/Grok/Gemini/Copilot) | OPEN-FP-5-GLUEBALL registered; OPEN-FP-5-GLUON reserved; OPEN-SS-19 + SS-9 conditionality inherited | reframing of SS-1..SS-9 + SM-7/8; no new derivation; single-m_e |
```

**"Last updated:" log entry (prepend):**
> 15 June 2026 (Session 161 Patch 15NN — **SF-5 strong-sector flagship v1.0 SHIPPED** (`flagship_papers/strong/sf-5_strong.tex`): synthesis/reframing of SS-1b/1c/1d, SS-2, SS-3, SS-4, SS-5, SS-7, SS-9, SM-7, SM-8. SU(3) exact (SS-1b) + unique-in-operator-representation (SS-3); 8 gluons = 6 edge + 2 diagonal, massless + spin-1 (SS-1c); confinement + positive β (SS-1d); string tension σ = M₀z²/(φ ℓ_edge) ≈ 926.5 MeV/fm (SS-4); α_s = 5/(8φ) with sin²θ_W+α_s = 1/φ; binding quantum B_pair = M₀/φ = 2.342 MeV, twelve N=Z alpha-chain nuclei RMS < 1% (SS-7). 4/4 panel SHIP, zero verdict-flipping objections. **Swarm count UNCHANGED** (no new derivation; all correspondences inherited+already-counted, as with SF-3). NEW OPEN-FP-5-GLUEBALL; OPEN-FP-5-GLUON reserved. Gluon-counting decision: lead the shipped theorem-level SS-1c octet, demote CONJ-SS-Gluon-4Vertex to flagged conjecture. Deuteron carried honestly (zero-param 2.342 + open +5.3% residual, OPEN-SS-19). NO new theorems (reframes SS-1b/SS-3). Phase 7A doc suite + anthology chapter landed Patches 1522/1523; this patch = Phase 7B.)

## C6 — `predictions.md` (swarm-count UNCHANGED)

**Anchor:** prepend to the "Last updated:" log; mirror the SF-3 Patch-1506 entry's "UNCHANGED" framing.

> 15 June 2026 (Session 161 Patch 15NN — **SF-5 strong-sector flagship v1.0 SHIPPED**: **Swarm count UNCHANGED at 108** — SF-5 introduces NO new derivation; every strong-sector correspondence (SU(3)/gluons, α_s = 5/(8φ), the complementarity, the string tension, the binding quantum, the twelve-nucleus cascade) is inherited from the already-counted SS-line / SM-7 results. The only original moves are the gluon-counting presentation decision and the deuteron-figure correction, neither a new empirical prediction. NEW OPEN-FP-5-GLUEBALL registered in `frontier_sectors/FP.md`. No THEO registered.)

## C5 — `frontier_sectors/FP.md` (OPEN-FP-5-* registration)

**Anchor:** after the `### OPEN-FP-3-CKM` entry (line ~14). Insert two new entries; bump the FP-section problem count in the section header.

```
### OPEN-FP-5-GLUEBALL: Lightest-scalar-glueball mass from a closed tetrahedral hDP loop
**Status:** OPEN (registered at SF-5 v1.0 SHIP, Patch 15NN; inherited from OPEN-SS-6).
The lightest scalar glueball is modelled as a closed tetrahedral hDP loop (the f_geom formula applied to a closed loop), but no closed-form mass is derived. The glueball is the neutral spherical qDP mass, distinct from the cage-bound mesons. SF-5 inherits this as open and does not headline it.

### OPEN-FP-5-GLUON: Four-vertex gluon-counting closure (reserved)
**Status:** RESERVED (registered at SF-5 v1.0 SHIP, Patch 15NN).
The conjecture CONJ-SS-Gluon-4Vertex (the SU(3) octet as a dressing of a four-baryon-vertex bonding taxonomy) is carried by SF-5 as a flagged forward-looking conjecture, NOT a headline, with its own falsification route (a): if substrate enumeration yields exactly 8 types it collapses to "the SM octet restated," and the shipped SS-1c result is arguably that enumeration. Any SF-5-era closure attempt registers here.
```

## C11 — `bibliography/cpp_references.bib` (Phase 7A but shared file → batched here)

**Anchor:** after the `abshier2026sf3` block (ends ~line 782). Add the SF-5 self-entry + the AME 2020 entry (cite key `ame2020`, used in the SF-5 .tex).

```bibtex
% --- SF-5 strong-sector flagship (v1.0 SHIPPED 15 June 2026, Session 161 Patch 15NN) ---
@misc{abshier2026sf5,
  author = {Abshier, Thomas Lee and {Claude Opus}},
  title  = {{SF-5: Strong-Sector Unification from 600-Cell Geometry --- SU(3) Colour, the Eight Gluons, Confinement, the String Tension, and the Light-Nucleus Binding Cascade from the Tetrahedral Cage}},
  year   = {2026},
  note   = {SF-5 v1.0, Conscious Point Physics Flagship Paper Series, Hyperphysics Institute},
  howpublished = {\url{https://github.com/Hyperphysics-Institute/CPP}}
}

@article{ame2020,
  author  = {Wang, Meng and Huang, W. J. and Kondev, F. G. and Audi, G. and Naimi, S.},
  title   = {The {AME} 2020 atomic mass evaluation},
  journal = {Chinese Physics C},
  volume  = {45},
  number  = {3},
  pages   = {030003},
  year    = {2021}
}
```
(If `ame2020` is already present from another paper, add only the SF-5 self-entry.)

## C13 — `book_project/chapters/INDEX.md` (anthology chapter registration)

**Anchor:** add a numbered list entry (after the SF-3 entry, item 11) + the discovery-order/cross-ref table row.

**List entry:**
```
12. **`SF-5_the_octet_was_in_the_tetrahedron.md`** — SF-5 v1.0 SHIPPED 15 June 2026. Strong-sector flagship; a synthesis/reframing of SS-1..SS-9 + SM-7/8 — SU(3) exact + unique-in-operator-representation and the eight gluons (6 edge + 2 diagonal) from the tetrahedral cage, confinement, the string tension 926.5 MeV/fm, α_s = 5/(8φ) with sin²θ_W + α_s = 1/φ, and the twelve-nucleus alpha cascade (RMS < 1%) on a single m_e calibration. Dramatic centerpiece: the *restraint* in the gluon-counting decision — the bold four-vertex forced-choice claim demoted to a flagged conjecture because the corpus's own theorem (SS-1c, eight gluons) absorbs it; the same discipline carries the honest +5.3% deuteron residual rather than an over-optimistic sub-percent claim. The octet was in the tetrahedron the whole time.
```

**Cross-ref table row:**
```
| `SF-5_the_octet_was_in_the_tetrahedron.md` | **Chapter 15: What Is Still Open** (Part Four, flagship-line inventory; OPEN-FP-5-GLUEBALL registered) | *Chapter 14: Honesty as a Procedure* (the gluon-counting restraint and the honest deuteron residual — claim what you have, flag the rest); *Chapter 6: The 600-Cell* (the tetrahedral cage as the colour carrier) |
```

## D1 — `README.md` (root, MANDATORY)

**Anchor:** the Registered Papers / SF-line table; update the SF-5 row to v1.0 SHIPPED and the flagship count. **Swarm headline UNCHANGED at 108.** Add to Strongest Results if desired: "SU(3) + the eight gluons derived from the tetrahedral cage; α_s = 5/(8φ) complementary to sin²θ_W."

## C10 — `programme_orientation.md` (TATWD, MANDATORY at v1.0 SHIP)

**Anchor:** the strong-sector chapter + the Part VIII Predictions Scorecard. Add SF-5 in connected prose (not bullets): the strong sector reframed from the tetrahedral cage on one calibration; the gluon-counting restraint; the α_s/sin²θ_W complementarity as the strong↔EW thread for SF-7. Scorecard: no new counted correspondences (already counted), but record SF-5 as the strong-sector flagship synthesis. Move no open problems out of Part VII; add OPEN-FP-5-GLUEBALL to Part VII.

## D2 — `INDEX.md` (root)

**Anchor:** add the new SF-5 files under a `flagship_papers/strong/` grouping: `sf-5_strong.tex`, `documentation_suite/` (10 files), `review/` (5 files), `reasoning/` (1520.md, 1521.md), `code/1520_verify_sf5_core.py`, and `book_project/chapters/SF-5_the_octet_was_in_the_tetrahedron.md`.

## `flagship_papers/README.md` (SF-line README — shared)

**Anchor:** line ~40, the SF-5 row. Update status `Planned (synthesis ...)` → **`v1.0 SHIPPED 15 Jun 2026 (4/4 panel)`**.

**FLAG FOR THOMAS (needs a decision, not auto-applied):** lines ~56 and ~63 of `flagship_papers/README.md` still carry the OLD gluon-counting framing — line 56 the boson table "Gluon | g | 1 (CPP) / 8 (SM)", and line 63 the narrative "there are not 8 distinct gluon types but rather different bonding relationships between the 4 tetrahedral vertices ... CONJ-SS-Gluon-4Vertex ... a substantive falsifiable claim addressed in SF-5." The SHIPPED SF-5 reversed this: it leads with the theorem-level eight-gluon octet and demotes the four-vertex claim to a flagged conjecture. These two lines now mis-describe what SF-5 ships. **Recommended:** soften line 63 to note the four-vertex claim is a flagged conjecture, not the SF-5 headline, and reconcile line 56's "1 (CPP)/8 (SM)" gluon count. I did NOT auto-edit this because it's an interpretive programme-narrative call across a shared file — your decision.

## Lower-priority / note-only (batch in the same patch where cheap)

- **C4 `master_glossary.md`** — append an end-of-file "## SF-5 strong-sector terms" section (binding quantum, mode-fraction complementarity, hDP gluon channels) if not already glossed from the SS line.
- **C8 `founders_vision.md`** — one-paragraph milestone note: SF-5 v1.0 completes the strong-sector flagship; SF-1/SF-3/SF-5 all shipped in a single day.
- **C9 `future_projects.md`** — mark SF-5 DONE; next SF-line targets SF-6 (electromagnetism) + SF-7 (grand unification).
- **C1 `theory-overview.md`** — strong-sector row refresh if it tracks per-sector flagship status.
- **C2 `axiom-registry.md`** — paper-attribution note only (SF-5 uses no new axioms).
- **C3 `theorem-registry.md`** — paper-attribution note only (SF-5 registers no new theorems; reframes SS-1b/SS-3).
- **C12 `problem_histories/`** — optional `PH-OPEN-FP-5-GLUEBALL.md` birth-registration.
- **C14 `methods_catalogue.md`** — no new methods (synthesis paper; STRAIGHT REUSE of existing derivation methods).

## H6/H7 — final mechanical audit

After the integration lands: run `bash scripts/publication_audit.sh SF-5` from repo root; resolve every `[FAIL]`; confirm no per-paper/per-series `.bib` (H7 — SF-5 uses inline `\bibitem`, compliant). Confirm `python3 flagship_papers/strong/code/1520_verify_sf5_core.py` runs clean.

---

*Staged at Patch 1524 (collision-free own-file under `flagship_papers/strong/`). The actual shared-registry integration is the remaining tranche — apply against live HEAD after a refresh.*

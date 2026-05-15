# SF-4 Handover Document — Session 81 Close (Patch 0342 v4.4 Archival Polish + Patch 0343 Documentation Closeout)

**Paper**: `flagship_papers/neutrinos/sf-4_neutrinos.tex`
**Status**: **v4.4 archival-deposit-quality** (Session 81 close, 11 May 2026, patch 0342). Three-reviewer convergence on SHIP-ready achieved at v4.3 (ChatGPT verdict (a) "v1.0 SHIP-ready" + Grok "outstanding, zero show-stoppers, ready for v1.0 archival" + Copilot "fully SHIP-ready, no remaining corrections required"); v4.4 incorporates Grok's four non-blocking archival polish items. Suitable for direct Zenodo + arXiv upload at Thomas's discretion.
**Closure path**: Three closure campaigns plus four ChatGPT review cycles from v1.0 SHIP (Session 54) through v4.3 SHIP-ready (Session 77), plus archival polish at v4.4 (Session 81) + three programme-level closeout patches (Sessions 78-81). The cage-shell mass formula is at conditional theorem closure level across all three originally-open structural problems: OPEN-FP-SF-4-1 (suppression mechanism + α-exponent reduction) RESOLVED at v3.0; OPEN-FP-SF-4-2 (vertex-by-vertex K3-Cage-Shell Consistency) RESOLVED at v4.0; SM-5 op:nu_id (foundational open problem of CPP neutrino sector) RESOLVED cross-sector at v4.0 — **first cross-sector closure in CPP**.

---

## Status as of Session 81 close

### Paper file
- `flagship_papers/neutrinos/sf-4_neutrinos.tex` at v4.4 archival-deposit-quality state
- 2517 lines source (+14 from v4.3 for four archival polish items)
- 51 pages compiled, 811 KB PDF on ClearPC per the Binary Artifact Workflow (sandbox compile differs slightly per workflow design)
- 25 bibliography entries
- 5 theorems + 1 proposition + 1 lemma (THEO-SF-4-1, PROP-SF-4-2, THEO-SF-4-3, THEO-SF-4-4, THEO-SF-4-5, LEMMA-SF-4-1)
- Two pdflatex passes clean (verified in sandbox); all cross-references resolve including the new `rem:conditional_closure` Remark added at v4.2

### Programme-level registrations
- `theorem-registry.md` updated at patch 0339 with THEO-SF-4-1 status upgrade + NEW THEO-SF-4-4 + NEW LEMMA-SF-4-1 + NEW THEO-SF-4-5. Programme totals: 54 → 56 theorems + 1 proposition + 1 lemma. UNCHANGED at v4.4 (no new theorem objects).
- `master_glossary.md` updated at patch 0339 with new section "SF-4 v4.x conditional-closure framework terms" (8 entries). UNCHANGED at v4.4.
- `paper_catalog.md` updated at patches 0339 (v4.0 → v4.3) and 0343 (v4.3 → v4.4 archival-deposit-quality).
- NEW `theorem-dependency-graph.md` at patch 0340 — programme-level theorem dependency map.
- NEW `templates/conditional_closure_framework.md` at patch 0340 — programme-level methodology document for conditional theorem closure and FI accounting.
- NEW `scripts/cpp-recompile-pdf.sh` at patch 0339 — bash script for ClearPC-canonical PDF compilation. Operational; ran successfully twice (v4.3 at commit 968e4ff, v4.4 at commit 64c2119).
- `CPP_the_theory.md` updated at patch 0343 — TATWD integration of SF-4 v4.4 closure narrative (new chapter on neutrino sector), Part VII open problems updated, Part VIII predictions scorecard expanded with neutrino-sector predictions, programme-level note on conditional-closure framework + cross-sector closure methodology (Finding β-10).

### Anthology chapter
- `book_project/chapters/SF-4_where_two_problems_met.md` shipped at patch 0335 (Session 74, ~4630 words, Rovelli/SciAm register). Section 8 close updated at patch 0339 to reference v4.3 + four-cycle review trajectory + explicit conditional-closure framing.

### v4.4 archival polish (patch 0342)
Four non-blocking items from Grok's review of v4.3 incorporated:
1. **Table 1 caption sourcing**: JUNO 2025 explicitly attributed for sin²θ_12 and Δm²_21; NuFIT 6.0 for atmospheric; DESI/Planck for cosmology with 100-120 meV relaxed range from alternative dataset combinations.
2. **NEW footnote `fn:mass_extraction`** on m_ν_2 row of Table 1: consolidates mass-extraction logic in one location. Explains how empirical comparison values are extracted via lightest-massless approximation m_1 → 0 (accurate to <1% since predicted m_1 ≈ 0.98 meV ≪ √Δm²_21 ≈ 8.66 meV); empirical m_2 → √Δm²_21, m_3 → √|Δm²_31|; m_β ≈ 8.7 meV for KATRIN/Project 8 comparison.
3. **NEW footnote `fn:cosmology_bounds_2026`** on Σm_ν row: 2026 bounds range and trajectory. 72 meV tightest combination (DESI 2024 + Planck 2018 + PR4 lensing); 100-120 meV with Pantheon+/DES-SN5YR; 80-90 meV DESI DR2 + Planck PR4 + CMB lensing in 2026 tightest combinations. SF-4 prediction 64.9 meV below tightest published bound; falsifier against tightening below ~60 meV.
4. **Minor m_ν_3 label correction**: "from Δm²_32" → "from |Δm²_31|" (the 50.9 meV value uses √|Δm²_31| where |Δm²_31| = Δm²_21 + |Δm²_32|; v4.3 label was technically slightly off).
5. Structural-residual paragraph m_ν_2 match-level updated 2% → 1.7% to reflect JUNO 2025 precision.

No theorem changes; no new sections; no structural modifications. Mathematical content unchanged from v4.3. v4.4 is the archival-deposit-quality version.

### Documentation suite (this file's home)
- `documentation_suite/handover-SF-4.md` — THIS FILE, updated at patch 0343 to Session 81 close state. Supersedes the prior Session 60 v2.0 SHIP close handover (preserved in git history).
- `documentation_suite/development-SF-4.md` — vignettes updated at patch 0341 with campaign-grouped narrative for Sessions 55-79.
- `documentation_suite/transcript-SF-4.md` — patch transactions log updated at patch 0341 with entries for patches 0316-0340.
- `documentation_suite/reasoning-SF-4.md` — Tier 4 reasoning capture updated at patch 0341 with pointer section to the three campaign sketch documents that hold the canonical Tier 4 source.

---

## What's resolved

### OPEN-FP-SF-4-1 (suppression mechanism + α-exponent reduction)
**Status: CONDITIONALLY RESOLVED at v3.0** via two-campaign closure:
- v2.0 Picture A axiomatic closure (Sessions 55-60, patches 0316-0321): four sub-claim closures of the Picture A suppression mechanism from CPP axioms A1-A11 + three foundational inputs (3D embedding, neutrino identification, spin-orbital 2:1 frequency-locking convention). Result: σ_ν = (1/z²)⁵ = 1/z¹⁰ ≈ 1.62 × 10⁻¹¹ rigorously derived.
- v3.0 α-exponent residual closure (Sessions 62-66, patches 0323-0328): four sub-claim closures of the V^(7/3) → V² reduction at the bound/unbound boundary, with the central CP anchor identified as the load-bearing structural element. Result: m_unbound = M₀ · V² · σ_ν at leading order in V (Theorem 3.1, THEO-SF-4-4).

Working sketches: `flagship_papers/neutrinos/sketches/SF-4_picture_A_axiomatic_closure.md` (1106 lines) + `SF-4_alpha_exponent_closure.md` (1184 lines).

### OPEN-FP-SF-4-2 (vertex-by-vertex K3-Cage-Shell Consistency) + SM-5 op:nu_id
**Status: JOINTLY CONDITIONALLY RESOLVED at v4.0 — FIRST CROSS-SECTOR CLOSURE IN CPP** via the Composite K3-Cage-Shell Coupling Theorem (Theorem 5.2, THEO-SF-4-5; Sessions 68-72, patches 0329-0334). The closure:
- Charged-lepton K3-vertex occupation at V_k breaks K3's S_3 to S_2(V_k) stabilizer
- Any leading-order S_2(V_k)-invariant perturbation lifts the antibonding-doublet degeneracy
- Standard S_3 → S_2 representation-theory branching rule 2|_{S_2} = 1_+ ⊕ 1_- uniquely (up to phase) yields the TBM-aligned basis
- Cage-shell coupling structurally selected within the symmetry-preserving perturbative class
- 6 FIs + 4 CPP axioms (A1+A4+A7+A9, A1+A7+A9 most load-bearing)
- Six verification flags Vβ-1 through Vβ-6 discharged Session 71
- Single derivation chain resolves both papers' open problems jointly — methodology registered as Finding β-10

Working sketch: `flagship_papers/neutrinos/sketches/SF-4_open_fp_sf_4_2_closure.md` (750 lines).

### Conditional-closure framing (programme-level methodology)
All v4.x closures are conditional theorem closures within the current CPP theorem stack. The framing was made explicit in SF-4 v4.2 (patch 0337) via Remark `rem:conditional_closure` and generalized to programme convention in `templates/conditional_closure_framework.md` (patch 0340). References to OPEN-* problems as "RESOLVED" throughout the paper should be read in the conditional sense — i.e., resolved at the current CPP theorem stack inheritance level, not as full unconditional derivational closure from CPP primitives alone.

---

## What's open

### δ_CP derivation (route ii)
**Status: deferred to SF-2 EW flagship.** The δ_CP CP-violating phase is the 8th of the 8 active-flavor neutrino-sector observable parameters. Per SF-4's route (ii) framing, δ_CP closure is the EW-sector responsibility, inherited as open from OPEN-SM-4 (Capotauro mechanism). Current SF-4 prediction count: 7/8 zero-parameter; closure to 8/8 depends on SF-2 closure of OPEN-SM-4.

**Candidate cross-sector closure pair**: SF-2 ↔ SM-5 OP-SM-4 (Capotauro mechanism for δ_CP). Following Finding β-10 methodology, the next cross-sector closure in CPP would close δ_CP in SF-2 simultaneously with OP-SM-4 in SM-5.

### Public posting
**Status: OSF pending** (v4.3 SHIP-ready 11 May 2026, awaiting deposit). Originally OSF batch DOI: 10.17605/OSF.IO/JXE8D was registered for the programme; arXiv submission expected after Zenodo deposit. The public-posting PDF will be regenerated locally on ClearPC per the Binary Artifact Workflow (patches 0339 establishes ClearPC as canonical compile machine) and uploaded directly.

### Majorana vs Dirac character
**Status: registered open for v5.0+ work.** The cage-shell mechanism does not specify whether neutrinos are Majorana or Dirac fermions; both pictures are consistent with the v4.3 result. Closure depends on substrate-level CP-conjugation properties of the unbound 3D orbital ZBW configuration — not in current SF-4 scope.

### 0νββ rate, sterile-neutrino predictions, radiative corrections, leptogenesis
All registered open in §11 of the paper as v5.0+ work. None in current scope.

---

## Forward queue

Priority order for post-Session 79 work:

(A) **ClearPC PDF recompile** (Thomas-side, ~1 minute). Per the new Binary Artifact Workflow:
```bash
cd ~/Documents/GitHub/CPP
bash scripts/cpp-recompile-pdf.sh flagship_papers/neutrinos
```
This compiles the v4.3 PDF locally on ClearPC and commits it as a follow-up to patch 0340. After this, the in-repo PDF matches the v4.3 .tex source and is GitHub-web-viewable.

(B) **TATWD integration to CPP_the_theory.md at v4.3**. The cross-sector closure narrative + the conditional-closure framework + the SF-line's progression from v1.0 partial-closure flagship to v4.3 conditional-theorem-closure SHIP-ready state are all worth integrating into the master TATWD narrative. Estimated effort: 1-2 sessions.

(C) **SF-2 EW flagship campaign launch**. The δ_CP derivation via OPEN-SM-4 Capotauro mechanism is the next major flagship-paper campaign, and the candidate for a second cross-sector closure in CPP (SF-2 ↔ SM-5 OP-SM-4). Estimated effort: 8-15 sessions for v1.0 SHIP, plus 3-4 ChatGPT review cycles per the SF-4 trajectory pattern.

(D) **Public posting (Zenodo + arXiv) at Thomas's discretion**. v4.3 is SHIP-ready per ChatGPT verdict (a); the only remaining task is Thomas's decision on when to deposit. Recommend after SF-2 ships so the SF-line lands as a unified set rather than piecemeal.

(E) **JUNO peer-review bibliography update**. The JUNO 2025 first physics paper (currently arXiv:2511.14593) is expected to advance through peer review; SF-4's bibliography entry should be updated to the final journal reference when available. Low priority; can be done as a touch-up patch any time before public posting.

---

## Lessons learned in 8 categories (consolidated through v4.3)

1. **Multi-reviewer review passes converge faster than single-reviewer iteration.** SF-4 v1.0 needed 5 review passes (3 ChatGPT + 1 Grok + 1 Copilot); SS-9 needed 7 with single-reviewer iteration. Confirmed across v4.0 → v4.3: each ChatGPT review pass after v4.0 caught a smaller class of issues, with the class scope reducing by an order of magnitude each cycle.

2. **Numerical-logic bugs slip past review until pointed out.** Three instances in SF-4 history: v0.6 §9.1.2 self-contradiction (survived 2 ChatGPT passes); v0.8 §3.4 mass-ratio arithmetic inconsistency (survived 4 review passes); v4.0 §5.6 partial-closure language directly contradicting Theorem 5.2 (survived internal review until v4.0 ChatGPT review caught it). Programme practice updated at patch 0339: per-SHIP global-consistency sweep before external review submission.

3. **Mass-ratio vs mass-squared-splitting language is a recurring trap.** Multiple review cycles required paper-wide grep on terminology fixes. Consistent across v1.0, v2.0, v3.0, v4.x.

4. **Reviewer convergence on "v1.0-ready" forward-looking statement is the right SHIP signal.** ChatGPT's verdict (a) "v1.0 SHIP-ready, no further substantive edits required" at v4.3 is the clearest possible SHIP signal — distinct from "ready after N fixes" verdicts.

5. **Documentation suite is ACTIVE post-v1.0 ship; only the .tex source freezes between SHIPs.** Confirmed across the v1.0 → v4.3 trajectory: the documentation suite (this file + the three companions) is updated at each version increment that adds substantive content. The .tex source freezes per SHIP version but the documentation evolves continuously.

6. **External review at scale identifies programme-level methodology gaps that internal review elides.** The conditional-closure framework was implicit throughout v1.0 → v4.0; it became explicit only when ChatGPT v4.1 review asked "what does 'RESOLVED' actually mean in this paper?" The framework now lives at programme level in `templates/conditional_closure_framework.md`. Pattern: methodological conventions tend to crystallize at specific friction points rather than being designed up-front.

7. **Cross-sector closure is methodologically distinct from ordinary cross-paper inheritance.** When two open problems in different papers are tied together (each paper's closure depending on the other), waiting for either to close independently is the default failure mode. Cross-sector closure inverts this via a single derivation chain that uses foundational inputs from both sectors. Methodology registered as Finding β-10.

8. **Binary artifacts in git create cross-machine friction.** The cross-machine .pdf blob hash mismatch at patch 0336 application surfaced a structural issue: pdflatex is byte-non-deterministic. Resolution: ClearPC designated as canonical compile machine; Claude commits .tex only; Thomas recompiles .pdf locally via `cpp-recompile-pdf.sh`. Programme convention adopted at patch 0339.

---

## Quick-start for next session

If the next session is **SF-2 launch**: start from the SF-2 audit phase. Read `flagship_papers/electroweak/sketches/SF-2_*.md` if any exist; otherwise begin with the audit document (Session 37 SF-4 audit was the model for the SF-line audit format). Cross-sector closure pair SF-2 ↔ SM-5 OP-SM-4 (Capotauro mechanism for δ_CP) is the candidate for second cross-sector closure in CPP per Finding β-10 methodology.

If the next session is **TATWD integration**: read `CPP_the_theory.md` current state. Integration scope: cross-sector closure narrative + conditional-closure framework + four-cycle review trajectory + SF-line's progression from v1.0 partial-closure flagship to v4.3 conditional-theorem-closure SHIP-ready state.

If the next session is **public posting**: Thomas's decision required first; if approved, the Zenodo deposit + arXiv submission proceed from the locally-compiled v4.3 PDF on ClearPC. The .tex source is already at v4.3 SHIP-ready state on origin; the only step is the upload.

If the next session is **SF-4 v5.0** (Majorana/Dirac, 0νββ, sterile-neutrino, leptogenesis): far horizon work. Not currently prioritized.

---

## Recent session count

- Sessions 37-54: Pre-v1.0 development through v1.0 SHIP (audit, mechanism selection, suppression derivation working, K3 Cage-Shell Consistency working, paper drafting, multi-reviewer review cycles, v1.0 SHIP at Session 54).
- Sessions 55-60: v2.0 Picture A axiomatic closure campaign (OPEN-FP-SF-4-1 first half), patches 0316-0321.
- Sessions 62-66: v3.0 α-exponent residual closure campaign (OPEN-FP-SF-4-1 second half), patches 0323-0328.
- Sessions 68-72: v4.0 cross-sector closure campaign (OPEN-FP-SF-4-2 + SM-5 op:nu_id jointly resolved), patches 0329-0334.
- Session 73: v4.0 programme-level registration, patch 0334.
- Session 74: Anthology chapter "Where Two Problems Met", patch 0335.
- Session 75: v4.1 from ChatGPT v4.0 review (6 structural fixes + NEW Lemma 3.1 + stale-text cleanup), patch 0336.
- Session 76: v4.2 from ChatGPT v4.1 review (4 calibration fixes including NEW Remark rem:conditional_closure), patch 0337.
- Session 77: v4.3 from ChatGPT v4.2 review (3 textual consistency fixes); ChatGPT verdict (a) v1.0 SHIP-ready, patch 0338.
- Session 78: Programme-level closeout patch 0339 (registers freeze + Binary Artifact Workflow + recompile script + anthology chapter v4.3 touch-up).
- Session 79: Programme-level methodology patch 0340 (NEW conditional_closure_framework + NEW theorem-dependency-graph + OS cross-references).

Total: ~25 sessions Session 55-79 + the v1.0 era Session 37-54 = ~42 sessions in the SF-4 dossier.

---

## Where to find detail

- **Paper text**: `flagship_papers/neutrinos/sf-4_neutrinos.tex` (current state at origin/main HEAD; v4.3 SHIP-ready).
- **Anthology chapter**: `book_project/chapters/SF-4_where_two_problems_met.md` (the Rovelli/SciAm-register narrative).
- **Tier 4 reasoning sketches**: `flagship_papers/neutrinos/sketches/SF-4_picture_A_axiomatic_closure.md` + `SF-4_alpha_exponent_closure.md` + `SF-4_open_fp_sf_4_2_closure.md`. These are the canonical verbatim reasoning capture for the three closure campaigns.
- **Programme conventions**: `templates/conditional_closure_framework.md` (v4.x methodology) + `theorem-dependency-graph.md` (inheritance map) + `templates/operating_system.md` § Binary Artifact Workflow (PDF compile discipline).
- **Companion docs in this suite**: `development-SF-4.md` (per-campaign vignettes), `transcript-SF-4.md` (patch transactions), `reasoning-SF-4.md` (Tier 4 capture pointer).

---

**This handover document supersedes**: `documentation_suite/handover-SF-4.md` v1.0 (Session 54), v2.0 (Session 60), and v4.3 (Session 79). The Session 81 close state is the current canonical handover and represents the dossier's final state — SF-4 v4.4 archival-deposit-quality, ready for public posting at Thomas's discretion.

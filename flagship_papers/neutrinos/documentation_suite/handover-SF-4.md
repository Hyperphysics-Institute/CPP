# SF-4 Handover Document — Session 54 v1.0 SHIP Close

**Paper**: `flagship_papers/neutrinos/sf-4_neutrinos.tex`
**Status**: **v1.0 SHIPPED** (Session 54 close, 9 May 2026, patch 0314).
**Reviewer convergence**: Five independent AI review passes (ChatGPT × 3, Grok × 1, Copilot × 1) all converged on v1.0-promotion-ready. ChatGPT pass-3 forward-looking statement: *"After those fixes, I would be comfortable promoting SF-4 to v1.0 SHIP as a partial-closure flagship prediction paper."*

---

## Status as of Session 54 close

**Paper**: SHIPPED at v1.0. The .tex file at `flagship_papers/neutrinos/sf-4_neutrinos.tex` carries the cage-shell-formula partial-closure flagship neutrino-sector paper as v1.0 SHIPPED. **Per the v1.0-ship anti-priority lessons learned from SS-9, the .tex source itself is FROZEN at v1.0 unless and until external feedback (post-public-posting) prompts a v1.x revision.**

**SF-4 documentation suite**: ACTIVE, not frozen. Subsequent sessions can add new SF-4 artifacts (anthology chapter, TATWD integration, supplemental docs, post-arXiv reviews) at progressively wider registers without re-opening the .tex source.

**Compiled state**:
- Source: 1850+ lines `.tex`
- PDF: 40 pages, 537 KB
- Two-pass `pdflatex` clean, all cross-references resolve

## What v1.0 SHIPPED contains

### Substantive content (frozen at v1.0)

**Foundation (§0–§3)**: Abstract, founder's voice (§1.5), claim-status ledger (§1.6 Table 1.1), SM-5 K3-eigenmode foundation (§2), Candidate-C cage-shell mass formula (§3) including:
- Mass formula $m_{\nu_i} = M_0 \cdot V_{\nu_i}^2 \cdot \sigma_\nu$
- Cage-shell assignment $V \in \{4, 12, 30\}$ in mass basis (with prominent boxed clarification at first appearance)
- Geometric-origin paragraph for $V$ values (icosahedral first shell / tetrahedral inscribed sub-cage / icosidodecahedral $d^2 = 2$ shell)
- Operator-level picture for $\alpha = 2$ at the bound/unbound boundary
- Mass-ratio predictions with explicit dual-convention presentation (absolute-mass 2%/8% vs ratio-level 4%/11%)

**Substantive derivations (§4–§5)**:
- Suppression mechanism §4: walk-dimension framework, integer channel enumeration ($d_{\mathrm{eff}} = 5$), three convergent CPP physical pictures (A: two-sided DI-bit / B: two ZBW half-cycles / C: edge-straddling), per-channel suppression $z^{-2}$, combined $\sigma_\nu = z^{-10}$ at 2% empirical match. Cosmological-bound sanity check $\Sigma m_\nu \approx 64.9$ meV at zero parameters.
- K3-Cage-Shell Consistency Theorem §5: Theorem 5.1 (three clauses); mass-basis-vs-flavor-basis foundational observation; Proposition 5.2 ($\mu\tau$-exchange symmetry); Theorem 5.3 (exact TBM angle recovery); Route C structural closure via 600-cell distance shells + SM-1 particle-type taxonomy.

**Closing sections (§6–§11)**: Master predictions table (refined category labels distinguishing absolute-scale PARTIAL CLOSURE from mass-ratio zero-parameter); $\delta_{CP}$ posture (route ii deferral with four candidate handles enumerated); higher-order corrections (OP-SM-7d inheritance); cumulative falsifier (5 falsifiers across direct + framework levels + partial-failure modular-falsification scenarios); open theorem-level work (OPEN-FP-SF-4-1, OPEN-FP-SF-4-2, items not addressed including running/leptogenesis); discussion (programme-level pattern, cross-sector implications, outlook).

### Theorem registrations (paper-internal at PARTIAL CLOSURE)

The three formal mathematical objects of SF-4 v1.0:

| ID | Object | Closure status | Source |
|----|--------|----------------|--------|
| **THEO-SF-4-1** | K3-Cage-Shell Consistency, structural-numerical level | Conditional theorem; clauses (i)+(ii) exact at zeroth order; clause (iii) at SM-5-inheritance level | §5.1 |
| **PROP-SF-4-2** | $\mu\tau$-exchange symmetry of $\hat{V}^2_{\mathrm{flavor}}$ | Theorem | §5.3 |
| **THEO-SF-4-3** | Exact recovery of TBM angles from $\hat{V}^2_{\mathrm{flavor}}$ | Theorem (tautological by construction) | §5.3 |

Registered in `theorem-registry.md` Session 54.

### Predictions (zero-parameter)

Seven of eight neutrino-sector parameters at zero free parameters:
- $m_{\nu_1} \approx 0.98$ meV (lightest, NH)
- $m_{\nu_2} \approx 8.81$ meV (within 2% of $\sqrt{\Delta m^2_{21}} \approx 8.66$ meV)
- $m_{\nu_3} \approx 55.1$ meV (within 8% of $\sqrt{|\Delta m^2_{31}|} \approx 50.9$ meV)
- $\Sigma m_\nu \approx 64.9$ meV (under DESI/Planck $\le 72$ meV bound)
- $\sin^2\theta_{12} = 1/3$, $\sin^2\theta_{23} = 1/2$, $\sin^2\theta_{13} = 0$ at TBM zeroth order (NuFIT 6.0 / JUNO 2025: $0.307/0.572/0.0220$ — corrections via OP-SM-7d)
- Normal mass hierarchy forced by cage-shell assignment

The 8th parameter ($\delta_{CP}$) is registered open and deferred to SF-2 EW-flagship per route (ii).

### Bibliography

22 bibliography entries (12 internal CPP + 10 external):
- CPP internal: SM-1, SM-3, SM-5, SM-7, SM-8, SM-9, SS-1, SF-line README + 4 sketches
- External: NuFIT 6.0 (arXiv:2410.05380), JUNO 2025 first physics (arXiv:2511.14593), DESI 2024, Planck 2018, Planck-PR4 alternative, KATRIN 2022, Project 8, DUNE TDR, Harrison-Perkins-Scott (TBM original), Ma-Rajasekaran ($A_4$ original), Altarelli-Feruglio (discrete flavor symmetries review)

## Polish track FINAL (v0.5 → v1.0)

| Stage | Session | Patch | Pass | Verdict | Items |
|-------|---------|-------|------|---------|-------|
| Integration polish + first PDF | 49 | 0309 | — | — | Stale-version sweep + 32-page PDF |
| ChatGPT pass 1 | 50 | 0310 | v0.5 | "NOT v1.0-shippable yet" | 8 substantive corrections + 10 bibliography + "derives" audit |
| ChatGPT pass 2 | 51 | 0311 | v0.6 | "Close to v1.0 SHIP quality" | 3 fixes (mass-ratio language; falsifier logic bug; cross-refs) |
| Grok pass 1 | 52 | 0312 (consolidated) | v0.7 | "Very close to v1.0 SHIP quality" | 6 polish suggestions |
| Copilot pass 1 | 52 | 0312 (consolidated) | v0.7 | "Close to v1.0 SHIP quality" | 11 polish suggestions |
| ChatGPT pass 3 | 53 | 0313 | v0.8 | "Promote to v0.9, not v1.0 yet" | 3 v1.0-blocking fixes + bookkeeping |
| **v1.0 SHIP** | **54** | **0314** | **v0.9** | **"Comfortable promoting"** | **SHIP mechanics** |

**Five-pass review tally**: ChatGPT × 3 + Grok × 1 + Copilot × 1 = 5 independent AI review passes. SS-9 used 7 passes; SF-4's 5 passes plus reviewer-convergence on "v1.0-ready" forward-looking statement is sufficient grounds for promotion.

## Programme state at SF-4 v1.0 ship

- **Theorems registered**: 52 → 54 (+ 1 proposition); SF-line section added to theorem-registry
- **Predictions**: 7 of 8 neutrino sector parameters at zero free parameters; $\delta_{CP}$ deferred to SF-2
- **Open problems**: OPEN-FP-SF-4-1 PARTIAL CLOSURE preserved (suppression mechanism Picture A theorem-level closure); OPEN-FP-SF-4-2 PARTIAL CLOSURE preserved (vertex-by-vertex K3-coupling theorem; tied to SM-5 antibonding-doublet open problem)
- **Conjectures**: CONJ-EW-W0 and CONJ-SS-Gluon-4Vertex registered Session 41 (architectural revision); preserved through ship
- **Negative results**: programme negative-result count UNCHANGED
- **Falsifiers registered**: 5 (JUNO inverted hierarchy; cosmological tightening to $\Sigma m_\nu < 50$ meV; principled direct-mass falsifier at $m_\beta \approx 8.7$ meV; PMNS deviation from TBM; substrate-mechanism deviation from $\sigma_\nu = z^{-2 d_{\mathrm{eff}}}$ form)

## Post-v1.0 work queue (priority order)

### A. OPEN-FP-SF-4-1 Picture A formalization (HIGH PRIORITY)

The suppression mechanism's structural-physical picture is at PARTIAL CLOSURE: three convergent CPP physical pictures, integer channel enumeration, 2% empirical match. Theorem-level closure from CPP axioms A1–A11 is registered as v1.0+ work.

Four enumerated sub-goals (from §10.1):
1. Picture A formalization (priority): rigorously establish (a) DI-bit send/receive independence in unbound regime, (b) channel coherence as AND of both sides aligning, (c) per-moment $1/z^2$ from these.
2. Independence verification: rule out (or quantify) substrate correlations between send and receive choices.
3. Channel-count rigor: quantify sub-leading corrections to $d_{\mathrm{eff}} = 5$ from partial-binding effects.
4. $\alpha = 2$ closure: theorem-level derivation of the $V^{7/3} \to V^2$ reduction at the bound/unbound boundary.

**Estimated effort**: 5–10 sessions of focused derivation work plus AI-review iteration. Single-paper continuation work; could ship as SF-4 v2.0 update or as a standalone follow-up paper.

### B. SM-5 antibonding-doublet open problem (CROSS-SECTOR COOPERATION)

OPEN-FP-SF-4-2 closure at vertex-by-vertex K3-coupling level is **tied to SM-5's existing open problem** on lifting the K3 antibonding-doublet degeneracy. Closure of SM-5's open problem would simultaneously close OPEN-FP-SF-4-2 to theorem level via Argument 3 (§5.6.3). Cross-sector mutual-closure opportunity.

**Estimated effort**: comparable to (A) but with high coupling to SM-5 work. Best pursued as joint SM-5/SF-4 work; closure benefits both papers simultaneously.

### C. SF-2 EW-flagship drafting (route ii closure)

The $\delta_{CP}$ derivation is deferred to SF-2 per route (ii). On SF-2 closure, SF-4 prediction count extends from 7/8 to 8/8 zero-parameter, plus higher-order corrections lift the looser-match residuals (8–11%) toward sub-1% via the same Capotauro mechanism. Four candidate handles enumerated for SF-2 forward reference (§7.2): cage-orientation angle, Capotauro bias, K3-eigenstate phase structure, substrate chirality.

**Estimated effort**: SF-2 is the next SF-line flagship after SF-4. Begin drafting after SF-4 v1.0 ship is propagated through registers; OPEN-FP-SF-4-1 work can proceed in parallel.

### D. Anthology chapter at Rovelli/SciAm register

Parallel to SS-9 *"The Polyhedron's Conditions"* (Session 34, ~5389 words). For SF-4: the title and bridge centerpiece are TBD but candidates include "*Why Are Neutrinos So Light?*" or "*The Geometry of Three Masses*". Audience: science-literate non-physicists. ~5000 words at popular-science register.

**Estimated effort**: 1–2 sessions. Can ship at any time post-v1.0 without re-opening the .tex.

### E. TATWD integration to CPP_the_theory.md

Parallel to SS-9 integration in Session 35. Add SF-4-specific chapter(s) to `CPP_the_theory.md` (Part VI substantive paragraphs covering the cage-shell mass formula, the K3-Cage-Shell Consistency Theorem, the suppression mechanism). Add Part VII open-problem chapter for the post-v1.0 work queue items above.

**Estimated effort**: 1 session.

### F. JUNO 2025 follow-up at peer-review publication

When the JUNO arXiv:2511.14593 paper progresses to peer-reviewed publication, replace the `\bibitem{juno2025_first_results}` reference with the peer-reviewed citation. Minor bibliography sweep only; no other changes needed.

**Estimated effort**: 0.1 sessions (housekeeping); triggered by external event.

## File inventory at v1.0 SHIP

```
flagship_papers/neutrinos/
├── README.md                          ← v1.0 SHIPPED status
├── sf-4_neutrinos.tex                 ← v1.0 SHIPPED, 1850+ lines
├── sf-4_neutrinos.pdf                 ← v1.0 SHIPPED, 40 pages, 537 KB
├── sf-4_outline.md                    ← v0.1 outline (Session 44, historical)
├── sketches/                          ← Pre-paper working documents
│   ├── README.md
│   ├── SF-4_neutrino_sector_audit.md       (Session 37)
│   ├── SF-4_mechanism_selected.md          (Session 39)
│   ├── SF-4_suppression_derivation.md      (Sessions 40–41)
│   └── SF-4_k3_cage_shell_consistency.md   (Sessions 42–43)
└── documentation_suite/               ← v1.0 SHIP four-tier docs
    ├── handover-SF-4.md                    ← THIS FILE (Session 54 v1.0 SHIP)
    ├── development-SF-4.md                 ← Per-session development arc
    ├── transcript-SF-4.md                  ← Per-session transactions
    └── reasoning-SF-4.md                   ← Tier 4 verbatim reasoning
```

## Lessons learned from SF-4 v1.0 campaign

1. **Multi-reviewer review passes converge faster than single-reviewer iteration.** The Grok + Copilot pass at v0.7 surfaced polish items ChatGPT had missed (operator-level picture, geometric-origin paragraph, Σm_ν sanity check, partial-failure scenarios) — independent reviewers catch independent blind spots.

2. **Numerical-logic bugs slip past review until pointed-out.** v0.6 §9.1.2 contained a self-contradiction (predicted $m_\beta \approx 8.7$ meV but said "$m_\beta > 5$ meV would falsify") that survived two ChatGPT passes before being caught at the v0.6 review (pass 2). Pattern: arithmetic-consistency sweeps should be a deliberate pre-ship pass, not assumed correct.

3. **Mass-ratio vs mass-squared-splitting language is a recurring trap.** The 4-pass mass-ratio language sweep (abstract → §3.4 → §6.1 → §8 → §11.2) shows how easy it is for terminology to drift between drafts. Lesson: when fixing terminology in one place, run a paper-wide grep to catch all instances.

4. **Reviewer convergence on "v1.0-ready" is the right SHIP signal.** After two ChatGPT passes both said "close to v1.0", and Grok + Copilot independently agreed, the convergence pattern was strong enough that ChatGPT pass-3's three-fix verdict ("comfortable promoting after these fixes") was the cleanest possible v1.0-promotion signal.

5. **Five passes (3 + 1 + 1) is sufficient where SS-9 needed seven.** SS-9 used 7 review passes (ChatGPT × 4 + Copilot × 2 + Grok × 1) with cache-resolution issues. SF-4's 5-pass discipline benefited from the reviewer-protocol lessons learned (submit .tex not PDF; trust convergence). Forward lesson: 5 passes is a defensible SHIP floor for partial-closure flagship papers when reviewers explicitly converge.

6. **Documentation suite is ACTIVE post-v1.0; .tex source is FROZEN.** The SS-9 lesson learned at Session 33 applies to SF-4: the four-tier documentation discipline applies whenever new SF-4 artifacts ship. Only the .tex source freezes at v1.0.

---

## Session 54 v1.0 SHIP CLOSE

SF-4 v1.0 SHIPPED. Five-pass review discipline complete. Partial-closure flagship neutrino-sector paper SHIPPED with:
- 7 of 8 zero-parameter predictions (3 masses + 3 mixing angles + hierarchy ordering, $\delta_{CP}$ deferred)
- 1 conditional theorem (Theorem 5.1) + 1 proposition (Proposition 5.2) + 1 secondary theorem (Theorem 5.3)
- 5 clean falsifiers
- 22 bibliography entries
- 40-page compiled PDF
- Four-tier documentation suite

Forward work flows through OPEN-FP-SF-4-1 + SM-5 cooperation + SF-2 closure. Anthology chapter and TATWD integration are post-ship doc-suite work that does not re-open the .tex.

**SF-4 SHIPPED.**

---

*Session 54 close, 9 May 2026, patch 0314. Next active flagship paper: SF-2 EW or SF-1 charged leptons per SF-line architecture; OPEN-FP-SF-4-1 follow-up work can proceed in parallel.*

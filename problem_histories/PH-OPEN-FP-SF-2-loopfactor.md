# Problem History: OPEN-FP-SF-2-loopfactor — Substrate-derivation of one-loop oblique correction structure

**Created:** 14 May 2026 (registered at SF-2 v1.0 SHIP, Session 83 close, Patch 0370)
**Status:** OPEN — registered open frontier at SF-2 v1.0 SHIP; closure path identified
**Research_Frontier.md entry:** OPEN-FP-SF-2-loopfactor
**Target paper:** SF-2 v1.x revision (post-public-posting feedback) OR Layer 4 continuum-EFT dedicated paper per PD-004 publication-pathway
**Parent paper:** SF-2 v1.0 SHIPPED 14 May 2026 (Session 83 close, Patch 0368)

---

## The Problem

Derive from CPP substrate primitives the one-loop effective field theory contribution of the W⁰ catalyst to the precision-electroweak oblique parameters S, T, U.

### Mechanism context (SF-2 v1.0)

The Companion v1.0 §5.3 presents parametric scaling ansätze for $\Delta S^{(W^0)}, \Delta T^{(W^0)}, \Delta U^{(W^0)}$ written in EFT-resembling notation (one-loop counting factors $1/(16\pi^2)$, $D_6$-symmetry-motivated structural coefficients of order unity, bracelet cage scale $Q_{\mathrm{cage}}$ vs $m_W$). These are dimensional scaling heuristics only, not renormalized one-loop electroweak corrections — explicitly disclaimed in the emphatic red mdframed box added at Patch 0367 above the equations. The mass-degeneracy structural prediction $\Delta T \approx 0$ is robust at parametric-scaling level (verified across entire Companion §5.7 sensitivity scan); $|\Delta S|, |\Delta U|$ are heuristic placeholders.

### Closure route

Full continuum-EFT derivation requires the five ingredients enumerated in the Companion §5.3 disclaimer box: (i) continuum EFT with explicit Lagrangian and propagator structure; (ii) gauge-fixing prescription; (iii) Ward-identity-preserving regulator; (iv) renormalization scheme matching to Peskin-Takeuchi conventions; (v) one-loop diagrammatic computation with substrate-specific Feynman rules. The Companion §5.7 sensitivity scan identifies the geometric target band $|r_{33} - r_{3Q}| \lesssim 0.18$ with $r_{33} \geq 0.85$ that the eventual derived calculation must land in — this is a falsifiable constraint on the Layer 4 continuum derivation (PRED-O-24).

### Open remarks

This is the central open problem for the W⁰ catalyst framework's precision-electroweak content. Without continuum-EFT closure, the framework remains structurally constrained substrate-level phenomenology (Layer 3 per PD-004) rather than a completed Yang-Mills field-theoretic derivation. ChatGPT v1.3 review identified this as the framework's biggest reality constraint: "Without a valid continuum bridge, the framework remains geometric phenomenology, not a completed physical theory." Closure path = Layer 4 dedicated paper (continuum-limit development; not folded into a flagship per ChatGPT explicit recommendation in PD-004).

---

## The Journey

### Pre-SF-2 (Sessions 1-80)

The problem was implicit in the CPP electroweak sector but not formally registered. SM-1 four-cage taxonomy + SS-1 binary icosahedral group structure provided foundational inheritances. EW-1 through EW-5 papers (predecessors to SF-2) had partial structural sketches but no theorem-level closure framework.

### Session 41 architectural revision (9 May 2026)

Patch 0301 revised SF-line architecture from 5-paper Option-3 to 7-paper architecture (SF-1 through SF-7); SF-2 scoped to electroweak cage bosons (W±/W⁰/Z/H) with W⁰ novel-particle prediction registered as CONJ-EW-W0. The six OPEN-FP-SF-2-* problems were not yet split out at this point — they were implicit in the "SF-2 substrate-level closure" goal.

### Sessions 81-82 SF-2 v0.x drafting (Patches 0345-0361)

Eleven patches building SF-2 main paper from v0.1 outline through v0.7 with three multi-reviewer convergence cycles. Mass formula architecture with three calibrated dilution factors ($\eta_W$, $\eta_Z$, $\eta_H$ — OPEN-FP-SF-2-η implicit) plus EWSB cage-formation framing in §11 (OPEN-FP-SF-2-EWSB implicit) plus structural-level discussions of one-loop oblique corrections, shell-density factor, DP-chain composition, and V-A chirality.

### Session 83 Companion paper + multi-reviewer cycles (Patches 0362-0367)

Six patches developing Companion paper from v1.0 kickoff through v1.4 with actual GPU-result incorporation (DP-chain composition exploratory toy MC reports (40.3% / 29.7% / 29.6% / 0.4%) at Patch 0364; oblique-parameter $\Delta T \approx 0$ structural prediction confirmation at Patch 0366; sensitivity-scan with-bounds-region geometric structure at Patch 0366; ChatGPT v1.3 final polish at Patch 0367). The six OPEN-FP-SF-2-* problems became explicitly tracked at this point as the rigor-frontier work remaining post-v1.0.

### Patch 0368 (14 May 2026) — v1.0 SHIP with OPEN-FP-SF-2-* registered

Joint main paper + Companion v1.0 SHIP at Patch 0368 (Session 83 close) with three-reviewer convergence on SHIP-at-v1.0 verdict. The six OPEN-FP-SF-2-* problems formally registered as the substrate-level closure frontier:
- OPEN-FP-SF-2-η: cage-stability dilution factor first-principles derivation
- OPEN-FP-SF-2-EWSB: EWSB cage-formation mechanism first-principles derivation
- OPEN-FP-SF-2-loopfactor: one-loop oblique correction structure first-principles derivation
- OPEN-FP-SF-2-shelldens: shell-density factor first-principles derivation
- OPEN-FP-SF-2-chaincomp: substrate-thermodynamic DP-chain composition derivation
- OPEN-FP-SF-2-CHIR: chirality emergence in W bracelet (V-A coupling derivation)

### Patch 0370 (14 May 2026) — programme-level registration

This file created at Patch 0370 (Session 83 close registers freeze) per the Research_Frontier architecture; entry added to Research_Frontier.md Flagship Papers (FP) section.

---

## Dependencies

**Inherits from:**
- SF-2 v1.0 framework (THEO-SF-2-1 through THEO-SF-2-5; PROP-SF-2-1 through PROP-SF-2-6)
- SM-6 Weinberg-angle spectral-trace correspondence (numerical inheritance, no derivation dependence)
- SM-7/8/9 cage-stability mass-formula machinery (parameter-architecture inheritance)
- SS-1 binary icosahedral group $\Gamma$ structure (gauge-algebra inheritance via THEO-SF-2-5)
- 600-cell topology and orbit-stabilizer structure (geometric foundational inputs)

**Likely shared closure path with:**
`OPEN-FP-SF-2-eta`, `OPEN-FP-SF-2-EWSB`, `OPEN-FP-SF-2-shelldens`, `OPEN-FP-SF-2-chaincomp`, `OPEN-FP-SF-2-CHIR`

The six OPEN-FP-SF-2-* problems are not fully independent — they share dependencies on substrate thermodynamics (OPEN-FP-SF-2-EWSB, OPEN-FP-SF-2-η, OPEN-FP-SF-2-shelldens, OPEN-FP-SF-2-chaincomp) and continuum-EFT structure (OPEN-FP-SF-2-loopfactor, OPEN-FP-SF-2-CHIR). Closure of these substrate-level frameworks at Layer 4 (per PD-004) may resolve multiple OPEN-FP-SF-2-* entries simultaneously.

---

## Falsification route

The closure of OPEN-FP-SF-2-loopfactor from CPP primitives plus the appropriate foundational inputs would be falsified by:
1. Foundational input errors (incorrect inheritance from SF-2 v1.0 framework or upstream papers)
2. Sub-claim proof errors (should be checked by external review during Layer 4 dedicated paper review cycle)
3. Experimental disagreement with the resulting prediction (e.g., precision-electroweak measurement contradicting derived $\Delta S, T, U$ structure for OPEN-FP-SF-2-loopfactor)

---

## Cross-sector connections

OPEN-FP-SF-2-CHIR potentially cross-sector-closeable with OPEN-SM-4 (Capotauro mechanism for $\delta_{CP}$) per the methodological pattern of SF-4 v4.0's first cross-sector closure (Finding β-10): single derivation chain simultaneously resolves open problems in two distinct papers when the foundational inputs of one closure are sufficiently rich to determine the closure in another sector. The Capotauro dedicated paper (Session 82 priority for SF-4 8/8 completion) is the candidate closure venue.

---

## Registered

14 May 2026 Session 83 close Patch 0370 (this patch) registers OPEN-FP-SF-2-loopfactor in Research_Frontier.md Flagship Papers (FP) section + this problem-history file created.

# Problem History: OPEN-FP-SF-2-CHIR — Chirality emergence in W bracelet structure (V-A coupling derivation)

**Created:** 14 May 2026 (registered at SF-2 v1.0 SHIP, Session 83 close, Patch 0370)
**Status:** OPEN — registered open frontier at SF-2 v1.0 SHIP; closure path identified
**research_frontier.md entry:** OPEN-FP-SF-2-CHIR
**Target paper:** SF-2 v1.x revision (post-public-posting feedback) OR Layer 4 continuum-EFT dedicated paper per PD-004 publication-pathway
**Parent paper:** SF-2 v1.0 SHIPPED 14 May 2026 (Session 83 close, Patch 0368)

---

## The Problem

Derive from CPP substrate primitives the 100% V-A coupling structure of W± gauge boson interactions with fermions at the massless helicity limit.

### Mechanism context (SF-2 v1.0)

The W± charged-current weak interactions exhibit pure V-A (vector minus axial-vector) coupling in the Standard Model, equivalent to coupling exclusively to left-handed fermions and right-handed anti-fermions. SF-2 v1.0 §5 PROP-SF-2-5 establishes that the W bracelet's $120°/240°$ phase bias delivers V-A coupling at $75\%$ from the bracelet's $D_6$ phase structure (structural preference, not theorem-level). The $100\%$ V-A at the massless helicity limit registers as the remaining theorem-level closure target.

### Closure route

Two potential closure paths: (1) Continuum-EFT Layer 4 derivation: the V-A structure emerges via gauge-invariance of the eventual Yang-Mills EFT (THEO-SF-2-5 proof outline) at the massless fermion limit; closure tied to the broader Layer 4 continuum derivation. (2) Substrate-level mechanism via Patch 0367 captured W⁰ neutrino scattering insight: the centroid-decoupling mechanism may provide a substrate-level chirality-emergence story (spinning DP/h-tet passes through W⁰ centroid → momentary DP Sea decoupling → emerges with discrete reorientation determined by post-centroid allowed directions); if the $D_6$ stabilizer of the W bracelet imprints chirality-specific anisotropy on the post-emergence direction distribution, this would be a substrate-level V-A derivation. The sketch is captured at `flagship_papers/electroweak/sketches/W0_neutrino_scattering_centroid_decoupling.md` with three-Layer development required before paper integration.

### Open remarks

Potential cross-sector closure pair with OPEN-SM-4 (Capotauro mechanism for $\delta_{CP}$): both are framework-level V-A / chirality questions in the electroweak sector. The Capotauro paper at SF-line dedicated venue may serve as the closure paper for both OPEN-FP-SF-2-CHIR and OPEN-SM-4 — analogous to SF-4 v4.0's cross-sector closure of OPEN-FP-SF-4-2 + SM-5 op:nu_id (the first cross-sector closure in CPP).

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

This file created at Patch 0370 (Session 83 close registers freeze) per the Research_Frontier architecture; entry added to research_frontier.md Flagship Papers (FP) section.

---

## Dependencies

**Inherits from:**
- SF-2 v1.0 framework (THEO-SF-2-1 through THEO-SF-2-5; PROP-SF-2-1 through PROP-SF-2-6)
- SM-6 Weinberg-angle spectral-trace correspondence (numerical inheritance, no derivation dependence)
- SM-7/8/9 cage-stability mass-formula machinery (parameter-architecture inheritance)
- SS-1 binary icosahedral group $\Gamma$ structure (gauge-algebra inheritance via THEO-SF-2-5)
- 600-cell topology and orbit-stabilizer structure (geometric foundational inputs)

**Likely shared closure path with:**
`OPEN-FP-SF-2-eta`, `OPEN-FP-SF-2-EWSB`, `OPEN-FP-SF-2-loopfactor`, `OPEN-FP-SF-2-shelldens`, `OPEN-FP-SF-2-chaincomp`

The six OPEN-FP-SF-2-* problems are not fully independent — they share dependencies on substrate thermodynamics (OPEN-FP-SF-2-EWSB, OPEN-FP-SF-2-η, OPEN-FP-SF-2-shelldens, OPEN-FP-SF-2-chaincomp) and continuum-EFT structure (OPEN-FP-SF-2-loopfactor, OPEN-FP-SF-2-CHIR). Closure of these substrate-level frameworks at Layer 4 (per PD-004) may resolve multiple OPEN-FP-SF-2-* entries simultaneously.

---

## Falsification route

The closure of OPEN-FP-SF-2-CHIR from CPP primitives plus the appropriate foundational inputs would be falsified by:
1. Foundational input errors (incorrect inheritance from SF-2 v1.0 framework or upstream papers)
2. Sub-claim proof errors (should be checked by external review during Layer 4 dedicated paper review cycle)
3. Experimental disagreement with the resulting prediction (e.g., precision-electroweak measurement contradicting derived $\Delta S, T, U$ structure for OPEN-FP-SF-2-loopfactor)

---

## Cross-sector connections

OPEN-FP-SF-2-CHIR potentially cross-sector-closeable with OPEN-SM-4 (Capotauro mechanism for $\delta_{CP}$) per the methodological pattern of SF-4 v4.0's first cross-sector closure (Finding β-10): single derivation chain simultaneously resolves open problems in two distinct papers when the foundational inputs of one closure are sufficiently rich to determine the closure in another sector. The Capotauro dedicated paper (Session 82 priority for SF-4 8/8 completion) is the candidate closure venue.

---

## Registered

14 May 2026 Session 83 close Patch 0370 (this patch) registers OPEN-FP-SF-2-CHIR in research_frontier.md Flagship Papers (FP) section + this problem-history file created.

---

## v3.0+ Layer 4 Closure Trajectory Pickup (Session 136 Patch 0482)

**Date:** 19 May 2026
**Session:** 136 opening (post-Session 135 Capotauro v2.0 v1.0 SHIPPED)
**Patch:** 0482

### What enabled the pickup

Capotauro v2.0 v1.0 SHIPPED (Session 135 Patch 0479) delivered **THEO-SD-CHIR-1** (Cross-Sector Substrate Chirality Unification Theorem; K3-doublet $\leftrightarrow$ W-bracelet pair; registered Patch 0434 Session 132): $|M^W| = \chi/6 = \phi^{-3}/6 \approx 0.0394$ at full Layer 3 rigor via the four-step proof chain (substrate-locality + Substrate-Locality Unification + cage-shell factor identity + pairing-convention identification with $\zeta^W$ = icosahedral-center inversion in 4D and matter-doublet basis in $E_2 \oplus E_1$ subspace of $D_6$). This is precisely the substrate-physics input that SF-2 v1.0 registered as missing for Layer 4 closure of OPEN-FP-SF-2-CHIR — the substrate-level chirality matrix element on the W-bracelet that the continuum-EFT projection of THEO-SF-2-5 (Yang-Mills EFT limit, proof-outline level) needs as input to deliver the V--A coupling structure at observable scales.

The v3.0+ closure trajectory was named as a Capotauro v2.0 forward-queue priority in the Session 135 handover (`handovers/2026-05-19_session_135_capotauro_v2.0_v1.0_SHIPPED.md` Forward queue Priority 3): "**SF-2 v2.0+ Layer 4 EFT closure**: proceeds in SF-2 paper's venue; closing OPEN-FP-SF-2-CHIR allows Falsifier 6 to become operative as a sharp empirical falsifier."

### Patch 0482 deliverables (scoping sketch creation)

NEW working sketch document created at [`flagship_papers/electroweak/sketches/SF-2_chir_layer4_closure.md`](../flagship_papers/electroweak/sketches/SF-2_chir_layer4_closure.md) (~450 lines), structured as:

- **§0 Working-session firewall**: surfaces two architectural decisions for Thomas's review:
  1. Route choice — Route (i) canonical continuum-EFT Layer 4 derivation extending THEO-SF-2-5 proof outline (recommended) vs. Route (ii) substrate-mechanism via Patch 0367 W$^0$ neutrino scattering centroid-decoupling sketch (cross-validation candidate for future-window work).
  2. Venue choice — Venue (b) dedicated Layer 4 continuum-EFT paper per PD-004 (recommended) vs. Venue (a) SF-2 v2.0+ flagship-paper extension (not recommended; contradicts PD-004) vs. Venue (c) joint Layer 4 paper with SM-2 v2.0+ chiral-polarity-bias closure feeding from sibling THEO-SD-CHIR-2 substrate handle (recommended deferred option if SM-2 v2.0+ scoping concurrent).
- **§1 Setup**: closure target articulation + Capotauro v2.0 substrate-handle inheritance + 10 foundational input enumeration (FI-CHIR-1 through FI-CHIR-10 across substrate inputs, continuum-EFT architecture, continuum kinematics categories) + Layer architecture mapping per PD-004.
- **§2 Two-route framing**: route comparison table + recommendation of Route (i) as primary closure path.
- **§3 Sub-claim decomposition under Route (i)**: four sub-claims (a)(b)(c)(d) covering bridge from substrate handle to effective Lagrangian + finite-mass Michel $\rho = 3/4$ derivation + massless helicity limit $100\%$ LH preference + Capotauro Falsifier 6 activation.
- **§4 Venue question**: three-option analysis with recommendation of Venue (b) per PD-004 ("dedicated papers are required — this cannot be folded into flagship phenomenology papers").
- **§5 Cross-sector dependencies**: Capotauro v2.0 substrate handle, SM-2 v2.0+ chiral-polarity-bias parallel, EW-5 Yang-Mills EFT inheritance.
- **§6 Session budget estimate**: 11-17 sessions for full theorem-level closure under Route (i) + Venue (b); 15-25 sessions under Venue (c) joint paper.
- **§7 Forward queue and anti-priorities**: route/venue decision as Priority 1 immediate; sub-claim (a) closure work as Priority 2 post-decision; SM-2 v2.0+ scoping as Priority 3 background.
- **§8 Status update**: programme state changes registered with this patch (trajectory promoted from "registered open frontier" to "v3.0+ Layer 4 closure trajectory OPENED at scoping level"; no theorems, predictions, falsifiers, conjectures registered new; problem counts unchanged).

### Programme state changes at Patch 0482

- **OPEN-FP-SF-2-CHIR trajectory PROMOTED** from "registered open frontier at SF-2 v1.0 SHIP" (Patch 0370) to **"v3.0+ Layer 4 closure trajectory OPENED at scoping level"** (this patch).
- Status field in `research_frontier.md` updated to reflect v3.0+ trajectory opening with full scoping-sketch context.
- This problem-history file updated with v3.0+ trajectory pickup entry (this section).
- No theorems registered (scoping is Layer 1/Layer 2 epistemic status; theorem-level closure occurs at sub-claim (a)+(b)+(c) closure, estimated 11-17 sessions out).
- No predictions registered (substrate-level $|M^W| = \chi/6$ already registered as inherited from THEO-SD-CHIR-1).
- No falsifiers registered new (Capotauro v2.0 Falsifier 6 already in §13.4 ledger; activation under Layer 4 closure is closure consequence, not new registration).
- Problem counts UNCHANGED.

### Forward queue post-Patch 0482

1. **Priority 1 (immediate)**: Thomas's review of scoping sketch + route/venue decisions.
2. **Priority 2 (substantive work, post-route/venue decision)**: Sub-claim (a) bridge from substrate handle $|M^W| = \chi/6$ to chirality-sensitive coupling in continuum-limit effective Lagrangian; estimated 2-3 sessions.
3. **Priority 3 (background)**: SM-2 v2.0+ scoping at sketch level enabling potential Venue (c) joint-paper promotion.

### Anti-priorities preserved at Patch 0482

- Do NOT begin substantive Layer 4 derivation work before route/venue decisions are made.
- Do NOT skip the venue decision and default to within-flagship SF-2 v2.0+ extension (contradicts PD-004).
- Do NOT pursue Route (ii) substrate-mechanism as primary closure path absent Thomas's substantive reason.
- Do NOT modify SF-2 v1.0 paper text during Layer 4 closure work under Venue (b).
- Do NOT mix Layer 4 closure with sub-shell-physics work or other unrelated OPEN-FP-SF-2-* entries.

---

## Cross-Sector Parallel Analysis and Venue Recommendation Update (Session 136 Patch 0483)

**Date:** 19 May 2026
**Session:** 136 continuation (post-Patch 0482 SF-2 v3.0+ trajectory opening)
**Patch:** 0483

### What this update resolves

Patch 0482 (this file's prior section) opened the OPEN-FP-SF-2-CHIR v3.0+ Layer 4 closure trajectory at scoping level and surfaced two architectural decisions for Thomas's review — route choice (Route (i) canonical continuum-EFT recommended; Route (ii) substrate-mechanism alternative registered as cross-validation candidate) and venue choice (Venue (b) dedicated Layer 4 paper recommended; Venue (c) joint Layer 4 paper with SM-2 v2.0+ named as "recommended deferred option" pending cross-sector parallel analysis; Venue (a) within-flagship extension not recommended).

The **cross-sector parallel question was open at Patch 0482**: how structurally identical are the SF-2 v2.0+ V--A coupling Layer 4 closure (this trajectory) and the SM-2 v2.0+ chiral-polarity-bias Layer 4 closure (sibling trajectory inheriting from Capotauro v2.0 THEO-SD-CHIR-2)? The hedge in Patch 0482 sketch §4.4 (Venue (c) as "recommended deferred option") was honest acknowledgment that the parallel structure had not been analyzed at scoping level.

Patch 0483 resolves this question via a paired scoping sketch for the SM-2 v2.0+ trajectory ([`flagship_papers/electroweak/sketches/SM-2_chiral_polarity_bias_layer4_closure.md`](../flagship_papers/electroweak/sketches/SM-2_chiral_polarity_bias_layer4_closure.md); ~416 lines). The SM-2 sketch §4 cross-sector parallel analysis is the load-bearing analytical content of Patch 0483.

### Cross-sector parallel analysis result (SM-2 sketch §4)

**Shared infrastructure** between the two Layer 4 closures:

1. **Substrate handle magnitude**: $|M^W| = |M^{qDP}| = \chi/6 = \phi^{-3}/6 \approx 0.0394$ — *numerically identical* and structurally identical via three-way cross-sector unification under OPEN-SD-CHIR-PRIMITIVE umbrella.
2. **Substrate-handle-to-effective-coupling bridge step** (sub-claim (a) in both sketches): the bridge architecture is sector-agnostic; identified as **the load-bearing technical step** in both sectors. Doing it once vs. twice is the central efficiency question.
3. **Foundational input stack**: substrate-level FIs (FI-CHIR-1/2/3 in SF-2 sketch = FI-CPB-1/2/3 in SM-2 sketch) are **identical**. Substrate-object stabilizer FIs are sector-specific but structurally parallel.
4. **Cross-sector unification framing under OPEN-SD-CHIR-PRIMITIVE umbrella**: both closures land under the umbrella registered Patch 0422 Session 130; both close umbrella manifestations (manifestation (ii) electroweak V--A for SF-2; manifestation (iii) electromagnetic handedness for SM-2).
5. **PD-004 layer mapping**: both closures are Layer 4 continuum-EFT projection work; both require dedicated venue (within-flagship extension is precluded for both).

**Distinct infrastructure** between the two Layer 4 closures:

1. **Substrate object stabilizer**: SF-2 has W-bracelet with $D_6 = S_3 \times \mathbb{Z}_2$; SM-2 has Linear-ZBW antipodal pair $\{v_i, -v_i\}$ with $D_{5d} \subset I_h$ of order 20.
2. **$\zeta$ generator**: SF-2 has $\zeta^W$ = icosahedral-center inversion in 4D (purely geometric); SM-2 has $\zeta^{qDP}$ = combined $CP$ operation (spatial inversion + $\hat{n}$-flip + qCP-sign flip).
3. **Continuum-EFT framework**: SF-2 has Yang-Mills $SU(2)_L \times U(1)_Y$ EFT (inherited from EW-5 THEO-EW-8 thm:YM\_EFT at proof-outline level); SM-2 has effective free-energy / partition-function framework for substrate configurations (substrate stat-mech; no specific gauge-theory inheritance required).
4. **Observable kinematic structure**: SF-2 has Michel parameter $\rho = 3/4$ at finite mass + $100\%$ LH at massless helicity limit; SM-2 has stabilization energy $\Delta F^{qDP}$ at observable thermodynamic scales.
5. **Falsifier type**: SF-2 has Capotauro Falsifier 6 (V--A coupling deviation); SM-2 has positive down-type quark observation.

### Joint paper architecture and session budget

**Joint Layer 4 paper architecture** (5 sections):

- §A shared substrate-handle-to-effective-coupling bridge (sub-claim (a) for both sectors; 2-3 sessions; the load-bearing shared technical step).
- §B SF-2 sector closure (W-bracelet $D_6$ stabilizer; Yang-Mills EFT projection; Michel parameter $\rho = 3/4$; 3-5 sessions).
- §C SM-2 sector closure (Linear-ZBW antipodal pair $D_{5d}$ stabilizer; effective free-energy projection; $\Delta F^{qDP}$ exclusion bound; 3-5 sessions).
- §D cross-sector unification framing (paper's structural identity claim; 1-2 sessions).
- §E paper drafting + reviewer cycle + v1.0 SHIP (parallel to Capotauro v2.0 cycle; 5-7 sessions).
- §F joint paper v0.1 outline (decision gate before §A; 1 session).

**Total joint paper closure budget**: **15-22 sessions** (revised from Patch 0482 sketch §6 estimate of 15-25 sessions based on cleaner cross-sector parallel analysis).

**Compare to two separate dedicated papers (Venue (b))**: SF-2 dedicated Layer 4 paper 11-17 sessions + SM-2 dedicated Layer 4 paper 11-16 sessions = **22-33 sessions total**.

**Joint paper saves an estimated 7-11 sessions** primarily via shared bridge work and shared reviewer-cycle infrastructure.

### Venue recommendation update (Patch 0482 framing → Patch 0483 framing)

**Patch 0482 sketch §4.4 framing**: "Venue (c) joint Layer 4 paper with SM-2 v2.0+ chiral-polarity-bias closure (sibling Layer 4 work feeding from THEO-SD-CHIR-2 substrate handle $\chi/6$ on the qDP/eDP sector) ... recommended deferred option if SM-2 v2.0+ scoping work lands concurrently."

**Patch 0483 sketch §5.1 framing (UPDATED)**: "Venue (c) joint Layer 4 paper PROMOTED to recommended primary venue."

**Reasoning for the update**:

1. **Shared bridge step is load-bearing**: identified as the load-bearing technical step in both sector closures (SF-2 sketch §3.1 and SM-2 sketch §3.1). Joint paper does this work once instead of twice; estimated 7-11 session savings primarily from this efficiency.
2. **Cross-sector unification framing is structurally compelling**: joint paper foregrounds the OPEN-SD-CHIR-PRIMITIVE umbrella's three-way unification ($|M^{K3}| = |M^W| = |M^{qDP}| = \chi/6$) at Layer 4 closure level, completing the architectural arc that Capotauro v2.0 established at Layer 3.
3. **SF-4 v4.0 precedent**: CPP's first cross-sector closure paper demonstrates the methodological pattern works; joint Layer 4 paper establishes the second instance of cross-sector closure pattern in CPP.
4. **Joint paper viability is high**: cross-sector parallel analysis shows distinct infrastructure is sector-specific but tractable (no exotic machinery in either sector); risks are manageable with joint paper v0.1 outline as decision gate.

### Venue (b) two separate papers as structural fallback

If joint-paper v0.1 outline surfaces unanticipated technical obstructions (e.g., one sector's continuum-EFT framework requires substantively more infrastructure than initially scoped, or reviewer-expertise mismatch makes joint paper externally indefensible at one of the two sector closures), fall back to Venue (b) two separate dedicated Layer 4 papers:

- SF-2 v2.0+ dedicated Layer 4 paper: closes OPEN-FP-SF-2-CHIR via Yang-Mills EFT projection; 11-17 sessions.
- SM-2 v2.0+ dedicated Layer 4 paper: closes SM-2 v2.0+ chiral-polarity-bias via effective stat-mech projection; 11-16 sessions.

The scoping work (Patch 0482 sketch + Patch 0483 sketch) is **venue-portable** — the sub-claim decomposition, foundational input enumeration, and cross-sector parallel analysis are preserved regardless of joint-vs-separate venue choice.

### Patch 0483 deliverables

- NEW `flagship_papers/electroweak/sketches/SM-2_chiral_polarity_bias_layer4_closure.md` (~416 lines) opens SM-2 v2.0+ Layer 4 closure trajectory + resolves Patch 0482 cross-sector parallel question + updates venue recommendation.
- `research_frontier.md` Last-updated header prepended with Patch 0483 cross-sector parallel analysis + venue recommendation update milestone.
- `research_frontier.md` OPEN-FP-SF-2-CHIR Status field updated to reflect Venue (c) joint Layer 4 paper recommended primary venue per cross-sector parallel analysis result.
- `problem_histories/PH-OPEN-FP-SF-2-CHIR.md` Patch 0483 cross-sector parallel analysis update entry appended (this section).

**Per anti-priority discipline**: Patch 0482 sketch (`SF-2_chir_layer4_closure.md`) is NOT modified at Patch 0483; the venue recommendation update is registered in the Patch 0483 sketch §5 and forward-cross-referenced from the Patch 0482 sketch's §4.4 framing as historical record of the venue analysis state at scoping-sketch-pair opening.

### Programme state changes at Patch 0483

- **SM-2 v2.0+ chiral-polarity-bias closure trajectory OPENED at scoping level** (parallel to OPEN-FP-SF-2-CHIR trajectory opened Patch 0482).
- **Cross-sector parallel analysis result registered**: joint Layer 4 paper viability HIGH (shared bridge step is load-bearing; distinct infrastructure is sector-specific but tractable; joint paper saves 7-11 sessions).
- **Venue recommendation UPDATED**: Venue (c) joint Layer 4 paper PROMOTED from "deferred option" Patch 0482 framing to **"primary venue"** Patch 0483 framing.
- **Joint paper v0.1 outline scoping registered as Priority 1 next-substantive-work item** (Patch 0484 candidate; 1 session; joint-paper viability decision gate before substantive §A shared bridge work begins).
- No theorems, predictions, falsifiers, conjectures registered new. Problem counts UNCHANGED.

### Forward queue post-Patch 0483

1. **Priority 1 (immediate)**: Thomas's review of scoping-sketch pair (Patches 0482 + 0483) + joint paper venue confirmation (Venue (c) as recommended primary venue).
2. **Priority 2 (substantive work, post-venue-confirmation)**: Joint paper v0.1 outline scoping (Patch 0484 candidate; 1 session; joint-paper viability decision gate).
3. **Priority 3 (post-v0.1-outline-completion)**: §A shared substrate-handle-to-effective-coupling bridge work (sub-claim (a) closure for both sectors jointly; 2-3 sessions).

### Anti-priorities preserved at Patch 0483

- Do NOT begin substantive Layer 4 derivation work before venue confirmation + v0.1 outline completion.
- Do NOT default to Venue (b) two separate papers without v0.1 outline surfacing structural obstructions.
- Do NOT modify SF-2 v1.0 or SM-2 v1.0 paper text during Layer 4 closure work under Venue (c) joint paper.
- Do NOT mix joint paper scope with other unrelated OPEN-FP-SF-2-* entries (η, EWSB, loopfactor, shelldens, chaincomp) or other SM-series open problems.
- Do NOT modify Patch 0482 sketch (`SF-2_chir_layer4_closure.md`) at this patch; venue recommendation update is registered in Patch 0483 sketch §5 + research_frontier.md + this problem-history file only (per anti-priority discipline preserving Patch 0482 sketch as historical record of venue analysis state at scoping-sketch-pair opening).

---

## Joint Paper v0.1 Outline + Viability Decision Gate PROCEED Verdict (Session 137 Patch 0484)

**Date:** 20 May 2026
**Session:** 137 opening (post Patch 0483 cross-sector parallel analysis + Thomas's Session 136 Venue (c) confirmation)
**Patch:** 0484

### What this update establishes

Patch 0484 creates the joint Layer 4 paper home directory `flagship_papers/chirality_continuum/` under the Venue (c) confirmation established at Session 136 close (post-Patch 0483). The v0.1 outline serves as the joint-paper viability decision gate before substantive Layer 4 derivation begins.

### Patch 0484 deliverables

- **NEW directory** `flagship_papers/chirality_continuum/` created as joint paper home (sector-neutral name; follows Capotauro precedent of named-flagship-without-SF-N-number papers).
- **NEW** `flagship_papers/chirality_continuum/README.md` (~150 lines) — flagship-paper home-directory README with paper-type framing (joint Layer 4 continuum-EFT closure paper; second cross-sector closure paper in CPP after SF-4 v4.0), status (v0.1 outline OPENED), foundational inheritance (substrate handle $|M^W| = |M^{qDP}| = \chi/6$ from THEO-SD-CHIR-1 + THEO-SD-CHIR-2 at full Layer 3 rigor), source-material map, OPEN-FP problems closed at v1.0 SHIP, OPEN problems explicitly NOT-in-scope, viability decision gate framing.
- **NEW** `flagship_papers/chirality_continuum/chirality_continuum_outline.md` (~448 lines) — v0.1 outline document.
- **NEW** `flagship_papers/chirality_continuum/sketches/README.md` — placeholder for future joint-paper-specific sketches (paired scoping sketches at Patches 0482 + 0483 remain at historical locations under `flagship_papers/electroweak/sketches/`).
- **UPDATE** `research_frontier.md` Last-updated header prepended with Patch 0484 milestone + OPEN-FP-SF-2-CHIR Status field updated to v0.1 outline ACTIVE.
- **UPDATE** `problem_histories/PH-OPEN-FP-SF-2-CHIR.md` Patch 0484 v0.1 outline entry appended (this section).

### Joint paper provisional identity

- **Working title (v0.1):** *Cross-Sector Layer 4 Closure of the Substrate Chirality Handle: Electroweak V--A Coupling and Quark Chiral-Polarity-Bias from $|M| = \chi/6$*
- **Bibliography key (provisional; locked at v1.0 SHIP):** `abshier_chirality_continuum`
- **Authors (anticipated):** Thomas Lee Abshier ND + Claude Opus (Anthropic)
- **Target venues:** Zenodo (DOI primary) + arXiv hep-ph (if endorsement obtainable) at v1.0 SHIP; OSF deposit (DOI 10.17605/OSF.IO/JXE8D umbrella) at v1.0 SHIP per established programme practice.
- **Paper type:** Joint Layer 4 continuum-EFT closure paper; second cross-sector closure paper in CPP after SF-4 v4.0 (Session 72 Patch 0333 OPEN-FP-SF-4-2 + SM-5 op:nu\_id joint closure).
- **OPEN-FP problems closed at v1.0 SHIP (anticipated):** OPEN-FP-SF-2-CHIR (this trajectory) + SM-2 v2.0+ chiral-polarity-bias EFT continuum-limit (Linear-ZBW-on-$-$qCP stabilization energy at observable scales).

### v0.1 outline 10-section paper structure

- Abstract (§1.1)
- Plain-language summary (§1.2)
- §1 Introduction (positioning + problem statement + scope-limitation upfront)
- §2 Inheritance and foundational input enumeration (FI-CHIR-CONT-1 through FI-CHIR-CONT-14)
- §3 The shared substrate-handle-to-effective-coupling bridge (paper's §A; load-bearing shared content; sub-claim (a) closure for both sectors jointly)
- §4 W-bracelet sector closure: V--A coupling at observable scales (paper's §B; sub-claims (b)+(c)+(d) for SF-2; Yang-Mills EFT projection + Michel parameter $\rho = 3/4$ + massless-helicity-limit 100\% LH preference)
- §5 qDP/eDP sector closure: chiral-polarity-bias exclusion at observable scales (paper's §C; sub-claims (b)+(c)+(d) for SM-2; effective free-energy projection + stabilization energy calculation + exclusion bound + SM cross-validation)
- §6 Cross-sector unification under OPEN-SD-CHIR-PRIMITIVE umbrella (paper's §D; structural identity claim)
- §7 Predictions and falsifiers (5-row predictions table; 6 falsifiers including Capotauro Falsifier 6 + positive-down-type-quark-observation)
- §8 Open Theorem-Level Work (post-v1.0-SHIP sub-claims + OPEN-SD-CHIR-PRIMITIVE umbrella (iv)+(v) future-window + Route (ii) substrate-mechanism cross-validation candidate)
- §9 Discussion (programme-level methodological pattern + cross-sector implications + outlook 2026-2032+)
- §10 References (~25 bibliography entries combining CPP-corpus inheritance + external references)

### Foundational input merger from scoping sketches

The 14 FI-CHIR-CONT-N entries merge the scoping sketches' FI inventories:

- **Shared substrate-level FIs (FI-CHIR-CONT-1/2/3)**: merged from Patch 0482 sketch FI-CHIR-1/2/3 = Patch 0483 sketch FI-CPB-1/2/3 (substrate primitive 4D direction $\hat{n}$; substrate chirality magnitude $|\chi| = \phi^{-3}$; substrate residual symmetry $H_3 = I_h$).
- **Sector A specific FIs (FI-CHIR-CONT-4A through -8A)**: W-bracelet substrate-object characterization with $D_6$ stabilizer; $\zeta^W$ generator (icosahedral-center inversion in 4D); Yang-Mills EFT framework inherited from EW-5 THEO-EW-8 thm:YM\_EFT at proof-outline level; standard SM kinematic-projection machinery for muon decay.
- **Sector B specific FIs (FI-CHIR-CONT-4B through -8B)**: Linear-ZBW substrate-object characterization with antipodal-pair $D_{5d}$ stabilizer; $\zeta^{qDP}$ generator (combined $CP$ operation); SM-2 v1.0 chiral-polarity-bias mechanism statement; effective free-energy / partition-function framework for substrate configurations; standard SM fractional-charge structure + empirical absence of positive down-type quarks.
- **Cross-sector unification FIs (FI-CHIR-CONT-9/10/11/12)**: OPEN-SD-CHIR-PRIMITIVE umbrella context; substrate-locality theorem inheritance from Capotauro v2.0; PD-004 layer architecture mapping; SF-4 v4.0 cross-sector-closure-pattern precedent.

The merged FI inventory at 14 entries is at the upper end of the conditional-theorem-closure paper range (compare Capotauro v2.0 12 FIs + SF-4 v4.0 ~10 FIs) but within reasonable bounds for a flagship paper.

### §10 v0.1 outline viability decision gate result

The v0.1 outline is the load-bearing content of Patch 0484. Assessed against 5 viability criteria:

1. **Section structure coherence** — 10-section structure workable; shared content vs sector-specific content separation clean; cross-sector unification framing in §6 ties the two sector closures together substantively. **VERDICT: ✓ PASS**.
2. **FI inventory manageability** — 14 FIs at upper end but within bounds; sector-specific FIs clearly labeled (-A vs -B suffix). **VERDICT: ✓ PASS**.
3. **Cross-sector framing structural compellingness** — Capotauro v2.0 substrate-level three-way unification gives joint paper genuine structural identity; joint paper extends this unification to Layer 4 closure of two of three sector projections (third — mass-mixing K3-doublet — at substrate-level only without observable-scale projection in this paper's scope). **VERDICT: ✓ PASS**.
4. **Sector-specific complication risk** — both sectors technically tractable; SF-2's Yang-Mills EFT projection is the more demanding technical content but well-scaffolded by SF-2 v1.0 §sec:YM\_EFT\_thm proof outline; SM-2's effective stat-mech projection is standard machinery. **VERDICT: ✓ PASS**.
5. **Reviewer-audience coherence** — joint paper's reviewer audience is mathematical-physicists / Layer-4-bridge-specialists; audience coherent across both sector closures. **VERDICT: ✓ PASS**.

**Net assessment: all 5 viability criteria PASS. Joint paper viability HIGH. Recommendation: PROCEED TO v0.2 SUBSTANTIVE DRAFTING at Venue (c) joint Layer 4 paper.**

### Drafting plan and timeline

- v0.1 outline (this patch, Patch 0484): paper architecture established + joint-paper viability decision gate. 1 session.
- v0.2 §A shared bridge work (Patches 0485+): substrate-handle-to-effective-coupling bridge sub-claim closure. 2--3 sessions; load-bearing technical step.
- v0.3 §B SF-2 sector closure (Patches 0488+): Yang-Mills EFT projection + Michel parameter $\rho = 3/4$ + massless-helicity-limit 100\% LH preference. 3--5 sessions.
- v0.4 §C SM-2 sector closure (Patches 0492+): effective free-energy projection + stabilization energy calculation + exclusion bound + SM cross-validation. 3--5 sessions.
- v0.5 §D cross-sector framing + paper polish (Patches 0496+): §6 + §7 + §8 + §9 + abstract + plain-language summary + bibliography. 1--2 sessions.
- v0.6--v0.9 reviewer cycle (Patches 0498+): multi-reviewer convergence per Capotauro v2.0 + SF-2 v1.0 + SF-4 v1.0 precedent. 3--5 sessions.
- v1.0 SHIP (Patch 0503+): final polish + title block + CHANGELOG + four-tier documentation suite + programme-level registry updates. 1--2 sessions.

**Total estimated: 15--22 sessions** from this v0.1 outline lock to v1.0 SHIP. Within SF-line per-paper estimate (5--14 sessions) extended by joint-paper cross-sector content (additional 5--8 sessions vs. single-sector closure).

### Venue (b) fallback preserved

If during v0.2+ substantive drafting unanticipated structural obstructions surface (cross-sector framing surfaces as contrived during §6 drafting; reviewer-audience splits irreconcilably during v0.6+ reviewer cycle; one sector's continuum-EFT framework requires substantively more infrastructure than scoped at outline level), the fallback to Venue (b) two separate dedicated Layer 4 papers remains a structurally clean option per Patch 0483 sketch §5.2 framing. The v0.1 outline content is venue-portable — sub-claim decomposition, FI enumeration, theorem-statement structures all preserve under Venue (b) fallback. Venue (b) fallback triggered ONLY if structural obstructions are substantively unmistakable.

### Programme state changes at Patch 0484

- (1) Joint Layer 4 paper home directory `flagship_papers/chirality_continuum/` CREATED under Venue (c) confirmation.
- (2) v0.1 outline ESTABLISHED with 10-section architecture + 14-FI inventory + 5-criterion viability decision gate.
- (3) Joint-paper viability decision gate result: ALL 5 CRITERIA PASS → PROCEED TO v0.2 SUBSTANTIVE DRAFTING.
- (4) Next-substantive-work item registered: Patch 0485 candidate opens §A shared substrate-handle-to-effective-coupling bridge work.
- (5) Patches 0482 + 0483 scoping sketches PRESERVED at historical locations per anti-priority discipline.
- (6) NO theorems registered (outline establishes structure, not theorem-level content).
- (7) NO predictions registered new (substrate-level $|M^W| = |M^{qDP}| = \chi/6$ inherited from THEO-SD-CHIR-1 + THEO-SD-CHIR-2).
- (8) Capotauro Falsifier 6 registered as anticipated-activation-at-v1.0-SHIP for the SF-2 leg; positive-down-type-quark-observation analog registered as anticipated-activation for SM-2 leg.

### Forward queue post-Patch 0484

1. **Priority 1 (immediate next substantive)**: Patch 0485 candidate — §A shared substrate-handle-to-effective-coupling bridge work (sub-claim (a) closure for both sectors jointly); the load-bearing technical step; v0.2 substantive drafting opening; 2--3 sessions.
2. **Priority 2**: Patches 0488+ — §B Sector A V--A coupling derivation; v0.3 substantive drafting; 3--5 sessions.
3. **Priority 3**: Patches 0492+ — §C Sector B chiral-polarity-bias derivation; v0.4 substantive drafting; 3--5 sessions.
4. **Subsequent priorities**: Patches 0496+ (§D cross-sector + polish; v0.5); Patches 0498+ (v0.6--v0.9 reviewer cycle); Patch 0503+ (v1.0 SHIP).

### Anti-priorities sustained at Patch 0484

- Do NOT modify SF-2 v1.0 or SM-2 v1.0 or Capotauro v2.0 paper text during this joint paper's drafting.
- Do NOT mix joint paper scope with other unrelated OPEN-FP-SF-2-* entries or other SM-series open problems.
- Do NOT exceed joint-paper scope (bounded to OPEN-FP-SF-2-CHIR + SM-2 v2.0+ chiral-polarity-bias closure specifically).
- Do NOT modify Patches 0482 + 0483 scoping sketches at this patch (preserved at historical locations per anti-priority discipline).
- Do NOT trigger Venue (b) fallback absent substantively unmistakable structural obstructions during v0.2+ substantive drafting.

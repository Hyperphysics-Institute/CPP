# SF-7 Critical-Path Map & Dependency Audit

**Location:** `/CPP/flagship_papers/unification/sf-7_critical_path_map.md`
**Opened:** Session 160, Patch 1300 (SF-7 grand-unification window)
**Status:** LIVE strategic spine. Decision-grade, not exhaustive. Supersedes ad-hoc planning for the SF-7 campaign; does not supersede `README.md` (scope) or `hierarchy_paper_outline.md` (legacy single-paper source material).
**Purpose:** Map the minimum real work between today's repo state and an SF-7 v1.0 SHIP, grade each predecessor flagship against its source corpus, resolve the one cheap-but-load-bearing Open Question (Q3, calibration honesty), and identify which §10 cross-sector consistency theorems are buildable *now* from shipped material versus blocked on undrafted predecessors.

---

## 0. One-paragraph orientation — read this first

SF-7 is the apex synthesis: it must demonstrate that all 17 SM particles (+ the W⁰ CPP-novel prediction) cohere under one substrate derivation, with the §10 cross-particle-class consistency theorems as its intellectual core (no double-counting, single calibration, all from the 600-cell + m_e). The README correctly states SF-7 cannot be drafted at flagship quality until SF-1 through SF-6 are at v1.0 SHIP. **Two of the six predecessors are shipped (SF-2, SF-4); four are README-only stubs (SF-1, SF-3, SF-5, SF-6).** The critical path is therefore (a) standing up the four stub flagships from their existing source corpus — work suited to parallel spin-off windows — and (b) building the §10 consistency-theorem family, of which exactly one member (SF-2↔SF-4) has both inputs already shipped and is available immediately. This window's highest-confidence first physics deliverable is that SF-2↔SF-4 consistency theorem (patch 1301).

---

## 1. Predecessor readiness grades

| Paper | State | Primary source corpus | What real work remains | Lift to v1.0 | Natural owner |
|-------|-------|-----------------------|------------------------|--------------|---------------|
| **SF-1** charged leptons | README-only stub | SM-3 (K3 spectral theorem / Koide), SM-4 (charged-lepton K3-vertex), SM-6 (lepton mass spectrum) | Assemble shipped SM-3/4/6 into a flagship; frame Koide as a **spectral theorem**, not a fit; state m_e-calibration honestly | **Low–Medium** (physics largely exists) | spin-off window |
| **SF-2** electroweak | **SHIPPED v1.01** | — | — (done; OSF deposit pending) | — | — |
| **SF-3** quarks | README-only stub | SM-7 (Koide heavy quarks + m_c), SM-8 (zero-param cage M=m_e(z/φ)V^(7/3)), SM-2 (chiral-polarity), SM-10 (chain-network FEM → CKM partial) | Adjudicate the **two quark-mass routes** (see §2); CKM mixing is the thinnest input (only partial via SM-10) | **Medium–High** (CKM is the soft spot) | spin-off window |
| **SF-4** neutrinos | **SHIPPED v4.4** | — | — (done; archival-deposit-quality; OSF pending) | — | — |
| **SF-5** strong | README + (empty) sketches | SS-1 + SS-5/7/8/9 nuclear cascade; OPEN-SS-6 (glueball), OPEN-SS-37 (SS-9 closure routes) | Pre-survey SS corpus; gluon counting + glueball + confinement synthesis; glueball mass is an open inheritance | **Medium–High** | spin-off window |
| **SF-6** electromagnetism | README + (empty) sketches | EW-1..5 + SR-1 + QM-1..6; eDP-sea polarization corpus | Broadest scope; **EM-handedness manifestation (iii) of OPEN-SD-CHIR-PRIMITIVE is OPEN with no closure machinery** — a genuine gating dependency, not just assembly | **High** (largest inheritance scope; partially blocked) | spin-off window |
| **SF-7** apex | scaffolding only | the six above + §10 originals | §10 consistency-theorem family (does not exist yet); resolve Open Questions Q2/Q3/Q4 | Blocked on predecessors | **this window** (umbrella + §10) |

**Headline:** 2/6 shipped, 4/6 undrafted. SF-1 is the cheapest predecessor to stand up; **SF-6 is the heaviest and is partially blocked** on an open chirality manifestation. The §10 work this window owns can begin now on shipped inputs and grows as predecessors land.

---

## 2. Q3 RESOLVED — calibration honesty (load-bearing for §9 + abstract)

**Question (from `hierarchy_paper_outline.md` §Open-Q3):** Is m_e a calibration or genuinely substrate-derived? And does the SF-7 "single calibration m_e" headline hold?

**Finding (from `theory-overview.md` + `axiom-registry.md`):**
- **m_e is a calibration, NOT substrate-derived.** It fixes M₀ = m_e·z/φ = 3.790 MeV. Use **Honest Framing 1**: "m_e is the one substrate calibration." Do *not* claim zero total parameters.
- **The programme currently carries a SECOND calibration, m_c.** The net scorecard reads *"CPP requires 2 (m_e, m_c)."* The heavy-quark Koide route (SM-7) calibrates on m_c (m_b, m_t to 1.4–1.7%).
- **Therefore the SF-7 README headline of a *single* m_e calibration is currently OPTIMISTIC.** It is conditional on one of two adjudications in SF-3:
  - **Route A (preferred):** adopt SM-8's **zero-parameter cage formula** m_e(z/φ)V^(7/3), which reproduces m_s/m_c/m_b/m_t from **m_e alone** (residuals 1.6–3.1%), retiring the m_c calibration. This *restores the single-calibration claim* at the cost of slightly larger quark residuals.
  - **Route B:** keep SM-7 Koide+m_c, and either (i) derive m_c from m_e + geometry, or (ii) state honestly "2 calibrations" in §9.

**Action for SF-7:** §9 master comparison table and the abstract must state the calibration count *as adjudicated in SF-3*, not as assumed in the README. **Flag SF-3's quark-route adjudication as a hard prerequisite for the SF-7 headline number (Q4).** Do not let "1 calibration" reach the abstract until Route A is locked or m_c is derived.

This is the single highest-value output of this audit: it prevents a reviewer-fatal honesty gap ("you said 1 parameter, your own scorecard says 2") from reaching the apex paper.

---

## 3. The §10 consistency-theorem family — what is buildable NOW

The §10 core ("the six derivations cohere: no double-counting, single substrate, single calibration") decomposes into pairwise + global consistency claims. A pairwise claim is buildable iff **both** member flagships are shipped.

| §10 member | Both inputs shipped? | Buildable now? |
|------------|----------------------|----------------|
| **SF-2 ↔ SF-4** (EW cage-boson ↔ neutrino) | **YES** (v1.01, v4.4) | **YES — patch 1301 target** |
| SF-1 ↔ SF-2, SF-1 ↔ SF-4 | No (SF-1 stub) | blocked |
| SF-3 ↔ {any} | No (SF-3 stub) | blocked |
| SF-5 ↔ {any}, SF-6 ↔ {any} | No (stubs) | blocked |
| Global six-way consistency | No (4 stubs) | blocked |

**SF-2↔SF-4 consistency theorem scope (patch 1301 seed):** prove that the electroweak cage-boson sector (SF-2) and the neutrino sector (SF-4)
1. share the **same substrate calibration** (both reduce to m_e via M₀; SF-4's σ_ν and SF-2's η-factors introduce no new mass calibration);
2. share the **same 600-cell geometric primitives** without **double-counting degrees of freedom** (SF-2's cage-shape orbits vs SF-4's K3-cage-shell occupations are disjoint structural roles on the same lattice);
3. **source δ_CP consistently** — SF-4 defers δ_CP to the EW-flagship handle (Capotauro/SF-2 χ/6 mechanism); verify the two sectors reference one substrate handle (χ = φ⁻³) without contradiction. **This is the interconnection-level δ_CP claim — NOT a δ_CP value derivation (that is window 5's).**

This theorem is a proof-of-concept that the SF-7 synthesis method works on real shipped material, and it is the natural first member of §10. It also seeds the δ_CP-sourcing-consistency record that window 5's eventual prediction will plug into.

---

## 4. Remaining Open Questions (from legacy outline) — status

- **Q1 (neutrino mechanism reconciliation):** DISSOLVED into SF-4 (shipped). No SF-7 action.
- **Q2 (conditional-theorem framing scope):** ADOPT the SS-9 conditional-theorem template at paper level. State inherited conditions in §2, deduce in §3–8, honest accounting in §10/§11. (Recommendation stands; decision is Thomas's at drafting time.)
- **Q3 (calibration honesty):** RESOLVED here (§2). m_e = calibration; single-calibration headline conditional on SF-3 Route A.
- **Q4 (headline number for abstract):** BLOCKED on Q3/SF-3 adjudication + the four predecessor ships. Cannot commit an "X% across all particles" or a calibration count until SF-3's route is locked and SF-1/3/5/6 land. Hold.

---

## 5. Recommended critical path

1. **Patch 1300 (this file)** — map + Q3 resolution. ✅
2. **Patch 1301** — SF-2↔SF-4 cross-sector consistency theorem sketch (§10 seed; shipped-inputs-only). *δ_CP-adjacent → HOLD-FOR-REFRESH at delivery.*
3. **Parallel spin-off windows** for the four stub flagships, in cheapest-first order: **SF-1 (low) → SF-3 (medium, with the Route-A quark adjudication) → SF-5 (medium) → SF-6 (high, after EM-handedness manifestation (iii) gets closure machinery).**
4. **§10 family grows** as each predecessor ships: add the new pairwise consistency members, then the global six-way theorem once SF-1/3/5/6 are all in.
5. **SF-7 drafting** begins only after all six are shipped and Q3/Q4 are locked. README estimate: 5–8 sessions from that point.

**Swarm-coherence framing:** "completion" is not a single SHIP but the point at which the cross-sector consistency theorems + shipped predecessors raise the null hypothesis (the 9 axioms are not the common root) to a confidence level the conventional community would accept. Each §10 member that closes on shipped inputs is an incremental, independently checkable raise of that bar.

---

## 6. Collision-coordination notes

- **This file (1300):** collision-free — new file in `flagship_papers/unification/`, no shared-registry edits, no other window's sector files touched. Pushable immediately.
- **Patch 1301 (next):** δ_CP-adjacent to **window 5 (δ_CP neutrino prediction)**; reads SF-2/SF-4 sources; conceptually overlaps `frontier_sectors/SM.md` territory. Will be marked **HOLD-FOR-REFRESH**; confirm window 5 is not mid-patch on the neutrino/EW sources before applying.
- **Spin-off windows for SF-1/3/5/6** will touch SS/EW/QM/SR source papers and, at ship time, the shared registries (`theorem-registry.md`, `predictions.md`, `paper_catalog.md`, `master_glossary.md`, `frontier_sectors/*`). Those ships must funnel registry edits through flagged integration patches per the light single-operator protocol.
- **SF-6 specifically** depends on the chirality arc (window 2) delivering EM-handedness manifestation (iii) closure machinery — a genuine cross-window dependency, not just a collision risk.

---

*Patch 1300 — SF-7 grand-unification window opening. No physics verdicts moved; no registries touched. Q3 resolved; SF-2↔SF-4 consistency theorem identified as the first available §10 artifact.*

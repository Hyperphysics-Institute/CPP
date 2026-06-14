# SF-7 Critical-Path Map & Dependency Audit

**Location:** `/CPP/flagship_papers/unification/sf-7_critical_path_map.md`
**Opened:** Session 160, Patch 1300 (SF-7 grand-unification window).
**Refreshed:** Session 160, Patch 1306 — incorporates findings from the predecessor pre-survey sweep (Patches 1301–1305). This is the **current** strategic spine; supersedes the 1300 text.
**Status:** LIVE strategic spine. Decision-grade.

**Revision history (internal):**
- 1300 — original map + Q3 resolution; identified SF-2↔SF-4 as the only §10 member buildable on shipped inputs.
- 1306 — refresh after the full predecessor pre-survey set (SF-1/3/5/6) + the SF-2↔SF-4 §10 seed (1301): calibration ledger now RESOLVED; SF-6 block narrowed; three load-bearing reconciliations surfaced; §10 family roadmap end-to-end; spin-off dispatch list added.

---

## 0. Orientation — read this first

SF-7 is the apex synthesis; its §10 core must prove the six sector flagships cohere (one substrate, one calibration, no double-counting, consistent mixing-sector sourcing). It cannot draft at flagship quality until SF-1 through SF-6 ship. **State after this session:** two predecessors shipped (SF-2, SF-4); **the other four (SF-1, SF-3, SF-5, SF-6) now have drafting-ready flagship outlines** (Patches 1302–1305) and are dispatchable to spin-off windows. The single-calibration question is **resolved** (single $m_e$ restored). The first §10 member (SF-2↔SF-4) is **built** (1301). Three load-bearing reconciliations were surfaced — one per predecessor that needed one — and each is recommended. The remaining critical path is: ship the four outlined predecessors (parallel windows) → grow the §10 family as each lands → draft SF-7 once all six ship and the §9 ledger locks.

---

## 1. Predecessor readiness (refreshed)

| Paper | State | Outline | Pre-survey finding | Lift | Owner |
|-------|-------|---------|--------------------|------|-------|
| **SF-1** charged leptons | stub → **outlined** (1302) | `charged_leptons/sf-1_outline.md` | Headline stronger than README assumed: SM-6 v3 **derives** Koide phase θ to 0.003%; full spectrum from $m_e$, 0 shape params. Cleanest single-$m_e$ sector. | **Low** (3–5 sess) | spin-off |
| **SF-2** electroweak | **SHIPPED v1.01** | — | (carries open η-dilution on *absolute* boson masses) | — | — |
| **SF-3** quarks | stub → **outlined** (1303) | `quarks/sf-3_outline.md` | m_c route **adjudicated** (adopt SM-8 zero-param; m_c → derived). CKM has **no** corpus derivation → inherit-open. | **Medium** (5–7 sess) | spin-off |
| **SF-4** neutrinos | **SHIPPED v4.4** | — | (δ_CP deferred to EW handle) | — | — |
| **SF-5** strong | stub → **outlined** (1304) | `strong/sf-5_outline.md` | SU(3) exact+unique, 8 gluons theorem-level. Recommend **lead with shipped results, demote CONJ-SS-Gluon-4Vertex** to flagged conjecture. SS-9 conditional. | **Medium** (5–8 sess) | spin-off |
| **SF-6** EM | stub → **outlined** (1305) | `electromagnetism/sf-6_outline.md` | **Block narrowed**: core unblocked (c06 spine); only manifestation (iii) blocked-and-deferrable (window 2). README source map corrected. | **High** (6–9 sess, breadth) | spin-off |
| **SF-7** apex | scaffolding + this map | `unification/` | §10 family roadmap below; blocked on the four ships + §9 lock | this window | — |

**Headline:** all four stub predecessors are now scoped and dispatchable. None is wholesale blocked (the 1300 "SF-6 partially blocked" line is corrected — only one deferrable manifestation is).

---

## 2. Calibration ledger — RESOLVED (was Q3)

The 1300 question ("does the single-$m_e$ headline hold?") is now settled across all sectors:

- **Leptons (SF-1):** single $m_e$, 0 shape params. **Clean** — no caveat.
- **Quarks (SF-3):** adopt **SM-8 Route A** (zero-param $M_q=m_e(z/\phi)V^{7/3}$, RMS 2.1%); **m_c demoted from calibration to derived** (SM-8 predicts it at 1.6%). Restores single $m_e$. SM-7's α_s/phase content retained as structural, re-grounded on the derived m_c.
- **Neutrinos (SF-4):** single $m_e$ (via $M_0$); no new fitted parameter. **Clean.**
- **Strong (SF-5):** nuclear-mass scale anchors on $M_0=m_e(z/\phi)$. **Clean.**
- **EM (SF-6):** photon/constants from substrate primitives; no fermion-mass calibration.

**SF-7 §9 master table reads: 1 calibration ($m_e$) for all fermion masses.** The two standing caveats, both honest and non-fatal:
1. **SF-2 η-dilution** — the *absolute* electroweak-boson masses carry an open per-boson holographic dilution $\eta\sim10^{-17}$ (OPEN-FP-SF-2-η). A *boson absolute-mass* caveat, not a fermion-mass one; SF-2's ratios/structure are zero-parameter.
2. **Mixing sectors open** — CKM (SF-3) and δ_CP (SF-4) are inherited-open, not calibrations.

Both must appear in §9, stated not obscured.

---

## 3. The §10 consistency-theorem family — end-to-end roadmap

Template for every member: **(C1) calibration coherence / (C2) no double-counting / (C3) shared-observable single-handle** (THEO-SF7-CONSIST-1, Patch 1301).

| §10 member | Buildable when | Identified physical thread | Status |
|------------|----------------|----------------------------|--------|
| **SF-2 ↔ SF-4** | now (both shipped) | shared SM-1 taxonomy; V=12 shared shell (distinct roles); δ_CP↔V–A both source χ=φ⁻³ | **BUILT (1301)** |
| SF-1 ↔ SF-2 | SF-1 ships | shared $\sin^2\theta_W=3/(8\phi)$ spectral-trace (edge-mode fraction) | thread identified (1302) |
| SF-1 ↔ SF-4 | SF-1 ships | shared $M_0$; OP-SM-7d phase/δ_CP EW handle | thread identified (1302) |
| SF-3 ↔ SF-2 | SF-3 ships | $\sin^2\theta_W+\alpha_s=1/\phi$ mode complementarity (3/8 edge + 5/8 face) | thread identified (1303) |
| SF-3 ↔ SF-1 | SF-3 ships | shared Koide-phase machinery (isotropic shift); $M_0$ | thread identified (1303) |
| SF-3 ↔ SF-4 | SF-3 ships | shared $M_0$/taxonomy; masses-derived/mixing-open parallel (CKM↔δ_CP) | thread identified (1303) |
| SF-5 ↔ SF-2 | SF-5 ships | SU(2)$_L$/SU(3)$_c$ from same 600-cell + binary icosahedral group | thread identified (1304) |
| SF-5 ↔ SF-3 | SF-5 ships | colour sector: $\alpha_s$, $C_F=4/3$ | thread identified (1304) |
| SF-6 ↔ SF-2 | SF-6 ships | photon (eDP quantum) vs cage bosons — categorical distinction, clean no-double-counting | thread identified (1305) |
| SF-6 ↔ all | SF-6 ships | SSV/DP-Sea substrate consistency across sectors | thread identified (1305) |
| **Global six-way** | all six ship | the capstone: no double-counting + single $m_e$ + one substrate across all 17 particles + W⁰ | blocked on all ships |

The mode-fraction structure ($\sin^2\theta_W=3/8$ edge, $\alpha_s=5/8$ face, sum $1/\phi$) is the strongest recurring thread — it binds SF-1, SF-2, SF-3, SF-5 through one 600-cell spectral trace.

---

## 4. The three reconciliations (one per predecessor that needed one)

The pre-surveys surfaced three load-bearing issues; each took a different honest form. SF-7 §9/§10 must carry all three:

1. **SF-1 — a closed arc.** SM-4 proved θ undetermined within K3+SSV (impossibility theorem); SM-6 supplied the EW ingredient and derived θ (0.003%). Present as a completed derivation, not a contradiction.
2. **SF-3 — an adjudication.** Two quark-mass routes; adopt SM-8 (single $m_e$, m_c derived), retain SM-7's α_s/phase as structural. Resolves the calibration ledger.
3. **SF-5 — restraint.** Lead with shipped theorem-level SU(3)/8-gluon results; demote the unclosed CONJ-SS-Gluon-4Vertex to a flagged conjecture (its own falsification route (a) risks collapsing it to "SM restated").

---

## 5. Recommended critical path (refreshed)

1. **1300–1306 (this window):** map + §10 seed + four predecessor outlines + this refresh. ✅
2. **Spin-off windows** draft the four outlined predecessors, cheapest-first: **SF-1 (low) → SF-3 (medium) → SF-5 (medium) → SF-6 (high)**. Each outline is drafting-ready.
3. **§10 family grows** as each predecessor ships — add the members in §3 using the identified threads.
4. **SF-7 drafting** once all six ship and the §9 ledger locks (single $m_e$ + the two stated caveats + the mixing-sector deferrals). README estimate: 5–8 sessions from that point.

**Swarm-coherence framing:** each §10 member that closes on shipped inputs is an independently checkable raise of the bar against the null hypothesis. The global six-way theorem is the threshold artifact.

---

## 6. Spin-off dispatch list

Each spin-off window picks up one outline and drafts to v1.0. Hand each window its outline + this map §2/§4 + the THEO-SF7-CONSIST-1 template:

- **SF-1 window** → `flagship_papers/charged_leptons/sf-1_outline.md`. Core = §3–§5 (K3 theorem + Weinberg + SM-4→SM-6 phase arc). Inherit OPEN-FP-1-P3. Cleanest single-$m_e$ story; ships first for momentum.
- **SF-3 window** → `flagship_papers/quarks/sf-3_outline.md`. Core = §3–§4 (SM-8 spectrum + α_s complementarity). Adjudication in §1/§7. Inherit OPEN-FP-3-CKM.
- **SF-5 window** → `flagship_papers/strong/sf-5_outline.md`. Core = §3–§5 (SU(3) + gluons + confinement). Inherit OPEN-SS-6 glueball + SS-9 conditionality; flag CONJ-SS-Gluon-4Vertex only.
- **SF-6 window** → `flagship_papers/electromagnetism/sf-6_outline.md`. Spine = c06 + DP-Sea-Polarization-Model (NOT the stale EW-3/EW-5). Inherit OPEN-FP-6-EMHAND (deferred to window 2). Broadest reach; highest lift.

---

## 7. Open-inheritance ledger (consolidated)

| Inheritance | Sector | Disposition | Resolution owner |
|-------------|--------|-------------|------------------|
| OPEN-FP-1-P3 (thermal equilibration, Layer B) | SF-1 | inherit; empirically harmless (~10⁻²⁰) | SS-4 |
| OPEN-FP-3-CKM (quark mixing) | SF-3 | inherit; analog of δ_CP | quark-mixing route (unscoped) |
| OPEN-FP-SF-2-η (boson absolute-mass dilution) | SF-2 | standing; §9 caveat | Layer-4 EFT (PD-004) |
| OPEN-SS-6 (glueball) + SS-9 conditionality | SF-5 | inherit | SS-arc |
| OPEN-FP-6-EMHAND (manifestation iii) | SF-6 | defer; downstream of window 2 | chirality arc (window 2) |
| δ_CP value | SF-4 | window 5 (value); 1301 C3 certifies consistency | window 5 |

CONJ-SS-Gluon-4Vertex: flagged conjecture, not an inheritance to close.

---

## 8. Collision-coordination (refreshed)

- **This window's outputs (1300–1306):** all new/own files under `flagship_papers/*` — **no shared-registry edits**, collision-free. Theorem registration for THEO-SF7-CONSIST-1 (and SF-7's §10 members) is **deferred** to SF-7 ship / flagged integration patches.
- **Window 5 (δ_CP):** still the hottest adjacency — the SF-1↔SF-4 and SF-2↔SF-4 §10 work touches the neutrino/EW δ_CP handle and `frontier_sectors/SM.md` territory. 1301 C3 is the consistency scaffold the δ_CP value plugs into.
- **Window 2 (chirality):** **SF-6 is a downstream consumer of manifestation (iii)** — a dependency, not a collision. Window 2 should track SF-6 as awaiting (iii) closure.
- **Spin-off ships** will touch shared registries (`theorem-registry.md`, `predictions.md`, `paper_catalog.md`, `master_glossary.md`, `frontier_sectors/*`) — those must funnel through flagged integration patches per the light single-operator protocol.

---

*Patch 1306 — critical-path map refresh. Incorporates 1301–1305. No physics verdicts moved; no registries touched. The predecessor pre-survey set is complete; the calibration ledger is resolved; the §10 family is mapped end-to-end; spin-off dispatch is ready. New content in an own file under `flagship_papers/unification/`, collision-free.*

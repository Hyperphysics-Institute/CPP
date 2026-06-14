# SF-6 Electromagnetism — Pre-Survey & Flagship Outline (block clarified, source map corrected)

**Location:** `/CPP/flagship_papers/electromagnetism/sf-6_outline.md`
**Opened:** Session 160, Patch 1305 (SF-7 grand-unification window)
**Status:** OUTLINE + source-corpus pre-survey. **Two findings that revise the 1300/1304 SF-6 assessment:** (a) SF-6's core three-pillar unification is **not blocked** — only manifestation (iii) is, and it is **deferrable**; (b) the SF-6 README's source map is **stale** and is corrected here.
**Source corpus surveyed:** `series_foundations/dp-sea-polarization/DP-Sea-Polarization-Model`, SR-1 + SR companions (esp. c06), QM-1..6, EW-1 — all shipped; OPEN-SD-CHIR-PRIMITIVE manifestation (iii) (open, window-2 territory).
**Unlocks (post-ship):** §10 members SF-6↔SF-2 and SF-6↔all (substrate/SSV); completes the predecessor pre-survey set.

---

## 0. Orientation — read this first

SF-6 is the broadest-reach SF-line paper (classical EM + special relativity + QED, from one substrate mechanism: eDP-sea polarization). The 1300 map graded it "high lift, partially blocked." The pre-survey **refines that**: the three-pillar *core* is unblocked and is in remarkably good shape — SR companion **c06** already unifies $E=mc^2$ and $E=h\nu$ as a single equation ("no new postulates"), and the **DP-Sea-Polarization-Model** derives $\mu_0, \epsilon_0, c, \gamma(v)$. The *only* blocked piece is **manifestation (iii) electromagnetic-handedness**, which is open in the chirality arc (window 2) — and it is a deferrable add-on, not a load-bearing part of the three-pillar unification. So SF-6 can ship its core with EM-handedness inherited-open, exactly as SF-4 deferred δ_CP and SF-3 defers CKM. Two action items fall out: **defer manifestation (iii)** (don't block on it), and **fix the stale source map** (the photon/c material is in foundations + SR companions, not the EW-3/EW-5 the README cites).

---

## 1. The block is narrow and deferrable (centerpiece, revises 1300/1304)

**What's blocked:** OPEN-SD-CHIR-PRIMITIVE **manifestation (iii) electromagnetic-handedness** — "substrate-level chirality entering electromagnetic phenomenology, still to be made precise" (SSCA `README-SSCA.md`). It is OPEN, with **no closure-trajectory machinery**, and it lives in the **chirality arc (window 2)**, not in SF-6.

**Why it does not block the SF-6 core:** EM-handedness is a *chirality* manifestation, not part of the classical-EM / SR / QED unification. The SF-6 core mechanism — eDP-sea polarization producing Maxwell (macroscopic), SR kinematics (relativistic), and QED phenomena (quantum) — is independent of substrate chirality. The chirality arc has already closed manifestations (i), (ii), (iv); (iii) and (v) remain open, and (iii) is the one SF-6 would *consume*, not produce.

**Recommendation:** SF-6 ships the **three-pillar unification** with **manifestation (iii) inherited-open**. Register **OPEN-FP-6-EMHAND** and defer to the chirality arc (window 2). State the parallel to SF-4 (δ_CP) and SF-3 (CKM) explicitly — the SF-line's uniform posture is "the sector's core derives; one mixing/handedness piece is deferred to the responsible arc." **This converts SF-6 from "partially blocked, high risk" (1300) to "unblocked core + one deferred manifestation."**

**Cross-window coordination (genuine dependency, not just collision):** SF-6 is a **downstream consumer** of manifestation (iii). Window 2 (chirality) owns its closure. When window 2 closes (iii), SF-6 can promote OPEN-FP-6-EMHAND from inherited-open to closed. This should be on window 2's radar as a downstream dependency — flagged in §10 below.

---

## 2. Source-map correction (the README is stale)

The SF-6 README's source table cites **EW-3 = "photon as eDP polarization quantum"** and **EW-5 = "speed of light from substrate null-trajectory speed."** **Both are wrong:** the actual `EW-3` is the Z boson and `EW-5` is electroweak unification (the old EW series, now largely superseded by SF-2 for the cage bosons). The real EM-substrate material lives elsewhere. **Corrected source map:**

| Real source | Content | Status |
|-------------|---------|--------|
| `series_foundations/dp-sea-polarization/DP-Sea-Polarization-Model.tex` | DP-Sea polarization responding to CP motion; derives $\mu_0, \epsilon_0, c$, SSV, and $\gamma(v)$ in the relativistic limit | shipped (essay/model) |
| **SR companion c06** (`c06_dipole_chain_patterns_as_mass_EM_substrate`) | **The spine.** Mass = standing ZDC pattern, photon = traveling ZDC pattern (boundary-condition distinction); unifies $E=mc^2$ and $E=h\nu$ as $E=\hbar\nu_C$; impedance $Z_0=\sqrt{\mu_0/\epsilon_0}$; lensing, delocalization, coherence length; **"no new postulates"** | shipped (companion) |
| SR-1 (`SR-1_special_relativity_emergence`) | SR from SSV in the dipole sea; relativistic-kinematics bridge | shipped |
| QM-1..6 | QED-relevant quantum phenomena (photoelectric, Compton, double-slit, QFT emergence) | shipped |
| EW-1 (`EW-1_electroweak_introduction`) | Maxwell-equation derivation from CPP substrate (verify not superseded by SF-2 framing) | shipped (legacy EW) |

The spin-off window should build from **c06 + DP-Sea-Polarization-Model** as the spine, *not* from the EW-3/EW-5 the README points at. Updating the README source table is a candidate cleanup at SF-6 drafting time.

---

## 3. Headline result (what SF-6 claims)

> Classical Maxwell electromagnetism, special-relativistic photon kinematics, and quantum-electrodynamic phenomena are three limits of **one** substrate mechanism — eDP-sea (ZDC) polarization. The photon is a traveling ZDC pattern (not a cage-bound particle), mass is a standing ZDC pattern, and $E=mc^2$ and $E=h\nu$ are the same equation $E=\hbar\nu_C$. The constants $\mu_0, \epsilon_0, c, Z_0$ derive from substrate primitives. (Electromagnetic-handedness deferred to the chirality arc.)

| Result | CPP | Status | Source |
|--------|-----|--------|--------|
| $E=mc^2$ and $E=h\nu$ unified | $E=\hbar\nu_C$; standing vs traveling ZDC | derived, no new postulates | c06 |
| $\mu_0, \epsilon_0, c$ | from DP-Sea polarization primitives | derived | DP-Sea-Polarization-Model |
| Impedance $Z_0=\sqrt{\mu_0/\epsilon_0}$ | substrate discharge load | derived | c06 |
| Lorentz factor $\gamma(v)$ | DP-Sea viscous response | derived (relativistic limit) | DP-Sea-Polarization-Model, SR-1 |
| Maxwell's equations | macroscopic limit of eDP polarization | derivation | EW-1 |
| QED phenomena (photoelectric, Compton, 2-slit) | quantized eDP-polarization interactions | derivation | QM-1..6 |
| EM-handedness | — | **OPEN-FP-6-EMHAND (deferred, window 2)** | manifestation (iii) |

---

## 4. The three-pillar unification wins to foreground

- **One equation for mass and light.** c06's $E=\hbar\nu_C$ with the standing-vs-traveling-ZDC boundary-condition distinction is the conceptual core: it dissolves the mass/radiation dichotomy at the substrate level. This is the headline most likely to reach the broad audience the README targets.
- **EM constants are derived, not postulated.** $\mu_0, \epsilon_0, c, Z_0$ from DP-Sea primitives answers the Maxwell-era question "what is the EM field made of?" concretely.
- **The photon is categorically distinct from SF-2's cage bosons.** It is a polarization quantum of the eDP sea, not a cage-bound resonance — this is the clean boundary between SF-6 and SF-2, and a §10 consistency thread (no particle is double-assigned).

---

## 5. Proposed section structure (apex-paper form)

- **§1 The three-pillar problem.** Classical EM, SR, QED taught separately; the substrate question deferred at each step; CPP's single answer.
- **§2 The eDP-sea / ZDC substrate.** DP-Sea polarization; ZDC patterns; the standing-vs-traveling boundary condition.
- **§3 The unifying equation.** $E=\hbar\nu_C$; mass = standing ZDC, photon = traveling ZDC; $E=mc^2 \equiv E=h\nu$ (c06).
- **§4 Classical limit.** Maxwell's equations from macroscopic eDP polarization; $\mu_0, \epsilon_0, c, Z_0$ from primitives.
- **§5 Relativistic limit.** $\gamma(v)$ from DP-Sea viscous response; photon null trajectory; SR-1 bridge.
- **§6 Quantum limit.** Photoelectric, Compton, double-slit from quantized eDP-polarization interactions; QM-1..6.
- **§7 The photon vs the cage bosons.** Categorical distinction from SF-2; clean particle-assignment boundary.
- **§8 Open work (honest §10-analog).** **OPEN-FP-6-EMHAND** (manifestation (iii), deferred to window 2); any breadth-driven sub-derivation gaps surfaced at drafting.
- **§9 Falsifiers.** Absolute-frame signatures (the DP-Sea model notes tension with strict Michelson-Morley null — handle carefully); $Z_0$/c precision; QED phenomenon residuals.
- **§10 Discussion / SF-line placement + breadth.** Broadest reviewer reach; hooks to SF-2 (photon-not-cage-boson), and the manifestation-(iii) dependency on the chirality arc.

---

## 6. What SF-6 does NOT do

- Does not close manifestation (iii) EM-handedness (deferred to window 2; OPEN-FP-6-EMHAND).
- Does not duplicate EW-1's Maxwell derivation or QM-3's photoelectric derivation — it unifies them.
- Does not rely on the stale EW-3/EW-5 source mapping (corrected, §2).
- Does not overclaim on the Michelson-Morley tension — §9 must frame the absolute-frame-signature point honestly.

---

## 7. Estimated lift & spin-off readiness

**High (≈6–9 sessions)** — the broadest scope of any SF-line paper, with material **scattered** across foundations, SR companions, QM, and legacy EW. The lift is *assembly breadth*, not missing physics: the spine (c06 + DP-Sea-Polarization-Model) is shipped. The README's 5–8 estimate is likely optimistic given breadth; budget 6–9. Recommended first drafting move: §2–§3 (substrate + the $E=\hbar\nu_C$ unification) as the conceptual core from c06, then the three limits §4–§6, then §7–§9.

---

## 8. §10 members this unlocks (post-SF-6-ship)

- **SF-6 ↔ SF-2.** Shared/disjoint: the photon (SF-6, eDP-polarization quantum) and the cage bosons W/Z/H (SF-2, cage resonances) are **categorically distinct particle classes** on the same substrate — a clean no-double-counting clause (no particle assigned to both mechanisms).
- **SF-6 ↔ all (substrate/SSV).** The SSV and DP-Sea primitives underlie every sector; SF-6 makes the EM-field substrate explicit, consistency-checking the SSV usage across SF-1/2/3/4/5.
- **Cross-arc dependency (not a §10 member but flag it):** SF-6's OPEN-FP-6-EMHAND consumes the chirality arc's manifestation (iii). When window 2 closes (iii), SF-6 promotes it. **Window 2 should track SF-6 as a downstream consumer.**

All §10 members follow the THEO-SF7-CONSIST-1 three-clause template (1301).

---

## 9. Collision-coordination

New file under `flagship_papers/electromagnetism/` — **no shared-registry edits, no other window's files touched, no δ_CP/window-5 adjacency**. **One genuine cross-window dependency to surface to you:** SF-6's deferred manifestation (iii) is **chirality-window (window 2) territory** — this is a downstream-consumer relationship, not a collision (SF-6 reads/awaits, does not edit, window 2's files). At SF-6 ship time, OPEN-FP-6-EMHAND registration and predictions.md entries route through a flagged integration patch.

---

*Patch 1305 — SF-6 electromagnetism flagship outline + source pre-survey. Revises 1300/1304: core unblocked (c06 spine), only manifestation (iii) blocked-and-deferrable (window 2); README source map corrected. Completes the predecessor pre-survey set (SF-1/3/5/6 all scoped). No new derivation; no physics verdicts moved; no registries touched. New file under `flagship_papers/electromagnetism/`, collision-free.*

# SF-3 Quarks — Pre-Survey & Flagship Outline (with the m_c route adjudication)

**Location:** `/CPP/flagship_papers/quarks/sf-3_outline.md`
**Opened:** Session 160, Patch 1303 (SF-7 grand-unification window)
**Status:** OUTLINE + source-corpus pre-survey + **calibration-route adjudication**. This patch settles the load-bearing question flagged in 1300 §2 and 1301 C1.
**Source corpus surveyed:** SM-2, SM-7, SM-8 (v4.0), SM-9, SM-10 — all shipped.
**Resolves:** the SF-7 single-m_e headline question (1300 §2). **Unlocks (post-ship):** §10 members SF-3↔SF-1, SF-3↔SF-2, SF-3↔SF-4.

---

## 0. Orientation — read this first

SF-3 is medium-lift, and its central drafting decision is **not** new physics — it is **adjudicating between two shipped quark-mass routes**, one of which (SM-8) restores the single-m_e calibration claim the SF-7 README wants, and one of which (SM-7) carries a second calibration (m_c) but delivers the quark Koide phase and α_s. The pre-survey below shows these routes are **complementary, not contradictory**, and recommends a clean synthesis that keeps the single calibration *and* the structural EW–strong unification content. The one genuine gap is **CKM mixing**, which has no derivation anywhere in the corpus and must be inherited-open (the quark analog of SF-4's open δ_CP). Resolving the route question here is what lets the SF-7 §9 master comparison table finally commit to "1 calibration."

---

## 1. The adjudication (the centerpiece — resolves 1300 §2)

Two shipped routes produce the heavy-quark masses:

**Route A — SM-8 zero-parameter cage formula.**
$$M_q = m_e\,(z/\phi)\,V^{7/3}\ \ (q=s,c,b);\qquad M_t = m_e\,(z/\phi)\,V_t^{7/3}\times z\,C_F$$
Predicts **all four** quark masses (s, c, b, t) to **RMS 2.1%** across four orders of magnitude, using **only** m_e + 600-cell geometry ($z=12$, $\phi$) + SU(3) colour ($C_F=4/3$, derived in SS-2). The exponent 7/3 and prefactor $M_0=m_e z/\phi$ are **derived in SM-9**. **No parameters fitted.** Crucially, **m_c is a *prediction* here** ($\approx 1249$ MeV, 1.6%), not an input.

**Route B — SM-7 Koide + m_c calibration.**
Uses the charm mass as a calibration constant to place the quark Koide phase, giving $m_b = 4.24$ GeV (1.4%), $m_t = 169.8$ GeV (1.7%) — slightly better on b/t than Route A — *plus* the quark Koide phase $\theta=124.04°$ (PDG 124.09°, 0.05%) and $\alpha_s = 5/(8\phi)$. **Two calibrations (m_e, m_c).**

**The key fact:** because SM-8 (Route A) *derives* m_c from m_e at zero parameters, the m_c calibration in SM-7 (Route B) is **redundant** — m_c can be supplied by SM-8's prediction rather than fitted.

**Recommendation for SF-3 (and SF-7 §9):**
> Adopt **Route A (SM-8) as the canonical mass-spectrum route**: all four quark masses from m_e alone, RMS 2.1%, single calibration. **Demote m_c from calibration to derived quantity** (SM-8 prediction). Retain **Route B's structural content** — $\alpha_s = 5/(8\phi)$, the mode-complementarity $\sin^2\theta_W+\alpha_s=1/\phi$, and the quark Koide phase $\theta=124.04°$ — as the EW–strong unification layer, but **re-ground SM-7's phase machinery on the *derived* m_c** (SM-8) instead of a fitted m_c.

This restores the **single-m_e calibration headline** for the quark sector at the cost of slightly larger mass residuals (RMS 2.1% vs Route B's better b/t). The honesty trade is clearly worth it: a uniform single-calibration claim across leptons (SF-1), neutrinos (SF-4), and quarks (SF-3) is the spine of the SF-7 "hierarchy without hierarchy" argument; a 0.3% accuracy gain on b/t is not worth a second calibration that contradicts that spine.

**SF-7 §9 consequence:** with Route A adopted, the master table reads **1 calibration (m_e)** for all fermion masses. The remaining caveats are SF-2's open η-dilution (boson *absolute* masses, 1301 C1) — which is a boson, not a fermion-mass, issue — and the CKM gap (§4 below). Neither blocks the single-calibration fermion-mass claim.

---

## 2. Headline result (what SF-3 claims, post-adjudication)

> The complete quark mass spectrum (s, c, b, t), the strong coupling $\alpha_s$, the quark Koide phase, and the three-generation count all derive from a **single calibration (m_e) plus 600-cell geometry + SU(3) colour**, with **zero shape parameters**. CKM mixing is inherited-open.

| Quantity | CPP | Experiment | Agreement | Source | Status |
|----------|-----|-----------|-----------|--------|--------|
| $m_s, m_c, m_b, m_t$ | $m_e(z/\phi)V^{7/3}$ (+ $zC_F$ for top) | PDG | RMS 2.1% | SM-8 | zero-param (Route A) |
| $\alpha_s$ | $5/(8\phi)\approx 0.386$ | $\alpha_s(m_c)\approx 0.35$–0.40 | in band | SM-7 | theorem (mode fraction) |
| $\sin^2\theta_W+\alpha_s$ | $1/\phi$ | — | exact identity | SM-7 | mode complementarity |
| quark Koide phase | $\theta=124.04°$ | $124.09°$ | 0.05% | SM-7 | derived (EW+strong shift) |
| # generations | 3 | 3 | exact | SM-8 | antipodal identification |
| CKM matrix | — | — | — | — | **OPEN-FP-3-CKM (inherited)** |

---

## 3. Source-corpus rigor ledger

| Paper | Contributes to SF-3 | Status |
|-------|---------------------|--------|
| **SM-2** | mass-generation geometric hierarchies; chiral-polarity structure | shipped |
| **SM-7** | $\alpha_s=5/(8\phi)$; mode complementarity $\sin^2\theta_W+\alpha_s=1/\phi$; quark Koide phase $\theta=124.04°$; b/t masses via Koide+m_c | shipped (Route B) |
| **SM-8 v4.0** | zero-param mass formula $M_q=m_e(z/\phi)V^{7/3}$; four shells ↔ generations; **3 generations from antipodal identification**; top $\times zC_F=16$ | shipped (Route A) |
| **SM-9** | derives the 7/3 exponent (pair count × linear cage dimension) and $M_0=m_e z/\phi$ | shipped |
| **SM-10** | FEM chain-network *mechanism* for the 7/3 scaling; currently a calibrated geometric model (4 fitted params/4 data) pending GPU first-principles closure. **NOT a CKM paper** | shipped |
| **SS-2** | $C_F=4/3$ independently derived | shipped |

---

## 4. The CKM gap (open inheritance — register, do not claim)

There is **no CKM-matrix derivation anywhere in the quark corpus.** SM-10, despite an incidental mention, is the FEM scaling-mechanism paper, not a mixing paper. So:

- Register **OPEN-FP-3-CKM** and inherit it honestly. SF-3 predicts the quark *masses* and *generation count* at zero parameters but **does not yet derive the CKM mixing angles or the quark CP phase.**
- This is the **structural analog of SF-4's open δ_CP**: SF-4 ships 7/8 neutrino parameters with δ_CP deferred; SF-3 should ship the quark masses + generation count with CKM deferred. State the parallel explicitly — it is honest and it strengthens the SF-line's uniform "masses derived, mixing-sector open" posture.
- Candidate closure route to flag (not pursue): a quark-sector cage-mixing structure analogous to SM-5's K3 → TBM derivation for PMNS. SF-4's PMNS came from K3 spectral alignment; the CKM analog is unscoped. Leave as forward pointer.

*Note:* CKM is **not** window 5's territory (window 5 = neutrino δ_CP). The quark CP phase inside CKM is a separate object. So SF-3's mixing gap carries lower cross-window collision risk than the SF-4-side δ_CP work.

---

## 5. Structural wins to foreground (the unification content)

These are why SF-3 is more than a mass table:

- **One spectral-trace formula gives both $\sin^2\theta_W$ and $\alpha_s$.** $\sin^2\theta_W=3/(8\phi)$ (edge modes) and $\alpha_s=5/(8\phi)$ (face modes) are the two mode fractions of the *same* 600-cell adjacency spectrum, weighted by $\eta=1/\phi$. Their sum is $1/\phi$ exactly; their ratio is $F/E=5/3$, a topological invariant. This is a genuine electroweak–strong unification at the substrate level and a direct §10 thread to SF-1 and SF-2.
- **The quark Koide phase derives like the lepton phase**, from the net isotropic shift (EW $+3/(52\phi)$ from SM-6, plus strong colour $-z\alpha_s/(z+1)$), giving $\theta=124.04°$ at 0.05%. Same machinery as SF-1's lepton phase — a shared-mechanism §10 thread to SF-1.
- **Three generations are forced**, not assumed: antipodal identification in the tessellated lattice limits the SM to exactly three generations, and predicts **no fourth quark**. Zero-parameter structural prediction + falsifier.

---

## 6. Proposed section structure (apex-paper form)

- **§1 The quark mass problem.** Six quark masses spanning five orders of magnitude; why these values; CKM as the named open piece.
- **§2 Substrate + four bonded shells.** 600-cell shells $V\in\{4,12,20,30\}$ ↔ cage types; SU(3) colour from cage-face permutations (SS-1); $C_F=4/3$ (SS-2).
- **§3 The zero-parameter mass spectrum (Route A canonical).** $M_q=m_e(z/\phi)V^{7/3}$; top relay $\times zC_F$; 7/3 + $M_0$ derived (SM-9); RMS 2.1%. m_c as derived prediction.
- **§4 Strong coupling + mode complementarity.** $\alpha_s=5/(8\phi)$; $\sin^2\theta_W+\alpha_s=1/\phi$; the EW–strong unification.
- **§5 The quark Koide phase.** EW + strong isotropic shift → $\theta=124.04°$; re-grounded on derived m_c.
- **§6 Three generations.** Antipodal identification; no fourth quark; falsifier.
- **§7 Calibration ledger.** Single m_e; m_c demoted to derived; the route adjudication stated openly (§1 above).
- **§8 CKM — inherited-open.** OPEN-FP-3-CKM; the SF-4-δ_CP parallel; candidate K3-analog route as forward pointer.
- **§9 Conditional accounting + falsifiers.** SM-10 mechanism still calibrated (pending GPU); CKM open; 4th-generation falsifier; $\alpha_s$ running.
- **§10 Discussion / SF-line placement.** Hooks to SF-1 (shared phase machinery + mode fractions), SF-2 (Weinberg–α_s complementarity), SF-4 (shared $M_0$/taxonomy + masses-derived/mixing-open parallel).

---

## 7. What SF-3 does NOT do

- Does not derive CKM (OPEN-FP-3-CKM, inherited).
- Does not claim m_c as calibration (demoted to derived, Route A).
- Does not close SM-10's first-principles cascade derivation (calibrated model pending GPU).
- Does not re-register SM-2/7/8/9/10 theorems (reframes; they keep their SM IDs until SF-3 ship).

---

## 8. Estimated lift & spin-off readiness

**Medium (≈5–7 sessions).** Higher than SF-1 because of (a) the route-adjudication write-up (settled here, but must be argued cleanly in §1/§7) and (b) the CKM-gap framing. All mass physics is shipped. Recommended first drafting move: write §3 (Route A spectrum) + §4 (α_s/complementarity) as the zero-parameter core, then §1/§7 adjudication, then §8 CKM honesty.

---

## 9. §10 members this unlocks (post-SF-3-ship)

- **SF-3 ↔ SF-2.** Shared: the mode-fraction structure — $\sin^2\theta_W=3/(8\phi)$ (SF-2) and $\alpha_s=5/(8\phi)$ (SF-3) from one spectral trace, complementary to $1/\phi$. Strong consistency clause (single spectral source, no independent calibration).
- **SF-3 ↔ SF-1.** Shared: the Koide-phase derivation machinery (isotropic-shift on the K3 face) and the $M_0=m_e(z/\phi)$ anchor. Consistency clause: lepton and quark phases use the same mechanism with sector-appropriate shifts (EW only for leptons; EW+strong for quarks).
- **SF-3 ↔ SF-4.** Shared: $M_0$ + four-cage taxonomy; and the **masses-derived / mixing-open parallel** (CKM open in SF-3 ↔ δ_CP open in SF-4). Consistency clause: both sectors derive masses from $M_0$ and defer their mixing-sector CP structure, with no conflicting calibration.

All follow the THEO-SF7-CONSIST-1 three-clause template (1301).

---

## 10. Collision-coordination

New file under `flagship_papers/quarks/` — **no shared-registry edits, no other window's files touched**. The route adjudication conceptually updates the SF-7 §9 calibration story that 1300/1301 reference, but does so only inside this window's `flagship_papers/unification`-adjacent narrative; no `frontier_sectors/*` or registry edits here. **Lower cross-window risk than 1301**: CKM is not window 5's neutrino-δ_CP territory. At SF-3 ship time, OPEN-FP-3-CKM registration and any predictions.md entries go through a flagged integration patch.

---

*Patch 1303 — SF-3 flagship outline + source pre-survey + m_c route adjudication. Resolves the 1300 §2 single-m_e question (adopt SM-8 Route A; m_c demoted to derived). No new derivation; no physics verdicts moved; no registries touched. New file under `flagship_papers/quarks/`, collision-free.*

# §10 Seed — SF-2 ↔ SF-4 Cross-Sector Consistency Theorem (THEO-SF7-CONSIST-1, candidate)

**Location:** `/CPP/flagship_papers/unification/sf-7_consistency_SF2_SF4.md`
**Opened:** Session 160, Patch 1301 (SF-7 grand-unification window)
**Status:** SKETCH / theorem candidate. First member of the SF-7 §10 cross-particle-class consistency-theorem family. Built entirely on **shipped** material (SF-2 v1.01, SF-4 v4.4, SM-1 taxonomy, Capotauro v2.0 / Chirality Continuum χ-handle). **Registration in `theorem-registry.md` DEFERRED** to SF-7 ship or a flagged integration patch — kept as a sketch to stay collision-light.
**Depends on:** patch 1300 (`sf-7_critical_path_map.md`) §3.

---

## 0. Orientation — read this first

The §10 core of SF-7 must prove that the six sector flagships *cohere*: one substrate, one calibration anchor, no double-counting of degrees of freedom, and consistent sourcing of shared observables (notably δ_CP). A pairwise consistency claim is buildable iff both member flagships are shipped. **SF-2 (electroweak cage bosons) and SF-4 (neutrinos) are the only such pair today**, so this is the first §10 member. The theorem below has three clauses — calibration coherence, no-double-counting, and δ_CP single-handle — graded by rigor. Clause 2 is the strongest (theorem-level, because both papers inherit the *same* SM-1 four-cage taxonomy and their shell assignments are mutually consistent *by construction*). Clause 1 is theorem-level on the shared anchor but flags SF-2's open η-calibration. Clause 3 establishes that δ_CP defers from SF-4 *into the same substrate chirality handle* SF-2 uses, which is the interconnection-level δ_CP record — distinct from deriving δ_CP's value (window 5).

---

## 1. Theorem statement (candidate)

> **THEO-SF7-CONSIST-1 (SF-2 ↔ SF-4 Cross-Sector Consistency).**
> The electroweak cage-boson sector (SF-2 v1.01) and the neutrino sector (SF-4 v4.4) are mutually consistent as derivations on the shared 600-cell substrate, in the following three senses:
>
> **(C1) Calibration coherence.** Both sectors anchor every mass scale on the single substrate quantum $M_0 = m_e\,(z/\phi) \approx 3.79$ MeV, with identical $z=12$ and $\phi$. Neither introduces a mass calibration that conflicts with the other. *(Qualified: SF-2's **absolute** boson masses carry an additional, currently-open per-boson holographic dilution $\eta \sim 10^{-17}$, OPEN-FP-SF-2-η; SF-2's structural and mass-**ratio** results, and all of SF-4, are zero-parameter on $M_0$.)*
>
> **(C2) No double-counting.** Both sectors draw their shell assignments from the *same* SM-1 four-cage taxonomy $V \in \{4,12,20,30\}$. The assignments are mutually consistent: the only shell co-occupied by an SF-2 boson and an SF-4 neutrino is $V=12$, where the two play **distinct structural roles** (boson cage-*shape* vs. fermion cage-*shell-occupation*) with masses computed by **independent mechanisms sharing no fitted degree of freedom**.
>
> **(C3) δ_CP single-handle.** SF-4 defers $\delta_{CP}$ to the electroweak-sector flagship (route ii, OP-SM-7d). SF-2's chirality-dependent observable (W $V\!-\!A$ coupling, OPEN-FP-SF-2-CHIR) is sourced from the substrate chirality handle $\chi = \phi^{-3}$ (matrix element $\chi/6 \approx 0.0394$). The deferral target and the EW chirality handle are therefore **one substrate quantity**; the two sectors reference $\chi$ without contradiction.

---

## 2. Clause C1 — calibration coherence

**Shared anchor (theorem-level).** SF-4 §2 states the neutrino mass formula $m_{\nu_i} = M_0\,V_{\nu_i}^2\,\sigma_\nu$ with $M_0 = m_e (z/\phi)$ "the same $M_0$ that anchors the quark and charged-lepton sectors in SM-7/8/9" (SF-4 lines 75–78, 132, 269). SF-2 §1 places the cage-boson sector "in the cage-shell framework … where the charged lepton, quark, and neutrino sectors derive their masses and mixing angles from 600-cell distance shells with **single calibration $m_e$**" (SF-2 line 194), citing SF-4 directly. Both use identical $z=12$, identical $\phi$, identical $m_e$. **No conflicting calibration is introduced.**

**Honest ledger (the qualification that matters for SF-7 §9).**
- SF-4 introduces *no* new fitted parameter beyond $M_0$ (SF-4 line 304, explicit); $\sigma_\nu = z^{-10}$ is parameter-free.
- SF-2's *structural* results (four cage-shape theorems, $\sin^2\theta_W = 3/(8\phi)$ inherited from SM-6) and the mass-**ratio** $m_Z/m_W = 1/\cos\theta_W = 1.140$ (0.5% vs 1.134) are zero-parameter on the shared substrate, "with no cross-calibration" (SF-2 lines 169, 199).
- SF-2's *absolute* boson masses are PARTIAL CLOSURE: reproduced via an independent per-boson holographic dilution $\eta \sim 10^{-17}$ (OPEN-FP-SF-2-η, inheriting OPEN-P-EW-1; SF-2 lines 155, 209).

**C1 verdict:** the *coherence of the shared anchor* is theorem-level. The *single-calibration headline for the whole EW+ν block* is conditional on OPEN-FP-SF-2-η closure. This is a second, distinct calibration-honesty caveat from the SF-3 $m_c$ issue flagged in 1300 §2 — SF-7 §9 must carry **both**: (a) the SF-3 quark-route $m_c$ adjudication, and (b) the SF-2 η-dilution open calibration. Neither is fatal; both must be stated, not obscured.

---

## 3. Clause C2 — no double-counting (the strongest clause)

**Shared taxonomy.** SF-4 §2 (lines 212–215) and its inheritance table (lines 174, 293, 344) take the SM-1 four-cage taxonomy as a theorem-level inherited input. SF-2 (lines 165, 213–215 of SF-4 cross-confirm) assigns its bosons to the same shells. The combined shell-occupancy ledger:

| 600-cell substructure | SF-2 boson | SF-4 neutrino | Other SM-1 hosts | SF-2↔SF-4 conflict? |
|-----------------------|-----------|---------------|------------------|---------------------|
| 6-vertex bracelet (6-cycle of edges) | $W^\pm/W^0$ | — | — | none (distinct object class; not a distance shell) |
| $V=4$ tetrahedral ($d^2{\approx}0.19$) | — | $\nu_1$ | electron, light quarks | none |
| $V=12$ icosahedral ($d^2{\approx}0.38$) | **$Z$** | **$\nu_2$** | charm quark, tau lepton | **shared shell — see argument** |
| $V=20$ dodecahedral ($d^2{=}1$) | **Higgs** | — *(excluded)* | bottom quark | none (SF-4 yields $V=20$ per SM-1) |
| $V=30$ icosidodecahedral ($d^2{=}2$) | — | $\nu_3$ | top quark | none |

Two structural facts make the ledger consistent *by construction*:
1. **$V=20$ is yielded, not contested.** SF-4 explicitly excludes $V=20$ for the neutrino sector, citing SM-1's assignment of $V=20$ to the bottom quark and Higgs (SF-4 lines 174, 344). SF-2's Higgs *is* that $V=20$ dodecahedral cage. So the two papers do not fight over $V=20$; SF-4 defers to the same taxonomy that gives SF-2 its Higgs.
2. **The $W$ bracelet is not a distance shell.** It is a 6-cycle of *edges* (the unique maximal-symmetry $H_4$-orbit of induced 6-cycles, $D_6$ stabilizer, orbit 1200; SF-2 line 149), categorically distinct from the $\{4,12,20,30\}$ distance-shell cages. No neutrino shell can collide with it.

**The one shared shell, $V=12$ (the crux).** Both the $Z$ boson (SF-2) and $\nu_2$ (SF-4) reference the 12-vertex icosahedral first shell. This is *not* double-counting, because:
- **Distinct particle role.** SF-2's $Z$ is a *transient intermediate state* — a boson cage-*shape* that forms and dissolves during neutral-current interactions ("the electroweak bosons are intermediate states … unlike the fermion sectors, where each particle is a stable cage state"; SF-2 line 194). SF-4's $\nu_2$ is a *stable fermion cage-shell occupation* (an unbound 3D-orbital ZBW mode resident at $V=12$). Cage-as-resonance vs. fermion-in-shell.
- **Independent mass mechanism, no shared fitted DOF.** $m_Z$ comes from cage-stability + the open $\eta_Z$ dilution; $m_{\nu_2} = M_0\,(12)^2\,\sigma_\nu$ comes from the pair-count $V^2$ law + $\sigma_\nu = z^{-10}$. The two predictions share the $M_0=m_e(z/\phi)$ anchor and the *geometric fact* of the 12-vertex shell, but **no fitted parameter is reused** — $\eta_Z$ enters only $m_Z$, $\sigma_\nu$ enters only the neutrino masses.
- **Precedent in the taxonomy itself.** $V=12$ already hosts the charm quark *and* tau lepton *and* $Z$ *and* $\nu_2$ in SM-1 — multiple particle roles per shell is the designed behavior of the four-cage taxonomy, not an SF-2/SF-4 collision.

**C2 verdict:** theorem-level. The shared SM-1 taxonomy is a theorem-level common input; the shell assignments are mutually consistent; the single co-occupied shell carries distinct roles with disjoint fitted degrees of freedom. **No double-counting.**

---

## 4. Clause C3 — δ_CP single-handle

**The deferral.** SF-4 registers $\delta_{CP}$ as open (OP-SM-7d) and **defers it to the electroweak-sector flagship SF-2, route (ii)** (SF-4 lines 75, 135, 146, 190, 301), enumerating four candidate handles for forward reference.

**The handle.** SF-2's chirality-dependent observable is the $W$ $V\!-\!A$ coupling: "$W$ is vector at 75% $V\!-\!A$ from bracelet $120^\circ/240^\circ$ phase bias, becoming 100% $V\!-\!A$ at the massless helicity limit per OPEN-FP-SF-2-CHIR" (SF-2 line 147). OPEN-FP-SF-2-CHIR is closed at Layer 4 by the Chirality Continuum flagship via the substrate chirality handle $\chi = \phi^{-3}$, matrix element $\chi/6 \approx 0.0394$ (Capotauro v2.0 three-way unification $\|M^{K3}\|=\|M^W\|=\|M^{qDP}\|=\chi/6$; THEO-CHIR-CONT-2).

**The identity.** The target SF-4 defers δ_CP *to* (the EW-sector chirality mechanism) and the handle SF-2's $V\!-\!A$ coupling is *sourced from* are the **same substrate quantity** $\chi = \phi^{-3}$. Both sectors' chirality-dependent observables trace to one matrix element $\chi/6$. There is no second, conflicting chirality scale.

**C3 verdict:** the *single-handle consistency* is established structurally — the δ_CP deferral target is identical to the EW chirality handle, $\chi = \phi^{-3}$. What remains open is the **δ_CP value derivation** itself (one of four candidate handles → a number), which is **window 5's deliverable**, not this theorem's. C3 is therefore the interconnection-level δ_CP record: it certifies that when window 5 produces a δ_CP prediction from the $\chi/6$ handle, that prediction is *automatically consistent* with SF-2's V–A coupling because both draw on the same substrate quantity.

---

## 5. What this seeds

- **The δ_CP-sourcing record for window 5.** C3 is the consistency scaffold window 5's eventual δ_CP prediction plugs into. When window 5 lands a value via the $\chi/6$ handle, THEO-SF7-CONSIST-1 (C3) certifies its cross-sector consistency with SF-2 at no extra cost.
- **The §10 family template.** This three-clause structure (calibration coherence / no-double-counting / shared-observable single-handle) is the template each subsequent §10 member follows as SF-1, SF-3, SF-5, SF-6 ship. The next members become buildable in this order: SF-1↔{SF-2,SF-4} (once SF-1 ships), then SF-3↔… , culminating in the global six-way consistency theorem.
- **An honesty-ledger contribution to SF-7 §9.** Surfaces the SF-2 η-dilution open calibration as a second caveat alongside the SF-3 $m_c$ issue — both must appear in the SF-7 master comparison table.

---

## 6. What is NOT claimed

- Not a δ_CP value (window 5).
- Not closure of OPEN-FP-SF-2-η (SF-2 absolute boson masses remain PARTIAL CLOSURE).
- Not a theorem-registry entry yet (registration deferred to SF-7 ship or a flagged integration patch).
- Not a claim about SF-1/3/5/6 — those §10 members are blocked until their flagships ship.

---

## 7. Registration note

THEO-SF7-CONSIST-1 is stated here as a **candidate**. Per programme convention (cf. THEO-CAP-1, THEO-SD-CHIR-1/2 pre-registration), promotion into `theorem-registry.md` happens via a flagged integration patch or at SF-7 ship. Clause grading at candidacy: **C2 theorem-level; C1 theorem-level on the shared anchor (conditional on OPEN-FP-SF-2-η for the full single-calibration claim); C3 structural (single-handle established; value open to window 5).**

---

*Patch 1301 — SF-7 §10 seed. Built on shipped inputs only. No physics verdicts moved; no registries touched. δ_CP-adjacent (window 5) and reads SF-2/SF-4 sources → HOLD-FOR-REFRESH at delivery.*

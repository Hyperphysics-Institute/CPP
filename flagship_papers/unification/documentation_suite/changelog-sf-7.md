# Changelog — SF-7: Standard Model Grand Unification from 600-Cell Geometry

Version history for `flagship_papers/unification/sf-7_grand_unification.tex`.
The canonical filename is fixed (no version suffix); version history is tracked here and in the `.tex` source-header comment block.

---

## v0.3 (DRAFT) — 21 June 2026, Patch 1317

First §10 consistency-theorem member built under the review-adopted build rule: **THEO-SF7-CONSIST-2 (SF-1 ↔ SF-2 spectral-trace consistency)** (`sec:consist2`).

**The theorem.** Both the charged-lepton sector (SF-1) and the electroweak cage-boson sector (SF-2) are forced to one Weinberg value $\sin^2\theta_W = 3/(8\varphi)$ by the *same* 600-cell edge-mode spectral trace ($\mathrm{Tr}(A^2):\tfrac13\mathrm{Tr}(A^3) = 1440:2400 = 3/8$, unique to the 600-cell; ×edge efficiency $1/\varphi$), and that value enters the two sectors through *independent observable channels*: SF-1 only via the Koide-phase isotropic shift $\varepsilon = 2\sin^2\theta_W/(z+1) = 3/(52\varphi)$ ($\theta = 132.731°$); SF-2 only via the boson mass ratio $m_Z/m_W = 1/\cos\theta_W = 1.140$ ($\approx0.5\%$). Their agreement is the geometric analogue of gauge universality — a non-trivial, falsifiable cross-sector constraint, **not** a shared free parameter and **not** a "both use the 600-cell" restatement. Four-part proof: (i) one geometric origin; (ii) two independent channels; (iii) non-trivial/falsifiable (a channel mismatch would falsify the shared substrate); (iv) no double-counting (the trace is a geometric input, not a fitted DOF — the spectral-trace analogue of `lem:c2indep`).

**Build-rule compliance:** carries a constraint forced jointly by the two sectors, with a unique obligation (cross-channel spectral-trace consistency) distinct from every other member. Roadmap updated (nine members remain). Abstract updated to two built members. SF-2-only macros (`\mZ`,`\mW`) avoided — plain `m_Z`/`m_W` used (SF-7 preamble does not define them). Compiles clean: `pdflatex` ×2, 9 pp, 0 errors, 0 undefined refs/cites, 0 overfull. Bundles `reasoning/1317.md`. Registration of THEO-SF7-CONSIST-2 deferred to the ship-time flagged patch.

---

## v0.2 (DRAFT) — 21 June 2026, Patch 1316

Review-cycle-1 calibration (architectural review closed 2×(A)/2×(B), zero (C), unanimous proceed). **C2 promoted to theorem** by meeting ChatGPT's three independence conditions rather than softening: the $Z$/$\nu_2$ independence Lemma (`lem:c2indep`, numbered three-part proof) discharges disjoint state variables, disjoint parameter sets, and perturbation invariance, with the single $m_e$ coupling named as the one permitted shared dependency. Four convergent deflations: C3 reworded to "shared *quantity* χ, not a shared mechanism (OP-SM-7d open)" + χ/6 = 0.0393446 footnote; §9 Closed/Partial/Open closure column + standardized headline qualifier; §10 panel-adopted circularity build rule. Compiles clean (8 pp, 0/0/0; two table overfulls fixed via `\resizebox`). Added `review/reviews-SF-7.md`; bundled `reasoning/1316.md`.



First skeleton of the SF-7 apex synthesis, assembled to the 16-section paper-formatting standard. Drawn from this window's 1300 band (next free 1314).

**Unblock milestone:** all six predecessor flagships are now SHIPPED v1.0 (SF-1 #1404, SF-2 v1.01, SF-3 #1505, SF-4 v4.4, SF-5 #1521, SF-6 #1607/1609) — the critical-path gate for SF-7 drafting is satisfied for the first time.

**Load-bearing content (shipped-predecessor-grounded):**
- §3–§8 per-sector synthesis paragraphs (SF-1 … SF-6 headlines).
- §9 the hierarchy-without-hierarchy ledger table — SM 19+ free parameters vs CPP 0 beyond the single $m_e$ calibration; two honest caveats footnoted (SF-2 $\eta$-dilution OPEN-FP-SF-2-$\eta$; open mixing sectors CKM + $\delta_{CP}$).
- §10.1 THEO-SF7-CONSIST-1 (SF-2 ↔ SF-4, the one built member) + the §10 roadmap table (ten members + the global six-way capstone, each with its identified thread).

**Scaffold (`%%TODO`, honest placeholders for later patches):** Plain Language Summary; §1–§2 full framing; §11 cumulative falsifier; §12 predictions; §13 discussion; Physical Interpretation + CP/GP Signature (PD-001 required); Conclusion + Swarm-Validation (PD-001 required) + Problem Status.

**Build note:** nine §10-roadmap status cells originally carried `%%TODO` as the literal cell value, which (since `%` opens a LaTeX comment) commented out the row terminators and blocked compilation; corrected to "to build." Compiles clean: `pdflatex` ×2, 7 pages, 0 errors, 0 undefined refs/cites, 0 overfull.

**Bundled:** `reasoning/1314.md` (verbatim reasoning capture). No verify script at v0.1 (§9 numbers all inherited; a `code/1314…` verifier is flagged for when the §9 numbers are frozen).

**Deferred to ship-time flagged integration patch (after a refresh against origin/main):** theorem-registry registration of THEO-SF7-CONSIST-1 and the §10 members; `paper_catalog.md`, `predictions.md`, `frontier_sectors/*`, `master_glossary.md`, bibliography master entry.

# Changelog — SF-7: Standard Model Grand Unification from 600-Cell Geometry

Version history for `flagship_papers/unification/sf-7_grand_unification.tex`.
The canonical filename is fixed (no version suffix); version history is tracked here and in the `.tex` source-header comment block.

---

## v0.6 (DRAFT) — 21 June 2026, Patch 1320

Fourth §10 member built under the build rule: **THEO-SF7-CONSIST-5 (SF-6 ↔ SF-2 photon–cage-boson categorical distinction)** (`sec:consist5`) — the cleanest categorical no-double-counting in the family.

**The theorem.** The photon (SF-6) and the electroweak cage bosons (SF-2) are categorically distinct substrate objects: the photon is a *delocalized traveling* eDP-sea ZDC pattern with no nucleation center (massless; the traveling boundary condition of E = ℏν_C), while the cage bosons are *localized* 600-cell cage structures (nucleated; massive). No boson belongs to both classes — the EM/EW boson content partitions cleanly across SF-2 and SF-6. Four-part proof: (i) photon = traveling sea mode; (ii) cage bosons = localized structures (architectural partition: SF-2 cages, SF-6 photon, SF-5 gluons); (iii) categorical disjointness — non-trivial because the SM unifies photon + weak bosons in one multiplet and mixes them, whereas CPP assigns disjoint substrate categories and the Weinberg mixing is carried by the geometric trace 3/(8φ) (a shared geometric *input*, not a structural DOF; cf. CONSIST-2), so mixing does not reintroduce double-counting; (iv) honest scope — rests on SF-6's Tier-1 ontological reduction; Tier-2 toy-model EM constants (OPEN-FP-6-CONSTANTS) not invoked.

**Why not circular / build-rule.** Unique obligation = ontological partition of boson content (delocalized sea mode vs localized cage structure), orthogonal to CONSIST-4 (gauge-group co-emergence), -2, -3. SF-6 itself names this thread. Roadmap row → built (six remain); caption + abstract (five built members) updated; v0.5→v0.6. Macros avoided (no SF-6-only \ZDC/\nuC/\eDP; plain ν_C, ZDC as text). Compiles clean: `pdflatex` ×2, 11 pp, 0 errors, 0 undefined refs/cites, 0 overfull. Bundles `reasoning/1320.md`. Registration deferred to ship-time.



Third §10 member built under the build rule: **THEO-SF7-CONSIST-4 (SF-5 ↔ SF-2 gauge-group co-emergence)** (`sec:consist4`).

**The theorem.** The two non-abelian SM gauge groups emerge from the single 600-cell through *disjoint structural features*: SU(2)_L from the *global vertex-group* (the 120 vertices are the binary icosahedral group Γ = 2I, a finite subgroup of SU(2); Cayley graph, THEO-EW-6) and SU(3)_c from a *local operator representation* on a tetrahedral sub-cage (eight DI-bit hopping operators T^a = λ^a/2, SS-1b, unique within the operator representation). Four-part proof: (i) SU(2)_L at the global group level; (ii) SU(3)_c at the local operator level; (iii) the constraint — disjoint structural features, no shared fitted DOF, one object supplies *both* non-abelian groups (and exactly SU(2)×SU(3)) by two independent structural facts; (iv) honest scope — theorem at the algebra level, continuum YM-EFT limit inherited as proof-outline (THEO-EW-8), SU(3) uniqueness within the operator representation.

**Why not circular.** "Both come from the 600-cell" is exactly what the build rule forbids; the genuine content is that the two groups use *different* structural features (global group law vs local sub-cage operator algebra), so the obligation (gauge-group co-emergence at disjoint structural levels) is real and distinct. This member is *structural* rather than numerical — orthogonal to CONSIST-2 (shared value) and CONSIST-3 (mode partition). Roadmap row → built (seven remain); caption + abstract (four built members, compacted) updated; v0.4→v0.5. Compiles clean: `pdflatex` ×2, 11 pp, 0 errors, 0 undefined refs/cites, 0 overfull. Bundles `reasoning/1319.md`. Registration deferred to ship-time.



Second §10 member built under the build rule: **THEO-SF7-CONSIST-3 (SF-3 ↔ SF-2 electroweak–strong mode complementarity)** (`sec:consist3`) — the build rule's own model constraint.

**The theorem.** The electroweak coupling sin²θ_W (SF-2, edge-mode fraction 3/(8φ)) and the strong coupling α_s (SF-3, face-mode fraction 5/(8φ)) are the two complementary mode fractions of one 600-cell adjacency spectral trace, drawn from *disjoint mode classes that exhaust the trace*: sin²θ_W + α_s = 1/φ, with α_s/sin²θ_W = F/E = 1200/720 = 5/3. Four-part proof: (i) disjoint exhaustive partition (edge vs face, no-double-counting at the mode level); (ii) **honest flag** — given the mode-fraction identification the sum identity is *definitional*, not a coincidence; (iii) the genuine falsifiable content is that the *independently measured* couplings sum to 1/φ (a measured pair off the F/E=5/3 partition, beyond α_s running tolerance, falsifies the identification); (iv) honest scope carried from SF-3 (structural correspondences, not RG-derived gauge couplings).

**Build-rule compliance:** unique obligation (disjoint exhaustive mode-partition), orthogonal to CONSIST-2 (one value, two channels) and CONSIST-1 (V=12 shell). SF-3 itself names this the strongest single §10 thread. Roadmap row → built (eight remain); caption + abstract (three built members) updated; v0.3→v0.4. Also fixed a perl-mangled `\leftrightarrow` in the v0.3 roadmap intro line. Compiles clean: `pdflatex` ×2, 10 pp, 0 errors, 0 undefined refs/cites, 0 overfull. Bundles `reasoning/1318.md`. Registration deferred to ship-time.



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

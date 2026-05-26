# OPEN-SD-CHIR-PRIMITIVE — Manifestation Inventory

**Location:** `/CPP/series_umbrella/series_substrate_chirality_arc/manifestation_inventory.md`
**Purpose:** Canonical tracker for the five named observable manifestations of the substrate's primitive chirality under the OPEN-SD-CHIR-PRIMITIVE umbrella problem. Per-manifestation closure status, closing paper, closing theorem, and current closure-trajectory machinery notes for the open manifestations.
**Established:** 26 May 2026 (Session 144 Patch 0571d — co-established with SSCA at the same Patch; consolidates manifestation-tracking content that previously lived split between `research_frontier.md` (umbrella entry), `frontier_sectors/SD.md` (substrate-dynamics sector entry), and F.1 §9 in-body inventory).
**Maintenance:** Updated at every SSCA paper SHIP that changes a manifestation's status, and at every regrouping Patch that adds or restructures the inventory.

---

## The umbrella problem

OPEN-SD-CHIR-PRIMITIVE was opened at Session 132 Patch 0434 in the wake of the THEO-SD-CHIR-1 cross-sector substrate-chirality unification theorem. It is the first programme-level umbrella entry in the CPP corpus — an OPEN entry that scopes a primitive feature of the framework (the substrate's chirality direction $\hat{n}$ and amplitude $\delta$) as a cross-sector unification target with multiple named manifestations.

The five manifestations are not arbitrary. They correspond to the five places in physics where the substrate's directional asymmetry is expected to surface as observable structure. The numerical magnitudes for manifestations (i)–(ii) coincide at $\chi/6 \approx 0.0394$ — different physical mechanisms producing the same number is the unification-at-magnitude-level claim that organizes the arc. Manifestations (iii)–(v) may or may not share this magnitude; the framework expects different magnitudes from different mechanisms but a common substrate-primitive origin.

## Manifestation status table

| # | Manifestation | Sector | Status | Closing paper | Closing theorem(s) | Rigor level |
|---|---|---|---|---|---|---|
| (i) | K3-doublet mass-mixing chirality | SM | **CLOSED** | Capotauro v1.0 | THEO-CAP-1 | Publication-grade L3 |
| (ii) | Electroweak V−A coupling (substrate-level) | SEW | **CLOSED** | Capotauro v2.0 | THEO-SD-CHIR-1 | Publication-grade L3 |
| (ii) | Electroweak V−A coupling (Layer 4 EFT) | SEW | **CLOSED** | Chirality Continuum | THEO-CHIR-CONT-2 | Layer 4 EFT |
| (iii) | Electromagnetic-handedness | SEM | **OPEN** | — | — | — |
| (iv) | Thermodynamic causal-arrow direction | SD | **CLOSED at sketch-document L3** | F.1 Dynamical Substrate Law | THEO-DSL-3 | Sketch-document L3 (umbrella) + Publication-grade L3 (building blocks) |
| (v) | Cosmological-vacuum asymmetry | SD / cosmology | **OPEN** | — | — | — |

## Per-manifestation detail

### (i) K3-doublet mass-mixing chirality — CLOSED

**Status:** CLOSED at publication-grade Layer 3 by Capotauro v1.0 (Session 122 Patch 0415, 16 May 2026).
**Closing theorem:** THEO-CAP-1 (Composite Capotauro Wigner-Eckart Theorem) deriving $|M| = \chi/6 = \phi^{-3}/6 \approx 0.0394$ on the K3-doublet from a single Wigner-Eckart factorization on the substrate's broken-symmetry order parameter.
**Empirical anchor:** Leptogenesis back-derivation matches within 2% ($\Delta p_{LR}^{\text{obs}} \approx 0.04$ vs predicted 0.0394).
**Closing paper:** `capotauro/capotauro.tex` (v1.0 SHIPPED + v2.0 v1.0 SHIPPED).

### (ii) Electroweak V−A coupling — CLOSED in two stages

**Stage 1 (substrate-level): CLOSED at publication-grade Layer 3 by Capotauro v2.0 (Session 135 Patch 0479, 19 May 2026).**
- Closing theorem: THEO-SD-CHIR-1 (Cross-Sector Substrate Chirality Unification Theorem) — establishes $|M^{K3}| = |M^W| = \chi/6 \approx 0.0394$ at substrate level via three-way cross-sector unification (K3-doublet + W-bracelet + qDP/eDP).
- Substrate-level magnitude identity locked at flagship-paper rigor.

**Stage 2 (Layer 4 EFT): CLOSED by Chirality Continuum (Session 137 Patch 0509, 20 May 2026).**
- Closing theorem: THEO-CHIR-CONT-2 (SF-2 W-bracelet V−A coupling derivation) — derives the Michel $\rho = 3/4$ + 100% LH coupling at massless-helicity limit via topological-projection argument bridging substrate handle to effective coupling.
- Layer 4 EFT continuum-limit residual that the substrate-level closure did not directly predict.
- Joint closure with manifestation in SM-2 v2.0+ qDP/eDP chiral-polarity-bias via THEO-CHIR-CONT-3 (same paper).

**Closing papers:** `capotauro/capotauro.tex` (v2.0) + `chirality_continuum/chirality_continuum.tex` (v1.0).
**Two-stage closure reflects:** the substrate-level claim being structurally different from the Layer 4 EFT claim. Substrate-level closure establishes the magnitude identity; Layer 4 EFT closure establishes the observable-coupling structure.

### (iii) Electromagnetic-handedness — OPEN

**Status:** OPEN. No paper initiated. No current closure-trajectory machinery.
**Expected closure-trajectory machinery:** likely a cross-sector argument relating the substrate's primitive direction $\hat{n}$ to the photon's polarization structure, possibly via the substrate-handle-to-effective-coupling bridge methodology established at THEO-CHIR-CONT-1. Whether the photon sector inherits a substrate-handle analogous to the W-bracelet substrate-handle is the first sub-question.
**Predicted magnitude (if any):** unknown. The framework expects a substrate-primitive origin but may produce a different observable magnitude than $\chi/6$ via different cage-shell + pairing-convention machinery.
**Tracking:** Listed in `research_frontier.md` OPEN-SD-CHIR-PRIMITIVE entry as manifestation (iii).

### (iv) Thermodynamic causal-arrow direction — CLOSED at sketch-document Layer 3

**Status:** CLOSED at sketch-document Layer 3 by F.1 Dynamical Substrate Law v1.0 (Session 142 Patch 0570, 24 May 2026).
**Closing theorem:** THEO-DSL-3 (substrate-locality umbrella) — establishes $\vec{j}_{DI}^{\,\text{net}}(v_{\text{host}}) = (6\delta/\phi^2)\hat{n} + \mathcal{O}(\delta^2)$. The first-shell-only dependence at first order in $\delta$ is what makes the thermodynamic arrow's substrate-level origin propagate as a *local* phenomenon rather than a non-local one.
**Rigor level:** sketch-document Layer 3 (umbrella), with three publication-grade Layer 3 hardened-theorem inputs (THEO-DSL-1 perturbation-locality propagation + THEO-DSL-2 first-shell perpendicularity + Theorem 5.1 host-to-first-shell uniform projection) and the post-SHIP G1 publication-grade hardening at Patch 0571 (`hardened_theorems/first_shell_inner_product_primitive.tex`). The four-artifact publication-grade sequence is complete; the umbrella itself remains at sketch-document Layer 3 pending its own dedicated hardening Patch.
**Open umbrella-internal items at F.1 §9:** OPEN-FP-F1-1 ($\mathcal{O}(\delta^2)$ extension); OPEN-FP-F1-2 (Layer 4 axiomatic derivation of Mechanism A from CPP A1–A11); OPEN-FP-F1-4 = manifestation (v) of this inventory (Sector-5 schema instantiation); OPEN-FP-F1-5 (non-vertex-aligned Reading C variants); OPEN-FP-F1-6 (prose-density tightening). OPEN-FP-F1-3 (G1 publication-grade hardening) was closed at Patch 0571.
**Closing paper:** `dynamical_substrate_law/dynamical_substrate_law.tex` (v1.0 SHIPPED).

### (v) Cosmological-vacuum asymmetry — OPEN

**Status:** OPEN. Registered as OPEN-FP-F1-4 in F.1's §9 inventory.
**Expected closure-trajectory machinery:** likely cosmological-nucleation arguments parallel to Capotauro's sub-claim (a) work. The manifestation would act as a substrate-level boundary condition: at some cosmological epoch, the substrate's primitive direction $\hat{n}$ was fixed (rather than averaged over a degenerate orientation manifold), with the selection mechanism being the closure question.
**Connection to existing open work:** OPEN-SM-4 sub-claim (a) (Capotauro nucleation event) is the closest existing trajectory anchor. Whether manifestation (v) reduces to sub-claim (a) or is a structurally distinct question is itself a sub-question.
**Predicted magnitude (if any):** unknown. The cosmological-vacuum asymmetry produces, downstream, the matter-antimatter asymmetry $\sim 10^{-10}$; the connection between the substrate's primitive direction and the baryon asymmetry passes through the leptogenesis chain that Capotauro v1.0 already engaged.
**Tracking:** Listed in `research_frontier.md` OPEN-SD-CHIR-PRIMITIVE entry as manifestation (v); listed in F.1 §9 as OPEN-FP-F1-4.

## Theorem-naming conventions across the arc

Each arc paper introduces its own theorem chain under a paper-specific naming convention. The three chains are not duplicates of each other; they cover different scope-and-rigor combinations:

- **THEO-CAP-N** — Capotauro paper theorems. N=1: Composite Capotauro Wigner-Eckart Theorem (the K3-doublet closure that the original v1.0 paper rests on).
- **THEO-SD-CHIR-N** — Substrate-Dynamics Chirality cross-sector theorems. Registered at programme level (not paper-bounded), reflecting cross-sector unification scope. N=1: Cross-Sector Substrate Chirality Unification Theorem (Capotauro v2.0); N=2: third-sector unification extension (Capotauro v2.0 qDP/eDP).
- **THEO-CHIR-CONT-N** — Chirality Continuum paper theorems. N=1: Substrate-Handle-to-Effective-Coupling Bridge (sector-agnostic); N=2: SF-2 W-bracelet V−A coupling derivation; N=3: SM-2 qDP/eDP chiral-polarity-bias derivation.
- **THEO-DSL-N** — Dynamical Substrate Law paper theorems. N=1: perturbation-theory propagation rule (publication-grade L3); N=2: first-shell geometric identities (publication-grade L3 conditional on G1, then unconditional post-G1-hardening); N=3: substrate-locality umbrella (sketch-document L3).

## Methodology cross-references

The arc's methodology patterns are documented in `README-SSCA.md` §"Methodology cross-references" and codified at the corpus level in `methods_catalogue/methods_catalogue.md` under METH-CHIR-CONT-1 through METH-CHIR-CONT-4 (and any subsequent METH-CHIR-N entries that future arc closures introduce).

## Arc retirement criterion

The OPEN-SD-CHIR-PRIMITIVE umbrella retires when all five manifestations are CLOSED at minimum sketch-document Layer 3 rigor. Current status: three of five closed (i, ii at both stages, iv); two open (iii, v). Estimated arc retirement: 10–30 sessions per the substrate-chirality programme cadence, contingent on machinery maturation for manifestations (iii) and (v).

When the umbrella retires, this inventory file remains as historical record. The SSCA sub-umbrella folder remains in place (the arc's papers are not relocated post-retirement). The arc's status becomes "completed arc" in the SU taxonomy; no new papers are added to it.

---

— Established at Patch 0571d (26 May 2026); arc-level README cross-reference `README-SSCA.md` (this folder); umbrella-entry cross-reference `research_frontier.md` OPEN-SD-CHIR-PRIMITIVE; SU-level cross-reference `series_umbrella/README-SU.md`; OS discipline cross-reference `templates/operating_system.md` §15.13 (Patch 0571f).

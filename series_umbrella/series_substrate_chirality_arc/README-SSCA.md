# Substrate-Chirality Arc (SSCA)

**Location:** `/CPP/series_umbrella/series_substrate_chirality_arc/`
**Purpose:** First sub-umbrella inside the Series Umbrella (SU). Groups the three CPP flagship papers organized under the OPEN-SD-CHIR-PRIMITIVE umbrella problem — Capotauro, Chirality Continuum, and F.1 Dynamical Substrate Law. The arc is structurally ongoing: three of the umbrella's five named manifestations are closed at varying rigor levels; two remain open.
**Established:** 26 May 2026 (Session 144 Patch 0571d — co-established with SU at the same Patch as the first sub-umbrella; the SSCA papers were migrated from `flagship_papers/{capotauro,chirality_continuum,dynamical_substrate_law}/` into this folder via `git mv` to preserve paper history).
**Canonical tracker:** `manifestation_inventory.md` (this folder) — the five-manifestation enumeration of OPEN-SD-CHIR-PRIMITIVE with current closure status per manifestation.

---

## The umbrella problem

OPEN-SD-CHIR-PRIMITIVE is the first programme-level umbrella entry in the CPP corpus, opened at Session 132 Patch 0434 in the wake of the THEO-SD-CHIR-1 cross-sector substrate-chirality unification theorem. Programme-level umbrella entries sit structurally above individual paper-bounded open problems; they scope a primitive feature of the framework as a *cross-sector* unification target, with multiple named manifestations that the framework expects to close one at a time as the mathematical machinery for each matures.

The substrate-chirality umbrella scopes the substrate's primitive chirality — characterized by a unit vector $\hat{n}$ in the four-dimensional substrate space and a dimensionless amplitude $\delta$ — as the framework-level origin of five distinct observable consequences. The five manifestations are not arbitrary; they correspond to the five places in physics where the substrate's directional asymmetry is expected to surface as observable structure:

1. **Mass-mixing chirality on the K3-doublet** — the chirality matrix element that controls parity violation in weak-interaction processes acting on charged leptons. Predicted magnitude $\chi/6 \approx 0.0394$.
2. **Electroweak V−A coupling** — the Standard Model's V−A current structure for the W boson, observed at 100% LH coupling in the massless-helicity limit.
3. **Electromagnetic-handedness** — substrate-level chirality entering electromagnetic phenomenology, still to be made precise.
4. **Thermodynamic causal-arrow direction** — the direction of time at substrate level, manifest as a directional bias in the information-bit current dynamics.
5. **Cosmological-vacuum asymmetry** — the universe-wide selection of one chirality sign at some cosmological epoch.

The arc's papers attack these manifestations one at a time, with the closure ordering driven by which mathematical machinery has matured rather than which manifestation is most foundational.

## The three arc papers

### Capotauro (v1.0 + v2.0)

**v1.0 SHIPPED 16 May 2026 Session 122 Patch 0415.** Substrate-vacuum chirality as primitive feature paper. Derives $|M| = \chi/6 = \phi^{-3}/6 \approx 0.0394$ on the K3-doublet via THEO-CAP-1 (the Composite Capotauro Wigner-Eckart Theorem). Primary empirical prediction $\Delta p_{LR} \approx 0.0394$ validated within 2% of the leptogenesis back-derived value $\sim 0.04$. Closes manifestation (i) of OPEN-SD-CHIR-PRIMITIVE.

**v2.0 v1.0 SHIPPED 19 May 2026 Session 135 Patch 0479.** First flagship paper in CPP to undergo a substantive v2.0 extension. Adds three-way cross-sector substrate-level unification $|M^{K3}| = |M^W| = |M^{qDP}| = \chi/6 \approx 0.0394$ via Theorems THEO-CAP-1 + THEO-SD-CHIR-1 + THEO-SD-CHIR-2. Closes manifestation (ii) at substrate level (the Layer 4 EFT closure of manifestation (ii) is Chirality Continuum's contribution). Introduces Reading C as the substrate-orientation choice via FI-C-RC-1 (primitive 4D direction $\hat{n}$) and FI-C-RC-2 (vertex-aligned reading at Layer 2).

Folder: `capotauro/` (within this SSCA folder).

### Chirality Continuum

**v1.0 SHIPPED 20 May 2026 Session 137 Patch 0509.** Second Layer 4 cross-sector closure in CPP (after SF-4 v4.0). First flagship paper in the corpus to adopt the ex ante joint-paper format at Patch 0484 viability decision gate. Three programme-level theorems registered at paper level: THEO-CHIR-CONT-1 (sector-agnostic substrate-handle-to-effective-coupling bridge), THEO-CHIR-CONT-2 (SF-2 W-bracelet V−A coupling derivation; Michel $\rho = 3/4$ + 100% LH at massless helicity limit), THEO-CHIR-CONT-3 (SM-2 qDP/eDP chiral-polarity-bias derivation; leptogenesis CP-asymmetry $\Delta p_{LR} \approx 0.0394$). Closes manifestation (ii) at Layer 4 EFT and jointly closes the SM-2 v2.0+ qDP/eDP chiral-polarity-bias open problem.

First CPP flagship to achieve three-reviewer convergence at first reviewer round each — strongest external validation pattern in programme history.

Folder: `chirality_continuum/` (within this SSCA folder).

### F.1 Dynamical Substrate Law

**v1.0 SHIPPED 24 May 2026 Session 142 Patch 0570.** First F-line flagship in CPP corpus history. F-line is reserved for flagships closing OPEN-SD-CHIR-PRIMITIVE umbrella manifestations beyond the chirality-spatial-sector scope. F.1 closes manifestation (iv) at sketch-document Layer 3 via Theorem 7.1 substrate-locality umbrella with closed-form first-order result $\vec{j}_{DI}^{\,\text{net}}(v_{\text{host}}) = (6\delta/\phi^2)\hat{n} + \mathcal{O}(\delta^2)$. Three publication-grade Layer 3 hardened-theorem inputs (Theorems 5.1 + 5.2 + 6.1) at `hardened_theorems/`, plus the post-SHIP G1 publication-grade hardening at Patch 0571 (`first_shell_inner_product_primitive.tex`) completing the four-artifact sequence.

Six in-body open problems registered (OPEN-FP-F1-1 through OPEN-FP-F1-6) at v1.0 SHIP; OPEN-FP-F1-3 closed at Patch 0571. The remaining five are tracked in the F.1 paper's §9 inventory and in `manifestation_inventory.md` (this folder).

Folder: `dynamical_substrate_law/` (within this SSCA folder).

## Closure status

Per `manifestation_inventory.md`:

| Manifestation | Status | Closing paper / theorem |
|---|---|---|
| (i) K3-doublet mass-mixing chirality | CLOSED | Capotauro v1.0 / THEO-CAP-1 |
| (ii) Electroweak V−A coupling — substrate | CLOSED | Capotauro v2.0 / THEO-SD-CHIR-1 |
| (ii) Electroweak V−A coupling — Layer 4 EFT | CLOSED | Chirality Continuum / THEO-CHIR-CONT-2 |
| (iii) Electromagnetic-handedness | **OPEN** | (no current closure-trajectory machinery) |
| (iv) Thermodynamic causal-arrow direction | CLOSED at sketch-document L3 | F.1 / THEO-DSL-3 |
| (v) Cosmological-vacuum asymmetry | **OPEN** | (registered as OPEN-FP-F1-4) |

## Methodology cross-references

The arc has produced four programme-level methodology patterns that apply beyond SSCA:

- **Programme-level umbrella registration** (Session 132 Patch 0434) — OPEN-SD-CHIR-PRIMITIVE was the first OPEN entry that scoped a primitive feature across multiple manifestations rather than a paper-bounded question. The pattern templates future programme-level umbrella entries.
- **Ex ante joint-paper format** (Chirality Continuum Patch 0484) — the decision to author a single paper closing two sectors at Layer 4 EFT, rather than two separate sector-bounded papers. Reviewer-validated at v1.0 SHIP.
- **Sketch-document Layer 3 umbrella with publication-grade Layer 3 building blocks** (F.1 v1.0 SHIP) — the scope-honest framing where an umbrella theorem stays at sketch-document level while its inputs reach publication-grade level, with conditional clauses spelled out in-headline rather than buried. The convergent reviewer verdict on this framing established it as a corpus-wide methodology pattern.
- **Four-artifact hardened-theorem sequence** (F.1 Patches 0550 + 0551 + 0552 + 0571) — the discipline of producing each hardened theorem as a standalone `hardened_theorems/<name>.tex` artifact with five-class exclusion enumeration, rather than burying the hardening in the paper's main text.

## Future trajectory

The two remaining manifestations are open with no current closure-trajectory machinery:

- **Manifestation (iii) electromagnetic-handedness** — what substrate-level chirality contributes to electromagnetic phenomenology. The closure-trajectory machinery would likely involve a cross-sector argument relating the substrate's primitive direction to the photon's polarization structure. No paper has been initiated.
- **Manifestation (v) cosmological-vacuum asymmetry** — what substrate-level chirality contributes at cosmological scale; the universe-wide selection of one chirality sign at some epoch. Registered as OPEN-FP-F1-4 in F.1's §9 inventory. The closure-trajectory machinery would likely involve cosmological-nucleation arguments parallel to Capotauro's sub-claim (a) work, with the manifestation acting as a substrate-level boundary condition.

The arc remains active. Future closures may add a fourth paper (either as an F-2 paper closing manifestation (iii) or (v), or as a joint paper closing both, or as a v3.0 extension of an existing arc paper). The arc retires when all five manifestations are closed — projected over the next 10–30 sessions per the substrate-chirality programme cadence.

## Files in this folder

- `README-SSCA.md` — this file.
- `manifestation_inventory.md` — canonical five-manifestation tracker with closure status, theorem-naming conventions, and per-manifestation closure-trajectory machinery notes.
- `capotauro/` — Capotauro v1.0 + v2.0 paper folder.
- `chirality_continuum/` — Chirality Continuum paper folder.
- `dynamical_substrate_law/` — F.1 Dynamical Substrate Law paper folder.

---

— Established at Patch 0571d (26 May 2026); paper-tracker reference `manifestation_inventory.md` (this folder); programme-level umbrella reference `research_frontier.md` OPEN-SD-CHIR-PRIMITIVE entry; SU-level discipline reference `templates/operating_system.md` §15.13 (Patch 0571f).

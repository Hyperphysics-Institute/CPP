# DM Project Map — arc state, conditionals, and cross-window dependencies

**Maintained in:** `series_phenomena/cosmology/dark_matter/` (DM lane). **Last updated:** Session 156, 10 June 2026 (Patch 0845).
**Purpose:** one place to see where the DM identification program stands, what DM-1 is conditional on, and which parallel window (900 chirality / 1000 Project C / 1100 cosmological constant) bears on each dependency. Inferred from corpus structure; confirm against the live windows.

---

## 1. The two papers

- **DM-1** — *does qDP/hTetra meet the empirical DM criteria?* Microphysics + positive discriminant. Draft: `DM-1_draft_manuscript.md`. **Scientific core largely written** (§4–§7 filled); remaining = polish, figures, one specific-dwarf fit, and the §8 calibrated inputs. **Shippable as a conditional discriminant paper now** (see §4 below).
- **DM-2** — *the Sea-gravitation gate* (`sea_gravitation/`, OPEN-SR-5). The cosmological identification leg. A→D **traversed twice, no kill, conditional**. The "uniform Sea does not gravitate" half is essentially in hand (Seeliger / Milne–McCrea; ∇(ΔSSV); D2 separable from the strong-field closure, condition (a) closed at Step 2a). The open half is the **Λ-suppression coefficient + horizon selection** (Step C partial / Step D conditional). Could be split into a small, orthogonal "inert uniform Sea" paper (Steps A/B/1/2a) fenced off from the Λ files.

## 2. DM-1's two conditionals — different kinds

| Conditional | What it is | Owner / lane | Does it block DM-1? |
|---|---|---|---|
| **CONJ-COSMO-1** | The paper's *premise*: DM = charge-neutral qDP/hTetra aggregates | DM arc (ours) | No — it is the subject, not a blocker |
| **Mechanism A** | A *rate law* posited in the F.1 DSL (§3–§4); discharge = **OPEN-FP-F1-2** (derive it from Axioms A1–A11, Layer 4) | F.1 / chirality lane (900); DM consumes the NESS measure read-only | No — DM-1 ships conditional, exactly as the F.1 chirality results do |

**Key fact:** Mechanism A is the *single shared residual* of the chirality arc and the DM arc. One Layer-4 derivation of it (OPEN-FP-F1-2, in the 900 lane) discharges it for **both** arcs at once — makes the chirality TARROW-2 W3→W1 move unconditional *and* grounds μ², *and* makes DM-1's results unconditional on that axis. Nobody does a separate "Mechanism A for DM."

## 3. Confirming CONJ-COSMO-1 (the identification program) — three legs

1. **Discriminant — DONE (this session, 0830–0843).** Derived velocity-independent σ_V/m ≈ 0.20 cm²/g; mild flat dwarf cores; distinguishes qDP/hTetra from collisionless CDM *and* velocity-dependent SIDM; falsifiable. This is the positive content that lifted the candidate above consistency-grade.
2. **DM-2 Sea gravitation — conditional (0720–0814).** Traversed no-kill; open piece = the Λ coefficient ↔ **1100 (cosmological constant) window**. Coordinate, don't race.
3. **Step 4 / structure formation — the WEAK LINK (ours).** Registered NOT confirmed: swirl-seed origin is causal/active-source → defect-spectrum wall (no super-horizon adiabatic correlations). Tied to EU-1 for seeds. The genuinely unfinished physics of the identification.

## 4. Window dependency map

| Window | Working on | Bears on | DM-1 relationship |
|---|---|---|---|
| **900 chirality** | the chirality arc; OPEN-FP-F1-2 is its named priority | **Mechanism A** (shared residual) | Discharging it makes DM-1 unconditional on Mechanism A — and chirality unconditional too. Not a blocker for shipping. |
| **1000 Project C** | Λ_QCD / DP scale from l_P + sea_strength (`op:lambda_psr`) | **the absolute mass scale** (DM-1 §8; would tighten f) | A §8 calibrated-input polish. Neither of DM-1's two conditionals. |
| **1100 cosmological constant** | the vacuum-energy / Λ piece | **DM-2 Λ-suppression coefficient** (a CONJ-COSMO-1 sub-dependency via DM-2) | The one real cross-window coordination point for full identification. |

## 5. Are we waiting?

- **For the conditional discriminant paper (DM-1):** No — not on any window. Ships conditional on CONJ-COSMO-1 (premise) and Mechanism A (stated standing condition, inherited from F.1).
- **For full confirmation of CONJ-COSMO-1:** Coordinate with **1100** on the DM-2 Λ coefficient; resolve **Step 4** (ours); the discriminant is done. Not waiting on 900 or 1000 for the conjecture.
- **For DM-1's results to become unconditional on Mechanism A:** whenever **900** lands OPEN-FP-F1-2 — a hard Layer-4 derivation, high-leverage (retires the shared conditional for both arcs), not guaranteed quick. Not required for shipping; it is an *upgrade*, not an *unblock*.

## 6. Lane / collision discipline

- DM work (DM-1, 0830–0845) lives entirely in `dark_matter/` — no shared-file touch; collision-safe vs all three windows.
- DM-2 *reads* `sea_gravitation/` but writes nothing there from the DM lane.
- OPEN-FP-F1-2 (Mechanism A) would touch `dynamical_substrate_law/` (F.1), distinct from Project C's `op:lambda_psr` (DP scale) and 1100's Λ files — collision-safe across the parallel windows.
- DM-2 Λ files (`sea_gravitation/stepC_*`, `stepD_*`) overlap 1100's cosmological-constant work — the **one** place to flag before either window edits.

## 7. Arc patch index (DM lane, Session 156)

0830–0836 Era-2 microphysics chain · 0837–0839 TODO-016 / Project C handover · 0840 σ/m(v) discriminant · 0841 viscosity σ_V/m ≈ 0.20 · 0842 dwarf core radius · 0843 5:1 ratio scoping (route B) · 0844 DM-1 draft + DM-2 reassessment · 0845 this map.

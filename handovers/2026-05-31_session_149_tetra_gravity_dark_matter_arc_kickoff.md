# HANDOVER — Tetra-Gravity Dark-Matter Derivation Arc (CONJ-COSMO-1)

*Carry this whole document into a fresh context window as the opening prompt. It doubles as the program sketch — there is no separate sketch. Date: 31 May 2026, Session 149 (parallel to the chirality primitive-vs-emergent arc running in the other window, currently ~patch 0685).*

---

## LINE 1 — BLOCKING CLONE-AND-GREP GATE (do this before touching anything)

Before registering any ID, placing any file, or computing any coefficient:
1. `git clone` (or pull) the CPP repo to a clean working clone; `cd ~/Documents/GitHub/CPP`.
2. **Confirm patch 0700 is free** (`grep -rn "Patch 0700" .` should be empty). If taken (the chirality window may have advanced), hop to the next free contiguous block (0710, 0720…) and use it consistently for the whole arc.
3. **Read, in this order, before any work:** `founders_vision.md` §6c (the canonical source for this arc — the full vision + the four gates + the 31-May Update); `frontier_sectors/SR.md` OPEN-SR-3/4/8 (the GR status); the SR-1 gravity content (`series_relativity/papers/SR-1_special_relativity_emergence.tex` + `mechanism-SR-1.md`); `frontier_sectors/CONJ.md` (existing CONJ numbering); `theorem-registry.md` header + SS/SD sections (do NOT edit the header changelog / DSL rows / Summary Statistics — those are the chirality window's live-collision zone).

This gate exists because skipping it caused the Session-146 misgrounding, and because today a planned `0673` label collided with the other window's already-pushed `0673` — verify, don't assume.

---

## CANONICAL KICKOFF SENTENCE

> "Open the tetra-gravity dark-matter arc at patch 0700 by registering OPEN-COSMO-DM-1 + CONJ-DPS-1/2/3 + CONJ-COSMO-1, then run the falsification-first sequence — Step 0 (weak-field SSV force law) → Step 1 (σ/m vs SIDM bound) → Step 2 (free-vs-baryon-bound bookkeeping) — and do NOT begin any paper/anthology framing until Steps 1 and 2 are computed and survive."

---

## 0. THE KERNEL (what we are deriving)

In SR-1, gravity is sourced by stored energy density: a mass raises the static excess Space Stress Vector (ΔSSV) in the Dipole Sea, and the gradient of ΔSSV is gravity. The new realization (founders_vision.md §6c): the four DP species emit **different** SSV (eDP < qDP < hTetra), so **a compositional inhomogeneity in the vacuum is automatically a gravitational inhomogeneity** — a CPP-native handle on dark matter that standard physics lacks. The conjecture: concentrations of qDP + hTetra (net-neutral, cold, collisionless at halo densities), seeded by early-universe radial-expansion "swirls," are the entity now called dark matter.

**Source of record:** `founders_vision.md` Part V §6c "Dipole-Sea Composition" (Patch 0672a). Everything below is downstream of that entry. Read it first.

## STATUS (as of handover)

The conjecture **qualitatively clears all four gates** (per the §6c 31-May Update):
- **Gate 1 (collisionless):** survivable — for a net-neutral qDP/hTetra the only long-range force is gravity (energy monopole); the EM/dipole limit cancels at range and the color/bonding limit is short-range (contact-scale), so the medium is collisionless at low halo densities. Subquantum cross-section + low density → negligible cloud-cloud collision rate (Bullet Cluster behavior). *(The earlier "SR-1's all-force unification sharpens this" worry was withdrawn — the forces act at different ranges.)*
- **Gate 2 (EM-quiet):** clear — net-neutral structures are electromagnetically dark at range.
- **Gate 3 (halo profile):** survivable — collisionless ⇒ non-dissipative ⇒ cannot collapse to a disk ⇒ stays an extended, dispersion-supported halo; the ρ∝1/r² / NFW flat-rotation-curve profile is a *generic* outcome of collisionless gravitational dynamics, not special qDP/hTetra microphysics.
- **Bookkeeping gate:** open — the baryon frame is itself hybrid-tetrahedral, so free qDP/hTetra must outweigh the already-baryonic population ~5:1 without double-counting.

**Qualitative clearance means "no obvious showstopper," NOT "derived."** Five quantitative checks remain (below). At least two of them have killed otherwise-beautiful DM models. **This arc is falsification-first: the first deliverables are the calculations that could break the model, not the writeup.**

## GR STATUS (corrected at handover — the gravity sector is largely BUILT)

The SR companion-paper set (`series_relativity/SR_companion_papers/`, restored from Archive 31 May 2026) develops gravity far beyond what the SR.md frontier dashboard reflects (the dashboard is STALE — it still lists OPEN-SR-4/SR-8 as OPEN with a "weak-field GR derived; full nonlinear not yet proved" note; reconcile it as a hygiene item, see below). What actually exists:

- **c05 (Newtonian gravity from SSV shell-broadcast):** derives **F = G m m'/r²** with **G = ℏc/m_P² exact** (CODATA-matching, zero free parameters, fixed by the 600-cell). Gravity is universally attractive because mass-energy SSV is unsigned (no polarity cancellation); 1/r² from shell-broadcast geometry; inertial = gravitational mass by construction.
- **c07 (weak-field GR):** weak-field isotropic Schwarzschild metric, geodesic motion, equivalence principle, and the factor-of-two lensing (temporal + spatial curvature, 1.75″) — no free parameters; also derives μ₀/ε₀/Z₀ from the lattice and GWs at c.
- **c08 strong-field GR, c11 Kerr, c12 Kerr-Newman, c09 GW echoes, c10 Hawking/Planck-remnant, c13 superradiance** also present (extent to be audited, but the sector is clearly substantial).

**Implication for this arc:** the weak-field Newtonian force law the rotation-curve dynamics ride on is **already derived (c05)** — `mass → ΔSSV → 1/r² acceleration` with G fixed. The DM arc is therefore **not blocked on a gravity derivation.** This removes the one structural risk flagged in the earlier draft of this handover.

## FALSIFICATION-FIRST WORK SEQUENCE (hard-ordered)

**Step 0 — Confirm the gravity foundation covers the application (mostly a citation/audit, NOT a derivation).** The weak-field Newtonian force law is already derived in **c05** (F = G m m'/r², G = ℏc/m_P²). Step 0 reduces to: (a) cite c05/c07; (b) confirm the regime of validity covers a *diffuse, extended, low-density galactic-halo* mass distribution (c05 is derived for point/shell sources — verify the superposition to a continuous halo density is clean and that nothing in the shell-broadcast assumes compact sources); (c) confirm collisionless test-mass orbits in this potential give the standard Newtonian rotation-curve relation v²(r) = G M(r)/r. If (b) surfaces a genuine gap for diffuse sources, that becomes a small derivation; otherwise Step 0 is a half-day audit. *(Side hygiene: reconcile the stale SR.md dashboard — OPEN-SR-4/SR-8 vs what c05/c07/c08 actually close.)*

**Step 1 — Gate 1 quantitative (σ/m vs SIDM bound). CHEAPEST POTENTIAL KILL — DO FIRST.** Compute the short-range bonding (qDP↔qDP, qDP↔hTetra, hTetra↔hTetra) momentum-transfer cross-section, integrated over halo-density encounter rates, and show σ/m ≲ ~1 cm²/g (the self-interacting-DM bound; for scale a nucleon sits *at* ~1 cm²/g, and these are subquantum). If σ/m exceeds the bound at halo densities, the model is at best collisional/SIDM and the cold-collisionless-DM identification fails here.

**Step 2 — Bookkeeping (free vs baryon-bound). SECOND CHEAPEST KILL.** From the freeze-out yields (the §6c skew + eDP:qDP=1:1 conservation lock + the hTetra sink), compute the ratio of *free* qDP/hTetra to qDP/hTetra *already bound into baryons*. For the free population to be dark matter it must be ~5× the baryonic mass, without double-counting the hybrid-tetrahedral content of nucleons.

**>>> HARD RULE: no paper, anthology, or "writeup" framing until Steps 1 and 2 are computed and survive. <<<**

**Step 3 — Coldness.** Estimate the qDP/hTetra velocity dispersion at decoupling; it must be COLD (warm/hot DM suppresses small-scale structure and is observationally constrained). Plausible for massive composite hTetras; must be shown.

**Step 4 — Power spectrum.** Show the early-universe "swirl" seeds (from radial-expansion collisions) can reproduce the observed matter power spectrum that standard cosmology obtains from inflationary perturbations.

**Step 5 — Quantitative halo / rotation curve.** Using the Step-0 force law + collisionless gravitational dynamics, reproduce ρ∝1/r² (or NFW) and approximately flat rotation curves quantitatively for a representative galaxy.

Only after Steps 0–5 survive: assemble for the multi-AI review panel (ChatGPT + Grok + Copilot) via the standard review-dispatch protocol, then consider paper/anthology.

---

## LOAD-BEARING ASSUMPTIONS (carry verbatim; each is a place the arc can break)

1. The qCP–qCP force is **attractive in the +qCP/−qCP configuration** (deepens the qDP well rather than fighting the electric binding). The qDP skew and the color-screening driver hang on this sign.
2. **hTetra binding > 2× hDP binding** (super-additive tetrahedral closure) — gives "common hTetras + scarce free hDPs" without fine-tuning.
3. **Collisionless / gravity-dominated commitment at halo scale.** Do NOT simultaneously lean on the bonding to *nucleate* halos and call it negligible for *collisionlessness*. Let gravitational instability do the clustering; bonding off-stage at halo density.
4. **Equal initial eCP:qCP inventory** (and roughly symmetric skimming into fermion cores) — required for the exact eDP:qDP = 1:1 conservation lock; the relation also tests this symmetry.

## REGISTRATION PLAN (patch 0700, the arc-opening patch)

Register, in `frontier_sectors/CONJ.md` and the frontier dashboard:
- **OPEN-COSMO-DM-1** — the tetra-gravity dark-matter derivation (umbrella work item; the falsification-first sequence above is its closure plan).
- **CONJ-DPS-1** — DP-sea skew + eDP:qDP 1:1 conservation lock + color-screening driver.
- **CONJ-DPS-2** — hTetra sink + freeze-out ordering + hTetra-binding > 2× hDP.
- **CONJ-DPS-3** — on-demand locally-generated hDP / W-bracelet beta decay (cross-link CONJ-SS-1).
- **CONJ-COSMO-1** — tetra-gravity dark matter (far-frontier; gated; depends on Steps 0–5).
- **Gravity foundation (already built):** cite c05 (Newtonian, G = ħc/m_P²) and c07 (weak-field GR). No new gravity prerequisite is needed for the weak-field application; OPEN-GRAV-SSV-GR-EXTENSION is NOT required. Flag the stale SR.md dashboard (OPEN-SR-4/SR-8) for reconciliation against c05/c07/c08.

`CONJ-DPS-*` / `CONJ-COSMO-*` are NEW sector prefixes (Dipole-Sea-population / cosmology). They did not exist at handover — confirm at the grep gate and mint deliberately.

## NUMBERING

Open at **0700**, run 0700, 0701, 0702… contiguously for this arc. The chirality window is at ~0685 and climbing; Thomas is watching for collision and will hop the arc to the next free block (0710/0720…) if the windows converge. Patch numbers are organizational labels — a label collision is harmless to `git am` (commit hashes differ; non-overlapping files), but keep the arc's labels distinct for sanity.

## POINTERS

- **Canonical vision source:** `founders_vision.md` Part V §6c (Patch 0672a).
- **Gravity mechanism:** SR-1 (`series_relativity/papers/SR-1_special_relativity_emergence.tex`, `mechanism-SR-1.md`); GR status: `frontier_sectors/SR.md` OPEN-SR-3/4/5/6/7/8.
- **Patch-delivery contract:** after `present_files` on a `.patch`, emit the apply-and-push macro, one clause per line with `&& \` continuation (incl. after `cd`); multiple patches = one macro with sequential `git am` lines.
- **Reasoning capture:** every physics patch bundles `.tex`/`.md` + verbatim reasoning fragment + verify script if it computes anything (per `templates/reasoning_capture_protocol.md`).
- **Review panel:** when a step's result is ready, open a self-contained review package per `templates/review_dispatch_protocol.md` (the THEO-SPIN-1 cycle this session is the recent template) and run ChatGPT + Grok + Copilot.

## SUPPLEMENTARY READING (for the Gate calculations — NOT line-1 blocking)

The SR companion set (`series_relativity/SR_companion_papers/`) characterizes much of the qDP/hTetra physics the Gates need. Read these as the relevant Gate is reached (not all up front):

- **Step 0 (force law):** `c05_newtonian_gravity_from_SSV` (F = G m m'/r², G = ℏc/m_P² exact) and `c07_weak_field_GR` (metric, geodesics, equivalence principle, factor-of-2 lensing). The rotation-curve dynamics ride on c05.
- **Gate 1 (σ/m — bonding cross-section):** `c02_dipole_stiffness_C` (the Dipole Sea stiffness C that normalizes the SSV quantum — the coupling strength behind both gravity and the bonding); `c06_DP_chaining_as_mass_and_EM_substrate` (DP/qDP chaining energetics); `c14_quark_confinement_qDP_chaining` (qDP–qDP confinement and chaining-length — directly bounds the "thermal collisions prevent significant chaining" claim and supplies the short-range bonding cross-section inputs); `c15_SU3_color_from_600-cell` (the color force at CP level — the *driver* of the qDP skew per CONJ-DPS-1, and the source for load-bearing assumption #1, the sign of the qCP–qCP force).
- **Gate 2 (bookkeeping) & Gate 3 (coldness):** `c04_ZBW_hbar_mass_units` (ZBW energy → mass/ℏ units → the qDP/hTetra masses needed for both the ~5:1 free-vs-bound ratio and the velocity-dispersion/coldness estimate); `c14`/`c15` again for the freeze-out yields.
- **hTetra / spin structure (cross-check):** `c20_Spin_I_emergent_Spin-Captured_DPs`, `c21_Spin_II_standing_wave_subharmonics`, `c22_Spin_III_…ZBW_standing_wave_spectrum` — the captured-DP/hTetra internal structure and ZBW spectrum. NOTE: cross-check these against **THEO-SPIN-1 (v1.1, multi-AI confirmed 3/3, this session)** — the spin/ZBW frequency ratio was corrected 2 → 2√2 (radius ratio 2); if the c20–c22 Sonnet-era papers still carry the old "2:1 frequency," that is a known correction, not a new result.

*Caveat:* the companion set was Archive-restored 31 May 2026 and predates parts of the current registry/protocol system; treat its results as authoritative physics but verify registry status (some "open" SR problems may already be closed here — see the todolist audit tickler). Do not let the audit block the DM Gate calculations.

## RELATIONSHIP TO THE PARALLEL CHIRALITY ARC

Independent physics; shared repository. The only coupling is the registry: both arcs edit `theorem-registry.md` / frontier files, so the clone-first/grep gate (Line 1) is mandatory every session to avoid the collision pattern. This arc stays out of the chirality window's live zones (registry header changelog, DSL rows, Summary Statistics).

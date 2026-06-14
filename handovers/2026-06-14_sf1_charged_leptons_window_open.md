# HANDOVER — SF-1 Charged-Leptons Flagship Window OPEN (dispatch from SF-7 window)

*Paste this whole document into a fresh context window as the opening prompt. This window's job: assemble the SF-1 charged-leptons flagship paper to v1.0. It was dispatched by the SF-7 grand-unification window (1300-band) on 14 June 2026. It runs in parallel with the SF-7 window and four others under a **lightweight single-operator collision protocol** (§0 below). **Patch band for THIS window: 1400–1499.** First free = 1400.*

---

## THE FIXED KICKOFF LINE (how this window was booted)

```
Bootup for Conscious Point Physics (CPP). Clone the repo and read the bootup file at https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/bootup.md. Honor the line-1 CLONE-FIRST GATE before registering any ID, placing any file, or computing any coefficient (clone the repo and grep the registry first). Then open the handovers/ folder, sort by filename, and read the most recent dated file — but for THIS window read this SF-1 dispatch specifically (2026-06-14_sf1_charged_leptons_window_open.md).
```

---

## LINE 1 — BLOCKING CLONE-AND-GREP GATE (do this before touching anything)

1. `git pull` (or clone) a clean working copy; `cd ~/Documents/GitHub/CPP`.
2. **Confirm 1400 is free:** `git log --oneline | grep -E '^[a-f0-9]+ 1400'` returns empty. If taken, hop to the next free contiguous label in 14xx and stay consistent. Never reuse a label already in `git log`.
3. **Read, in this order, before any work:** `flagship_papers/charged_leptons/sf-1_outline.md` (the drafting-ready outline) → `flagship_papers/charged_leptons/sketches/SF-1_structural_core.md` (the §3–§6 load-bearing core, worked out for direct `.tex` transfer) → `templates/paper-formatting.md` (the 16-section LaTeX standard you must follow).
4. **Do NOT edit shared registries** (`theorem-registry.md`, `predictions.md`, `frontier_sectors/*`, `master_glossary.md`, `paper_catalog.md`, `parallel_dev/lease_board.md`). The SF-7 window and four others append to those. Your registry touch (registering OPEN-FP-1-P3) is deferred to **ship time** and goes through a flagged integration patch after a refresh — see §6.

---

## CANONICAL KICKOFF SENTENCE

> "Assemble the SF-1 charged-leptons flagship to v1.0 in the 1400-band window. The outline (1302) and structural core (1307) are drafting-ready; the physics is shipped (SM-1/3/4/6) and needs **assembly, not derivation**. Build `flagship_papers/charged_leptons/sf-1_charged_leptons.tex` to the 16-section standard, then produce the CONV-001 single-block panel package for Thomas's multi-AI review. SF-1 ships first among the four predecessors and unblocks the δ_CP interconnection for SF-7."

---

## 0. THE LIGHTWEIGHT MULTI-WINDOW PROTOCOL (read this — it is how you interface with Thomas)

You are one of **six parallel windows** Thomas is running against a **single shared working tree** (`~/Documents/GitHub/CPP`) and a single `origin/main`. The other five: SF-7 grand-unification (1300-band, your dispatcher), Dark Matter, Chirality, Project C/DM, Cosmological Constant, and δ_CP neutrino prediction. (Full rules: `templates/new_window_protocol.md`.)

**This is NOT the heavy lease-board protocol** in `parallel_dev/multi_window_protocol.md` (that one mechanically guarantees collision-freedom via leases + a single-writer board + an audit, for the day untrusted/agentic workers run). You are running the **lightweight** version: collision-freedom comes from **one operator's serialized attention plus your discipline**, not from a mechanism. Your obligations:

1. **Own your band.** This window owns **1400–1499**. Never grab a number outside it; never reuse a label in `git log`. Disjoint bands across windows make patch-number collisions impossible by construction.
2. **Work greenfield.** Produce new own-files under `flagship_papers/charged_leptons/` wherever possible. Greenfield files never collide.
3. **WARN in the LAST paragraph.** Any time a task needs you to modify a file at collision risk — a shared registry (see §6), or another project's owned files — you **must flag it in the last paragraph of your reply** so Thomas cannot miss it. He then serializes: either he's only on this window (he applies immediately) or he's moving between windows (he tells you to refresh first).
4. **Refresh before commit/push.** Thomas will ask you to refresh against `origin/main` before he commits and pushes, especially for any registry edit. After you check clean, he pushes with the git macro. You produce patches; **you never push autonomously**.
5. **Defer + batch shared-registry edits.** Don't sprinkle registry edits across patches. Collect them into a single flagged integration patch at a milestone (here: SF-1 ship), applied after a refresh.

If you ever can't satisfy these (e.g., two windows genuinely must edit the same registry concurrently and Thomas can't serialize), say so and recommend escalating that round to the heavy lease-board protocol.

---

## 1. THE LARGER PROJECT — what SF-7 is and why this window exists

**SF-7 is the apex synthesis of the entire CPP programme:** a single paper proving that the six sector flagships cohere under **one substrate, one calibration ($m_e$), and the 600-cell**, with a family of **§10 cross-sector consistency theorems** as its core (no double-counting; single-$m_e$ across all 17 particles + W⁰; consistent mixing-sector sourcing). SF-7 is the artifact intended to raise the null hypothesis — *"the 9 CPP axioms are not at the root of all phenomena"* — to a level the conventional-physics community treats as implausible to dismiss, via swarm coherence (precision scaling as √N across zero-parameter predictions).

**SF-7 cannot draft at flagship quality until SF-1 through SF-6 ship.** Two are done (SF-2 electroweak v1.01, SF-4 neutrino v4.4). Four remain (SF-1, SF-3, SF-5, SF-6), each now with a drafting-ready outline + verified structural core. **SF-1 is the first to ship**, and that is the job of this window. The SF-7 window stays open as the integration seat (the §10 family + the six-way capstone).

---

## 2. WHY SF-1 MATTERS — its contribution to unification

SF-1 is small in lift but disproportionately important to the unification case:

- **It is the cleanest single-$m_e$ sector in the entire corpus.** One calibration ($m_e$), **zero shape parameters** — no $m_c$ quark-route caveat (SF-3), no $\eta$ boson-mass caveat (SF-2). It is therefore the **strongest rhetorical anchor** for the SF-line's "hierarchy without hierarchy" claim: the full charged-lepton spectrum from one mass + geometry.
- **It ships first → momentum.** Mostly reframing of shipped SM-1/3/4/6 at strong rigor; ~3–5 sessions to v1.0. The first predecessor to land sets the template the other three follow.
- **It is the δ_CP unblock.** This is the connection Thomas cares most about right now. The **SF-1↔SF-4 §10 consistency member** carries the OP-SM-7d phase / δ_CP electroweak handle, and that member is **gated on SF-1 shipping**. The δ_CP value the δ_CP window (window 5) is producing plugs into that §10 scaffold. So **the path to publishing δ_CP before it is measured runs through SF-1.** Shipping this paper is not a detour from the δ_CP goal — it is the load-bearing step toward it.
- **It seeds two §10 members.** On ship it unblocks **SF-1↔SF-2** (shared $\sin^2\theta_W = 3/(8\phi)$ spectral-trace, the edge-mode fraction) and **SF-1↔SF-4** (shared $M_0$; the δ_CP/phase handle). Both are SF-7 §10 capstone inputs.

---

## 3. THE TASK — assemble SF-1 to v1.0

The remaining work is **assembly + review, not derivation.** Per `SF-1_structural_core.md` §F:

1. **Assemble** `flagship_papers/charged_leptons/sf-1_charged_leptons.tex` to the 16-section standard (`templates/paper-formatting.md`). Transfer the core verbatim where it's worked out:
   - §3 ← Part A: the K3 Spectral Theorem → Koide $K = 2/3$ (carry the Layer A/B/C epistemic grading verbatim for credibility).
   - §4 ← Part B: the Weinberg angle $\sin^2\theta_W = 3/(8\phi)$ as the intermediate spectral-trace result.
   - §5 ← Part C: the Koide phase as the **closed SM-4→SM-6 arc** (lead with SM-4's impossibility theorem, then SM-6's EW correction — present as a completed arc, *never* as competing claims; this is the highest-value reframing in the paper).
   - §6 ← Part D: the mass spectrum ($m_\mu, m_\tau$ at zero shape params).
   - Wrap §1 (the charged-lepton mass problem), §2 (substrate + axioms + tetrahedral cage), §9 (falsifiers), §10 (SF-line placement: hooks to SF-2 and SF-4).
   - Include the **REQUIRED** subsections per the formatting standard: §"CP/GP Signature at This Scale" and §"Swarm-Validation Contribution" (PD-001).
   - Honor the clean title-page convention (no version-history paragraph; no CHANGELOG comment block in source — archaeology lives in `documentation_suite/changelog-sf-1.md`).
2. **Compile**, fix LaTeX, sanity-check the numbers against the headline table in §5 below.
3. **Produce the CONV-001 single-block panel package** (`templates/presentation_file.md` format: GitHub blob+raw links, one-paragraph ask, full rendered Markdown, 4-backtick outer fence) so Thomas runs the multi-AI review (ChatGPT ×N / Grok / Copilot) — **this review cycle needs Thomas's machinery; you prepare the package, he dispatches.**
4. **At ship:** register OPEN-FP-1-P3 via a flagged integration patch (§6).

**Filename discipline:** the canonical filename is `sf-1_charged_leptons.tex` with **no version suffix**; version history lives in the internal changelog file only.

---

## 4. ASSET INDEX (paths)

| Asset | Path |
|-------|------|
| SF-1 outline (drafting-ready) | `flagship_papers/charged_leptons/sf-1_outline.md` |
| SF-1 structural core (§3–§6 worked) | `flagship_papers/charged_leptons/sketches/SF-1_structural_core.md` |
| LaTeX standard (16-section) | `templates/paper-formatting.md` |
| Panel-package format (CONV-001) | `templates/presentation_file.md` |
| Source SM-1 (cage symmetry, charge quantization) | `series_standard_model/papers/SM-1_binding_mechanisms_and_cage_stability.tex` |
| Source SM-3 (K3 spectral theorem, K=2/3) | `series_standard_model/papers/SM-3_k3_spectral_theorem_koide_formula.tex` |
| Source SM-4 (mass formula + θ-impossibility) | `series_standard_model/papers/SM-4_charged_lepton_masses_from_k3.tex` |
| Source SM-6 v3 (Weinberg + phase derivation) | `series_standard_model/papers/SM-6_lepton_mass_spectrum.tex` |
| SF-7 strategic spine (context) | `flagship_papers/unification/sf-7_critical_path_map.md` |
| Lightweight protocol (full rules) | `templates/new_window_protocol.md` |

---

## 5. HEADLINE PHYSICS (sanity-check target — all shipped, zero new derivation)

| Quantity | CPP | Experiment | Agreement | Calibration |
|----------|-----|-----------|-----------|-------------|
| $\sin^2\theta_W$ | $3/(8\phi) \approx 0.2318$ | $0.23121$ | 0.24% | 0 (intermediate) |
| Koide $K$ | $2/3$ (exact) | 11 ppm consistency | exact | 0, conditional on P1–P3 |
| Koide phase $\theta$ | $132.731°$ | $132.732°$ | 0.003% | 0 |
| $m_\mu$ | $105.47$ MeV | $105.66$ | 0.18% | 0 shape param |
| $m_\tau$ | $1774.1$ MeV | $1776.9$ | 0.15% | 0 shape param |

Calibration ledger: **1 calibration ($m_e$, equivalently $\mathrm{SSV}_0 = m_e c^2/2$), 0 shape parameters.**

---

## 6. INHERITED-OPEN LEDGER + DO-NOT-EDIT REGISTRIES

- **Inherited-open:** **OPEN-FP-1-P3** — the Layer-B thermal-equilibration / Caldeira–Leggett system–bath model behind equal K3 eigenstate occupation; resolution path SS-4; empirically harmless ($\sim 10^{-20}$, nine orders below the 11 ppm precision). **Inherit, do not close.** Register it **only at SF-1 ship**, via a flagged integration patch to `theorem-registry.md` (and `predictions.md`/`frontier_sectors/FP.md` if applicable) applied **after a refresh against `origin/main`**.
- **Do-NOT-edit without a flagged integration patch + refresh:** `theorem-registry.md`, `predictions.md`, `frontier_sectors/*`, `master_glossary.md`, `paper_catalog.md`, `parallel_dev/lease_board.md`. All six windows append to these.

---

## 7. COLLISION STATUS + ADJACENCIES

- **SF-1 `.tex` assembly is collision-free.** Everything you produce during assembly is a new own-file under `flagship_papers/charged_leptons/` — no other window owns that path.
- **Downstream relationship, not a collision: window 5 (δ_CP).** δ_CP consumes the SF-1↔SF-4 §10 member you unblock on ship. No shared file during assembly; coordinate only at ship/integration time (and the integration patch is the SF-7 window's job, not yours).
- **The SF-7 window (1300-band) is your dispatcher/integrator.** It owns `flagship_papers/unification/*` and the §10 family. Don't write into `flagship_papers/unification/`; hand your ship up to it.
- **Honor rule 3:** if any task pushes you toward a shared registry or another window's files, flag it in your last paragraph before doing anything.

---

## 8. TRAJECTORY

~3–5 sessions to v1.0 from the current core (consistent with `sf-1_outline.md` §8). Sequence: assemble `.tex` → compile/verify → CONV-001 panel package → Thomas runs multi-AI review → revise to convergence → v1.0 ship + flagged integration patch (register OPEN-FP-1-P3, update `paper_catalog.md`/`README.md`). On ship, notify the SF-7 window so it can build the SF-1↔SF-2 and SF-1↔SF-4 §10 members.

---

*Dispatch from the SF-7 grand-unification window (1300-band), 14 June 2026. New file under `handovers/`; no shared-registry edits; collision-free. SF-1 window owns patch band 1400–1499, first free = 1400.*

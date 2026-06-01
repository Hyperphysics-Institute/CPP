# HANDOVER — CPP Cosmological-Sector Arc (OPEN-SR-5: Sea-Gravitation, Friedmann, and the Dark-Energy↔Dark-Matter Unification)

*Carry this whole document into a fresh context window as the opening prompt. It doubles as the program sketch — there is no separate sketch. Date: 31 May 2026, Session 149 continuation. Spun out of the tetra-gravity dark-matter arc (CONJ-COSMO-1), which paused cleanly at patch 0706 with all OPEN-SR-5-independent falsification gates survived. A separate chirality arc runs in another window (tip ~patch 0691 at this writing).*

---

## LINE 1 — BLOCKING CLONE-AND-GREP GATE (do this before touching anything)

Before registering any ID, placing any file, or computing any coefficient:
1. `git clone` (or pull) the CPP repo to a clean working clone; `cd ~/Documents/GitHub/CPP`.
2. **Confirm the opening patch number is free.** This arc opens at **0720** (the DM arc used 0700–0706; chirality is climbing through 069x). `grep -rn "Patch 0720" .` should be empty. If taken, hop to the next free contiguous block (0730, 0740…) and use it consistently.
3. **Read, in this order, before any work:**
   - `frontier_sectors/SR.md` **OPEN-SR-5** (elevated to scoped on Patch 0705 — it carries requirements (i)/(ii)/(iii) verbatim; this handover expands them) and OPEN-SR-3/6/7;
   - `series_phenomena/cosmology/dark_matter/R2_sea_gravitation_scoping.md` (the DM-arc analysis that produced this arc) and `scripts/0705_lambda_sea_estimate.py`;
   - `series_relativity/SR_companion_papers/c05_newtonian_gravity_from_SSV/` (gradient-sourced gravity — the crux) and `c07_weak_field_GR/`;
   - `series_relativity/SR_companion_papers/c08 strong-field_GR/development/development_notes.md` §8 (the unregistered vacuum-Sea Λ estimate);
   - `founders_vision.md` §6c (the Dipole-Sea composition + the dark-sector vision) and §"Big Bang" material;
   - `theorem-registry.md` header + SR/SD sections (do NOT edit the header changelog / DSL rows / Summary Statistics — chirality-window live zone).

This gate exists because skipping it caused the Session-146 misgrounding, and because this session repeatedly hit silent non-landings; **verify, don't assume.**

---

## CANONICAL KICKOFF SENTENCE

> "Open the CPP cosmological-sector arc at patch 0720 by registering OPEN-SR-5 sub-items (5a homogeneous-source/Friedmann, 5b suppression-derivation, 5c Sea-vs-matter distinction) + CONJ-COSMO-2 (dark-energy↔dark-matter unification from the one Sea), then run the falsification-first sequence — Step A (the homogeneous-source problem: can gradient-sourced gravity reproduce homogeneous-density-driven Friedmann expansion, or does it conflict with BBN/CMB? — CHEAPEST KILL, do first) → Step B (Sea-vs-matter distinction) → Step C (derive the Λ suppression, retire the (l_P/R_H)² coincidence) → Step D (recover the Friedmann equation) — and do NOT claim the dark-sector unification or unblock DM Steps 4–5 until Step A survives and Steps C–D are computed."

---

## 0. THE KERNEL (what we are deriving, and the prize)

CPP gravity (c05) is sourced by the **gradient** of the net Space Stress Vector: F = m'c²·k·∇(ΔSSV). A uniform field exerts no force. The DM arc (CONJ-COSMO-1) showed this makes a uniform Dipole Sea *locally* inert by construction — which is what lets Sea inhomogeneities (swirls) act as dark matter. The c08 development notes separately record that the uniform Sea's vacuum SSV could *be* the cosmological constant Λ.

**The prize:** if a single CPP cosmological sector can show that the **one** Dipole Sea yields, from one mechanism, both (a) a uniform-mode contribution that is the suppressed Λ (dark energy) and (b) inhomogeneity-mode gravity that is dark matter, then CPP unifies **two of cosmology's three dark puzzles** from one substrate. That is the headline result this arc targets (registered as CONJ-COSMO-2).

**But the same gradient-sourcing that enables the DM picture creates a sharp problem (Step A below): homogeneous matter/radiation density drives the Friedmann expansion, yet gradient-sourced gravity gives zero force for any homogeneous density. Reconciling this — without breaking BBN/CMB-era cosmology — is the make-or-break, and it is the first thing to confront.**

## 1. STATUS (what exists / what is missing)

**Exists:**
- **c05** — Newtonian gravity from SSV shell-broadcast; gravity = gradient of net SSV; G = ℏc/m_P² (see caveat: TODO-014, G is the Planck-mass definition rearranged — absolute scale is one shared calibration, not derived).
- **c07** — weak-field GR (metric, geodesics, equivalence principle, factor-2 lensing). **c08** — strong-field GR (exact Schwarzschild, singularity resolution). c11/c12 Kerr/Kerr-Newman, c09/c10/c13 present.
- **c08 dev notes §8** — an **unregistered** estimate: ρ_Λ ≈ α_geom·(E_P/l_P³)·(l_P/R_H)² ≈ observed (factor ~1.5 *with the particle horizon*). See §6 below for why this is not yet a derivation.
- **OPEN-SR-5** — elevated from a 23-March stub to a scoped problem on Patch 0705, carrying (i)/(ii)/(iii) and the bidirectional OPEN-COSMO-DM-1 link.

**Missing (the work of this arc):** the cosmological sector itself. c07/c08 explicitly list "cosmological solutions (Friedmann equations from homogeneous isotropic DP sea)" as **future** work. There is no Friedmann analog, no derived Λ suppression, no principled Sea-vs-matter gravitation distinction.

## 2. THE SCOPED REQUIREMENTS (carry verbatim — from OPEN-SR-5 / R2 scoping)

A single CPP cosmological sector must yield, from ONE mechanism (not three assumptions):
- **(i)** uniform Sea mode → vacuum/Λ contribution suppressed to ~observed magnitude, with the suppression factor **derived** — not the inserted (l_P/R_H)² of the c08 estimate.
- **(ii)** Sea inhomogeneities (swirls) → unsuppressed local-gradient gravity of dark-matter amplitude (c05 mechanism); the swirl spectrum also sets the DM/baryon ratio (DM-arc R1) and feeds the DM power spectrum (DM Step 4).
- **(iii)** the Friedmann expansion history (radiation → matter → Λ eras) recovered, including that uniform matter/radiation gravitate cosmologically even though the uniform *Sea* mode is suppressed — a principled Sea-vacuum-mode vs matter-overdensity distinction.

## 3. THE c08 Λ ESTIMATE AND WHY IT IS NOT YET A DERIVATION

`scripts/0705_lambda_sea_estimate.py` (in the DM arc) reproduces and stress-tests it:
- The factor (l_P/R_H)² ≈ 10⁻¹²² is exactly what turns the Planck density into ~the observed Λ — but that *is* the well-known Λ ~ 1/R_H² near-coincidence.
- The result swings ~10× on the horizon choice (Hubble length → 6.8× observed; particle horizon → 0.66×). CPP fixes neither the horizon nor *why* ρ_vac ~ 1/R_H².
- R_H grows with cosmic time, so a vacuum density tracking 1/R_H² is *dynamical*, inheriting (not solving) the "why now" coincidence problem.
- **Therefore:** treat the c08 estimate as a suggestive numerical target, NOT a result. Step C's job is to derive the suppression (or show it cannot be derived). Do not register or cite it as a derivation — this arc's falsification-first ethos forbids promoting a coincidence-level estimate.

## 4. FALSIFICATION-FIRST WORK SEQUENCE (hard-ordered)

**Step A — The homogeneous-source problem. CHEAPEST POTENTIAL KILL — DO FIRST.** c05 gives F ∝ ∇(ΔSSV), so any homogeneous density (uniform ΔSSV) produces zero local force. Yet the Friedmann expansion is driven by homogeneous matter/radiation density (the decelerating matter era; BBN and CMB acoustic physics depend on the standard expansion rate H(z)). Resolve precisely: **how does gradient-sourced CPP gravity produce a cosmological expansion that responds to homogeneous density?** Two outcomes:
  - (a) there is a *global/horizon-scale mode* that sources expansion separately from local gradients (the (l_P/R_H)² horizon factor may be a clue that the global mode is physical) — if so, characterize it; this is the path forward.
  - (b) "only gradients gravitate" cannot reproduce the matter/radiation-dominated expansion → the model conflicts with BBN/CMB → **hard kill** for the gradient-only picture (would force a rethink of c05 at cosmological scales).
  This is the make-or-break and is cheap to confront conceptually before any derivation.

**Step B — The Sea-vs-matter distinction.** Given Step A's resolution, what *principled CPP criterion* makes the uniform Sea contribute only a suppressed Λ while uniform matter/radiation drives normal expansion? (Candidate framing: matter = SSV *excess* concentrations on the Sea with structure even when smooth on large scales; vacuum Sea = the ground-state substrate. Make this rigorous, not hand-wave.)

**Step C — Derive the Λ suppression.** Replace the inserted (l_P/R_H)² with a CPP-derived suppression factor; resolve the horizon ambiguity; address the R_H(t) "why now." Target ~observed Λ as a *derived* output, not a fit.

**Step D — Recover the Friedmann equation** quantitatively (radiation/matter/Λ eras; H(z)). This is the consistency capstone.

**>>> HARD RULE: do not claim the dark-sector unification (CONJ-COSMO-2), and do not unblock DM Steps 4–5, until Step A survives and Steps C–D are computed. <<<**

Only after A–D: feed back to DM Steps 4 (power spectrum from swirl seeds) and 5 (quantitative halo / rotation curve), and assemble for the multi-AI review panel.

## 5. LOAD-BEARING ASSUMPTIONS (each is a place the arc can break)

1. c05's gradient-sourcing is correct **and extends to cosmological scales** (Step A tests exactly this).
2. The Sea has a well-defined uniform "vacuum" mode distinct from matter/radiation overdensities (Step B must make this principled).
3. The SSV is dimensionally well-defined (depends on **OPEN-SR-3**, a prerequisite).
4. The absolute Planck/lattice scale is one shared calibration (TODO-014) — absolute Λ and H₀ magnitudes ride on it.

## 6. REGISTRATION PLAN (patch 0720, the arc-opening patch)

- **OPEN-SR-5** is already the scoped umbrella (Patch 0705). Add sub-items in `frontier_sectors/SR.md`: **OPEN-SR-5a** (homogeneous-source / Friedmann reconciliation — Step A), **OPEN-SR-5b** (derived Λ suppression — Step C), **OPEN-SR-5c** (Sea-vs-matter distinction — Step B).
- **CONJ-COSMO-2** — dark-energy↔dark-matter unification from the one Dipole Sea (uniform mode → suppressed Λ; inhomogeneities → DM). FAR-FRONTIER, GATED on Steps A–D. Register in `frontier_sectors/CONJ.md`; cross-link CONJ-COSMO-1 and OPEN-COSMO-DM-1.
- Cross-link **OPEN-SM-6** (same CC problem from the SM side — "will be the same theorem when solved").
- Do NOT register the c08 Λ estimate as a result.

## 7. NUMBERING

Open at **0720**; run 0720, 0721… contiguously. DM arc occupied 0700–0706; chirality is in 069x and climbing. Verify free at the clone gate; hop to 0730/0740 if converged. (Label collisions are harmless to `git am` but keep arc labels distinct for sanity.)

## 8. WORKING-ENVIRONMENT / GIT PROTOCOL (hard-won this session — read before pushing anything)

Thomas's machine is Windows / Git Bash (MINGW64), repo at `~/Documents/GitHub/CPP`, downloads land in `~/Downloads`. Two failure modes bit repeatedly this session:
- **CRLF normalization.** The working tree is CRLF; LF patches **reject on every mid-file `git am` hunk** (EOF appends and brand-new files apply fine). `git am --3way` also fails ("sha1 lacking") because the LF pre-image blob isn't in the CRLF object store. **Workaround used successfully:** deliver every registry/mid-file edit as a **download-and-run idempotent Python script** that edits at the byte level (preserving CRLF) with ASCII anchors and base64-embedded content (immune to terminal paste-mangling of unicode). New files can ship as ordinary patches. **Durable fix (do this at the START of the arc if the chirality window is quiescent):** a `.gitattributes` normalization (`* text=auto` + `git add --renormalize .`), after which plain `git am` works again. Run `git config --get core.autocrlf` and `cat .gitattributes` first.
- **Push race with the chirality window.** Both arcs push to `main`; chirality pushed between a `pull` and a `push`, silently rejecting the DM push (non-fast-forward) and leaving commits local-only. **Always** put `git pull --rebase origin main` *immediately* before `git push`, and re-run that pair if rejected.
- **ALWAYS verify origin after a push** by re-cloning and grepping for the content — do not trust "applied." This session lost an entire 0700–0703 batch to an unverified non-landing.

## 9. POINTERS

- **DM arc (paused, complete through Step 3):** `series_phenomena/cosmology/dark_matter/` — `R2_sea_gravitation_scoping.md` (this arc's origin), `step1/2/3_*.md`, `scripts/0703–0706_*.py`, `reasoning/0700–0706.md`. Arc handover: `handovers/2026-05-31_session_149_tetra_gravity_dark_matter_arc_kickoff.md`.
- **Gravity foundation:** c05 (gradient-sourced gravity), c07/c08 (GR), c08 dev notes §8 (Λ estimate).
- **Registry:** OPEN-SR-5 (scoped), OPEN-SR-3/6/7, OPEN-SM-6, OPEN-COSMO-DM-1, CONJ-COSMO-1.
- **Vision:** `founders_vision.md` §6c.
- **Patch-delivery contract / reasoning-capture / review-dispatch protocols:** `templates/`.

## 10. RELATIONSHIP TO OTHER ARCS

- **DM arc (CONJ-COSMO-1):** this arc is its unblocking prerequisite. DM Steps 4–5 cannot proceed honestly until Steps A–D here survive. If Step A *kills* the gradient-only cosmology, that reflects back on CONJ-COSMO-1 (the DM picture would need a different gravitational footing) — so Step A is load-bearing for both arcs.
- **Chirality arc:** independent physics, shared repository. Only coupling is the registry; the Line-1 clone/grep gate is mandatory every session, and this arc stays out of the chirality window's live zones (registry header changelog, DSL rows, Summary Statistics, CONJ-CHIR/THEO-CHIR/THEO-SPIN entries).
- **OPEN-SM-6:** the same cosmological-constant problem from the Standard-Model side; will be the same theorem when solved — coordinate so the two are not derived inconsistently.

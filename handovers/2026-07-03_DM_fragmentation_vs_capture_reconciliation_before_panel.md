# CONTEXT HANDOVER — DM velocity-dependence mechanism reconciliation (fragmentation vs capture) before CONV-001 panel

**Date:** 2026-07-03 · **Lane:** DM 18xx · **Author:** Opus (thread continuation) · **Git:** origin/main @ `e9a895a` (DM 1858)

---

## RESUME HERE — the one question that gates the panel

**Does a typical-cluster (v ≈ 1500–2000 km/s) collision fragment the Cross-Rod, or not?**

- **Paper DM-1 v1.0 says YES:** cluster collision energy ≈ 1.95 MeV > E_bond ⇒ rod fragments ⇒ σ/m drops ⇒ collisionless ⇒ cluster-safe. This is the shipped, panel-ratified-4/4 velocity-dependence mechanism (§5 `sec:xsec`, from the 0860 fragmentation ledger).
- **This thread (1855–1858) says the number doesn't obviously support that:** computing the strip/fuse onset from the pinned E_ee (0.9 MeV, 1813) and m_element (1408 MeV, 0886) gives v_thr ≈ 2000–4000 km/s for short rods (∝1/√N), so *typical clusters sit BELOW threshold* → do NOT fragment → stay intact at σ/m = 0.11·N ≈ 1.6 → **over-core typical clusters**. The paper's ~1.95 MeV cluster-collision figure and this thread's ~0.13–0.5 MeV estimate (½μv² at cluster v) disagree by ~4–15×; the discrepancy is in the *effective collision energy* (what mass/velocity/fraction actually participates in fragmentation).

**These two claims are about the paper's central discriminant and cannot both be right. Resolve this FIRST — it decides what §5 says.** Three outcomes:
1. **Fragmentation holds** (cluster collision energy really does exceed E_bond) → paper §5 mostly stands; this thread's capture detour was a response to a *wrong collision-energy estimate*; §5 needs only light updates.
2. **Fragmentation fails for typical clusters** → capture (1858) is needed as the suppression mechanism; §5 must be rewritten to capture; dwarf cores become conditional on R_s.
3. **Both contribute** → reconcile the split (fragmentation at high-v tail + capture falloff).

**Honest flag:** I am NOT certain this thread's capture picture *supersedes* the paper's fragmentation picture vs. sits beside it unreconciled, or was partly a garden-path driven by my own collision-energy estimate. The reconciliation is genuinely open. Load the 0860 fragmentation ledger and the 1856–1858 capture calcs side by side and settle the collision-energy number before choosing a mechanism.

---

## What is ROBUST vs CONDITIONAL (do not overclaim to the panel)

- **ROBUST / parameter-free / panel-ready:** velocity-dependent, **cluster- and Bullet-safe** self-interaction. True under *either* mechanism (fragmentation crushes σ/m at high v; capture's steep 1/r Rutherford falloff also crushes it). This is the honest headline.
- **CONDITIONAL / in flux:** (a) the velocity-dependence *mechanism* (fragmentation vs capture — the reconciliation above); (b) *dwarf cores* — conditional on the fragmentation-energy question, and if capture wins, on the de-novo **R_s** (DM-core DP-Sea screening length, target ~15–30 fm, never calculated; OPEN-SS-43).

## The other unreconciled number

**σ/m = 0.11·N (paper, geometric) vs σ_T/m ∝ N^0.7 (thread 1856 transport MC).** The paper uses a linear geometric σ/m; the momentum-transfer Monte Carlo (1856, ε≈0.30 flat, sphere-validated) scales as ~N^0.7 (rod–rod, orientation-averaged) and does NOT match 0.11·N (linear = the L² perpendicular limit). Decide which cross-section is the observable for σ/m before §5 quotes a magnitude. Does not change the fork direction (both grow with N ⇒ short N) but changes the exact dwarf-N.

---

## What this thread committed (1855–1858, all on origin @ e9a895a)

- **1855** — kinetic-aggregation re-frame: formation N is trivial at the short observable target; **retired the N_form ~ 400–1000 formation target** (that was a formation-lane number; the paper's observable N_dwarf ~ 5–60 was already short, so this did NOT change the paper's headline N). La Mer L_n = 1.52·α^(−0.49). Reworks the never-applied color-framed 1855.
- **1856** — rod transport efficiency **ε ≈ 0.30 flat** (sphere-validated 1.03); σ_T/m grows with N (~N^0.7); **retired N=500** (long rod over-cores ~11×); flagged the 0.11·N-vs-N^0.7 mismatch. Superseded OPEN-SS-41/41a/42 (the ΔG*_nuc barrier program).
- **1857** — **retired the threshold / v_thr framing** (Thomas's 1/r²-locked-lattice: E_qq magnitude-only, no confinement range ⇒ no δ* crossover); capture-focusing curve; surfaced the fragmentation/cluster tension.
- **1858** — **screened unipolar E_qq residual** = dwarf-coring mechanism IDENTIFIED. Founder insight: E_qq is attract-only ⇒ a qCP aggregate cannot dipole-cancel its field (the bipolar eCP coat does, which is why E_ee's coat is short-range and under-cores ~20×) ⇒ net ~1/r² residual escapes, DP-Sea-screened (SSV-summation-to-zero) at a finite length R_s. Verify: E_c ~ 0.3 MeV, R_s ~ 15–30 fm reaches dwarf σ/m ~ 1–2, clusters ~0.003. Magnitude CONDITIONAL on de-novo R_s(N); cluster-safety robust for any R_s.
- **Founder's Voice** promoted to canonical `founders_vision.md` (2026-07-03 entry): unipolar E_qq non-cancellation, point-like-at-infinity 1/r², SSV-summation-to-zero sea-screening.

## The sync problem (why the panel would bounce)

Paper §5 (`sec:xsec`) = **fragmentation** mechanism. Registry OPEN-SS-43 / DM 1858 = **capture** mechanism. Out of sync. If the panel follows the GitHub links to the frontier it sees a capture mechanism the paper never mentions, plus the fragmentation cluster-safety this thread put a question mark on. **Do not run CONV-001 until §5 and the registry agree.**

---

## Reconciliation task list (the fresh session's job, in order)

1. **Collision-energy calc.** Compute ½μv² for a typical-cluster Cross-Rod–Cross-Rod collision honestly (what μ — full rod, local segment? what v — dispersion, tail?) and compare to E_bond (~0.8 keV–2 MeV window). Settle: fragment or not. This is the single make-or-break for mechanism choice.
2. **Pick the mechanism** per outcome 1/2/3 above.
3. **Cross-section convention:** 0.11·N vs σ_T/m(N) — pick the observable.
4. **Rewrite §5** consistent with the chosen mechanism + the registry (1856–1858). Lead with the robust cluster/Bullet-safe result; present dwarf cores honestly (conditional if capture).
5. **THEN** assemble CONV-001 (`templates/presentation_file.md`, single 4-backtick block: GitHub links + one-para intro + rendered Markdown) and run the multi-AI panel.

## Downstream (after reconciliation, if capture wins)

**R_s de-novo derivation** — DP-Sea penetration depth of an extended N-element qCP aggregate before the interior E_qq leaks as a net residual. New Strong-Sector-Series physics (SSV-summation-to-zero for an aggregate, not a lone qCP/pion); corpus has never touched it; founder-driven. Target R_s ~ 15–30 fm → dwarf cores; ~1 fm → weak-SIDM fallback.

## Key files

- Paper: `series_phenomena/cosmology/dark_matter/DM-1/DM-1_substrate_dark_matter_candidate.tex` (§5 `sec:xsec` = fragmentation; framed v0.1→v1.0 revision notices at top of §5).
- Fragmentation ledger: patch 0860 (in `.../scripts/` or reasoning 0860).
- Capture calcs: `.../code/1856_rod_transport_efficiency.py`, `1857_capture_focusing_window.py`, `1858_eqq_screened_residual_capture.py`.
- Frontier: `frontier_sectors/SS.md` → OPEN-SS-43. Vision: `founders_vision.md` (2026-07-03).
- Pinned inputs: E_ee = 0.9 MeV (1813), m_element = 1408 MeV (0886), E_qq = 66 MeV.

## Unchanged / carried

Cluster σ/m robust headline; over-coring EXCLUDED; DM-1 stays **v1.0** (fragmentation text, pending reconciliation — do NOT quietly overwrite before the mechanism is settled); CONJ-COSMO-1 founder-gated; panel HELD until §5 ↔ registry reconciled.

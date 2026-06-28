# Handover — the E_bond pin (SF-2/SF-5 edge-bond SSV make-or-break)

**Task:** pin **E_ee** (= the ledger's E_bond, the scission bond), the one number that converts DM-1 from a
viable corona-safe candidate into a *discriminating* prediction. Pinning it collapses N_dwarf → a single σ/m →
a hard core-size-vs-halo-mass curve → moves CONJ-COSMO-1 off NOT-confirmed.
**Date opened:** 2026-06-28 (continuing the `260625 0865 DM` window; Thomas remote, memorial travel).
**Origin:** registered SF-2/SF-5 make-or-break; scoped at patch 0887; the robust shoulder banked at 0865.
**Why a handover:** this is a foundational SF-substrate arc, not a DM-local patch — it may close, or it may
reduce to an open root. It needs a clean boot and an honest attack plan, not a hot-path guess.

---

## BLOCKING CLONE-AND-GREP GATE (before anything else)
1. Clone fresh; `git log --oneline | head -30`. This work is **SF-2/SF-5 lane** physics — draw patch numbers
   from the SF-2/SF-5 band (grep for the next free one), **not** the 08xx DM band. If a result promotes, the
   DM-side consumption (σ/m number) is a later DM-lane patch.
2. Read §Required reading in order. Grep `frontier_sectors/FP.md` + `CONJ.md` before registering anything.
3. **Anti-priority (hard):** do **NOT** fabricate a coupling, a scale, or a screening fraction to manufacture
   E_ee. 0865 refused this and so did the close-out session. An honest stall (the make-or-break does not close)
   is a valid, reportable outcome — far better than a fabricated number on a v1.0 paper.

## KICKOFF SENTENCE
> *You are attacking the E_bond pin. DM-1 v1.0 ships with a velocity-dependent σ/m = 0.11·N that reaches the
> dwarf-core band; the single missing number is the equilibrium aggregate size N_dwarf, fixed by the edge-bond
> depth E_ee via freeze-out. 0865 already banked the robust shoulder: the fm-scale Coulomb ceiling
> α·ℏc/ℓ_rung = 1.44 MeV sits at the top of the fragmentation window [0.8 keV, 2 MeV], so E_ee = η_screen ·
> 1.44 MeV with the pass-band η_screen ∈ [~6×10⁻⁴, 1]; the ordering E_qq > E_ee is sign-certain; and the
> 14-Gyr lifetime floor shares one sub-20-keV substrate scale with the 0860 fragmentation hook. The whole
> make-or-break has therefore collapsed to ONE quantity: derive η_screen (the screening-residual fraction) — or
> equivalently E_ee as a ratio to a known SF DP scale — from the edge-bond charge geometry. Try the ratio route
> first; it may sidestep the sub-Planck near-cancellation entirely.*

## What is already banked (do not re-derive — build on it)
From `reasoning/0865.md` (the robust shoulder, Layer C) + the scoping doc `edge_bond_ssv_makeorbreak_scoping.md`:
- **(A) Window reachable.** Effective fm-scale ceiling α·ℏc/ℓ_rung = **1.44 MeV** sits at the window top.
  In-window ⇔ η_screen ≡ E_ee/(α·ℏc/ℓ_rung) ∈ **[~6×10⁻⁴, 1]** — a wide, natural, un-fine-tuned band.
- **(B) Ordering** E_qq > E_ee, sign-certain (screening geometry, not magnitude). **E_ee is the ledger depth**
  (governs breakage, length kinetics, lifetime); E_qq pairs with the G1 angular spring.
- **(C) Lifetime floor** E_ee ≳ 100·kT_present coincides with 0860's kT_amb ≲ ~19 keV — one substrate scale.
- **(D) Over-determined target:** E_ee ∈ [0.8 keV, 2 MeV] AND E_ee/kT_form ~ 24–41 (the freeze-out band size).

## The sharp target and two routes
**Target:** derive **η_screen** (one O(1)-to-O(10⁻³) number) — or E_ee as a ratio to E_eDP/E_qDP — from the
edge-bond charge configuration. That is the entire remaining make-or-break.

- **Route A — geometric/ratio (TRY FIRST; may close).** CPP's DP binding energies are *ratio-clean*
  (E_qDP = 3·E_eDP, E_hDP = √(E_eDP·E_qDP)); the absolute scale is calibrated but the **ratios** are derived
  from charge geometry. The edge-bond is a *screened residual of the same charges*. So attempt E_ee as a
  **geometric fraction of a pinned DP scale** — E_ee = f_geom · E_eDP, with f_geom from the edge screening
  configuration (the eCP/qCP positions at the e–e edge, the partial like/opposite cancellation, the pre-tension
  separation ratio). If f_geom is fixed by geometry alone, the **sub-Planck absolute near-cancellation is never
  evaluated** — you get E_ee as a ratio, η_screen falls out, and the pin closes. **This is the win condition.**
- **Route B — the absolute SSV charge-sum (the hard root).** If Route A needs a coupling/scale not fixed by
  geometry, the absolute depth is the sub-Planck near-cancellation: bare terms ~10¹⁶–10¹⁷ GeV at r₀ ≪ fm,
  residual at keV–MeV (a ~10¹⁸× cancellation). This **cannot be eyeballed** and needs the inter-CP binding
  potential / SSV charge-sum framework — which is *the same thing whose absence leaves SF-2's cage masses
  calibrated.* At that point the E_bond pin **reduces to its shared root** (see precision note) and becomes a
  foundational substrate-thermodynamics arc, not a DM-payoff patch.

## Precision note (do not conflate — this corrects 0887/0891 loose phrasing)
There are **two different η's**: (1) **η_screen** here ≈ E_ee/[α·ℏc/ℓ_rung] ∈ [6×10⁻⁴, 1] — the screening
fraction you are deriving; (2) **η_W/η_Z/η_H ~ 10⁻¹⁷** = OPEN-FP-SF-2-η, the SF-2 *cage-mass* dilution. The
E_bond pin is **not strictly downstream of OPEN-FP-SF-2-η**; it **shares a root** with it — the absence of a
derived inter-CP binding potential / substrate-thermodynamic framework (FP.md: "likely shared closure path via
substrate-thermodynamic framework"; the framework is currently undefined — "equilibrium/effective-temperature/
ensemble/ergodicity/substrate-dynamics undefined" per the SF-2 v1.3 review). **Route A's whole value is that it
may close E_ee without touching that root.** Determine quickly whether A bottoms out at geometry (win) or at
the undefined framework (then the honest arc is OPEN-FP-SF-2-η itself, or OPEN-SR-9 — the deeper alternatives
in the campaign-close handover).

## What a win / a stall looks like
- **Win:** η_screen (or E_ee/E_eDP) derived from geometry, landing in [6×10⁻⁴, 1] / [0.8 keV, 2 MeV] with
  E_ee/kT_form ~ 24–41 reachable → register the SF result, then a DM-lane patch consumes it: N_dwarf collapses,
  σ/m becomes a single curve, and CONJ-COSMO-1 can be revisited (panel-gated). A return *outside* the window is
  the pre-registered **falsification** of the Cross-Rod candidate — also a real result, not a failure.
- **Honest stall:** Route A needs an undefined coupling. Report that E_bond reduces to OPEN-FP-SF-2-η's root /
  the substrate-thermodynamic framework; do not fabricate. Recommend pivoting to that root or to OPEN-SR-9.

## Required reading (in order)
1. `series_phenomena/cosmology/dark_matter/reasoning/0865.md` (the robust shoulder A–D — the foundation).
2. `series_phenomena/cosmology/dark_matter/edge_bond_ssv_makeorbreak_scoping.md` (0887 — the full spec).
3. SF-2 v1.0 (the cage-mass machinery + the η calibration) and SF-5 (the strong-sector edge couplings,
   E_qDP = 264 MeV scale). Find via `flagship_papers/electroweak/` and `…/quarks/` or grep the paper catalog.
4. `frontier_sectors/FP.md` §OPEN-FP-SF-2-η (the shared root) + `problem_histories/PH-OPEN-FP-SF-2-eta.md`.
5. `series_phenomena/cosmology/dark_matter/code/0865_edge_bond_depth_window.py` (the banked bracketing).

## Environment / standing contracts (unchanged)
- Apply-chain (Thomas's machine): Windows + Git Bash; repo `~/Documents/GitHub/CPP`; downloads `~/Downloads`.
  Precautionary apply-and-push block + `git am --3way` recovery note after every `.patch`.
- Patch-delivery contract: artifact + verbatim reasoning fragment + verify script if computation + a **verbatim**
  founder-contribution block when a TLA contribution shapes the result (paste his words, not a summary — the
  0890 audit found the block was catching the fact but not the words).
- CONV-001 for any registry move; panel-gate lemma/OPEN changes; keep dead-ends in the record; distinguish
  computed/cited/bracketed/assumed; never fabricate substrate numbers; stage the founder's voice, never
  auto-write canonical `founders_vision.md`.

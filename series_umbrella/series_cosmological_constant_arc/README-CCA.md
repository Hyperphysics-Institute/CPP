# Series Cosmological-Constant Arc (SCCA) — charter

**Folder:** `series_umbrella/series_cosmological_constant_arc/`
**Role:** the cross-sector umbrella that **reconciles CPP's three accounts of the
cosmological-constant suppression into one mechanism**, decides static-vs-dynamical Λ,
makes `OPEN-SR-5` and `OPEN-SM-6` one theorem, and wires the result to the dark-matter
identification's **R2** gate (`OPEN-COSMO-DM-1`).
**Opened:** 10 June 2026 (handover `handovers/2026-06-10_session_156_CC_reconciliation_umbrella.md`); founding scoping patch **1101**.
**Status:** SCOPING delivered (Patch 1101). **NO VERDICT MOVED** — no THEO, no PRED, no count
change; everything below is conditional on the c08 closed field equation (a standing conjecture).
**Lane:** CC umbrella, band **1101+** (lightweight two-window check-and-warn with the Project-C
1000s lane and the DM 08xx lane; shared registries + the DP-Sea flagship are STOP-and-warn).

---

## The problem in one paragraph

The cosmological constant — observed `ρ_Λ ≈ 5.3×10⁻¹⁰ J/m³`, ~120 orders below the naive
Planck vacuum density — is the largest quantitative embarrassment in conventional physics.
CPP "solves" it in **three places that were never reconciled**, and the inconsistency became
load-bearing once the DM identification was staked on it. The three accounts give the right
order for incompatible reasons; this arc decides which is physical and collapses the rest.

## The three accounts (as found, at their sources)

| Tag | Where | Claim | Character |
|---|---|---|---|
| **(A) dynamical** | `OPEN-SR-5` Step C (Patch 0722), `frontier_sectors/SR.md` | `ρ_Λ = c²H²/8π G = (1/8π) ρ_P (l_P/R_H)²`; scaling **and** 1/8π **derived**; IR scale = future event horizon (Step D3); factor ~2 of observed | horizon-scale, **time-varying** (ρ_Λ ∝ H²) |
| **(B) microscopic** | `OPEN-SM-6`, `frontier_sectors/SM.md` | paired-DP cancellation leaving residual `∝ E_P⁴ (l_P/R)²`; ~order of magnitude | SM-side; SM.md already calls SR-5 "the same problem from the GR perspective" |
| **(C) static** | `DP_sea_and_cage_composition.tex` (lines 64, 181, 507) | `ρ_vac ~ ρ_sea/N⁴ ≈ 10⁻¹²⁰ ρ_P` via "holographic bit recycling", N = 10³⁰ GPs/l_P | substrate ratio, **constant** |

## The candidate thesis (Patch 1101 — to be enacted via the CC-U children, not asserted here)

**One mechanism, three levels.** Gravity couples to the SSV **excess** above the Sea ground
state (c05), so the uniform Sea sources zero gravity (no catastrophe). The microscopic statement
of "uniform Sea cancels" is SM-6's paired-DP cancellation; the GR statement is SR-5's
excess-sourcing. The only gravitating leftover is the largest gradient a discrete-UV,
causally-bounded-IR Sea cannot cancel — the **horizon-scale mode**, `(l_P/R_H)²`. So **(A) and (B)
are the same theorem two ways**, and the suppression is **dynamical** (ρ_Λ ∝ H²).

**(C) is demoted, not retired-as-a-number.** Today `R_H/l_P ≈ 8.5×10⁶⁰ ≈ N²` (with N ≈ 10³⁰),
so `1/N⁴ ≈ (l_P/R_H)²` **at the present epoch** (`code/1101_cc_coincidence_check.py`): the static
"constant 1/N⁴" is the dynamical horizon suppression evaluated *now*, not an independent
mechanism. And it cannot be made fundamental: Patch 0736 verified lattice **resolution enters no
prediction formula** (the 1004 commit states "GP-count cannot derive Λ without overturning it"),
and N ≈ 10³⁰ is itself flagged unverified/not-relied-upon (1004/1005). **Verdict: dynamical wins;
the N⁴ *mechanism claim* is retired and reframed (a DP-Sea flagship edit, same epistemic class as
TODO-016, requiring Thomas's sign-off).**

## Target / falsifier / on-success

- **Target:** one substrate mechanism that (i) suppresses the uniform-Sea vacuum to ~observed
  without inserting the horizon or N by hand, and (ii) leaves swirl-inhomogeneities gravitating at
  DM amplitude — discharging R2 and collapsing SR-5 ∪ SM-6 into one theorem.
- **Falsifier:** if no single mechanism does both, the dark-energy↔dark-matter unification fails
  and the DM identification loses its R2 leg. Sub-falsifier (CC-U/1): the N⁴ claim cannot be
  rescued as fundamental (already essentially established — see above).
- **The honest cap (CC-U/4):** all of the above is conditional on the **c08 closed field equation**
  `G_μν = 8πG/c⁴ T_μν[LSP]` (excess-sourcing), which c08 itself flags as an unsolved conjecture. If
  gravity sources from absolute |SSV|, the ground state gravitates and **both** the CC suppression
  and the R2 split break together. Closing c08 is the real mountain; it is separable from the
  reconciliation and is **not** attempted in the first round.

## Children

See `INDEX.md`. Falsification-first order: **CC-U/1** (N⁴ audit) → **CC-U/2** (static vs dynamical)
→ **CC-U/3** (SR-5 ≡ SM-6) → **CC-U/5** (R2 wiring) → **CC-U/4** (c08, the standing cap).

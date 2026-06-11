# Handover — c08 Closed Field Equation (`op:einstein`): the attack arc on the shared cap of the CPP dark sector

**Arc:** Conscious Point Physics — relativity sector (c08 strong-field GR), with cross-sector stakes (CC via SR-5, dark matter via R2).
**Open problem:** c08 `op:einstein` — the central open problem of `c08_strong-field_GR.tex`. **The single conjecture that caps both the cosmological-constant reconciliation and the dark-matter R2 split.**
**Date opened:** 11 June 2026 (Session 156), teed up by the CC reconciliation umbrella (CC-U/4 scoping, Patch 1105). **To be run in its own relativity-sector window, own band, base_ref at start.**
**This is the durable record and the opening prompt for a fresh window. Paste it in to start; re-fetch from `handovers/` if context is lost.**

---

## KICKOFF LINE (paste to start a session)

```
Bootup for Conscious Point Physics (CPP). Clone the repo and read the bootup file at https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/bootup.md. Honor the line-1 CLONE-FIRST GATE before registering any ID, placing any file, or computing any coefficient. Then open handovers/, sort by filename, read the most recent dated file — then load THIS file: 2026-06-11_session_156_c08_op_einstein_attack_kickoff.md.
```

## BLOCKING CLONE-AND-GREP GATE (before anything else)

1. Clone fresh; `git log --oneline | head -30` — see the live frontier and free patch bands (multiple windows push concurrently; the chirality lane is in 09xx, DM in 08xx, the CC umbrella used 1101–1105).
2. **Claim your own band** confirmed against `git log` (do not reuse any consumed number). Record a base_ref = current HEAD.
3. Read the §Required reading in order before deriving.
4. If multiple windows are open, paste the anti-collision protocol (`templates/anticollision_protocol.md`).

## KICKOFF SENTENCE

> *You are attacking the **single conjecture underneath the entire CPP dark sector**: c08's `op:einstein`. Two things must be shown about the continuum limit of the nonlinear CPP self-consistency field equation — (a) it **recovers Einstein** `G_μν = 8πG T_μν/c⁴`, and (b) its source is the SSV **excess** `∇²(Δ|SSV|) = (8πG/c⁴)T` with the ground state genuinely **excluded**, not the absolute `|SSV|`. Part (b) is the high-leverage one: ground-state exclusion is exactly what makes the uniform Sea inert, and on it rest both the cosmological-constant suppression (SR-5 Step D2) and the dark-matter "uniform inert / swirls gravitate" split (R2). If the reduction sources from absolute `|SSV|`, the ground state gravitates, the vacuum catastrophe returns, and the CC suppression and the DM identification fail together. Closing `op:einstein` is the genuine resolution of the cosmological-constant problem in CPP.*

## Orientation — read this first

c08 (`series_relativity/SR_companion_papers/c08_strong-field_GR.tex/c08_strong-field_GR.tex`) defines
the **CPP field equation** as a self-consistency condition: the metric reconstructed from the LSP
density equals the LSP propagation operator on that metric, `M[ρ_LSP] = G[M[ρ_LSP]]`, with explicit
nonlinear form `F(g[PSR_eff], …) = (8πG/c⁴)T`. c08 writes a weak-field/excess reduction
`∇²(Δ|SSV|) = (8πG/c⁴)T` (near line 542) but states that whether the full nonlinear `F` is **exactly
equivalent** to Einstein's `G_μν = 8πG T_μν/c⁴` in the continuum limit is its **central open problem**
(`op:einstein`, near lines 170, 527–532). The CC umbrella (Patches 1101–1105) established that this
one problem is the shared cap for the whole dark sector and scoped it (see
`series_umbrella/series_cosmological_constant_arc/1105_ccu4_c08_scoping.md`). This arc climbs it.

## The crux (state it sharply before deriving)

The conjecture splits into two sub-problems, of which **(b) is the cheaper potential kill**:

- **(a) GR-recovery.** Does the continuum limit of the nonlinear self-consistency operator `F` reduce
  to `G_μν = R_μν − ½g_μν R = 8πG T_μν/c⁴`? c07's LSP→metric mapping (Prop. 2.1) + the linearized
  broadcast equation should give the weak-field Newtonian limit (c05 already has Newtonian gravity
  from SSV); the open piece is the **nonlinear/curvature** term introduced by `g[PSR_eff]`.
- **(b) Excess-vs-absolute sourcing (the high-leverage fork).** In the rigorous continuum limit, does
  the source reduce to `∇²(Δ|SSV|)` (ground state cancels ⇒ uniform Sea inert) or to a form depending
  on absolute `|SSV|` (ground state gravitates ⇒ catastrophe)? c05's broadcast mechanism is
  **differential** (each GP broadcasts an LSP set by its neighbors' state), which makes gradient/excess
  structure natural at weak field; the risk is that the **nonlinear curvature-dependent term**
  (`g[PSR_eff]`, c08 ~line 514) reintroduces an absolute-`|SSV|` coupling. **Decide (b) first.**

## What "done" looks like

A derivation showing, in the continuum/weak-field limit of `F`: (a) `F → G_μν = 8πG T_μν/c⁴`
(Einstein recovery), and (b) the source is `∇²(Δ|SSV|) = (8πG/c⁴)T` with the ground state genuinely
excluded — the excess form is *the* rigorous reduction, not a separately-posited ansatz. Either
outcome conditionalizes or unconditionalizes the dark sector at once; a clean (b)-kill (absolute
`|SSV|`) falsifies the CC suppression and the DM R2 split together.

## Suggested approach (falsification-first)

1. **(b) first, cheapest kill.** Take the LSP broadcast equation at each Grid Point (c08 ~line 504),
   write its continuum limit explicitly, and check whether a spatially **uniform** `|SSV|` (the Sea
   ground state) drops out of the source. If it survives in the source, that is a candidate kill of
   the inert-Sea premise; if it cancels (as the differential broadcast structure suggests), (b) holds
   and the inert-Sea premise is vindicated. This is a bounded analytic check, not a full derivation.
2. **(a) next.** Linearize `F` about flat space, confirm the Newtonian limit matches c05, then attack
   the nonlinear curvature term: does `g[PSR_eff]`'s curvature dependence assemble into `R_μν − ½g_μν R`?
3. Treat numerical/lattice checks (small-N self-consistency solutions of `M[ρ_LSP] = G[M[ρ_LSP]]`) as
   a corroboration route if the analytic reduction stalls.

## Required reading (in order)

1. `series_relativity/SR_companion_papers/c08_strong-field_GR.tex/c08_strong-field_GR.tex` — §"The CPP
   Field Equation" (the self-consistency condition, the explicit `F`, `op:einstein`, the excess form
   ~line 542).
2. `series_relativity/SR_companion_papers/c05_newtonian_gravity_from_SSV/…` — gradient-sourcing
   `F = m'c²k∇(ΔSSV)` (the weak-field precedent; the reason excess-sourcing is natural).
3. c07 (LSP→metric mapping, Prop. 2.1) and the Absolute Moment companion `c1` (PCD cycle, CP Exclusion
   Rule, minimum-metric resolution).
4. `frontier_sectors/SR.md` — OPEN-SR-5 Step D2 (what rests on ground-state exclusion).
5. `series_umbrella/series_cosmological_constant_arc/1105_ccu4_c08_scoping.md` — the cross-sector cap
   framing; and `1101_cc_reconciliation_scoping.md` for the CC stakes.
6. `series_phenomena/cosmology/dark_matter/R2_sea_gravitation_scoping.md` (+ the CC-U/5 reframe draft) —
   the DM stake in the same conjecture.

## The deepest risk / falsifier

`op:einstein` may simply be **hard** — a nonlinear self-consistency reduction with no closed form. The
falsifier for the *dark sector* (not for the arc): if the rigorous continuum source provably depends
on absolute `|SSV|` (ground state gravitates), both the CC suppression and the DM R2 split are
falsified. The arc itself "fails gracefully" into a characterized open problem (the result stays
conditional, exactly as it is now).

## On success

A proof that the CPP field equation recovers Einstein **and** sources from the SSV excess
unconditionalizes the entire dark sector in one stroke: it discharges SR-5 Step D2, removes the cap on
the CC reconciliation (collapsing OPEN-SR-5/OPEN-SM-6 into an *unconditional* theorem), and discharges
the DM R2 gate. This is the keystone — the genuine CPP resolution of the cosmological-constant problem
and the foundation of the qDP/hTetra → dark-matter identification.

## Scope / window / collision note

Relativity sector (c08), cross-sector stakes (CC + DM). **Its own window, own band, base_ref at start.**
It will read — but should not edit from this window — the CC arc (`series_umbrella/series_cosmological_constant_arc/`,
CC umbrella lane) and `dark_matter/` (DM 08xx lane). Shared-registry touches (`frontier_sectors/SR.md`
OPEN-SR-5 status, a possible `op:einstein ↔ OPEN-SR-5 ↔ R2` cross-link, `theorem-registry.md` only on
success) are integrator-batched and STOP-and-warn under the lightweight anti-collision protocol
(`templates/anticollision_protocol.md`).

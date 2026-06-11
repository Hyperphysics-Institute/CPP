# op:einstein Closure Arc — charter

**Folder:** `series_relativity/op_einstein_closure/`
**Problem:** c08 `op:einstein` — whether the nonlinear CPP self-consistency field equation
(`M[ρ_LSP] = G[M[ρ_LSP]]`, explicitly c08 eq:field_eq) reduces in the continuum limit to Einstein
`G_μν = 8πG T_μν/c⁴`, **and** whether its source is the SSV **excess** `Δ|SSV|` (ground state
excluded) rather than absolute `|SSV|`. **The single conjecture capping the whole CPP dark sector.**
**Opened:** 11 June 2026, from the kickoff handover `handovers/2026-06-11_session_156_c08_op_einstein_attack_kickoff.md` (teed up by the CC umbrella, CC-U/4).
**Status:** ATTACK OPEN. Step (b) examined (Patch 1107) — **the cheapest kill does NOT fire**; cap
narrowed. **op:einstein is NOT closed.** No verdict moved.

---

## Why it matters (one paragraph)
Ground-state exclusion — gravity sourced by `Δ|SSV|` not `|SSV|` — is what makes the uniform Sea
inert. On it rest both the cosmological-constant suppression (SR-5 Step D2) and the dark-matter R2
split (uniform inert / swirls gravitate). If the rigorous reduction of c08's field equation sources
from absolute `|SSV|`, the ground state gravitates, the vacuum catastrophe returns, and the CC
suppression and the DM identification fail **together**. Closing `op:einstein` is the genuine
resolution of the cosmological-constant problem in CPP.

## The two sub-problems
- **(a) GR-recovery** — does the nonlinear feedback term `F` (c08 eq:F_term) assemble into the full
  `R_μν − ½g_μν R` in the strong field? c08 proves the weak-field limit (companions 5, 7) and notes
  Schwarzschild is consistent with both Einstein and the bare CPP equation, so the spherical vacuum
  case cannot decide it. **The hard core; open.**
- **(b) Excess-vs-absolute sourcing** — does the uniform Sea ground state cancel from the source? The
  cheapest potential kill. **Examined in Patch 1107 (Step (b)): does not fire — see below.**

## Step (b) result (Patch 1107) — the cheapest kill does not fire
c08 eq:field_eq is written entirely in `Δ|SSV|` (both the linear Laplacian and the nonlinear `F`).
Two routes for absolute `|SSV|` to re-enter were tested (`code/1107_stepB_curvature_check.py`):
- **(b1) source:** `F ∝ (Δ|SSV|)²/(1+kΔ|SSV|)²` vanishes identically at `Δ|SSV|=0` (leading order
  `O(Δ²)`, pure excess); with `Δ|SSV|=0` the whole LHS is zero ⇒ the uniform Sea sources nothing.
- **(b2) metric background:** for `g_μν = Ω²η_μν` (PSR_eff sets `Ω`), the Ricci scalar is
  `R = 2(−ΩΩ'' + Ω'²)/Ω⁴`, which is **0 for constant Ω** ⇒ a uniform `|SSV|`/PSR_eff background is
  **flat**; curvature tracks *gradients* of `Ω` (= gradients of `|SSV|` = the excess), not its
  absolute value.

**Conclusion:** *as c08's field equation is written*, excess-sourcing / inert-uniform-Sea holds and
the catastrophe does not return through either door. This does **not** close `op:einstein` — see the
residual.

## The honest residual (what Step (b) does NOT settle)
1. **Rigorize the shell-sum.** c08 derives the excess form via a proof *sketch* ("LSP broadcast at
   each GP, summed over shells, gives `∇²(Δ|SSV|)=…`"). Step (b) shows the *stated* equation is
   inert-Sea-safe; the open (b)-task is to confirm the shell-sum reduction genuinely produces the
   excess form with **no dropped absolute-`|SSV|` term**.
2. **Cosmological mode (separate).** Local-curvature inertness ≠ cosmological suppression. The uniform
   Sea's coupling to the global Friedmann scale factor (the Λ question) is the SR-5 Step A/C horizon
   mechanism, not this local field equation.
3. **(a) nonlinear GR-recovery** remains the hard core.

## Falsifier / on-success
- **Dark-sector falsifier:** if the rigorous continuum source provably depends on absolute `|SSV|`
  (ground state gravitates), CC suppression and DM R2 are falsified together. (Step (b): not fired.)
- **On success:** a proof of (a)+(b) unconditionalizes the dark sector at once — discharges SR-5 D2,
  collapses OPEN-SR-5/SM-6 into an unconditional theorem, discharges R2.

## Children / steps
See `INDEX.md`. Order: **(b) shell-sum rigor** → cosmological-mode handoff (SR-5) → **(a) nonlinear
GR-recovery** (the summit).

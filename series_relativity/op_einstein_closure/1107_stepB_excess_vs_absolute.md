# Step (b) — Excess vs absolute |SSV| sourcing (Patch 1107)

**Arc:** `series_relativity/op_einstein_closure/` · **Charter:** `README.md` · **Verify:**
`code/1107_stepB_curvature_check.py`
**Result:** the cheapest potential kill of the dark sector **does not fire**. **op:einstein NOT
closed; NO VERDICT MOVED** (SR-5 Step D2 is *narrowed*, not discharged — it still rests on the
residual below).

## The question
c08 eq:field_eq:
> `∇_λ∇^λ(Δ|SSV|) + F[PSR_eff, Δ|SSV|] = (8πG/c⁴)T`,  `F = 2k(Δ|SSV|)²/(1+kΔ|SSV|)² · ∇_λ∇^λ ln(1+kΔ|SSV|)`.

Ground-state exclusion (gravity ← `Δ|SSV|`, not `|SSV|`) is the premise that makes the uniform Sea
inert and underwrites both the CC suppression and the DM R2 split. Step (b) asks: can absolute
`|SSV|` re-enter and let a uniform Sea source curvature? Two routes — the source, and the metric
background.

## (b1) The source term
Both pieces of the LHS are functions of `Δ|SSV|` alone. The nonlinear prefactor
`2k(Δ|SSV|)²/(1+kΔ|SSV|)²` vanishes identically at `Δ|SSV|=0` (leading behavior `O((Δ|SSV|)²)` —
pure excess), and `∇²(Δ|SSV|)=0` for uniform `Δ|SSV|`. So a uniform Sea (`Δ|SSV|=0`) gives
`LHS = 0 = (8πG/c⁴)T` ⇒ `T=0`: **no matter, no curvature — the uniform Sea sources nothing.** Absolute
`|SSV|` does not appear in the source.

## (b2) The metric background g[PSR_eff]
The covariant derivative acts on `g_μν[PSR_eff]`, and `PSR_eff` is set by *absolute* local `|SSV|` —
the one place absolute magnitude enters. Model the scale dependence as `g_μν = Ω(x)²η_μν` with
`Ω` set by `PSR_eff`. Computing the Ricci scalar (`code/1107_stepB_curvature_check.py`):
> `R = 2(−ΩΩ'' + Ω'²)/Ω⁴`.

For **constant `Ω`** (uniform `PSR_eff`, i.e. uniform absolute `|SSV|`), `R = 0`: the background is
**flat** — a uniform absolute `|SSV|` is a mere unit rescaling, carrying no curvature. Curvature
appears only through **gradients** of `Ω` (`Ω'`, `Ω''`), which track gradients of `PSR_eff` =
gradients of `|SSV|` = the **excess** structure. So absolute `|SSV|` does not gravitate even through
the metric-background door.

## Conclusion and the honest residual
*As c08's field equation is written*, excess-sourcing / inert-uniform-Sea holds through **both**
routes — the cheapest kill does not fire, and the vacuum catastrophe does not return. This is a
genuine narrowing of the cap, but it is **not** a closure of `op:einstein`, because:

1. **Shell-sum rigor (the real (b)-task).** c08's excess form rests on a proof *sketch*. Step (b)
   shows the *stated* equation is safe; confirming the shell-sum reduction produces the excess form
   with no dropped absolute-`|SSV|` term is the open (b) work.
2. **Cosmological mode (separate sector).** Local inertness ≠ cosmological suppression; the uniform
   Sea's Friedmann coupling is SR-5 Step A/C (horizon mechanism), not this local equation.
3. **(a) nonlinear GR-recovery** — whether `F` assembles into `R_μν − ½g_μν R` — remains the summit;
   Schwarzschild cannot decide it (c08 remark).

**Net:** the dark sector's cheapest failure mode is closed; the cap on the CC reconciliation is now
the *narrower* conjunction {shell-sum rigor + nonlinear GR-recovery}, still conditional, with the
cosmological-mode piece living in SR-5.

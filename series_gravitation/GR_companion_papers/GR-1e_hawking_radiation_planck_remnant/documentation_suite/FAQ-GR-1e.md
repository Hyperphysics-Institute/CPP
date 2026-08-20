# FAQ — GR-1e

**Q1. Why does evaporation stop?**
Because the geometry runs out, not because the temperature does. The
semiclassical Hawking derivation needs the Schwarzschild radius to span
many lattice cells (N = r_S/l_P ≫ 1). At M ~ m_P, N → 2: the horizon is
a boundary of width l_P separating two cells from three. The smooth
near-horizon region the mechanism requires does not exist, so the
approximation is not merely inaccurate — it is geometrically undefined.

**Q2. Isn't the real reason that the Hawking temperature diverges?**
No, and the paper checks rather than assumes. At M = m_P the Hawking
temperature is T_P/8π ≈ 0.040 T_P — 4% of Planck, well below the lattice
maximum. The thermal constraint does not bind first, with roughly a
factor of 25 to spare. Eliminating the obvious alternative is what makes
the geometric argument worth anything.

**Q3. What is the remnant?**
A stable Planck-mass object, M_rem ~ m_P ≈ 2.18×10⁻⁸ kg, roughly two
Planck lengths across, that cannot evaporate further.

**Q4. Is it stable, or just where the calculation gave up?**
The paper claims genuine mechanical stability: a self-sustaining fixed
point where gravitational SSV compression is exactly balanced by CP
Exclusion repulsion at PSR_eff = l_P/2. No external pressure is invoked,
and both effects were already in the theory. This is the paper's
strongest and most attackable claim — see `reviews-GR-1e.md`.

**Q5. Does this change how long black holes last?**
Not observably. The modification is confined to the final Planck epoch,
and (m_P/M₀)³ ≪ 1 for any astrophysical hole, so the evaporation time is
essentially the standard ~2.1×10⁶⁷ yr for a solar mass. Early-time
Hawking radiation is unchanged.

**Q6. Does the remnant solve the information paradox?**
No — and the paper says so itself. Because there is no singularity,
nothing *destroys* the information. But the remnant's capacity is of
order k_B, far below the original black hole's Bekenstein–Hawking
entropy S_BH = k_B A/4l_P². The paper concludes explicitly that the
resolution must involve the full Hawking radiation train, not the
remnant alone, and defers the unitarity question to a full quantum
treatment.

**Q7. What about the Page time?**
Untouched. Page's argument concerns the point (≈ t_evap/2) after which
unitary radiation must begin encoding information, and CPP's
modification lives entirely at the very end of evaporation. The
early-time radiation is unchanged, so the information question is
displaced to the final Planck epoch rather than reopened throughout.

**Q8. Is this a full quantum derivation?**
No. The termination argument is geometric and thermodynamic. The
Bogoliubov-coefficient calculation — quantum field modes from the
asymptotic past to the near-Planck epoch, with the inner boundary at
r₀ = r_S + l_P — has not been done, and it is what would reveal whether
the late-time spectrum departs from thermal *before* termination.
Registered as the paper's first open problem.

**Q9. Are Planck remnants observable?**
Only indirectly, and the paper does not develop it. They interact
gravitationally through G = ħc/m_P². Their electromagnetic behaviour
depends on whether the residual CP charge configuration is net neutral —
an open question. If primordial black holes formed and have evaporated,
a cosmological relic density would follow, but deriving that bound is
deferred.

**Q10. Has this been reviewed?**
No dedicated round exists — and the foundation is thinner than it may
appear: GR-1c's Planck-core theorem, on which everything here rests, is
itself unreviewed (CONV-027 covered only GR-1c's field-equation
Proposition). What *is* externally confirmed is the exterior physics,
which is why the claim that ordinary evaporation runs unchanged for
M ≫ m_P is on firm ground.

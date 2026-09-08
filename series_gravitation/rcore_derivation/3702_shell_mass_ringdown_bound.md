# AP-5 owed item 2, reframed by a consistency check: the ringdown bounds the visible shell's MASS, and with it the object's tidal response. 3675's GR admittance needs Schwarzschild(M) continued through the shell, i.e. the enclosed demand ≈ M from 8M/3 down to the wave horizon. A mass fraction μ in the shell weakens the sea's potential there and shifts the (2,2) pole: +2.3% at μ = 0.05, +5.3% at 0.10, +12% at 0.20. GW150914's box admits μ ≲ 0.10; GW250114's percent-level box admits a few percent. Hence Λ̃(shell) ≲ 0.2 (estimate-grade), PRED-O-40 sharpened — and a NEW constraint on the register sector: the R-core is centrally concentrated, ≳ 90% of M inside 2M; a uniform flat core (42% inside 2M) is excluded for black holes by the ringdown

**Patch 3702, Session 166, 8 Sep 2026.** Verify `code/3702_shell_mass_ringdown_bound_verify.py` (3/3, ~3 min). Reasoning `reasoning/3702.md`. Proxy interior (indicative, not a derived register profile): m(r) = M(1 − μ) for r ≤ 2.2M, rising linearly to M at 8M/3; Zerilli-type potential with M → m(r); ingoing at r₊ = 2M(1 − μ); exterior vacuum M; the panel-standard machinery of 3675 (Leaver at μ = 0 to 0.005%).

## §1 The consistency requirement nobody had written down
The wave-sector result under D3 (3675 T1; 3668 T3 at Kerr) is that the surface presents GR's admittance because the wave propagates on the sea's demand field, *which was taken to be Schwarzschild(M) all the way to v = 2*. The demand field at a radius inside the R-core is the count of DI-bits from the CPs *interior* to it (the count law's shell theorem, 3693 T3): it equals M/r̄ only if the CPs are all inside. The register sector's picture of a flat core with matter throughout (3636 for neutron stars; the excluded budget profile for the R-core, density rising outward) would put a large fraction of M in the visible shell 2M → 8M/3, where it would *reduce* the sea's enclosed demand and change the potential the wave sees. **So the ringdown result and the interior matter distribution are coupled**, and the ringdown constrains the distribution.

## §2 The bound (T1–T3)
| μ = M_shell/M | δf/f (2,2) | δτ/τ | GW150914 box (+6.3/−4.8 %; +24/−22 %) |
|---|---|---|---|
| 0.02 | +0.8 % | +3.6 % | inside |
| 0.05 | +2.3 % | +8.5 % | inside |
| 0.10 | +5.3 % | +14.5 % | inside (edge) |
| 0.20 | +12.1 % | +14.3 % | **outside** |
| 0.30 | +18.6 % | −3.5 % | **outside** |
**μ_max ≈ 0.10 on GW150914's box; a few percent on GW250114's** (its two-mode ringdown pins f₂₂₀ at the percent level; not folded in numerically here). The shell's tidal response scales with the responding mass at fixed radius, so **Λ̃(shell) ≲ μ_max × 1.7 ≈ 0.17** (GW150914) and **≲ 0.05** (GW250114), estimate-grade. **PRED-O-40 sharpens: 0 < Λ̃ ≲ 0.2**, two orders below GW250114's 34.8 and an order below 3685's full-body bound — still non-zero, still CPP's own signature, further from reach.

## §3 The structural finding
**The R-core is centrally concentrated: ≳ 90% of M inside the wave horizon at 2M.** For a uniform-density core of radius 8M/3 the mass inside 2M is (3/4)³ = 42%: excluded by the ringdown for black holes. This is a constraint on AP-5's register (clock) law — owed item 3 — that did not exist before this check: whatever D1 + D2 give for the interior profile of a collapsed object, the matter must be deep inside the wave horizon, with the visible shell nearly empty (≲ 10%, likely ≲ 3%). Two readings consistent with the record: (i) the collapse continues inward *below* 8M/3 at up to c/2 (the floor caps displacement per Moment, not position) until the matter is deep inside, and 8M/3 is where the *register* saturates in the field, not where the matter stops; (ii) the R-core's density rises steeply inward. Neither is the flat core of the neutron-star case — and it need not be: neutron-star cores have no wave horizon and D/K barely above 1, so the flat-core statics (3634–3637) stand there; the black-hole interior is the deep-saturation regime (depth 3 at the horizon, more inside) where the profile is a different object. **The register law must produce both.**

## §4 Standing
- Owed item 2: the object's Λ̃ is now bounded from the ringdown, **0 < Λ̃ ≲ 0.2** (GW150914 box) — the number itself awaits the interior profile (item 3), on which it now depends explicitly.
- Owed item 3 (clock law) acquires a constraint: central concentration ≥ 90% within 2M for black holes; flat core for neutron stars.
- PRED-O-40 sharpened in the next `predictions.md` touch (with V2.9); PRED-O-39 and 41 unaffected.
- The proxy is labelled: a Zerilli-type potential with m(r) in place of M is the standard indicative treatment, not the matter-coupled even-parity equation; the sign and order of the shift are robust (a weaker interior potential raises the frequency), the percentages are indicative.

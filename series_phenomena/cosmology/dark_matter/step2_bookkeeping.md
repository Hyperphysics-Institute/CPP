# DM Arc — Step 2: Free vs Baryon-Bound Bookkeeping

**Patch:** 0704 (Session 149, 31 May 2026) · **Work item:** OPEN-COSMO-DM-1 Step 2 · **Gate:** bookkeeping
**Status of result:** order-of-magnitude — **NO kill, NO clean pass.** The gate is satisfiable but explains nothing, and it exposes one real structural dependency.
**Verify:** `scripts/0704_bookkeeping.py`

---

## 1. What Step 2 tests

The "second-cheapest kill." For free qDP/hTetra concentrations to *be* dark matter, the free population must total ~5× the baryonic mass (observed Ω_DM/Ω_b ≈ 5.36), and the qDP/hTetra already bound inside nucleons must not be double-counted into the free total.

## 2. The three sub-questions, answered

**(a) Is abundance the constraint? No — the reservoir is vast.** The Dipole Sea is the vacuum substrate. At the confinement scale (one ~0.3 GeV net-neutral DP per ~r₀³ cell, a deliberately conservative lower bound) its density is ρ_Sea ≈ 3×10¹⁹ kg/m³ — ~10² × nuclear density. Against ρ_DM ≈ 2.3×10⁻²⁷ kg/m³, the swirl *overdensity* needed to source all cosmic-mean dark matter is δ = ρ_DM/ρ_Sea ≈ **7×10⁻⁴⁷** (halo-scale: ~10⁻⁴¹). So ~5:1 is trivially reachable from an infinitesimal Sea overdensity. There is no scarcity problem; if anything the reservoir is embarrassingly large.

**(b) Is double-counting the problem? No — it is a ~19% effect, cleanly avoidable.** If the baryon-internal qDP/hTetra (≈ρ_b) were wrongly added to the free total, the ratio would read 6.36 instead of 5.36 — a 19% inflation, not an order of magnitude. The bound population is cleanly separable (in-baryon vs in-Sea-clump), and the surviving baryon relic is set by η ≈ 6×10⁻¹⁰, negligible against the Sea. The gate's stated worry (double-counting) is therefore *not* where the difficulty lies.

**(c) The actual constraint: does the uniform Sea gravitate?** This is what Step 2 surfaces that wasn't on the table. If the uniform ambient Sea gravitated cosmologically, Ω_Sea = ρ_Sea/ρ_crit ≈ **10⁴⁵** (QCD-scale; ~10¹²⁰ for a Planck-scale Sea) — the vacuum catastrophe. So the dark-matter picture *requires* the uniform Sea **not** to gravitate cosmologically while its swirl-inhomogeneities **do**. In CPP that is at least self-consistent in spirit — gravity is the *gradient* of ΔSSV, so a uniform Sea exerts no force — but whether "only inhomogeneities gravitate" reproduces the observed Friedmann expansion (which does respond to uniform radiation/matter density) is unbuilt. This ties the bookkeeping directly to the cosmological sector and the cosmological-constant problem (OPEN-SR-5).

## 3. Verdict

**No kill, no clean pass.** Two honest takeaways:

1. **The ~5:1 ratio is not derived.** It is set by the free primordial swirl-overdensity amplitude (δ ≈ 10⁻⁴⁷), which is exactly as unexplained as ΛCDM's Ω_DM/Ω_b — the conjecture *relocates* the cosmic coincidence rather than resolving it. §6c already concedes this: *"the relative abundances at STP are empirical questions."* Nothing in the eDP:qDP = 1:1 lock or the hTetra freeze-out pins the overall DM/baryon ratio to ~5.

2. **The real open requirement is the Sea-gravitation consistency** — that the uniform Sea is gravitationally inert cosmologically while its concentrations gravitate as DM. This could be a *feature* (a native dodge of the vacuum-energy catastrophe) or a *liability* (conflict with the Friedmann success of standard cosmology); it cannot be adjudicated until the cosmological sector exists.

## 4. What this means for the arc (gate status)

- The bookkeeping gate does **not** falsify CONJ-COSMO-1 — there is no abundance or double-counting kill.
- But it **does not vindicate it either**, and it demotes the gate from "second kill" to "satisfiable-but-empty": passing it costs one tuned input (the swirl amplitude) the framework does not yet predict.
- **Two derived requirements for CONJ-DPS-2 / CONJ-COSMO-1 going forward:**
  - (R1) a structural reason — if one exists — for the swirl amplitude / DM-baryon ratio, or an explicit acknowledgement that it is inherited as a free input on par with ΛCDM;
  - (R2) the Sea-gravitation consistency, **GATED on OPEN-SR-5** (cosmological constant / vacuum DP-sea energy). Recommend cross-linking OPEN-COSMO-DM-1 ↔ OPEN-SR-5 and treating the cosmological sector as a hard prerequisite for any *quantitative* DM cosmology (Steps 4–5), not just this gate.

## 5. Recommendation

Steps 1 and 2 are now both computed and both survive (no kill). Per the handover hard rule, paper/anthology framing is unlocked — but I would **not** advise writing yet, because the honest headline so far is "no showstopper, two derived requirements, one of them gated on an unbuilt sector." The higher-value next move is to confront R2 directly: scope what the CPP cosmological sector (the Friedmann analog / OPEN-SR-5) must say about Sea gravitation, since both the halo dynamics (Step 5) and the DM-baryon ratio (R1) ultimately ride on it. Step 3 (coldness) and Step 4 (power spectrum) are cheaper and can proceed in parallel, but they are subordinate to the Sea-gravitation question.

# Brick #4 follow-up: the "crowded launch lane" tested — packing gives power laws, not ln(n)

*Patch 0748, Session 154. Tests the "crowded launch lane" mechanism proposed in the swarm
(Thomas + Copilot) as an *organic* source of the harmonic/ln(n) depth law. Toy + verify (with
simulation): `series_phenomena/cosmology/early_universe/scripts/0748_launch_lane_test.py`. NO THEO.
**Result: simulated, it does NOT give ln(n). 1D no-passing lane → constant reach → n_s = 1 (cliff);
3D radial fill → PSR_base ∝ n^{1/3} → n_s = −1. Both excluded. Packing/exclusion order-statistics give
power laws, never the harmonic series. n_s = 0.9649 stays viable-and-favored, not derived.***

## What the transcript got right (credit where due)

The conversation's *negative* results are correct and match the 0747 audit:
- Geometric "equal-N shells" give ΔR = ⅓R and R ∝ N^{1/3} ⇒ increments ∝ k^{−2/3} — **not** harmonic.
- Brownian diffusion gives a **Gaussian** profile (not exponential, not harmonic).
- Linear per-CP ⇒ ∝ n (excluded); (n−1)/n ⇒ saturating constant ⇒ the n_s = 1 cliff (excluded).
- Thomas's own hand-assigned "1, 1+½, 1+½+⅓…" was correctly flagged (by Thomas) as a *tuning*, not a
  mechanism — exactly the right instinct.

So the diagnosis was sound: ln(n) needs the per-CP increment to fall as 1/k (harmonic), and the
mechanical/geometric forms don't do it.

## What was tested here: the "crowded launch lane"

Proposal: n CPs stacked on a GP launch along the SSV direction; random order, finite reach PSR_base,
no passing, no double occupancy; the claim is that the order statistics yield a harmonic progression
→ PSR_base(n) ∝ ln n. **Simulated** (not assumed):

- **1D no-passing lane:** the first CP always reaches the far end L; later CPs pack inward (L, L−1, …).
  The **outermost reach is constant (= L)** ⇒ PSR_base(n) = const ⇒ **n_s = 1 (HZ cliff)**. The mean
  reach is linear-decreasing. And a lane cannot hold n ∼ 10⁷⁹ CPs anyway. Not harmonic.
- **3D radial fill:** CPs launch in random directions, each occupies the first free GP along its ray.
  Simulated R(n) fits **R ∝ n^{0.29}** (≈ n^{1/3}, finite-size sim slightly low) ⇒ PSR_base ∝ n^{1/3}
  ⇒ **n_s = −1**, excluded. (Same k^{−2/3} the geometric shell argument gave — it *is* the geometric
  effect.)

A log would barely move (ln 200 = 5.3 → ln 12800 = 9.5); the sim went 5.7 → 19.0 — clearly power-law,
not logarithmic.

## Why "order statistics → harmonic" is a misapplication

The **positions / gaps** of n points packed in a lane or ball are **uniform** (gaps ∼ L/n) or
**power-law** (R ∼ n^{1/d}) — never harmonic. The harmonic series 1 + ½ + ⅓ + … appears in probability
only in **records / coupon-collector** counts (expected #records in n trials = Σ1/k) and in the
**entropic derivative** d/dn ln(n!) ∼ ln n. It does **not** appear in where particles physically land
under packing/exclusion. This mechanism is packing, so it returns power laws.

## The real pattern (the honest lesson)

Tally of every depth-law mechanism tested across 0745–0748:

| mechanism | PSR_base(n) | n_s | status |
|---|---|---|---|
| mechanical linear / per-CP | ∝ n | −5 | excluded |
| pairwise repulsion | ∝ n² | −11 | excluded |
| surface / screened-power | ∝ n^{2/3} | −3 | excluded |
| geometric shell / 3D fill / launch-lane | ∝ n^{1/3} | −1 | excluded |
| (n−1)/n, 1D lane | → const | 1 | excluded (cliff) |
| diffusion | Gaussian | — | no harmonic structure |
| **configurational chemical potential / records** | **∝ ln n** | **0.9649** | the only survivor |

**Mechanical, geometric, and packing/exclusion primitives ALL give power laws or constants — all
excluded.** The log appears *only* from a genuinely statistical-combinatorial source: the
configurational chemical potential μ = ∂F/∂n with F ∼ −T·ln(W), W = number of microstates of the stack
(equivalently d ln(n!)/dn ∼ ln n), or records/coupon-collector counting.

So the honest tension is now sharp: **the data want ln n; CPP's geometric/dynamical/placement
primitives keep returning power laws.** Getting ln n appears to require a genuinely *entropic*
ingredient — the boost driven by the **configurational entropy** of the stack (how many ways n CPs can
be arranged), a microstate-counting quantity — rather than any placement/launch/geometry rule. That is a
different *kind* of ingredient than anything tried so far, and whether CPP legitimately has it (a
well-defined stack entropy whose derivative drives PSR_base) is the real open question.

## Honest status (unchanged)

- Architecture right (0746): count-driven PSR_base, decoupled from gravity SSV.
- Organic ln(n) mechanism still **not found**; the launch-lane / packing route is now **also excluded**.
- n_s = 0.9649 remains **viable and favored** (the only non-absurd value, and it lands on Planck if the
  boost is logarithmic in the count), **not derived**.
- The sharpened target: a CPP-native **configurational entropy** of the stack whose chemical potential
  (∂/∂n) drives PSR_base — a microstate-counting quantity, not a placement rule. Nothing geometric or
  mechanical will give the log; only counting microstates will.

## Pointers

- Builds on 0747 (micro-rule audit), 0746 (count-vs-stress fork). Tests the Thomas + Copilot transcript.
- Toy + simulation + verify: `.../early_universe/scripts/0748_launch_lane_test.py`.
- Reasoning: `series_relativity/development/reasoning/0748_launch_lane_test.md`.
- THE target: does CPP have a configurational stack entropy S(n) with ∂S/∂n ∼ ln n driving PSR_base?
  That microstate-counting question is the only remaining route to a derived ln n (and thus to making
  n_s = 0.9649 a zero-parameter prediction).

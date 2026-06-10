# How mild is "mild"? Dwarf core radius from σ_V/m ≈ 0.20 — a few-hundred-pc core, flat across scale

**Patch:** 0842 (Session 156, 10 June 2026) · **Type:** first-pass — translates 0841's σ_V/m into a core size. · **Lane:** DM-2 / `dark_matter/` (no shared-file touch; collision-safe vs Project C window).
**Builds on:** 0841 (σ_V/m ≈ 0.20, velocity-independent). **Verify:** `code/0842_dwarf_core_radius.py`.

---

## The clean quantity: the one-scatter density ρ₁

A SIDM core forms where each particle has scattered ~once over the halo age — i.e. where the local density exceeds **ρ₁ = 1/[(σ_V/m)·v·t]**. With σ_V/m = 0.20 cm²/g and t = 10 Gyr:

| scale | v [km/s] | ρ₁ (CPP, σ_V/m=0.20) | ρ₁ (strong SIDM, σ/m=1.0) |
|---|---|---|---|
| dwarf | 30 | 0.078 M⊙/pc³ | 0.016 |
| galaxy | 200 | 0.012 | 0.0023 |
| cluster | 1500 | 0.0016 | 0.0003 |

The core radius is the radius at which the underlying (NFW) profile falls to ρ₁: deeper-than-ρ₁ regions thermalize and core; shallower regions keep the cusp.

## The dwarf core: a few hundred parsecs

For a representative dwarf NFW (ρ_s = 0.02 M⊙/pc³, r_s = 1.5 kpc):

- **CPP (σ_V/m = 0.20): r_core ≈ 0.27 kpc** (~270 pc).
- Strong SIDM (σ/m = 1.0): r_core ≈ 0.81 kpc.

Observed dwarf cores span ~0.2–1 kpc, so **CPP's predicted core sits at the small/detectable edge** of that range — clearly distinguishable from a pure-CDM cusp (r_core → 0), but a factor ~3 smaller than the strong-SIDM interpretation. That is the quantitative meaning of "mild": a real, few-hundred-parsec core, near the current resolution floor for dwarf rotation curves and stellar-kinematic core measurements.

## The cluster side (consistency check)

At cluster velocities ρ₁ ≈ 0.0016 M⊙/pc³ sits below typical cluster central DM densities, so a **modest** central core forms (tens of kpc out of a ~Mpc halo). σ_V/m ≈ 0.20 at cluster scales is **at the edge of current cluster bounds** — comfortably consistent with the looser merger/ellipticity limits (~0.5–1 cm²/g), in mild tension with the tightest cross-system cluster inferences (~0.1). It is not excluded.

## The falsifiable signature: flatness

Because σ_V/m is velocity-independent (0840/0841), **CPP cannot produce the large-dwarf-core / small-cluster-core pattern that velocity-dependent SIDM fits prefer.** It predicts a single flat σ_V/m ≈ 0.20 producing *mild cores at every scale* — ~0.1–0.3 kpc in dwarfs, modest cores in clusters, with no velocity scaling. This is the sharp, testable handle: if the cross-system data require σ/m to fall from ~1–3 (dwarfs) to ~0.1 (clusters), CPP's flat 0.2 is falsified (too small at dwarfs, mildly too large at clusters). If the data are consistent with a flat ~0.1–0.3, CPP predicts it with no free knobs beyond f.

## Robust claims vs caveats

Robust (model-independent): cores are **mild** (~0.1–0.3 kpc in dwarfs), **flat across scale**, and **at the small but detectable edge**. Magnitude caveats: r_core is halo-model dependent (the choice of ρ_s, r_s, the velocity profile, and one-scatter-vs-isothermal modeling — factor ~2), on top of the factor-3 from f (0835). So the *core size* is an order-of-magnitude first-pass (~0.1–0.5 kpc), while the *qualitative pattern* (mild, flat, detectable-edge) is robust. Scope: first-pass, no verdict/THEO/ID; conditional on the qDP/hTetra-DM conjecture, the Mechanism-A measure, and f≈0.2.

# σ/m(v) from the derived residual potential — CPP predicts a *velocity-independent* mild self-interaction (the qDP/hTetra discriminant)

**Patch:** 0840 (Session 156, 10 June 2026) · **Type:** first-pass derivation + observational overlay (the positive discriminant for DM-1). · **Lane:** DM-2 / `dark_matter/` (no shared-file touch; collision-safe vs the Project C window).
**Builds on:** 0831 (residual potential), 0835 (f ≈ 0.2, V₀ ≈ 53 MeV), 0833 (m_qDP ≈ 264 MeV, bosonic). **Figure:** `figures/0840_sigma_over_m_velocity.png`. **Verify/figure:** `code/0840_sigma_v_sidm.py`.

---

## What this computes and why it matters

The consolidation doc (Patch 1200) graded the candidate **consistency-only** because every gate it passed was a generic-CDM test — using the bare geometric σ/m ≈ 4×10⁻³ cm²/g, the candidate was indistinguishable from a collisionless WIMP. The Era-2 derivation replaced that bare guess with a real residual potential (two-gluon color van der Waals, V₀ ≈ 53 MeV, λ ≈ 1.3 fm, hard core ~1 fm; 0831/0835). This patch computes the **velocity-dependent self-interaction cross-section** σ/m(v) from that potential — finite-energy s-wave scattering, m_qDP = 264 MeV — across the dwarf-to-cluster velocity range, and overlays it on the SIDM observational constraints. This is the first qDP/hTetra-**specific** signature in the arc.

## Result: σ/m is velocity-independent

Solving the radial Schrödinger equation at finite collision energy across v = 30 → 3000 km/s:

| v [km/s] | regime | σ/m (f=0.1) | σ/m (f=0.2) | σ/m (f=0.5) |
|---|---|---|---|---|
| 30 | dwarf | 0.205 | 0.148 | 0.019 |
| 200 | galaxy | 0.205 | 0.148 | 0.019 |
| 1500 | cluster | 0.205 | 0.148 | 0.019 |
| 3000 | merger | 0.205 | 0.148 | 0.019 |

**σ/m is flat to all displayed digits across the entire astrophysical range.** The reason is kinematic and robust: kλ ≈ 9×10⁻⁵ (dwarf) to 9×10⁻³ (cluster-merger) — i.e. kλ ≪ 1 *everywhere*, so scattering stays in the s-wave, scattering-length limit (σ → 4π a²) and only develops velocity structure when kλ ~ 1, which is v ~ c. This is a direct consequence of the constituents being **heavy** (264 MeV) and the residual range **short** (1.3 fm). It is the *opposite* of light-mediator SIDM (a light dark-photon/scalar mediator gives σ/m ∝ 1/v⁴, falling steeply with velocity).

**Magnitude (central): σ/m ≈ 0.15 cm²/g** at f ≈ 0.2 (distinguishable s-wave). Two effects move it within an O(1) window: identical-boson statistics (0833) enhance s-wave scattering by ×2 → ≈ 0.30; the viscosity/transfer cross-section relevant for SIDM is ×⅔ for isotropic scattering. The dominant uncertainty is the depth fraction f (0835, factor ~3): the f-band gives σ/m ≈ 0.02–0.25, with a Ramsauer dip near f ≈ 0.5. So: **σ/m ≈ 0.1–0.3 cm²/g, velocity-independent**, magnitude factor-~3, flatness robust.

## Overlay on the SIDM constraints (figure)

- **Clusters** (v ~ 1000–2000 km/s; bound σ/m ≲ 0.1–1 from mergers/ellipticity): the CPP band sits **below** the exclusion — **consistent**.
- **Dwarfs** (v ~ 30–50 km/s; observable cores favor σ/m ~ 0.5–few, coring threshold ~0.1): the CPP band sits **at/just above the coring threshold**, below the strong-core preference — **mild cores, at the low edge**. The identical-boson ×2 line (≈0.3) reaches toward the favored region but does not enter it.

**Honest correction to my earlier framing.** I previously called this "squarely in the live SIDM window." The computation says it is milder and more specific than that: it is at the *low edge* of the window, and — the real headline — it is **velocity-independent**. The distinctive, novel claim is not "strong SIDM cores" but "a *flat* σ/m."

## The discriminant (the publication spine)

This is the positive, qDP/hTetra-specific signature the consolidation doc said was missing, and it discriminates on two axes:

1. **Against collisionless CDM** (WIMPs, axions, sterile neutrinos: σ/m ≈ 0) — CPP predicts a *definite, derived, nonzero* σ/m ≈ 0.1–0.3 cm²/g. Clean.
2. **Against velocity-dependent SIDM** (light-mediator models: σ/m ∝ 1/v⁴) — CPP predicts σ/m **flat** across dwarf→cluster, from the heavy constituent + short range. This is a sharp *qualitative* distinction testable over the full velocity range, and it is the kind of prediction that is hard to mimic and easy to falsify.

**Falsifiability.** If the data ultimately demand velocity-*dependent* SIDM — strong dwarf cores (σ/m ~ 1–few) together with tight cluster bounds (≲0.1) — CPP's flat ~0.15 fails on the dwarf side (too weak for strong cores; it cannot rise at low v). Conversely, if the data settle on a *mild, ~velocity-independent* σ/m ~ 0.1–0.5, CPP predicts it from first principles with no free knobs beyond f. Either way it is a real, falsifiable test, not a consistency restatement.

## Where this sits in the program

This lifts DM-1 from consistency-grade toward a *positive signature* — the microphysics now makes a qDP/hTetra-specific, falsifiable prediction. It is **independent of DM-2** (Sea gravitation) and of **Project C** (the absolute mass scale): the *flatness* is robust to both; only the magnitude's factor-3 would tighten if f is pinned (partly Project C's territory). The full cosmological *identification* still waits on DM-2; this is the content that makes the eventual bank-and-release worth more than consistency-grade.

## Scope

First-pass. **No closure, no THEO/ID, no verdict.** s-wave, distinguishable baseline; identical-boson (×2) and viscosity (×⅔) are noted O(1) refinements; the f≈0.2 magnitude is the 0835 factor-3 estimate; higher partial waves verified negligible (kλ≪1). Conditional on the qDP/hTetra-DM conjecture and the Mechanism-A measure.

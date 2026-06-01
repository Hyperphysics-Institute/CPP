# DM Arc — Step 5: Quantitative Halo / Rotation Curve

**Patch:** 0724 (1 June 2026) · **Work item:** OPEN-COSMO-DM-1 Step 5 · **Gate:** rotation curve
**Status of result:** **PASS (representative galaxy).** c05's zero-parameter force law + a collisionless qDP/hTetra halo reproduce an approximately flat rotation curve (~220 km/s) for a Milky-Way-like galaxy, with M_halo/M_baryon ≈ 4.5 within 30 kpc — consistent with the Step-2 reservoir and the canonical ~5:1.
**Verify:** `scripts/0724_rotation_curve.py` (CHECK 1/2/3 PASS)
**c08 exposure:** **LOW.** This rides on c05 *local* gravity (Newtonian limit), which is derived and not contingent on the OPEN-SR-5 cosmological field-equation condition. (Step 4, power spectrum, is the c08-exposed half.)

## What was computed

- **Force-law foundation (CHECK 1).** c05 gives F = G m m'/r² with G = ℏc/m_P², m_P the 600-cell lattice scale — a zero-parameter law (matches CODATA G), not a GR fit. The rotation-curve dynamics ride on this.
- **Isothermal halo → exactly flat (CHECK 2).** A singular isothermal qDP/hTetra halo, ρ = v_flat²/(4πG r²), gives M(<r) = v_flat² r/G and hence v(r) = v_flat *exactly* at all radii. The flat rotation curve is the direct consequence.
- **Representative galaxy (CHECK 3).** Exponential baryonic disk (M_disk = 6×10¹⁰ M_⊙, R_d = 3 kpc) + cored isothermal halo (r_c = 4 kpc, v_flat = 220 km/s): the baryons-only curve declines Keplerian beyond the disk (113→93 km/s, 20→30 kpc), while disk+halo stays flat (219→218 km/s) with v(8 kpc) = 214 km/s (observed ~220). The halo/baryon mass ratio within 30 kpc is 4.5 — trivially supplied by the Step-2 reservoir.

## Honest framing (this is the load-bearing caveat)

**A flat rotation curve is a GENERIC outcome of any extended collisionless halo under Newtonian gravity — it is not, by itself, a CPP-discriminating prediction.** Every viable dark-matter model reproduces flat curves; that is the low bar of admission, not a distinguishing success. What is CPP-specific here is narrower and should be stated as such:

1. The force law is **c05-derived** (G fixed by the 600-cell, zero parameters) rather than a fitted Newtonian/GR input.
2. The halo is the **same qDP/hTetra population** independently vetted in Steps 1–3 (collisionless, abundant, cold) — **no new dark sector** beyond the Dipole Sea is introduced.
3. c05's shell-broadcast force **superposes cleanly to a diffuse, extended source** (the Step-0 regime-of-validity audit), so applying it to a galactic halo is legitimate.

## What is NOT done (the discriminating test)

The genuinely CPP-discriminating result would be to **derive the halo profile ρ(r) from CPP swirl dynamics** (the early-universe radial-expansion seeds + collisionless gravitational evolution) — predicting isothermal/NFW rather than *assuming* it, and predicting halo scaling relations (e.g. the baryonic Tully–Fisher relation, core sizes). That derivation is the open piece and overlaps **Step 4 (power spectrum)**; it is not attempted here. Assuming the profile and recovering flat curves is a necessary consistency check, passed — not the discriminating win.

## Status of the arc after Step 5

- **Steps 1, 2, 3, 5 done (survive); Step 0 audited.** Only **Step 4 (power spectrum)** remains for the falsification-first sequence — the harder, more c08-exposed, and most discriminating step (does the swirl-seed mechanism reproduce the observed P(k)?).
- CONJ-COSMO-1 (Tetra-Gravity Dark Matter) remains a conjecture; the cheap kills are all survived and the rotation-curve consistency holds, but the discriminating tests (profile from first principles; power spectrum) are the remaining substance.

## Honest caps

- Representative-galaxy demonstration with assumed halo profile; not a population fit, not a derived profile.
- The cored-isothermal inner rise is a modeling choice (cuspless); CPP does not yet predict core vs cusp (the cusp-core problem is untouched).
- Inherits the Step-1 qDP/hTetra mass *estimates* (~0.3–1.5 GeV); a lighter qDP would not affect the rotation curve (gravity is mass-blind given the halo density) but matters for Steps 1/3.

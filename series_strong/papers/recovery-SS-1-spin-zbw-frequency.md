# Recovery — Spin-½ and the Inner/Outer ZBW Orbital Frequency Ratio

**Type:** Tier-4 reasoning-recovery artifact (pre-rigid-documentation derivation recovered into the rigid corpus).
**Recovers:** the original derivation behind CONJ-P-SS-1 ("2:1 ZBW orbital frequency ratio"), used implicitly in SS-1 and as a foundational input in SF-4.
**Source:** claude.ai chat `ee212abb-bed7-418f-aae7-5a801b3b6f30` ("Buffer overflow content replacement", 19 March 2026), the "Spin I / ZBW Mass companion" working LaTeX, predating the Four-Tier Documentation Discipline. Referenced downstream in chat `a49b320e` (SS-1 development window).
**Status:** RECOVERED. The recovered derivation **contradicts the "2× frequency" statement as recorded in CONJ-P-SS-1 and SF-4** (see §3). Corrected result registered; THEO candidate pending multi-AI review (Session 149, Patch 0572b).

---

## 1. The recovered derivation (faithful)

A captured dipole pair (DP) orbits the central unpaired CP of a spin-½ fermion. In the Mode-2 standing-wave configuration the two poles sit at fixed radial nodes/antinodes:

- inner pole (the +eCP for the electron) at the interior antinode **r_in = r_th/3**;
- outer pole (the −CP) at the interior node **r_out = 2·r_th/3**;

where r_th = ℏ/(2 m_e c). Hence the **radius ratio**

> **r_out / r_in = 2** (exact)

is fixed by the integer arithmetic of the Mode-2 trigonometric zeros, independent of r_th, m_e, e, ℏ, k_e.

**Orbital frequencies (force balance).** Each pole orbits the centre under the 1/r² Coulomb force, so centripetal balance gives ω² = k_e e² /(m r³), i.e. ω² ∝ 1/r³. Therefore

> (ω_in/ω_out)² = (r_out/r_in)³ = 2³ = 8 ⟹ **ω_in / ω_out = 2√2** (exact)

again independent of all physical constants. The tangential speeds follow: v_in/v_out = √2 (the speeds are **not** equal).

**Spin quantization.** Total orbital angular momentum L = m_e ω_out r_in² (2√2 + 4); imposing L = ℏ/2 fixes r_in = a_Bohr / [4(1+√2)²].

**Phase lock (anti-winding).** Because ω_in ≠ ω_out the DP would otherwise wind up; the inner +eCP's **radial ZBW at the Compton frequency** ν_C = m_e c²/ℏ phase-locks the two orbits (beat frequency (2√2 − 1)ω_out locked to the ZBW), and the configuration is non-radiating because it is a standing pattern in the 600-cell lattice, not an accelerating free charge.

**Universality.** The derivation uses only (i) the 1/r² force law, (ii) the standing-wave condition r_out = 2 r_in, (iii) L = ℏ/2. None is electron-specific, so spin-½ is universal: muon/tau via eDP capture, quarks via qDP capture (strong-force analogue of the Coulomb potential), neutrinos via neutral-DP capture. The photon's spin-1 is two-CP capture.

## 2. What is actually derived

Three distinct quantities, none of which is "frequency ratio 2":

| Quantity | Value | Origin |
|---|---|---|
| Radius ratio r_out/r_in | **2** (exact) | Mode-2 standing-wave nodes |
| Orbital angular-frequency ratio ω_in/ω_out | **2√2 ≈ 2.828** (exact) | 1/r² force balance + radius ratio |
| Inner radial ZBW frequency | Compton ν_C = m_e c²/ℏ | ZBW-mass companion |

## 3. The discrepancy (the reason this is a correction, not a confirmation)

CONJ-P-SS-1 and SF-4 record the result as **"inner orbital at 2× the outer frequency"** — a *frequency* ratio of **2**. The recovered derivation gives a frequency ratio of **2√2**, with **2** being the *radius* ratio. The "2× frequency" statement therefore conflates the radius ratio with the frequency ratio (or silently drops the √2).

A frequency ratio of exactly 2 would require **equal orbital speeds** (v_in = v_out ⟹ ω ∝ 1/r ⟹ ω_in/ω_out = r_out/r_in = 2). But equal speeds are not force-balanced; the derivation explicitly gives v_in/v_out = √2. So the force-balanced (Kepler) frequency ratio is 2√2, and "2×" is not a force-balanced result.

**Provenance (per Thomas, Session 149):** the "2×" value originated with Grok and was confirmed by Sonnet; it entered CONJ-P-SS-1/SF-4 as the working convention. The careful standing-wave + Coulomb derivation recovered here (which postdates the rough "2×" and was not migrated into the rigid corpus) gives 2√2. Thomas holds no investment in the "2×" value and directs that the canonical claim be whatever calculation is correct and the reviewers sign off on.

## 4. Implications

1. **CONJ-P-SS-1** is corrected to the true result (radius ratio 2 / angular-frequency ratio 2√2) — see Patch 0572b CONJ.md edit.
2. **SF-4** uses the relationship only as a *phase-lock* — Picture A (the shipped d_eff = 5 closure) merges spin + orbital orientation into one channel because they are locked to a single geometric direction, which the recovered derivation establishes regardless of the ratio value. The ratio's numeric value (2 vs 2√2) is **not** load-bearing for σ_ν = z⁻¹⁰. Only the wording "2:1 frequency" is inaccurate. Picture B (not selected) is the one that depended on the literal value 2 ("two inner half-cycles per moment"); the 2√2 correction therefore *strengthens* the Picture-A-over-B argument. SF-4 reconciliation = wording fix → v1.1 (Patch 0572c).
3. The genuine theorem is **spin-½ universality from {1/r² force, standing-wave r_out = 2 r_in, L = ℏ/2}, yielding ω_in/ω_out = 2√2** — a different, richer statement than "2× frequency." Registered as a candidate pending the multi-AI review cycle (Patch 0572d), per the THEO-DSL-N candidate→confirmed precedent and Thomas's reviewer-sign-off criterion.

## 5. Trivial verification

ω ∝ r^(−3/2) (Kepler for 1/r²) with r_out/r_in = 2 gives ω_in/ω_out = 2^(3/2) = 2√2 ≈ 2.8284. The model assumption to scrutinize is the two-poles-at-different-ω picture held from winding by the ZBW phase-lock (recovered §1); this is the foundational input a reviewer should press.

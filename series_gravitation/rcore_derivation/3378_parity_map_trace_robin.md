# The parity map — the register pins the spatial TRACE, which is a frequency-dependent Robin wall on the Zerilli function; a conformal ansatz cannot carry an even-parity wave; the odd sector is OPEN; the a = 0 line moves

**Patch 3378, Session 161, 2 Sep 2026.** Verify `code/3378_parity_map_trace_robin_verify.py` (17/17). Reasoning `reasoning/3378.md`. Closes the conditional step of 3377; overwrites 3377's "Dirichlet on Z⁺" branch.

**Standing:** Parts 1–2 DERIVED (symbolic; two independently recalled reconstruction formulas agree identically, which is the check on both). Part 3 COMPUTED at a = 0 (indicative for the Kerr flagship). Part 4 OPEN.

## §1 A conformally-flat spatial slice cannot carry an even-parity gravitational wave

CPP's spatial metric is `ψ⁴ δ_ij`, set by the register. In a Regge–Wheeler-type gauge (`G = h₁ = 0`) that is `H₂ = K`. Three facts, all symbolic:

1. The two standard reconstructions of `(K, H₂)` from the Zerilli–Moncrief function `Z⁺` — Lousto–Price's explicit `H₂` and the inversion of Moncrief's definition — **agree identically**. (Recalled independently; their agreement is the check on both.)
2. For a Zerilli mode, `H₂ − K = c₁(r, ω) Z⁺ + c₂(r) Z⁺′` with `c₂ = −M(λr + 3r − 3M)/(r(λr + 3M)) ≠ 0` and `c₁ ≠ 0` (carrying `ω²`). A propagating mode has `H₂ ≠ K`.
3. With `G = h₁ = 0` fixed, the only residual gauge freedom is `ξ_t`, whose Lie derivative leaves `g_rr` and `g_θθ` unchanged: **`H₂ − K` is gauge-fixed-invariant.**

Hence `H₂ = K` everywhere is not a gauge choice but a *physical restriction* that excludes propagating even-parity waves. **The register field is not the even-parity gravitational wave.** The wave's traceless part `H₂ − K` lives outside CPP's scalar dictionary. This is the CONV-028 "scalar vs rank-2 charter language" flag, now with a theorem behind it.

## §2 What the register mirror pins: the trace — and it is a Robin law on `Z⁺`

To first order the conformal factor is the spatial trace: `δ ln ψ⁴ = (H₂ + 2K)/3`. "Register pinned at the wall" is therefore

    H₂ + 2K = 0   at r_w,

**not** `Z⁺ = 0` (3377's conditional branch) and **not** `K = 0` alone. Through the reconstruction, with `Z⁺″` eliminated by the Zerilli equation, this is one Robin condition on the even master function:

    (dZ⁺/dr*)/Z⁺ = β(ω) = [ 2.496 − 14.46 (Mω)² ] / M        (ℓ = 2, r_w = 9M/4).

`β` is **frequency-dependent** (the `ω²` enters because `H₂` involves `Z⁺″`) and **changes sign at Mω₀ = 0.415** — Neumann on `Z⁺` there. The flagship's `Mω = 0.366` sits 12% below the crossing, where `β = +0.56/M`: neither Dirichlet nor Neumann.

3377's "20° on the odd sector" was conditional on `Z⁺ = 0`; that map does not hold. Withdrawn.

## §3 The a = 0 line under the derived wall (even sector, Zerilli, Wigner scan as at 3297 Check 7)

| Wall | lowest resonance Mω | Wigner delay | Hz at 62 M_⊙ (a = 0) |
|---|---|---|---|
| Dirichlet (shipped assumption) | 0.457 (broad; 0.436–0.468 plateau) | ~20 | 238 |
| **β(ω), derived** | **0.412** | ~250 (see below) | **215** |
| Neumann β = 0 (diagnostic) | 0.382 — at the barrier top | 88 | 199 |
| β = 0.56 const (flagship value, diagnostic) | 0.444 | 31 | 231 |

`|R| = 1` for all walls (1e-9). **The derived wall moves the lowest even-sector resonance down by ~5–10% and narrows it** — a Neumann-like wall supports a near-trapped mode at the barrier top (delay 88 vs 20), and the derived wall is Neumann exactly at 0.415. The 250 delay at 0.412 sits at the sign change and includes the boundary's own dispersion (`−2β′/ω ~ 60`): **its width is not a cavity Q and is not claimed.** The physical statement is the shift and the softening, not a line width.

At the Kerr flagship (χ = 0.68, 191 Hz) the recompute requires the Teukolsky/even-sector map — next.

## §4 The odd sector is OPEN

The register does not govern the traceless part. CPP has no rank-2 dictionary. So the odd-parity wall law is not derived, not derivable from the register, and — since 3297 — the ladder GR-2 shipped (RW axial, then Teukolsky s = −2 with `X = 0`) was computed on a sector the theory does not yet constrain, with a wall it never derived. **The CPP prediction at a = 0 is the even sector under the trace-pinned Robin wall.** Whether the odd sector echoes at all is a question about the DP-sea's anisotropic (vector) response — a physical-picture question, the founder's, if the arc needs it.

## §5 What changes, and what is owed

- 3377: Robin-on-odd branch withdrawn; parity finding stands and is now the *reason* the odd sector is open.
- GR-2: caveat (a) becomes a derivation on the even sector and an OPEN on the odd; V2.0 = even-sector line set under `β(ω)` with the Kerr recompute. Not enacted here.
- **Owed:** (i) the Kerr recompute — the even-sector wall under χ ≠ 0 (Teukolsky ↔ Zerilli map at the wall, or a Kerr–Zerilli-type even master equation); (ii) the O(kd) skin term (3376 formulation) as an amplitude correction on top of `β(ω)`; (iii) the odd-sector rule, if any — founder.
- This is not yet the win: the flagship number moves but the Kerr value is not computed. The panel waits.

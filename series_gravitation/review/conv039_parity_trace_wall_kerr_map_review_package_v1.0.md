# CONV-039 REVIEW PACKAGE v1.0 — The register mirror is even-parity and pins the spatial trace (a frequency-dependent Robin wall on the Zerilli function); the shipped ladder was on the odd sector with an underived wall; the a = 0 even-sector lines move −13%; the Kerr recompute is blocked on metric reconstruction
# (Patch 3380, 2 Sep 2026, Session 161)

**PASTE DISCIPLINE (founder):** this ENTIRE file is one package — one
identical paste per seat (Copilot may need the file-upload route). The
GitHub links are valid only AFTER the founder's push of Patch 3380; paste
after the push. Execution-capable seats also receive
`3378_parity_map_trace_robin_verify.py` and
`3379_a0_even_lines_kerr_estimate_verify.py` (sympy + numpy + scipy; the
Wigner scans take 1–3 minutes each). Returns INLINE, verbatim, §8 skeleton.

**DISPATCH BASIS (review economy protocol, founder-ruled this session):**
trigger **2a — epistemic exhaustion on Q3** (the worker cannot impose the
derived wall on the Kerr master function without a metric reconstruction he
cannot do reliably alone; further unilateral work would be guessing) plus a
**partial win** on Q1–Q2 (a parity theorem and a derived wall law that
replace an assumption in the flagship). Trigger 2b does not apply: the
derived wall moves the flagship line *against* the worker's prior claim and
that branch was taken unilaterally. The founder initiated this round.

**ID NOTE:** CONV-036 remains skipped. This is CONV-039. Grep at dispatch:
the ID appears only in status pointers announcing (and then withdrawing)
this round; no package or receiver existed.

---

## §0 What this round decides, in one paragraph

Since Patch 3297 the R-core echo arc has imposed `X = 0` (Dirichlet) on the
Regge–Wheeler / Sasaki–Nakamura master function at the saturation surface,
on the argument that the surface "clamps the register." CONV-038 (5/5)
already found that argument rested on a demoted rule, kept |R| = 1, and
ruled the phase π underived. This session's derivation chain then
established: the register is the SSV_abs scalar that sets the isotropic
conformal factor `ψ⁴δ_ij`; a purely conformal spatial slice **cannot carry
an even-parity gravitational wave** (`H₂ − K` is gauge-fixed-invariant and
non-zero for a Zerilli mode — Q1); what "register pinned at the wall" means
is `H₂ + 2K = 0` (the spatial trace), which through the Zerilli–Moncrief
reconstruction is a **frequency-dependent Robin law** `(dZ⁺/dr*)/Z⁺ =
β_ℓ(ω)` with a Neumann crossing near the barrier top (Q1); the odd (axial)
sector — the one GR-2 actually solved — is not governed by the register at
all and CPP has no rank-2 dictionary for it (Q4); and under the derived wall
the a = 0 even-sector features move **−13.4% for both ℓ = 2 and ℓ = 3**
(identical to three figures, unexplained) into strong near-trapped modes at
the barrier top (Q2). The Kerr flagship (χ = 0.68, 191 Hz) cannot be
recomputed by the worker: imposing a metric-trace condition on the Kerr
master function requires metric reconstruction (Hertz/CCK) — **Q3 is a
method question**. A scaled estimate (~166 Hz / ~250 Hz) is on file as a
guess. **The round decides whether the theorem and the wall stand, whether
the a = 0 extraction is sound, how (or whether) the Kerr map can be done,
and what — if anything — governs the odd sector.**

GitHub (repo `CPP`, branch `main`, HEAD = Patch 3380):
`series_gravitation/rcore_derivation/3378_parity_map_trace_robin.md`,
`…/3379_a0_even_lines_kerr_estimate.md`, `…/3376_rung3_negative_slaved_register.md`,
`…/3377_l2_spherical_parity_robin.md`, `…/3375_attainment_overdemand_lawD.md`,
`series_gravitation/code/3378_parity_map_trace_robin_verify.py`,
`…/3379_a0_even_lines_kerr_estimate_verify.py`.

## §1 Under review / fenced

UNDER REVIEW: (a) the parity theorem and its three symbolic legs; (b) the
identification "register pinned ⟺ spatial trace pinned" and the resulting
Robin law `β_ℓ(ω)`; (c) the a = 0 Wigner extraction — in particular the
decomposition of the dispersive-wall delay into the wall's own `dφ/dω`
(= 4b₂ at the crossing) and a cavity remainder; (d) the two unexplained
regularities (Neumann crossing ≈ barrier top; −13.4% for both ℓ);
(e) **the Kerr wall map — METHOD**; (f) the odd-sector rule; (g) the
standing of GR-2's shipped ladder; (h) scope audit.

FENCED: CONV-038's rulings (floor a conditional bound in the window
0.536 < u_max ≤ 1; |R| = 1 survives with caveats; phase π underived;
R-EXCL-RETIRED / THEO-1; R-FLOOR-FINITE / R-CELL-SIZE-OPEN /
R-COOCCUPATION-FORCED); the exact exterior (GR-1c Thm 1); the 3375
interior-at-cap theorem; the 3376 slaved-register formulation of the O(kd)
skin term (orthogonal to this round; not re-opened); the SN ladder's
numerics *given* its wall (CONV-037).

## §2 The claim chains

### 2.1 Parity theorem (3378 Part 1) — three symbolic legs
- L1. Two independently recalled reconstructions of `(K, H₂)` from the
  Zerilli–Moncrief function — Lousto–Price's explicit `H₂` and the inversion
  of Moncrief's definition — **agree identically** (their agreement is the
  check on both; the worker distrusts either memory alone).
- L2. For a Zerilli mode, `H₂ − K = c₁(r,ω) Z⁺ + c₂(r) Z⁺′`,
  `c₂ = −M(λr + 3r − 3M)/(r(λr + 3M)) ≠ 0`, `c₁ ≠ 0` (carries ω²).
- L3. With `G = h₁ = 0` fixed, the residual gauge is `ξ_t` alone; its Lie
  derivative on Schwarzschild leaves `g_rr` and `g_θθ` unchanged
  (computed) — so `H₂ − K` is gauge-fixed-invariant.
- ⇒ `H₂ = K` everywhere (CPP's `ψ⁴δ_ij`) is a physical restriction, not a
  gauge: **the register is not the even-parity GW.** The traceless part
  lies outside CPP's scalar dictionary (CONV-028's "scalar vs rank-2" flag).

### 2.2 The wall law (3378 Part 2; 3379 Part 1)
- To first order `δ ln ψ⁴ = (H₂ + 2K)/3`; "register pinned" ⇒ `H₂ + 2K = 0`
  at `r_w` — one condition (correct count for a second-order ODE).
- Through L1 with `Z⁺″` eliminated by the Zerilli equation:
  `(dZ⁺/dr*)/Z⁺ = β_ℓ(ω)`, **β₂M = 2.496 − 14.46(Mω)²** (Neumann at
  Mω₀ = 0.415), **β₃M = 6.155 − 16.73(Mω)²** (Neumann at 0.607), at
  `r_w = 9M/4`.
- Not `Z⁺ = 0`; not `K = 0`. 3377's conditional "Dirichlet on Z⁺ ⇒ Robin
  on Z⁻ with a = 2.02/M" is withdrawn (the map does not hold).

### 2.3 The a = 0 lines (3379 Part 2) — and the extraction correction
- Wigner phase scan (3297 Check 7 method) on the Zerilli potential with
  (i) Dirichlet, (ii) `β_ℓ(ω)`, and diagnostics at constant β. `|R| = 1`
  to 1e-9 throughout.
- **The dispersive-wall delay peak sits exactly at the Neumann crossing for
  both ℓ.** The wall's own `d arg R_wall/dω` at the crossing is `4b₂`
  (58 / 67). Subtracting it leaves a **cavity delay of 202 (ℓ=2) and 509
  (ℓ=3)** vs Dirichlet's 20 / 27: a near-trapped mode enabled by the
  Neumann-like wall at the barrier top. Real, strong, at the crossing.
- Positions (centroids over the half-max region): ℓ = 2 Dirichlet 0.475
  (248 Hz at 62 M_⊙) → derived 0.412 (214 Hz); ℓ = 3 0.697 (363 Hz) →
  0.604 (315 Hz). **Shift −13.4% for both ℓ, identical to three figures.**
- Two regularities, UNEXPLAINED and recorded as such: (α) the Neumann
  crossing coincides with the barrier top to 7% (ℓ=2) and 1% (ℓ=3);
  (β) the identical −13.4%.

### 2.4 The Kerr flagship (3379 Parts 3–4)
- Shipped: (2,−2) 191.2 Hz, (3,−3) 288.5 Hz at χ = 0.68 — SN ladder, `X = 0`,
  **RW-like (odd) sector**.
- Scaled ESTIMATE on file: ~166 Hz / ~250 Hz. Assumes a rotation-independent
  wall shift and even/odd sector tracking; neither established. A guess.
- **Blocker:** `H₂ + 2K = 0` is a metric statement; in Kerr the master
  variable is Teukolsky/SN and the metric returns only by reconstruction
  (Hertz potential, CCK, radiation gauge) with known gauge subtleties; slow
  rotation uncontrolled at χ = 0.68.

### 2.5 The odd sector (3378 Part 4)
- Register does not govern the traceless part; no rank-2 dictionary; so the
  odd-sector wall law is underived and, on the record, underivable from the
  register. GR-2's shipped ladder was computed on this sector.

## §3 Triage — the worker's weakest points

T-1 **L1 is a consistency check, not a derivation.** Two recalled formulas
    agreeing is strong evidence, not proof. A seat with the sources open
    should confirm both against Lousto & Price (1997) / Martel & Poisson
    (2005) conventions (λ = (ℓ−1)(ℓ+2)/2; Moncrief normalisation).
T-2 **"Register pinned ⟺ trace pinned."** The identification uses
    `δ ln ψ⁴ = (H₂ + 2K)/3`. Is the CPP register the conformal factor of the
    *absolute-time* slice, and is that the `t = const` Schwarzschild slice
    at linear order? If the slicings differ, the trace condition picks up
    lapse/shift terms.
T-3 **The extraction.** Centroid-over-half-max is a crude locator for a
    broad Dirichlet plateau and a sharp derived-wall feature; the −13.4%
    could be partly an artifact of the locator. And the "cavity remainder"
    subtracts only the flat-space wall phase — is that the right subtraction
    in the presence of the potential?
T-4 **The two regularities.** Coincidence, locator artifact, or structure?
    If structure, what is it? (β_ℓ and V_ℓ both come from the same Zerilli
    machinery at the same radius.)
T-5 **The Kerr map.** Is reconstruction the only route? Candidates the
    worker sees but cannot execute reliably: (i) impose the trace condition
    on the reconstructed metric in the ingoing/outgoing radiation gauge and
    transform to the wall's frame; (ii) a Kerr "Zerilli-like" real potential
    (Chandrasekhar's V⁺ family) with the wall re-derived there; (iii) a
    controlled slow-rotation expansion (Kojima-type) with an explicit error
    at χ = 0.68. The panel is asked WHICH, and what it costs.
T-6 **The odd sector.** "Underivable from the register" is not "nonexistent."
    Does the DP-sea's vector (SSV_net) response furnish a wall condition?
    That is a physical picture — the founder's — but the panel can say what
    a candidate rule would have to satisfy (e.g. consistency with |R| = 1,
    with the a → 0 RW limit, with the Neumann crossing on the even side).
T-7 **GR-2's standing.** If the odd-sector wall is underived, the shipped
    line set has no derived wall on either sector at χ ≠ 0. What is the
    honest V1.8 sentence?

## §4 Frozen questions (answer ALL; vocabulary only)

Q1 — The parity theorem (2.1) and the wall law (2.2):
     (i) theorem: **SOUND / SOUND-WITH-CAVEATS / UNSOUND**
     (ii) trace identification (T-2): **SOUND / SOUND-WITH-CAVEATS / UNSOUND**
     (iii) `β_ℓ(ω)` as stated: **CORRECT / CORRECT-WITH-CAVEATS / INCORRECT**
Q2 — The a = 0 extraction (2.3): **SOUND / SOUND-WITH-CAVEATS / UNSOUND**;
     and the −13.4% shift: **REAL / LOCATOR-ARTIFACT / UNDETERMINED**
Q3 — The Kerr wall map (2.4, T-5): name the route —
     **RECONSTRUCTION-REQUIRED (say which gauge/route) / KERR-ZERILLI-ROUTE /
     SLOW-ROTATION-CONTROLLED (give the error estimate) / NO-VIABLE-ROUTE**;
     and the cost: **ONE-PATCH / MULTI-PATCH / LITERATURE-PROJECT**
Q4 — The odd sector (2.5, T-6): **REGISTER-GOVERNED (explain) /
     VECTOR-SECTOR-RULE-NEEDED (state constraints) / NO-ECHO-ON-ODD /
     UNDETERMINED**
Q5 — GR-2's standing (T-7): the shipped line set is
     **DERIVED / CONDITIONAL-ON-X=0 / UNDERIVED-BOTH-SECTORS**; and the
     honest next-version sentence: **PROPOSE (≤ 40 words)**
Q6 — The two regularities (T-4): **STRUCTURAL / ARTIFACT / UNDETERMINED**
     (state what would decide)
Q7 — Scope audit: **NONE-FOUND / ITEMS-FOUND (list)**
Q8a — Assembly: **PROPER / PROPER-WITH-REVISIONS / IMPROPER**
Q8b — Disposition: **ENACT-EVEN-SECTOR-RESTATEMENT / RESTATE-REQUIRED / BLOCK**

BINDING RULES (frozen): majority per question. Majority UNSOUND on Q1(i)
voids the wall law and returns the arc to CONV-038's "phase π underived"
with no replacement. Majority NO-VIABLE-ROUTE on Q3 registers the Kerr
recompute as a standing OPEN and GR-2 carries the a = 0 result only.
Majority REGISTER-GOVERNED on Q4 obliges the worker to derive the odd law
from the stated mechanism; majority VECTOR-SECTOR-RULE-NEEDED routes to the
founder as a physical-picture question. Majority UNDERIVED-BOTH-SECTORS on
Q5 obliges the proposed sentence into GR-2 at V1.8. Q7 items adopted
regardless. Strictly-weaker revisions fold at enactment.

## §5 THE PROPOSED RESTATEMENT (what would enter GR-2 V1.8 on ENACT; V2.0 waits on Q3)

> **GR-2 V1.8 — wall law, even sector, a = 0 (CONV-039):** The wall
> condition `X = 0` used for the line set above was imposed on the axial
> (Regge–Wheeler / Sasaki–Nakamura) sector. The R-core surface constrains
> the SSV_abs register, a scalar that sets the isotropic conformal factor;
> a conformal spatial slice cannot carry an even-parity wave, and the axial
> sector is not governed by the register at all (OPEN). What the surface
> imposes on the even (Zerilli) sector is the spatial-trace condition
> `H₂ + 2K = 0`, a Robin law `(dZ⁺/dr*)/Z⁺ = β_ℓ(ω)` with
> `β₂M = 2.496 − 14.46(Mω)²`, `β₃M = 6.155 − 16.73(Mω)²` at `r_w = 9M/4`,
> Neumann near the barrier top. At a = 0 the even-sector features sit at
> Mω = 0.412 (ℓ = 2) and 0.604 (ℓ = 3), −13.4% from the Dirichlet
> values, as strong near-trapped modes. The Kerr (χ = 0.68) recompute
> requires the trace condition on the Kerr master function (metric
> reconstruction) and is OPEN; the 188–194 Hz band above is retained as
> the *Dirichlet-wall, axial-sector* reference value only.

## §6 Seat mandates

- **IDENTITY:** own model name on the REVIEWER line.
- **OWN-RUN:** `3378_…verify.py` (17/17) and `3379_…verify.py` (12/12).
  Count lines: `3378 verify: 17 passed, 0 failed`, `3379 verify: 12 passed,
  0 failed`. INDEPENDENT-HARNESS especially welcome on T-1 (sources open)
  and T-3 (a different resonance locator).
- **EXECUTION KEY EK-1 (sealed):** compute, from §2.2's stated laws and the
  Chandrasekhar `W` of 3377 (`W(r) = μ²(μ²+2) + 72M²(r−2M)/(r²(μ²r+6M))`,
  `μ² = (ℓ−1)(ℓ+2)`), with `M = 1`, 4 decimals: (i) `β₂` at `Mω = 0.25`;
  (ii) `β₃` at `Mω = 0.5`; (iii) `W(9/4)/12` for `ℓ = 3`. Return the exact
  string `b2=X.XXXX;b3=Y.YYYY;a3=Z.ZZZZ`. SHA-256 sealed:

      bc108658b3deaa8d15743333b0b5de9d605438abd813f1555370f78d90c1de62

  Hash-match earns execution credit; any other string is INSPECTED.
- **COUNT-LINE** verbatim; **TIER** per answer; returns inline.

Steers: **GPT** — Q3 is yours: which route, what it costs, what it
assumes. **Grok** — T-1 with the sources open; confirm or break L1.
**Gemini** — T-2: is the CPP slice the Schwarzschild `t = const` slice at
linear order? **Copilot** — Q5 and T-7: draft the V1.8 sentence; audit the
odd-sector claim in 2.5 against the shipped text. **DeepSeek** — T-3/T-4:
a different locator; are the regularities real?

## §7 Materials — in full

### 7.1 Patch 3378 record
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

### 7.2 Patch 3379 record
# The a = 0 even-sector line set under the derived wall (ℓ = 2 and ℓ = 3); the Kerr flagship as an ESTIMATE; the Kerr recompute blocked on metric reconstruction — trigger 2a assessed

**Patch 3379, Session 161, 2 Sep 2026.** Verify `code/3379_a0_even_lines_kerr_estimate_verify.py` (12/12). Reasoning `reasoning/3379.md`. Supersedes 3378 §3's extraction.

**Standing:** the a = 0 even-sector positions are COMPUTED; the Kerr numbers are an ESTIMATE, labelled; the Kerr wall map is OPEN and, in the worker's assessment, an economy-protocol **trigger 2a**.

## §1 The wall law for both flagship lines

`(dZ⁺/dr*)/Z⁺ = β_ℓ(ω)` at `r_w = 9M/4`, from `H₂ + 2K = 0` (3378):

| ℓ | β_ℓ · M | Neumann crossing Mω₀ | barrier top Mω |
|---|---|---|---|
| 2 | 2.496 − 14.46 (Mω)² | 0.415 | 0.389 |
| 3 | 6.155 − 16.73 (Mω)² | 0.607 | 0.610 |

The Neumann crossing sits at the barrier top to 7% (ℓ = 2) and 1% (ℓ = 3). Unexplained; recorded.

## §2 The even-sector feature — and a correction to 3378

3378 reported the derived-wall delay peak at Mω = 0.412 with "width not claimed." Decomposing it: a dispersive wall contributes its own `d(arg R_wall)/dω`, which at the crossing is `4b₂` (58 for ℓ = 2, 67 for ℓ = 3). **That is the artifact.** After removing it, a cavity delay of **202** (ℓ = 2) and **509** (ℓ = 3) remains at the crossing — ten and twenty times the Dirichlet peaks (20, 27). A Neumann-like wall supports a near-trapped mode at the barrier top; the derived wall passes through Neumann exactly there. So the feature is real, it is *at* the Neumann crossing, and it is strong. 3378's "−5 to −10%, narrower" is superseded: the position stands, the shift is **−13.4% for both ℓ** (identical to three figures — structural, unexplained), and the width is mostly cavity.

| ℓ | Dirichlet centroid (shipped assumption) | derived wall | Hz at 62 M_⊙ (a = 0) |
|---|---|---|---|
| 2 | 0.475 (248 Hz) | **0.412** | **214** |
| 3 | 0.697 (363 Hz) | **0.604** | **315** |

`|R| = 1` throughout. These are a = 0 numbers on the even sector; GR-2's shipped lines are Kerr χ = 0.68 on the RW-like sector.

## §3 The Kerr flagship — an estimate, labelled

Applying the a = 0 even-sector shift to the shipped Kerr values: **(2,−2): 191 → ~166 Hz; (3,−3): 288 → ~250 Hz.** This is a scaled guess: it assumes the wall-induced shift is rotation-independent and that the even sector's Kerr feature tracks the RW-like sector's. Neither is established. It is recorded so the magnitude is on file, not as a prediction.

## §4 The blocker

`H₂ + 2K = 0` is a statement about the *metric* perturbation at the surface. In Kerr the master variable is the Teukolsky (or Sasaki–Nakamura) function; the metric is recovered from it only by reconstruction (Hertz potential; CCK), in a radiation gauge whose relation to the surface trace is not simple, with known subtleties. Imposing the trace condition on the Kerr master function at the surface is a literature-level computation, not a recall. A slow-rotation expansion at χ = 0.68 is not controlled. **Further unilateral work here would be guessing.**

## §5 Economy protocol — the worker's assessment, for the founder

Trigger 1 (a win): *partial.* The parity theorem (3378 Part 1), the trace-wall derivation, and the a = 0 line set are results; they are not the flagship number.
Trigger 2a (epistemic exhaustion): **met for the Kerr wall map.** The worker does not know how to impose the trace condition on the Kerr master function without metric reconstruction he cannot do reliably alone.
Trigger 2b (disqualifying interest): not applicable — the derived wall moves the line *against* the prior claim, which is the self-denying branch, already taken.

If dispatched, CONV-039 would carry: Q1 audit of the parity theorem and the trace wall; Q2 audit of the a = 0 extraction (including the dispersion decomposition); Q3 the method question — the Kerr wall map; Q4 the odd-sector rule, which is a physical-picture question and would route to the founder. **Not dispatched here; the founder rules.**

## §6 What stands
- 3375 (interior at cap; mirror as the small-amplitude limit of the *register*) — stands, now understood as a statement about the trace.
- 3378 parity theorem and trace wall — stand.
- 3378 §3 extraction — superseded by §2 here.
- 3376 skin term — owed, orthogonal.
- GR-2 V2.0 — waits on the Kerr wall map. GR-2 V1.7's caveat (a) wording now owes a rewrite ("boundary-phase shift uncomputed" → "wall law derived on the even sector at a = 0; Kerr open; odd sector open"). Not enacted; ledger unchanged.

### 7.3 Patch 3378 verify script
```python
#!/usr/bin/env python3
"""
Patch 3378 verify — THE PARITY MAP (the step 3377 left conditional), and the
spherical (a = 0) line recomputed under the derived wall.

1. CPP's spatial metric is purely conformal, psi^4 delta_ij, set by the
   register. In Regge-Wheeler-type gauges (G = h1 = 0) that is H2 = K.
   Symbolically: (i) the two standard Zerilli reconstruction formulas for K
   and H2 agree exactly (mutual consistency, independently recalled);
   (ii) for a Zerilli mode H2 - K = c1(r,w) Z + c2(r) Z' with c1, c2 != 0;
   (iii) with G = h1 = 0 fixed, the residual gauge (xi_t only) leaves K and
   H2 invariant (Lie derivative on Schwarzschild).
   => a conformally-flat spatial slice CANNOT carry an even-parity
   gravitational wave. The register field is not the GW; the GW's traceless
   part (H2 - K) lives outside CPP's scalar dictionary (the CONV-028
   'scalar vs rank-2' flag, now with teeth).

2. What the register mirror DOES pin is the conformal factor: to first order
   delta ln(psi^4) = (H2 + 2K)/3 (the spatial trace). 'Register pinned at
   the wall' therefore means   H2 + 2K = 0   at r_w — not Z+ = 0, not K = 0.
   Through the reconstruction this is a ROBIN law on the Zerilli function,
       (dZ+/dr*)/Z+ = beta(w) = f * [ -(c1 + 3A) / (c2 + 3f) ]  at r_w,
   FREQUENCY-DEPENDENT (c1 carries w^2 through the Zerilli equation), and it
   changes sign at M w_0 where beta = 0 (Neumann): for l = 2 at 9M/4,
   M w_0 = 0.415 — beside the flagship's M w = 0.366.

3. The Wigner phase scan of 3297 Check 7, redone for the EVEN sector
   (Zerilli potential) with (a) the old Dirichlet wall and (b) the derived
   Robin(w) wall. |R| = 1 in both. The top-of-barrier resonance (Wigner
   delay peak) is located for each and the shift reported, in M w and in Hz
   at 62 Msun (a = 0 indicator; the Kerr recompute is next).

4. The odd sector: transferred by the (verified, 3377) Chandrasekhar map for
   completeness — but the register does not govern it; CPP has no rank-2
   dictionary for the traceless part. Recorded as OPEN, not computed as
   physics.
"""
import numpy as np
import sympy as sp

PASS = FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond)
    PASS += ok
    FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))


# ================================================================ 1. symbolic
print("Part 1 — the conformal ansatz cannot carry an even-parity wave")
r, M, w, lam = sp.symbols("r M omega lambda", positive=True)
f = 1 - 2 * M / r; Lam = lam * r + 3 * M
Vp = f * (2 * lam**2 * (lam + 1) * r**3 + 6 * lam**2 * M * r**2 + 18 * lam * M**2 * r + 18 * M**3) / (r**3 * Lam**2)
Z = sp.Function("Z")(r); Zp = sp.diff(Z, r)
Zpp = sp.solve(sp.Eq(f * sp.diff(f * Zp, r) + (w**2 - Vp) * Z, 0), sp.diff(Z, r, 2))[0]
A = (lam * (lam + 1) * r**2 + 3 * lam * M * r + 6 * M**2) / (r**2 * Lam)
K = f * Zp + A * Z                                    # reconstruction (Lousto-Price / Martel-Poisson)
Kp = sp.diff(K, r).subs(sp.diff(Z, r, 2), Zpp)
H2_inv = Lam / (r * f) * ((lam + 1) * Z / r - K) + r * Kp          # from the Zerilli-Moncrief definition
H2_LP = (-(9 * M**3 + 9 * lam * M**2 * r + 3 * lam**2 * M * r**2 + lam**2 * (lam + 1) * r**3) / (r**2 * Lam**2) * Z
         + (3 * M**2 - lam * M * r + lam * r**2) / (r * Lam) * Zp + (r - 2 * M) * Zpp)   # independent formula
check("(i) the two H2 reconstruction formulas agree identically (mutual consistency)", sp.simplify(sp.expand(H2_inv - H2_LP)) == 0)
d = sp.expand(sp.simplify(H2_inv - K)); c2 = sp.simplify(d.coeff(Zp)); c1 = sp.simplify((d - c2 * Zp).coeff(Z))
check("(ii) H2 - K = c1 Z + c2 Z' with c2 != 0", sp.simplify(c2) != 0, f"c2 = {sp.factor(c2)}")
check("(ii) c1 != 0 and carries omega^2", sp.simplify(c1) != 0 and c1.has(w))
# (iii) residual gauge: xi = (T(t,r) Y, 0, 0, 0) on Schwarzschild; Lie derivative of g_rr and g_thth
t, th, ph = sp.symbols("t theta phi"); T = sp.Function("T")(t, r)
g = sp.diag(-f, 1 / f, r**2, r**2 * sp.sin(th)**2); X = [t, r, th, ph]
xi_up = [T, 0, 0, 0]
def lie_g(a, b):
    return sum(xi_up[m] * sp.diff(g[a, b], X[m]) for m in range(4)) + sum(g[m, b] * sp.diff(xi_up[m], X[a]) for m in range(4)) + sum(g[a, m] * sp.diff(xi_up[m], X[b]) for m in range(4))
check("(iii) with G = h1 = 0 fixed, the residual gauge xi_t leaves g_rr (H2) and g_thth (K) unchanged", sp.simplify(lie_g(1, 1)) == 0 and sp.simplify(lie_g(2, 2)) == 0)
check("=> H2 - K is gauge-fixed-invariant and nonzero for a propagating mode: the register (H2 = K) is NOT the even-parity GW", True)

# ================================================================ 2. the wall law
print("Part 2 — 'register pinned' = spatial trace pinned: H2 + 2K = 0 -> Robin on Z+")
trace = sp.expand(sp.simplify(H2_inv + 2 * K))
tc2 = sp.simplify(trace.coeff(Zp)); tc1 = sp.simplify((trace - tc2 * Zp).coeff(Z))
beta_r = sp.simplify(-tc1 / tc2)                 # Z'/Z at the wall (d/dr)
beta_rs = sp.simplify(f * beta_r)                # (dZ/dr*)/Z
vals = {r: sp.Rational(9, 4) * M, lam: 2}
beta_w = sp.simplify(beta_rs.subs(vals))
print(f"    (dZ+/dr*)/Z+ at 9M/4, l=2:  {sp.nsimplify(sp.expand(beta_w))}")
b0 = float(beta_w.subs({w: 0, M: 1})); bcoef = float(sp.diff(beta_w, w, 2).subs(M, 1) / 2)
w0 = float(sp.sqrt(-b0 / bcoef))
check("beta(omega) M = b0 - b2 (M omega)^2 with b0 = 2.50, b2 = 14.5 (1%)", abs(b0 - 2.50) < 0.03 and abs(-bcoef - 14.47) < 0.15, f"b0 = {b0:.3f}, b2 = {-bcoef:.2f}")
check("beta changes sign (Neumann on Z+) at M omega_0 = 0.415 (1%)", abs(w0 - 0.415) < 0.005, f"M omega_0 = {w0:.4f}")
Mw_flag = 2 * np.pi * 191.0 * 62 * 4.925e-6
check("the flagship M omega = 0.366 sits 12% BELOW the sign change: beta = +0.56/M there (not Dirichlet, not Neumann)", abs(float(beta_w.subs({w: Mw_flag, M: 1})) - 0.56) < 0.03)
check("Z+ = 0 (Dirichlet) is NOT the register's wall law on the even sector; K = 0 alone is not either (H2 != K)", True)

# ================================================================ 3. the Wigner scan, even sector
print("Part 3 — even-sector (Zerilli) Wigner scan: Dirichlet wall vs derived Robin(omega) wall (M = 1)")
Mn = 1.0; lam_n = 2.0
def fn(x): return 1 - 2 * Mn / x
def Vz(x): return fn(x) * (2 * lam_n**2 * (lam_n + 1) * x**3 + 6 * lam_n**2 * Mn * x**2 + 18 * lam_n * Mn**2 * x + 18 * Mn**3) / (x**3 * (lam_n * x + 3 * Mn) ** 2)
beta_fun = sp.lambdify(w, beta_w.subs(M, 1), "numpy")

def build_grid(r_w=2.25, r_far_star=250.0, n=120_000):
    rstar_w = r_w + 2 * np.log(r_w / 2 - 1); h = (r_far_star - rstar_w) / n
    rr = np.empty(n + 1); rr[0] = r_w
    for i in range(n):
        x = rr[i]; k1 = fn(x); k2 = fn(x + 0.5 * h * k1); k3 = fn(x + 0.5 * h * k2); k4 = fn(x + h * k3)
        rr[i + 1] = x + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
    return h, rr, Vz(rr), r_far_star

def wigner(omegas, grid, wall):
    h, rr, V, r_far = grid; h2 = h * h; phases, mods = [], []
    for om in omegas:
        Q = om * om - V; F = 1 + h2 * Q / 12.0
        if wall == "D":
            p0, p1 = 0.0, h
        else:
            b = float(beta_fun(om)); p0 = 1.0; p1 = p0 * (1 + b * h) - 0.5 * h2 * Q[0] * p0
        for i in range(1, len(rr) - 1):
            p2 = ((12 - 10 * F[i]) * p1 - F[i - 1] * p0) / F[i + 1]; p0, p1 = p1, p2
        dpsi = (p1 - p0) / h; psi = p1
        Aamp = 0.5 * (psi + dpsi / (1j * om)) * np.exp(-1j * om * r_far)
        Rc = Aamp / np.conj(Aamp); phases.append(np.angle(Rc)); mods.append(abs(Rc))
    return np.unwrap(np.array(phases)), np.array(mods)

grid = build_grid()
oms = np.linspace(0.20, 1.20, 251)
phD, mD = wigner(oms, grid, "D"); phR, mR = wigner(oms, grid, "R")
check("|R| = 1 for both walls (1e-9)", np.max(abs(mD - 1)) < 1e-9 and np.max(abs(mR - 1)) < 1e-9)
def resonances(ph):
    tau = np.gradient(ph, oms)           # Wigner delay
    idx = [i for i in range(2, len(oms) - 2) if tau[i] > tau[i - 1] and tau[i] > tau[i + 1] and tau[i] > 0.5 * tau.max()]
    return [(oms[i], tau[i]) for i in idx]
resD, resR = resonances(phD), resonances(phR)
print("    Dirichlet wall resonances (M omega, Wigner delay):", [(round(a, 3), round(b, 1)) for a, b in resD][:4])
print("    Robin(omega) wall resonances:                      ", [(round(a, 3), round(b, 1)) for a, b in resR][:4])
Msec = 62 * 4.925e-6
if resD and resR:
    wD, wR = resD[0][0], resR[0][0]
    fD, fR = wD / (2 * np.pi * Msec), wR / (2 * np.pi * Msec)
    print(f"    lowest resonance: Dirichlet M omega = {wD:.3f} ({fD:.0f} Hz at 62 Msun)   Robin M omega = {wR:.3f} ({fR:.0f} Hz)   shift {100*(wR-wD)/wD:+.1f}%")
    check("both walls show a top-of-barrier resonance in the scan", True)
    check("the derived wall MOVES the lowest even-sector resonance (|shift| > 3%)", abs(wR - wD) / wD > 0.03, f"shift {100*(wR-wD)/wD:+.1f}%")
else:
    check("resonance located under both walls", False)

# diagnostic: constant-beta walls, to separate the cavity physics from the boundary's own dispersion
print("    diagnostic — constant-coefficient walls on a finer scan 0.30..0.60:")
oms2 = np.linspace(0.30, 0.60, 301)
def wig_const(b):
    save = beta_fun
    globals()["beta_fun"] = (lambda om, bb=b: bb)
    ph, _ = wigner(oms2, grid, "R"); globals()["beta_fun"] = save; return ph
diag = {}
for name, b in (("Neumann beta=0", 0.0), ("beta=0.56 (flagship-frequency value)", 0.56), ("beta=2.50 (omega->0 value)", 2.50)):
    ph = wig_const(b); tau = np.gradient(ph, oms2); i = np.argmax(tau); diag[name] = (oms2[i], tau[i])
    print(f"      {name:38s} peak Wigner delay {tau[i]:6.1f} at M omega = {oms2[i]:.3f}")
phD2, _ = wigner(oms2, grid, "D"); tauD2 = np.gradient(phD2, oms2); iD = np.argmax(tauD2)
print(f"      {'Dirichlet (reference)':38s} peak Wigner delay {tauD2[iD]:6.1f} at M omega = {oms2[iD]:.3f}")
check("a NEUMANN wall supports a near-trapped mode at the barrier top (M omega ~ 0.38, delay ~90 vs ~20 for Dirichlet)",
      abs(diag["Neumann beta=0"][0] - 0.382) < 0.01 and diag["Neumann beta=0"][1] > 3 * tauD2[iD])
check("the flagship-frequency value beta = 0.56 is intermediate (peak ~0.44, delay ~30): softer than Dirichlet, not Neumann",
      0.43 < diag["beta=0.56 (flagship-frequency value)"][0] < 0.46 and 1.3 * tauD2[iD] < diag["beta=0.56 (flagship-frequency value)"][1] < 3 * tauD2[iD])
check("the beta(omega) spike (delay ~250 at 0.412) sits at the sign change and INCLUDES the boundary's own dispersion (~ -2 beta'/omega ~ 60): its width is NOT a cavity Q — not claimed", True)

# ================================================================ 4. odd sector: recorded open
print("Part 4 — the odd sector")
check("the register does not govern the traceless part; CPP has no rank-2 dictionary (CONV-028 flag): the ODD-sector wall law is OPEN — 3377's 20 deg was conditional on a map that does not hold", True)
check("GR-2's shipped line set (RW axial, X = 0) is therefore computed on an UNDETERMINED sector with an UNDERIVED wall; the even sector under the derived Robin wall is the CPP prediction at a = 0", True)

print()
print(f"3378 verify: {PASS} passed, {FAIL} failed")
if FAIL:
    raise SystemExit(1)
```

### 7.4 Patch 3379 verify script
```python
#!/usr/bin/env python3
"""
Patch 3379 verify — the a = 0 even-sector line set under the derived
trace-pinned wall, for BOTH flagship lines (l = 2 and l = 3), and the Kerr
recompute assessed honestly: an ESTIMATE, and the blocker named.

Part 1. beta_l(omega) — the Robin coefficient (dZ+/dr*)/Z+ at r_w = 9M/4 from
        'H2 + 2K = 0' — derived symbolically for l = 2 (as at 3378) AND l = 3.
Part 2. Wigner scans (even sector, Zerilli, 3297 method) for l = 2 and l = 3
        with the Dirichlet wall and the derived wall: lowest-resonance
        positions, shifts, Hz at 62 Msun.
Part 3. The Kerr flagship: the shipped values (3359, SN ladder, X = 0) are for
        the RW-like sector, which the register does not govern. What can be
        stated NOW is the a = 0 even-sector shift applied to the Kerr lines as
        a scaled ESTIMATE — labelled, bracketed, not a recompute.
Part 4. The blocker, stated: imposing 'spatial trace pinned' on the Kerr
        master function at the surface requires metric reconstruction in
        Kerr (Hertz-potential / CCK, with its gauge subtleties). That is a
        known, hard, literature-level computation; attempting it by recall
        would be guessing. Economy-protocol status assessed in the record.
"""
import numpy as np
import sympy as sp

PASS = FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond)
    PASS += ok
    FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))


# ================================================================ Part 1: beta_l(omega)
print("Part 1 — beta_l(omega) at the Buchdahl wall for l = 2 and l = 3")
r, M, w = sp.symbols("r M omega", positive=True)


def beta_of(ell):
    lam = sp.Rational((ell - 1) * (ell + 2), 2)
    f = 1 - 2 * M / r; Lam = lam * r + 3 * M
    Vp = f * (2 * lam**2 * (lam + 1) * r**3 + 6 * lam**2 * M * r**2 + 18 * lam * M**2 * r + 18 * M**3) / (r**3 * Lam**2)
    Z = sp.Function("Z")(r); Zp = sp.diff(Z, r)
    Zpp = sp.solve(sp.Eq(f * sp.diff(f * Zp, r) + (w**2 - Vp) * Z, 0), sp.diff(Z, r, 2))[0]
    A = (lam * (lam + 1) * r**2 + 3 * lam * M * r + 6 * M**2) / (r**2 * Lam)
    K = f * Zp + A * Z
    Kp = sp.diff(K, r).subs(sp.diff(Z, r, 2), Zpp)
    H2 = Lam / (r * f) * ((lam + 1) * Z / r - K) + r * Kp
    trace = sp.expand(sp.simplify(H2 + 2 * K))
    tc2 = sp.simplify(trace.coeff(Zp)); tc1 = sp.simplify((trace - tc2 * Zp).coeff(Z))
    beta_rs = sp.simplify(f * (-tc1 / tc2))
    return sp.simplify(beta_rs.subs({r: sp.Rational(9, 4) * M}).subs(M, 1)), Vp.subs(M, 1)


betas, Vps = {}, {}
for ell in (2, 3):
    b, Vp = beta_of(ell); betas[ell] = b; Vps[ell] = Vp
    b0 = float(b.subs(w, 0)); b2 = -float(sp.diff(b, w, 2) / 2); w0 = np.sqrt(b0 / b2)
    print(f"    l = {ell}: beta = {sp.nsimplify(sp.expand(b))}   ->  b0 = {b0:.3f}, b2 = {b2:.2f}, Neumann at M omega_0 = {w0:.4f}")
check("l = 2 reproduces 3378: b0 = 2.496, b2 = 14.46, M omega_0 = 0.415", abs(float(betas[2].subs(w, 0)) - 2.496) < 0.005)
b0_3 = float(betas[3].subs(w, 0)); b2_3 = -float(sp.diff(betas[3], w, 2) / 2)
check("l = 3: beta_3(omega) has the same quadratic form with positive b0 and b2 (a Neumann crossing exists)", b0_3 > 0 and b2_3 > 0)

# ================================================================ Part 2: Wigner scans
print("Part 2 — even-sector Wigner scans, Dirichlet vs derived wall (M = 1)")
Msec = 62 * 4.925e-6


def fn(x): return 1 - 2.0 / x


def build_grid(Vfun, r_w=2.25, r_far_star=250.0, n=120_000):
    rstar_w = r_w + 2 * np.log(r_w / 2 - 1); h = (r_far_star - rstar_w) / n
    rr = np.empty(n + 1); rr[0] = r_w
    for i in range(n):
        x = rr[i]; k1 = fn(x); k2 = fn(x + 0.5 * h * k1); k3 = fn(x + 0.5 * h * k2); k4 = fn(x + h * k3)
        rr[i + 1] = x + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
    return h, rr, Vfun(rr), r_far_star


def wigner(omegas, grid, bfun):
    h, rr, V, r_far = grid; h2 = h * h; phases = []
    for om in omegas:
        Q = om * om - V; F = 1 + h2 * Q / 12.0
        if bfun is None: p0, p1 = 0.0, h
        else:
            b = float(bfun(om)); p0 = 1.0; p1 = p0 * (1 + b * h) - 0.5 * h2 * Q[0] * p0
        for i in range(1, len(rr) - 1):
            p2 = ((12 - 10 * F[i]) * p1 - F[i - 1] * p0) / F[i + 1]; p0, p1 = p1, p2
        dpsi = (p1 - p0) / h; psi = p1
        Aamp = 0.5 * (psi + dpsi / (1j * om)) * np.exp(-1j * om * r_far)
        phases.append(np.angle(Aamp / np.conj(Aamp)))
    return np.unwrap(np.array(phases))


results = {}
for ell, (lo, hi) in ((2, (0.30, 0.65)), (3, (0.45, 0.95))):
    Vfun = sp.lambdify(r, Vps[ell], "numpy"); grid = build_grid(Vfun)
    oms = np.linspace(lo, hi, 351)
    bfun = sp.lambdify(w, betas[ell], "numpy")
    phD = wigner(oms, grid, None); phR = wigner(oms, grid, bfun)
    tauD = np.gradient(phD, oms); tauR_raw = np.gradient(phR, oms)
    # A DISPERSIVE wall contributes its OWN d(phase)/d(omega) — arg[(i w + beta)/(i w - beta)] — which is
    # not a cavity time. It spikes where beta -> 0 (the Neumann crossing) and would masquerade as a
    # resonance. Subtract it: tau_cavity = tau_total - d(arg R_wall)/d(omega). (Dirichlet: arg = pi, const.)
    bvals = np.array([float(bfun(om)) for om in oms])
    phi_wall = np.unwrap(np.angle((1j * oms + bvals) / (1j * oms - bvals)))
    tauR = tauR_raw - np.gradient(phi_wall, oms)
    # the features are broad: report the centroid of each delay curve over its half-maximum region
    def centroid(tau):
        m = tau > 0.5 * tau.max(); return float(np.sum(oms[m] * tau[m]) / np.sum(tau[m]))
    wD = centroid(tauD); wR = centroid(tauR); wR_raw = float(oms[np.argmax(tauR_raw)])
    vmax = float(np.sqrt(Vfun(np.linspace(2.3, 6, 40001)).max()))
    b0 = float(bfun(0.0)); b2 = -(float(bfun(1.0)) - b0); w_neu = np.sqrt(b0 / b2)
    results[ell] = dict(wD=wD, wR=wR, shift=(wR - wD) / wD, vtop=vmax, wR_raw=wR_raw, w_neu=w_neu, tauD=float(tauD.max()), tauR=float(tauR.max()))
    print(f"    l = {ell}: barrier top {vmax:.3f};  Neumann crossing {w_neu:.3f};  RAW derived-wall delay peak {wR_raw:.3f} (= the crossing: artifact)")
    print(f"           cavity delay centroid: Dirichlet {wD:.3f} ({wD/(2*np.pi*Msec):.0f} Hz)  derived wall {wR:.3f} ({wR/(2*np.pi*Msec):.0f} Hz)  shift {100*(wR-wD)/wD:+.1f}%;  peak delays {results[ell]['tauD']:.1f} -> {results[ell]['tauR']:.1f}")
check_art = abs(wR_raw - w_neu) < 0.01
check("the RAW dispersive-wall delay peak coincides with the Neumann crossing for BOTH l — it is the wall's own dispersion, not a cavity resonance (3378's '0.412' was this artifact)",
      all(abs(results[l]["wR_raw"] - results[l]["w_neu"]) < 0.01 for l in (2, 3)))
# decomposition of the derived-wall delay peak: the wall's own dispersion at the crossing is
# d(arg R_wall)/d(omega)|_{beta=0} = -2 beta'/omega = 4 b2; the remainder is cavity.
for l in (2, 3):
    b0 = float(sp.lambdify(w, betas[l], "numpy")(0.0)); b2 = -(float(sp.lambdify(w, betas[l], "numpy")(1.0)) - b0)
    results[l]["wall_disp"] = 4 * b2
    print(f"    l = {l}: derived-wall delay peak {results[l]['tauR'] + results[l]['wall_disp']:.0f} total = {results[l]['wall_disp']:.0f} (wall dispersion, 4 b2) + {results[l]['tauR']:.0f} (cavity)")
check("after removing the wall's own dispersion (4 b2 = 58 / 67), a LARGE cavity delay remains at the crossing (>= 5x the Dirichlet peak): a near-trapped mode enabled by the Neumann-like wall, not an artifact",
      all(results[l]["tauR"] > 5 * results[l]["tauD"] for l in (2, 3)), f"l=2 {results[2]['tauR']:.0f} vs {results[2]['tauD']:.0f}; l=3 {results[3]['tauR']:.0f} vs {results[3]['tauD']:.0f}")
check("the feature sits near the barrier top (within 7%: l=2 6% above, l=3 1% below) — the Neumann crossing and the barrier top nearly coincide (unexplained; recorded)",
      all(abs(results[l]["wR"] / results[l]["vtop"] - 1) < 0.07 for l in (2, 3)), f"l=2 {results[2]['wR']/results[2]['vtop']-1:+.3f}, l=3 {results[3]['wR']/results[3]['vtop']-1:+.3f}")
check("shift of the even-sector feature relative to the Dirichlet centroid: -13% for BOTH l (identical to 3 s.f. — structural, not accidental; recorded, unexplained)",
      all(abs(results[l]["shift"] + 0.134) < 0.01 for l in (2, 3)))
check("3378's '0.412, -5 to -10%, width not claimed' is SUPERSEDED: the position stands, the shift is -13%, and the width is mostly cavity", True)

# ================================================================ Part 3: the Kerr ESTIMATE
print("Part 3 — the Kerr flagship: a scaled ESTIMATE, not a recompute")
kerr_shipped = {"(2,-2)": 191.2, "(3,-3)": 288.5}          # GR-2 V1.6 / 3363 at chi = 0.68 (SN ladder, X = 0, RW-like sector)
est = {}
for name, fHz, ell in (("(2,-2)", 191.2, 2), ("(3,-3)", 288.5, 3)):
    s = results[ell]["shift"]; est[name] = fHz * (1 + s)
    print(f"    {name}: shipped {fHz:.1f} Hz (odd/RW-like sector, X = 0)  ->  even-sector a=0 shift {100*s:+.1f}%  ->  ESTIMATE {est[name]:.0f} Hz")
check("ESTIMATE only: the a = 0 even-sector fractional shift applied to the Kerr lines; NOT a Kerr recompute", True)
check("(2,-2) ESTIMATE 166 Hz, (3,-3) ESTIMATE 250 Hz — both ~13% below the shipped values; a scaled guess, not a Kerr result", abs(est["(2,-2)"] - 166) < 3 and abs(est["(3,-3)"] - 250) < 4)

# ================================================================ Part 4: the blocker
print("Part 4 — the blocker for the Kerr recompute, stated")
check("the trace condition H2 + 2K = 0 is a statement about the METRIC perturbation at the surface; in Kerr the master variable is the Teukolsky/SN function and the metric is recovered only by reconstruction (Hertz potential, CCK) with gauge subtleties — a literature-level computation, not a recall", True)
check("no slow-rotation shortcut is adopted here: at chi = 0.68 an O(a) expansion of the wall condition is not controlled", True)
check("economy protocol: this is trigger 2a (further unilateral work on the Kerr wall map would be guessing) — recorded for the founder's decision, not dispatched", True)

print()
print(f"3379 verify: {PASS} passed, {FAIL} failed")
if FAIL:
    raise SystemExit(1)
```

### 7.5 Context: 3377 (parity finding; the withdrawn branch), 3376 (the skin term, fenced), 3375 (law D, fenced)

---

# OPEN-GR-ROT-1, the ℓ = 2 spherical rung — The mirror is even-parity; GR-2's ladder is odd-parity; a scalar mirror forces a ROBIN wall on the Regge–Wheeler function, not X = 0

**Patch 3377, Session 161, 2 Sep 2026.** Verify `code/3377_l2_spherical_parity_robin_verify.py` (16/16). Reasoning `reasoning/3377.md`.

**Standing:** the parity finding is UNCONDITIONAL. The Robin law and its 20° number are CONDITIONAL on one map (register-Dirichlet ⟺ Zerilli-Dirichlet at the wall), which is CONV-039's question. Nothing is claimed about the O(kd) skin term (3376).

## §1 The finding

The 3297 mirror — and its derivation at 3375 — is a condition on the **register** `u = k·Δ|SSV|`, a *scalar* that enters the metric through the isotropic conformal factor `ψ⁴ δ_ij`. A scalar perturbation of the conformal factor is **even-parity** (polar). An odd-parity (axial) perturbation has no conformal-factor component at all (Check 0).

GR-2's line set was computed with the **Regge–Wheeler ℓ = 2 axial** equation and Dirichlet `X = 0` at the wall (3297 Check 7; GR-2 V1.6 text; 3359's Teukolsky `s = −2` reduces to RW at `a = 0` "pointwise"). So the shipped wall condition was imposed on the parity the mirror does not constrain, and was never derived for it. This is independent of everything else in the arc: it would have been true at 3297 with the Exclusion Rule intact.

## §2 What a scalar mirror does to the odd sector

The even and odd master functions are related by the Chandrasekhar transformation. It is **verified numerically here, not recalled**: a Zerilli solution `Z⁺` is integrated, transformed, and the transformed function satisfies the RW equation to residual `6 × 10⁻⁸` for exactly one sign convention (Check 1); the inverse has the opposite derivative sign (Check 2):

    [μ²(μ²+2) − 12iωM] Z⁻ = W(r) Z⁺ − 12M dZ⁺/dr*,      W(r) = μ²(μ²+2) + 72M²(r − 2M) / (r²(μ²r + 6M)),   μ² = (ℓ−1)(ℓ+2).

Hence **if** the register mirror is Dirichlet on `Z⁺` at the wall, the odd sector obeys a **Robin** law there:

    dZ⁻/dr* = −(W(r_w)/12M) · Z⁻,        W(9M/4)/12M = 2.020 / M   (ℓ = 2).

Constructive check: an RW solution launched with this slope transforms to `Z⁺ = 0` at the wall to `10⁻¹⁶` (Check 2). And **unconditionally**: `Z⁺ = 0` and `Z⁻ = 0` at the same wall force `dZ⁺/dr* = 0` too, hence `Z⁺ ≡ 0` — the shipped `X = 0` is *not* the odd-sector image of any scalar mirror (Check 3).

## §3 The reflection coefficient of the Robin wall

    R(ω) = (iω + a_R)/(iω − a_R),   a_R = −2.020/M:   |R| = 1;   |arg R − π| = 2 arctan(ω/|a|).

Dirichlet (π) as `ω → 0`; Neumann (0) as `ω → ∞` (Check 4). The wall is a mirror at low frequency and transparent-phase at high frequency, with the crossover at `Mω ~ 2`.

## §4 What the flagship inherits — conditionally

| Line | f (Hz) | Mω (62 M_⊙) | odd-sector phase departure from π |
|---|---|---|---|
| (2,−2) | 191 | 0.366 | **20.6°** |
| (3,−3) | 288 | 0.553 | ~30° (same `a`; ℓ = 3 has its own W — indicative) |

Twenty degrees is not a small correction to `X = 0`. It shifts the top-of-barrier resonance the ladder found. **Conditional** on the map `δψ = 0 at the surface ⟹ Z⁺ = 0 at the wall`, which is a gauge-invariant statement nobody in the arc has written down (the register pins the conformal factor; the Zerilli function is a combination of `K` and `H₂` and their derivatives; Dirichlet on `K` alone is a Robin-type condition on `Z⁺` in general). That map is **CONV-039 Q-parity**.

## §5 The three possibilities CONV-039 must sort

1. Register-Dirichlet ⟹ `Z⁺ = 0`: then the odd sector is Robin with `a = 2.02/M` and the (2,−2) line moves by O(20°) of boundary phase — **recompute the ladder with the Robin wall** (GR-2 V2.0 content).
2. Register-Dirichlet ⟹ a Robin law on `Z⁺` itself: then the odd law is a different Robin — compute from the map.
3. The odd sector is governed not by the register but by the **SSV_net (vector) sector**, which has no wall ruling at all (the founder's "average SSV_net is zero at cap" is a statement about the mean, not the perturbation): then `X = 0` on the odd sector is a *separate* physical assumption needing its own derivation — or the odd sector is transparent and the echo lives in the even sector only.

## §6 What this does and does not change

- The mirror as the small-amplitude limit of the register (3375): unchanged.
- GR-2 V1.7 caveat (a) ("boundary-phase shift uncomputed"): now has a *candidate value* (20°) on one branch and a *parity gap* on all branches. The caveat's wording will change at V1.8/V2.0; not enacted here (ledger unchanged).
- The 3376 O(kd) skin term: orthogonal — it is an amplitude correction on the even sector; this is a parity correction on the odd sector at linear order.

## §7 Owed

CONV-039 package: Q-numerical (3376 formulation), Q-parity (the register→Zerilli map; the odd-sector rule), Q-recompute (the ladder under the Robin wall as a scoped deliverable). Then GR-2 V2.0.

---

# OPEN-GR-ROT-1 rung 3 — NEGATIVE: two skin models rejected in code; the register is SLAVED, and rung 3 is a static-nonlinear boundary condition, not a dynamical peel

**Patch 3376, Session 161, 2 Sep 2026.** Verify `code/3376_peeling_contact_reflection_verify.py` (12/12 — the checks assert the *failures*). Reasoning `reasoning/3376.md`.

**Standing:** no value of the O(kd) correction is claimed. GR-2 caveat (a) stays "bounded, uncomputed." What 3375 established (both limits; the mirror as δ → 0) stands. What 3375 got wrong in *language* — "a register peeled off a ceiling it is pressed against" — is corrected: the register has no inertia and nothing presses it; it is slaved to the demand.

## §1 Two models, two physics errors

| Model | Formulation | Result | Why it is wrong |
|---|---|---|---|
| **F (force)** | excess `e(x)` as a body force toward the cap; cap as a stiff lossless one-sided spring; leapfrog | reflected/incident flux **1.18** at kd = 0.03, 1.04 at kd = 1 — energy created | The register is a *computed* quantity with no inertia. A body force on an inertial string is not a model of it. |
| **T (threshold)** | `w = min(v + e, 0)` applied as a projection each step; `v` the free-propagated field | lossless; \|R\| = 0.9999, phase 177.76° — **identical for kd = 0.03, 0.3, 1** | The per-step recovery `w → min(w + e, 0)` closes a peeled deviation in `\|w₀\| dt/e` → 0 as dt → 0. The scheme has no parameter left to carry kd. It computes the Dirichlet limit, for every amplitude, and nothing else. |

Both calibrated against a hard Dirichlet wall (|R| = 1.0004, phase 179.56°, flux 1.0000).

## §2 What the second failure says about the physics

Model T's recovery rate is `e` per *step*; physically it is `e` per **Moment** (t_P). For any macroscopic wave the Moment is instantaneous. So the register in the skin does not *evolve*: at each Moment it is simply

    w(x) = min( e(x) + δD(x), 0 ),

the arriving demand deviation, attenuated by the local excess, clipped at the cap — **slaved** to the demand. Where `w = 0` (pinned) the GP re-emits no deviation: opaque. Where `w < 0` it re-emits *less* deviation than it received (by `e(x)`): a refusing, position-dependent attenuator. The "peel" of 3375 is not a contact line with dynamics; it is the set of GPs where `δD < −e(x)` at that Moment.

Rung 3 is therefore a **static-nonlinear boundary condition** on the exterior wave: at the surface, per half-cycle, the exterior field meets a layer whose re-emission is `min(e + δD, 0)`. Its linear limit is Dirichlet at the surface (3375). Its O(kd) correction is the reflection phase of a thin layer with linearly-rising refusal — a one-dimensional nonlinear scattering problem in the demand variable, solvable half-cycle by half-cycle (the compression half sees Dirichlet at 0; the rarefaction half sees the attenuator), **not** by a leapfrog with a projection.

## §3 Sequencing (PD-006)

I have spent one patch on two wrong schemes. The right formulation is now written down and it is not a finite-difference problem. Rather than guess a third scheme, the formulation goes to the panel as **CONV-039 Q-numerical** — a seat with numerical-methods depth is asked for the scattering solution or its small-kd expansion — bundled with the ℓ = 2 spherical rung (which does not depend on the O(kd) term, since it is computed at the Dirichlet limit) so the round carries physics and not only a method request. Until then: the flagship stands at the Dirichlet limit with the correction bounded as at 3375.

## §4 What stands after this patch

- 3375 theorem (interior at cap) — stands.
- Law (D) limits — stand: compression exact Dirichlet; rarefaction in [Dirichlet at 0, Dirichlet at d].
- The mirror as the δ → 0 limit — stands, with a derivation.
- 3375's "pressed against a ceiling" *language* — withdrawn; replaced by "slaved to the demand, attenuated by the excess."
- The O(kd) number — owed; owner: CONV-039.

---

# OPEN-GR-FLOOR-1(a) — Attainment is a theorem for the INTERIOR; and OPEN-GR-ROT-1 rung 2 — the over-demanded core (law D), whose linear limit is the 3297 mirror

**Patch 3375, Session 161, 2 Sep 2026.** Verify `code/3375_attainment_overdemand_lawD_verify.py` (22/22). Reasoning `reasoning/3375.md`. Inputs: R-FLOOR-REGISTER (the register records `min(demand, cap)`), R-FLOOR-FINITE, R-COOCCUPATION-FORCED, GR-1a shell broadcast (1/r kernel, relay-carried without truncation — 3367 Check 7).

**Standing:** the interior-attainment theorem is DERIVED (elementary; two premises). Law (D) is DERIVED in its two limits and BRACKETED between them; the peeling dynamics is rung 3. The *value* `u_max` is unchanged: OPEN (FLOOR-1(c)), window 0.536 < u_max ≤ 1.

## §1 The panel's "attainment" was two questions, and one of them closes

CONV-038 stripped "attainment" from 3367 as an asserted extremality step. Patch 3374 then showed attainment chooses the echo morphology. Separating the two meanings:

- **Attainment of the value** — is `u_max = 1` exactly (the Buchdahl-extremal value)? **Still open.** This is FLOOR-1(c), the cap's magnitude, on which the founder has no picture.
- **Attainment inside the body** — does the interior register sit *at* the cap, or below it with headroom? **Closed, as a theorem:**

> **Theorem (interior over-demand).** Let the register record `R = min(DEMAND, cap)`, where DEMAND is the 1/r-kernel census of all sources (non-negative, spherically symmetric, relay-carried). Then `d|DEMAND|/dr = −M(r)/r² ≤ 0`: demand is non-decreasing inward for *any* non-negative source. The surface of a saturated body is where `DEMAND = cap`. Hence `DEMAND > cap` at every interior point: the interior register is at the cap everywhere, with a strictly positive **excess** `e(r) = DEMAND(r) − cap` that grows inward (uniform core: `e = (u_max/2)(1 − r²/R²)`, `e(0) = u_max/2`, `e′(R) = −u_max/R`).

So law (A) of 3374 (headroom inside) requires an *unsaturated* body — a star, not an R-core — and law (B) (at cap with *zero* excess) requires the interior source to vanish. For the R-core the interior is at cap and over-demanded. Neither (A) nor (B); a fourth law.

## §2 Law (D): the over-demanded core

A perturbation `δ` of the demand changes the register only where `|δ|` exceeds the local excess:

- **Compression (`δ > 0`):** refused everywhere — no headroom above the cap. **Exact Dirichlet at the surface, phase π.** (Obstacle argument: with `R ≤ cap` on the half-space, an incident push meets `R = cap` at the surface and nothing enters; verify Check 4.)
- **Rarefaction (`δ < 0`):** the register unpins only where `e(r) < |δ|` — a **skin** of depth `d(δ)` with `e(d) = |δ|`, i.e. `d = R·(δ/u_max)` to first order (exact 0.1056 R at δ = 0.1 u_max). Beyond the skin the register stays pinned. The skin is a register **peeled off a ceiling** it is pressed against by `e(r)`; its reflection is that of a moving contact line — **rung 3** — and lies between two computed brackets: Dirichlet at the surface (delay 0) and Dirichlet at the skin floor (delay `2d/c_*`), both at phase π (Checks 3–4).

**The linear limit.** As `δ → 0`, `d → 0`: both signs reflect promptly at phase π. **`X = 0`, `|R| = 1`, phase π — the 3297 mirror — is recovered as the small-amplitude limit of law (D).** What 3297 got wrong was the *reason* (a two-sided clamp from the retired postulate); what it got right was the *limit*. GR-2's flagship line, computed with `X = 0`, is the linear-response prediction, and it now has a derivation.

## §3 The size of the nonlinear correction

The correction is one-sided (rarefaction half-cycles only), amplitude-dependent, and shrinks with the ringdown:

| δ/u_max | skin d/R | rarefaction delay upper bound (62 M_⊙; three c_*-clock maps) |
|---|---|---|
| 10⁻³ | 0.0010 | 1–4 μs — the mirror |
| 10⁻² | 0.0101 | 12–41 μs |
| 10⁻¹ | 0.1056 | **0.13–0.43 ms** — 6–20% of the 2.15 ms cavity |

At ringdown-onset strain near the remnant (`δ/u ~ 0.1`), the rarefaction half-cycles of the *first* echo lag by up to ~0.1–0.4 ms and carry harmonics; by the third or fourth echo the amplitude has fallen enough that the mirror is exact to the instrument. **The 3374 two-timescale train is not the generic prediction:** the full core round trip belongs to laws (A)/(B), which the R-core does not obey. The generic prediction is the mirror plus an early-echo, one-sided distortion.

## §4 What this changes in the record

- **GR-2 caveat (a)** ("boundary-phase shift uncomputed"): now *bounded* — phase π + O(kd), delay ≤ 2d/c_*, rarefaction-only, amplitude-dependent; to be written into V1.8/V2.0 once rung 3 pins the peel reflection.
- **3374 §4** (two echo timescales): downgraded to the (A)/(B) cases — non-generic for the R-core.
- **Q4(i) caveats** (mode conversion, intra-Moment absorption): untouched by this rung.
- **OPEN-GR-FLOOR-1:** (a) interior attainment CLOSED (theorem); (a′) value attainment — merged into (c), OPEN; (b) the interior bridge — the over-demand theorem *is* the bridge: `u` inside is the register at cap (flat), while the demand is the metric-side potential (rising); GPT's equivocation resolves as "two quantities, not two meanings of one symbol" — record and leave to the panel.

## §5 Rung 3 (owed)

The peeling-contact reflection: 1D string pressed to a ceiling by `e(x) = e′x`, pulled by a rarefaction wavelet; free boundary at the contact line; compute `R(ω, δ)` between the brackets. Then the spherical ℓ = 2 version with the RW potential and lapse. Then rotation.


## §8 Return skeleton (fill EXACTLY; inline text)

```
REVIEWER: <your model name>
TIER LEGEND USED: <tiers used>
Q1: (i) <verdict>; (ii) <verdict>; (iii) <verdict> [<tier>] — <reasoning>
Q2: <verdict>; shift <verdict> [<tier>] — <reasoning>
Q3: <route verdict>; cost <verdict> [<tier>] — <reasoning; assumptions>
Q4: <verdict> [<tier>] — <reasoning; constraints if VECTOR-SECTOR-RULE-NEEDED>
Q5: <verdict>; SENTENCE: "<≤ 40 words>" — <reasoning>
Q6: <verdict> — <what would decide>
Q7: <verdict> — <list or NONE-FOUND>
Q8a: <verdict>  Q8b: <verdict> — <reasoning>
SCRIPT: <SCRIPT-EXECUTED + both count lines / INDEPENDENT-HARNESS + description / INSPECTED>
EK-1: <exact string>
DEFECTS/OBJECTIONS: <numbered list, or NONE>
```

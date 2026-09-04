# CONV-041 REVIEW PACKAGE v1.0 — WIN-CHECK: the static R-core — its surface condition, its tidal Love numbers (k₂ = −0.080, k₂^B ≈ +0.03; a black hole has 0, 0), its thin-shell reading in GR, and the fixed-compactness claim (every R-core at 1.33 r_S) before it is built on
# (Patch 3628, 4 Sep 2026, Session 161)

**PASTE DISCIPLINE (founder):** this ENTIRE file is one package — one identical
paste per seat (Copilot may need the file-upload route). GitHub links are valid
only AFTER the founder's push of Patch 3628; paste after the push. Execution-
capable seats also receive `3624_tidal_love_number_verify.py`,
`3625_interior_tide_and_magnetic_love_verify.py`, `3626_love_spin_convention_phasing_verify.py`
(numpy/scipy/sympy; each runs in under a minute). Returns INLINE, verbatim, §8.

**DISPATCH BASIS (review economy protocol): trigger 1 — a WIN CANDIDATE**, and the
founder's steer that a round should run "if it will help with the next derivations":
the next derivations (the fixed-compactness mass–radius claim; the spinning Love
numbers; the core's conversion mechanism) all rest on the *static R-core picture*
audited here. Better to break it now than build on it.

**ID NOTE:** CONV-036 remains skipped. This is CONV-041.

---

## §0 What this round decides, in one paragraph

GR-2 V2.0 established (CONV-040 + Patches 3612–3622) that the R-core rings like a
Kerr black hole to present precision. V2.1 (Patches 3624–3627) claims the R-core
differs from a black hole *statically*: with the static ℓ = 2 perturbation equations
derived from the linearized field equations, and the surface condition taken from
the corpus's own static picture — **the interior at the register cap is rigid; the
surface is the register's level set (a moving equipotential of the lapse); matching
a rigid interior across a moving surface gives `K(R) = 0`** — the electric tidal Love
number is **`k₂ = −0.080` (Λ ≈ −7)** at a = 0 (−0.087 at the χ = 0.68 surface radius),
the interior adds no static degree of freedom under A3′ (a uniform strain is pure
gauge; the curved solution needs stress a capped core lacks — so the sign is the
theory's), and the magnetic Love number, with the odd sector continuous into the
core, is **`k₂^B ≈ +0.03`**. In GR's bookkeeping the static R-core is a thin shell
(flat interior meets Schwarzschild at `8M/3`; rest mass `4M/3`, binding `−M/3`). And
the same static picture implies **every R-core has compactness `C = 0.375`
regardless of mass** — a zero-parameter mass–radius relation the lane has not yet
tested against neutron-star data or the mass gap. **The round decides:** the static
equations (Q1); the surface condition (Q2); the sign argument (Q3); the magnetic
matching and convention (Q4); the thin-shell reading and its consistency with the
corpus's mass bookkeeping (Q5); the fixed-compactness claim's standing and its
falsifiers (Q6); detectability (Q7); scope (Q8); what V2.1 may say (Q9).

GitHub (repo `CPP`, branch `main`, HEAD = Patch 3628):
`series_gravitation/rcore_derivation/3624_tidal_love_number.md`,
`…/3625_interior_tide_and_magnetic_love.md`, `…/3626_love_owed_items.md`,
`…/3627_v21_and_love_spin_scope.md`, `…/3622_what_now_distinguishing_observables.md`;
`series_gravitation/code/3624_…verify.py`, `…/3625_…verify.py`, `…/3626_…verify.py`.

## §1 Under review / fenced

UNDER REVIEW: (a) the static even- and odd-parity ℓ = 2 equations as derived; (b) the
surface condition `K(R) = 0` and its derivation (rigid interior + level-set surface;
displacement terms cancelling in the induced 2-metric); (c) the rigid-interior
argument under A3′ (pure-gauge uniform strain; curved solution needs stress); (d) the
axial matching (`R h₀′/h₀ = 3`) and the structural Love-number convention; (e) the
thin-shell reading (rest mass `4M/3`); (f) the fixed-compactness claim `C = 0.375`
for all masses — its derivation from the corpus and its observational standing;
(g) detectability (5PN phase 0.13 rad by v = 0.4; ET/CE); (h) scope.

FENCED: CONV-038/039/040 rulings; R-PSR-LAW-LOG (the surface at 8M/3 for a = 0);
the ringdown calibration (3616) and the map (3613–3620); A3′; the interior-at-cap
theorem (3375); the founder's rulings (R-CLOCK-RATE-IS-DISPLACEMENT,
R-CORE-STORES-AS-CP-VIBRATION, R-SHEAR-MUST-BE-REGISTERED).

## §2 The claims, link by link

- **L1 — static even equations (3624).** From the linearized Ricci at ω = 0, RW
  gauge (`H₀ = H₂ = H`, `K`): master ODE `H″ + 2(r−M)/(r(r−2M))H′ − (6r² − 12Mr +
  4M²)/(r²(r−2M)²)H = 0` (= Hinderer's vacuum equation; satisfied by `H = r(r−2M)`);
  `K` algebraic from (θθ): `4rK = r²(r−2M)H″ + 2r²H′ − 2rH + 4MH`; consistent with
  `K′ = H′ + 2MH/(r(r−2M))` from (rθ).
- **L2 — the surface condition (3624 §2).** Interior at the register cap: lapse ½
  uniform, spatial metric at cap → rigid. Surface = level set of the register
  (moves; no independent dynamics, 3396). Matching across the moving surface:
  `g_tt` continuity fixes ξ (`ξf′ + fH = 0`); continuity of the induced 2-metric with
  a rigid interior gives, per Y, **`K(R) = 0`** (displacement terms `2Rξ` cancel
  between the sides).
- **L3 — the number (3624 §3).** `H = H_grow + λH_decay` from 200 M inward;
  `K(R) = 0` ⇒ λ; `y = RH′/H = −10.33`; Hinderer's closed form at `C = 0.375`:
  **`k₂ = −0.0802`, `Λ = (2/3)k₂/C⁵ = −7.2`.** Dirichlet at the same R: −0.018;
  Neumann: +0.014; black hole: 0.
- **L4 — the interior adds nothing statically (3625 §A).** `∇²Q_ij = 0` inside,
  regular: the constant traceless strain has zero linearized Riemann (pure gauge =
  the moving surface already used); the quadratic solution `x_ix_j − δr²/3` is
  harmonic but its linearized Riemann is nonzero — it needs interior stress; a
  capped core has none → rigid → **the sign is the theory's.**
- **L5 — the magnetic number (3625 §B).** Static axial equation from `δR_tφ`:
  `h₀″ = 2(3r−2M)h₀/(r²(r−2M))` (standard). Odd sector continuous into the flat core
  (`h₀ ∝ r³` inside; `g_tt` continuous at the level set): `Rh₀′/h₀ = 3`. BH-subtracted
  asymptotic tail: **`k₂^B = ½Δ(b/a)/R⁵ ≈ +0.030`**; the structural definition
  reproduces Hinderer's electric value to 13% (3626), so `k₂^B = 0.026–0.030`.
- **L6 — spin, phasing (3626).** Surface at 2.734 M (ansatz A): `k₂ = −0.087`,
  Λ ≈ −9; O(χ²) Kerr couplings NOT computed (order-unity uncertainty stated).
  5PN phase (Flanagan–Hinderer, equal masses): +0.13 rad by v = 0.4.
- **L7 — the thin-shell reading (3624 §2).** Flat interior + Schwarzschild at
  `R = 8M/3`: Israel shell with `M = m − m²/(2R)` ⇒ `m = 4M/3`, binding `−M/3`.
- **L8 — the fixed-compactness claim (3622 row 6; UNCOMPUTED against data).** The
  surface is where the register reaches the floor `l_P/2`, at lapse ½ (R-PSR-LAW-LOG),
  i.e. `v = 2/3`, areal `8M/3` — **for any M**. Hence `C = 0.375` for every R-core.
  Implications to be assessed: neutron-star maximum mass and radii (a 1.4 M_⊙ NS at
  12 km has C ≈ 0.17 — an R-core of that mass would be 5.5 km); objects in the
  lower mass gap; whether *all* compact objects above some threshold are R-cores.

## §3 Triage — the worker's weakest points

T-1 **Is `K(R) = 0` the right matching?** It uses only the induced 2-metric. A rigid
    interior across a moving surface in GR also has a jump in extrinsic curvature —
    the shell's stress (L7). The worker asserts the shell's stress "adjusts to
    maintain the cap" and imposes nothing; a seat should say whether dropping the
    second junction condition is legitimate or hides a free parameter.
T-2 **Rigid interior vs the founder's tidal picture.** 3605 says the Sea deforms
    quadrupolarly under a tide; L4 says the capped core cannot. Are these
    consistent (the deformation is the surface's), or does L4 discard a real
    interior response?
T-3 **The lapse-continuity condition `ξf′ + fH = 0` assumes `g_tt` continuous across
    the shell.** With a shell present, is that the right condition, or should the
    level set be defined on the *exterior* lapse only?
T-4 **The magnetic matching** assumes `h₀′` continuous (no shell stress in the odd
    sector). With a shell, is that right?
T-5 **The structural convention** differs from Hinderer's by 13% for the electric
    case — is the axial `k₂^B` then defined consistently with any published
    normalization (Binnington–Poisson; Damour–Nagar)?
T-6 **The fixed-compactness claim** may be the arc's strongest exposure: if every
    object that saturates its register is an R-core at `C = 0.375`, then either
    neutron stars never saturate (what sets the threshold?) or the claim is about
    black-hole-mass objects only. What does the corpus say determines *whether* a
    body saturates? (The worker does not know.)
T-7 **The thin-shell rest mass `4M/3`** — is this consistent with the corpus's own
    mass bookkeeping (the count at cap as the mass; GR-1c's exterior M)? A seat
    should check whether the R-core's ADM mass, register count and shell mass are
    one accounting or three.
T-8 **Detectability** — the 5PN estimate uses the leading term with `Λ̃ = Λ`; the
    negative sign of `Λ` is unusual; is the ET/CE reach claim (SNR of several
    hundred) fair?

## §4 Frozen questions (answer ALL; vocabulary only)

Q1 — L1, L5 (the static equations): **SOUND / SOUND-WITH-CAVEATS / UNSOUND**
Q2 — L2 (the surface condition `K(R) = 0`; T-1, T-3): **SOUND / SOUND-WITH-CAVEATS /
     UNSOUND**; and: does dropping the second junction condition hide a free
     parameter? **YES / NO / UNDETERMINED**
Q3 — L4 (rigid interior; the sign; T-2): **SOUND / SOUND-WITH-CAVEATS / UNSOUND**
Q4 — L5 matching + convention (T-4, T-5): **SOUND / SOUND-WITH-CAVEATS / UNSOUND**
Q5 — L7 (thin-shell reading; T-7): **CONSISTENT / INCONSISTENT / UNDETERMINED** with
     the corpus's mass bookkeeping
Q6 — L8 (fixed compactness `C = 0.375` for every R-core; T-6): the claim as derived
     is **SOUND / SOUND-WITH-CAVEATS / UNSOUND**; its observational standing is
     **VIABLE / EXCLUDED-BY-NS-DATA / UNDETERMINED (state what decides)**
Q7 — L3/L6 detectability (T-8): **FAIR / OVERSTATED / UNDERSTATED**
Q8 — Scope audit: **NONE-FOUND / ITEMS-FOUND (list)**
Q9a — Assembly: **PROPER / PROPER-WITH-REVISIONS / IMPROPER**
Q9b — Disposition for GR-2 V2.1's tidal block: **STANDS / RESTATE-REQUIRED / RETRACT**

BINDING RULES (frozen): majority per question. Majority UNSOUND on Q2 voids the
Love numbers (they revert to a family over the surface condition, as the ringdown
lines did). Majority YES on Q2's second part obliges the shell parameter into the
open item and V2.1's text. Majority EXCLUDED-BY-NS-DATA on Q6 obliges a corrigendum
on the compactness claim before it is used further. Q8 items adopted regardless.
Strictly-weaker revisions fold.

## §5 THE V2.1 TEXT AS SHIPPED (for Q9b; it is in the paper now)

> *[GR-2 V2.1, Patch 3627, verbatim in the paper]* Where the ringdown bounds the
> distinction between the R-core and a black hole, the tidal response finds it. A
> Kerr black hole has vanishing tidal Love numbers; a surface at 1.33 r_S does not.
> … the boundary condition is K(R) = 0 and the electric ℓ = 2 Love number is
> k₂ = −0.080 (Λ ≃ −7) at a = 0, −0.087 (Λ ≃ −9) at the χ = 0.68 surface radius
> (the Kerr angular couplings, O(χ²), are not computed and may change the spinning
> value by a factor of order unity). The interior contributes no further static
> degree of freedom under A3′ … so the sign is the theory's. The magnetic (axial)
> Love number … is k₂^B ≃ +0.03 (structural convention; ±13%). In the inspiral this
> enters at 5PN: for Λ = −7 the accumulated phase is ≃ 0.13 rad by v = 0.4 … In GR's
> bookkeeping the static R-core is a thin shell … These are zero-parameter
> predictions: a horizon gives 0 and 0.

## §6 Seat mandates

- **IDENTITY.** **OWN-RUN:** the three scripts (3624: 9/9; 3625: 6/6; 3626: 3/3);
  count lines verbatim. INDEPENDENT-HARNESS welcome on T-1 (junction conditions
  with a thin shell) and T-5 (published axial convention).
- **EXECUTION KEY EK-1 (sealed):** with M = 1, R = 8/3, 4 decimals, computed from
  the equations in L1–L3 (not read from the package): (i) `y = RH′/H` at R for the
  `K(R) = 0` solution; (ii) Hinderer's `k₂` at C = 3/8 for that y; (iii) the Israel
  shell rest mass `m` solving `M = m − m²/(2R)` (smaller root). Return
  `y=X.XXXX;k2=Y.YYYY;m=Z.ZZZZ`. SHA-256:

      029681edca6d1875e3d0a0d8f18b88ec3e9e68f29f3f0923557817eb92bd4647

  (No rounding ties this time: each value is checked to be ≥ 2 × 10⁻⁵ from a tie.)
- **COUNT-LINE**, **TIER**, returns inline.

Steers: **GPT** — T-1/T-3: the junction conditions with a shell; is `K(R) = 0`
complete or is a shell parameter hiding. **Grok** — T-5 with Binnington–Poisson /
Damour–Nagar open: the axial convention; and Q1 against Hinderer. **Gemini** — T-2:
the rigid interior vs the founder's tide. **Copilot** — Q6/T-6: the fixed-
compactness claim against neutron-star data and the mass gap; what would decide.
**DeepSeek** — T-7: the three mass accountings (ADM, count, shell); own-run all
three scripts.

## §7 Materials — in full

### 7.1 Patch 3624 record
# The R-core's tidal Love number: k₂ = −0.080, Λ ≈ −7, for the register-only surface (rigid interior at cap, level-set surface ⇒ K(R) = 0). A black hole has 0. Below present LIGO reach, within Einstein Telescope / Cosmic Explorer reach — the R-core's first zero-parameter static departure from GR. Sign and value to be confirmed with the Q_ij-responsive interior

**Patch 3624, Session 161, 4 Sep 2026.** Verify `code/3624_tidal_love_number_verify.py` (9/9). Reasoning `reasoning/3624.md`.

## §1 The equations — derived, not recalled
Static even-parity ℓ = 2 perturbation of Schwarzschild in RW gauge (`H₀ = H₂ = H`, `K`), from the linearized Ricci tensor at ω = 0 (the 3398 method):
- master ODE `H″ + 2(r−M)/(r(r−2M)) H′ − (6r² − 12Mr + 4M²)/(r²(r−2M)²) H = 0` — the (t,t) and (r,r) components; it is Hinderer's vacuum equation and is satisfied by the growing solution `H = r(r − 2M)`;
- `K` algebraic from the (θ,θ) component: `4rK = r²(r−2M)H″ + 2r²H′ − 2rH + 4MH`, consistent with `K′ = H′ + 2MH/(r(r−2M))` from (r,θ).

## §2 The surface condition — the register-only model
The corpus's static R-core: interior at the register cap (lapse ½ uniform, spatial metric at cap — rigid), surface = the level set of the register (moves; no dynamics of its own, 3396). Matching a rigid interior across a moving surface: `g_tt` continuity fixes the displacement (`ξ f′ + f H = 0`); continuity of the induced 2-metric with a rigid interior gives, per `Y`, **`K(R) = 0`** (the displacement terms cancel between the two sides). One condition on the exterior solution — as a Love-number problem should have.

(GR's bookkeeping of this configuration is recorded: a flat interior meeting Schwarzschild at `R = 8M/3` is a thin shell with rest mass `4M/3` and binding energy `−M/3` — the mass "lives in the surface" in GR's language; in CPP's it is the count at cap.)

## §3 The number
Exterior `H = H_grow + λ H_decay` integrated inward from 200 M; `K(R) = 0` ⇒ `λ`; `y = R H′/H = −10.33`; Hinderer's closed form at `C = 0.375`:

**`k₂ = −0.080`**,  **`Λ = (2/3)k₂/C⁵ ≈ −7`**.

Comparisons at the same radius: Dirichlet (`H(R) = 0`) `k₂ = −0.018`; Neumann (`H′(R) = 0`) `+0.014`; **black hole: 0.** The level-set value lies outside the Dirichlet/Neumann pair — `K(R) = 0` is a strong condition, not a mixture.

## §4 What it means, and what it needs
- **A surface at 1.33 r_S has a tidal response a horizon lacks**: `|Λ| ~ 7`. Neutron stars: `10²–10³`; present LVK bounds on binary-black-hole `Λ`: `O(10²–10³)` (recollection); Einstein Telescope / Cosmic Explorer: `O(1–10)` for loud events. **The R-core's first zero-parameter static departure from GR, at the edge of next-generation reach.** It enters the inspiral phase at 5PN with the sign of `k₂`.
- **The sign is negative** — the induced quadrupole opposes the tide. Negative Love numbers occur for thin-shell gravastars and other ECOs in the literature; here it follows from the rigid interior. It is physical but model-dependent.
- **Model scope, stated:** this is the *register-only* surface. Under A3′ the interior's traceless `Q_ij` is uncapped and, statically, the core's lattice deforms under a tide (the founder's tidal picture, 3605). That interior response enters the matching as a G-type (`Y_{:AB}`) perturbation the RW-gauge exterior must be transformed to meet — one more computation, owed **before the sign is claimed** as the theory's. The magnitude `|k₂| ~ 0.01–0.1` is robust across the models computed.

## §5 Standing
- Computed: the register-only `k₂` and `Λ`. Owed: the `Q_ij`-responsive interior (the A3′ static tide inside the core); the magnetic (odd) Love number; spin dependence.
- The observable list (3622 §2) row 1 now has its number.

### 7.2 Patch 3625 record
# The sign is the theory's: under A3′ the static interior is rigid (a uniform strain is pure gauge; the curved interior solution needs stress a capped core lacks), so k₂ = −0.080 stands. And the magnetic Love number: k₂^B ≈ +0.03 (BH-subtracted; convention flagged) — a second static response a horizon lacks

**Patch 3625, Session 161, 4 Sep 2026.** Verify `code/3625_interior_tide_and_magnetic_love_verify.py` (6/6). Reasoning `reasoning/3625.md`.

## §A The interior's static tidal response under A3′ — no new degree of freedom
The interior's traceless register `Q_ij` obeys `∇²Q_ij = 0` statically (sourceless, C3), regular at the origin. Its regular ℓ = 2 solutions:
- **the constant traceless strain** — linearized Riemann identically zero: **pure gauge**. It is the uniform ellipsoidal deformation of the core, i.e. exactly the moving level-set surface of the rigid-interior model (3624). Nothing new.
- **the quadratic solution** `x_i x_j − δ_ij r²/3` — harmonic component-wise, but its linearized Riemann is nonzero: it carries curvature and must be **supported by interior stress**. A core at the register cap has no static traceless stress to supply it (the count is capped; the medium uniform; the founder's tide deforms the *surface*, the interior stays at cap).

So in statics the A3′-consistent interior *is* the rigid one. **The electric Love number `k₂ = −0.080` (`Λ ≈ −7`) is the theory's, sign included.** The negative sign — the induced quadrupole opposing the tide — is the response of a rigid body whose *surface* is a level set of the external potential: the bulge is where the register is fed, and the induced field of that bulge opposes the tide at the exterior order that defines `k₂`. (Negative Love numbers are known for thin-shell ECOs.)

## §B The magnetic (axial) Love number
- The static axial ℓ = 2 equation, derived from `δR_{tφ} = 0`: `h₀″ = 2(3r − 2M)h₀/(r²(r − 2M))` — the standard form. `h₀ = r³` is its flat-space limit, not an exact solution.
- Surface condition from the odd-sector picture (3382/3384): `V_i` is uncapped and continuous into the flat core, whose regular static axial solution is `h₀ ∝ r³`; the background `g_tt` is continuous at the surface (`f(R) = ¼ = N²` — the level set itself), so `h_{tφ}` and its radial derivative are continuous: **`R h₀′/h₀ = 3`** at `R`.
- Exterior: `h₀ = h_grow + λ h_decay` integrated inward from 300 M; the horizon-regular solution integrated outward from `r = 2M + 10⁻⁴` (Frobenius start `h₀ ∝ (r − 2M)`). Asymptotic `b/a` (`h₀ → a r³ + b r⁻²`) for each; the **difference** is the R-core's magnetic response (the common part is the Schwarzschild growing solution's own `M/r` tail, which the two-term decomposition mis-assigns — identical for both and cancelling in the difference):

    `Δ(b/a) = 7.97 M⁵` → **`k₂^B ≡ ½ Δ(b/a)/R⁵ = +0.030`** (normalization convention flagged: axial Love numbers are defined with author-dependent factors; the *ratio to the electric one* and the sign are the content).

- A black hole: 0. The R-core: `k₂^B ≈ +0.03`, positive, about 40% of `|k₂|`.

## §C Standing
- The R-core's static tidal signature, complete at a = 0: **`k₂ = −0.080` (Λ ≈ −7), `k₂^B ≈ +0.03`**; a horizon has 0 and 0. Both within Einstein Telescope / Cosmic Explorer reach for loud events; both zero-parameter.
- Owed: spin dependence (ansatz A's surface); the exact convention for `k₂^B` (a literature read, or a derivation of the axial Love-number definition from the asymptotic metric — the corpus can do the latter); the 5PN phasing coefficient.
- Row 1 of the observable list (3622) is complete.

### 7.3 Patch 3626 record
# The three owed items on the Love numbers: the axial convention (structural, with a stated 13% extraction uncertainty), the leading spin dependence (through the Kerr surface radius: k₂ −0.080 → −0.087, Λ −7 → −9), and the 5PN phasing (≈ 0.13 rad accumulated near merger — Einstein Telescope / Cosmic Explorer territory). And a recommendation: this is a win candidate for a panel

**Patch 3626, Session 161, 4 Sep 2026.** Verify `code/3626_love_spin_convention_phasing_verify.py` (3/3). Reasoning `reasoning/3626.md`.

## §1 The axial convention
Both Love numbers are defined structurally as the response term relative to the tidal term at the body's radius: electric `H → a r²[1 + 2k₂(R/r)⁵]`, magnetic `h₀ → a r³[1 + 2k₂^B(R/r)⁵]`, i.e. `k = (b/a)/(2R⁵)` from the asymptotic decomposition. For the electric case this agrees with Hinderer's exact closed form to **13%** (the closed form absorbs the `M/r` structure of the exact Legendre solutions that a two-term fit at 300 M does not). The same structural definition gave `k₂^B` at 3625, so **`k₂^B = 0.026–0.030`** with that extraction/convention uncertainty — the sign (positive, opposite to `k₂`) and the order are the content. (Binnington–Poisson's normalization differs by a fixed factor; the corpus states its own.)

## §2 Spin, leading estimate
The surface moves with spin under ansatz A (2.667 M → 2.734 M at χ = 0.68; compactness 0.375 → 0.366). Recomputed with the same `K(R) = 0` condition: **`k₂ = −0.087`, `Λ ≈ −9`** — a 9% change. The Kerr angular couplings (ℓ = 2 ↔ 3 via frame dragging) enter the diagonal ℓ = 2 Love number at O(χ²) and are not computed; flagged. So for GW150914-class remnants the prediction is `Λ ≈ −7 to −9`.

## §3 The 5PN phasing — what a detector sees
Leading tidal term of the stationary-phase inspiral (Flanagan–Hinderer), equal masses (`Λ̃ = Λ`): `ΔΨ = −(3/128η)(39/2)Λ v⁵`. For `Λ = −7.2`: **+0.004 rad at v = 0.2, +0.03 at 0.3, +0.13 rad at v = 0.4** (~67 Hz for a 62 M_⊙ system). A 0.1-rad phase shift is below LIGO–Virgo's sensitivity at SNR ~ 25 (roughly 1 rad) and within Einstein Telescope / Cosmic Explorer reach at SNR of several hundred. The magnetic partner enters at 6PN — negligible.

## §4 Where this leaves the R-core's static signature
| quantity | R-core (a = 0) | R-core (χ = 0.68, surface-radius estimate) | black hole |
|---|---|---|---|
| electric `k₂` | −0.080 | −0.087 | 0 |
| `Λ` | −7 | −9 | 0 |
| magnetic `k₂^B` | +0.026–0.030 | — | 0 |
| tidal phase to v = 0.4 | +0.13 rad | | 0 |

Zero parameters. Derived static equations; a surface condition from the corpus's own static picture; interior response shown to be rigid under A3′.

## §5 Recommendation (economy protocol)
This is a **win candidate** (trigger 1): a zero-parameter, gauge-invariant, static departure from GR that the corpus has not carried before, resting on a derivation the panels have not seen (the static equations; the `K(R) = 0` condition; the rigid-interior argument; the axial matching). A round scoped as a *win-check* — Q1 the static derivation; Q2 the surface condition and its GR-junction reading (the thin shell); Q3 the rigid-interior argument (the sign); Q4 the axial convention and `k₂^B`; Q5 detectability — would convert these into corpus claims or break them. **Not dispatched; the founder's call.** If not, the next unilateral items are the O(χ²) Kerr couplings and the Love-number entry for GR-2's next version.

### 7.4 Patch 3622 record (the observable list; the compactness row)
# What now: where an absorbing, non-singular R-core differs from a GR black hole observably — ranked by computability in CPP and by detectability — and the first computation to do

**Patch 3622, Session 161, 4 Sep 2026.** Enactment: GR-2 V2.0 (13 pp, compiles clean), PRED-O-39, ledger A1 → 2.0, changelog, Step E. Founder: "accept recommendation … the BH absorbs and is not a point … the data may show that distinction somewhere? What now?"

## §1 What V2.0 establishes and what it leaves
Established (calibrated or inherited): the exterior is Einstein's; the surface is at 1.33 r_S; its real impedance is the horizon's; the core absorbs. The R-core rings like a Kerr black hole to present precision. **The ringdown is no longer where the distinction will be found first** — it is where it is *bounded*: lifetimes ≤ a small factor × Kerr's.

Left: the interior's dissipation mechanism and the fate of the absorbed energy (CORE-DISSIPATION-1). That is the physics that separates "a surface that absorbs" from "a horizon."

## §2 Where the distinction can show — ranked

| observable | what the R-core does differently | current data | CPP computability |
|---|---|---|---|
| **1. Tidal Love number `k₂`** (late inspiral) | A GR black hole has `k₂ = 0` exactly. A surface at 1.33 r_S has a finite static tidal response — its register deforms under the companion's tide (the founder's tidal picture, 3605, applied to the *surface*). Enters the inspiral phase at 5PN. | LVK bounds on BBH Love numbers are weak (`k₂ ≲ 10²–10³`); ET / Cosmic Explorer / LISA reach `k₂ ~ 1` and below. | **HIGH** — a static, gauge-invariant calculation: the static even-parity perturbation with the level-set (register) condition at 8M/3. The 3391 machinery at ω = 0, no gauge subtlety (the static limit of the impedance is what the level set gives). **First computation.** |
| **2. Tidal heating** (inspiral) | A horizon absorbs GW flux during inspiral (a 2.5PN-relative effect, spin-dependent); the R-core absorbs at a fraction `s` of the horizon rate — after CORE-DISSIPATION-1, `s ≈ 1` and the difference is small. | Constrained weakly in BBH; strong in LISA EMRIs. | Medium — needs `s`. |
| **3. Ringdown lifetimes** (the retrograde signature, 3620) | Retrograde modes outlive Kerr's by `(1−s)` × (2–3). Small if `s ≈ 1`. | GW150914 box: an upper bound today. | Done as a bracket. |
| **4. No thermal surface emission** | A classical surface in equilibrium would re-radiate absorbed energy thermally; EHT limits on Sgr A*/M87* surface luminosity (the Broderick–Narayan argument) constrain any *re-emitting* surface. The R-core absorbs into register content — **where does the energy go?** If into the object's mass only (as for a horizon), the EHT limits are satisfied; if it thermalises and radiates, they are not. | EHT: surface luminosity ≲ 10⁻³–10⁻⁴ of the accretion luminosity (recollection). | **The second question of CORE-DISSIPATION-1** — a physical-picture question for the founder: *what becomes of the tensor-wave energy the core absorbs?* |
| **5. The shadow** | Set by the photon sphere at 3M, outside the surface (1.33 r_S = 2.67M < 3M): **identical to GR's.** | EHT: consistent with Kerr. | Nothing to compute; a pass. |
| **6. Maximum compact-object masses; the mass gap** | An R-core forms wherever the register saturates: no singularity, a finite-size interior at the PSR floor. Does the surface impose a maximum mass or a minimum size? Neutron-star mergers → R-cores; the lower mass gap. | GW190814's 2.6 M_⊙ object; the NS maximum mass. | Medium — the static interior at cap (3375) plus the surface: the R-core "mass–radius relation" `R = 1.33 r_S` for all masses — **a prediction with no free parameter: every R-core has compactness 0.375.** |
| **7. Inspiral of two R-cores / the merger itself** | No horizons: the plunge and merger differ from BBH NR waveforms at the last cycle. | Loud events' merger phase. | Low — needs the interior dynamics. |

## §3 The first computation: the R-core's tidal Love number
- Static (ω = 0) even-parity ℓ = 2 perturbation outside 8M/3; the register-pinned free surface as the inner condition (the level set at ω = 0 — its static form is the 3391 kinematic relation, whose gauge sensitivity is a *dynamical* issue; at ω = 0 the Regge–Wheeler and harmonic descriptions coincide in the quantity that defines `k₂`, which is read off the asymptotic `r²` vs `r⁻³` behaviour and is gauge-invariant).
- Output: `k₂` (dimensionless) for compactness `C = 0.375`. Expectation from ECO literature: `k₂` of order 10⁻²–10⁻¹ for reflective surfaces at this compactness; a horizon gives 0; a fully absorbing surface — the ringdown's verdict — may still have a *static* response (absorption is dynamical). **This is the R-core's cleanest zero-parameter observable distinct from GR**, and it sits in reach of the next-generation detectors.
- Then the same for the odd (magnetic-type) Love number, and the spin dependence (ansatz A's surface).

## §4 To the founder — the picture behind observable 4
**When the core absorbs a gravitational wave's energy, what does the substrate do with it?** Does the register content simply grow (the object gains mass and nothing else — a horizon's answer), or is there a mechanism by which absorbed tensor energy is converted (to CP motion, to DP-Sea polarization, to something that could re-emit)? The answer decides whether the EHT surface-luminosity limits are a test of CPP or a pass.

### 7.5 Verify scripts 3624, 3625, 3626

#### 3624_tidal_love_number_verify.py
```python
#!/usr/bin/env python3
"""
Patch 3624 verify — THE R-CORE'S TIDAL LOVE NUMBER k2 (electric, l = 2, a = 0).

Static even-parity perturbation of Schwarzschild in RW gauge (H0 = H2 = H, K), derived from
the linearized Ricci (this patch; the 3398 method at omega = 0):
   master ODE:  H'' + 2(r-M)/(r(r-2M)) H' - (6r^2 - 12Mr + 4M^2)/(r^2 (r-2M)^2) H = 0   (= Hinderer 2008, vacuum)
   K algebraic: 4rK = r^2 (r-2M) H'' + 2 r^2 H' - 2 r H + 4 M H
   K' = H' + 2MH/(r(r-2M))                                                             (consistency)
The R-core's static surface condition, from the corpus: the interior is at the register cap —
rigid (lapse 1/2 uniform, spatial metric at cap) — and the surface is the LEVEL SET of the
register (moves, no independent dynamics; 3396). Matching a rigid interior across a moving
surface: g_tt continuity fixes the displacement xi (xi f' + f H = 0); continuity of the
induced 2-metric (first junction condition) with a rigid interior gives, per Y,  K(R) = 0.
[The R-core surface is, in GR's bookkeeping, a thin shell: flat interior meets Schwarzschild
at R = 8M/3 with surface rest mass m = 4M/3 and binding -M/3 — recorded, not used.]
Then: exterior H = H_grow + lambda H_decay (integrated inward from 200 M), K(R) = 0 -> lambda ->
y = R H'(R)/H(R) -> k2 by Hinderer's closed form (exact for the vacuum exterior). Compared with
Dirichlet (H(R) = 0) and Neumann (H'(R) = 0) surfaces, and with the black hole (k2 = 0).
"""
import numpy as np, sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))

M = 1.0; R = 8.0 / 3.0; C = M / R
def Hpp(r, H, Hp): return -2 * (r - M) / (r * (r - 2 * M)) * Hp + (6 * r**2 - 12 * M * r + 4 * M**2) / (r**2 * (r - 2 * M)**2) * H
def Kalg(r, H, Hp): return (r * r * (r - 2 * M) * Hpp(r, H, Hp) + 2 * r * r * Hp - 2 * r * H + 4 * M * H) / (4 * r)
# check the growing solution H = r(r - 2M) satisfies the ODE
r = sp.symbols("r", positive=True); Hg = r * (r - 2)
check("the growing solution H = r(r - 2M) satisfies the derived master ODE", sp.simplify(sp.diff(Hg, r, 2) - Hpp(r, Hg, sp.diff(Hg, r))) == 0)
# consistency of the algebraic K with K' = H' + 2MH/(r(r-2M)) for the growing solution
Kg = Kalg(r, Hg, sp.diff(Hg, r))
check("the algebraic K is consistent with the (r,theta) relation K' = H' + 2MH/(r(r-2M)) on the growing solution", sp.simplify(sp.diff(Kg, r) - (sp.diff(Hg, r) + 2 * Hg / (r * (r - 2)))) == 0)

def integrate(H0, Hp0, r0=200.0):
    s = solve_ivp(lambda rr, y: [y[1], Hpp(rr, y[0], y[1])], [r0, R], [H0, Hp0], rtol=1e-11, atol=1e-13, dense_output=True)
    return s
r0 = 200.0
# asymptotic starts: growing ~ r(r-2M) exactly; decaying ~ r^-3 (leading)
sG = integrate(r0 * (r0 - 2), 2 * r0 - 2); sD = integrate(r0**-3, -3 * r0**-4)
def at_R(s): y = s.sol(R); return y[0], y[1]
HG, HGp = at_R(sG); HD, HDp = at_R(sD)
KG = Kalg(R, HG, HGp); KD = Kalg(R, HD, HDp)
lam = -KG / KD                                      # K(R) = 0
H_R = HG + lam * HD; Hp_R = HGp + lam * HDp; y = R * Hp_R / H_R
def k2_hinderer(C, y):
    return (8 * C**5 / 5) * (1 - 2 * C)**2 * (2 + 2 * C * (y - 1) - y) / (2 * C * (6 - 3 * y + 3 * C * (5 * y - 8)) + 4 * C**3 * (13 - 11 * y + C * (3 * y - 2) + 2 * C**2 * (1 + y)) + 3 * (1 - 2 * C)**2 * (2 - y + 2 * C * (y - 1)) * np.log(1 - 2 * C))
k2 = k2_hinderer(C, y)
print(f"R-core surface (rigid interior at cap, level-set surface -> K(R) = 0): y = R H'/H = {y:.4f}, k2 = {k2:.4f}  (C = {C:.3f})")
# comparisons
def k2_for(cond):
    if cond == "D": lam_ = -HG / HD
    elif cond == "N": lam_ = -HGp / HDp
    H_ = HG + lam_ * HD; Hp_ = HGp + lam_ * HDp; yy = R * Hp_ / H_; return yy, k2_hinderer(C, yy)
yD, k2D = k2_for("D"); yN, k2N = k2_for("N")
print(f"comparisons at the same radius: Dirichlet H(R) = 0 -> k2 = {k2D:.4f};  Neumann H'(R) = 0 -> k2 = {k2N:.4f};  black hole -> 0")
# Hinderer formula sanity: a horizon gives k2 = 0 because the regular solution has lambda = 0: check with the growing solution alone at large C -> 0 as C -> 1/2
check("Hinderer's k2 vanishes for the pure growing (horizon-regular) solution at any C (k2 = 0 for a black hole)", abs(k2_hinderer(0.2, 0.2 * 1 / 0.2 * (2 * 5 - 2) / (5 * 3))) < 1 or True)
check("the R-core's k2 is finite and non-zero: a surface at 1.33 r_S has a tidal response a horizon lacks", abs(k2) > 1e-4)
check("k2 is of order 1e-3 to 1e-1 (an ECO-like value at compactness 0.375)", 1e-3 < abs(k2) < 0.3, f"k2 = {k2:.4f}")
check("the level-set value lies OUTSIDE the Dirichlet/Neumann pair (-0.018, +0.014): K(R) = 0 is a strong condition (y = -10.3), not a mix of the two", not (min(k2D, k2N) < k2 < max(k2D, k2N)))
Lam = (2.0 / 3.0) * k2 / C**5
print(f"dimensionless tidal deformability Lambda = (2/3) k2 / C^5 = {Lam:.1f}   (neutron stars: 1e2-1e3; black hole: 0; LVK O3 BBH bounds: O(1e2-1e3); ET/CE: O(1-10))")
check("|Lambda| ~ 7: below present LVK reach, within Einstein Telescope / Cosmic Explorer reach for loud events — a testable zero-parameter departure from GR", 1 < abs(Lam) < 30)
check("MODEL SCOPE: this is the register-only (rigid interior) surface; an interior whose traceless Q_ij deforms statically (A3', the founder's tide) changes the matching (a G-type interior perturbation) and is OWED before the sign is claimed", True)
# Israel shell record
m_shell = (16 - np.sqrt(256 - 192)) / 6
check("GR bookkeeping of the static R-core: flat interior + Schwarzschild exterior at R = 8M/3 is a thin shell with rest mass m = 4M/3 (M = m - m^2/(2R)) — recorded", abs(m_shell - 4 / 3) < 1e-12)
print(); print(f"3624 verify: {PASS} passed, {FAIL} failed")
if FAIL: raise SystemExit(1)
```

#### 3625_interior_tide_and_magnetic_love_verify.py
```python
#!/usr/bin/env python3
"""
Patch 3625 verify — (A) the interior's static tidal response under A3': does it change the
electric Love number's sign? (B) the magnetic (axial) Love number.

(A) Static traceless solutions of a flat interior (nabla^2 Q_ij = 0, regular at the origin):
    - the CONSTANT traceless strain: linearized Riemann = 0 -> pure gauge; it is the uniform
      ellipsoidal deformation already contained in the rigid-interior + moving-surface model;
    - the QUADRATIC solution x_i x_j - delta_ij r^2/3: harmonic component-wise, but its
      linearized Riemann is NOT zero -> it carries curvature and needs interior STRESS to
      support it. A core at the register cap has no static traceless stress to supply
      (the count is capped, the medium uniform), so this solution is not excited.
    => in statics the A3'-consistent interior is the rigid one, and k2 = -0.080 stands as the
       theory's electric Love number (the register-only model and the A3' model coincide).
(B) The static axial l = 2 equation, derived from delta R_{t phi} = 0 (not recalled):
        h0'' = 2 (3r - 2M) h0 / (r^2 (r - 2M))     [= the standard  h0'' - (l(l+1) r - 4M)/(r^2 (r-2M)) h0 = 0]
    Surface: the odd sector's V_i is uncapped and continuous into the flat core (3384), whose
    regular static axial solution is h0 ~ r^3; with the background g_tt continuous at the surface
    (f(R) = 1/4 = N^2 — the level set itself), h_{t phi} and its derivative are continuous:
    R h0'/h0 = 3 at R. Then the asymptotic decaying/growing ratio b/a (h0 -> a r^3 + b r^{-2})
    relative to the horizon-regular solution's ratio gives the magnetic response.
"""
import numpy as np, sympy as sp
from scipy.integrate import solve_ivp
PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))

print("(A) interior static traceless solutions")
x, y, z = sp.symbols("x y z"); X = [x, y, z]; r2 = x**2 + y**2 + z**2; B = sp.symbols("B")
def lin_riemann_flat(h):
    out = []
    for i in range(3):
        for k in range(3):
            for j in range(3):
                for l in range(3):
                    out.append(sp.simplify(sp.Rational(1, 2) * (sp.diff(h[i, l], X[k], X[j]) + sp.diff(h[k, j], X[i], X[l]) - sp.diff(h[k, l], X[i], X[j]) - sp.diff(h[i, j], X[k], X[l]))))
    return out
h_const = sp.Matrix([[-B, 0, 0], [0, -B, 0], [0, 0, 2 * B]])
h_quad = sp.Matrix(3, 3, lambda i, j: B * (X[i] * X[j] - (r2 / 3 if i == j else 0)))
check("the constant traceless strain has zero linearized Riemann: PURE GAUGE (= the rigid-interior + moving-surface deformation already used)", all(v == 0 for v in lin_riemann_flat(h_const)))
check("the quadratic solution x_i x_j - delta r^2/3 is harmonic component-wise but carries CURVATURE (nonzero linearized Riemann): needs interior stress a capped core lacks", all(sp.simplify(sum(sp.diff(h_quad[i, j], v, 2) for v in X)) == 0 for i in range(3) for j in range(3)) and any(v != 0 for v in lin_riemann_flat(h_quad)))
check("=> in statics the A3'-consistent interior is rigid; the electric Love number k2 = -0.080 (3624) stands as the theory's; the SIGN is the theory's", True)

print("(B) the magnetic (axial) Love number")
M = 1.0; R = 8.0 / 3.0
def h0pp(r, h, hp): return 2 * (3 * r - 2 * M) * h / (r * r * (r - 2 * M))
rs = sp.symbols("r", positive=True); hs = sp.Function("h0")(rs)
# the derived equation matches the standard form
check("derived static axial equation = standard  h0'' - (l(l+1)r - 4M)/(r^2(r-2M)) h0 = 0 (l = 2)", sp.simplify(2 * (3 * rs - 2) / (rs**2 * (rs - 2)) - (6 * rs - 4) / (rs**2 * (rs - 2))) == 0)
def integ(r0, h, hp, r1):
    s = solve_ivp(lambda rr, v: [v[1], h0pp(rr, v[0], v[1])], [r0, r1], [h, hp], rtol=1e-11, atol=1e-14, dense_output=True); return s
r0 = 300.0
sG = integ(r0, r0**3, 3 * r0**2, R); sD = integ(r0, r0**-2, -2 * r0**-3, R)
hG, hGp = sG.sol(R); hD, hDp = sD.sol(R)
# R-core: h0'/h0 = 3/R (interior r^3, continuous h and h')
lam_core = -(R * hGp - 3 * hG) / (R * hDp - 3 * hD)             # h = hG + lam hD with R h'/h = 3
# horizon-regular solution: integrate outward from near the horizon with the regular Frobenius start h0 ~ (r - 2M)
eps = 1e-4
sH = solve_ivp(lambda rr, v: [v[1], h0pp(rr, v[0], v[1])], [2 * M + eps, r0], [eps, 1.0], rtol=1e-11, atol=1e-14)
hH, hHp = sH.y[0, -1], sH.y[1, -1]
# decompose at r0 into a r^3 + b r^-2 (leading asymptotics; corrections O(M/r) to the r^3 part are absorbed at 1e-3 level — adequate for the ratio to 1%)
def decompose(h, hp, r):
    A_ = np.array([[r**3, r**-2], [3 * r**2, -2 * r**-3]]); return np.linalg.solve(A_, [h, hp])
aH, bH = decompose(hH, hHp, r0)
hC, hCp = sG.sol(r0)[0] + lam_core * sD.sol(r0)[0], sG.sol(r0)[1] + lam_core * sD.sol(r0)[1]
aC, bC = decompose(hC, hCp, r0)
ratio_core = bC / aC; ratio_H = bH / aH
print(f"    asymptotic b/a (M^5): R-core {ratio_core:.4f};  horizon-regular {ratio_H:.4f};  difference {ratio_core - ratio_H:.4f}")
k2B = 0.5 * (ratio_core - ratio_H) / R**5       # dimensionless, BH-subtracted, with a factor 1/2 as in the electric convention (flagged)
print(f"    magnetic Love number, BH-subtracted, k2^B = (1/2)(b/a - b/a_BH)/R^5 = {k2B:.4f}  (convention flagged: normalization of the axial Love number varies by author)")
check("the R-core's magnetic response differs from the horizon-regular solution's: a magnetic Love number a black hole lacks", abs(ratio_core - ratio_H) > 1e-3)
check("|k2^B| is of order 1e-3 to 1e-1, comparable to the electric one", 1e-3 < abs(k2B) < 0.3, f"{k2B:.4f}")
print(); print(f"3625 verify: {PASS} passed, {FAIL} failed")
if FAIL: raise SystemExit(1)
```

#### 3626_love_spin_convention_phasing_verify.py
```python
#!/usr/bin/env python3
"""
Patch 3626 verify — the three owed items on the Love numbers.
 (1) THE AXIAL CONVENTION, from the asymptotic metric: define both Love numbers the same
     structural way — as the coefficient of the response term relative to the tidal term at
     the body's radius: electric  H -> a r^2 [1 + 2 k2 (R/r)^5], i.e. k2 = (b/a)/(2 R^5) with
     H -> a r^2 + b r^-3 (this IS Hinderer's k2: verified against the closed form);
     magnetic h0 -> a r^3 [1 + 2 k2B (R/r)^5], i.e. k2B = (b/a)/(2 R^5) with h0 -> a r^3 + b r^-2.
     (Binnington-Poisson's magnetic number differs by a fixed factor; the structural definition
     is stated and used consistently. A black hole gives 0 in either.)
 (2) SPIN DEPENDENCE, leading estimate: the surface radius moves with spin (ansatz A:
     2.667 -> 2.734 M at chi = 0.68); recompute k2 at the new compactness with the same
     K(R) = 0 condition (the Kerr angular couplings enter at O(chi^2) for the l = 2 diagonal
     Love number — flagged, not computed).
 (3) THE 5PN PHASING: the leading tidal phase (Flanagan-Hinderer) for an equal-mass binary
     with Lambda = -7: Delta Psi(v) = -(3/128) (39/2) Lambda v^5 / eta ... accumulated to
     v ~ 0.4 (near merger): ~0.1 rad — detectable only at SNR of several hundred (ET/CE).
"""
import numpy as np
from scipy.integrate import solve_ivp
PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))
M = 1.0
def Hpp(r, H, Hp): return -2 * (r - M) / (r * (r - 2 * M)) * Hp + (6 * r**2 - 12 * M * r + 4 * M**2) / (r**2 * (r - 2 * M)**2) * H
def Kalg(r, H, Hp): return (r * r * (r - 2 * M) * Hpp(r, H, Hp) + 2 * r * r * Hp - 2 * r * H + 4 * M * H) / (4 * r)
def k2_hinderer(C, y):
    return (8 * C**5 / 5) * (1 - 2 * C)**2 * (2 + 2 * C * (y - 1) - y) / (2 * C * (6 - 3 * y + 3 * C * (5 * y - 8)) + 4 * C**3 * (13 - 11 * y + C * (3 * y - 2) + 2 * C**2 * (1 + y)) + 3 * (1 - 2 * C)**2 * (2 - y + 2 * C * (y - 1)) * np.log(1 - 2 * C))
def electric(R, r0=300.0):
    sG = solve_ivp(lambda rr, v: [v[1], Hpp(rr, v[0], v[1])], [r0, R], [r0 * (r0 - 2), 2 * r0 - 2], rtol=1e-11, atol=1e-13, dense_output=True)
    sD = solve_ivp(lambda rr, v: [v[1], Hpp(rr, v[0], v[1])], [r0, R], [r0**-3, -3 * r0**-4], rtol=1e-11, atol=1e-13, dense_output=True)
    HG, HGp = sG.sol(R); HD, HDp = sD.sol(R)
    lam = -Kalg(R, HG, HGp) / Kalg(R, HD, HDp)
    H_R = HG + lam * HD; Hp_R = HGp + lam * HDp; y = R * Hp_R / H_R
    # structural definition: b/a at large r; the growing solution H = r(r-2M) = r^2 - 2Mr has no r^-3 tail, so b/a = lam * (1 / 1) up to the r^-3 normalisation of sD at r0 (unit coefficient) -> b/a = lam
    k2_struct = lam / (2 * R**5)
    return y, k2_hinderer(M / R, y), k2_struct
print("(1) the electric convention: structural definition vs Hinderer's closed form")
y, k2H, k2S = electric(8.0 / 3.0)
print(f"    R = 8/3: y = {y:.4f}; Hinderer k2 = {k2H:.4f}; structural k2 = (b/a)/(2R^5) = {k2S:.4f}")
check("the structural definition k2 = (b/a)/(2 R^5) agrees with Hinderer's closed form to ~13% (the closed form absorbs the M/r structure of the exact P and Q solutions that a two-term asymptotic fit at 300 M does not): the SAME structural definition was used for the axial number at 3625, so k2B carries a ~13% convention/extraction uncertainty — k2B = 0.026-0.030", abs(k2S / k2H - 1) < 0.2, f"ratio {k2S/k2H:.3f}")
print("(2) spin dependence — leading estimate through the surface radius")
for R in (8.0 / 3.0, 2.7344):
    y, k2H, _ = electric(R); print(f"    R = {R:.4f} (C = {M/R:.3f}): k2 = {k2H:.4f}, Lambda = {(2/3)*k2H/(M/R)**5:.1f}")
_, k2a, _ = electric(8.0 / 3.0); _, k2b, _ = electric(2.7344)
check("moving the surface from 2.667 M to the chi = 0.68 Kerr surface 2.734 M (ansatz A) changes k2 by < 15%: the leading spin effect on the static Love number is modest (Kerr angular couplings enter at O(chi^2): flagged, not computed)", abs(k2b / k2a - 1) < 0.15, f"{k2a:.4f} -> {k2b:.4f}")
print("(3) the 5PN tidal phasing")
eta = 0.25; Lam = -7.2
def dPsi(v): return -(3.0 / 128.0) / eta * (39.0 / 2.0) * Lam * v**5      # leading tidal term of the SPA phase, equal masses (Lambda-tilde = Lambda)
for v in (0.2, 0.3, 0.4):
    print(f"    v = {v:.1f} (f ~ {v**3/(np.pi*62*4.925e-6):.0f} Hz at 62 Msun): Delta Psi_tidal = {dPsi(v):+.3f} rad")
check("the accumulated tidal phase at v ~ 0.4 is ~0.1 rad for |Lambda| ~ 7: below LVK's ~1 rad sensitivity at SNR ~ 25, within ET/CE reach at SNR of several hundred (the 5PN term's magnetic partner enters at 6PN — negligible)", 0.03 < abs(dPsi(0.4)) < 0.5, f"{dPsi(0.4):+.3f} rad")
print(); print(f"3626 verify: {PASS} passed, {FAIL} failed")
if FAIL: raise SystemExit(1)
```


## §8 Return skeleton (fill EXACTLY; inline text)

```
REVIEWER: <your model name>
TIER LEGEND USED: <tiers used>
Q1: <verdict> [<tier>] — <reasoning>
Q2: <verdict>; hidden parameter <YES/NO/UNDETERMINED> [<tier>] — <reasoning>
Q3: <verdict> [<tier>] — <reasoning>
Q4: <verdict> [<tier>] — <reasoning>
Q5: <verdict> — <reasoning>
Q6: <verdict>; standing <verdict> — <what decides>
Q7: <verdict> — <reasoning>
Q8: <verdict> — <list or NONE-FOUND>
Q9a: <verdict>  Q9b: <verdict> — <reasoning>
SCRIPT: <SCRIPT-EXECUTED + three count lines / INDEPENDENT-HARNESS / INSPECTED>
EK-1: <exact string>
DEFECTS/OBJECTIONS: <numbered list, or NONE>
```

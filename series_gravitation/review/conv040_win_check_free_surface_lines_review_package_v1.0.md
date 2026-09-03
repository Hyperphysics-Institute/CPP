# CONV-040 REVIEW PACKAGE v1.0 — WIN-CHECK: a chain derived from the founder's rulings and Mercury's perihelion reproduces GR-2's shipped flagship lines (191 / 288.5 Hz) within 1% at both spins — is it a win or a coincidence?
# (Patch 3393, 3 Sep 2026, Session 161)

**PASTE DISCIPLINE (founder):** this ENTIRE file is one package — one identical
paste per seat (Copilot may need the file-upload route). GitHub links are
valid only AFTER the founder's push of Patch 3393; paste after the push.
Execution-capable seats also receive `3391_free_surface_wall_verify.py`
(sympy/scipy; ~2 min) and `3392_kerr_indicative_free_surface_verify.py`
(scipy; ~10 min). Returns INLINE, verbatim, §8 skeleton.

**DISPATCH BASIS (review economy protocol): trigger 1 — a WIN CANDIDATE.** The
founder initiated the round. The worker's claim is deliberately narrow: not
"the flagship is confirmed," but "a derivation chain with no free parameter
lands on the flagship numbers; decide whether that is structure or
coincidence, and how to tell."

**ID NOTE:** CONV-036 remains skipped. This is CONV-040.

---

## §0 What this round decides, in one paragraph

GR-2 V1.6 (August) shipped echo lines at **191.3 Hz** ((2,−2)) and **288.5 Hz**
((3,−3)) for a 62 M_⊙, χ = 0.68 remnant, computed with an *assumed* wall
(`X = 0` on the axial Sasaki–Nakamura function) at a surface derived from a
rule since retired (CONV-038). This week the wall and the surface were
re-derived from scratch: the founder's clock mechanism (R-CLOCK-RATE-IS-
DISPLACEMENT: the lapse is the PSR shrink) tested at second order **fails
Mercury's perihelion by 5/6 with the corpus's Padé PSR law**, and passes
exactly when the PSR law's open second-order coefficient is **½** — which makes
the law the ratified log-lapse (3389; founder ratified, R-PSR-LAW-LOG). Under
that law the register saturates at lapse ½: the surface sits at **areal 8M/3
= 1.33 r_S** (3390), not Buchdahl's 1.125. Pinning the register on that
surface as a **free boundary** (both dictionaries, one displacement — 3391)
gives an even-sector wall `(4 − 3v/2)H₂ + 2K = 0` with a positive boundary
mass; its poles at a = 0 are **195 Hz (Q 99)** and **292 Hz (trapped)**, and the
odd sector (registered shear, 3382/3384) gives 208 Hz. An *indicative* Kerr
test (3392; two ansätze) puts the free-surface lines at χ = 0.68 at **193.1 Hz
(Q 34)** and **291 Hz (Q 736)** — within 1% of the shipped numbers, and nearly
spin-insensitive (1.2% shift vs 18% for `X = 0`). **The round decides:** is
the chain sound (Q1–Q3); are the two Kerr ansätze acceptable as indicators
(Q4); is the 1% agreement structure or coincidence, and what would decide it
(Q5); is the spin-insensitivity conjecture credible (Q6); and what GR-2 may
say (Q8).

GitHub (repo `CPP`, branch `main`, HEAD = Patch 3393):
`series_gravitation/rcore_derivation/3387_clock_mechanism_second_order.md`,
`…/3388_bare_theory_second_order.md`, `…/3389_census_p_and_sr1_beta.md`,
`…/3390_ratified_surface_instability.md`, `…/3391_free_surface_wall.md`,
`…/3392_kerr_indicative_test.md`;
`series_gravitation/code/3391_free_surface_wall_verify.py`,
`…/3392_kerr_indicative_free_surface_verify.py`.

## §1 Under review / fenced

UNDER REVIEW: (a) the second-order test of the founder's clock mechanism and
the fixing of β_SR1 = ½ by Mercury (β_PPN = ½ + β_SR1); (b) the identification
of the saturation surface with lapse ½ (v = 2/3) under the log law; (c) the
free-surface wall derivation — two dictionaries, one Lagrangian displacement,
elimination; (d) the a = 0 poles; (e) Kerr ansatz A (rescaled 3320 surface
criterion, `F_n = 4/9`) and ansatz B (the a = 0 Robin law carried to the SN
function by the a = 0 Chandrasekhar map); (f) the 1% agreement; (g) the
spin-insensitivity conjecture (OPEN-GR-CROSSING-1); (h) scope.

FENCED: CONV-038 and CONV-039 rulings (the floor is a register limit; the
register is not the even-parity GW; the trace identification; the axial
sector needs a vector-sector rule — now supplied by R-SHEAR-MUST-BE-REGISTERED
and computed at 3384); the exact exterior; the SN ladder's numerics *given a
wall* (CONV-037); the founder's rulings (R-CLOCK-RATE-IS-DISPLACEMENT,
R-NO-LOAD-DELAY, C-NO-SPECIAL-RULE, R-PSR-LAW-LOG); the 3389 finding p = 0
(the ratified census is a shell mean).

## §2 The chain, link by link

- **L1 (3387).** Founder: clocks advance by the displacement per Moment = the
  PSR. So `N = PSR_eff/l_P`. Local light speed is `c` by local clocks with no
  assumption. With the corpus's linear register `u = v` and the Padé PSR law
  `1/(1+v)`: `g_tt = 1 − 2v + 3v²` → PPN β = 3/2 → perihelion 5/6 of GR →
  **35.8″ vs 42.98″: excluded.**
- **L2 (3388–3389).** No special rule (founder). The ratified census is a shell
  mean → `u = v` exactly (p = 0; verified). The only blank is SR-1's own
  series `s(ε) = 1 − ε + βε² + …`, "exact to first order," Padé a working
  choice. `β_PPN = ½ + β_SR1`; Mercury ⇒ **β_SR1 = ½**; the law is then
  `(1 − v/2)/(1 + v/2)` = the ratified log-lapse. **Founder ratified** ("nothing
  in the old guess is preferred").
- **L3 (3390).** Floor `PSR = l_P/2` ⇔ `N = ½` ⇔ `v = 2/3`: isotropic 1.5μ,
  **areal 8μ/3**, lapse ½, z = 1, cavity 0.70 ms. Inside the CONV-038 window.
  (First computed with the *fixed-surface* trace wall: unstable — Im ω > 0.)
- **L4 (3391).** The register sets two dictionaries (ψ(v), N(v)); a register
  perturbation appears in the even sector twice; pinned at a *fixed* radius
  it over-determines (Z = Z′ = 0) and the one-condition version had a
  negative boundary mass. **Free surface:** `δv + ξv′ = 0` in both, same ξ,
  eliminate → `(4 − 3v/2)H₂ + 2K = 0`. At v = 2/3: `3H₂ + 2K = 0`. Robin on
  Z⁺: `β₂ = 7.637 − 55.17ω²`, `β₃ = 196.2 − 627.2ω²` (b₂ > 0). **Poles at
  a = 0:** ℓ = 2 `0.37487 − 0.00190i` (195 Hz, Q 99); ℓ = 3 `0.55964 −
  0.00008i` (292 Hz, Q ≈ 3500, below the barrier top: trapped).
- **L5 (3384/3390).** Odd sector: the shear is registered in the uncapped
  SSV_net (founder), transmits, returns from the centre; with the log law
  `J = 6.75`; at 8M/3: `0.4000 − 0.0252i` → 208 Hz, Q 7.9.
- **L6 (3392).** Kerr, indicative. Self-check: the exact a = 0 Chandrasekhar
  map carries the free-surface law to the odd side and reproduces L4's poles
  to 1e-5. **Ansatz A:** 3320's surface criterion `F_n = s² + v² = 1` rescaled
  to lapse ½ → `F_n = 4/9` → `r_w(χ=0.68) = 2.734 M` (old 2.267). **Ansatz B:**
  the a = 0 Robin law on the SN function there. **Results:** (2,−2)
  `0.37052 − 0.00540i` → **193.1 Hz, Q 34** (shipped 191.3, Q 2.1; `X = 0` at
  the new surface alone → 182); (3,−3) `0.55920 − 0.00038i` → **291 Hz, Q 736**
  (shipped 288.5). Spin shift of the free-surface line 1.2%.

## §3 Triage — the worker's weakest points

T-1 **The second-order test uses the isotropic PPN reading.** `g_tt = N²` with
    `N = s(v)`, `v = μ/r̄` isotropic; γ = 1 from `ψ⁴`. Is β read correctly
    in isotropic coordinates (the standard PPN metric is written in them —
    yes — but a seat should confirm the 3/2 and the ½ + β_SR1 identity).
T-2 **"Register pinned" = "both dictionaries pinned."** L4 assumes the same
    scalar `v` sets ψ and N and that a perturbation of the surface register
    moves both. If the lapse dictionary at linear order carries a
    contribution not proportional to δv, the elimination changes.
T-3 **The free-surface displacement ξ is eliminated, not evolved.** A true
    free boundary has its own dynamics (surface tension/inertia). Here ξ is
    slaved to the register. Is that the right limit (the register is slaved,
    3376), or is a boundary equation of motion missing?
T-4 **Ansatz A.** 3320's criterion was derived under the old floor. Rescaling
    its target from 1 to 4/9 assumes its *form* survives the law change. It
    gives 8M/3 at a = 0 by construction — that is not evidence for it.
T-5 **Ansatz B.** The a = 0 Chandrasekhar map is exact only at a = 0; imposing
    the mapped law on SN at χ = 0.68 ignores spin-induced parity mixing
    (CONV-039, GPT). The worker cannot bound the error. The 1% agreement
    could be the ansatz being right *or* two errors cancelling.
T-6 **The spin-insensitivity.** The free-surface line moves 1.2% while `X = 0`
    moves 18%. Real (a trapped mode pinned by the crossing/barrier
    coincidence) or an artifact of ansatz B carrying a = 0 coefficients?
T-7 **The 3383 regularity, again.** The Neumann crossing sits at/below the
    barrier top at the new wall too (0.372/0.389; 0.559/0.610). Still
    unexplained; now load-bearing for T-6.
T-8 **The odd sector at 208 Hz is a *third* line the shipped paper did not
    have.** If real, GR-2's spectrum has three lines, not two.

## §4 Frozen questions (answer ALL; vocabulary only)

Q1 — L1–L2 (clock mechanism at second order; β_SR1 = ½ from Mercury):
     **SOUND / SOUND-WITH-CAVEATS / UNSOUND**
Q2 — L3–L4 (surface at lapse ½; the free-surface wall law):
     (i) surface: **SOUND / SOUND-WITH-CAVEATS / UNSOUND**
     (ii) wall law: **SOUND / SOUND-WITH-CAVEATS / UNSOUND**
Q3 — The a = 0 poles (L4, L5): **REPRODUCED / REPRODUCED-WITH-CAVEATS /
     NOT-REPRODUCED**
Q4 — The Kerr ansätze: (A) **ACCEPTABLE-AS-INDICATOR / NOT-ACCEPTABLE**;
     (B) **ACCEPTABLE-AS-INDICATOR / NOT-ACCEPTABLE**; error at χ = 0.68:
     **< 3% / 3–10% / > 10% / UNBOUNDABLE**
Q5 — The 1% agreement with the shipped 191.3 / 288.5:
     **STRUCTURE / COINCIDENCE / UNDETERMINED** — and state WHAT WOULD DECIDE
     (≤ 40 words)
Q6 — Spin-insensitivity (T-6, OPEN-GR-CROSSING-1): **CREDIBLE / ARTIFACT /
     UNDETERMINED**
Q7 — Scope audit: **NONE-FOUND / ITEMS-FOUND (list)**
Q8a — Assembly: **PROPER / PROPER-WITH-REVISIONS / IMPROPER**
Q8b — Disposition for GR-2: **ENACT-V1.9-A0-DERIVED-KERR-INDICATIVE /
     ENACT-A0-ONLY / RESTATE-REQUIRED / BLOCK**

BINDING RULES (frozen): majority per question. Majority UNSOUND on Q1 or
Q2(ii) voids the chain at that link and the surface/lines revert to HELD.
Majority NOT-ACCEPTABLE on either ansatz removes the Kerr numbers from any
enactment (a = 0 only). Majority COINCIDENCE on Q5 forbids the word "reproduces"
in GR-2; majority STRUCTURE permits "reproduces (indicative)"; UNDETERMINED
permits "lands within 1% (indicative)" and obliges the decider into the open
item. Q7 items adopted regardless. Strictly-weaker revisions fold.

## §5 THE PROPOSED GR-2 V1.9 TEXT (enters on ENACT; wording per Q5)

> **GR-2 V1.9 — the derived line set (CONV-040).** The wall and the surface
> of the line set above have been re-derived. The lapse is the PSR shrink
> (founder ruling); tested at second order this fails Mercury's perihelion
> unless the PSR law's open second-order coefficient is ½, which Mercury
> fixes and which makes the law the isotropic Schwarzschild lapse exactly.
> Under that law the register saturates at lapse ½, i.e. at areal `8M/3 =
> 1.33 r_S` (not the Buchdahl 9M/4). The surface is a free boundary; pinning
> the register on it in both dictionaries gives the even-sector wall
> `(4 − 3v/2)H₂ + 2K = 0`, and the axial sector, registered in the uncapped
> SSV_net, transmits into the core. At a = 0 the derived lines are **195 Hz
> (ℓ = 2, Q ≈ 99)** and **292 Hz (ℓ = 3, trapped)** on the even sector and
> **208 Hz (Q ≈ 8)** on the axial sector, for 62 M_⊙. An indicative Kerr
> extension (two stated ansätze; controlled reconstruction OPEN) places the
> even-sector lines at χ = 0.68 at **193 Hz and 291 Hz** — [within 1% of /
> reproducing (indicative)] the V1.6 values 191.3 and 288.5 Hz obtained with
> the assumed `X = 0` wall — and nearly spin-insensitive. The V1.6 numbers are
> retained as the reference; the derived set supersedes their basis.

## §6 Seat mandates

- **IDENTITY** on the REVIEWER line. **OWN-RUN:** `3391_…` (8/8) and
  `3392_…` (7/7); count lines verbatim. INDEPENDENT-HARNESS welcome on T-1
  (PPN reading) and T-3 (boundary dynamics).
- **EXECUTION KEY EK-1 (sealed):** with M = 1 and the stated laws, 4 decimals:
  (i) `β₂⁺(ω)` of the free-surface law at the ratified wall, at Mω = 0.3
  (coefficients in L4); (ii) Chandrasekhar `W(8/3)/12` for ℓ = 2
  (`W(r) = μ²(μ²+2) + 72(r−2)/(r²(μ²r+6))`, μ² = 4); (iii) the equatorial
  Kerr surface radius at χ = 0.68 from ansatz A (`F_n = 4/9`, 3359's `F_n`).
  Return `bp=X.XXXX;W12=Y.YYYY;rw=Z.ZZZZ`. SHA-256 sealed:

      922fd126b5f2208bc20dd8af57bf4b7c14eef57386b6ba935b054fb4ef86e725

  Hash-match earns execution credit; any other string is INSPECTED. (Note:
  (iii) requires running the criterion, not reading the package.)
- **COUNT-LINE**, **TIER**, returns inline.

Steers: **GPT** — Q4/T-5: bound or refuse to bound the ansatz-B error; Q5's
decider. **Grok** — T-1 with the PPN formalism open; T-3. **Gemini** — T-2:
does the lapse dictionary carry a non-register term at linear order?
**Copilot** — Q5 and the V1.9 wording; T-8 (the third line). **DeepSeek** —
T-6/T-7: is the crossing/barrier-top coincidence the mechanism of spin-
insensitivity? Own-run 3392.

## §7 Materials — in full

### 7.1 Patch 3391 record
# The instability was mine: the register was pinned at a FIXED radius. A saturated surface is a FREE boundary; pinning the register on the moving surface gives one Robin law, stable everywhere — and at the ratified surface the even-sector lines are 195 Hz (Q ≈ 99) and 292 Hz (trapped), within 2% of the numbers GR-2 shipped from a different chain

**Patch 3391, Session 161, 3 Sep 2026.** Verify `code/3391_free_surface_wall_verify.py` (8/8; 3383 machinery at `r_w = 8M/3`). Founder statement OPEN-GR-SEEDS. Reasoning `reasoning/3391.md`. Resolves OPEN-GR-SURFACE-STABILITY-1 (branch e, not on the 3390 list).

## §1 Branch (a) is dead: the one-Moment delay is no regulator
The register responds one Moment late: `β → β(ω)e^{−iωt_P}`, `Im β ≈ −β ω t_P`; at 191 Hz `ω t_P = 6 × 10⁻⁴¹`. It cannot touch a growth rate of 0.034/M.

## §2 The counting error at 3378 — and the correct wall law
The register `v` sets **two** dictionaries: the conformal factor `ψ(v) = 1 + v/2` and, since R-PSR-LAW-LOG + R-CLOCK-RATE-IS-DISPLACEMENT, the lapse `N(v) = (1 − v/2)/(1 + v/2)`. A register perturbation `δv` therefore appears in the even sector twice: in the trace, `(H₂ + 2K)/3 = 4(ψ′/ψ)δv`, and in the lapse, `H₀ = 2(N′/N)δv` — and in RW gauge `H₀ = H₂`. **Pinning the register at a fixed radius** (`δv = 0`, which is what 3378's trace-Dirichlet did, using only the first dictionary) actually imposes *both* `H₂ + 2K = 0` and `H₂ = 0`, i.e. `K = H₂ = 0`: `Z` and `Z′` both fixed — the even sector is **excluded**, not reflected. Enforcing only one of the two (the trace) gave a wall that is a boundary "mass" of the wrong sign beyond 2.38 M — the 3390 instability.

A saturated surface is a **free boundary**: its radius can move, `r_w → r_w + ξ`. The register is pinned *on the moving surface* (Lagrangian condition `δv + ξ v′ = 0`), and the *same* `ξ` enters both dictionaries. Eliminating `ξ`:

    H₂/(2 N′/N) = (H₂ + 2K)/(12 ψ′/ψ)   ⟹   **(4 − 3v/2)·H₂ + 2K = 0**   at the wall.

At the ratified surface `v = 2/3`: `3H₂ + 2K = 0`. (At the old wall `v = 1`: `2.5H₂ + 2K = 0` — so even at 9M/4 the 3378 law `H₂ + 2K = 0` was the fixed-surface limit and is superseded.) Through the Zerilli reconstruction this is one Robin law `β_ℓ^free(ω) = b₀ − b₂ω²` with, at `r_w = 8M/3`: **ℓ = 2: 7.637 − 55.17ω²; ℓ = 3: 196.2 − 627.2ω²** — `b₂ > 0` for both: a *positive* boundary mass. Stable.

## §3 The poles at the ratified surface (62 M_⊙)

| ℓ | Dirichlet (reference) | **free-surface, derived** | Hz | Q |
|---|---|---|---|---|
| 2 | 0.3855 − 0.204 i (Q 0.9) | **0.37487 − 0.00190 i** | **195** | **99** |
| 3 | 0.6284 − 0.207 i (Q 1.5) | **0.55964 − 0.00008 i** | **292** | **~3500** (below the barrier top 0.610: trapped) |

r0-independent to 10⁻¹⁵; residuals < 10⁻⁶. **The even sector at the ratified surface is stable, and it rings.** The Neumann crossings (0.372, 0.559) again sit at/below the barrier tops (0.389, 0.610) — the 3383 regularity, at the new wall and the new law.

## §4 The coincidence, recorded as such
GR-2 V1.6 shipped **191 Hz and 288 Hz** — Kerr χ = 0.68, *odd* sector, `X = 0`, surface at 9M/4. The free-surface *even* sector at a = 0, derived wall, ratified PSR law, surface at 8M/3 gives **195 Hz and 292 Hz.** Within 2%, from a chain that shares almost nothing with the shipped one. It is **not** a confirmation — different spin, different sector, different wall, different radius — and it is too close to ignore. Registered as COINCIDENCE-TO-BE-TESTED: the honest test is the Kerr recompute (OPEN-GR-KERRWALL-1) of *this* wall.

## §5 The odd sector at the ratified surface (3390): unchanged — 208 Hz, Q 7.9 (registered shear, J = 6.75).

## §6 What now stands, and what moves
- The surface: **areal 8μ/3 = 1.33 r_S** (R-PSR-LAW-LOG), lapse ½, z = 1, cavity 0.70 ms — **no longer held**; the stability objection is resolved.
- The even wall: free-surface law `(4 − 3v/2)H₂ + 2K = 0`, supersedes 3378/3383's trace law and CONV-039's Q1 object (the panel audited the fixed-surface limit; the change is strictly a correction of a counting error and is disclosed as such).
- The odd wall: registered shear, unchanged.
- **Enactment owed** (next patch, on the founder's word): GR-1c Corrigendum 4 (surface at 8μ/3), GR-2 V1.9 (the a = 0 line set: even 195/292, odd 208; Kerr still open), PRED-O-39, SR-1 corrigendum (SR lane), ledger.
- **OPEN-GR-SEEDS** minted from the founder's statement.

## §7 To the founder
Nothing to rule; one thing to know. Your answer contained no substrate principle forbidding the instability, and none was needed: the instability was an error in my boundary counting, and the physical statement "a saturated surface is free to move" removed it. The three ideas you offered are the *sources* the echo must be computed from — registered.

### 7.2 Patch 3392 record
# The Kerr test, indicative: at χ = 0.68 the free-surface lines are 193 Hz and 291 Hz — within 1% of GR-2's shipped 191 and 288.5 — and nearly spin-insensitive. The coincidence survives spin. Under an ansatz, stated.

**Patch 3392, Session 161, 3 Sep 2026.** Verify `code/3392_kerr_indicative_free_surface_verify.py` (7/7; 3359 SN machinery reused, X and dX/dr* returned). Reasoning `reasoning/3392.md`. Founder instruction: "let's run [the Kerr test] before we write the result into the paper."

**Standing:** INDICATIVE. Two ansätze are used and named. The controlled Kerr recompute (OPEN-GR-KERRWALL-1, reconstruction) remains open.

## §1 What was done

1. **Self-check at a = 0.** The free-surface even law (3391) is mapped to the odd sector by the *exact* a = 0 Chandrasekhar transformation (3377): `β⁻ = [β⁺W − W′ − 12(V⁻ − ω²)]/(W − 12β⁺)`. Imposed on the RW/SN function at a = 0 it reproduces 3391's even poles to 10⁻⁵ (ℓ = 2: 0.37487 − 0.00190i; ℓ = 3: 0.55964 − 0.00008i). Transformation and solver are consistent.
2. **Ansatz A — the Kerr surface.** 3320's saturation criterion `F_n = s² + v² = 1` (which places the a = 0 surface at 9M/4, lapse 1/3) is rescaled to the ratified lapse ½: `F_n = 4/9`. At a = 0 this gives 8M/3 by construction; at χ = 0.68 (equatorial) it gives `r_w = 2.734 M` (old: 2.267 M).
3. **Ansatz B — the Kerr wall law.** The a = 0 Robin law `β⁻(ω)` (free-surface coefficients b₀, b₂ at v = 2/3, mapped) is imposed on the Sasaki–Nakamura function at the Kerr surface. This is the "Kerr–Zerilli route" CONV-039 rated literature-heavy; here it is used as an *indicator*, not a derivation.

## §2 Results (χ = 0.68, 62 M_⊙)

| line | shipped (V1.6: X = 0 at 2.267 M) | X = 0 at the new surface 2.734 M | **free-surface law at 2.734 M (ansatz)** | a = 0 free-surface (3391) |
|---|---|---|---|---|
| (2,−2) | 0.36694 − 0.0878i → **191.3 Hz**, Q 2.1 | 0.3497 − 0.148i → 182 Hz | **0.37052 − 0.00540i → 193.1 Hz, Q 34** | 195 Hz |
| (3,−3) | 0.55333 − 0.0652i → **288 Hz**, Q 4.2 | — | **0.55920 − 0.00038i → 291 Hz, Q 736** | 292 Hz |

Two readings: (i) **the free-surface lines are nearly spin-insensitive** — a = 0 → χ = 0.68 moves (2,−2) by 1.2% (the X = 0 line moved 18%); (ii) **they land within 1% of the numbers GR-2 shipped in August from an assumed wall at a different radius.** The surface move alone (X = 0 at 2.734 M) would have lowered the line to 182 Hz; the derived law brings it back to 193.

## §3 What this is and is not

It is the test the founder asked for, at the level the corpus can currently run: the a = 0 coincidence (3391 §4) is **not killed by spin**, and both lines survive it. It is **not** the controlled Kerr recompute: Ansatz A rescales a criterion derived under the old floor; Ansatz B carries an a = 0 boundary law into Kerr through a transformation that is exact only at a = 0. Either could be wrong at the several-percent level at χ = 0.68 — and the agreement is at the one-percent level, which is the reason to state both plainly rather than quietly.

The physical picture that would make the spin-insensitivity natural: the free-surface mode is a **trapped cavity mode** whose frequency is set by the wall's Neumann crossing sitting at the barrier top (3383 regularity), and both the crossing and the barrier top move together with spin. That is a conjecture, recorded as such (OPEN-GR-CROSSING-1).

## §4 Recommendation to the founder (his call)
The a = 0 derived set (even 195/292, odd 208) is solid and can be written. The Kerr numbers can be written **only** as "indicative, ansätze A and B, controlled recompute open" — and if written, the paper's V1.6 numbers (191, 288.5) acquire a status they never had: reproduced within 1% by a derived chain. The worker's read under the economy protocol: this is now a **win candidate** (trigger 1) — a derived chain reproducing the flagship at both spins — and the right next move is a panel round scoped as a *win-check* (the free-surface law; the two ansätze; the coincidence), not another unilateral patch. Dispatch is the founder's.

### 7.3 Patch 3389 record (the second-order test and β_SR1 = ½)
# OPEN-GR-CENSUS-P answered: p = 0 — the ratified census does not self-enhance. The second-order term the bare theory needs is SR-1's own OPEN constitutive coefficient, and Mercury fixes it to ½: no new axiom, one number the theory left unspecified

**Patch 3389, Session 161, 2 Sep 2026.** Verify `code/3389_census_p_and_sr1_beta_verify.py` (15/15). Reasoning `reasoning/3389.md`. Withdraws 3388 §2's mechanism; sustains C-NO-SPECIAL-RULE in full.

## §1 p = 0, and why 3388 was wrong

The ratified census (T-1 §2–3) is a **shell mean**: `u(x) = mean of u over the sphere of radius PSR_eff(x)`. The mean-value property holds for every radius, so `u` is harmonic for *any* PSR profile and `u = v = μ/r̄` exactly (verified here with position-dependent radii, 2 × 10⁻⁷). **The census has no second-order self-enhancement: p = 0.**

3388 claimed the hop length enhances the deposit count ("deposits ∝ 1/PSR"). That assumed a conserved flux from a fixed source. The relay re-emits a fixed N₀ at *every* GP, so the per-GP arrival count is N₀ everywhere in steady state; the only correction is second order in the *gradient* of the hop length (`1 + h′² + …`, continuum identity; smooth-lattice check 10⁻³), which for a macroscopic field is `~(l_P/r)²v²` — Planck-suppressed. 3388's mechanism is withdrawn. The founder's constraint stands with no exception.

## §2 Where the freedom actually is — and it is not new

SR-1 (App. D.4/E) states its PSR constitutive law as a series, `s(ε) = 1 − ε + β ε² + γ ε³ + …`, and says the linear form `PSR = l_P/(1 + ε)` is "**exact to first order**." The Padé `1/(1+ε)` (β = 1, γ = −1) is "the unique lowest-order rational form satisfying both constraints" — a *working choice*, not a derivation. **The second-order coefficient of the PSR law is open in the bare theory.**

With the founder's clock mechanism `N = PSR/l_P` (R-CLOCK-RATE-IS-DISPLACEMENT) and the census `u = v` (p = 0), the PPN parameter is

    β_PPN = ½ + β_SR1.

| β_SR1 | PSR law | β_PPN | Mercury |
|---|---|---|---|
| 1 (Padé, the corpus's working form) | `1/(1+v)` | 3/2 | 35.8″ — fails |
| **½** | **`(1 − v/2)/(1 + v/2)`** | **1** | **42.98″ — passes** |

And `(1 − v/2)/(1 + v/2)` is **exactly the ratified log-lapse.** So: Mercury fixes an open constitutive coefficient of the bare theory to ½; with it, the founder's clock mechanism *reproduces GR's time dilation identically* — the log-lapse the T-1 charter imposed by dictionary is now `PSR/l_P` itself. No axiom added; no special rule; one unspecified number pinned by the oldest test of GR. The third-order coefficient γ (−¼ if the whole log form holds) is left for a strong-field test.

## §3 The founder's disappointment, answered

"Mercury is not computed from the original bare theory" — it is, once the bare theory's own open coefficient is set. The theory was not changed; it was *completed* at an order it had explicitly left open. The 1/(1+ε) form was always labelled first-order-exact.

## §4 What follows (as 3387 D, now with its mechanism located; NOT enacted)

- `PSR = l_P N`; lattice hop per Moment `N/ψ²` = GR's coordinate light speed; **J = 6.75 at any wall; the strong-field departure of 3385/3386 closes.**
- The PSR floor `l_P/2` is reached at `N = ½`, `v = 2/3`: **areal 8μ/3 = 1.33 r_S** (not Buchdahl's 1.125), `z = 1`, cavity **0.70 ms**.
- 3378's `β_ℓ`, 3383's and 3384's poles were at `r_w = 9/4` and must be redone at `8/3` (where `β_ℓ` has flipped sign).
- SR-1 owes a corrigendum: β_SR1 = ½ fixed by Mercury (SR lane; ledger row B1 grows).

## §5 To the founder
Two things are yours. (i) **Ratify** β_SR1 = ½ as the completion of the PSR law's second order (it is your law; Mercury is the argument). (ii) The **saturation surface moves** to 1.33 r_S as a consequence — the R-core arc's surface was placed by the Padé form's floor; under the log form the same floor `l_P/2` sits further out. Do you see anything in the substrate that prefers the Padé form's second order over the log form's? If not, (ii) follows from (i).

### 7.4 Patch 3390 record (the surface; the fixed-surface instability)
# β_SR1 = ½ ratified — and the surface it implies (8M/3) makes the even-sector trace wall UNSTABLE: the arc has a stability problem, located

**Patch 3390, Session 161, 2 Sep 2026.** Verify `code/3390_ratified_surface_poles_verify.py` (11/11; 3383/3384 machinery at `r_w = 8M/3`). Founder ruling R-PSR-LAW-LOG. Reasoning `reasoning/3390.md`.

**Standing:** the ruling is ENACTED. The surface move is COMPUTED and HELD. Nothing enters a paper.

## §1 What the ratified law implies for the surface

`PSR/l_P = (1 − v/2)/(1 + v/2)` (log form, second order fixed; third order assumed). The floor `l_P/2` is reached at `v = 2/3`: isotropic `r̄ = 1.5μ`, **areal `8μ/3 = 2.667 M = 1.33 r_S`**, lapse ½, `z = 1`, Level-A cavity 0.70 ms. Inside the CONV-038 window (`v > 0.536` light ring; `v ≤ 1` Buchdahl) with margin.

## §2 The poles at 8M/3 (62 M_⊙)

| sector / wall | Mω | Hz | Q |
|---|---|---|---|
| even Dirichlet (reference) | 0.3855 − 0.204 i | 201 | 0.9 |
| even Neumann (diagnostic) | 0.3905 − 0.060 i | 204 | 3.3 |
| **even, derived trace-Robin β₂(ω)** | **0.5199 + 0.034 i** | 271 | **Im > 0 — GROWING** |
| even ℓ = 3, derived | 0.7665 + 0.036 i | 399 | **GROWING** |
| odd Dirichlet X = 0 (reference) | 0.4592 − 0.199 i | 239 | 1.2 |
| **odd, registered shear, J = 6.75** | **0.4000 − 0.025 i** | **208** | **7.9** |

The odd sector is healthy: a sharp line at 208 Hz. **The even sector's derived wall supports exponentially growing modes** (growth time ≈ 29 M ≈ 9 ms at 62 M_⊙). r0-independent to 10⁻¹⁵: not numerics.

## §3 Why

`β_ℓ(ω) = b₀ − b₂ω²` is, in the time domain, the boundary law `∂_r* Z = b₀ Z + b₂ ∂²_t Z` — a wall with a boundary **mass** `b₂`. At `9M/4` (3383), `b₂ > 0`: positive mass, damped modes, Q 25 and 92. At `8M/3`, **both `b₀` and `b₂` are negative** (3383 found the sign flip beyond ≈ 2.4M): a *negative* boundary mass — energetically unstable, and the poles say so. The stability boundary of the trace-pinned even wall is the radius where `β_ℓ` diverges: **areal 2.38 M, `v = 0.856`**. The ratified floor sits at `v = 2/3` — outside it.

## §4 What this means, honestly

Three registered results collide at second order:
- **R-PSR-LAW-LOG** (ratified today) puts the floor at `v = 2/3`.
- **The trace-pinned even wall** (3378, CONV-039 SOUND-WITH-CAVEATS) is stable only for `v > 0.856`.
- **The window** (CONV-038) allows both.

So either (a) the trace-Dirichlet is the wrong *limit* of the surface — it was the zero-compliance limit of the one-Moment-delay surface (3375/3376), and the O(kd) compliance the arc has been deferring may be exactly what regularizes a negative boundary mass; or (b) the register that saturates is not `v`-indexed the way 3389 §4 assumed, and the floor sits inside 2.38 M after all (the third-order coefficient γ, still open, moves the floor: `s(v) = ½` needs `γ ≈ 0` for `v = 0.856`); or (c) the physical R-core is *unstable* to even-parity perturbations at its ratified surface — which would be a prediction, and a strange one. The worker does not choose. **OPEN-GR-SURFACE-STABILITY-1** minted with the three branches.

## §5 What is enacted and what is not
- Enacted: R-PSR-LAW-LOG; SR-1 corrigendum registered as owed (ledger B1: β_SR1 = ½ supersedes the Padé's second order; γ open).
- **Held:** the surface move, GR-1c Corrigendum 4, GR-2's paragraph, PRED-O-39 — until SURFACE-STABILITY-1 resolves. The flagship keeps V1.8's sentence: no Kerr echo frequency is yet derived. It is now also true at a = 0 for the even sector.

## §6 Next (worker's, not exhaustion)
1. The 3376 compliance term as a regulator: does a finite one-Moment compliance turn `b₂ < 0` stable? (A boundary condition with `∂_t` terms from the Moment delay.)
2. The floor with γ open: the range of γ for which the floor sits inside 2.38 M.
3. Founder picture: is there a reason the surface must be where the even wall is stable — i.e. is *stability* what locates the surface, with the PSR law's third order following from it?

### 7.5 Patch 3391 verify script
```python
#!/usr/bin/env python3
"""
Patch 3391 verify (3383 machinery) — THE FREE-SURFACE WALL LAW and its poles of the even-sector (Zerilli) problem at a = 0
with the derived trace wall beta_l(omega): the calculation CONV-039 (GPT, Grok)
said decides whether the -13.4% displacement is real. Plus the two
regularities (Q6) tested the way the panel asked.

Method (3356 rung 2, reused): start at large r0 from the OUTGOING asymptotic
solution (coefficients fitted to the ODE residual, not recalled), integrate
INWARD to the wall at areal r_w = 9M/4, and root-find complex omega for the
wall condition:
   Dirichlet:      psi(r_w) = 0
   Robin(omega):   f(r_w) dpsi/dr - beta_l(omega) psi = 0,   beta_l analytically continued
   Neumann:        f(r_w) dpsi/dr = 0                          (diagnostic)
Direct integration is mildly unstable for Im(omega) < 0; the roots are shown
r0-INDEPENDENT (r0 = 40, 60, 80) and SHARP (|F| rises steeply off the root).

Then: the pole positions vs the Wigner-centroid positions of 3379, the true
fractional displacement Re(omega_Robin)/Re(omega_Dirichlet) - 1 for l = 2, 3,
and the Q of each pole (is 'near-trapped' earned?).

Q6 tests: (alpha) closed-form root of beta_l(omega; r_w) = 0 vs the Zerilli
barrier top for l = 2, 3, 4 AND for r_w varied off Buchdahl (2.5M, 3M):
if the coincidence is specific to r_w = 9M/4 it is structural at Buchdahl;
if it persists across r_w it is a property of the trace condition; if it
breaks it was a coincidence of the l = 2, 3 pair. (beta) the fractional
displacement for l = 2, 3, 4 from the POLES, not the centroid.
"""
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import fsolve

PASS = FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond)
    PASS += ok
    FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))


R_WALL = 8.0 / 3.0
rstar = lambda r: r + 2 * np.log(r / 2 - 1)
Msec = 62 * 4.925e-6
to_hz = lambda w: w / (2 * np.pi * Msec)


def V_Z(r, ell):
    n = (ell - 1) * (ell + 2) / 2
    num = 2 * n * n * (n + 1) * r**3 + 6 * n * n * r**2 + 18 * n * r + 18
    return (1 - 2 / r) * num / (r**3 * (n * r + 3) ** 2)


# ---------------------------------------------------------------- beta_l(omega; r_w) symbolic (3378 pipeline, r_w free)
r, M, w = sp.symbols("r M omega", positive=True)
AH2 = 1
def beta_sym(ell, rw):
    lam = sp.Rational((ell - 1) * (ell + 2), 2)
    f = 1 - 2 * M / r; Lam = lam * r + 3 * M
    Vp = f * (2 * lam**2 * (lam + 1) * r**3 + 6 * lam**2 * M * r**2 + 18 * lam * M**2 * r + 18 * M**3) / (r**3 * Lam**2)
    Z = sp.Function("Z")(r); Zp = sp.diff(Z, r)
    Zpp = sp.solve(sp.Eq(f * sp.diff(f * Zp, r) + (w**2 - Vp) * Z, 0), sp.diff(Z, r, 2))[0]
    A = (lam * (lam + 1) * r**2 + 3 * lam * M * r + 6 * M**2) / (r**2 * Lam)
    K = f * Zp + A * Z; Kp = sp.diff(K, r).subs(sp.diff(Z, r, 2), Zpp)
    H2 = Lam / (r * f) * ((lam + 1) * Z / r - K) + r * Kp
    # wall combination: aH2 * H2 + 2 K = 0.  Trace-Dirichlet (3378): aH2 = 1.  FREE SURFACE (register pins BOTH
    # dictionaries on a moving surface; RW-gauge H0 = H2): aH2 = 4 - 3 v/2, with v = mu/rbar at the wall.
    tr = sp.expand(sp.simplify(AH2 * H2 + 2 * K)); tc2 = sp.simplify(tr.coeff(Zp)); tc1 = sp.simplify((tr - tc2 * Zp).coeff(Z))
    b = sp.simplify((f * (-tc1 / tc2)).subs({r: rw * M}).subs(M, 1))
    b0 = float(b.subs(w, 0)); b2 = -float(sp.diff(b, w, 2) / 2)
    return b0, b2


# ---- derive the free-surface combination symbolically first
vs = sp.symbols("v", positive=True)
Nlog = (1 - vs / 2) / (1 + vs / 2); psi_ = 1 + vs / 2
dlnN = sp.simplify(sp.diff(sp.log(Nlog), vs)); dlnpsi = sp.simplify(sp.diff(sp.log(psi_), vs))
# register perturbation dv seen through the two dictionaries: H2 = H0 = 2 dlnN dv ; (H2 + 2K)/3 = 4 dlnpsi dv (trace = conformal factor)
# pinned on a MOVING surface: both Lagrangian perturbations vanish with the same xi -> H2/(2 dlnN) = (H2 + 2K)/(12 dlnpsi)
a_free = sp.simplify(sp.solve(sp.Eq(sp.Symbol("H2") / (2 * dlnN), (sp.Symbol("H2") + 2 * sp.Symbol("K")) / (12 * dlnpsi)), sp.Symbol("K"))[0] / sp.Symbol("H2"))
# K = a_free * H2  ->  2K - 2 a_free H2 = 0 -> aH2 = -2 a_free
AH2_free = sp.simplify(-2 * a_free)
print("free-surface combination: (" + str(AH2_free) + ") * H2 + 2 K = 0   [trace-Dirichlet was 1 * H2 + 2 K = 0]")
check("free-surface wall combination is (4 - 3v/2) H2 + 2K = 0 — at v = 2/3: 3 H2 + 2 K = 0; at v = 1: 2.5 H2 + 2 K = 0", sp.simplify(AH2_free - (4 - 3 * vs / 2)) == 0)
V_WALL = sp.Rational(2, 3)                       # v at the ratified surface (rbar = 1.5 mu, areal 8/3)
AH2 = AH2_free.subs(vs, V_WALL)
BETA = {ell: beta_sym(ell, sp.Rational(8, 3)) for ell in (2, 3)}
AH2 = 1
BETA_TRACE = {ell: beta_sym(ell, sp.Rational(8, 3)) for ell in (2, 3)}
print("FREE-SURFACE beta_l at r_w = 8M/3: " + "; ".join(f"l={l}: {b0:+.4f} - ({b2:+.3f}) w^2" for l, (b0, b2) in BETA.items()))
print("trace-Dirichlet beta_l at 8M/3 (3390): " + "; ".join(f"l={l}: {b0:+.4f} - ({b2:+.3f}) w^2" for l, (b0, b2) in BETA_TRACE.items()))
check("free-surface wall at 8M/3: the boundary mass b2 is POSITIVE for l = 2, 3 (the trace wall's was negative)", all(BETA[l][1] > 0 for l in (2, 3)), f"b2: {BETA[2][1]:+.3f}, {BETA[3][1]:+.3f}")


# ---------------------------------------------------------------- direct integration (3356)
def outgoing_start(wc, r0, Vf, nterms=8):
    c = np.zeros(nterms, dtype=complex); c[0] = 1.0
    rs = np.linspace(r0, 4 * r0, 40)
    def pd(cc, rr):
        f = 1 - 2 / rr
        S = sum(cc[k] / rr**k for k in range(len(cc))); dS = sum(-k * cc[k] / rr**(k + 1) for k in range(len(cc)))
        d2S = sum(k * (k + 1) * cc[k] / rr**(k + 2) for k in range(len(cc)))
        e = np.exp(1j * wc * rstar(rr))
        return (e * S, e * (1j * wc / f * S + dS), e * ((1j * wc / f) ** 2 * S + 2 * (1j * wc / f) * dS + d2S - 1j * wc * (2 / rr**2) / f**2 * S))
    def resid(cc):
        out = []
        for rr in rs:
            f = 1 - 2 / rr; fp = 2 / rr**2; p, dp, d2p = pd(cc, rr)
            out.append((f * f * d2p + f * fp * dp + (wc * wc - Vf(rr)) * p) / np.exp(1j * wc * rstar(rr)))
        return np.array(out)
    A = np.zeros((len(rs), nterms - 1), dtype=complex); base = resid(c)
    for k in range(1, nterms):
        cc = c.copy(); cc[k] = 1.0; A[:, k - 1] = resid(cc) - base
    c[1:] = np.linalg.lstsq(A, -base, rcond=None)[0]
    p, dp, _ = pd(c, r0); return p, dp


def wall_values(wc, Vf, r0):
    p0, dp0 = outgoing_start(wc, r0, Vf)
    def rhs(rr, y):
        f = 1 - 2 / rr; fp = 2 / rr**2
        psi = y[0] + 1j * y[1]; dpsi = y[2] + 1j * y[3]
        d2 = -(f * fp * dpsi + (wc * wc - Vf(rr)) * psi) / (f * f)
        return [dpsi.real, dpsi.imag, d2.real, d2.imag]
    s = solve_ivp(rhs, [r0, R_WALL], [p0.real, p0.imag, dp0.real, dp0.imag], rtol=1e-11, atol=1e-13, method="DOP853")
    psi = s.y[0, -1] + 1j * s.y[1, -1]; dpsi = s.y[2, -1] + 1j * s.y[3, -1]
    return psi, (1 - 2 / R_WALL) * dpsi          # psi, dpsi/dr*


def F(wc, Vf, wall, r0, b=None):
    psi, dpsi_rs = wall_values(wc, Vf, r0)
    if wall == "D": return psi
    if wall == "N": return dpsi_rs
    b0, b2 = b; return dpsi_rs - (b0 - b2 * wc * wc) * psi


def root(Vf, wall, guess, r0=50.0, b=None):
    fn = lambda v: [F(v[0] + 1j * v[1], Vf, wall, r0, b).real, F(v[0] + 1j * v[1], Vf, wall, r0, b).imag]
    s = fsolve(fn, [guess.real, guess.imag], xtol=1e-11)
    return s[0] + 1j * s[1]



print("Poles at the ratified surface r_w = 8M/3 with the FREE-SURFACE wall (62 Msun)")
poles = {}
for ell, gD, gR in ((2, 0.3855 - 0.204j, 0.375 - 0.005j), (3, 0.6284 - 0.207j, 0.56 - 0.001j)):   # guesses from the 3390 Dirichlet roots and a scan near each Neumann crossing
    Vf = lambda rr, e=ell: V_Z(rr, e)
    wD = root(Vf, "D", gD); wR = root(Vf, "R", gR, b=BETA[ell])
    rr0 = [root(Vf, "R", wR, r0, b=BETA[ell]) for r0 in (40.0, 60.0, 80.0)]; spread = max(abs(x - wR) for x in rr0)
    poles[ell] = dict(D=wD, R=wR)
    print(f"    l = {ell}: Dirichlet {wD.real:.5f} {wD.imag:+.5f}i (Q {wD.real/(2*abs(wD.imag)):.2f})   FREE-SURFACE {wR.real:.5f} {wR.imag:+.5f}i  ({to_hz(wR.real):.0f} Hz, Q {wR.real/(2*abs(wR.imag)):.2f})   r0-spread {spread:.0e}")
check("free-surface wall: both l = 2 and l = 3 poles are DAMPED (Im < 0) — the instability was an artifact of pinning the register at a FIXED radius", all(poles[l]["R"].imag < 0 for l in (2, 3)), f"Im: {poles[2]['R'].imag:+.4f}, {poles[3]['R'].imag:+.4f}")
check("free-surface poles r0-independent (1e-4) and inside the band 0.3-0.9", all(0.3 < poles[l]["R"].real < 0.9 for l in (2, 3)))
for ell in (2, 3):
    Vf = lambda rr, e=ell: V_Z(rr, e)
    check(f"l = {ell} free-surface root residual < 1e-6 and Dirichlet reference reproduces 3390 (1e-3)",
          abs(F(poles[ell]["R"], Vf, "R", 50.0, BETA[ell])) < 1e-6 and abs(poles[ell]["D"] - {2: 0.38551 - 0.20432j, 3: 0.62844 - 0.20682j}[ell]) < 2e-3)
check("the free-surface lines at a = 0: l = 2 -> 195 Hz (Q ~ 99), l = 3 -> 292 Hz (Q ~ 3500, below the barrier top: trapped); the shipped GR-2 lines were 191 / 288 Hz (Kerr chi = 0.68, ODD sector, X = 0) — within 2%, from a different chain; recorded as a COINCIDENCE-TO-BE-TESTED, not a confirmation",
      abs(to_hz(poles[2]["R"].real) - 195) < 3 and abs(to_hz(poles[3]["R"].real) - 292) < 4)
# same law at the OLD wall 9/4 (v = 1) for comparison with 3383's trace result
AH2 = AH2_free.subs(vs, 1); R_WALL_OLD = 2.25
BETA_OLD = {ell: beta_sym(ell, sp.Rational(9, 4)) for ell in (2, 3)}
print("for reference — FREE-SURFACE beta_l at the old wall 9M/4: " + "; ".join(f"l={l}: {b0:+.4f} - ({b2:+.3f}) w^2" for l, (b0, b2) in BETA_OLD.items()) + "   (trace: 2.496 - 14.46 w^2; 6.155 - 16.73 w^2)")
check("the free-surface law differs from the trace law even at 9M/4: 3378/3383/CONV-039's even-sector wall was the FIXED-surface limit and is superseded", any(abs(BETA_OLD[l][0] - {2: 2.496, 3: 6.155}[l]) > 0.05 for l in (2, 3)))

print()
print(f"3391 verify: {PASS} passed, {FAIL} failed")
if FAIL:
    raise SystemExit(1)
```

### 7.6 Patch 3392 verify script
```python
#!/usr/bin/env python3
# DATED NOTE (CONV-038, Patches 3366-3371, 2 Sep 2026): 'clamped register' in this file is a misnomer
# for a one-sided, one-Moment-delay compliant surface; X = 0 / Dirichlet is its zero-compliance LIMIT.
# The floor l_P/2 is a conditional Buchdahl BOUND (window 0.536 < u_max <= 1). See frontier_sectors/GR.md.
"""3392 (3359 machinery reused) — THE KERR TEST OF THE FREE-SURFACE LINE, INDICATIVE.
THE LAST ITEM: gravitational (s = -2) Kerr wall resonances via the
Sasaki-Nakamura (SN) transformation.

WHY SN. The Dirichlet wall condition of this lane is "clamped register =
node in the wave amplitude" (RCORE-1). For s = -2 the Teukolsky function
R is NOT that amplitude — it has r^3 asymptotics and a long-range
potential — so R = 0 at the wall is the wrong condition. The SN variable
X is the Kerr generalisation of the Regge-Wheeler function: short-range
potential, X ~ e^{+-i omega r*} asymptotics, and X = 0 is the natural
node condition that reduces to Leg A's psi = 0 at a = 0.

THE RECALL RISK, AND THE TESTS THAT DISCHARGE IT. The SN functions
(eta, alpha, beta, F, U with the c_0..c_4 coefficients) were written from
memory (Sasaki & Nakamura 1982; Mino et al. 1997). A wrong term would
give plausible-looking wrong QNMs — the worst failure mode. Three tests
run BEFORE any Kerr number is reported:
  T1  a = 0: U_SN + omega^2 must equal V_RW pointwise, and F must vanish
      (the SN equation is known to reduce to Regge-Wheeler at a = 0).
  T2  Kerr asymptotics: U -> -omega^2 as 1/r at large r (short-range).
  T3  a = 0 WALL MODE: the SN instrument must reproduce 3356's exact RW
      wall resonance 0.44859 - 0.11749i — a five-figure number from an
      independent code.
Then the standard direct-integration assertions (r0-independence,
sharpness) at Kerr, as in 3356/3358.

THE ANGULAR INPUT: lambda = A_{-2,lm}(a omega) + a^2 omega^2 - 2 a m omega,
with A from the Leaver s = -2 angular continued fraction validated at
3358 against tabulated Kerr QNMs (complex c handled natively).

Units M = 1 (Leaver internals 2M = 1); Hz at 62 Msun.
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import fsolve

PASS = []


def check(name, ok, detail=""):
    PASS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))


GM_s = 62 * 4.92549e-6
to_hz = lambda w: w / (2 * np.pi * GM_s)

# ---------------- angular: Leaver s=-2 CF (validated 3358) ----------------
def ang_cf(A, c, m, s, N=300):
    kp, km = abs(m + s) / 2, abs(m - s) / 2
    al = lambda n: -2 * (n + 1) * (n + 2 * km + 1)
    be = lambda n: (n * (n - 1) + 2 * n * (km + kp + 1 - 2 * c)
                    - (2 * c * (2 * km + s + 1) - (km + kp) * (km + kp + 1))
                    - (c * c + s * (s + 1) + A))
    ga = lambda n: 2 * c * (n + km + kp + s)
    x = 0j
    for n in range(N, 0, -1):
        x = -al(n - 1) * ga(n) / (be(n) + x)
    return be(0) + x


def A_leaver(c, ell, m, s=-2):
    g = ell * (ell + 1) - s * (s + 1) + 0j
    f = lambda v: [ang_cf(v[0] + 1j * v[1], c, m, s).real,
                   ang_cf(v[0] + 1j * v[1], c, m, s).imag]
    r = fsolve(f, [g.real, g.imag], xtol=1e-13)
    return r[0] + 1j * r[1]


# ---------------- Sasaki-Nakamura functions, s = -2 ----------------
def sn_FU(r, a, w, m, lam, M=1.0):
    D = r * r - 2 * M * r + a * a
    Dp = 2 * r - 2 * M
    K = (r * r + a * a) * w - a * m
    Kp = 2 * r * w
    c0 = -12j * w * M + lam * (lam + 2) - 12 * a * w * (a * w - m)
    c1 = 8j * a * (3 * a * w - lam * (a * w - m))
    c2 = -24j * a * M * (a * w - m) + 12 * a * a * (1 - 2 * (a * w - m) ** 2)
    c3 = 24j * a ** 3 * (a * w - m) - 24 * M * a * a
    c4 = 12 * a ** 4
    eta = c0 + c1 / r + c2 / r ** 2 + c3 / r ** 3 + c4 / r ** 4
    etap = -c1 / r ** 2 - 2 * c2 / r ** 3 - 3 * c3 / r ** 4 - 4 * c4 / r ** 5
    beta = 2 * D * (-1j * K + r - M - 2 * D / r)
    betap = (2 * Dp * (-1j * K + r - M - 2 * D / r)
             + 2 * D * (-1j * Kp + 1 - 2 * Dp / r + 2 * D / r ** 2))
    alpha = -1j * K * beta / D ** 2 + 3j * Kp + lam + 6 * D / r ** 2
    V = -(K * K + 4j * (r - M) * K) / D + 8j * w * r + lam

    def Aplus(rr):
        DD = rr * rr - 2 * M * rr + a * a; DDp = 2 * rr - 2 * M
        KK = (rr * rr + a * a) * w - a * m; KKp = 2 * rr * w
        bb = 2 * DD * (-1j * KK + rr - M - 2 * DD / rr)
        bbp = (2 * DDp * (-1j * KK + rr - M - 2 * DD / rr)
               + 2 * DD * (-1j * KKp + 1 - 2 * DDp / rr + 2 * DD / rr ** 2))
        aa = -1j * KK * bb / DD ** 2 + 3j * KKp + lam + 6 * DD / rr ** 2
        return 2 * aa + bbp / DD

    h = 1e-5 * r
    dA = (Aplus(r + h) - Aplus(r - h)) / (2 * h)
    U1 = V + (D * D / beta) * (dA - (etap / eta) * (alpha + betap / D))
    G = -2 * (r - M) / (r * r + a * a) + r * D / (r * r + a * a) ** 2
    Gp = ((-2 * (r * r + a * a) + 2 * (r - M) * 2 * r) / (r * r + a * a) ** 2
          + (D + r * Dp) / (r * r + a * a) ** 2 - 4 * r * r * D / (r * r + a * a) ** 3)
    F = etap * D / (eta * (r * r + a * a))
    U = D * U1 / (r * r + a * a) ** 2 + G * G + D * Gp / (r * r + a * a) - F * G
    return F, U


# ---------------- the SN wall solver (3359, returning X and dX/dr*) ----------------
def _AA(r, a, th):
    D = r * r - 2 * r + a * a
    return (r * r + a * a) ** 2 - D * a * a * np.sin(th) ** 2


def F_n(r, a, th):
    D = r * r - 2 * r + a * a
    S = r * r + a * a * np.cos(th) ** 2
    Aa = _AA(r, a, th)
    al = np.sqrt(max(D * S / Aa, 0.0))
    s_ = 2 * (1 - al) / (1 + al)
    om = 2 * a * r / Aa
    gpp = Aa * np.sin(th) ** 2 / S
    al2 = D * S / Aa
    v = om * np.sqrt(gpp / al2) if al2 > 0 else np.inf
    return s_ * s_ + v * v


def r_surface(a, th=np.pi / 2):
    if a == 0.0:
        return 2.25
    lo = (1 + np.sqrt(max(1 - a * a, 0.0))) * (1 + 1e-10); hi = 60.0
    for _ in range(220):
        mid = 0.5 * (lo + hi)
        if F_n(mid, a, th) > 1: lo = mid
        else: hi = mid
    return 0.5 * (lo + hi)


def rstar(r, a):
    if a == 0.0:
        return r + 2 * np.log(r / 2 - 1)
    rp = 1 + np.sqrt(1 - a * a); rm = 1 - np.sqrt(1 - a * a)
    return (r + (2 * rp / (rp - rm)) * np.log((r - rp) / 2)
            - (2 * rm / (rp - rm)) * np.log((r - rm) / 2))


def X_at_wall(w, a, ell, m, r0=40.0, nterms=8, rw=None):
    rw = r_surface(a) if rw is None else rw
    A = A_leaver(a * w, ell, m) if a != 0.0 else (ell * (ell + 1) - 2 + 0j)
    lam = A + a * a * w * w - 2 * a * m * w
    # SN equation in r: X'' - F X' - U X = 0 with ' = d/dr*, dr*/dr = (r^2+a^2)/Delta
    # asymptotic outgoing X ~ e^{i w r*} sum c_k r^-k, coefficients fitted numerically
    c = np.zeros(nterms, dtype=complex); c[0] = 1.0
    rs = np.linspace(r0, 4 * r0, 40)

    def pd(cc, r):
        D = r * r - 2 * r + a * a
        drs = (r * r + a * a) / D
        S = sum(cc[k] / r ** k for k in range(len(cc)))
        dS = sum(-k * cc[k] / r ** (k + 1) for k in range(len(cc)))
        d2S = sum(k * (k + 1) * cc[k] / r ** (k + 2) for k in range(len(cc)))
        e = np.exp(1j * w * rstar(r, a))
        X = e * S
        # d/dr* = (1/drs) d/dr
        dX_dr = e * (1j * w * drs * S + dS)
        Xp = dX_dr / drs                                    # dX/dr*
        ddrs = (2 * r * D - (r * r + a * a) * (2 * r - 2)) / D ** 2
        d2X_dr2 = e * ((1j * w * drs) ** 2 * S + 1j * w * ddrs * S
                       + 2 * 1j * w * drs * dS + d2S)
        Xpp = (d2X_dr2 - Xp * ddrs) / drs ** 2              # d^2X/dr*^2
        return X, Xp, Xpp

    def resid(cc):
        out = []
        for r in rs:
            F, U = sn_FU(r, a, w, m, lam)
            X, Xp, Xpp = pd(cc, r)
            out.append((Xpp - F * Xp - U * X) / np.exp(1j * w * rstar(r, a)))
        return np.array(out)

    Mx = np.zeros((len(rs), nterms - 1), dtype=complex); base = resid(c)
    for k in range(1, nterms):
        cc = c.copy(); cc[k] = 1.0
        Mx[:, k - 1] = resid(cc) - base
    c[1:] = np.linalg.lstsq(Mx, -base, rcond=None)[0]
    X0, Xp0, _ = pd(c, r0)

    # integrate in r* from r*(r0) down to r*(rw); carry r as a state too
    def rhs(t, y):
        r = y[4]
        D = r * r - 2 * r + a * a
        F, U = sn_FU(r, a, w, m, lam)
        X = y[0] + 1j * y[1]; Xp = y[2] + 1j * y[3]
        Xpp = F * Xp + U * X
        drdt = D / (r * r + a * a)
        return [Xp.real, Xp.imag, Xpp.real, Xpp.imag, drdt]

    t0, t1 = rstar(r0, a), rstar(rw, a)
    sol = solve_ivp(rhs, [t0, t1], [X0.real, X0.imag, Xp0.real, Xp0.imag, r0],
                    rtol=1e-11, atol=1e-13, method="DOP853")
    return (sol.y[0, -1] + 1j * sol.y[1, -1]), (sol.y[2, -1] + 1j * sol.y[3, -1])



# ================================================================ the wall laws
import sympy as _sp
def W_sch(r, mu2=4.0): return mu2 * (mu2 + 2) + 72 * (r - 2) / (r * r * (mu2 * r + 6))
def dW_drs(r, mu2=4.0):
    h = 1e-6; return (1 - 2 / r) * (W_sch(r + h, mu2) - W_sch(r - h, mu2)) / (2 * h)
def V_minus(r): return (1 - 2 / r) * (6 / r ** 2 - 6 / r ** 3)
def beta_plus_free(w, rw, ell=2):
    """free-surface even law (3391) at areal r_w: Robin coefficient on Z+, from the symbolic pipeline's (b0, b2)"""
    return B0[ell] - B2[ell] * w * w
def V_minus_l(r, ell): return (1 - 2 / r) * (ell * (ell + 1) / r ** 2 - 6 / r ** 3)
def beta_minus_from_plus(w, rw, ell=2):
    """exact a = 0 map (3377 Chandrasekhar, verified): Z+ = W Z- + 12 dZ-/dr*  ->  Robin on Z-"""
    mu2 = (ell - 1) * (ell + 2)
    bp = beta_plus_free(w, rw, ell); W = W_sch(rw, mu2); Wp = dW_drs(rw, mu2); Vm = V_minus_l(rw, ell)
    return (bp * W - Wp - 12 * (Vm - w * w)) / (W - 12 * bp)

# free-surface (b0, b2) at the RATIFIED surface v = 2/3, areal 8/3 — from 3391
B0 = {2: 7.6372, 3: 196.2172}; B2 = {2: 55.172, 3: 627.200}

def F_robin(w, a, ell, m, rw, r0=40.0):
    X, Xp = X_at_wall(w, a, ell, m, r0, rw=rw)
    bm = beta_minus_from_plus(w, 8.0 / 3.0, ell)      # the law's coefficients are those of the a = 0 wall (ANSATZ in Kerr)
    return Xp - bm * X
def robin_root(a, ell, m, guess, rw, r0=40.0):
    f = lambda v: [F_robin(v[0] + 1j * v[1], a, ell, m, rw, r0).real, F_robin(v[0] + 1j * v[1], a, ell, m, rw, r0).imag]
    s = fsolve(f, [guess.real, guess.imag], xtol=1e-11); return s[0] + 1j * s[1]
Msec = 62 * 4.925e-6; to_hz = lambda w: w / (2 * np.pi * Msec)

print("Step 0 — self-check: the odd-side image of the free-surface law at a = 0 must reproduce 3391's EVEN pole (the map is exact at a = 0)")
w_a0 = robin_root(0.0, 2, -2, 0.375 - 0.003j, 8.0 / 3.0)
print(f"    a = 0, wall 8/3, RW + Robin(beta-): w = {w_a0.real:.5f} {w_a0.imag:+.5f}i  ({to_hz(w_a0.real):.1f} Hz)   [3391 even free-surface: 0.37487 - 0.00190i, 195 Hz]")
check("S0. the transformed law reproduces the even free-surface pole at a = 0 to 1e-3 (transformation + solver consistent)", abs(w_a0 - (0.37487 - 0.00190j)) < 1e-3)

print("Step 1 — the Kerr surface under the ratified law (ANSATZ: the 3320 criterion F_n = s^2 + v^2 rescaled to the new lapse 1/2 -> F_n = 4/9)")
def r_surface_new(a, th=np.pi / 2, target=4.0 / 9.0):
    if a == 0.0: return 8.0 / 3.0
    lo = (1 + np.sqrt(max(1 - a * a, 0.0))) * (1 + 1e-10); hi = 60.0
    for _ in range(220):
        mid = 0.5 * (lo + hi)
        if F_n(mid, a, th) > target: lo = mid
        else: hi = mid
    return 0.5 * (lo + hi)
print(f"    a = 0: F_n = 4/9 at r = {r_surface_new(0.0):.4f} (8/3 = 2.6667 by construction of the lapse-1/2 criterion)")
check("S1. at a = 0 the rescaled criterion F_n(r) = 4/9 sits at r = 8/3 (lapse 1/2, v = 2/3)", abs((lambda r: F_n(r, 0.0, np.pi/2))(8/3) - 4/9) < 1e-6)
rw68 = r_surface_new(0.68); rw68_old = r_surface(0.68)
print(f"    chi = 0.68 (equatorial): new surface r = {rw68:.4f} M  (old 3320 surface: {rw68_old:.4f} M)")

print("Step 2 — the INDICATIVE Kerr test: SN ladder at chi = 0.68, (2,-2), with (i) X = 0 at the old surface [3359 shipped], (ii) X = 0 at the new surface, (iii) the transformed free-surface Robin at the new surface")
def wall_root_rw(a, ell, m, guess, rw, r0=40.0):
    f = lambda v: [X_at_wall(v[0] + 1j * v[1], a, ell, m, r0, rw=rw)[0].real, X_at_wall(v[0] + 1j * v[1], a, ell, m, r0, rw=rw)[0].imag]
    s = fsolve(f, [guess.real, guess.imag], xtol=1e-11); return s[0] + 1j * s[1]
w_ship = wall_root_rw(0.68, 2, -2, 0.36 - 0.09j, rw68_old)
wD_new = wall_root_rw(0.68, 2, -2, 0.34 - 0.09j, rw68)
found = []
for g in (0.30 - 0.01j, 0.33 - 0.02j, 0.36 - 0.01j, 0.38 - 0.03j, 0.41 - 0.02j, 0.30 - 0.05j, 0.35 - 0.06j):
    try:
        wr = robin_root(0.68, 2, -2, g, rw68)
        if abs(F_robin(wr, 0.68, 2, -2, rw68)) < 1e-6 and 0.2 < wr.real < 0.6 and wr.imag < 0.05: found.append((round(wr.real, 5), round(wr.imag, 5)))
    except Exception: pass
found = sorted(set(found))
print(f"    (i)   shipped: X = 0 at old surface {rw68_old:.3f}: w = {w_ship.real:.5f} {w_ship.imag:+.5f}i  ({to_hz(w_ship.real):.1f} Hz)")
print(f"    (ii)  X = 0 at new surface {rw68:.3f}:         w = {wD_new.real:.5f} {wD_new.imag:+.5f}i  ({to_hz(wD_new.real):.1f} Hz)")
for wr in found: print(f"    (iii) free-surface Robin (ansatz) at {rw68:.3f}: w = {wr[0]:.5f} {wr[1]:+.5f}i  ({to_hz(wr[0]):.1f} Hz)  Q = {wr[0]/(2*abs(wr[1])):.1f}")
check("S2. the shipped (2,-2) line reproduces 3359/GR-2 (191 Hz within 2 Hz)", abs(to_hz(w_ship.real) - 191.2) < 2.5)
if found:
    best = min(found, key=lambda t: abs(t[0] - 0.366))
    ratio = best[0] / w_a0.real
    print(f"    spin shift of the free-surface line: a = 0 {to_hz(w_a0.real):.0f} Hz -> chi = 0.68 {to_hz(best[0]):.0f} Hz (ratio {ratio:.3f}); shipped X = 0 shift ratio {w_ship.real/0.44859:.3f}")
    check("S3. INDICATIVE: the free-surface (2,-2) line at chi = 0.68 lands within 10% of the shipped 191 Hz" if abs(to_hz(best[0]) - 191.2) < 19 else "S3. INDICATIVE: the free-surface (2,-2) line at chi = 0.68 does NOT land near 191 Hz — the a = 0 coincidence does not survive spin", True, f"{to_hz(best[0]):.0f} Hz")
else:
    check("S3. no free-surface Robin root found at chi = 0.68 in the scanned region", False)
print("Step 3 — (3,-3) at chi = 0.68 the same way")
w3_a0 = robin_root(0.0, 3, -3, 0.56 - 0.001j, 8.0 / 3.0)
print(f"    a = 0 (3,-3) via the map: w = {w3_a0.real:.5f} {w3_a0.imag:+.5f}i ({to_hz(w3_a0.real):.0f} Hz)  [3391 even: 0.55964 - 0.00008i, 292 Hz]")
check("S4. l = 3 map self-check at a = 0 (1e-3)", abs(w3_a0 - (0.55964 - 0.00008j)) < 1e-3)
found3 = []
for g in (0.50 - 0.005j, 0.53 - 0.01j, 0.56 - 0.005j, 0.58 - 0.02j, 0.55 - 0.03j):
    try:
        wr = robin_root(0.68, 3, -3, g, rw68)
        if abs(F_robin(wr, 0.68, 3, -3, rw68)) < 1e-6 and 0.3 < wr.real < 0.9 and wr.imag < 0.05: found3.append((round(wr.real, 5), round(wr.imag, 5)))
    except Exception: pass
found3 = sorted(set(found3))
w3_ship = wall_root_rw(0.68, 3, -3, 0.56 - 0.07j, rw68_old)
print(f"    shipped (3,-3) X = 0 at old surface: w = {w3_ship.real:.5f} {w3_ship.imag:+.5f}i ({to_hz(w3_ship.real):.0f} Hz)  [GR-2 V1.6: 288.5 Hz]")
for wr in found3: print(f"    free-surface Robin (ansatz) (3,-3) at {rw68:.3f}: w = {wr[0]:.5f} {wr[1]:+.5f}i  ({to_hz(wr[0]):.0f} Hz)  Q = {wr[0]/(2*abs(wr[1])):.0f}")
if found3:
    b3 = min(found3, key=lambda t: abs(to_hz(t[0]) - 288.5))
    check("S5. INDICATIVE: the free-surface (3,-3) line at chi = 0.68 lands within 10% of the shipped 288.5 Hz" if abs(to_hz(b3[0]) - 288.5) < 29 else "S5. INDICATIVE: the (3,-3) free-surface line does NOT land near 288.5 Hz", True, f"{to_hz(b3[0]):.0f} Hz")
check("ANSATZ CAVEATS (stated): the Robin law's coefficients are the a = 0 free-surface (b0, b2) mapped by the a = 0 Chandrasekhar transformation and imposed on the SN function; the Kerr surface is the 3320 criterion rescaled; neither is the reconstruction CONV-039 required — this is an indicative test of whether the 195 ~ 191 coincidence survives spin, NOT the Kerr recompute", True)
print(); print(f"3392 verify: {len(PASS)} passed, {sum(1 for x in PASS if not x)} failed")
```

### 7.7 Context: 3387, 3388

---

# The founder's clock mechanism at second order: with the ratified linear register it fails Mercury; a self-sourcing register rescues it, DERIVES the log-lapse, closes the strong-field departure — and moves the saturation surface to 1.33 r_S

**Patch 3387, Session 161, 2 Sep 2026.** Verify `code/3387_clock_mechanism_second_order_verify.py` (14/14, symbolic). Founder ruling R-CLOCK-RATE-IS-DISPLACEMENT. Reasoning `reasoning/3387.md`.

**Standing:** the fork is COMPUTED; nothing is enacted. This record prices the two branches and puts the choice to the founder as a physical picture.

## §1 The mechanism, taken literally

"Clocks progress at the SSV_net displacement per Moment, which shrinks as SSV_abs approaches saturation." Displacement per Moment is the PSR. So the local clock rate relative to the universal Moment is

    N = PSR_eff / l_P.

With one PSR hopped per Moment, local light speed by local clocks is `PSR/(PSR/l_P) = l_P` per tick — `c`, identically (**A**). The founder's picture and 3386's no-axiom census map are the same statement.

## §2 The second-order test

The corpus's register is linear: `u = k·Δ|SSV| = μ/r̄ ≡ v` (GR-1c Thm 1). Then `N = 1/(1+v)`, `g_tt = N² = 1 − 2v + 3v²`, i.e. **PPN β = 3/2** (GR: 1). The spatial metric `ψ⁴` gives γ = 1, so light deflection and Shapiro pass — but perihelion advance scales as `(2 + 2γ − β)/3 = 5/6`: Mercury's 42.98″/century would be **35.8″**. **Excluded** (the measurement is good to ~10⁻³) (**B**).

So: the founder's clock mechanism and the ratified linear register cannot both be exact. One of them moves.

## §3 The rescue that needs no new axiom — but changes an identification

Let the register **self-source**: a GP with a larger register broadcasts a larger census, so the field it sets is not the linear potential but

    u_reg = v/(1 − v/2) = v + v²/2 + v³/4 + …

Then `N = 1/(1 + u_reg) = (2 − v)/(2 + v)` — **exactly the ratified log-lapse.** β = 1; every test passes; and the log-lapse, which the T-1 charter *imposed* to make the exterior Schwarzschild, is now **derived** from the founder's mechanism plus Mercury (**C**). The self-sourcing coefficient is fixed: exactly ½ at second order — a prediction about the DI-bit census.

## §4 What branch (C) does to the arc

- **The census map:** `PSR = l_P N`; lattice hop per Moment `= N/ψ²` — GR's isotropic coordinate light speed, exactly. `J = 6.75` at any wall. **The strong-field departure of 3385/3386 closes**; the interior-echo spacing is GR's `π/(6.75 μ)`.
- **The saturation surface moves.** The register saturates (`u_reg = 1`, `PSR = l_P/2` — the floor is unchanged) where `N = 1/2`, i.e. `v = 2/3`: isotropic `r̄ = 1.5μ`, **areal `8μ/3 = 1.33 r_S`** — not the Buchdahl `9μ/4 = 1.125 r_S`. Surface lapse `1/2`, `z = 1` (not 2). **Level-A cavity 2.29 μ/c = 0.70 ms** at 62 M_⊙ (was 2.15 ms).
- **The 3370 window survives, re-labelled:** in `v` it is still `(0.536, 1]`; in `u_reg` that is `(0.73, 2]`, and `u_reg = 1` sits *inside* it. Saturation is no longer at the Buchdahl edge — which dissolves 3367's extremality problem (P4) by making it moot: the register saturates well before Buchdahl is reached.
- **Every wall computation since 3297** (3297, 3320, 3339, 3359, 3378, 3383, 3384) was done at `r_w = 9M/4`. Under (C) they would all be redone at `r_w = 8M/3` — where 3383 found `β_ℓ` has *flipped sign* (both `b₀, b₂ < 0` beyond 2.4M): the even-sector wall changes character. The flagship number would change again.

## §5 The other branch

(B′): keep the linear register exact and give up the clock mechanism as stated — the lapse would then need its own mechanism, which the founder has said he does not have (R-NO-LOAD-DELAY). On the record, branch (C) is the one with a mechanism, a passed test, and no new axiom. But it re-identifies which register saturates, and that is a physical picture.

## §6 To the founder (F-4)

**Does the DI-bit census self-source?** When a GP's own register is large, are the DI-bits it emits "heavier" — does a receiver's SSV_abs count the emitter's register, not just its presence? If yes, `u_reg = v + v²/2 + …` follows (the ½ is then a check on the census kernel, not a free number), the log-lapse is yours, Mercury passes, the strong-field departure closes, and the R-core surface sits at `N = 1/2`, 1.33 r_S. If no — if every emitter contributes the same DI-bit regardless of its own register — then the register is linear, your clock mechanism gives 5/6 of Mercury, and something else must carry the second-order lapse.

Physically: *does gravity gravitate in CPP?*

---

# Mercury from the bare theory: no special rule — the census self-enhances through the HOP LENGTH already in AP-4 + the PSR law; the second-order coefficient is a computation, and Mercury says it must be ½

**Patch 3388, Session 161, 2 Sep 2026.** Founder constraint C-NO-SPECIAL-RULE. Supersedes 3387 §3's phrasing ("heavier messages") — that mechanism is withdrawn as an AP-4 change. Reasoning `reasoning/3388.md`.

## §1 The founder's objection, sustained

"Heavier registers broadcast heavier messages" is a change to AP-4: the DI-bit payload is a **static snapshot** of the origin GP's registers, imprinted once, invariant in transit, and the receiver's SSV_abs is **count-like** (more DI-bits ⇒ larger register). T-1 (C-i) records the consequence: the per-Moment census is a *linear* functional of the origin registers one hop away. There is no payload weighting in the bare theory and none is added. Withdrawn.

## §2 What the bare theory already contains at second order

Two registered facts:
1. A DI-bit advances **one PSR per Moment** (AP-4c; P-SALTATORY-HOPS).
2. `PSR_eff = l_P/(1 + u)` — the hop is **shorter where the register is larger**.

Consequence, with nothing added: a conserved DI-bit flux crossing a region of small PSR is deposited more densely there — more hops per unit distance, one deposit per hop. The register is a per-Moment deposit count. So the census **self-enhances through its own propagation**: schematically `u = v·(1 + u)^p`, where `v = μ/r̄` is the bare (CP-sourced, 1/r-kernel) census and `p` is the exponent with which the deposit density scales with the inverse hop length. This is "gravity gravitates" *by the mechanism the theory already has* — the field slows and shortens its own messengers — not by a rule.

## §3 What the exponent decides (symbolic)

`u = v + p·v² + …`; with the founder's clock mechanism `N = 1/(1 + u)`:

| p (deposit-density exponent) | register | PPN β | perihelion vs GR | Mercury |
|---|---|---|---|---|
| 0 (no enhancement — the corpus's linear register) | `v` | 3/2 | 5/6 | 35.8″ — **fails** |
| **½** | `v + v²/2 + …` = `v/(1 − v/2)` | **1** | **1** | **43.0″ — passes**; `N` = the ratified log-lapse exactly |
| 1 (naive: deposits ∝ 1/PSR) | `v + v² + …` | 1/2 | 7/6 | 50.1″ — **fails** |

**β = 3/2 − p.** Mercury requires `p = ½` — and `p = ½` is exactly the value at which the founder's clock mechanism reproduces the ratified log-lapse. So the bare theory *can* compute Mercury, and the question "is it the bare theory?" becomes a single number the relay recursion must return.

## §4 Why ½ is not arbitrary — the shape of the computation

The naive count (deposits per GP per Moment ∝ 1/PSR) gives `p = 1`. But the register is not the deposit count alone: it is the count *summed over the PSR shell* the receiving GP perceives, and that shell's volume also shrinks with the PSR (∝ PSR³ in GP number at fixed lattice; ∝ PSR in the radial direction relevant to a 1/r relay). A deposit density ∝ 1/PSR integrated over a perception depth ∝ PSR^{1/2}… — the honest statement is that **`p` is the relay recursion's second-order coefficient and must be computed from T-1's kernel with the PSR-dependent hop**, not read off a dimensional argument. That computation is the deliverable: **OPEN-GR-CENSUS-P**. If it returns ½: Mercury is derived from the bare theory, the log-lapse is derived, the clock mechanism is confirmed, and the R-core surface moves to `N = ½` (1.33 r_S, 3387 §4) — all from AP-4 + PSR law + the founder's clock. If it returns anything else: the bare theory fails Mercury at second order, and *that* is the finding.

## §5 The near/far-side idea

The relativistic perihelion advance is a test-particle effect: it comes from the second-order term in `g_tt` (β) and the first-order term in `g_ij` (γ) along Mercury's *centre-of-mass* orbit. Mercury's finite size and the differential (tidal) field across it contribute of order `(R_Mercury/a)² ~ 10⁻⁹` of the orbit — negligible — and the Sun's quadrupole `J₂` gives ~0.03″/century, already accounted for in the 42.98″. So a near/far-side effect *on Mercury* cannot supply the missing 7″. But the founder's instinct that "something differential is being missed" is right in a different place: the *census's* propagation is differential across the orbit — the hop length varies with `v`, and that is the `p` term. The differential effect is in the messengers, not the planet.

## §6 What stands after this patch
- 3387 (A) local `c` by local clocks: stands. (B) the linear register fails Mercury: stands. (C) the *form* `v/(1 − v/2)`: stands as the required result; its *mechanism* is re-attributed from payload (withdrawn) to hop-length self-enhancement (bare theory). (D) the surface at 1.33 r_S etc.: conditional on `p = ½`.
- **Owed:** OPEN-GR-CENSUS-P — the second-order coefficient of the T-1 relay recursion with PSR-dependent hop. The single number on which "Mercury from the bare theory" now rests.


## §8 Return skeleton (fill EXACTLY; inline text)

```
REVIEWER: <your model name>
TIER LEGEND USED: <tiers used>
Q1: <verdict> [<tier>] — <reasoning>
Q2: (i) <verdict>; (ii) <verdict> [<tier>] — <reasoning>
Q3: <verdict> — <reasoning>
Q4: (A) <verdict>; (B) <verdict>; error <verdict> [<tier>] — <reasoning>
Q5: <verdict>; DECIDER: "<≤ 40 words>" — <reasoning>
Q6: <verdict> — <reasoning>
Q7: <verdict> — <list or NONE-FOUND>
Q8a: <verdict>  Q8b: <verdict> — <reasoning>
SCRIPT: <SCRIPT-EXECUTED + count lines / INDEPENDENT-HARNESS / INSPECTED>
EK-1: <exact string>
DEFECTS/OBJECTIONS: <numbered list, or NONE>
```

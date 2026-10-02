# The Founder's Proposal — the PSR Set by the Grid-Point Count of the Planck Sphere: in Its Compounding Form It Fixes Mercury's ½ and Removes the Background Residual, at the Price of GR-1c's Exact Schwarzschild and a 4.6% Larger Black-Hole Shadow

**Patch:** 4365. **Lane:** foundations, with GR. **Session:** 242.
**Founder:** `founders_voice/4365_psr_from_planck_sphere_gp_count.md`.
**Verify:** `series_standard_model/code/4365_psr_from_planck_sphere_gp_count.py` (sympy).
**Critic:** an independent fresh-context critic checked a draft; its return is appended verbatim to
`series_standard_model/reviews/2026-10-01_session_242_critic_returns_verbatim.md`. Its corrections are adopted (§6).

## 1. The proposal, read against the corpus

The founder notes that the corpus has never said how a GP turns its SSV_abs into a PSR distance. That is correct:
R-PSR-LAW-LOG (3390) is a calibrated constitutive law, PSR/l_P = 1 − ε + ε²/2 + O(ε³) with ε = kΔ, and its third order
is open. He proposes correlating SSV_abs with **the number of GPs enclosed in the Planck sphere** for that SSV_abs.

On GR-1j's rigid lattice, a ball of fixed radius l_P always holds the same number of GPs. The only reading with
content is therefore **the ball of radius equal to the local PSR**: n(Δ) = GPs inside it, and q = PSR/PSR_∞ =
(n/n_∞)^{1/3}. This restates the PSR law as a counting rule. The physics is in **how the count falls as stress rises**,
which the proposal leaves open. The 4364 source rule, written in the same terms, is **injection ∝ n_s**: the number a
GP already needs to set its PSR also sets how strongly a resident CP stamps its DI-bits.

## 2. Two readings of "correlate"

| count rule | PSR law it gives | second order | background factor on the local field (under 4364's source rule) |
|---|---|---|---|
| (A) n ∝ 1/SSV_abs (proportional) | q = (1+3ε)^{−1/3} = 1 − ε + 2ε² | 2 (β = 5/2, Mercury fails; = 4360/4361) | 1 − 3ε₀ + 9ε₀²: first order, ~10⁸× the clock bound |
| (B) n = n_∞ e^{−3kΔ} (compounding: each equal step of stress removes the same fraction of the GPs) | q = e^{−ε} = 1 − ε + ε²/2 − ε³/6 | **½, Mercury's value** | **1, exactly** |

"Correlate" reads most naturally as (A), and (A) fails. (B) is **Claude's reading, not the founder's**, and is put to
him as a physical picture (§5).

## 3. What (B) does, and its conditions

- **Uniqueness (conditional).** If a source injects in proportion to its count (S ∝ n_s), then exact local invariance
  of G requires d ln n/dΔ to be constant, which gives (B) and only (B) (script: `dsolve`). Its second order is ½, so
  **the two open choices (source rule, PSR law) become one**. It is not a parameter-free prediction. Invariance fixes
  the product of source rule and law, and a source rule ∝ R_s³/|d ln q/dΔ|_s would make any law invariant. The
  argument holds **within CPP's linear census**, with the gather kernel and the assembled metric. GR keeps local
  invariance with a non-exponential lapse.
- **A second route to the same form (the critic's, checked here).** On CPP's assembled metric (g₀₀ = −q², g_ij = q⁻²δ)
  the static wave operator is q²∇²_flat. If Δ is flat-harmonic (GR-1j) and the log-lapse is too, then ln q ∝ Δ,
  which is (B), independently of the source rule. The input is "one PSR sets rulers and clocks" (founder, 4362).
- **The background scales out exactly.** e^{−(ε₀+δε)} = e^{−ε₀}·e^{−δε}, so the absolute stress (Sun, Galaxy,
  cosmology) only rescales local units. TODO-4364-EPSABS closes for G under (B), and for α if its reading is
  metric-coupled (4364 §2, still inferred).

## 4. Erratum to 4364 §2

4364 reported a residual (1 − ε₀²/2) in local G. That came from **truncating** the ratified law at second order. With
its open third-order coefficient γ₃ the residual is **1 − (3γ₃ + ½)ε₀²**:

| law | γ₃ | residual |
|---|---|---|
| truncated (what 4364 used) | 0 | −ε₀²/2 |
| GR-1c's Padé, exact Schwarzschild | −¼ | +ε₀²/4 (annual swing 1.6×10⁻¹⁸ at U_sun, 1.6×10⁻¹⁶ at U_gal) |
| (B) | −1/6 | 0 |

## 5. The price, and the tests

- **GR-1c conflict (pre-existing, now explicit).** GR-1c's boxed theorem (L280–293) is *exactly* isotropic
  Schwarzschild: lapse (1−ϱ)/(1+ϱ) and spatial factor (1+ϱ)⁴. Its Form A (L636–645) is the Padé log-lapse. Rulers
  and clocks then shrink by different factors at second order. The founder's 4362 ruling, one PSR for both, gives
  g_ij = q⁻²δ, and with it (B). The 3837 note ("R-PSR-LAW-LOG **is** e^{−ε}") was never reconciled with GR-1c either.
  Adopting (B) means withdrawing GR-1c's "exactly Schwarzschild" at third order and redoing 3390's held surface,
  which used the Padé exterior (TODO-4365-THIRDORDER).
- **Strong field (script).** With one PSR for rulers and clocks, (B) is the exponential metric:
  - the photon sphere sits at isotropic r = 2m, areal radius **3.30 m** (GR: 3 m);
  - the shadow's critical impact parameter is **2e·m = 5.437 m** against GR's 5.196 m, **4.6% larger**;
  - there is no horizon.

  Event-Horizon-Telescope shadow sizes agree with GR at roughly the 10% level, so this is not excluded today, but it is
  a near-term test.
- **Unchanged:** first and second order (β = γ = 1), so the classical solar-system tests stand. The black-hole floor
  q = ½ (AP-5; R-DIBIT-COUNT-AT-FLOOR, n_floor = n_∞/8) sits at ε = ln 2.

**Question to the founder (physical picture).** When stress rises at a grid point, its Planck sphere shrinks and holds
fewer grid points. Which picture is yours?
- (i) Each equal step of added stress removes the same *fraction* of the grid points, like compound interest.
- (ii) The count is simply inversely proportional to the total stress.

(i) gives Mercury's orbit without a calibration and keeps every laboratory the same in any background. It also makes
black holes slightly different from Einstein's: no horizon, and a shadow about 5% larger, which telescopes can check.
(ii) fails Mercury and the clocks.

## 6. Critic's corrections, adopted

- "The founder's counting rule" became "the founder's framing; the compounding form is Claude's" (§2).
- "Unique" became "unique given the pure-count source rule, within CPP" (§3).
- "Mercury as a consequence" became "two choices become one" (§3).
- "Removes the residual" became "the residual was partly a truncation artefact" (§4).
- "Only third order" became "third order, which overturns GR-1c's exact theorem and is testable now" (§5).
- Struck: the draft's floor line. The truncated polynomial only touches ½ at its minimum (ε = 1); it never crosses it.

## 7. PD-008

- **The convenient branch:** crediting (B) to the founder because it works. Refused: it is put to him (§5).
- **Not claimed:** that the exponential is GR's lapse (it is not), or that the corpus has chosen it. GR-1c's −¼ stands
  until the founder rules.

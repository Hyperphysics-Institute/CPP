# OPEN-GR-RCORE-1 — Planck-core reflectivity from the ratified T-1 framework

**Registered:** Patch 3297, Session 154 (20 Aug 2026). ID minted after clean
CLONE-FIRST grep (no prior `RCORE` occurrence in the corpus).
**Verify:** `series_gravitation/code/3297_rcore_verify.py` — 9/9 PASS,
computation-before-claims.
**Standing:** DERIVED-PENDING-REVIEW. Conditional on the W2/PSR grounding, by
design, like everything in the gravitational arc. Carries a HALT finding
against shipped GR-1d (§5) — GR-1d is NOT edited at this patch, per the HALT
discipline (FTERM precedent, Patches 3258–3262).

**Why now.** The W-B suite pass identified Planck-core reflectivity as the one
uncomputed quantity blocking three of GR-1h's four open problems AND GR-1d's
amplitude problem (`frontier_sectors/GR.md`, Patch 3292 finding 4). GR-1d Open
Problem 1 states its own requirement: "the full CPP field equation …
evaluated in the strong-field interior." That requirement is now met — T-1 is
CHARTER (CONV-027 4–1, conditions discharged; founder ratified Patch 3262),
with the R-CSTAR-MAP kinematic mapping ratified in the same act. The founder's
Session-154 opening instruction: run the priority calculation.

---

## §1 Inputs (all previously ratified or shipped; nothing new posited)

1. **PSR formula** (GR-1c; W2 strength): PSR_eff(r) = l_P / (1 + k·Δ|SSV|),
   with the vacuum solution k·Δ|SSV| = GM/(r c²) ≡ μ/r.
2. **CP Exclusion floor** (GR-1c Thm 2 / GR-1e): PSR_eff ≥ l_P/2, saturated at
   k·Δ|SSV| = 1.
3. **Coordinate identification** (GR-1c's own declaration, "lattice ≡
   isotropic — the lattice is flat; rulers and clocks shrink"; RE-DERIVED and
   ratified at T-1, Patch 3258/3262): the r in the PSR formula is the
   **lattice = isotropic** radial coordinate r̄.
4. **T-1** (CHARTER): (1/c_*²)∂²_t(Δ|SSV|) − ∇²_lattice(Δ|SSV|) = census
   source, with c_*(x) = PSR_eff(x)/(√3 t_P).
5. **R-CSTAR-MAP** (ratified law): c ≡ R_vac/(√3 t_P), R_vac = l_P.
6. **AP-4 messenger conservation** (ratified axiom layer): DI-bits are
   conserved; per-GP registers refresh from arrivals each Moment.
7. **GR-1e mechanical fixed point**: the saturated core is a stable
   force-balance equilibrium (no secular energy sink).

## §2 Result R-1 — |R_core| = 1 (unit modulus)

A census-wave perturbation δu (u ≡ Δ|SSV|) incident on the saturated surface
cannot be absorbed:

- **No storage:** at the surface the register value is pinned at the Exclusion
  floor (k·u = 1, PSR_eff = l_P/2). There is no register headroom in the
  compression direction; the saturated interior cannot take up census-wave
  content.
- **No sink:** DI-bits are conserved (AP-4). The perturbation's messenger
  content cannot vanish; it is re-emitted at the surface shell.
- **No secular transfer:** the GR-1e fixed point is stable — incident
  perturbations do not pump the core to a new equilibrium; the balance
  restores per-Moment.

Therefore all incident census-wave flux returns: **|R_core(ω)| = 1** for all
ω far below the lattice cutoff (ωτ ≪ 1; astrophysical GW frequencies sit
~46 orders of magnitude below 1/t_P). The scattering solve (verify check 7)
confirms unitarity to machine precision (max ||R|−1| = 2.2×10⁻¹⁶) given the
§3 boundary condition — the numerical check verifies internal consistency of
the model (real potential + energy-conserving wall), while the physical
content of |R| = 1 rests on the conservation argument above.

**GR-1d's amplitude problem is thereby closed at argument level:** the echo
amplitude chain |h_n| = |R_core|ⁿ |T_bar|²ⁿ |h_rd| has no free reflectivity
parameter. First echo at |T_bar|² ≈ 5% of ringdown amplitude, exactly the
number GR-1d computed under its |R| = 1 assumption — now derived, not assumed
(verify check 8).

## §3 Result R-2 — reflection phase π (Dirichlet), linear order

The Exclusion floor clamps the register at the surface: δu → 0 there in the
linear regime (a positive δu would violate PSR ≥ l_P/2; the clamped register
is a fixed end). Dirichlet boundary ⇒ reflection coefficient −1 ⇒ **phase π**
— confirming the "pressure node" phase GR-1d assumed without derivation.

**Registered limitation (honest):** the floor is a one-sided constraint
(δu < 0 momentarily unsaturates the surface layer). The linear Dirichlet
treatment is the leading-order model; the rectification correction from the
unilateral constraint is an open refinement, folded into OPEN-GR-RCORE-2
(§7). It does not touch |R| = 1 (conservation is exact); it can shift the
phase and the effective surface location at higher order.

## §4 Finding F-R1 — the exclusion surface sits OUTSIDE the would-be horizon

This is the calculation's structural yield, and it is forced by inputs 1–3
with no freedom:

- Saturation at k·Δ|SSV| = μ/r̄ = 1 puts the surface at **isotropic r̄ = μ**.
- The exact isotropic→areal map r = r̄(1 + μ/2r̄)² sends r̄ = μ to **areal
  r = 9μ/4 = (9/8) r_S** (verify check 0) — *outside* the areal horizon 2μ.
  The horizon's isotropic image r̄ = μ/2 lies strictly inside the excluded
  region r̄ < μ (check 1).
- Equivalently in the ratified log-lapse dictionary: k·Δ|SSV| runs over [0, 1]
  on the entire exterior; the dictionary singularity at k·Δ|SSV| = 2
  (artanh(1) — the horizon) is **unreachable. The Exclusion floor censors the
  horizon.**
- Surface lapse: exactly **1/3**, by both the isotropic Schwarzschild form and
  the artanh dictionary (check 2). Surface redshift z = 2.
- Census speed at the surface: **c_*(surface) = c/2** under ratified
  R-CSTAR-MAP (check 3). NOTE-GR-CSTAR-STRONGFIELD's "~0.29c" is the pre-map
  shorthand figure — 1/(2√3) = 0.2887, reproduced exactly under c = l_P/t_P
  (check 3). The note's physics (strong-field census-speed reduction)
  survives; its number updates to c/2 under the law ratified in the same
  patch cycle that minted the note.

**CPP black holes are horizonless compact objects with a hard surface at
areal (9/8) r_S.**

### Consilience C-R1 — exact Buchdahl saturation (zero parameters)

GR's Buchdahl theorem bounds any static, spherically symmetric matter
distribution to R ≥ (9/8) r_S = 9GM/(4c²), with the bound saturated by the
incompressible sphere at critical central pressure, surface redshift z = 2.
The CPP core — incompressible by the CP Exclusion floor — lands **exactly on
the Buchdahl bound**, with **exactly** the Buchdahl-critical surface lapse 1/3
(check 2). No parameter was available to tune: the surface location is fixed
by k·Δ|SSV| = 1 and the ratified coordinate identification. GR's own maximum-
compactness theorem and CPP's exclusion mechanics name the same radius from
opposite directions. Registered as a consilience observation; unminted as a
prediction.

## §5 HALT-GR-1D-DELAY — the shipped delay formula does not survive the ratified coordinate identification

GR-1d Theorem (shipped): Δt = (4GM/c³) ln(2M/m_P) — ≈ 112 ms for GW150914
(verify check 5 reproduces 112.7 ms from GR-1d's own formula). That result
rests on two steps: (i) reading r_core = r_S/2 as areal (placing the core
inside the horizon), and (ii) displacing the effective reflective surface to
r_0 = r_S + l_P "by Planck-scale quantum effects," which imports the
ln(r_S/l_P) ≈ 88 enhancement.

Under the ratified identification (input 3), step (i) is not available: the
surface is at areal 9μ/4, outside the horizon, and no near-horizon
displacement argument arises because there is no horizon. The delay becomes:

- **Level A (measured-metric propagation, eikonal barrier at the photon
  sphere):** Δt_A = **(3/2 + 8 ln 2) GM/c³ ≈ 7.045 GM/c³** exactly (check 5).
  GW150914 (M = 62 M_☉): **2.15 ms**, echo comb spacing ≈ 465 Hz. The
  finite-ℓ correction moves the ℓ = 2 barrier peak to r ≈ 3.28μ, round trip
  ≈ 8.60 GM/c³; the time-domain evolution measures 8.20 GM/c³ (check 7).
- **Level B (T-1 lattice dynamics, c_*(r̄) = c/(1 + μ/r̄)):**
  Δt_B = **(√3 + 2 ln(1 + √3/2)) GM/c³ ≈ 2.980 GM/c³** (check 6) — 0.91 ms
  for GW150914.

Both are closed forms with no free parameters; both are **milliseconds, not
112 ms**, and the ln(2M/m_P) factor is gone. The prediction becomes sharper
and far more exposed: ~ms-scale echo structure at ~5% amplitude on
GW150914-class remnants is territory existing LIGO ringdown analyses can
constrain. If the data already exclude it, that is the swarm-validation ethic
functioning as designed — the falsifier got stronger.

**HALT discipline applied:** GR-1d (and GR-1e's horizon-based framing) are
shipped papers. Nothing is edited at this patch. Adjudication owed: founder
ratification of the coordinate reading of the exclusion surface (it is
already implied by GR-1c's own coordinate declaration and the ratified T-1
identification — but its consequence contradicts a shipped Theorem, which is
exactly the FTERM situation), then a CONV round. Note the review-coverage
map: GR-1c Theorems 1–2, on which GR-1d/GR-1e/GR-1g rest, have never had a
dedicated round — this finding is a natural anchor for that round.

## §6 Downstream: what this unblocks and re-frames

- **GR-1d amplitude problem (Open Problem 1): CLOSED at argument level** —
  |R_core| = 1, phase π, derived (§2–§3). Delay formula: superseded pending
  adjudication (§5).
- **GR-1h problems 1–3:** the boundary condition at the core is now
  specified (Dirichlet, |R| = 1 at areal 9μ/4). The "Planck-core bomb" is
  re-framed: a horizonless, perfectly reflecting, spinning compact object is
  the textbook setting of the **ergoregion instability** — the sharpened
  question is whether CPP Kerr cores possess ergoregions outside their
  exclusion surfaces, and on what timescale the instability acts. Registered
  inside OPEN-GR-RCORE-2; Kerr untouched here.
- **GR-1e:** the remnant fixed-point mechanics (§1 input 7) is unaffected —
  it is a force-balance statement. The *Hawking framing* (horizon
  temperature, "inside the horizon" language) inherits the F-R1 tension;
  flagged for the same adjudication, unworked here.
- **NOTE-GR-CSTAR-STRONGFIELD disposition (the five-paper exposure):**
  subsumed under F-R1. There is no horizon; GR-1f/GR-1g "near-horizon
  velocity reaching c" bounds and GR-1h's horizon-velocity threshold are to
  be re-read as near-surface statements with c_* ≥ c/2. The note's number
  updates 0.29c → c/2 (§4). Per-paper working = a W-D-style dated-note pass
  after the §5 adjudication settles what the notes should say.

## §7 What is NOT claimed, and OPEN-GR-RCORE-2

Not claimed: external review (none yet — DERIVED-PENDING-REVIEW); the tensor
sector treated beyond the scalar analogue at the wall; the nonlinear
one-sided-constraint correction (§3); any Kerr result; any change to shipped
text.

**OPEN-GR-RCORE-2 (minted):** the residue bundle — (a) Level A vs Level B
discrepancy (7.05 vs 2.98 GM/c³): the dynamical-sector dictionary question
(does T-1 lattice propagation map onto measured-metric null propagation?),
which is the same territory as the registered dispersion-family falsifier;
(b) unilateral-constraint refinement of the Dirichlet phase; (c) tensor-
sector wall condition; (d) Kerr geometry: ergoregion vs exclusion surface,
ergoregion-instability timescale. Level A is the conservative headline
pending (a).

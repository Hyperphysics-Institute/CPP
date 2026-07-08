# G4 · Stage-3 EXECUTED — D(T_amb) from the PCD displacement rules: the harmonic-null theorem, the activated law, and the corner that carries the gate (Patch 2330, 7 July 2026)

**What this patch is:** the 2329 handover's single pre-registered task ("derive D(T_amb)"),
executed under the founder's no-carried-velocity ruling
(`founders_voice/no_carried_velocity_displacement_from_ssv_2026-07-07.md`). **Verify:**
`code/2330_g4_stage3_d_of_tamb.py` (12/12). **No resting paper touched. NO VERDICT MOVED:
G4 stays UNRESOLVED-QUANTIFIED; OPEN-DM-AGG-1 stays open** — but both change character, per
§4–§6, and two new surfaces are registered (AGG-1-R, OPEN-DM-TAMB-1).

All three 2329 pre-registrations (PRW-D today; the AGG-1 knee schedule; the Planck-floor
kill branch) were written before this computation and are graded in §7 against it unmodified.

## 1. The harmonic-null theorem (the founder's ruling, made load-bearing)

Under the ruling, a quiescent Sea DP center has no inertial memory: its per-Moment
displacement is a function of the local SSV_net/SSV_abs only. The center is therefore
*slaved* to the local field. For the field's registered gapless coherence mode
(2317: ω = ck, exact at the discrete level, C-e), the center's velocity autocorrelation is
fixed by the thermal mode spectrum ~ ω³ n_B(ω), whose ω → 0 weight vanishes identically.
By Kubo, D_coherent = (π/3)·S_vv(0) = **0, exactly**: a harmonic field makes the center
quiver, not diffuse — coherent field-following transports *nothing*, at any temperature.
The incoherent per-Moment residue is bounded by the Planck floor l_P·c/6 ≈ 2.7×10⁻²¹ c·fm,
×1.9×10¹⁸ below the PRW-D bottom (verify checks 1–2).

**Consequence:** the 2329 kill branch sharpens from "no field-level persistence → KILL" to
a theorem: *every coherent route is closed*. Survival requires a **threshold channel** —
discrete, thermally activated events. Two exist in the registered rules, and together they
are the whole law.

## 2. The two threshold channels, and the law

**Channel T (site hopping / transport).** Occupancy moves when a DP center hops one pitch
a. The saddle is a partial stretch of the center's e-channel contact bonds; the full break
is E_ee = 0.9 MeV (M3), so E_a = κ_a·E_ee with κ_a ∈ [1/3, 1) [**J-2330-1**]. Attempts
decorrelate at the ZBW internal cycle of the quiescent DP (U2): each cycle re-phases the
center's response to the ambient fluctuation ensemble, giving independent attempts at
ν = κ_ν·E_z/ħ [**J-2330-2**; the cadence fork is condition **C-i**, graded in §3].

  D_hop(T_amb) = (a²ν/6)·exp(−E_a/T_amb),  saturating at min(a²ν/6, c·ℓ_cp/3).

**Channel L (activated creation / local).** The lowest Sea creation channel is the
e-channel at E_gap = 0.9 MeV (2311 inventory). At T_amb > 0 it is thermally activated at
the same cadence: Γ_loc = κ_c·ν·exp(−E_gap/T_amb) [**J-2330-3**]. This relaxes occupancy
*locally* — k-independent — and refines 2327's C-h-1: occupancy conservation is exact only
at T = 0; Channel L is the finite-T correction.

**The law (the deliverable):** the knee entering the 2321/2327 Θ construction is the total

  **knee_tot(T_amb) = ħ·[D_hop(T_amb)·k² + Γ_loc(T_amb)],  k = 1/R_s** —

monotone increasing in T_amb through the gap and saturating toward the band edge ħc/a
(verify check 5). **The survive branch's "D early-high, late-in-window" is now a
DERIVED-FORM statement** under any monotone cooling T_amb(z) — it was the founder-input
clause of the 20-July decision; it is now a property of the law.

## 3. The cadence fork (C-i), graded

- **C-i-T (thermal bandwidth, ν = T/ħ):** the Kramers/Rice prefactor for Langevin dynamics.
  Tops out at D = 8.4×10⁻⁴ c·fm at the U6 prior ceiling — ×6 below the window bottom even
  at zero barrier. **KILLED within priors** (check 4).
- **C-i-Z (ZBW cadence, ν = κ_ν E_z/ħ) — PRIMARY.** PCD is not Langevin: the registered
  internal cycle is a fast clock that re-phases the center's per-Moment response; the
  ambient ensemble is re-sampled per cycle. Brings U2 into the gate exactly as SI-1's
  Stage-3 forward-map note anticipated.
- **C-i-P (Planck cadence, ν = 1/t_P):** demands E_a/T_amb ∈ [47.1, 49.0]; at
  T_amb = kT_form this is κ_a ∈ [0.86, 0.89] — a striking E_ee/kT_form numerology, **noted
  and DISFAVORED**: successive Moments sample a correlated thermal field, and the 2320
  per-Moment regeneration carries quiescent, not thermal, weight. Independence at Planck
  cadence is unregistered. Carried as the outer cap, not the answer.

## 4. What PRW-D becomes: the corner, and who carries it

PRW-D was registered as a window in D; its invariant form is the knee window
[1.60, 11.27] keV (Θ(4.25 keV) ≥ 0.66). Under the law this inverts to pinned combinations
in SI-1 unknowns:

- transport-dominated: **X4 ≡ κ_ν E_z·exp(−E_a/T_amb,0) ∈ [6.2, 43.7] MeV**;
- local-dominated: **X4′ ≡ κ_c κ_ν E_z·exp(−E_gap/T_amb,0) ∈ [1.60, 11.3] keV**.

The Monte-Carlo existence scan over the full priors (U2, U6, κ_a ∈ [1/3,1),
κ_ν, κ_c ∈ [1/3,3]; 4×10⁵ samples; check 9) gives:

- **The corner is NON-EMPTY** — 4.0% of the prior volume; marginals (5–95%):
  T_amb,0 ≈ 82–872 keV, κ_a unconstrained, E_z broad.
- **The corner is carried ~99.8% by Channel L.** The operative pinned combination is X4′;
  E_a nearly drops out. The knee today, if the candidate survives, is not transport at all
  — it is the thermally activated creation channel, k-independent.
- **Suite consistency survives the channel-identity change** (check 10): with a
  k-independent knee the published anchors hold at both window edges (dwarf P = 1.000,
  pin ≥ 0.9996, LSB 0.874 ≥ the 0.87 bar). The window statement is invariant in knee form.
- **T_amb,0 sits ×5–×53 above the F7 soft target** (kT_form = 16.4 keV). Named tension;
  F7 is CONJECTURED-soft.

## 5. What OPEN-DM-AGG-1 becomes: transport closed, R-III required

- **Transport alone cannot deliver route (i)** (check 6): every hop-branch prefactor in
  the U2 prior saturates at or below the ballistic cap, knee_hop ≤ 324 keV <
  knee_req(pin) = 579 keV. The transport-optimal activation is v_on = 66.9 km/s
  (z ~ 1.4×10⁷, ~2.8×10⁴ captures/Hubble) — **the 2328 light-speed row is now the derived
  optimum of the entire hop branch.** This half of route (i) is CLOSED by derivation.
- **Channel L above the gap (regime R-III) is the route** (checks 7–8): for T_amb ≳ E_gap
  the knee rises toward band-edge class, and protection extends — on the exact 2328
  machinery — down to **v_edge = 0.15 km/s, (1+z) ≈ 3.1×10⁴**, deep in the dark ages
  (locating 2328's band-edge crossing exactly). Under free-streaming cooling
  T_amb ∝ (1+z), covering the whole protected descent requires only T_amb,0 ≥ 29 eV —
  **generic**: every corner value of §4 over-covers by ×10³⁺.
- **The residual (AGG-1-R, registered here):** the post-crossing tail below v_edge. The
  window-D rate at v_edge is 17/Hubble as a ceiling, and the onset is marginal
  (Θ = Θ_crit) by construction; the honest number is the tail *integral* under the derived
  law with a specified T_amb(z) — a single bounded computation, queued, not claimed.

## 6. The new kill surface: the closure bound (OPEN-DM-TAMB-1, registered here)

If the gapless coherence mode itself thermalizes at T_amb, its energy density
(π²/30)T⁴/(ħc)³ gravitates as radiation under one-ledger sourcing (only the quiescent
monopole is annihilated; departures source). That caps **T_amb ≤ 3.2 meV** (check 11).
The §4 corner exceeds this by ×10²⁹⁺ — and so does the F7 soft target itself (×6.5×10²⁶
at 16.4 keV): **the bound bites the entire keV-class U6 prior and predates this patch.**
Evasions, either of which must be established:

- **(a) a two-temperature Sea:** the coherence mode cold (sub-meV), the activation
  statistics carried by a dilute gapped excitation component at T_amb. The Boltzmann
  factors of §2 are unchanged; the harmonic-null theorem then holds a fortiori. Requires
  the mode–component equilibration time to exceed Hubble — a computable statement.
- **(b) a one-ledger exemption for Sea self-excitation** — needs a G-sector derivation,
  not an assertion.

Registered against U6; not adjudicated here.

## 7. Grading against the 2329 pre-registrations (unmodified)

1. **Planck-floor branch:** does NOT fire as a kill — persistence exists, but *only*
   through the activated threshold channels; the harmonic-null theorem closes every
   coherent route (this is the floor made rigorous, and escaped by derivation, not fiat).
2. **PRW-D today:** not resolved to a number — resolved to a **derived law plus a
   non-empty two-unknown corner** (X4′ in (E_z·κ's, T_amb,0)), suite-consistent, carried
   by a channel nobody had named. G4 stays UNRESOLVED-QUANTIFIED.
3. **AGG-1 schedule:** monotone cooling DERIVED in form; route (i) NARROWED to
   R-III-required, with transport closed and the residual isolated in AGG-1-R.

## 8. Caveats (named)

1. **J-2330-1/2/3** are O(1)-graded identifications (saddle fraction, ZBW attempt
   cadence, creation-attempt cadence); the κ spans carry them, but the *identifications*
   are modeling choices in the SI-1 J-tag sense, panel-reviewable.
2. **C-i (cadence fork):** C-i-Z is primary by the registered-ontology argument of §3;
   C-i-P is disfavored, not excluded — its E_ee/kT_form numerology is on the record.
3. **Subdiffusive escape (2327 C-h-3)** is resolved in passing on the hop branch (simple
   activated kinetics, no heavy-tailed generator) but not on exotic disorder variants.
4. **The closure bound (§6)** is the sharpest open threat to the corner; if neither
   evasion holds, the corner — and F7's reading of T_amb — dies with it.
5. **AGG-1-R** (tail integral) and the 2324-inherited caveats stand.

## 9. Ledger

Stage-3 **EXECUTED**. New named condition C-i (cadence, three branches, Z primary). C-h-1
refined (T = 0 exact; Channel L the finite-T correction). New pinned combinations X4/X4′
(SI-1 §4 updated). New registrations: **AGG-1-R** (tail integral), **OPEN-DM-TAMB-1**
(closure bound vs U6). The 20-July input sharpens once more, still without a
recommendation: the open condition is now *"does the Sea's activated creation channel put
knee_tot in a factor-7 window today (X4′), with the above-gap early history generic and
the closure bound evaded"* — one derived law, two registered unknowns, one named threat.

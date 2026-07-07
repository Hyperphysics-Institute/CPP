# Grok W2 executed — formation-N vs floor-N, and the radiation-era aggregation epoch (Patch 2328, 7 July 2026)

**What this patch is:** the queued red-team computation (Grok W2, CONFIRMED-open at the 2311
adjudication; "1855-style kinetics with capture+floor active → N distribution → floor check").
**Verify:** `code/2328_grok_w2_formation_floor_reconciliation.py` (8/8). **No resting paper touched;
no registered verdict moved.** The reconciliation splits into a static layer (PASSES) and a dynamic
layer that opens a new named condition: **OPEN-DM-AGG-1, the radiation-era aggregation epoch** —
registered here.

## A. Static reconciliation (restated) — PASS

The 1855–1860 arc already closed the static question: formation kinetics gives N_form ~ 3–27
(monomer addition at E_bond/kT ≈ 4; the N ~ 500 strand retired), the floor MC was run at N = 18
(1871, registry-pinned geometry), and the cluster ceiling is N ≲ 18–21 (1860, transport
convention). The floor-N sits inside the formation window and at the ceiling — three independent
arrows at short N.

## B. Formation epoch — capture reach-dead, the 1855 endpoint unmodified

At formation (kT = 16 keV) the rod thermal velocity is 337 km/s, where Θ_crit = 1.59 > 1: capture
is infeasible at *ceiling* spectral weight, and the elastic floor only thermalizes. Rod–rod capture
does not alter the monomer-addition kinetics during formation proper. Grok's "capture active during
the kinetics" is answered: not during formation — **after** it.

## C. The new surface: post-formation, capture activates in the radiation era — universally

After kinetic decoupling (immediate; SM coupling is XQC-scale) rod velocities redshift v ∝ a⁻¹,
descending from 337 km/s through the entire anchor ladder before structure formation revives them.
Because **Θ_crit ∝ v² (reach saturation) falls faster with v than the encounter response at any
knee**, dissipative capture switches on during the descent for *every* registered spectrum under
D = const:

| Spectrum | Activation | Rate at/along activation |
|---|---|---|
| PRW-D survive window | v_on ≈ 244–291 km/s, z ~ 5–6×10⁷ | ~10⁵ captures/rod/Hubble |
| light-speed transport cap (2327 kill side) | v_on ≈ 67 km/s, z ~ 1.3×10⁷ | ~1.6×10⁴ (P = 0.69 at the pin epoch) |
| bare Ohmic floor | v ≈ 0.05 km/s, z ~ 10⁴ | ~2 — borderline, O(1) |

Along the survive-class descent the rate stays above unity for the **entire radiation era**
(6.3×10⁴ / 2.3×10⁴ / 3.1×10³ at v = 200/50/10 km/s; ~1 at equality): integrated ≥10⁵ captures per
monomer lineage. **The monomeric 25-GeV population — the calibration object of every anchor
(floor at N = 18, dwarf/pin/LSB σ/m, XQC F5, m_rod itself) — does not survive to the halo era
under D = const.** Only the bare-Ohmic case grades as borderline (dimers at most), and 2327
established that occupancy conservation *forces* transport-class spectra or stronger.

## D. OPEN-DM-AGG-1 (registered here) — the aggregation-epoch condition

The candidate as published requires one of:

- **(i) A D(T_amb) cosmological history (the natural route).** Holding capture off at epoch z(v)
  requires knee(z) ≳ 36 keV (v = 200) / 0.58 MeV (50) / 14.5 MeV (10) — an escalating (~v⁻²)
  requirement met by a hot early Sea cooling into today's values, down to v ~ 0.05 km/s, below
  which no knee suffices (the requirement crosses the 197-MeV band edge — hence the universal
  O(1) dark-age tail). Route (i) delays activation into the deep dark ages and reduces the runaway
  to that borderline tail; whether the tail itself fires depends on the perturbation velocity
  floor (caveat 3). **The same Stage-3 quantity that decides G4 decides the activation epoch: the
  D derivation must deliver D as a function of Sea state (D(T_amb)), not only today's value. One
  derivation, two gates.**
- **(ii) An aggregation endpoint that reproduces the monomer-calibrated anchors** via the
  registered d_f map, (σ/m)_agg = (σ/m)_mono (R_g/a)^{2−d_f} — compact endpoints lower σ/m
  (cluster-safe, anchor-breaking), fractal ones raise it (cluster kill). Disfavored on its face;
  would be a DM-4-scale Smoluchowski computation to even attempt.

**Branch grading:** in the G4-kill outcome the candidate is already dead as the suite's
explanation, so AGG-1 is moot for the release there (one line: the reverted-relic floor value
would shift by the d_f factor; bounds have ×10 room). **The bite is on the survive branch: PRW-D
alone is no longer sufficient for survival — PRW-D + a route-(i) history is.** The 20-July input
gains one clause: the named open condition is now *D today in the window AND D early above it*,
which is a monotone-cooling statement — arguably *more* natural than a constant D, but underived.

## E. W2 verdict

**Static: PASS. Dynamic: CONDITIONAL on OPEN-DM-AGG-1 in every branch (under D = const).** The
floor-N check cannot close until the activation history does. No registered claim moves; the
anchors' unit-monomer assumption acquires a named cosmological condition, exactly parallel in
structure to the unit-efficiency assumption G4 named at 2311.

## F. Caveats (named)

1. **D = const is the operative assumption** — the finding is precisely that it must be false
   (route i) or the endpoint must conspire (route ii).
2. **Velocity history:** free-streaming v ∝ a⁻¹ from formation; the elastic floor self-thermalizes
   the population (~225 scatterings/Hubble at z ~ 10⁷) but conserves energy, so the scaling
   stands for the NR gas. Order-unity g*(T) factors in t(T) not tracked.
3. **The O(1) dark-age tail** (v ≲ 0.05 km/s) sits at the mercy of the perturbation velocity
   floor (peculiar velocities from growing structure are comparable at z ≲ 10⁴); genuinely
   uncertain, severity O(1) — dimer-fraction class, flagged not dramatized.
4. **b(v) and σ/m(v) extrapolations** beyond the registered anchors use the anchor-pair log
   slopes; the activation epochs move by O(1) factors under alternatives, the universality does
   not (it rides on Θ_crit ∝ v²).
5. **P at easy coat (0.6 MeV)** — conservative for activation (hard coat activates later but the
   descent rates dwarf the difference).

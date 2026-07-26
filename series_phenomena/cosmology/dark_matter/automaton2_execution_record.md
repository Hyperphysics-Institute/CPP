# AUTOMATON-2 EXECUTION RECORD (appended per leg; frozen 2801 prereg)

## LEG 1 — GATES: G1 3/3 PASS (Coulomb survives the directed relay), G2 PASS, **G3 FAIL (condensed-phase class)** — STOP + RE-PREREG, with the failure diagnosed as a DENSITY PHASE PHENOMENON the founder's C26 predicted (Patch 2802)

**Executed 2026-07-25. Engine: `code/2802_automaton2_engine.py`
(FCC even-sublattice, native 12-neighbor adjacency; W_R
directed-front kernel field rule; C19/C20 verbatim CP rule, nothing
added). Reasoning: `reasoning/2802.md`.**

**G1 = P-A2-1 (quoted): 3/3 PASS — EMERGENT COULOMB SURVIVES THE
DIRECTED RELAY, more cleanly than under the A1 idealized shell.**
R = 2: normalized ρ ∈ [0.986, 1.044], Δp = 0.052. R = 3: ρ ∈
[0.991, 1.004], Δp = 0.011. R = 4: ρ ∈ [0.996, 1.002], Δp = 0.010.
(FCC parity note: axis samples at even r only — implementation
consequence of the sublattice, not a deviation.) The founder's
icosahedral hop relay (C22) produces inverse-square electrostatics
to ±0.4% pointwise at R = 4. Prediction P-A2-1: CONFIRMED.

**G2 (quoted): PASS.** Net charge conserved to −1.2e−11; L1 field
content trend −0.4% (bounded).

**G3 = D-A2-1 (quoted): FAIL under the frozen [W] bands.** Final
quarter of 2×10⁴ Moments at fill = 1/8, R = 3: mover fraction 0.034
(band ≥ 0.20); CPs in clusters ≤ 2: 38% (band ≥ 60%); max cluster
34 (band ≤ 8). Census: {1: 246, 2: 42, 3: 31, 4: 29, 5: 13, 6: 11,
7: 2, 8: 2, 11: 1, 12: 2, 15: 1, 19: 2, 21: 2, 34: 1}. Per the
frozen clause: STOP; no production; no Gibbs comparison ran.

**CRITICAL PHENOMENOLOGY (same-font): this is NOT the A1 quench.**
A1 froze absolutely (zero motion, total pile collapse). The A2 Sea
sustains a STEADY 3.4% per-Moment mover fraction for 20,000 straight
Moments — ~29 CPs in motion every Moment, indefinitely — with 28%
free CPs, a pair population, and a moderate cluster tail. Mover
identity (300-Moment census): activity is DISTRIBUTED — free CPs
1.8%/Moment, pair members 3.6%, small-cluster members 5.0%, large
clusters 1.8% — bond-scale churn everywhere, not edge stragglers.

**Post-FAIL diagnostics (sanctioned; the prereg names density as
the first axis):** fill = 1/16 → mover fraction 0.171 (5× the 1/8
value), 60% in clusters ≤ 2 (MEETS that band), one 55-CP droplet
(fails max-cluster). Fill = 1/4 → mover 0.001, a single 1344-CP
condensate holding 77% of all CPs. **Aliveness and pair-dominance
rise monotonically with dilution: the failure is a DENSITY-DRIVEN
CONDENSATION, the bonded ↔ condensed phase structure the founder's
C26 conditioned the bonded regime on ("the DPs are sufficiently
diffuse…") and D-A2-5 registered as a structural prediction.** The
persistent single droplet at 1/16 coexisting with a live dilute gas
is textbook phase-coexistence phenomenology: at supersaturated
density a condensate nucleates regardless of bands. The [W]
fill = 1/8 sat on the condensed side; the worker's choice, not the
founder's physics, set the density.

**Disposition:** STOP honored; the re-prereg (fresh patch) will
commit a PRINCIPLED fill axis (more dilute, per C26) with ALL BANDS
UNCHANGED — in particular the 0.20 mover band stays even though
0.171 was observed at 1/16, because lowering a band toward an
observed number is fitting the test to the answer. P-A2-1 stands
CONFIRMED regardless of G3. The 79.5% untouched; no panel action
(win packet assembles when the arc completes).

---

## LEG 2 — G3R (dilution ladder): BOTH FILLS FAIL AS FROZEN — STOP; phenomenology resolved to LIVE GAS + INERT CRYSTALLITES; a scale hypothesis registered for analysis before any further axis (Patch 2804)

**Executed 2026-07-25 under the frozen 2803 ladder. Both-fail branch
fires; per the freeze, its language is corrected same-font by the
data: this is NOT "no live gas phase" — the gas phase is
emphatically alive.**

**G3R fill = 1/32 (quoted):** mover 0.432 (PASS ≥ 0.20); clusters
≤ 2: 76% (PASS ≥ 60%); max cluster 21 (FAIL ≤ 8). Census {1: 164,
12: 1, 19: 1, 21: 1}. **G3R fill = 1/16 (committed leg, seed
2804):** mover 0.096 (FAIL); clusters ≤ 2: 92% (PASS); max 36
(FAIL). Census {1: 396, 36: 1}. **VERDICT: FAIL at both rungs; no
production; no Gibbs battery ran.**

**Droplet-fate diagnostic (4000 further Moments at 1/32):** the
three droplets are EXACTLY static — sizes 21/19/12 and free count
164 unchanged to the CP — neither growing nor evaporating: inert
A1-class micro-crystals embedded in a gas whose free CPs move at
~57% per Moment. Two-phase structure: **live gas + dead
inclusions.** The bare rule's gas is self-sustainingly agitated;
its condensed phase is kinetically frozen (droplet interiors have
no jostling neighbors to receive C24's thermalized KE, and no
environmental fluctuation cracks them on these timescales).

**SCALE HYPOTHESIS (registered for analysis BEFORE any further
axis; checkable from committed checkpoints, no new runs needed):**
the cluster definition (contact at ≤ 1.5 lattice units) presumes
bonded DPs are contact pairs — but in CPP's own scales the ZBW
amplitude is Compton-class, i.e., ENORMOUS in GP units, and C28's
"very shallow" oscillation is shallow relative to that scale, not
relative to one lattice spacing. **The 164 "free" CPs may BE the
bonded ZBW Sea** — dedicated cycling partners at multi-GP
separation, which a contact census misclassifies as unbonded gas.
Decisive tests, queued as the next analytical leg: (i) unlike-pair
correlation of the live gas (preferred partner distance?); (ii)
partner persistence (does each + CP keep the SAME nearest − partner
across Moments — dedicated bonds — or exchange constantly —
plasma?); (iii) per-CP displacement autocorrelation (the ZBW cycle
signature). If persistence is high at a preferred separation, the
live phase is the founder's bonded Sea seen at the right scale, and
the [W] cluster bands were operationalized at the wrong one.

**Founder questions surfaced (PD-006; no worker resolution):** (Q-a)
Does C30's chaining prohibition condemn compact droplets, or
specifically chain-geometry polymers? The ≤ 8 cap was a [W] proxy.
(Q-b) Is gas + inert-crystallite coexistence acceptable Sea
phenomenology (condensation nuclei), or must the true Sea evaporate
its droplets — and if the latter, is the C27 rogue-wave flux the
intended evaporation channel? These await the founder AFTER the
scale-hypothesis analysis, which may dissolve part of them.

**Disposition:** STOP honored; no bands changed at any point (the
0.20 band was retained through a 0.171 near-miss and is now
vindicated by the 0.432 at 1/32); next leg = the three
scale-hypothesis analyses on committed checkpoint data, then either
a re-operationalized G3 (only with founder-ratified physics
grounds) or the founder questions as posed.

---

## LEG 3 — SCALE-HYPOTHESIS ANALYSIS: **CONFIRMED — THE BONDED ZBW SEA IDENTIFIED** (Patch 2805)

**Executed 2026-07-25 on a 4000-Moment full trajectory recorded from
the committed 1/32 G3R state (archived:
`data/x3x4/automaton2_scale_traj.pkl.gz`). Gas subset: 102 CPs
(52 ± pairs); static droplet subset: 114 CPs.**

**Test (ii) — partner persistence (the decisive test): 100.0% at
EVERY lag — dt = 1, 10, 100, 500, 1000, 2000, 4000 Moments — against
a 2.0% random-assignment null. 52 of 52 pairs keep the SAME
dedicated unlike partner for the entire window. C26's dedicated
semi-persistent DP bond: EMPIRICALLY CONFIRMED.**

**Test (iii) — the ZBW cycle: pair separation oscillates through
SUPERPOSITION — range [0.0, 2.8] GP, mean 1.72, per-pair std 1.19 —
periodically (separation autocorrelation returning to 0.97–0.99
every ~10 Moments; velocity autocorrelation exactly 1.000 at lag
12). The turning radii sit at the lattice's √2 and 2√2: a quantized
swing superposition ↔ √2 ↔ 2√2. C28's shallow dedicated-pair
oscillation and C25's superposition-exit: EMPIRICALLY CONFIRMED.
D-A2-2's ZBW spectral signature is thereby delivered (period 10–12
Moments at this density/R).**

**Test (i) — pair correlation: the gas's unlike/like ratio is
effectively infinite at r ≈ √2 and 2√2 and background elsewhere —
the gas contains NO like-charge contact structure and consists
entirely of unlike pairs at the ZBW turning radii.**

**REFINED PICTURE OF RECORD:** the automaton's two phases are (1)
**the founder's bonded ZBW Sea** — dedicated ± pairs cycling through
superposition with lattice-quantized amplitude — and (2) inert
crystallite droplets (the A1 quench in miniature). The G3/G3R
"FAIL"s were the [W] contact-census misreading phase (1) as unbonded
gas: pairs mid-swing (beyond 1.5 GP) counted as singletons. The
frozen verdicts stand as written (bands are bands), but their
operationalization is now demonstrated wrong-scale by measurement.

**Same-font tension noted (not resolved):** partner persistence of
100% over 4000 Moments means ZERO partner switching at this density
— C27's rogue-wave dance is ABSENT here. The switching engine
evidently requires higher density (more overlapping far fields) or
droplet-boundary dynamics; at 1/32 the Sea is bonded but socially
frozen. Registered for the density-dependence characterization.

**Founder requests (PD-006; two rulings, now sharp and small):**
- **R-1:** ratify a re-operationalization of the D-A2-1 aliveness
  gate in C26's OWN terms — e.g., dedicated-bond fraction (CPs in
  ≥ N-Moment persistent unlike pairs) ≥ 60%, mover fraction ≥ 0.20,
  and max STATIC cluster ≤ 8 — so that G3RR tests the physics C26
  actually states. (Worker will not re-band after seeing data
  without founder authority; this is the fitting-the-test guard.)
- **R-2:** the droplet ruling as previously posed (Q-a/Q-b): do
  inert compact crystallites violate C30 (a CHAINING prohibition),
  and is Sea + crystallite coexistence acceptable phenomenology?

---

## LEG 4 — G3RR: FAIL AS FROZEN (B3, B4) — ARC AT NATURAL PAUSE; one freeze defect disclosed; the crystallite is a PLANAR SHEET (Patch 2808)

**Executed 2026-07-25 under the frozen 2807 bands (R-1/R-2
authority). Quoted:** B1 dedication 100% of mobile CPs (PASS ≥ 60%);
B2 mover 0.281 (PASS ≥ 0.20); B3 droplet-phase mass 58% (FAIL
≤ 30%), growth +0%; B4 worst gyration aspect ~4.9e8 (FAIL ≤ 6).
Census: 188 singletons + one 28-CP cluster. **VERDICT: FAIL; STOP
honored; production, ballistic test, and Gibbs battery remain
gated-out (honestly: NOT run).**

**DEFECT DISCLOSED (D-G3RR-1, same-font):** the [W] phase
definition ("static = droplet phase") conflated two populations:
the 28-CP crystallite AND ~97 PARKED SINGLETONS — isolated CPs
immobile for the whole final quarter, stuck where SSV_net rounds
below the displacement floor. The R-2 ruling concerned
crystallites; under a crystallite-only reading the droplet mass is
28/216 = 13% (would PASS B3, growth 0%). The frozen verdict stands
as written; the defect is recorded for any successor gate.

**FINDING (B4 is real, and remarkable):** the crystallite's minimal
gyration eigenvalue is ~0 — it is a PLANAR SHEET: a two-dimensional
± alternating facet, not a compact blob and not a 1D chain. The R-2
compactness reasoning did not anticipate 2D order; whether a salt-
plane facet violates C30's chaining prohibition is a genuine
doctrine question now backed by a concrete object.

**STATE OF THE BARE RULE (the arc's consolidated finding):** at
every tested density the bare Moment rule produces a THREE-component
mixed state: (1) a live, 100%-dedicated ZBW-cycling bonded Sea
(C26/C28/C25 confirmed by measurement); (2) parked singletons
(rounding-floor stasis of isolated CPs); (3) planar ± crystallites
(inert, bounded, 2D-ordered). A predominantly-live Sea did not
emerge at any tested configuration. Open physics questions for the
founder and/or panel: the parked-singleton population (is the
displacement floor the physical PSR quantization or a simulation
artifact?), the 2D sheet's doctrinal status under C30, and whether
C27's rogue-wave flux at higher density is the intended melting
channel for both.

**Disposition:** arc at NATURAL PAUSE; per the founder's economy
governance, the WIN PACKET now assembles for the five seats
(`conv001_2026-07_automaton_s4x_win_packet.md`) carrying the banked
results and the open questions.

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

---

## LEG 5 — CRYSTALLITE DIAGNOSTIC CAMPAIGN: the fault is located in the MODEL REGIME, not the founder's physics (Patch 2810)

**Executed 2026-07-25 at founder direction (win packet HELD), with
predictions frozen first (`automaton2_crystallite_diagnostic_predictions.md`,
Patch 2809). Scripts: `code/2809_scale_scan.py` + session diagnostics.
Reasoning: `reasoning/2810.md`. Characterization only — no verdict
class, no promotion consequence.**

### Findings against the frozen predictions

**P-X1 (floor census): FALSIFIED AS STATED, CONFIRMED IN SUBSTANCE.**
75% of static CPs are rounding-limited (band was > 80%). Decisive
detail: **0% of static CPs are force-free** — every one feels a
field, mean committed displacement 0.397 GP, just under the ½-GP
snap. They are not at rest; they are *quantized* to rest.
**Premise correction (same-font):** in the G3RR final state the
28-CP sheet is NOT static — all 28 members moved within 200 Moments.
The genuinely frozen population is the 126 parked singletons. The
"static crystallite" picture of leg 4 held only for the 2803 seed.

**P-X4 (scale test): CONFIRMED, dramatically.** At IDENTICAL density
(fill 1/4, N = 1728): R = 3 (13 CPs per PSR) → mover 0.000, a single
1447-CP condensate. R = 6 (325 CPs per PSR) → **mover 1.000, max
cluster size 1 — not one cluster anywhere.** Corrected-fill runs at
R = 6: fill 1/8 (160 CPs/PSR) mover 1.000, no clusters; fill 1/32
(80 CPs/PSR) mover 0.968, no clusters. **Condensation, crystallites,
sheets, and parked singletons are ALL artifacts of running with
PSR/spacing ≈ 1.5. With a Planck sphere that actually contains a
Sea, no structures form at any tested density — exactly the founder's
stated expectation.** (Disclosed: the scan's first two runs were
mislabeled 1/32 by a fill-arithmetic error; they were fill 1/4. The
error is corrected in the committed script and the comparison it
supports — same density, two R values — is unaffected.)

**Mechanism decomposition (fill 1/8):** R = 3 — ratio |SSV_net|/
SSV_abs mean 0.154 against a floor of 0.5/R = 0.167, so only 40%
clear the floor, median displacement 0.00 GP. R = 6 — ratio mean
0.364 against floor 0.083, 100% clear, displacement 2.12 GP. Larger
PSR both raises the ratio and lowers the floor in ratio-space; the
frozen phase at R = 3 is a quantization trap, not a bound state.

**P-X5 (turnover): NOT CONFIRMED — and the reason is a NEW and more
important finding.** At R ≥ 6 there are no structures to turn over,
but the motion is not thermal either: **velocity autocorrelation is
exactly −1.000 at lag 2 and +1.000 at lag 20 — every CP flipping in
rigid global lockstep, a synchronous-update period-2 limit cycle**
(displacement mean = median = 2.12 GP, zero spread). R = 3 movers do
the same at tiny amplitude. **No tested uniform-PSR configuration
thermalizes; the automaton lands on limit cycles, not chaos** — so
the founder's formation–dissolution equilibrium has never actually
been tested, because the thermal bath it presupposes was never
produced.

**The candidate desynchronizer — and it is the founder's own
physics.** The uniform PSR = R is a worker simplification (A1 DR-2,
carried into A2); C22/the founder's rule makes PSR
SSV_abs-dependent. Diagnostic proxy (PSR ∈ {4, 6, 8} bucketed by
local SSV_abs, declared a proxy, not doctrine): mover 1.000, no
structures, **displacement spread appears (mean 3.21 ± 1.59 GP vs
2.12 ± 0.00 uniform) and the lockstep degrades from exactly −1.000
to −0.902 at lag 2, with lag-1 autocorrelation collapsing to +0.012
and lag-3 to −0.075.** Variable range demonstrably begins to
desynchronize the Sea — a partial, encouraging, not-yet-thermal
result.

**P-X2 (perturbation/metastability): NOT RUN.** P-X3 (sub-GP
accumulation, a declared doctrine deviation): **NOT RUN.** Both were
frozen against the structures that the scale test has now shown to
be regime artifacts; running them would characterize an artifact.
Reported unrun rather than quietly dropped.

### Answer to the founder's question (model / limits / expectations / physics)

**The fault is the MODEL and its LIMITS; the founder's physics stands
untested rather than contradicted.** Three worker-side causes, in
order of severity: (1) **no scale separation** — PSR/spacing ≈ 1.5
where the framework needs ≫ 1; this alone manufactures every
structure we have been studying; (2) **displacement quantization** —
the ½-GP snap converts residual fields into exact stasis, creating
absorbing states with no analogue in a continuum Sea; (3) **uniform
PSR** — a simplification that removes the SSV_abs-dependent range
variation which is the founder's own mechanism and which the proxy
test shows begins to break the synchronous lockstep. The founder's
expectation (small stable population maintained by
formation/dissolution balance) requires a thermal tail; no tested
configuration produced one; the framework's prediction therefore
remains open, and the next automaton generation must earn a thermal
bath before any crystallite population is meaningful.

### Recommended next axis (worker recommendation; founder rules)

AUTOMATON-3 with (i) the founder's SSV_abs → PSR law as *physics*
rather than proxy (founder question: the exact law), (ii) PSR ≫
spacing by construction, (iii) sub-GP position accumulation or an
explicitly quantized-displacement justification, and (iv)
thermalization as the FIRST gate — no crystallite, Gibbs, or inertia
claim until velocity statistics show a tail rather than a limit
cycle.

---

## LEG 6 — THE EXAMINATION SEQUENCE: lock-in traced to ABSENT MOMENTUM; the founder's kinetic mechanism VALIDATED IN PROXY, with its predicted artifact found (Patch 2811)

**Executed 2026-07-25/26 at founder direction (document the
examination sequence). Script: `code/2811_velocity_proxy_diagnostic.py`.
Reasoning: `reasoning/2811.md`. All runs DIAGNOSTIC — no verdict
class, no promotion consequence, no doctrine change. C21 (bit content)
and C23 (no velocity memory; inertia in Sea arc configuration) STAND;
the velocity vector used below is a LABELED PROXY for arc-stored
inertia, run under the founder's explicit approval and with his stated
caveat carried: a hard-coded velocity cannot represent all
energy-transfer and axis-change variables exactly, so artifacts are
possible — and one was found (see §4).**

### §1 — Sequence step 1: random ZBW phase/axis initialization (founder's proposal)
Paired-DP init with random ZBW phase (superposed/√2/2√2) and random
3D axis; deterministic evolution thereafter; R = 6, N = 864, fill 1/8.
**Result: the founder's predicted heterogeneity APPEARS and PERSISTS**
— speed spread CV = 0.51 vs EXACTLY ZERO under uniform init; no
clusters at all (census: 864 singletons). **But lock-in returned:**
lag-2 velocity autocorrelation drifted −0.838 (early) → **−0.969**
(late). Diversity without exchange.

### §2 — Sequence step 2: the time-resolved regime (is short-window periodicity just fast ZBW, as the founder proposed?)
M = 64, R = 6, 40 sparse DPs, separation ≈ 8 GP ≫ step ≈ 2.7 GP, so a
ZBW cycle spans many Moments. **Two corrections to the worker's own
prior reading:** (a) the attractor is **period-4**, not period-2
(autocorr ≈ 0 at odd lags, ≈ −0.9 at lags 2, 10, 50 — all ≡ 2 mod 4);
the earlier "period-2" claim was itself undersampled. (b) The founder's
aliasing hypothesis is therefore PARTLY RIGHT — resolution was
misleading me — but does not dissolve the finding, because:
**DP CENTERS ARE PINNED. MSD scaling exponent α = 0.14** (2 = ballistic,
1 = diffusive, 0 = pinned); centers jitter 30–140 GP² over 1200 Moments
with no growth trend. **A center that cannot coast cannot collide,
cannot rebound, and cannot slowly re-orient anything — so the
randomization channel the founder identifies (multibody kinetic
collision directing SSV_net) has no stage to act on in the model as
built.** The gap is not a missing degree of freedom; it is missing
MOMENTUM: C23 stores inertia in the Sea's arc configuration, but the
model's state vector (positions + scalar charge field; C21 bits carry
charge/polarity/origin only) contains no rotational or orientational
state for that storage to inhabit.

### §3 — Sequence step 3: the velocity proxy (founder-approved) — **THE MECHANISM VALIDATES**
[W] proxy law: v ← v + η·σ_c·(SSV_net/|SSV_net|)·(|SSV_net|/SSV_abs);
x ← x + v (continuous positions — which also removes the ½-GP snap
floor); collisions within 1.0 GP → elastic exchange + energy-conserving
random re-orientation of the pair's relative velocity (the founder's
"varying the DP ZBW oscillation axis with each collision").

| coupling η | KE growth | MSD α | speed CV | collisions |
|---|---|---|---|---|
| 0.05 | 49× | 0.31 | 0.294 | 232 |
| 0.01 | 2.2× | 0.76 | 0.409 | 459 |
| 0.002 | 1.2× | 0.73 | 0.460 | 268 |

Long weak-coupling run (η = 0.004, 60 DPs, 2500 Moments):
- **LOCK-IN BROKEN.** Velocity autocorrelation decays smoothly
  (1.000 → 0.999 → 0.995 → 0.981 → 0.946 at lags 1/3/10/25/50) with
  **no alternation whatsoever** — the period-4 attractor is gone.
- **KINETIC TRAJECTORIES APPEAR.** MSD α = 0.76 (vs 0.14 pinned) —
  motion is now transport, approaching diffusive.
- **COLLISIONS OCCUR:** 797 events with axis re-randomization.
- **MAXWELL–BOLTZMANN SPEED STATISTICS.** CV = 0.513 against the 3D
  MB value 0.422; decile χ² vs a mean-matched MB distribution = 14.7
  on 9 dof — **MB-CONSISTENT**. (The η-scan brackets it: CV = 0.409
  and 0.460 at η = 0.01 and 0.002.)

**The founder's mechanism is validated in proxy: given momentum, the
kinetic trajectories, collisions, rebounds, and thermal speed
statistics he specified all appear, and the lock-in he said should be
impossible indeed becomes impossible.**

### §4 — The artifact the founder predicted, found and named
**Energy is not conserved: slow, roughly LINEAR heating** (KE last-half
/ first-half = 3.87× at η = 0.004; 49× at η = 0.05). Diagnosed cause:
the proxy applies field-derived momentum to CPs with **no back-reaction
on the field**, which is regenerated each Moment from positions alone —
an infinite energy reservoir. This is precisely the founder's stated
concern ("a hard-coded velocity … will not produce an exactly accurate
representation of all the variables, and so something will be
misrepresented"). Consequence for interpretation, stated plainly: the
proxy demonstrates that **momentum unlocks the dynamics and generates
thermal statistics**, but it is a DRIVEN system, not a closed one, so
it CANNOT be used to test C24's fluctuation–dissipation balance or
P-A2-3 (Gibbs). Those require the doctrine-true arc-inertia
implementation, in which the Sea both stores and returns the momentum.

### §5 — Consolidated state of the investigation
1. Emergent Coulomb: CONFIRMED twice (unaffected by everything since).
2. Bonded ZBW Sea with 100% dedicated partners: CONFIRMED (leg 3).
3. Crystallites/sheets/parked singletons: REGIME ARTIFACTS of
   PSR/spacing ≈ 1.5 and the ½-GP snap (leg 5) — the founder's
   formation–dissolution equilibrium remains untested, not contradicted.
4. Lock-in: traced to ABSENT MOMENTUM, not to missing degrees of
   freedom (this leg) — and broken the moment momentum is supplied.
5. The founder's kinetic-randomization mechanism: VALIDATED IN PROXY,
   with MB speed statistics as the strongest single indicator.
6. Remaining obstacle, precisely located: the model has nowhere to
   store arc inertia. Founder's own assessment recorded — a faithful
   implementation "would require FEM since every CP of every DP … is
   also carrying the arc momentum for other DPs," i.e. computationally
   very intensive; whether inertia is irreducibly collective (and thus
   inaccessible at any hostable lattice size) is now the open
   structural question for AUTOMATON-3 chartering.

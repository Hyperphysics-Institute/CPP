# PRE-REGISTRATION — MOBILE-SEA MOVING-SOURCE TEST (DRESSED DRIVE)

**Patch 2902. Written and committed BEFORE the dressed measurement is
executed. The git history is the evidence of ordering. The dressed drive
has NOT been read at commit time — only the validations of §6 and the
β = 0 numerical-floor calibration have been run.**

**Lineage.** This is the machine-language computation that Patches
2900–2901 collapsed the inertia roadmap onto, under three founder
rulings: (i) constant SSV_net / co-moving arcs as the solution path
(31 Jul, capture at
`founders_voice/founder_direction_constant_ssv_net_entrainment_2026-07-31.md`);
(ii) one primitive for all CPs, no arc compliance, emission unchanged by
state (31 Jul, capture at
`founders_voice/founder_ruling_universal_primitive_no_arc_compliance_2026-07-31.md`);
(iii) shell-broadcast ballistic propagation per the c05 spec (Patch 2893
spec-mismatch finding) with Branch-1 verified structure (Patch 2895:
ballistic, 1/r², isotropic, retarded by construction).

---

## §1 — THE QUESTION

The toy models (2884/2897/2900) show the drive on a coasting CP from a
**static** Sea carries β² curvature with the exact coefficient **c = 1/5**
(Patch 2900), which destroys the Newton-I coasting family (B1). The toy
also shows Sea entrainment **can** cancel the curvature (2900, Test 2),
but cannot decide whether the substrate's forced entrainment does so —
the answer lives in the near field where toy cutoffs are arbitrary
(Patch 2901).

**Question: in a substrate-level run where every Sea CP moves by the
primitive and nothing is adjustable, what is the curvature of the dressed
drive?**

## §2 — ENGINE SPECIFICATION (from spec, not from committed engines)

Deterministic pairwise retarded shell-broadcast N-body,
`code/2902_mobile_sea_engine.py`:

1. **Propagation** (c05 §§69–71; Branch 1 as verified at 2895): every CP
   emits a fixed quantum per Moment onto its growing spherical shell;
   reception amplitude from emitter e at receiver r is
   amp = 1/(4π R_ret²), where R_ret solves the retarded condition
   |x_r(t) − x_e(t′)| = c_lat·(t − t′), c_lat = 1. Ballistic, retarded by
   construction. Contribution direction = the bit's travel direction
   (emission point → receiver); sign = q_e·q_r (like charges push along
   travel, unlike pull against it).
2. **Emission is state-independent** (founder ruling ii): every CP, bound
   or free, moving or still, emits identically. No induced-response
   amplitude anywhere.
3. **Reception → motion** (the primitive, verbatim from the C19/C20 class
   used in every AUTOMATON engine): SSV_net = Σ signed vector
   contributions; SSV_abs = Σ amplitudes;
   step = min(|SSV_net|/SSV_abs, 1)·PSR along SSV_net. Applied
   **per-CP** — each member of a bound pair moves by the sum on its own
   position; arc stretch and restoring behaviour must emerge (ruling ii;
   implementation decision recorded at 2901 for founder correction).
4. **No self-force** (founder ruling, SF-6 arc): e = r excluded. Partner
   interaction included — pair binding and ZBW oscillation are outputs.
5. **Source**: one unbound CP, charge +1, advected at prescribed uniform
   velocity β·x̂ (backward-extrapolated pre-history; the Sea, initially
   undisturbed, equilibrates during the declared window — the dressed
   state is *reached*, not assumed).
6. **Sea**: neutral ± pairs (separation d₀ = 0.6, PSR = 0.5), pair
   centres on a regular grid (spacing 2.5) filling a cylinder about the
   source's path, transverse radius ρ ∈ [1.0, ρ_max], initial dipole
   orientations transverse-radial (x-reflection symmetric, so the β = 0
   axial drive vanishes by symmetry — the numerical floor measures the
   violation).
7. **Softening**: R² → R² + 0.05² (declared limitation; the primitive's
   step cap bounds motion regardless).

**Registered limitations:** open domain (finite cylinder) — SSV_abs at
the source is domain-dependent, so the **primary observable is the raw
axial SSV_net** (locally convergent; the entrained-dipole response falls
faster than 1/r³), convergence-tested per §5. Softening and the ρ = 1.0
inner exclusion are cutoffs; **both must be varied per §5 before any
verdict** — the 2901 lesson is that the answer may live in the near
field.

## §3 — OBSERVABLES

With ⟨·⟩ a time-average over the measurement window (declared per run,
after equilibration ≥ one light-crossing of the domain):

- **D(β) ≡ ⟨SSV_net,x at the source⟩** — the dressed drive.
- **Condition A (sign):** D > 0 (forward, along motion) ⟹ the Sea's net
  response is REPULSIVE ⟹ CONJ-FP-1 Condition A HOLDS. D < 0 ⟹ drag ⟹
  Condition A FAILS.
- **Curvature:** fit D(β)/β = k(1 − c_sub·β² − c₄·β⁴) over the β grid.
- **Entrainment profile:** ⟨Sea-CP drift velocity⟩ binned by position
  relative to the source — the forced co-moving profile, an output with
  no ε anywhere in the code.

**β grid:** {0.05, 0.10, 0.15, 0.20}, plus β = 0 (floor).

## §4 — FROZEN BANDS

Let F₀ = |D(0)| (the measured β = 0 floor) and require signal quality
Q: |D(β)| > 5·F₀ at every β, else **INCONCLUSIVE**.

| outcome | criterion | consequence |
|---|---|---|
| **CANCELLATION** | Q holds; sign of D uniform in β; **\|c_sub\| < 0.05** at the largest domain, stable under §5 variations | The dressed drive is linear at β²-order: the substrate's forced entrainment cancels the static-Sea curvature. The founder's constant-SSV_net travelling state exists at this order; LINK 3 passes at β²; the B1 conflict is resolved at the substrate level (c₄ then becomes the open order). |
| **RETAINED** | Q holds; sign uniform; **c_sub ∈ [0.10, 0.30]** stable under §5 | The curvature survives dressing at ~the static value. The conflict is real at substrate level; the remaining live options are the μ(v) cross-sector condition (B1 §5) or a primitive-level change. |
| **DRAG SIGN** | Q holds; **D < 0 at every β** | **Condition A FAILS.** CONJ-FP-1's mechanism yields drag; the conjecture is dead as stated regardless of curvature. |
| **INCONCLUSIVE** | anything else — Q fails, sign flips with β, c_sub outside all bands, or §5 instability | No verdict; state the obstacle. **Not reportable as support for either side. Re-banding after the result is forbidden.** |

**Worker expectation, declared in advance:** the steady-state argument of
Patch 2900 §3 (a travelling configuration time-independent in the
co-moving frame has no transients, and the curvature reads as a transient
of the undressed background) predicts **CANCELLATION**. Declared so that
a confirming result is weaker evidence than a disconfirming one, and so
these bands cannot move.

## §5 — CONVERGENCE REQUIREMENTS (2892 lesson: no verdict from one box)

A band verdict requires stability (c_sub moving < 0.05, sign unchanged)
under: (a) two domain sizes (ρ_max and cylinder length both increased
≥ 1.4×); (b) two inner exclusions (ρ_min = 1.0 and 1.5); (c) two
softenings (0.05 and 0.10); (d) doubled measurement window. Any
instability ⟹ INCONCLUSIVE with the obstacle stated.

## §6 — VALIDATIONS (run BEFORE the dressed measurement; committed with
this prereg)

- **V1 static pointing/falloff:** static source, frozen Sea: SSV_net at
  probe CPs points at the source and amp scales as 1/4πr² to numerical
  precision.
- **V2 ZBW pair stability:** an isolated pair remains bound and bounded
  over ≥ 500 Moments (binding is emergent, not imposed).
- **V3 β = 0 floor:** full configuration, source at rest: |D(0)| = F₀
  recorded; symmetry violation only.
- **V4 smoke:** moving source, mobile Sea, short run: energy of motion
  bounded (step cap respected), no numerical blow-up. **The axial drive
  is NOT read in V4.**

## §7 — STANDING

Executes under CONJ-FP-1 (no new registry ID). Condition B stands CLOSED
per 2895 and is not re-litigated here. Ledger untouched: 1B OPEN; PR7
PARTIAL; six of seven; B7 holds DM-1/2/3; Candidate (B) 79.5%. G1 and
P-A2-1 stand; statics suspension per 2892 stands; 7 July
no-carried-velocity ruling stands.

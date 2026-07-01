# Mechanism (revised velocity sector) — Strip-then-Fuse — DM-1

**STATUS: STAGED, founder-gated. Post-v1.0 companion note. Supersedes step 5 ("velocity dependence") of
`mechanism-DM-1.md` PENDING founder approval + a CONV-001 panel pass.** DM-1 stays v1.0; this note documents
the corrected velocity mechanism assembled in patches 1815–1826 (30 June 2026, Opus lane). It does not edit the
v1.0 papers. Layer C throughout (order-of-magnitude, CPP-geometry-dependent — not framework-free). **CONV-001
round 1 CLOSED (4/4: ChatGPT, Grok, Copilot all SwC; Gemini NOT-SOUND engaged) — net SOUND-WITH-CHANGES; see
"Panel review" below. JUNCTION: founder edge-hinge (1831) corrects 1830 — self-limiting SECURED; κ_θ static pin
FAILED by Earnshaw (1834, 1833 static RETRACTED) → real κ_θ is ZBW-dynamic; founder gradient read (1835): scissor
mode considerably softer → κ_θ ~0.05–0.23 MeV (sub-E_ee, below threshold) → cluster floor ~0.4–0.8 VIABLE on
dynamic physics; (1836) floor verdict collapses to a SCALE-FREE ratio g = κ_scissor/κ_bend < 6/N (Earnshaw +
all absolute scales cancel); **SF-2/SF-5 delivered G1a (OPEN-SS-40, patches 2200–2202) and DM consumed it (1839):
the ponderomotive |E|²-curvature resolves Earnshaw, g ≈ 0.02 ≪ g_crit=0.43 (~17× margin, corpus-pinned via the
no-sub-Coulomb screening argument) → cluster floor VIABLE, direction robust, lands ~0.4–0.8 (whole band ≤ cluster
bound ~1.0); stiff-ribbon/soft-scissor tension dissolved (same bond, ratio → requirements reinforce; junction is
the softer of two STIFF modes, not fragile). EXACT floor (0.4 vs 0.8) + G1b absolute κ_θ pending the ZBW
amplitude = OPEN-FP-SF-2-η. NO promotion on the floor alone — G1b/G2/G3 (OPEN-SS-39) open.**

## Why this note exists (the revision)

DM-1 v1.0's velocity-dependent σ/m — the signature that cores dwarfs and frees clusters — was carried by a
**fragmentation** picture (`mechanism-DM-1.md` step 5): cluster collisions deposit ~MeV, exceed an edge-bond
window, and **break the rod in two**, lowering N (σ/m ∝ N). Thomas's 29 June geometry correction
(`founders_vision.md`, patches 1815/1817) removed the basis for that picture, and the collisional program
built to replace it converged on a different, self-consistent mechanism: **strip-then-fuse**. The qualitative
signature (dwarf cores, cluster suppression, σ/m falling with v) **survives**; its mechanism is replaced.

## The geometry correction that forced the revision (1815/1817)

The rod's central core is a **continuous, uniform E_qq color spine** — every transverse plane identical, no
intra/inter-element segregation. The eCP shell (E_ee) is **not** the longitudinal scission bond; it is a
secondary outer-radius **bending-stiffness** layer at larger lever arm. Pinned scales: E_qq ≈ 66 MeV (= α_s
ℏc/d), E_ee ≈ 0.9 MeV, m_element = 4 qDP + 4 eDP ≈ 1408 MeV, d ≈ 1.0–1.3 fm.

## Three walls the old fragmentation picture hits — and why nothing dynamical clears them

With a uniform E_qq core, **fragmentation is suppressed at all dark-matter velocities** (patches 1816–1820):
1. **Energy wall.** Severing one cross-section costs ~n_w²·E_qq ~ 600 MeV; a cluster collision delivers ~0.5
   MeV — a ~1000× gap (1818, 1820). Direct cut, cumulative damage, and a phonon mechanism all fail for the
   *same* gap (mechanism-independent). The crack arrests at the 73×-tougher core (v_through ~ 10⁵ km/s).
2. **v_pen wall.** Driving two cores into contact through their coats needs v_pen ~ 1.1×10⁴ km/s with
   local-patch backing — above cluster velocities (1816).
3. **Repair gate.** A stripped spot's bare core is locally re-coated by the eDPs just knocked off (Thomas's
   correction; the Sea is not depleted) — so the bare spot does not simply persist.

The conclusion of 1820 was stark: a uniform core gives **velocity-independent** σ/m, in tension with the data —
**unless** a mechanism clears all three walls. Strip-then-fuse does.

## The strip-then-fuse mechanism (Thomas), clearing all three walls

1. **Strip (cheap).** A cluster-velocity collision strips the eCP coat (E_ee scale, ~MeV — achievable, 1818)
   at the contact, exposing bare E_qq color on both rods. **No core cut — clears the energy wall.**
2. **Penetrating tail (clears v_pen).** The cores reach color range only in the *penetrating tail* of
   collisions: **perpendicular, central** hits on **long** rods, where the **rod-tail inertia** backs the
   contact and the KE held in the DP Sea (SF-6) **sustains** the relative velocity (no instant rebound). With
   that backing the threshold drops from ~1.1×10⁴ to **v_thr ~ 1500–2200 km/s** (1822, 1824) — into the
   cluster band.
3. **Force-balance gate (1824).** The penetration depth δ* is the crossover where the cores' E_qq attraction
   equals the eDP-coat E_ee repulsion. Confined color switches on at R_color ~ d and overwhelms E_ee by ~73×
   there, so δ* ~ the color range ~ d ⇒ δ*/d ~ 1 ⇒ v_thr ~ 1770 km/s (central). **Clears the repair gate:**
   color (≫ recombination, by the electric-vs-color hierarchy) wins once the cores are inside the range.
4. **Fuse (downhill).** Two bare cores in range fuse exothermically into an **X-cross** (a central glueball
   joining four arms shorter than the reactant rods). Number-decreasing; rate rises with velocity.

## The observable: a velocity-THRESHOLD σ/m(v)

Per-fusion σ/m drop (1823): the X scatters as a more compact / flexibly-jointed object → σ/m_X/σ/m_rod ∈
**[1/8 (flexible), 1/2 (rigid)]**; the single-point glueball favors the flexible end. The full convolution —
velocity distribution × impact angle × impact position × N-distribution, with the **cumulative** fused
fraction f_fused = 1 − exp(−N_coll·p_pen) — gives (1825):

| environment | v_rel (km/s) | σ/m (cm²/g) |
|---|---|---|
| dwarf / galaxy / group | ≲ 900 | **~3.1** (cores) |
| cluster | ~2300 | **~0.8** |
| Bullet / mergers | ~3600+ | **~0.2** |

**σ/m falls from ~3.1 (dwarf cores) to ~0.8 (clusters) — a factor ~4 — with a falsifiable KNEE at ~1000–1500
km/s** (a threshold, not a power law: distinct from light-mediator v⁻⁴ SIDM). Two couplings make it work: v_thr
is N-dependent (long rods penetrate easier *and* dominate σ/m), and the suppression compounds over the cluster
collision history.

## Self-limiting (1826) — built into the penetration physics, no runaway

Crossing-point fusion **shortens the rigid segment**; v_thr ∝ 1/√N, so each fusion raises the threshold by
~√2. After **k ~ 1–2 fusions** v_thr exceeds the local velocity and fusion **stalls**. The same v_thr that
*gates* fusion *self-limits* it. The floor is bounded and velocity-dependent (~3.1 dwarf → ~0.8 cluster → ~0.2
mergers), sitting **far above** the no-self-limit runaway fixed point (~0.07) — **no over-depletion.** (A floppy
d_f ~ 2 aggregate's coil-σ/m saturation is a secondary backstop; segment-shortening self-limits first.)

## Inputs (pinned/geometric) and the O(1) knobs (flagged)

Pinned/corpus: E_qq, E_ee, m_element, d, α_s, the electric-vs-color hierarchy (α_s/3α)² ≈ 311, v_sound =
√(E_qq/m_element) ≈ 0.22c, the optical-depth N_scatter. Geometric: perpendicularity acceptance, impact-position
backing, δ*/d ~ 1 (force balance). **O(1) knobs (flagged, not fit):** per-fusion drop ∈ [1/8, 1/2]; N_char
(formation length, sets σ/m₀); the N_coll normalization; the segment-halving model for k_max.

## Honest stress points (for the panel)

- **Cluster floor (~0.8) is upper-band** — the tightest constraint and where the candidate is most exposed.
  Improves for smaller N₀, smaller per-fusion drop, or a fatter velocity tail; **worsens to ~1.6 if the
  X-junction is rigid** (drop ~ ½). So the flexible-junction claim (1823) is load-bearing.
- **R_color ~ d** is the load-bearing input behind v_thr ~ 1770 (1824); a notably sub-d color range pushes
  v_thr up and the typical-cluster tension back.
- **Segment-halving** (k_max) is a model approximation; the *self-limiting* (monotonic v_thr rise) is robust,
  the exact floor is not.
- **N_coll** couples the curve to the optical depth; representative, carries O(1).

## Panel review (CONV-001 round 1) — verdicts, dissent engagement, and the folded sharpening

**Returned 4 of 4 — round 1 CLOSED** (30 June 2026). ChatGPT **SOUND-WITH-CHANGES**; Grok **SOUND-WITH-CHANGES**;
Copilot **SOUND-WITH-CHANGES**; Gemini **NOT-SOUND**. *(Attribution correction: an earlier fold labeled the
recurring SwC review "ChatGPT"; that review is Grok's. ChatGPT's distinct review — verdict table, R_color
"RESTATE-WITH-FIX", explicit three-wall grading — arrived separately and is folded below.)* The three SwC
reviews and Gemini's dissent **converge** on the same load-bearing items, and engaging Gemini's objections on the
merits sharpens them. (Honor-don't-outvote: Gemini's four points are answered individually below, not dismissed
by tally.)

**Gemini Obj 1 — "rigid core ⇒ rigid joint; can't be stiff and floppy." DISSOLVED.** The objection conflates
two independent stiffnesses. The E_qq bond gives high **stretch** stiffness (resists pulling the spine apart →
no fragmentation); the X-junction's **angular/hinge** stiffness (resistance to the four arms *pivoting* about a
single-point glueball contact) is a *different* property and is the actual unknown. A strong but spatially
localized bond can be angularly compliant — two stiff rods spot-welded at one point still scissor. So
"stretch-stiff core + angular-flexible junction" is not a contradiction. **What survives** is not Gemini's
contradiction but the shared concern (ChatGPT, Copilot too): the junction angular stiffness is **asserted, not
derived**. That is a real residual — see the sharpening below.

**Gemini Obj 2 — "R_color ~ d is numerology." FAIR CAUTION (partly answered).** Copilot defends it directly:
the qDP bond length *is* d and the qDP transverse size is O(d), so the residual-color range between exposed
cores is ~d. ChatGPT and Gemini are right that the note *asserted* it. Fold: R_color ~ d traces to the qDP bond
length/size (both ~d); it is **load-bearing** and wants an explicit strong-sector (SF-5) support, and the v_thr
sensitivity to it must be stated (a 0.7d range pushes v_thr up by ~1/√0.7 ≈ 1.2× → ~2100 km/s, tightening the
cluster end). Not numerology, but not yet derived either.

**Gemini Obj 3 — "flexible joint ⇒ decoupled arms ⇒ full backing ⇒ no self-limiting." INVALID — backwards
(verified numerically).** If the joint is angularly flexible, the arms *are* decoupled — so a later collision
on an arm is backed by **only that arm's** (shorter, N/2) inertia, giving v_thr(N/2) ≈ 4050 km/s, **higher**
than the parent rod's 2865. Threshold **rises** → fusion stalls. The *rigid* joint is the dangerous case:
whole-X backing (2N) gives v_thr ≈ 2025 km/s, **lower** → runaway. So the flexible joint **is required for**
self-limiting; it does not contradict it. Gemini inverted the inertial bookkeeping.

**Gemini Obj 4 — "Sea backing ⇒ strongly-interacting fluid ⇒ drag ⇒ violates collisionless DM." INVALID
(conflation), but worth a disclosure.** The SF-6 backing is **transient, local** collisional energy-routing at
the contact (fm/fs scale) — KE briefly held in Sea modes instead of rebounding instantly. It is **not** a
sustained macroscopic ram pressure. Uniform motion of a rod through the Sea is **drag-free by the SR-1
construction** (the Sea is the Lorentz-invariant vacuum; if it dragged DM it would drag ordinary matter too,
since it is the same medium EM propagates through). The vacuum mediating a violent collision without dragging
uniform motion is exactly how the EM vacuum already behaves. No dynamical-friction / large-scale-structure
problem. The note should say this explicitly.

**The sharpening (the round's decisive result).** Obj 1 and Obj 3, properly answered, collapse the candidate's
exposure to **one property: the angular (hinge) stiffness of the single-point glueball junction** — and that one
property controls **both** open numbers, which therefore **stand or fall together**:

| junction angular stiffness | per-fusion drop → cluster floor | post-fusion backing → self-limiting |
|---|---|---|
| **flexible** (point-contact pivots) | ~1/8 → **σ/m ≈ 0.8** (viable) | arms decoupled (N/2 backing) → v_thr **rises** → **stalls** |
| **rigid** (locked cross) | ~1/2 → **σ/m ≈ 1.6** (in tension) | whole-X backing (2N) → v_thr **falls** → **runaway** |

This refutes Gemini's "cannibalizes its own logic" charge: the model consistently needs **stretch-stiff +
angular-flexible**, and *both* desired behaviors (low floor, self-limiting) follow from the *same* angular
flexibility. The junction angular stiffness is therefore the **one number we can compute next** that settles two
open items at once.

**ChatGPT's correction (folded, honored): it is not a *single* question — it is a coupled package.** ChatGPT's
genuine review (SwC) flags that the make-or-break is the **coupled trio** of (i) the color range R_color, (ii)
the penetrating-tail *rate*, and (iii) the flexible-X transport suppression — not the junction stiffness alone.
That is correct, and it tempers the round-1 framing: the junction stiffness is the *most computable* of the
three and uniquely controls floor + self-limiting together, but R_color and the tail-rate are **co-load-bearing**
and must not be treated as settled while the stiffness is pinned. ChatGPT additionally grades the three walls
unequally: the **energy wall** is cleanly cleared (strip, don't cut), but the **v_pen wall** ("conditionally
yes — geometry/distribution-sensitive") and the **repair gate** ("conditionally yes — only if color capture at
range outruns recoating") are the *less secure* two, and both lean on the same color-range physics as R_color.
So R_color is not one isolated knob; it propagates into the repair gate and the tail-rate as well — which raises
its priority. ChatGPT also rightly calibrates the layer label: **Layer C here means an order-of-magnitude
estimate, NOT "framework-free"** — the mechanism depends throughout on CPP-specific geometry (color range,
recoating, rod-collision kinematics, X-junction transport). The earlier "framework-free" phrasing (in the panel
cover) is withdrawn; "Layer C, CPP-geometry-dependent" is the accurate label.

**Net panel position (round 1 CLOSED, 4/4): SOUND-WITH-CHANGES** — 3 SwC (ChatGPT, Grok, Copilot) + 1 NOT-SOUND
(Gemini, engaged). Folded changes: (a) distinguish stretch- vs angular-stiffness and name the junction angular
stiffness as the make-or-break controlling both the floor and the self-limiting (above); (b) elevate **R_color ~
d to a named live risk, NOT a settled input** — ChatGPT "RESTATE-WITH-FIX", Grok "needs SF-5 support", Gemini
"numerology": the three-reviewer consensus pressure, and it propagates into the repair gate and tail-rate, so it
ranks alongside the junction stiffness (record the qDP-bond-length identification + the v_thr sensitivity, flag
SF-5 support as required, keep it live); (c) add the Sea-drag clarification — transient local energy-routing,
uniform motion drag-free per SR-1 (Obj 4); (d) grade the three walls unequally (energy clean; v_pen and repair
conditional, color-range-sensitive); (e) withdraw "framework-free" — Layer C = order-of-magnitude,
CPP-geometry-dependent. Gemini's NOT-SOUND is **recorded as a standing dissent**: its two valid pressures
(junction stiffness underived; R_color wants strong-sector support — both now shared by the SwC majority) are
preserved; its two invalid points (Obj 3 backwards; Obj 4 conflation) are rebutted with the reasoning above.
**No promotion** — ChatGPT explicitly endorses only a *staged, founder-gated* CONJ-COSMO-1 discussion and "does
not yet justify treating the velocity curve as final"; concur. **DM-1 stays v1.0; CONJ-COSMO-1 founder-gated.**

## Junction angular stiffness — first calculation (1830): the cluster floor leans tense

The coupled-trio calculation the panel asked for has been run on its decisive leg (`code/1830_...py`). A
junction is angularly **flexible (a hinge)** — the case the ~0.8 floor needs — **iff κ_θ < 3B/L_arm** (pivoting
the junction is cheaper than bending the arm). With the arm flexural rigidity from the E_ee shell, B ≈ 0.71
MeV·fm, the threshold is **3B/L_arm ≈ 0.15–0.53 MeV** for the relevant arms (N = 28…8) — **below E_ee.** The
natural junction scale is ≥ E_ee ≈ 0.9 MeV (color-knot reorganization), up to E_qq ≈ 66 MeV if color-continuous;
either **exceeds** the threshold. So the junction **leans rigid-to-marginal, not clean-flexible**, giving
per-fusion drop ~1/3–1/2 and **cluster floor ~1.0–1.6 cm²/g — mild-to-moderate tension**, not the 0.8 assumed in
round 1.

Two partial mitigations: the crossing geometry **excludes** the fully-rigid E_qq limit (no continuous
perpendicular spine → the junction is a knot, removing the 1.6 worst case but landing near the E_ee-marginal ~1.0
case); and 3B/L_arm ∝ 1/N means **shorter arms are more flexible**, with self-limiting stopping fusion at short
arms (the late, floor-setting junctions are the most flexible). Neither rescues it: flexibility still needs κ_θ ≲
0.3–0.5 MeV (sub-E_ee), not guaranteed. The other two legs move the **same** way — sub-d R_color and a thinner
penetrating tail both *raise* the floor — so the trio's risks add rather than cancel.

**Revised floor reading:** bracket **[0.8 flexible (now disfavored) — 1.6 rigid (geometry-excluded)], computed
lean ≈ 1.0–1.5 (tense).** The clean 0.8 is downgraded to the optimistic edge. **The velocity-sector viability now
rides on one SF-5 number:** the angular energy U(θ) of a 4-arm color knot — κ_θ ≲ 0.4 MeV rescues the 0.8 floor;
κ_θ ≳ E_ee leaves the cluster tension standing. Not falsified (B carries an O(1) area-moment factor; SF-5 could
find sub-E_ee softness), but the cluster end is now the make-or-break, consistent with all four reviewers'
concern. **No promotion — more exposed, not less.**

## Founder's junction mechanism — the qq edge-hinge (1831): corrects 1830, floor → ~0.8–1.0

Thomas supplied the junction-formation sequence, and it **corrects 1830's category error.** Two
velocity-qualified rods strip a single eDP each; the 8qDP cores appose at 90°; **neither core fractures** and
**no glueball forms** (the collision is below the transverse-plane fracture energy — the established energy
wall); a **single strong qq bond forms between the two edges** — a literal hinge, like two hTetras bonded on
apposed qq edges. The rods' rigidity prevents bending into a full-face 8qCP bond, so they stay **edge-bonded and
free to hinge.**

**Where 1830 was wrong:** it tied the junction angular stiffness to the **bond depth** (modeled a knot, κ_θ ≥
E_ee) and concluded a tense floor. For an **edge** bond, rotating about the edge **does not stretch the bond** —
so E_qq sets only the **stretch** stiffness (holds the junction, forbids fragmentation), while the **hinge
(dihedral) stiffness is decoupled** and set by secondary coat/steric effects (≲ E_ee). This is the
mechanism-level realization of the stretch-stiff + angular-flexible split — now grounded, not assumed. Three
consequences, all favorable vs 1830:

1. **Hinge stable.** A one-point edge hinge folds by rotating about the edge (rods go coplanar/side-by-side),
   **not** stacking face-to-face; the rigid face-bond needs a translation a single-point hinge + rigid rods
   cannot supply → the face-bond is **geometrically inaccessible**, no hinge→rigid conversion channel.
2. **Self-limiting SECURED.** The free hinge **guarantees** inertial decoupling (arm backs penetration with its
   own N/2 inertia → v_thr rises → stalls); the rigid-junction runaway required a rigidity the hinge lacks. The
   1828/1830 runaway worry is **removed by the mechanism.**
3. **Cluster floor → ~0.8–1.0.** Wide kinematic dihedral range → substantial orientation-averaging if soft.
   Floor ≲ 0.8 as long as the **residual dihedral stiffness κ_θ ≲ 0.4–0.5 MeV (sub-E_ee)** — plausible for a
   geometric hinge with secondary coat/steric restoring torque and one of four eDPs already stripped.

**Revised floor (supersedes the 1830 reading):** the 1830 "tense ~1.0–1.5" lean was an artifact of the wrong
(knot) junction model and is **partially retracted.** With the edge-hinge: floor **~0.8 (soft hinge) to ~1.0
(E_ee-scale dihedral bias)** — favorable-to-marginal, not tense. The make-or-break re-sharpens to **one tractable
number: the dihedral restoring torque of a single locally-stripped qq edge-hinge** (coat + steric) — a
one-junction calculation, no longer the strong-sector 4-arm-knot problem. **Still no promotion** (κ_θ ~ E_ee
would land at ~1.0); founder mechanism STAGED for `founders_vision.md`.

## κ_θ computed (1833): ~0.27 MeV (sub-E_ee), cluster floor ~0.8, viable-to-marginal

The make-or-break number is now computed (`code/1833_...py`). The hinge bond is hinge-soft, so κ_θ comes from the
**perimeter eCP charges** near the hinge, whose separations change with the dihedral: nearest pair at ~d, r(φ) =
2d sin(φ/2), U = kq²/r with kq² = E_ee·d. With alternating-perimeter partial cancellation and the locally-stripped
contact (1 of 4 eDPs gone), **κ_θ ≈ 0.27 MeV (best), ~0.2–0.5 MeV over O(1) charge-count/cancellation** —
**sub-E_ee**, confirming the edge-hinge softness. Against the flexibility threshold 3B/L_arm, κ_θ ≈ 0.27 is
**below** it for the floor-setting post-fusion arms (N = 14 → 0.30; N = 8 → 0.53), i.e. **those junctions hinge**
→ per-fusion drop ~1/4 → **cluster floor ≈ 0.8 (range 0.4–1.0)**. The candidate lands **viable-to-marginal**,
**clearing the 1830 tense scenario.** The full σ/m(v) curve (~3.1 dwarf → ~0.8 cluster → ~0.2 mergers, knee
~1000–1500 km/s) now rests on a **computed** junction stiffness.

**Residual:** κ_θ ≈ 0.27 sits *close* to the N = 14 threshold (0.30), so it is flexible-but-not-by-much; the O(1)
perimeter charge-count/cancellation could move it to ~0.5 (floor ~1.0, marginal) or ~0.15 (floor ~0.4, comfortably
viable). Pinnable by the full dihedral Madelung sum over the **28 June alternating-charge-square** perimeter — an
in-corpus calculation, not a strong-sector unknown. **Still no promotion** (floor marginal until κ_θ is pinned).

## κ_θ pin attempt (1834): static sum FAILS by Earnshaw — the 1833 static number is RETRACTED

The full alternating-square dihedral sum was run to collapse the range. **It did not — it broke the static
method.** Across 24/25 geometries the static dihedral stiffness κ_θ(90°) is **negative** (90° is an electrostatic
*maximum*): this is **Earnshaw's theorem** (a static point-charge cluster has no stable equilibrium; by Laplace
the curvatures sum to zero). The 1833 static ≈ 0.27 MeV was a two-term subset that hid the net instability and is
**retracted.** Static electrostatics cannot supply the hinge restoring torque.

The stiffness is therefore the **ZBW dynamic (ponderomotive) stiffness** — the *same* mechanism Thomas posited
for the rod's longitudinal E_ee (28 June, `founders_vision.md`): cycle-symmetric oscillation time-averages to a
second-order restoring force that stabilizes what statics cannot. So the Earnshaw failure **re-derives the
dynamic-stiffness mechanism from the DM side.** Scale: the longitudinal dynamic stiffness *is* ~E_ee; the hinge
is a softer mode, so κ_θ^dyn ~ f·E_ee, f ~ 0.1–1 → **~0.1–0.9 MeV → floor ~0.4–1.6, lean ~0.8–1.0.** The range is
**not collapsed — relocated** to a ponderomotive dihedral calculation needing the ZBW frequency/amplitude.

**Net:** cluster floor stays **viable-to-marginal (~0.8–1.0), genuinely undecided**, now correctly a
dynamic-stiffness quantity. **Self-limiting and hinge stability (1831) are unaffected** (kinematic/geometric,
κ_θ-independent). No promotion; the ponderomotive dihedral calc is the real make-or-break.

## Founder gradient read (1835): scissor mode considerably softer → floor VIABLE

Thomas's physical read settles the *direction* of the dynamic stiffness. The longitudinal stiffness is the E_qq
compression between **face-to-face 8qCP cubes** (close, steep SSV gradient); the hinge bonds sit **farther apart**
(eDP coat pairs across the hinge; qDP pairs near the hinge but past the face-to-face core) and at **variable
distance**, so the SSV gradients are "considerably softer, and variable along the lever arm." Since the
ponderomotive stiffness goes as the **gradient squared**, which falls steeply with separation, "farther apart" is
a strong suppression: f = (d/r_hinge)^p gives **f ~ 0.05–0.25** even at r_hinge ~ 2d → **κ_θ ~ f·E_ee ~ 0.05–0.23
MeV — sub-E_ee and below the flexibility threshold** (0.30 at N = 14). (Reinforcement: the near-hinge qDP pairs at
90° are beyond color range R_color ~ d, so they interact electrically, not via color — sub-E_qq.) Hinge flexible →
drop ~1/8–1/4 → **cluster floor ~0.4–0.8 → VIABLE.**

**Direction now doubly supported** (founder structural read + ponderomotive gradient scaling agree, independently)
— the floor lands in the allowed band on correct (dynamic, non-Earnshaw) physics, the first time in this arc it
does so without an assumed flexibility. **Exact floor (0.4 vs 0.8) still pending the full ponderomotive calc**
(ZBW freq/amplitude + SSV gradient law); a shallow-gradient branch (p ≲ 2) could still reach ~1.0 marginal. **No
promotion** until that calc; the verdict *direction* (viable) no longer depends on it.

## κ_θ resolves to a scale-free ratio (1836): floor verdict = g < 6/N, unified with the edge-bond SSV potential

Running the full κ_θ converges on the corpus's **own edge-bond SSV potential** — the **G1 make-or-break** flagged
25 June, which sets the ribbon ℓ_p and per-rung E_ee. The X-junction dihedral stiffness **is** that same qq-edge-
bond angular stiffness. Since κ_θ (scissor) and the arm rigidity B (in-line bend) are the **same potential in two
geometries**, the flexibility test κ_θ < 3B/L_arm collapses to a **scale-free ratio**:

  **g ≡ κ_scissor/κ_bend < 6/N** (= 0.43 at N = 14)

and the absolute stiffness, kT_form, ZBW frequency/amplitude, **and the static-vs-dynamic (Earnshaw) sign
question all CANCEL** — whatever stabilizes the bend stabilizes the scissor the same way. Only geometry survives.
Thomas's read fixes it: the scissor is the same bond with the rods **perpendicular** (off-hinge charges farther
apart than the in-line ribbon bend), so g ~ 0.06–0.30 — **below 0.43 → flexible → floor ~0.4–0.8 → VIABLE.**

This **unifies** the DM cluster floor, ℓ_p, and E_ee onto **one edge-bond SSV potential** (the existing 25 June
make-or-break), and makes the verdict robust to every absolute-scale uncertainty that broke 1833 (bouncing
static value) and 1834 (Earnshaw) — both of which **cancel in the ratio**. **Definitive g** = that potential
evaluated in scissor-vs-bend geometry (open SF-2/SF-5 calc). **No promotion** until then; but the floor now hangs
on a calculation the programme already prioritizes, not a DM-specific unknown, and the anchored estimate is
viable. (1834's Earnshaw finding stands for the full static config but is moot for the ratio.)

## Relation to DM-1 v1.0

DM-1 v1.0 stands: the species (Cross-Rod), the σ/m = 0.11·N floor, the no-corona closure (OPEN-COSMO-DM-3), and
the dwarf-cores result are unchanged. **This note replaces only the *velocity mechanism*** — fragmentation →
strip-then-fuse — and only **upon founder approval + a panel pass.** Notably, the same early-coat / balanced-
late-Sea physics that closed the corona (OPEN-COSMO-DM-3) is what makes the strip-then-fuse penetration the
operative channel — one root, both results.

## Patch trail

Geometry correction 1815/1817 · walls 1816 (v_pen) / 1818 (bending fork) / 1819 (shell-strip σ/m) / 1820 (no
shortening) · strip-then-fuse 1821 (gate) / 1822 (penetration tail) / 1824 (force-balance δ*) · curve 1823
(per-fusion drop + first curve) / 1825 (full convolution) · self-limiting 1826.

## Disposition

STAGED for founder review. **CONV-001 round 1 CLOSED (4/4, net SOUND-WITH-CHANGES). Junction: founder edge-hinge
(1831) secures the self-limiting; κ_θ static pin FAILED by Earnshaw (1834) → the stiffness is ZBW-dynamic
(ponderomotive), the same mechanism as the rod's longitudinal E_ee (28 June); and the founder's gradient read
(1835) settles its direction — the scissor mode is considerably softer than the longitudinal compression (hinge
charges farther apart, softer/variable SSV gradients), so κ_θ ~0.05–0.23 MeV (sub-E_ee, below threshold) →
cluster floor ~0.4–0.8, VIABLE.** This is the first point in the junction arc where the floor sits in the allowed
band on correct (dynamic) and founder-grounded physics. The remaining tightening is the **full ponderomotive dihedral calc** (ZBW frequency/amplitude + SSV gradient law,
shared with the 28 June longitudinal derivation) — removes the 0.4-vs-0.8 residual; only a shallow-gradient
branch could still reach ~1.0 marginal. **Update (1836): the calc converges on the corpus edge-bond SSV
potential (the 25 June G1 make-or-break), and the floor verdict collapses to a SCALE-FREE ratio g =
κ_scissor/κ_bend < 6/N — in which the absolute scale, kT, ZBW params, and the Earnshaw sign question all cancel.
Founder geometry → g ~ 0.06–0.30 < 0.43 → VIABLE.** The DM floor, ℓ_p, and E_ee are now unified onto **one
edge-bond SSV potential**; the definitive g is that potential in scissor-vs-bend geometry (open SF-2/SF-5 calc,
now closing three questions not one). The gradient read + g-ratio unification were staged to `founders_vision.md`
(30 June entry), and the edge-bond SSV calc was handed to the SF-2/SF-5 lane.

**Update (SF return, consumed 1839): G1a DELIVERED — floor VIABLE, direction corpus-pinned.** SF-2/SF-5 evaluated
the ratio (OPEN-SS-40, patches 2200–2202) and returned it viable. The key physics: the *static* curvature (2200)
gave g ≈ 1.6–3.8 (tense) — but that operator is wrong (the static config is Earnshaw-unstable, exactly 1834); the
correct **ponderomotive |E|²-curvature** (2201, the calc 1835 named "mine to run") resolves Earnshaw (q = 0 a true
minimum, both modes restoring) and gives **g ≈ 0.02**; and the viability *condition* (steep/screened field) is
**met by the corpus, not assumed** (2202: a localized near-cancellation residual cannot be sub-Coulomb, plus
derived fm-scale screening → ~17× margin under g_crit). DM consumed g (1839): **cluster floor VIABLE, direction
robust, lands ~0.4–0.8 cm²/g (whole band ≤ cluster bound ~1.0); self-limiting re-confirmed; the stiff-ribbon /
soft-scissor tension dissolves** (same bond, ratio ⇒ a large κ_bend is the denominator that makes g small — the
junction is the *softer of two stiff modes, not a fragile joint*). Two corrections recorded straight: the g ~ 0.1
estimate had the right direction but mis-referenced the softness to the E_qq core (the hierarchy cancels in the
true ratio → pure geometry ~0.02); 1836's ratio *framing* is confirmed. **Still open (no promotion):** the exact
floor (0.4 vs 0.8) and G1b (absolute κ_θ → ℓ_p) both root on **OPEN-FP-SF-2-η** (ZBW amplitude); G2 (E_qq/E_ee)
and G3 (glueball-arrest, **OPEN-SS-39**, the sharpest remaining kill risk) open. On approval: (a) DM-side ℓ_p×g
partial-G1b (absolute κ_scissor, no FP-blocker); (b) **panel round 2** — framed as a *velocity-sector floor
clearance*, not a candidate-wide green light, carrying the stiff-vs-soft consistency result. **DM-1 stays v1.0 /
Layer-C; CONJ-COSMO-1 founder-gated.**

# Mechanism (revised velocity sector) — Strip-then-Fuse — DM-1

**STATUS: STAGED, founder-gated. Post-v1.0 companion note. Supersedes step 5 ("velocity dependence") of
`mechanism-DM-1.md` PENDING founder approval + a CONV-001 panel pass.** DM-1 stays v1.0; this note documents
the corrected velocity mechanism assembled in patches 1815–1826 (30 June 2026, Opus lane). It does not edit the
v1.0 papers. Layer C throughout (order-of-magnitude, CPP-geometry-dependent — not framework-free). **CONV-001
round 1 CLOSED (4/4: ChatGPT, Grok, Copilot all SwC; Gemini NOT-SOUND engaged) — net SOUND-WITH-CHANGES; see
"Panel review" below.**

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

STAGED for founder review. **CONV-001 round 1 CLOSED — 4/4 in, net SOUND-WITH-CHANGES** (3 SwC + Gemini
NOT-SOUND, dissent recorded). The panel's converging make-or-break is the **coupled trio**: the glueball-junction
**angular stiffness** (the one number computable next, controlling cluster floor + self-limiting together), the
**color range R_color ~ d** (now a named live risk — propagates into the repair gate and tail-rate; wants SF-5
support), and the **penetrating-tail rate**. On founder approval: (a) supersede `mechanism-DM-1.md` step 5 with a
pointer to this note; (b) take the junction-angular-stiffness calculation first, then the R_color ~ d
strong-sector (SF-5) support; (c) founder-gated, open the CONJ-COSMO-1 *discussion* (staged only — the panel
endorses a discussion, not finality for the velocity curve). **No promotion until the coupled trio is pinned;
DM-1 stays v1.0; CONJ-COSMO-1 founder-gated.**

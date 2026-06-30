# Mechanism (revised velocity sector) — Strip-then-Fuse — DM-1

**STATUS: STAGED, founder-gated. Post-v1.0 companion note. Supersedes step 5 ("velocity dependence") of
`mechanism-DM-1.md` PENDING founder approval + a CONV-001 panel pass.** DM-1 stays v1.0; this note documents
the corrected velocity mechanism assembled in patches 1815–1826 (30 June 2026, Opus lane). It does not edit the
v1.0 papers. Layer C throughout.

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

STAGED for founder review. On approval: (a) supersede `mechanism-DM-1.md` step 5 with a pointer to this note;
(b) CONV-001 panel pass (single-block protocol) with the stress points above named; (c) founder-gated, open the
CONJ-COSMO-1 discussion — the velocity signature is now mechanistic on the corrected geometry.

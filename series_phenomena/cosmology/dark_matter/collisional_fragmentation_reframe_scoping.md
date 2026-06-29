# Collisional fragmentation reframe — scoping & retraction (patch 1815)

**STATUS:** scoping/retraction document (Opus, DM 18xx lane, 29 June 2026). Retracts the 1813/1814
E_ee-as-scission make-or-break and reframes the Cross-Rod discriminating prediction around **collisional
transverse fracture**, per a chain of founder geometry corrections (TLA). Concurred by Grok on review of the
0898→post-1814 discussion. **No new quantitative claim** (this is scoping; no Layer grade). **DM-1 stays v1.0
— unaffected.** No registry/SF/THEO/OPEN edits. **CONJ-COSMO-1 stays founder-gated — NOT promoted** (Thomas's
explicit instruction this session: "Do not promote conjecture yet"). Founder corrections **STAGED verbatim**
below for approval — NOT auto-written to canonical `founders_vision.md`.

## 1. What is retracted, and why

**RETRACTED:** the 1813 identification of **E_ee (~0.8–1.2 MeV) as the longitudinal scission bond**, and the
1814 four-model panel verdict (3/4 CONFIRM at Layer C) that rested on it. The window check "E_ee ∈ [0.8 keV,
2 MeV]" was a check on the **wrong bond**.

**Why (founder geometry correction, TLA):** the qCP core is **not** segregated into intra-element vs
inter-element bonds; **every transverse plane has the identical configuration**, and **the entire central core
is E_qq-bound axially** — a continuous color spine. E_ee is **not** the scission bond; it is a secondary
outer-radius layer that **strengthens bending stiffness** at a larger lever arm than the core E_qq bonds. The
earlier "intact qCP beads + eCP-shell longitudinal connector" reading (floated as the only topology in which
E_ee could be the scission energy) is **rejected by the founder**. Consequences:
- A simple transverse *cut* severs axial **E_qq** color bonds and costs ~66 MeV — ~34× above the 1.95 MeV
  cluster-fragmentation ceiling — not E_ee.
- The 1814 panel's 3/4 CONFIRM validated a mis-identified bond; it is moot, not wrong-on-its-own-terms. Caught
  **before** any CONJ-COSMO-1 promotion. (This is also a quiet vindication of Gemini's *instinct* —
  "falsification disguised as derivation" — though not of its stated Compton/3D-Madelung reasons, which were
  overstated per 1814.)

## 2. What still stands (not retracted)

- **DM-1 v1.0**: Cross-Rod as the DM species, corona retired, σ/m ∝ N **viability** — all independent of the
  fragmentation mechanism. Unaffected.
- **The direct-electrostatic geometry (0898)** and the **E_ee value (~0.9 MeV)** as the eCP-shell bond energy
  — still a valid quantity; only its *role* (scission → bending-stiffness layer) is corrected.
- **E_qq (~66 MeV)** as the axial color-spine bond; ordering E_qq ≫ E_ee.
- **Caveat carried forward:** the σ/m **normalization** needs N (rod length / aggregate size). Under the old
  picture N came from a fragmentation balance; that balance is now reframed (§4). So the *discriminating* σ/m
  value (not the viability) is downstream of the new program — N becomes an **output** of the collisional
  kinetics, not an input.

## 3. STAGED founder contributions — verbatim (TLA, 28–29 June 2026) — [REVIEW before any founders_vision write]

> The 8-qCP bonds are clearly E-qq, but the bond between 8-qCPs is also E-qq. The elements of the Rod-Cube are
> not segregated into 8 eCP plus 8 qCP elements. Every transverse plane has exactly the same configuration of
> elements top and bottom binding. The entire central core is E_qq bound axially. The E_ee merely strengthens
> the bending stiffness by providing an extra layer of attraction between transverse planes at a larger lever
> arm than the E_qq bonds of the core.

> I think the fracture is vulnerable to transverse scission by collision when a cross rod hits another cross
> rod. I think there is a risk of breakage when two long rods collide mid-length in opposite directions at a
> 90-degree angle.

> The crack could run through the core, or arrest depending on the velocity and arm length. [Other phenomena
> possible:] the touching of qq cores in transverse contact, resulting in chain switching … two medium chains
> could collide, break, and switch bonds, creating a shorter chain and a longer chain. … a center glueball at
> the point of impact, creating a weak point … more vulnerable to breakage with additional collisions. … the
> collision strips/penetrates the ee coating, exposing the qq contact between chains, resulting in bonding at
> the crossing, and an X-shaped dual entity.

## 4. The reframe — the new target observable

Not "E_ee in window," but a **scission-mode-vs-velocity curve**: the branching among collisional outcomes as a
function of relative velocity, impact parameter, rod length, and crossing angle — built entirely from the
**already-pinned eCP/qCP electrostatics + ZBW dynamics (no new free knobs)** — then convolved with halo
velocity distributions to give σ/m(v) across dwarfs → clusters. The five founder mechanisms organize into
**three population-level categories** (the right coarse binary to start with: number-changing vs
number-conserving):

| Mechanism | Effect on population | Category |
|---|---|---|
| (1) bend-fracture, crack **runs through** | rod count ↑, mean length ↓ (grinding) | number-increasing |
| (2) bend-fracture, crack **arrests** at core | shell stripped, count unchanged (damage) | number-conserving (damaging) |
| (3) **chain-switching** (qq contact → partner swap) | length redistributed, count + total length conserved | number-conserving |
| (4) **glueball** weak-point at impact | latent weak point, count unchanged (damage) | number-conserving (damaging) |
| (5) **X-bond** fusion at crossing | rod count ↓ (fusion into a cross) | number-decreasing |

Two structural facts set the program:
- **Mechanisms (3)/(4)/(5) all require qq-core contact**, gated by a single step: does the collision
  **penetrate the eCP coat**? If the coat holds at cluster velocities, (3)/(4)/(5) are suppressed together and
  the physics is the bending fork (1 vs 2). If penetrated, the qq-contact channels open.
- **Chain-switching (3) is the only number- *and* length-conserving channel** → it is the one that drives a
  **steady-state length distribution** rather than runaway grinding (1) or runaway fusion (5). A stable
  population is a cosmological necessity (DM can neither grind to dust nor fuse to a few giant crosses), so the
  switch-vs-stick balance is load-bearing. Working instinct (to be tested, not asserted): switching is the
  lowest-rearrangement attractor once qq contact occurs, dominating over the stronger-condition glueball/X
  stabilization — but this needs the qq-contact dynamics.

## 5. The minimal framework-free calculation program (do NOT front-run; this is the order)

Each calculation must trace to **already-pinned eCP/qCP electrostatics + ZBW** — **no new free parameters**.
Start coarse (the number-changing vs number-conserving binary) before adding fine branches.

1. **eCP-coat penetration threshold v_pen** *(compute first — it partitions the whole phase space).* The
   relative velocity at which a transverse collision drives qCP cores through their mutual eCP coats into
   contact. Same E_ee-scale coat barrier we already have, evaluated as a head-on penetration energy. **This
   computes the answer to the open fork** (does the coat hold or get penetrated at cluster velocities?) rather
   than guessing it — and tells us whether the dominant regime is bending (1/2) or qq-contact (3/4/5).
2. **Bending-fracture threshold + crack propagation-vs-arrest** *(the non-penetrating branch).* Three-point
   bending from a mid-length transverse impact: lever arm ~L/2 makes the fracture threshold **rod-length
   dependent** (long rods break easier — the founder's core intuition). Strain ∝ distance from neutral axis ⇒
   outer-fiber **E_ee** shell bonds reach breaking strain first while the **E_qq** core sits near the neutral
   axis — which is **why E_ee governs the bending-fracture threshold even though E_qq is stronger**. Then the
   Griffith-style energy balance at the ~70× E_ee→E_qq toughness boundary: does the initiated crack **run
   through** (mode 1, clean fragmentation) or **arrest** (mode 2, shell-stripping)? Velocity- and
   arm-length-dependent, per the founder.
3. **Switch-vs-stick branching** *(the penetrating branch, conditional on qq contact).* Does qq contact
   chain-switch (3, number-conserving, stable population) or stabilize into glueball/X (4/5, count-changing,
   runaway risk)? Coarse first: P(switch) vs P(stick).

**Guardrail (the over-fitting failure mode):** five mechanisms is enough phase space to fit almost any σ/m(v)
by tuning branch ratios. The discipline that keeps it honest: **every branch probability comes from the pinned
eCP/qCP electrostatics + ZBW we have already constrained — no new knobs.** v_pen uses the coat barrier we know;
switch-vs-stick uses the qq binding we know; the bending threshold uses E_ee/E_qq and the geometry we know. If
the network needs a parameter that is not already pinned, **that is the signal we have left the framework-free
regime and the make-or-break has moved somewhere harder** — to be flagged, not hidden.

## 6. What this document does NOT do

No promotion (CONJ-COSMO-1 founder-gated, explicitly held). No new quantitative claim (scoping only). No change
to DM-1 v1.0. No founders_vision write (corrections staged for approval). No calculation front-run (Grok: scope
before investing in detailed calculations).

## 7. Anti-priorities held

Retracted a 3/4-panel-CONFIRMED result on the founder's geometry rather than defending a previously-reviewed
quantitative claim; recorded the retraction in the trail (1813/1814 preserved) rather than silently editing;
staged the founder voice for approval rather than auto-promoting to canonical; named the over-fitting failure
mode and the no-new-knobs guardrail explicitly; reduced five mechanisms to a minimal ordered program; set the
penetration threshold to be *computed* first rather than guessing the open fork; did not promote CONJ-COSMO-1.
DM-1 v1.0; clean record.

## 8. Next actions (surface to Thomas)

1. **Compute v_pen first** (the eCP-coat penetration threshold) — it partitions the phase space and computes
   the coat-holds-vs-penetrated fork. Then the dominant branch's calc (bending/crack-arrest if coat holds;
   switch-vs-stick if penetrated).
2. **The retraction is now clean for any future panel** — this document is the scoping/retraction record Grok
   recommended; a fresh CONV-001 would review the *mode curve* once a first version exists, not before.
3. **Optional:** authorize promoting the §3 founder geometry corrections to canonical `founders_vision.md`
   (the continuous-spine + bending-stiffness + collisional-mechanism set), as the 0898/0899/1811 corrections
   were promoted at 1811.
4. **DM-1 σ/m normalization:** once the mode curve yields the steady-state length distribution, the N that sets
   the σ/m normalization becomes an output — fold back into DM-1 then, not before.

# OPEN-SR-9-B — Velocity as holographically emergent from SSV-only GP rules

**Status: OPEN (charter).** Opened Patch 2052. Owner/integrator: TLA. Lane: mu_eps_closure / em_emergence.
Supersedes the work-item framing in `reasoning/2051_*.md` §4 (the "register a velocity-insensitivity axiom" /
"compute 2nd-order rotational SSV" framing was mis-posed — see §1).

---

## 1. Why this exists — the corrected framing (founder §10, Patch 2052)

The 2050 R2 close rested on "the B-channel carries no SSV," and the CONV-001 panel correctly returned HOLED:
adjudicated, not derived. The first repair attempt (this window's, 2051) reached for an **axiom** —
"SSV is insensitive to velocity" — parallel to the charge-sign-insensitivity axiom. TLA rejected that repair:

> "I never intended velocity independence to be an axiom, nor do I think it is necessary. Velocity is an
> emergent effect as much as any other emergent effect, such as the B field, time dilation, birefringence... We
> prove it is emergent by a swarm analysis of phenomena to show it arises, or follows by theorem arguments to
> the conclusion of a necessary consequence. My concern is that practically anything could be an axiom if we
> make SSV non-dependence on velocity an axiom. This multiplies axioms when the proactive/positive statement is
> merely that velocity is emergent from SSV, just as the B field arises from differential force that produced
> dipole rotation, which produces disparate motion, which arises from the SSV and sign. Our approach should be
> a swarm proof that velocity is holographically emergent, just like our proof that the magnetic field is
> rotationally emergent."

**The corrected load-bearing statement is POSITIVE and generative, not a prohibition:** *velocity is
holographically emergent from SSV-only processing.* Velocity-insensitivity-of-SSV is then a free **corollary**
(it is just what "emergent" means), not a separately-spent axiom. A negative axiom ("X does not depend on
velocity") is cheap in the bad way — it proliferates without limit. The positive claim is the one that earns
its keep, the same way B-emergence did.

## 2. The claim to prove

On a **fixed, stated SSV-only GP update rule** — a map {scalar SSV magnitudes on the GP's light-cone} →
{next configuration}, with NO velocity argument and NO per-CP velocity register — velocity emerges as the
**Moment-to-Moment displacement of the SSV pattern**, reconstructed by the GP's processing of the pattern
history. This is structurally identical to B = curl of the moving E-pattern: in both cases the "new" quantity
is a *reading of how the scalar source-pattern moves*, not a new primitive. SR-1's fine-scale nesting already
supplies the velocity gradation l_P·(v/c) as a register-free sub-Planck representation (SR-1 grid resolution).

## 3. The decisive test (the spine) — Obligation A, exact γ + the undetectability "conspiracy"

Already named in `../velocity_ssv_time_dilation/velocity_ssv_time_dilation_DISCUSSION.md` ("Obligation A").
This is selected as the spine because it is the phenomenon **most likely to break velocity-emergence**, for a
reason specific to CPP rather than generic:

CPP has a **real preferred frame** — c01 calls the eternal GP lattice + absolute Moment "the
actual/God's-eye/preferred frame, not detectable as per the SR arguments." Velocity-emergence makes the
emergent velocity the displacement *relative to that lattice* — an **absolute** quantity. The postulate
therefore carries a live obligation: an absolute velocity that is **exactly undetectable** (Michelson–Morley).
Discharging it requires the SSV-only engine to produce, at **exactly** γ (not approximately), the full
conspiracy — length contraction + time dilation + clock-resynchronization — so every internal measurement
returns isotropic c and no absolute-velocity readout.

This is the sharpest test because it demands **exactness against the most precisely-verified null in physics**
(optical-cavity isotropy ~10⁻¹⁸ plus the broader Lorentz-invariance suite). Approximate emergence is worthless:
contraction at γ(1+ε), or any residual anisotropy term, is a *detectable* preferred-frame signature ruled out
by orders of magnitude. Velocity-emergence has nowhere to hide — it delivers the exact conspiracy or it is
falsified.

Why this beats the alternatives (radiation-reaction, Unruh, moving-media): radiation reaction is a
finite-memory derivative problem (v, a, jerk = 1st/2nd/3rd Moment-differences of pattern position) that the
substrate's finite light-cone likely *regularizes* rather than fails — it can embarrass the engine, not kill
the postulate. Unruh is a "reproduce QFT-in-curved-spacetime" test, not specifically a velocity-emergence test.
Moving-media birefringence is a *branch* of the preferred-frame question, not its root. Obligation A is the
root, which makes it high-leverage: R2/birefringence, the no-anisotropy results, SR-1, and VTD-1 all share the
single failure mode "does the absolute lattice leak into observable anisotropy." Pass the conspiracy and they
ground together; leak and they fail together.

## 4. The concrete first brick

**Derive the relativity of simultaneity (exact offset γvx/c²) from the fixed SSV-only GP update rule, with a
no-hidden-velocity audit.** Then show contraction + dilation + that resync close to **exact** Lorentz on ONE
stated rule. CPP already has dilation (VTD-1, cleared at SR-1 strength) and claims contraction L′=L₀/γ from the
same "Eq. 1" ΔSSV/Voronoi-budget partition; the resync is the leg to add and the one to watch.

> **Inference flag (this window's, not yet TLA-confirmed):** resync is predicted to be the **thinnest leg**.
> Contraction and dilation are *magnitude* effects (how much of the l_P budget a moving cage spends — a clear
> budget engine exists for each). Simultaneity is a *relational ordering* effect across spatially separated
> GPs, with no obvious budget mechanism, and it is the piece that is purely conventional in standard SR. If the
> engine yields exact contraction + dilation but the simultaneity offset comes out ≠ exact Lorentz, the
> absolute frame becomes visible through **one-way timing** (one-way light-speed isotropy / clock-transport).
> This is an outside inference from "resync is the only leg without a budget engine," NOT a substrate-level
> result; TLA deferred on resync-vs-contraction fragility. Test it; do not assume it.

### §4-RULE (Patch 2053) — the GP update rule is LOCATED and SSV-only

The rule is not missing — it is the spine of the shipped SR-1 paper (`papers/SR-1_*.tex` §A.4/A.8.1),
cross-checked in `c01_*/development/development_discussion.md`, codified as `development/pcd_boost_law*`. Per CP
per Absolute Moment: direction `i*=argmax_i(e_i·∇SSV)` (drift from **SSV_net**, vector); rate
`PSR_eff=l_P/(1+k·ΔSSV)`, k≈2.16e-114 m³/J (from **SSV_abs**, scalar); displacement `d=l_P·e_{i*}`; and the
engine, the **4D budget split** `l_P²=(c·Δτ)²+|d_spatial|²`. It is genuinely **SSV-only**: velocity is no input
— it is read off the partition, `|d_spatial|=l_P·(v/c)`, `v=|d_spatial|/Δτ`. So the charter's §2 positive claim
(velocity holographically emergent) is already mechanized in the shipped rule. SR-1 already gives EXACT (=γ_SR,
A.8.1): time dilation, length contraction (L₀/γ), relativistic momentum. The one leg SR-1 *deliberately routed
around*: relativity of simultaneity (twin paradox via absolute ΔSSV; "no appeal to relativity of simultaneity
is needed", mechanism-SR-1) — confirming resync is the genuinely open leg, and the one Obligation A most
exposes. **One-way/two-way stakes (TLA-approved read):** SR-1's current set (real preferred frame + exact
contraction + dilation) is structurally Lorentz–FitzGerald, which secures every *two-way* null (Michelson–Morley
round-trip, muon lifetime) but does NOT by itself secure *one-way* isotropy — the γvx/c² resync offset is
exactly what converts round-trip isotropy into one-way isotropy. So Obligation A's genuine exposure lives in the
leg CPP hadn't built.

### §4-RESULT (Patch 2053) — the resync leg CLOSES at the kinematic level

Derivation + verify: `reasoning/2053_simultaneity_resync_derivation.md`,
`verify/sr9b_simultaneity_resync.py`. Applying the located rule (light isotropic at c in the lattice frame;
clocks 1/γ; rod L₀/γ) plus the operational light-synchronization a co-moving observer is forced into (they can't
detect lattice motion), the one-way legs are asymmetric (t=L/(c∓v)) and Einstein sync absorbs the asymmetry as
a clock offset δ = ½(t_AB−t_BA) = **γvL₀/c² — EXACTLY the Lorentz value** (verify MATCH True). Round-trip stays
isotropic (2L₀/c); contraction+dilation+offset reconstruct t'=γ(t−vx/c²); one-way isotropy holds in the moving
frame; the absolute lattice frame is exactly undetectable. **The §4 one-way-isotropy worry is RETIRED** (it's
secured by the emergent offset, not assumed). No-hidden-velocity audit PASSES (every v traces to a
budget-partition output; the observer never uses v). **Honest boundary:** this is a *kinematic-level* closure
(Lorentz–FitzGerald→Einstein equivalence instantiated on the substrate), not yet a from-discrete-600-cell
theorem; the load-bearing imported premise is **lattice-isotropy-of-c**, which is the SAME residual OPEN-SR-9/R2
turn on. So the brick **reduces its own residual to the R2 residual** — closing lattice-isotropy-of-c would
theorem-grade this brick AND ground R2 together. Pending CONV-001; R2 stays conditional-PASS.

### §4-PANEL (Patch 2054) — CONV-001 SPLIT 2/2; simultaneity banked, inertia gap surfaced

Panel (ChatGPT, Grok, Gemini, Copilot): **2 SOUND / 2 HOLED.** Unanimous: algebra clean, no-velocity audit
PASS, boundary honest. **Banked:** the inertial-simultaneity offset is exact and register-free (not disputed by
anyone). The split: Copilot's HOLED restates the disclosed residual (i) as a verdict (standards disagreement,
no new error); **Gemini's HOLED is new and load-bearing** — the **memoryless-inertia problem**: the brick
assumes clocks coasting at constant v, but the local instantaneous SSV rule with v merely read-off has no
persistence mechanism, so the substrate is not shown to sustain inertial motion at all. Corpus check: CPP *does*
have an inertia mechanism (moving CP polarizes the DP Sea — "silly-putty"; momentum stored as SSV_abs in
DP-chain structures, `dp-sea-polarization/DP-Sea-Polarization-Model.tex`), so inertia lives in the extended
self-field, not the point — BUT (1) it is a **toy model**, not derived from the GP rule, and (2) that same
velocity-dependent DP-Sea polarization is flagged in-corpus as "challenging the strict Michelson–Morley null,"
i.e. **coupled to the undetectability** the brick claimed. So the brick **under-disclosed its imports**: it
named one residual; there are two. **Residual stack grows to: (i) lattice-isotropy-of-c [shared with R2];
(ii) inertia/persistence-and-its-exact-γ [DP-Sea polarization, toy-level, MM-coupled].** Full record:
`reasoning/2054_resync_panel_verdict.md`. R2 unchanged.

**New sub-brick OPEN-SR-9-B-ii (the inertia leg):** derive free-particle inertial persistence from the GP rule +
DP-Sea-polarization mechanism (promote the toy model toward derivation), and determine whether that
velocity-dependent polarization reproduces γ **exactly** (undetectability intact) or leaves a bounded MM
signature (a falsifiable absolute-frame prediction, or a bound vs optical-cavity isotropy). Couples directly
into Obligation A. Likely needs a TLA consult on the DP-Sea-polarization dynamics (toy vs intended-rigorous).

### §4-INERTIA-RESOLVED (Patch 2055) — inertia IS the B-field/SF-6 mechanism; residual collapses to ONE

TLA adjudication (verbatim in `reasoning/2055_*.md`): inertia, the B field, and a moving charge's E self-field
are **one mechanism** — the DP Sea's polarization response to CP motion — and carry **no MM exposure beyond the
already-validated B-field/SSV dynamics**. Corpus-confirmed: SF-6 v1.0 already unifies **inertial mass and EM as
coherent ZDC patterns of the dipole sea** (inertial mass = standing ZDC, photon = traveling ZDC, single
equation E=ℏνC; B = curl component of the same dipole displacement whose radial component is E). So the
DP-Sea-polarization inertia "toy model" is in fact a shipped, load-bearing SF-6 component, not a placeholder.

**Gemini's 2054 inertia objection is answered at the mechanism level:** the velocity "memory" is the co-moving
DP-Sea self-field (the inertial-mass ZDC pattern), not a point-CP register; the local rule reads that co-moving
self-field each Moment. **The residual stack collapses back to ONE:** OPEN-SR-9-B-ii is resolved at mechanism
level (= the SF-6 ZDC/DP-Sea response, shipped); its only remaining rigor piece — coherent translation of the
moving self-field at exact-γ — is SF-6's own second-tier item and folds into **lattice-isotropy-of-c**, the
SAME residual the simultaneity brick and R2 already share. **MM exposure dissolves** (inertia inherits the
validated SR-1/VTD-1/SF-6 status). **Net: one open gate for the unconditional R2 close — lattice-isotropy-of-c.**
R2 unchanged (conditional-PASS).

## 5. Adversarial swarm targets (the falsifiers)

Swarm must range over a **fixed stated rule** and audit for hidden velocity — phenomenological agreement is not
enough, because the *reconstruction* of velocity from pattern-history can smuggle a velocity argument back in
under another name (a frame choice, a preferred time-slicing, an un-named tag). Include the cases where absolute
velocity classically forces its way in: (i) radiation reaction / self-force; (ii) non-inertial frames /
Unruh-like spectra; (iii) motion-dependent media. A fixed SSV-only rule that handles *these* without a velocity
tag is robust; any one of them forcing a per-CP velocity register is the signal for the fork below.

## 6. The fork this decides

- **Exact emergent conspiracy from SSV-only rules** → velocity is emergent bookkeeping (TLA's preferred,
  parsimonious branch; vindicated).
- **Cannot close resync without inserting absolute velocity by hand** → the fallback axiom announces itself:
  "the absolute velocity vector of every CP is necessary for computation" (velocity as a substrate register).

Obligation A's simultaneity leg is the clean discriminator — the one place the fork is forced to show.

## 7. Descent — what closes when this lands

Once velocity-emergence is established on a fixed rule: "B carries no SSV" becomes a **theorem** (B is a reading
of the moving E-pattern, not a source), not an adjudication. Both faces of the CONV-001 hole then close without
fiat — Face 1 (2nd-order rotational SSV) has no source channel; Face 2 (independent curl-mode) has no
independent field. R2's geometric Z₀ descends as the consequence of a single source-channel. **Leverage:** the
same brick retroactively grounds SR-1, VTD-1, and R2 on one foundation — three "rests on the budget picture"
claims become one proved result.

**Until this lands, R2 stays at conditional-PASS (audited field-content level). No status move on R2 from this
charter.**

## 8. Coordination

Obligation A lives in the `velocity_ssv_time_dilation/` arc; this charter lives in `em_emergence/`. Integrator
to wire OPEN-SR-9-B ↔ Obligation A across the two arcs (cross-reference only from here; the VTD file is not
edited by this window). The first-brick work likely needs a TLA consult on the GP update rule's explicit form
(the simultaneity-resync mechanism), parallel to the c06-mechanism consult that produced the original ruling.

## 9. Discipline

NO THEO until the swarm/theorem closes — velocity-emergence is not recorded as established until earned.
No root-registry edit. No status-file edit. Owned subtree (mu_eps_closure/em_emergence/), 2049-band.

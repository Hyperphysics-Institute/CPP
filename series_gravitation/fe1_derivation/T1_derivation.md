# T-1 DERIVATION (W-2) — THE GENERAL CPP FIELD EQUATION FROM THE MESSENGER CENSUS

**Patch 3258 (19 Aug 2026, Session 150). OPEN-GR-FE-1 charter step W-2
(charter Patch 3254; founder picture Patches 3255/3257). Verify:
`series_gravitation/code/3258_t1_relay_verify.py`, 10/10 PASS — every
mathematical claim below is machine-checked; claims were written AFTER
the computations ran.**

**Epistemic standing (inherited, not upgraded):** everything below is
conditional on the PSR constitutive form
PSR_eff = l_P/(1 + k·Δ|SSV|), whose SR-1 grounding stands at W2
viability strength (GR-1 §7); k is a normalisation convention. The
charter bars are honored: no Einstein equation is posited and worked
backward; no variational principle is imported; no constant is tuned;
LOCAL scope only.

**Outcome in one line:** a T-1 candidate is DERIVED from the registered
picture; its static sector reproduces every corpus SOLUTION exactly
(the GR-1a source relation, the GR-1c isotropic metric, Newton/Poisson,
linearised Einstein); but its static reduction does NOT match the
GR-1c Proposition's stated F-term at leading nonlinear order — and the
symbolic computation shows GR-1c's F-term also fails against GR-1c's
OWN exact solution. Per charter §4, this is a **HALT-and-register**:
GR-1c is not adjusted; the finding is minted as **OPEN-GR-FE1-FTERM**
and put to founder/panel adjudication before W-3/W-4 proceed.

---

## §1 — Inputs (all registered; nothing new)

From the axiom layer: A1′ (three CP types; AP-4 payload {origin
address, E, S}, static snapshot, fixed per-GP emission count, reset at
Moment-level delivery); A3′ (completed broadcast; AP-4d: SSV_net and
SSV_abs are receiver-computed state); A4 (Nexus Moment
synchronization). From the founder picture (3255/3257): GPs execute
Perceive+Compute; CPs execute Displace per the GP-computed SSV_net;
DI-bits are conserved and reused; every GP begins each Displace cycle
with the same DI-bit count; "every GP's DI-bit total influence on its
PSR is the same as every other GP"; symmetry exists only over the full
PCD cycle, not its pieces; the lattice is fixed/absolute with ZERO
configuration freedom (CP configuration is the only freedom); the
Voronoi-cell-to-PSR ratio is an OPEN input — it is carried symbolically
below and, as it turns out, drops out of every leading-order statement.
From the arc: the PSR constitutive form and the shell-broadcast source
relation k·Δ|SSV| = GM/rc² (GR-1a); the two-component broadcast
(GR-1b); FACT G1 lattice geometry.

## §2 — The census (discrete, exact)

Let u(x, t) denote the departure field Δ|SSV|_abs at GP x at Moment t
— the excess of the receiver-computed SSV_abs census over the
homogeneous-Sea value. Three structural facts, each an axiom-text or
picture-text consequence:

**(C-i) Linearity.** The per-Moment computed state at a GP is a sum
over DI-bit arrivals of imprinted static snapshots (AP-4). Fixed
per-GP emission count + reset-at-delivery ⇒ the update is a LINEAR
functional of the origin-GP registers one hop away. Superposition is
exact at messenger level.

**(C-ii) Homogeneous cancellation.** The uniform Sea (including the
uniformly distributed DP-Entity background, per founder Q4) contributes
equally at every GP — the founder's equal-influence invariant. Hence
the dynamics closes on the DEPARTURE field u; the homogeneous
background drops out identically. (This is also why the entity/free
distinction is gravitationally silent at LOCAL scale.)

**(C-iii) One hop = one Moment = one PSR.** DI-bits disperse fan-wise
and land in a thin band at the PSR (founder Q1; AP-4c origin→PSR
reading), under universal Nexus synchrony. The elementary transport
kernel is therefore the SHELL of radius R(x) = PSR_eff(x), traversed
in one Moment τ = t_P. The GPs beneath are FIXED and absolute (founder
Q5): the kernel acts on the rigid lattice; only its RADIUS varies with
local stress. N_V (GPs per PSR) enters only the kernel's sampling
density and cancels from every mean — carried symbolically, never
load-bearing (the W-1 constraint honored).

The census update is then: the shell-mean operator
M_R[u](x) = mean of u over the sphere of radius R(x) about x, on the
flat absolute lattice.

## §3 — Statics: the mean-value property is exact, for ANY PSR profile

In a static configuration the census must be self-consistent Moment to
Moment: u(x) = M_{R(x)}[u](x) at every vacuum GP. **Verify Check 1**
establishes the classical fact numerically at 1e-9 precision including
POSITION-DEPENDENT R(x): the shell mean of 1/r about any exterior
point equals 1/r at that point for EVERY radius. Consequences, all
machine-checked:

1. **Vacuum statics = Laplace's equation on the absolute lattice,
   exactly** — not to leading order: because the mean-value property
   characterizes harmonic functions for every radius simultaneously,
   the PSR variation cannot deform the static vacuum equation.
   ∇²_lattice u = 0.
2. **The exact solution is the corpus profile.** u = GM/(k c² r) —
   i.e. k·Δ|SSV| = GM/rc², GR-1a's source relation — is harmonic
   (Check 5, exact) and is the unique spherically symmetric vacuum
   solution vanishing at infinity. **Derived, this time, from the
   census; and it identifies the absolute-lattice radial coordinate
   with the ISOTROPIC coordinate of GR-1c's metric** — which is
   precisely why the corpus's exact solution is conformally flat in
   space: the lattice IS flat; only the rulers (PSR_eff) and clocks
   shrink. The GR-1i graded-index picture is the same statement.
3. **Sources.** Mass = compressed-DP aggregates (founder Q2) = a local
   census excess: GPs inside matter integrate additional SSV_abs
   content. Gauss normalization (Check 7): ∇²_lattice u = −(4πG/kc²)ρ
   in the registered convention — Newton/Poisson, matching companion 5,
   with the linearised-Einstein weak field inherited from companion 7.

## §4 — Dynamics: reversibility forces the relay; the relay forces the wave operator

What closes the time sector? Two candidates for the Moment-update:

**Irreversible one-level relay** u(t+1) = M_R u(t) + source. **Dead
end, machine-established (Check 3):** the shell operator's plane-wave
eigenvalue is sinc(kR) (Check 2), strictly inside (−1, 1) for all
k > 0 — every mode DAMPS; nothing propagates. An irreversible census
cannot carry gravity's dynamics. It also violates the picture: DI-bits
are conserved and reused; the automaton is deterministic; nothing in
the substrate dissipates.

**Reversible two-level relay.** Messenger conservation + determinism +
the founder's full-Moment symmetry (Q3: "there is no symmetry in the
pieces of a Moment" — the completed cycle couples emission at t−1,
transit, and delivery at t+1) force the two-level time-symmetric FORM
u(t+τ) + u(t−τ) = 𝒜u(t) (annex L1, Patch 3261: ℬ = −1 is the only
nontrivial time-reversal-invariant one-register recurrence), with 𝒜
restricted by one-hop locality to the class 2[α·M_R + (1−α)I],
α ∈ (0,1] (annex L2). The continuum operator below is
CLOSURE-INDEPENDENT across that entire class (annex L3; the earlier
"unique closure" wording was withdrawn per the CONV-027 Q5 minority).
The picture-preferred member, α = 1 (AP-3's per-Moment register
refresh), is:

    u(x, t+τ) + u(x, t−τ) = 2·M_{R(x)}[u](x, t) + source terms.

**Checks 4a–c:** its dispersion is cos(ωτ) = sinc(kR) — REAL ω for
every k (unitary; no damping — the conservative structure survives the
continuum), with long-wavelength phase AND group velocity

    c_* = R/(√3·τ) = PSR_eff(x)/(√3·t_P).

Expanding for slow variation (wavelengths ≫ PSR), the continuum limit
is the variable-speed wave equation ON THE ABSOLUTE LATTICE:

**T-1 (candidate, lattice frame; conditional-on-PSR at W2):**

    (1/c_*(x)²) ∂²_t u  −  ∇²_lattice u  =  (4πG/kc⁴)·S[compressed-DP census]
    with  c_*(x) = PSR_eff(x)/(√3 t_P),   u = Δ|SSV|_abs.

Static reduction: §3 (exact). Weak field: linearised Einstein
(inherited). Measured-frame translation: rulers = PSR_eff, clocks =
the GR-1 rate — the GR-1b/GR-1c metric dictionary; light propagating
BY the relay sees the graded index n ≈ 1 + 2GM/c²r (GR-1i §10).

**Finding F-1 (the √3):** the relay's emergent speed is
√α·PSR_eff/(√3 t_P). As the CONV-027 minority correctly pressed, the k
convention CANNOT absorb this factor in the homogeneous limit (where
Δ|SSV| = 0); the repair is the explicitly registered kinematic mapping
**R-CSTAR-MAP** (adjudication §6, Patch 3261): c ≡ R_vac/(√3·t_P) with
the picture-preferred α = 1 — a registered normalisation at the k
standing with no long-wave observable content. The physical residue is
the dispersion FAMILY cos(ωτ) = α·sinc(kR) + (1−α) (annex L4):
falsifier-shaped, non-vacuous, still deliberately UNMINTED.

**Finding F-2 (two-component extension).** The identical census run on
the vector channel (AP-4 E/S vectors → SSV_net) yields the same relay
operator on V_i — consistent with A3′'s "all channels obey the same
icosahedral shell-sum, flat per-hop transport." The tensor channel
(Q_ij) is A3′-registered structure; its census derivation is W-4
territory (T-3), not claimed here.

## §5 — What the derivation did NOT need

No Einstein equations, no action principle, no metric ansatz, no tuned
constant, no fixed Voronoi/PSR ratio (N_V cancels from all means), and
no use of the founder's full-duplex Nexus speculation (3257 addendum —
registered, unused, as ruled).

## §6 — Redirections honored

The §5-charter expectations were redirected by the picture and the
derivation followed the picture: conservation entered as MESSENGER
count + equal-redistribution (C-i, C-ii) — not as an energy-flux
bookkeeping; the source entered as compressed-DP SSV_abs census excess
only — no independent kinetic term was introduced (anything kinetic
must emerge; none was needed for T-1); A3′ full-Moment symmetry is
load-bearing exactly where predicted (the two-level closure).

## §7 — HALT ADJUDICATION (charter §4, executed)

**The test:** is the T-1 static reduction the GR-1c nonlinear wave
equation (GR-1c Prop. field_eq: ∇_λ∇^λ(Δ|SSV|) + 𝓕 = 8πG T/c⁴, with
𝓕 = [2k(Δ|SSV|)²/(1+kΔ|SSV|)²]·□ln(1+kΔ|SSV|))?

**Machine result (Check 5, symbolic, exact):** on GR-1c's OWN exact
vacuum profile k·Δ|SSV| = a/r (a = GM/c², isotropic radius):

- the curved d'Alembertian does NOT vanish:
  □_g(Δ|SSV|) = −a³/(2k r⁵) + O(a⁴) — the O(a²) term cancels
  identically; the required compensator is F* = +a³/(2k r⁵) + …;
- the GR-1c stated 𝓕, under all three defensible readings (flat-□,
  curved-□, literal-k prefactor), is O(a⁴) at leading order
  (coefficient −2/r⁶ class) — **wrong order AND wrong sign class**;
- the LATTICE-frame reduction (this document's) is solved by the exact
  profile EXACTLY (flat Laplacian of a/kr = 0, symbolic zero).

**Adjudication:** solution-level agreement is EXACT (T-1's statics
produce precisely the GR-1c metric via the dictionary, and the
weak-field/classical-test sector is untouched — GR-1i's 8/8 stands on
the solution, which both formulations share). Equation-level, the T-1
static reduction is NOT the GR-1c Proposition as stated — and the same
computation shows the GR-1c 𝓕-formula is inconsistent with GR-1c's own
exact solution, independent of this derivation. The charter is explicit
for this branch: **HALT and register; do not adjust GR-1c.** Registered
as:

**OPEN-GR-FE1-FTERM** — the GR-1c Proposition's 𝓕-term, a
proof-sketch-level formula, fails against the exact isotropic solution
at leading nonlinear order (O(a³) required, O(a⁴) supplied; symbolic,
Check 5). Founder/panel adjudication owed on: (i) whether GR-1c
receives a corrigendum replacing the 𝓕-formula with the lattice-frame
statement (or the exact dictionary term □_g − ∇²_flat), and (ii)
whether the T-1 candidate above is accepted as the charter's T-1, at
which point W-3 (Birkhoff on the lattice-frame equation — where
uniqueness of the harmonic exterior is classical) and W-4 (T-3 source
tensor) unlock. Until adjudicated, the T-1 candidate carries
DERIVED-PENDING-ADJUDICATION standing and nothing downstream cites it.

## §8 — Ledger

Verify 10/10. No axiom touched; no paper touched; GR-1c untouched (HALT
discipline). New IDs: OPEN-GR-FE1-FTERM (GR.md). T-1 candidate:
DERIVED-PENDING-ADJUDICATION. W-3/W-4: gated on the adjudication.
Big-wave deposit gate (Patch 3231): unchanged.

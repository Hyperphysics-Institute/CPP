# Inertia-leg capstone — Patch 2057: conditional losslessness theorem + the root, and where we set this down

**STATUS: verbatim (captured at-patch).** Window: 2049-band. Closes the inertia leg at an honest status (NOT
exactness). Verify: `verify/sr9b_bolus_losslessness.py`. NO THEO; no status move; R2 unchanged.

## 1. The conditional "bolus" losslessness theorem (TLA dynamical mechanism + analytic skeleton)

TLA's dynamical mechanism (founder, prior turns): inertia is a rigid co-moving ΔSSV gradient — the standing
rear→front self-field set up by the original acceleration, which persists after the force is withdrawn and
translates as a unit. Push-from-behind, resist-in-front, and re-exposure are **simultaneous** (one static
configuration in the co-moving frame), not a sequential charge/discharge cycle. The simultaneity (no lag) is
what makes it lossless; the rigidity is the velocity memory.

Analytic skeleton (`verify/sr9b_bolus_losslessness.py`): assume premise **P** — every field component depends on
position only through ξ = x − vt (rigid co-moving pattern). Local energy continuity ∂u/∂t + ∇·S = 0 then
collapses (since ∂/∂t = −v ∂/∂ξ on f(ξ)) to d/dξ(S_x − v u) = 0, so the co-moving net flux S_x − v u is constant
along the motion. A **localized** bolus (fields → 0 fore and aft) forces that constant to 0, giving S_x = v u
everywhere: the only flux is the pattern carrying its own energy bodily forward. Hence dE_bolus/dt = 0 — **no
radiation, lossless coasting, constant velocity.** This is TLA's "fields superimpose and cancel conservatively,"
reduced from an intractable force-by-force sum to one premise + three steps.

## 2. What it proves, and what it does NOT (the honesty label, in the script itself)

- **PROVES (conditional theorem):** P ⟹ zero radiation ⟹ lossless coasting. The hard force-accounting is not
  faked; it is *localized* onto premise P.
- **DOES NOT PROVE:** that the **discrete** 600-cell + PCD dynamics admit exact P at a continuum of velocities.
  On a discrete lattice P can fail by Peierls/lattice drag or lattice-Cherenkov tails. **P holds exactly iff the
  substrate has exact emergent Lorentz invariance.** This is mechanism-level + analytic support, NOT exactness.

## 3. The root theorem (the shared stone — inherit this map, not just the leg)

One root sits under this whole region: **exact emergent Lorentz invariance from PCD dynamics on the discrete
600-cell.** The following are all **corollaries of that one root**, not independent problems:
- inertial coasting losslessness (this leg) — needs exact rigid self-field translation (massive ZDC, v<c);
- lattice-isotropy-of-c (massless ZDC at c) — the simultaneity brick's and R2's premise (i);
- R2's geometric Z₀ / B-neutrality descent;
- the SF-6 Michelson–Morley falsifier's named escape route (SSV-independent geometric Z₀, OPEN-FP-6-CONSTANTS);
- the reversibility/irreversibility ladder & arrow of time (coherent↔incoherent self-field↔Sea energy transfer
  is the *same* coupling that governs drag).
Sharp obstacle, recorded honestly: H₄ is a *finite* point group and cannot *be* the continuous Lorentz group;
any exact emergence must come from the **PCD dynamics** generating a continuous symmetry the static lattice
lacks. Getting exact Lorentz from a discrete substrate is a genuinely hard open problem across all
emergent-spacetime physics (lattice QCD recovers it only in the continuum limit; causal sets via randomness).
Favorable note: v<c is sub-luminal vs the lattice signal speed, so no Cherenkov *threshold* is crossed — a
necessary (not sufficient) condition for radiationless translation, satisfied for free.

## 4. Disposition — where we set the inertia leg down (TLA "enough" call, endorsed)

- **Mechanism:** established (qualitative dynamical account; reproduces vacuum inertia conservation). Graduates
  from "toy storage" to "qualitatively-established dynamical account with empirical support."
- **Losslessness:** proven **conditional on rigidity P** (§1). Not exactness.
- **Exactness:** named and **parked** as a deep open problem at the axiom surface (= the root, §3). NOT a
  blocking falsifier — any residual drag is Planck-suppressed, below all current experiment; "theorem-grade
  convergence with empirical evidence" is not available at that scale (no evidence to converge to). Honest
  shelf: same as "exact Lorentz from a discrete substrate," which no emergent-spacetime program possesses.
- **FEM:** if run, it is **consistency evidence only, never closure** (numerics can bound a drag, not prove
  exact-zero). Do NOT let FEM be recorded as proof — that is the 2055 overclaim failure mode in new costume.
- **R2:** unchanged, conditional-PASS. Inertia is a *sibling* corollary of the root, not upstream of R2; do not
  "wait for R2" to settle inertia — both move when the root moves.

## 5. Paper status
No paper on this complex yet, and not gated on R2. The natural artifact is a *conditional unification* paper —
"inertial coasting, simultaneity, lattice-isotropy, R2/Z₀, MM-escape, and the arrow of time are one structure,
modulo the exact-emergent-Lorentz root" — publishable either when the root falls, or now if the conditional map
is judged worth publishing explicitly labeled conditional. Flagged as a **candidate**, TLA's call, deferred.

## 6. Script-discipline re-audit (the reminder TLA asked for)
Per the reasoning-capture protocol, **every computation-bearing physics patch must ship its verify script in the
tree** (not /tmp, not prose-only). Session 2049-band audit at this patch: 2050 ✓ (sr9_dispersion_two_strain.py),
2053 ✓ (sr9b_simultaneity_resync.py), 2057 ✓ (sr9b_bolus_losslessness.py); 2051/2052/2054/2055/2056 carried no
computation (verdict/charter/correction) → none owed. **Standing instruction for the next window: at each
handover, re-run this audit (grep verify/ vs the computation-bearing patches in the band) rather than trusting
the discipline held — it rots silently.**

## 7. Discipline
Owned subtree (mu_eps_closure/em_emergence/), 2049-band. No root-registry or status-file edit. No status move.
NO THEO (conditional/mechanism support; nothing recorded as theorem). Collision-clean against HEAD 2056.

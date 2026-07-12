# CONV-001 ROUND — VERIFY THE MAKE-OR-BREAK INVERSION (kill → survives) + HOSTILE PASS

**Round type:** VERIFICATION + HOSTILE PASS on a **VERDICT REVERSAL**.
**Patches under review:** 2433 (reopen + corrected geometry #3), 2434 (charge-switching rescue), 2435 (δ = 3/7).
**No verdict moves this round.** Founder adjudicates on your returns.

**Integrity flag (read first).** This same worker, this session, moved candidate (B)'s make-or-break: **favorable
(2426) → FALSIFIED (2431, which THIS panel concurred on at 2429, Gemini's transverse-softening objection D driving
it) → SURVIVES (2434/2435).** Each flip followed a founder correction. That oscillation is itself a reason for
maximum skepticism. **Explicitly asked below: is the inversion sound physics, or is the worker now over-fitting to
the survival answer the founder leaned toward?** Say so plainly if you smell motivated reasoning.

**Raw files:**
- https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/series_phenomena/cosmology/dark_matter/reasoning/2433.md  (corrected geometry #3, jello core)
- https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/series_phenomena/cosmology/dark_matter/code/2434_chargeswitch_stiffness_geom3.py
- https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/series_phenomena/cosmology/dark_matter/reasoning/2434.md
- https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/series_phenomena/cosmology/dark_matter/code/2435_dm_lattice_delta_symmetry.py
- https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/series_phenomena/cosmology/dark_matter/reasoning/2435.md
- https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/series_phenomena/cosmology/dark_matter/reasoning/2430.md  (the transverse-softening finding the inversion must overcome)

## What changed (why the kill was reopened)
The founder identified that the 2431 kill's geometry was wrong. Corrected geometry #3: axial spacing uniform
(E_qq-set); eCP coat at a LARGER transverse radius than the qCP core; **qCP core is "jello"** — no static bending
integrity (Earnshaw). New physics (founder): the static opposite-charge lattice is Earnshaw-null, so bending
stiffness comes from CHARGE-SWITCHING — a duty fraction δ in which a CP presents SAME charge to a neighbour
(repulsive, positive curvature).

## The claim under review
1. **2434:** κ_θ = δ·Σ k_rep·x². Core-dominated (coat smaller by α/α_s ≈ 1/53). Clean analytic (verified):
   **κ_θ/E_bond = 2δ** in the deep branch (E_bond = E_qq). Branches differ by exactly α_s/α ≈ 53 (deep E_qq vs
   shallow E_ee).
2. **2435:** the DM-lattice δ, from the 8-qCP cube's 4+/4− NEUTRALITY (the SS-1-C₃ analog): over all C(8,4)=70
   neutral configs, any pair is same-charge **δ = 30/70 = 3/7 = 0.4286**, geometry-independent (brute-forced).
   Uniform sampling justified by the jello/Earnshaw property (no static minimum to trap in). δ = 3/7 exceeds the
   0.22 crossover by ~2×.
3. **Verdict:** κ_θ/E_bond = 2·(3/7) = 6/7 = **0.857 ≫ 0.43 → STIFF → candidate SURVIVES at drifted mass**
   (N ≈ 12, ~17 GeV, DD-clear); N=8 specifically still out.

## VERIFY
1. **2δ relation** — is κ_θ = δ·Σk_rep·x² the right stiffness, and does it reduce to 2δ (core, r_q = d/√2)?
2. **δ = 3/7** — is the 4+/4− neutrality combinatorial count correct and geometry-independent?
3. **branch factor α_s/α ≈ 53** and coat negligibility (α/α_s) — right?
4. **N_stab ≈ 12 / mass ~17 GeV** — consistent with the drifted-mass claim?

## HOSTILE PASS — break these (in priority order)
**(A) Does charge-switching actually OVERCOME 2430's transverse softening, or sidestep it? [most important]**
2430 found the ponderomotive stiffness tensor strongly anisotropic and sign-indefinite (transverse soft). The
inversion adds a NEW stiffening channel (charge-switching) but never showed 2430's softening is wrong or
subdominant. Is the worker stacking a new positive term on top of an unaddressed negative one? Does same-charge
repulsion during appositions provide TRANSVERSE (bending) stiffness specifically, or only axial?

**(B) The uniform-sampling assumption (δ = 3/7).** 3/7 is the infinite-temperature / degenerate-hop value. The
justification is "jello/Earnshaw → no static minimum → quasi-uniform." Is that sound, or does the dynamics still
dwell in opposite-charge (Madelung-low) configs and suppress δ? It would need to fall below 0.22 (a >2×
suppression) to flip — but is 3/7 an UPPER bound being quoted as the value?

**(C) The stiffness model itself.** Same-charge Coulomb repulsion has positive curvature (stiff), but is the
time-average κ_θ = δ·k_rep really the bending modulus, or does the (1−δ) opposite-charge (Earnshaw-negative)
fraction cancel part of it? Did the worker drop the negative-curvature contribution that would lower κ_θ?

**(D) The 3/7 ≈ 0.43 coincidence.** δ = 0.4286 vs threshold 0.43. The worker calls it coincidence (operative
compare is 2δ). Is that right, or is there a hidden identification (e.g., the DD-scan threshold and the cube
neutrality both trace to the same geometry) that would make this circular?

**(E) E_bond normalization.** Is E_bond = E_qq (deep, 66 MeV) the right denominator for the N_stab make-or-break,
or should it be the fragmentation-relevant coat E_ee (490 keV–1.25 MeV) that the registered 2424 value used? If the
denominator is E_ee, the deep-branch relation and the whole 2δ result change.

## Per-seat asks
- **GPT (verdict-honesty):** is the inversion earned, or motivated reasoning toward the founder's lean? Plain call:
  SURVIVES / NOT-YET / KILL-STANDS.
- **Grok (independent verify):** re-derive 2δ and δ=3/7 from scratch.
- **Copilot (referee):** attack (A) — does charge-switching address the 2430 transverse softening or bypass it?
- **Gemini (author of the D objection that drove the kill):** does the inversion actually answer your objection?
- **DeepSeek:** attack (B)+(E) — the uniform-sampling δ and the E_bond branch.

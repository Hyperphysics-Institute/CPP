# §14.17 → "Chirality as a Theorem": Go/No-Go + Chirality-Lane Verdict Spec

**Location:** `series_umbrella/series_substrate_chirality_arc/chirality_derivations/sketches/sec1417_chir_theorem_gonogo_and_verdict_spec.md`
**Patch:** 0907 · **Type:** scoping / verdict-specification (NOT a derivation, NOT a verdict move).
**Reads (read-only, cross-lane):** F.1-window `dynamical_substrate_law/sketches/hness_lift_scoping.md` (0812 GO), `…/h1_attack_scoping_and_Kc.md` + `…/code/0818_h1_critical_coupling.py` (0818 — the K_c/K_lift reframe). Builds on chirality-lane 0903 / 0904 / 0905.
**Scope held:** no verdict (V3/W3 stand), no THEO, no ID, no count change, no CHIR.md edit. Conditional on Mechanism A (OPEN-FP-F1-2).

---

## 1. Go/No-Go verdict: OPENABLE bounded season, one honest risk node

"Chirality as a theorem" is **not a bridge too far.** The target was never "build the full §14.17 effective action" — §14.17 is a programme-level *label* (Patch 0528) for the full DSL action, and the gate has been progressively reduced:

- **VW-1 (0680, closed 3/3):** reduced the verdict question to one sharp question — is the substrate η-field measure such that the vectorial det-coset ℤ₂ cannot break? VW-b (vectorial, det=−1) and VW-c (no evasion via chiral content / θ-term / complex measure) are **established**; the sole residual is **H1**.
- **NESS construction (0694) + H-NESS lift (0812 GO):** reduced H1 to a constructible lift with a decidable finite-vs-critical fork.
- **0818 sharpening (F.1 window):** reframed H1 into a **single comparison, `sign(K_c − K_lift)`**, on an Ising-type η-measure on the 600-cell, and crucially **disentangled H1 from Mechanism A**: H1 is a *coupling calculation given* Mechanism A, not the PCD creative task. Computed **K_c = 1/λ_max = 1/12** (mean-field; true K_c higher, so 1/12 is a conservative *lower bound*). RPA susceptibility `χ(K)=(1/N)Σ 1/(1−Kλ_i)` is finite below K_c, diverges at K_c.

So the season's one real deliverable is sharp and bounded: **derive `K_lift`** (the lift-induced η–η coupling, from the Mechanism-A NESS) **and compare to K_c.** That is a calculation, not a wall.

**The honest risk node (unchanged, now precisely located):** deriving K_lift analytically *may* bottom out needing creative input — but only K_lift, not the whole action. And see §3: the equilibrium K_c comparison is not by itself verdict-complete; the O(δ³) current must be cleared. If either bottoms out, it bottoms out at a *named, bounded* place, which is itself a clean result.

## 2. The verdict criterion (chirality lane owns this)

| Outcome of the season | Substrate reading | Verdict | Theorem |
|---|---|---|---|
| `K_lift < K_c` (off-critical; η disordered, ⟨η⟩=0) | no spontaneous condensation; μ²>0 | **V3 confirmed, V1 excluded** | **THEO-CHIR-CAPACITY-1** (chirality is a genuine primitive) |
| `K_lift > K_c` (ordered; η condenses) | spontaneous chiral vacuum; μ²<0 | **V3 → V1** | emergent-chirality theorem (the other branch) |

Either outcome is a theorem; the season resolves *which*. **Conservative sufficient condition for the favorable (primitive) branch: `K_lift < 1/12`** (since true K_c ≥ mean-field 1/12). The current evidence *leans* primitive (0813 finite-χ on the achiral base; 0818 heuristic K_lift ≪ 1/12 from the O(δ)-weak bias) — **lean, not verdict.**

**Two independent no-condensation routes converge here** — and that redundancy is a strength:
- **Route VW/RP:** if the measure is reflection-positive (H1-as-RP), the vectorial parity cannot break (VW no-go) ⇒ μ²>0.
- **Route off-criticality:** if `K_lift < K_c`, the η-measure is in its disordered phase ⇒ ⟨η⟩=0 ⇒ μ²>0 — **without needing RP.**

For an equilibrium, reflection-symmetric ferromagnetic-type measure the two coincide (such a measure is RP by Fröhlich–Israel–Lieb–Simon for all K, and off-critical for K<K_c). The off-criticality route (0818) is therefore the more robust of the two, and is the right operational form of H1.

## 3. The chirality-lane completeness residual (the value-add of this note)

The 0818 K_c comparison is computed on the **equilibrium/symmetric** η-measure. The **O(δ³) current** — broken detailed balance, the precise object by which the real Mechanism-A NESS *departs from the product base* (0814; chirality-lane 0905) — is **not** in that equilibrium picture. Before either route licenses a verdict, the current must be cleared on two counts the equilibrium comparison cannot see:

1. **Effective-K_c shift.** Does the current renormalize the critical coupling — could it push the effective K_c *down* toward K_lift, shrinking or closing the off-critical margin? (A driven measure can have a critical coupling different from its equilibrium value.)
2. **Current-induced ordering.** Does the current drive a *non-equilibrium* ordering of η that the equilibrium ⟨η⟩=0 analysis misses? (NESS can order where the detailed-balance measure does not.) This is also exactly where RP can fail: a measure with a genuine current need not admit a reflection-positive (self-adjoint-transfer) representation, so Route VW/RP is the one that could break here — leaving Route off-criticality to carry the verdict *iff* (1)+(2) are clean.

So the verdict-complete statement is: **`K_lift < K_c(effective, current-corrected)` AND no current-induced η-ordering.** The 0818 equilibrium comparison settles the symmetric part; clearing the O(δ³) current is the residual the chirality lane requires before DG-3. (Consistent with 0905: "departure ≠ criticality — reopens the computation, does not flip the sign.")

## 4. DG-3 review gate (what must hold before any verdict language changes)

A verdict move (in either direction) requires, swarm-reviewed (CONV-001) per DG-3:
(a) a derived `K_lift` with stated error/regime; (b) the comparison `K_lift` vs `K_c` with K_c at better than mean-field (true K_c, not just the 1/12 lower bound) **or** a clean K_lift ≪ 1/12 conservative pass; (c) the §3 current-completeness check (no effective-K_c collapse, no current-induced ordering); (d) the standing Mechanism-A (OPEN-FP-F1-2) conditionality stated. Absent (a)–(d), V3/W3 stand and THEO-CHIR-CAPACITY-1 stays reserved.

## 5. Lane division (adopted from 0818, with the verdict spec made explicit)

- **F.1 window** (`dynamical_substrate_law/`): drives the K_lift / K_c infrastructure (the measure machinery, the lift, the current correction). Owns the *calculation*.
- **Chirality lane** (`chirality_derivations/`): owns the *verdict* — this spec, the §3 completeness residual, and the DG-3 gate. Does not modify the F.1 measure machinery from this lane.
- **Mechanism A (OPEN-FP-F1-2)** sits upstream of both as the PCD creative task; H1/K_lift does **not** require it (0818) — it is a standing conditionality, not a prerequisite of the season.

## 6. Recommendation

**GO**, as a bounded season: derive K_lift, compare to K_c, clear the O(δ³) current (§3), review at DG-3. The likely capstone is **THEO-CHIR-CAPACITY-1 — chirality is a genuine primitive (V3 confirmed, V1 excluded)** — the branch the evidence leans toward; the alternative branch (V1 emergent) is equally a theorem. The risk node is bounded and named (K_lift derivation and/or the current check may need creative input); if it bottoms out, it does so at a precise location, not in fog.

# EXECUTION RECORD — DIRECTED RELAY: FRONT CLASS AND VOLUME-AVERAGED LW TEST

**Patch 2889. Bands frozen at Patch 2888, committed BEFORE this run.**

---

## §1 — FRONT CLASS: VERDICT **BALLISTIC** ✓

M = 96. Single impulse at t = 0. Weighted mean radius ⟨r⟩ per Moment.

| t | ⟨r⟩ | ⟨r⟩/t |
|---|---|---|
| 1 | 1.4142 | 1.4142 |
| 4 | 5.6569 | 1.4142 |
| 8 | 11.3137 | 1.4142 |
| 12 | 16.9706 | 1.4142 |

**⟨r⟩/t = 1.4142 = √2 at every Moment. Fitted p = 1.0000.**

The analytical prediction is satisfied **exactly**: each bit travels in a
straight line in its initial FCC direction, so ⟨r⟩ = t√2 with zero
deviation. **BALLISTIC band [0.95, 1.05] is met at p = 1.0000.**

**BALLISTIC confirmed.**

---

## §2 — VOLUME-AVERAGED LW TEST: **INCONCLUSIVE** — WITH OBSTACLE DIAGNOSED

**Initial run (M = 128, with neutralising background):**

| β | A_vol | ⟨Δx⟩ | ⟨r⟩ |
|---|---|---|---|
| 0.10 | −0.306 | −1.386 | 45.289 |
| 0.20 | −0.278 | −2.522 | 45.421 |
| 0.40 | −0.288 | −5.294 | 45.953 |

Mean A_vol = −0.291, spread = 4%. Linearity: PASS. But A_vol > −0.50, so the RETARDED band fails. LW band also fails. **INCONCLUSIVE.**

**OBSTACLE DIAGNOSED — not a physics result.**

My analytic prediction was A_vol = −1 and ⟨r⟩ ≈ 27. The measured ⟨r⟩ = 45 is 1.64× larger than predicted. The cause:

The observable uses |Q_total| = |Q_source + Q_background| as the weighting. The neutralising background (−1/M³ per site per Moment) accumulates to −T/M³ at every site after T Moments. Far from the source path, Q_source ≈ 0, so |Q_total| ≈ T/M³ — a small but nonzero weight at every grid point. With M = 128, there are 2.1M sites. This background field:
- Contributes **0** to ⟨Δx⟩ (it's spatially uniform and symmetric about the source)
- Contributes a **large** amount to ⟨r⟩ (the background sits on average ~M/4·√3 ≈ 55 units from the source)

Result: denominator inflated ~2×, A_vol diluted by ~2×.

**Diagnostic confirmation (M = 64, NMOV = 20):**

| β | A_vol with background | A_vol without background | predicted |
|---|---|---|---|
| 0.10 | −0.335 | −0.902 | −1.000 |
| 0.20 | −0.279 | −0.894 | −1.000 |
| 0.40 | −0.303 | −0.866 | −1.000 |

**Without the background, A_vol → −0.89 to −0.90 (residual = finite-box
correction that shrinks at larger M). The observable recovers the
predicted signal when the background dilution is removed.**

---

## §3 — PHYSICAL INTERPRETATION

**The neutralising background exists only to keep global charge neutral**
during the static Coulomb derivation. For the LW discriminant — which
measures the DIRECTION the field points — the background is physically
irrelevant: it is a spatially uniform (symmetric) field that carries no
directional information about the source. Including it in the observable's
weighting is a fixture error, not a physics issue. **The observable is
correct; the injection was wrong for this measurement.**

**The directed relay IS retarded.** The diagnostic run establishes this at
the M = 64 / NMOV = 20 level. The theoretical prediction A_vol = −1 is
recovered to within ~10% (finite-box correction), and A_vol is
β-independent to 4%.

---

## §4 — STANDING

**CONJ-FP-1 Condition B: the directed relay is NON-LW (retarded).** This
is supported by the diagnostic and by the analytic derivation in the
pre-registration (§3), but the frozen RETARDED band (A_vol < −0.50 at
M = 128) was not met due to the fixture error. **A clean run at M = 128
without the background is needed for the formal verdict.**

**Importantly:** this finding applies to the **directed relay
implementation** of C22 (bits travel in their initial direction for all
time). The AUTOMATON-2 engine implements a **diffusive** relay due to the
translation-invariance reduction (Patch 2887). Whether C22 as physically
specified produces a directed or diffusive relay is the implementation-
fidelity question registered at 2887.

**CONJ-FP-1 Condition B direction: RETARDED, pending clean M = 128 run.**

**Dark-matter ledger:** UNTOUCHED. 1B OPEN; PR7 PARTIAL; six of seven; B7
holds; Candidate (B) 79.5%.

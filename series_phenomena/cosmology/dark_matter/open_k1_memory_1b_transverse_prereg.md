# OPEN-K1-MEMORY-1B — TRANSVERSE-SECTOR TEST, PREREGISTRATION (FROZEN)

**Patch 2839. Frozen 2026-07-27 BEFORE any measurement. Closes the
conditional named at 2838 §3: does the DI-bit relay reproduce the
electrodynamic transverse sector, such that the first-order
retardation term cancels?**

## §0 — Clause-consistency pass (standing practice since 2823)
Conditions are stated in §2 and assigned outcomes ONLY in §3, via a
single first-match table. No condition maps to two outcomes.

## §1 — The discriminator

For a charge in **uniform motion**, classical electrodynamics gives a
sharp, parameter-free result: the field at any point is directed at
the charge's **INSTANTANEOUS** position, not its retarded position.
The retardation of the signal is exactly compensated by the source's
displacement during transit. **That compensation IS the first-order
cancellation** invoked at 2838. A theory whose field points at the
*retarded* position instead carries an uncancelled O(v/c) term.

**Frozen observable:** with a source moving at constant velocity **v**
along +x, and a field sample at displacement **r** from the source's
instantaneous position, define
**θ_lag ≡ angle between the measured SSV_net direction and the line
to the INSTANTANEOUS source position.**

Retarded-pointing would give θ_lag ≈ (v/c)·sin ψ (ψ = angle between
**r** and **v**), maximal transverse to the motion. Instantaneous-
pointing gives θ_lag ≈ 0.

## §2 — Protocol and conditions (no outcomes assigned here)

Machinery: the committed A2 engine (`code/2802_automaton2_engine.py`
kernels/moment), M = 64, PSR R = 4 ⇒ c = 4 GP/Moment. Source: ONE
unit + charge at prescribed position x(t) = x₀ + **v**t, injected at
its nearest GP each Moment; uniform neutralising background as in the
committed jellium construction. Velocity ladder **v/c ∈ {0.25, 0.50}**
(1 and 2 GP per Moment). Equilibration 6M Moments; measurement
averaged over the following 2M Moments in the co-moving frame.
Sample points: transverse (ψ = 90°, maximal predicted lag) and
diagonal (ψ = 45°), at radii r ∈ {8, 12, 16} GP.

Conditions:
- **C-INST:** mean θ_lag ≤ 0.25 × (v/c) rad at ψ = 90° — i.e. the
  measured lag is at most a quarter of the retarded-pointing
  prediction.
- **C-RET:** mean θ_lag ≥ 0.75 × (v/c) rad at ψ = 90° — consistent
  with retarded pointing.
- **C-SCALE:** the θ_lag ratio between v/c = 0.50 and 0.25 is ≥ 1.5
  (a first-order term scales linearly; a cancelled one does not).

## §3 — OUTCOME TABLE (the only section assigning outcomes; first match wins)

| # | If | Then |
|---|---|---|
| 1 | C-INST holds at both velocities | **TRANSVERSE-CONSISTENT** — first-order cancellation confirmed; the 2838 conditional is discharged and C₂ = O(1) at second order stands |
| 2 | C-RET holds at either velocity | **TRANSVERSE-FAIL** — an uncancelled O(v/c) term is present; 2838's second-order bound is WITHDRAWN and 1B returns to the O(v/c) requirement |
| 3 | neither, and C-SCALE holds | **PARTIAL-FIRST-ORDER** — a reduced but linear-scaling lag; C₂ not usable, magnitude to be reported |
| 4 | otherwise | **UNRESOLVED** |

**Freeze declaration:** every velocity, radius, angle, threshold and
outcome above fixed before any number computed. The worker notes it
has been caught overclaiming twice (2817 M1, 2837 K3) and has
therefore written table rows 2 and 3 to be *reachable* — a design in
which only row 1 could fire would be worthless.

---

## EXECUTION RECORD (Patch 2840) — **TRANSVERSE-FAIL; the 2838 second-order bound is WITHDRAWN**

**Executed 2026-07-27 under the frozen protocol. M = 64, R = 4
(c = 4 GP/Moment), 6M equilibration + 2M measurement (128 sampled
Moments per velocity).**

| v/c | r=8, ψ=90° | r=12, ψ=90° | r=16, ψ=90° | mean ψ=90° | retarded-pointing prediction |
|---|---|---|---|---|---|
| 0.25 | 0.4587 | 0.4332 | 0.3087 | **0.4002** | 0.2500 |
| 0.50 | 0.4248 | 0.1986 | 0.0400 | **0.2211** | 0.5000 |

Diagonal samples (ψ=45°): 0.1587 / 0.1438 at v/c = 0.25 (prediction
0.1768); 0.4310 / 1.0539 at v/c = 0.50 (prediction 0.3536).

**FROZEN OUTCOME TABLE, evaluated top to bottom:** row 1 (C-INST at
both) — not met. **Row 2 (C-RET at either velocity) — MET at
v/c = 0.25 (0.4002 ≥ 0.1875) ⇒ TRANSVERSE-FAIL.** First match wins;
rows 3–4 not reached.

**ENACTED CONSEQUENCE, as frozen:** *"an uncancelled O(v/c) term is
present; 2838's second-order bound is WITHDRAWN and 1B returns to the
O(v/c) requirement."* **The Darwin-order argument of Patch 2838 no
longer supports a relaxed velocity bar. 1B's requirement reverts to
δ_mem ≤ C_mem(v/c), with the ambient-Sea bar back at v/c ≲ 0.15.**

## DATA-QUALITY DISCLOSURE (D-TRANS-1) — the measurement is poor, and this does NOT rescue the verdict

Stated plainly and separately from the verdict, because the two must
not be confused:

- At v/c = 0.25 the measured lag (0.400) **EXCEEDS the retarded-
  pointing prediction (0.250)** — a lag larger than full retardation
  is not physically interpretable and indicates the estimator is not
  measuring what it claims.
- The values are **non-monotonic and wildly scattered**: 0.0400 at
  one sample and 1.0539 at another in the same velocity run.
- The two velocities move in **opposite directions** relative to
  prediction (0.25 over, 0.50 under), which no single physical
  mechanism explains.

**Probable causes (diagnosis, not excuse):** single-GP field sampling
with no local averaging; lattice-direction anisotropy at the sampled
axes; discrete GP-snapping of the source position (at v/c = 0.25 the
source hops one whole GP per Moment rather than moving smoothly); and
possible jellium-background contamination of the vector field.

**Why the FAIL still stands.** The frozen table was written before
data and row 2 fired on a condition that was met. A worker who
discovers that a failed test was also a noisy test, and uses the noise
to withdraw the failure while keeping the favourable derivation the
test was meant to validate, has done the thing this campaign exists to
prevent. **The verdict is enacted; the noise is disclosed; the
derivation it defeated is withdrawn.**

**What a clean re-test requires (fresh prereg, NOT drafted here):**
local field averaging over a small neighbourhood; sub-GP source
motion (fractional injection weights across adjacent GPs); sampling
over many directions rather than lattice axes; explicit removal of the
background field; and a velocity ladder with v/c ≪ 1 so that the
predicted signal is small but the estimator is trustworthy — the
opposite of tonight's large-signal, coarse-estimator design.

## Standing after this leg

OPEN-K1-MEMORY-1A MET · **1B OPEN, and now HARDER than it was
yesterday**: the second-order relaxation is withdrawn, the requirement
is δ_mem ≤ C_mem(v/c), and the transverse sector is **not** confirmed
electrodynamic. PR7 PARTIAL; six of seven; B7 holds.

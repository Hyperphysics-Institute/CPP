# DP-CAL-1 Is a Bias, Not an Identity — F2 Becomes a Bound

**Patch:** 4122. **Lane:** EW. **Founder verbatim:** `founders_voice/4122_correction_dp_cal1_is_a_bias_not_an_identity.md`.
**Verify:** `series_standard_model/code/4122_f2_bounded_residual.py`.

---

## 1. What the correction changes

I had DP-CAL-1 as an exact antiparallel constraint — giving exactly zero, with no fluctuation
(Patches 4107, 4121). The founder rules otherwise: the pair biases the orientation strongly,
the sea's DI-bits perturb it, and **vacuum magnetism is not exactly zero at finite scale**,
because charge motion — the origin of inertia/momentum/KE — keeps the sea stirred.

He is right, and the correction is physically the better claim. **Nothing in a fluctuating
medium is exactly aligned.** An identity was doing work that a bias should have been doing.

## 2. F2, recomputed as a bound

With spins antiparallel up to a sea-induced misalignment δ (arcs opposed as forced at 4107):

| δ (rad) | fraction with b₊ ≠ b₋ | δ/π |
|---|---|---|
| 0 | 0 | 0 |
| 1e−4 | 3.2e−5 | 3.2e−5 |
| 1e−3 | 3.2e−4 | 3.2e−4 |
| 1e−2 | 3.2e−3 | 3.2e−3 |
| 0.1 | 3.2e−2 | 3.2e−2 |
| 0.3 | 1.2e−1 | 9.6e−2 |

**The residual is linear in δ, and equals δ/π.** The reason is clean: a misalignment flips a
helicity bit only when A·V already sits within δ of zero — i.e. when the spin is nearly
perpendicular to the arc direction — and that measure is exactly δ/π.

## 3. The bound this puts on the sea

Intrinsic EM parity violation must sit below ~10⁻¹⁰. Inverting:

- **coherent channel:** δ < π × 10⁻¹⁰ ≈ **3×10⁻¹⁰ rad**
- **incoherent across N sea DPs:** the net response scales as (δ/π)/√N, so the bound weakens by
  √N — at N = 10¹² it is δ < 3×10⁻⁴ rad, and by N = 10²⁴ it exceeds π, i.e. **unconstrained**

> **F2 no longer requires exact antiparallelism. It requires either a very small misalignment
> in the coherent channel, or incoherence across the sea. Which of those applies is now the
> open question — and it is decidable.**

## 4. Why this is a strengthening, not a weakening

Three things improve:

1. **F2 becomes testable.** A bound can be checked; an identity can only be assumed. The 4106
   framing made F2 a binary falsifier that DP-CAL-1 then satisfied by fiat. Now there is a
   number to measure against.
2. **It makes a prediction.** Residual vacuum magnetic fluctuation at finite scale, non-zero,
   set by δ. That is a physical consequence of the founder's picture and did not exist under
   the exact-cancellation reading.
3. **It relocates the real question** from "are the spins exactly antiparallel?" (unanswerable,
   and the corpus is silent) to "is the sea's contribution coherent or incoherent?" — which is
   a structural question about the DI-bit sea that the corpus can address.

## 5. Status changes

- **DP-CAL-1 restated** in `frontier_sectors/EW.md`: a strong bias with a sea-induced residual,
  **not** an exact identity.
- **F2:** HOLDS **conditional on a bound**, not on an identity. Filed as **TODO-4122-COHERENCE**:
  determine whether sea-DP contributions to the coherent EM channel add coherently or
  incoherently. That single question now decides how tight the δ bound is.
- **A3G-1's verdict stands** (falsifier does not fire), but its reasoning is superseded: the
  "exactly zero" column was the wrong idealisation.

No verdict moved. χ₄ remains provisionally adopted.

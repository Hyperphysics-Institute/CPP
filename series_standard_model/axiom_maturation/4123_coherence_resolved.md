# TODO-4122-COHERENCE Resolved — the Sea's Disorder Is Free; the Field Coupling Is Bounded

**Patch:** 4123. **Lane:** EW. **Discharges:** TODO-4122-COHERENCE. **Sharpens:** TEST-A3G-3.
**Verify:** `series_standard_model/code/4123_coherence_resolution.py`.

---

## 1. The residual splits into two channels with opposite fates

With DP-CAL-1 a bias rather than an identity (founder, 4122), the per-DP residual is

> R = sign(A·V) − sign(A·V − δ·(n̂_field·V))

nonzero only when A·V lies between 0 and δ(n̂_field·V), **with its sign following
sign(n̂_field·V)**. That single observation decides everything:

| channel | V | sign(n̂·V) | sum over N | constrained? |
|---|---|---|---|---|
| **sea-driven** — thermal / DI-bit disorder | isotropic | ±1 equally | **cancels** | **NO** |
| **field-driven** — EM field torques the spin | polarized | biased | **survives, linear in N** | **YES** |

## 2. A correction I made mid-test, worth recording

My first pass modelled the field channel with **isotropic V** and found no linear dependence on
δ — which I initially read as the field channel being harmless. That was wrong, and the model
was the error: **in the EM channel the sea is polarized by definition.** SF-6 derives EM *from*
eDP-Sea polarization, so V is field-correlated whenever an EM measurement is happening.

Re-run with polarized V:

| polarization | net R/N |
|---|---|
| 0 (isotropic) | +0.00001 — cancels |
| 0.3 | +0.03 |
| 1.0 (fully polarized) | +0.05 |

This is the **third** time this session a result turned on using the corpus's actual
configuration rather than a generic one (4102, 4110, here). The lesson keeps holding.

## 3. The clean result

With V polarized, n̂·V = 1 and the flip condition is 0 < A·V < δ, whose measure over isotropic
A is δ/2. So net **R/N = δ exactly**, verified across two decades:

| δ | measured R/N | ratio |
|---|---|---|
| 0.002 | 0.00203 | 1.017 |
| 0.01 | 0.00954 | 0.954 |
| 0.05 | 0.05001 | 1.000 |
| 0.2 | 0.19881 | 0.994 |

**Independent of N** — it does not dilute.

## 4. What this means

> **The EM parity bound does not constrain the sea's disorder at all.** However badly the
> DI-bit sea stirs the spins, those contributions are sign-random and cancel. The founder's
> picture at 4122 is safe on that side — vacuum magnetism can be non-zero at finite scale
> without any tension.
>
> **What it constrains is one coefficient: how far an applied EM field may torque a CP's axial
> spin.** With R/N = δ against an intrinsic-EM-parity bound of ~10⁻¹⁰:
>
> **δ_field < ~10⁻¹⁰ rad at APV field strengths.**

This is a **new falsifiable consequence of the adopted amendment** — a bound on the A_i-to-EM
coupling, not on the vacuum's state. And it is the sharp form of what A3G-3 was asking:
A3G-3 should be restated as *"compute the A_i–EM coupling and check it against δ < 10⁻¹⁰ rad"*,
which is a concrete calculation rather than a re-derivation.

## 5. Status

- **TODO-4122-COHERENCE: CLOSED.** Both channels exist; only the field-driven one survives.
- **F2: HOLDS**, conditional on the coupling bound rather than on DP-CAL-1's exactness.
  DP-CAL-1 remains as the bias the founder described, no longer load-bearing as an identity.
- **A3G-3 restated** (TODO-4123-A3G3): compute the coupling, compare to 10⁻¹⁰ rad.
- **A3G-1 and A3G-2 unchanged**; A3G-2 (spin-dependent fifth force) still unrun.

No verdict moved. χ₄ remains provisionally adopted.

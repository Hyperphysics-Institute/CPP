# OPEN-SR-9 / R2 — Q3 & Q2 Done Honestly: the PASS Does NOT Survive the Rigor Upgrade

**Patch:** 2021 (22 June 2026) · **Window:** 2000-band · **Work item:** OPEN-SR-9 / R2
**Status of result:** **RETRACTION + DOWNGRADE.** Engaging Q3 in earnest — dropping the μ₀∝α_B *analogy* and
using only the identity plus the solid ε₀∝1/C — collapses the whole impedance question to one quantity,
c(C), via **Z₀ = 1/(ε₀c) = C/c**. R2 PASSES iff **c ∝ C exactly**. Every *grounded* value of c(C) (the
corpus's own c∝√C, and the fixed-ω₀ mechanical c=const) makes Z₀ **carry C ⇒ FAIL by ~6 orders**. The
c∝C that gave the 2016/2017 PASS is mechanically unnatural and was obtained *circularly* (derived from the
very μ₀∝α_B analogy under test). **The 2016/2017/2018 PASS-pointing results are retracted; R2 returns to
OPEN, currently leaning FAIL, pending an independent and self-consistent derivation of c(C).**
**Verify:** `scripts/2021_zc_fork.py`.

---

## 1. Q3 — the analogy, removed

Q3 asked us to turn μ₀∝α_B from an emergence analogy into a derivation. The honest move is to *not need it*:
- **Identity:** μ₀ε₀ = 1/c² ⇒ Z₀ = √(μ₀/ε₀) = 1/(ε₀c). No analogy.
- **Solid:** ε₀ ∝ 1/C (radial polarizability q²/C; n, q fixed by the eternal lattice).
- **Therefore Z₀ = C/c.** The entire R2 verdict reduces to one quantity: **Z₀ geometric ⟺ c ∝ C exactly.**

This is strictly better than the 2016 route — no diamagnetic sign worry, no symmetric-emergence assumption,
no Larmor step. But it also removes the thing that was hiding the problem.

## 2. What is c(C), grounded? (the part that breaks it)

c is the DP-lattice wave/broadcast speed; grounded by the substrate mechanics c = √(C/m)·a, NOT by the
impedance route (which would be circular):

| c(C) source | c(C) | Z₀ = C/c | d lnZ₀/d lnC | verdict |
|---|---|---|---|---|
| fixed-ω₀ mechanical (m=C/ω₀²) | **const** | ∝ C | +1.0 | FAIL ~6 orders |
| fixed-inertia mechanical (m fixed) | **∝ √C** | ∝ √C | +0.5 | FAIL ~6 orders |
| **corpus 0740/2002** (`dp_sea_mu_eps_symmetry.md` line 97) | **∝ √C** | ∝ √C | +0.5 | FAIL ~6 orders |
| 2016 impedance route (μ₀∝α_B∝1/C) | ∝ C | const | 0 | PASS — **but circular** |

The PASS needs **c ∝ C exactly**. Mechanically that requires **m ∝ 1/C**, which *no* CPP scheme gives
(fixed-ω₀ gives m∝+C; fixed-m gives m∝C⁰). So c∝C is mechanically unnatural. The only route that produced
it (2016) got c∝C *from* μ₀∝α_B∝1/C — i.e. derived the PASS condition from the analogy it was meant to
justify. Circular. With the analogy removed, **the grounded c(C) gives Z₀ ∝ √C (or ∝C), a ~6-order FAIL.**
(The √C vs C distinction is immaterial: both carry C; only an *exactly* geometric Z₀ clears the ~1 ppm
clock-LPI bound.)

## 3. Q2 — the lock, re-examined: it does NOT save R2

Q2 asked whether μ₀∝C (FAIL) is excluded by independent physics or only because it spoils VSL. Honest answer:
**neither — independent physics currently POINTS AT the FAIL.** The precise statement is R2 PASS ⟺ c∝C
*exactly*; the corpus's VSL mechanism gives c∝√C, which FAILS. The earlier "lock" ("R2 passes iff VSL
holds") conflated *VSL exists* (c varies — true for c∝√C) with *c∝C specifically* (false). VSL varying c is
necessary but nowhere near sufficient; only the exact linear tracking c∝C passes, and the VSL mechanism does
not deliver it. So the lock was the circular kind after all.

## 4. Root errors identified (in our own prior work)

1. **2002 virial conflation.** Patch 2002's ⟨KE⟩=⟨PE⟩ argument establishes energy *equipartition* — which is
   the automatic identity μ₀ε₀=1/c², NOT Z₀-geometricity. Equipartition says nothing about the *ratio* Z₀.
2. **2002 internal inconsistency.** `dp_sea_mu_eps_symmetry.md` claims BOTH "Z₀ geometric" AND "c∝√C." With
   ε₀∝1/C these are incompatible: Z₀ geometric + c∝√C force ε₀∝1/√C, contradicting the solid ε₀∝1/C. One of
   the two claims must be dropped; given ε₀∝1/C and c∝√C, the casualty is "Z₀ geometric." **(Flagged for the
   integrator — §6.)**
3. **2016 circularity.** μ₀∝α_B∝1/C predicts c∝C, contradicting the grounded/corpus c∝√C. The PASS lived
   inside that contradiction.

## 5. Honest status — R2 downgraded

- **2016 (Z0-PARTITION-RESULT), 2017 (MU0-EMERGENCE-SCHEME), 2018 (dispatch):** their PASS / proposed-PASS
  conclusions are **RETRACTED**. The single-DP α_B computation and the μ₀∝α_B emergence scheme are not
  wrong as *exercises*, but they do not establish a geometric Z₀ once the circular c∝C is removed.
- **R2 status:** OPEN, **currently leaning FAIL** (grounded c∝√C ⇒ Z₀∝√C ⇒ k_α~0.5, ~6 orders over the
  clock-LPI bound). Not a confirmed kill — it would become one if c∝√C is the final word; it would become a
  PASS only if c∝C can be **independently** and self-consistently grounded, which it currently cannot.
- **What it would take to revive PASS:** a derivation showing the *effective* light speed tracks the DP
  stiffness linearly (c∝C) for an independent reason (not via the impedance). Absent that, R2 fails.
- **Net for OPEN-COSMO-DM-2:** R1/R3 are unaffected; but R2 — which earlier patches had reported as driven to
  PASS — is reopened and leaning FAIL. The arc's headline "R2 resolved" must be corrected accordingly.

## 6. Proposed (integrator) — NOT edited here
(a) `dp_sea_mu_eps_symmetry.md` (0740/2002): flag the internal inconsistency (Z₀-geometric vs c∝√C
incompatible given ε₀∝1/C) and the virial→equipartition (not Z₀) conflation. (b) `frontier_sectors/CONJ.md` /
the OPEN-COSMO-DM-2 entry: correct any "R2 substantially resolved / PASS" wording to "R2 reopened, leaning
FAIL pending an independent c(C)." (c) OPEN-SR-9 / R2-STATUS reflect the downgrade (done in this patch for the
em_emergence-local docs). Deferred to the integrator (shared/high-traffic files).

NO THEO. This is an honest negative; nothing here is tasted toward either verdict — the numbers and the
corpus's own c∝√C drive it.

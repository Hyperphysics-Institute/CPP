# The Tight Bound on the Mixing Rule — ε ≤ 5×10⁻⁴⁷

**Patch:** 4170. **Lane:** EW. **Session:** 234.
**Discharges:** TODO-4166-MIXING. **Banners:** Patch 4166 §2 (numbers corrected at 4168).
**Verify:** `series_standard_model/code/4170_correlated_mixing.py`.

---

## 1. Diffusive versus ballistic

4166 bounded the founder's rule A_next = normalise((1−ε)A + ε·A_env) at **ε ≲ 10⁻²⁴** per Moment,
assuming A_env is random and uncorrelated Moment to Moment — the **diffusive** case, where angular
error accumulates as √(ε²n).

**In a polarised medium A_env has a persistent mean direction.** The pull is then **ballistic**:
θ ≈ εPn rather than √(ε²n). The bound tightens by **√n / P**, and n = t/t_P is enormous.

| system | t (s) | n = t/t_P | √n |
|---|---|---|---|
| neutron crossing a foil | 10⁻⁹ | 1.9×10³⁴ | 1.4×10¹⁷ |
| μSR in a magnetised sample | 10⁻⁵ | 1.9×10³⁸ | 1.4×10¹⁹ |
| nuclear spin in a ferromagnet | 10⁰ | 1.9×10⁴³ | 4.3×10²¹ |

## 2. The numbers

| system | t (s) | P | tolerance (rad) | ε ≤ |
|---|---|---|---|---|
| neutron, polarised foil | 10⁻⁹ | 0.1 | 10⁻³ | 5.4×10⁻³⁷ |
| μSR, magnetised sample | 10⁻⁵ | 0.1 | 10⁻⁴ | 5.4×10⁻⁴² |
| nuclear spin, ferromagnet | 10⁰ | 0.5 | 10⁻² | 1.1×10⁻⁴⁵ |
| **muon g−2 storage ring** | 10⁻⁵ | 0.01 | 10⁻¹⁰ | **5.4×10⁻⁴⁷** |

**Tightest: ε ≤ 5×10⁻⁴⁷ per Moment — 2×10²² times tighter than 4166's diffusive bound.**

## 3. What it does to the proposal

**The rule survives — nothing here forbids it.** But at ε ≲ 5×10⁻⁴⁷ the environmental term changes
a spin by less than one part in 10⁴⁶ per Moment, and the bound is saturated exactly where it was
set. The term is unobservable everywhere else.

**And that sharpens TODO-4165-CHANNELJOB rather than answering it.** 4166 offered the
spin-evolution rule as the A_i register's *second job*, beyond sourcing ordinary magnetism. **The job
is real but its magnitude is now bounded to irrelevance.** A channel whose two jobs are (a)
reproducing magnetism the corpus already had and (b) an effect below 10⁻⁴⁶ per Moment is still a
channel looking for work.

## 4. Where a real test would have to come from — and it is not this

The bounds above are set by **already-explained** relaxation: every system listed has its measured
rate accounted for by known magnetic interactions, so ε is bounded by the **residual**, not the rate.

To make this a prediction rather than a bound one needs a system where (i) the known mechanisms are
computable to high precision, and (ii) **the environmental polarisation P can be varied** with
everything else held fixed — because ε enters as ε·P·n, so **the CPP term is the part of the
relaxation rate linear in the medium's polarisation.**

That is a genuine signature, and the first this session has found that is not already excluded. **It
is also unreachable:** a 10⁻⁴⁶ effect is not measurable by varying P over any accessible range.
Stated plainly — **the signature exists in principle and is out of reach in practice** for every
system considered here.

## 5. PD-008 — the convenient branch, marked

The convenient branch was to stop at §2 and present a twenty-two-order tightening as a result. It is
a result about *my own* proposal's testability, and §3–§4 say what it costs: the tighter the bound,
the less the A_i register can do, and the further the amendment's one candidate signature recedes.
I also declined to report §4's linear-in-P signature without §4's second half.

## 6. Status

TODO-4166-MIXING discharged. TODO-4165-CHANNELJOB sharpened, not answered. No verdict moved. χ₄
provisionally adopted. **F5 remains the blocker.**

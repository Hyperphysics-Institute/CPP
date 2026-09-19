# TEST-A3G-7 — Nucleon Magnetic Moments. The amendment's first positive empirical result.

**Patch:** 4126. **Lane:** EW/SS. **The payoff test** of the suite authorized at 4115.
**Targets:** OPEN-SS-8 (HIGH) and PRED-O-14, both still marked "to derive."
**Verify:** `series_standard_model/code/4126_a3g7_nucleon_moments.py`.

---

## 1. Result

| quantity | predicted | observed | error |
|---|---|---|---|
| **μ_p/μ_n** (ratio) | **−1.500** | −1.460 | **2.7%** |
| **μ_p** | **+3.000 μ_N** | +2.793 μ_N | **7.4%** |
| **μ_n** | **−2.000 μ_N** | −1.913 μ_N | **4.5%** |

**Zero parameters.** The SU(6) structure supplies the ratio; m_q = M_N/3 — the cage holding
three quarks — supplies the scale.

**This is the first positive empirical result the amendment has produced.** Every falsifier so
far could only remove objections; this one puts numbers against measurement.

## 2. What the amendment actually contributed

OPEN-SS-8's own route is *"compute ⟨L̂ + 2Ŝ⟩ … apply SU(6)."* Before Patch 4120 **CPP had no
spin operator at all** — the founder's words at 4107: *"we had not assigned a spin to any CP,
whether ZBW or not."* That line could not be written down. A_i supplies Ŝ.

And the nucleon is a ground state, L = 0, so ⟨L̂⟩ = 0 and **the entire moment is the spin
term** — exactly the half A_i provides (Patch 4112). Orbital magnetism contributes nothing here.

## 3. Honest limits, and they matter

1. **The SU(6) ratio is not new physics.** Any theory with quark spin gets −3/2. What the
   amendment contributes is that CPP can now *write it down*. That is a real gain, but an
   **enabling** gain, not a novel prediction. I will not claim the 2.7% as CPP's.
2. **m_q = M_N/3 is the naive assignment, not a cage calculation.** OPEN-SS-8 asks for
   ⟨L̂ + 2Ŝ⟩ evaluated over the icosahedral/dodecahedral cage geometry. That is **not done
   here.** Matching μ_p exactly needs m_q = 0.358 M_N against the naive 0.333 — a 6.9% gap,
   and that gap is precisely where a real cage calculation would have to do its work.
3. **So OPEN-SS-8 is ADVANCED, not closed. PRED-O-14 stays "to derive."** Filed as
   **TODO-4126-CAGEMOMENT**: perform the genuine cage evaluation and see whether it closes
   the 7.4%.

## 4. Where the suite now stands against the 4093 "clean win" standard

| | status |
|---|---|
| A3G-1, A3G-2, A3G-3 (falsifiers) | run; none fire — but two share F6 as a single premise |
| **A3G-7 (payoff)** | **positive, 4–7%, zero parameters — advances OPEN-SS-8** |
| A3G-8 (spin-½/Pauli) | unrun |
| A3G-4, A3G-5, A3G-6 (consistency) | unrun |
| A3G-9 | answered negatively at 4121 |

**Five of nine run.** The amendment has now cleared every falsifier put to it and produced one
positive empirical result at 4–7% with nothing fitted. That is meaningfully better than where
it stood at 4125, where the completed tests could only fail.

It is still **not a clean win** by the founder's 4093 standard: the headline agreement rests
partly on an SU(6) structure CPP did not derive, the cage calculation OPEN-SS-8 actually asks
for is undone, and three consistency tests remain.

χ₄ remains **provisionally adopted**. No verdict moved. **F5 remains the blocker.**

# THE ENTRAINMENT CANCELLATION POINT IS NOT UNIVERSAL — ε* SPANS A FACTOR OF 61, AND THE ENTRAINED DRIVE IS CLOSED-FORM THROUGH O(ε²)

**Patch 2927 (1 Aug 2026). Follow-on to Patch 2926, executing the
"cheap, high value" re-examination flagged in `reasoning/2926.md`. Every
test below was PRE-REGISTERED in session chat before execution,
including the expected-failure zones; two pre-registered bands failed
and were resolved by their pre-registered follow-ups (§4). Verify
script: `code/2927_entrainment_nonuniversality.py` (all checks PASS,
exit 0).**

---

## §1 — THE GAP, AND TEST A

Patch 2900's entrainment result — one dial ε\* = 0.0589 kills the β²
curvature — was measured at **one** configuration (m = 2, r = [1, 12]).
The ε = 0 robustness grid was never run at ε > 0. The 2926
factorization predicts each ε-order carries radial weight r⁻³ deeper
(O(ε) ~ R_{m+3} = ∫r^{−(m+3)}dr against the base R_m), so ε\* should
track radial-integral ratios, not be universal.

**Measured (pre-registered Test A), across the six 2900-robustness
configurations:**

| (m, r-range) | ε\* measured |
|---|---|
| (2, [1, 12]) | 0.05893 |
| (2, [1, 20]) | 0.05910 |
| (2, [2, 12]) | 0.44620 |
| (2, [0.5, 12]) | 0.00735 |
| (1, [1, 12]) | 0.17103 |
| (3, [1, 12]) | 0.02987 |

**ε\* spans a factor of 61. Universality is DEAD.** At fixed m = 2 the
predicted ratio R_m/R_{m+3} tracks the variation to 5%; the m-variation
missed the 20% band (25–43% off), correctly indicating a missing
m-dependent angular factor — which §2 supplies exactly.

## §2 — THE ENTRAINED DRIVE THROUGH O(ε²), ALL CLOSED FORM

Gradient/Hessian contraction of G(y) = y_x/|y|^{m+1} against the exact
retarded unit vector (2926 forms: û_x = −[μ(1+β²)+2β]/g,
(û·y)/r = −(1 − 2β²(1−μ²)/g), g = 1+2βμ+β², |û| = 1) gives, with
R_p = ∫r^{−p}dr:

    D(β; ε) = 2π [ R_m Φ(β) + ε R_{m+3} Ψ(β; m) + ε² R_{m+6} X(β; m) ]
              + O(ε³),

odd in β, Φ the 2926 base function, and — because the m-dependence
enters only through prefactors, five m-free angular integrals determine
everything — the exact series coefficients (Ψ = ψ₁β + ψ₃β³ + …,
X = χ₁β + χ₃β³ + …):

| coefficient | exact value |
|---|---|
| ψ₁(m) | −8(2m+1)/3 |
| ψ₃(m) | −8(4m+1)/3 |
| χ₁(m) | −4(m+1)(3m+2)/3 |
| χ₂ₙ even | 0 (odd function, verified) |
| χ₃(m) | −4(m+1)(113m+22)/15 |

Consequences:

1. **Slope at the origin:** dc/dε|₀ = −(2/5)(11m+3)·R_{m+3}/R_m
   (= −10 R′/R at m = 2).
2. **The cancellation condition:** ε\* is the smallest positive root of
   **R_m φ₃ + ε R_{m+3} ψ₃(m) + ε² R_{m+6} χ₃(m) = 0**, φ₃ = 8/15.
   ε\* is a **joint property of the kinematics and of where the Sea's
   response lives** — the 2900 "physically modest ~6% dial" is
   r-range-contingent, full stop.
3. **Effective expansion parameter:** ε·|χ₃R_{m+6}/(ψ₃R_{m+3})| ~
   ε/r³_min — which is why ε\* = 0.446 at r_min = 2 is *more*
   perturbative than ε\* = 0.171 at r_min = 1 (the inversion that
   drove §4's diagnosis).

Coefficient derivations validated **three independent ways, exact
agreement**: (i) sympy autodiff of the full integrand at m ∈ {1,2,3,4}
(in-session); (ii) quadratic-in-m reconstruction from m ∈ {1,2,3}
verified at the held-out m = 4; (iii) the Hessian-contraction
decomposition with symbolic m (the committed script's route), plus
finite-difference checks (a)/(a2) against the numeric integral.

## §3 — CHECK LEDGER

**(a) O(ε) identity — PASS.** Central FD of dD/dε at ε = 0 vs
2πR₅Ψ(β; 2): the deviation equals the discrete R₅ radial-sum offset
(+4.681e-2 at 480 points) to < 2×10⁻⁴ at every β.

**(a2) O(ε²) identity — PASS.** Second central difference vs
2πR₈X(β; 2): deviation equals the discrete R₈ offset. Order ε²
validated independently of the symbolic route.

**(b) ε\* prediction — FAILED as pre-registered, then attributed (§4).**

**(c) k drift — PASS.** k(0)×(discrete-R₂ factor) = −15.554, the 2900
value to five digits; k(ε\*) to O(ε²) = −16.9 vs 2900's −16.96 (0.3%).

## §4 — THE FAILED BAND AND ITS PRE-REGISTERED RESOLUTION

The O(ε²)-truncated continuum ε\* missed the pre-registered 5% band on
three small-ε\* configs (6–10% low), while the declared
"expected-failure" config (2, [2, 12]) at ε\* = 0.446 agreed *best*
(0.959) — the failure pattern pointed **away** from the pre-registered
O(ε³) explanation (that error would grow with ε\*, not shrink). The
suspect became quadrature: the measured ε\* were bisected on the
discrete 480×720 integral, whose three radial weights carry *different*
offsets (R̂₂: +1.27%, R̂₅: +4.68%, R̂₈: larger; worst at small r_min).
Pre-registered attribution tests:

1. **Discrete radial sums in the analytic quadratic:** gap closes to
   1.5–3.2% on five configs (m = 1 remains 9.7%).
2. **Grid refinement:** measured ε\*(2, [1, 12]) rises monotonically
   0.05893 → 0.05991 → 0.06042 toward the continuum root 0.06283
   (Richardson ≈ 0.061; the remaining ~3% is the O(ε³) deficit, correct
   sign: c(ε) superlinear ⟹ true root below the quadratic-truncated
   one).
3. **Residual ordering:** the residuals order exactly by the next-term
   parameter ε\*·|χ₃R_{m+6}/(ψ₃R_{m+3})|: 0.46 → 9.7%, ~0.28 → ~3%
   (three statistical ties), 0.26 → 2.7%, 0.21 → 1.5% — including the
   r_min inversion.

**Verdict: every residual is accounted for by identified causes
(discrete radial sums + O(ε³)) with the right sign, the right ordering,
and the right inversion.** Nothing in the data resists the closed-form
theory.

## §5 — WHAT THIS MEANS FOR THE ARC, AND WHAT IT DOES NOT

**It means:** the cancellation Newton I needs from direction (A) is a
**structure-tuned condition**, not a kinematic accident — the equation
in §2.2 couples the exact kinematic rationals to the radial profile of
the Sea's response. "The substrate has a ~6% entrainment dial" is not a
meaningful sentence; the meaningful question, now posed against exact
machinery, is the fixed-point one: **does the substrate's own
self-consistent response solve the cancellation condition — and at all
β-orders (the c₄ story of 2900 §2), which one dial cannot?** The 2900
registered prediction (c₄ → 0 under full self-consistency) now has an
exact target stack to be tested against.

**It does NOT mean:** Newton I is recovered or refuted; nothing here
touches the β⁰ core, anti-screening, or the statics suspension; the
one-shot entrainment model remains a model — its self-consistent
completion is future work. Ledger untouched. No frontier items opened
or closed; completion note recorded in `frontier_sectors/EW.md`
(sketch-tier per arc precedent, per the 2926 PD-006 scope ruling).

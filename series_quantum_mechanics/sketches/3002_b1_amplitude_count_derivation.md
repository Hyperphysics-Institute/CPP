# OPEN-QMRG-B1 DERIVATION CANDIDATE — THE AMPLITUDE–COUNT BRIDGE FROM ELASTIC ENERGY BALANCE

**Patch 3002 (4 Aug 2026).** Closes OPEN-QMRG-B1 (registered CONV-014
adjudication E-3) at derivation grade, PANEL-PENDING. Verify script:
`series_quantum_mechanics/code/3002_b1_energy_balance_check.py` —
EXECUTED this patch, ALL ASSERTIONS PASS, stdout in §5.

**The obligation (E-3):** derive B-QMRG-1 — |SSV_net,⊥|² ∝ ρ — from
substrate dynamics, independently of QM-1's unitarity Proposition and
QM-5's mode quantization (mutual-support prohibition: neither may be
cited as support). Mandatory before any grade elevation of the
unitarity Proposition or the Born-rule reconciliation.

---

## §1 — The fork, faced first

The messenger's NAME — Displacement Increment — suggests a rival
scaling. Two microphysical readings of "N messengers maintain the
register":

- **Reading L (amplitude-like):** each messenger deposits a fixed
  displacement increment, coherently aligned ⇒ sustained |S| ∝ N ⇒
  |S|² ∝ N².
- **Reading I (intensity-like):** each messenger transfers a fixed
  energy quantum; the medium's elasticity converts maintained energy
  to displacement quadratically ⇒ |S|² ∝ N.

**AP-2 decides the fork.** The ratified founder ruling P-2 (Patch
2989) states the count is "intensity-like, NOT amplitude-like."
Reading L makes the count amplitude-like — it contradicts the
ratified ontology. Reading I is the unique AP-2-consistent reading.
The name "Displacement Increment" correctly describes the microscopic
delivery event; the SUSTAINED register's scaling passes through the
elastic medium, and stiffness is where the square root comes from.
(The verify script confirms the fork is physically real: the rival
scaling is reproducible, but only by phase-locking every kick to one
quadrature — §5(b) — which additionally conflicts with P-3's reading
of synchrony as temporal cycle-structure, not quadrature alignment.)

## §2 — The derivation (three named inputs, all ratified or Tier-1)

**Input I-1 (Sea elasticity; SF-6 Tier 1/2).** Small polarization
displacements of the eDP Sea store energy quadratically:
u = ½κ|S_⊥|², with κ the same dipole stiffness that sets μ₀ and ε₀
(SF-6's "one eDP stiffness" locking E and B). The harmonic regime is
the weak-field regime B-QMRG-1 was already registered for. Writing
the medium's inertial density μ and ω² = κ/μ gives the canonical
oscillator form.

**Input I-2 (per-Moment turnover; A3′, ratified).** The GP resets its
registers each Moment from newly arriving Perceive-stage data. The
sustained register is therefore a driven-damped steady state: the
per-Moment refresh is the turnover (damping) against which the
arriving flux maintains the pattern.

**Input I-3 (energy quantum per messenger; corpus).** Each DI-bit is
the "fundamental quantum of information/energy transfer" (registered
acronym definition), and the mode's quantum is ħω under the Tier-1
identification E = ħν_C. A messenger maintaining a mode of rotation
rate ω transfers ε = ħω.

**Balance.** In steady state, per Moment: energy in = energy turned
over. With N messengers per unit time each delivering ħω, and the
elastic storage u = ½κ|S_⊥|² = ½μω²|S_⊥|²:

    N·ħω ∝ turnover rate × μω²|S_⊥|²
    ⇒  |S_⊥|² ∝ N·ħ/(μω)  ∝ ρ        (fixed mode; fixed medium)

**This is B-QMRG-1, with its constant.** Per count unit, the
sustained displacement-squared is ħ/(2μω) up to the O(1) turnover
factor — which is EXACTLY the canonical 1/(2ω) field normalization.

## §3 — The anti-circularity payoff

The CONV-014 concern (GPT/Gemini; Copilot's solo CIRCULAR) was that
the bridge smuggles the harmonic structure QM-5 presupposes. The
derivation above consumes: AP-2 (ratified), A3′ (ratified), SF-6
stiffness (Tier 1/2 corpus), E = ħν_C (Tier 1). It consumes NOTHING
from QM-5's quantization or QM-1's unitarity. Instead it OUTPUTS the
1/(2ω) per-quantum normalization that QM-5's field operator
(1/√(2ω_k) mode expansion) presupposes — the presupposition becomes a
prediction-match. The loop the panel feared (QM-5 ⇒ bridge ⇒ QM-1 ⇒
QM-5) is cut at its first link: the harmonic structure's origin is
the Sea's elasticity, registered in the EM sector two flagships ago.
GPT's mutual-support prohibition is honored and can now be DISCHARGED
at adjudication: the relation has an independent derivation, so
QM-1 and QM-5 no longer need each other for it.

## §4 — Robustness note (two mechanisms, one exponent)

The √N scaling arises twice over: (i) energetically, via elastic
storage of quantized flux (§2 — the load-bearing route); (ii)
statistically, since arrivals from a rotating pattern sample the ZBW
cycle (P-3 temporal synchrony), and the planar sum of N
cycle-distributed increments obeys ⟨|S|²⟩ ∝ N by the random-walk
theorem even without elasticity (verified §5(d)). The bridge does not
depend on an assumed coherence structure; both the coherent-energetic
and the phase-distributed-statistical limits give the same exponent.

## §5 — Verify stdout (EXECUTED, Patch 3002)

```
--- (a) BRIDGE: cycle-distributed kicks, <S^2> vs N ---
 cycle-distributed: values=['9.117e-04', '4.297e-03', '1.519e-02', '6.464e-02']  log-log slope = 1.01
 PASS: <S^2> proportional to N — the intensity-like (AP-2) scaling

--- (b) NEGATIVE CONTROL: phase-locked kicks, <S^2> vs N ---
 phase-locked: values=['3.384e-02', '5.152e-01', '8.216e+00', '1.331e+02']  log-log slope = 1.99
 PASS: the rival amplitude-like reading requires quadrature phase-locking — slope 2, contradicting AP-2's intensity clause

--- (c) MODE NORMALIZATION: eps = hbar*omega per kick, <S^2> vs omega at fixed N ---
 omega-scan: values=['6.196e+02', '2.731e+02', '1.705e+02', '7.722e+01']  log-log slope = -0.97
 PASS: per-quantum displacement^2 ~ hbar/(mu omega) — the canonical 1/(2 omega) normalization RECOVERED as output

--- (d) ROBUSTNESS: elasticity-free planar random-walk sum ---
 random-walk: values=['9.642e+00', '1.015e+02', '1.009e+03', '9.666e+03']  log-log slope = 1.00
 PASS: the statistical route gives the same exponent — two mechanisms, one scaling

ALL ASSERTIONS PASS
```

## §6 — Status, honest limits, registrations

**OPEN-QMRG-B1 status: DERIVATION CANDIDATE, PANEL-PENDING.**
Proved vs inherited:
- The quadratic-vs-linear fork resolution is forced by ratified AP-2
  (theorem-adjacent: the rival reading contradicts a ratified
  clause).
- The balance argument is elementary given I-1..I-3; its named
  inherited inputs are all ratified or Tier-1 corpus content.
- The toy model demonstrates the scalings but is a TOY: one elastic
  element, Poisson kicks, linear damping standing in for the
  per-Moment turnover. A lattice-level derivation (the full
  neighbor-coupled elastic Sea) is the hardening path; the O(1)
  turnover factor is not computed.
- The (c) normalization match to QM-5 is a consistency OUTPUT, cited
  as such and not as support (mutual-support prohibition honored).

**Enactment this patch:** QM-1 → v2.3 (Grade remark: OPEN-QMRG-B1
entry → derivation candidate, panel-pending; the mutual-support
prohibition noted as dischargeable at adjudication). Bar scope (E-1)
UNCHANGED. **Both CONV-014 blocking items (R-4, B1) are now closure/
derivation candidates — the arc is ready for its second review round
(CONV-015), with TWO verify scripts and SCRIPT-EXECUTED credit
available.**

**Ledger:** DM untouched; `data/kmem2` absent. QM: OPEN-QMRG-B1 →
DERIVATION CANDIDATE; R-4 CLOSURE CANDIDATE (3001); OPEN-QMRG-UNIQ
remains open (not blocking under the E-1 scope; a candidate CONV-015
question). Nothing minted; bar PARTIAL unchanged.

# OPEN-QMRG-R4-MULTILINK RESOLUTION CANDIDATE — THE COMMITTED REFRESH LAW FORCES THE SINGLE-EDGE CLASS

**Patch 3005 (4 Aug 2026).** Resolves OPEN-QMRG-R4-MULTILINK
(registered CONV-015 adjudication E-2; conditionality trigger T1) at
registry-theorem grade with a verified quantitative moat,
PANEL-PENDING. Verify script:
`series_quantum_mechanics/code/3005_multilink_pair_kernel_check.py`
— EXECUTED this patch, ALL ASSERTIONS PASS, stdout in §5. The script
contains an unprinted RNG-stream sentinel per the Patch-3004
KEY-DESIGN RULE, available for the next round's withheld key.

**The obligation (GPT's charter, E-2):** determine whether the
committed substrate refresh permits multi-edge-correlated terms; if
so, prove plane preservation or bound the leakage.

---

## §1 — The answer: it does not permit them, by three ratified clauses

The question is answered by the registry before any computation. The
committed refresh law is fixed by ratified text, each clause
independently load-bearing for the exclusion:

**Clause 1 — additive register formation (A3′ / the registered
definition).** The canonical glossary text (ratified per AP-3,
founder text 2958 V-2): *"the GP computes, holds, and per-Moment
refreshes SSV_abs and SSV_net from Perceive-stage arrivals"*, with
SSV_net defined throughout the registry as *"the vector sum of all
SSV contributions at a Grid Point."* A SUM is additive in per-arrival
contributions by definition: the register-formation step contains no
cross-terms between arrivals. A multi-edge-correlated kernel — one
whose contribution from edge b depends jointly on edge a's arrival —
is not a permitted reading of "vector sum"; it is a different law.

**Clause 2 — minimal messenger content (AP-2, ratified P-1).** DI-bit
content = {charge, type, origin address}; nothing else. A single
arrival therefore carries exactly one direction datum (its edge
vector, via the origin address) and no information about any other
edge's traffic. The per-arrival deposited contribution is a function
of one arrival's data — the single-edge class — because the data for
anything richer is not on the messenger.

**Clause 3 — per-Moment reset (A3′).** *"The GP resets its SSV values
each Moment from the newly arriving Perceive-stage data."* The
register is rebuilt from arrivals, not from a joint function of
arrivals with retained state; the reset closes the remaining route by
which arrival-arrival correlation could enter through the receiver's
memory within a Moment.

**Consequence (the exclusion theorem, registry grade).** Under the
committed law, the per-Moment refresh kernel is a sum over edges of
per-edge maps built from {charge, type, edge vector}: exactly the
single-edge class T(v) = αI + βvvᵀ (with per-edge scalar weights
permitted) that the 3001 lemma already covers. Introducing a
multi-edge-correlated term requires violating at least one ratified
clause — richer messenger content (against AP-2), non-additive
register formation (against the vector-sum definition), or
cross-arrival joint processing (against the reset clause). MULTILINK
is thereby resolved not by bounding a permitted channel but by
showing the channel is not in the committed law.

## §2 — The chirality question, faced honestly

The one place the corpus might have committed a cross-product rule is
its primitive chirality (n̂, Reading C; four of five manifestations
closed). Checked against the registry: the committed dynamical entry
point of chirality is **F.1 Mechanism A — a per-edge
propagation-rate asymmetry** δ(v·n̂) (F.1 Theorem 7.1: net DI-bit
current depends only on first-shell content at first order in δ).
A direction-dependent per-edge SCALAR rate is (a) single-edge and
(b) component-diagonal — Channel A of the 3001 taxonomy — and the
L-1 exactness argument is weight-independent: a scalar stencil cannot
mix vector components under ANY per-edge weighting, chiral or not.
**The committed chirality mechanism is plane-exact.** The E×B /
handedness manifestations are derived observable-level structures
(pattern-class irrep content), not register-formation rules; no
(v_a × v_b) Compute rule exists in the committed corpus.

## §3 — The quantitative moat (what WOULD happen in excluded or adjacent classes)

Three verified facts give the exclusion its force and its margin:

**M-1 (symmetric pair weights cannot source chirality).** For any
symmetric weight w(v_a·v_b), the shell's chiral sum
Σ_{a≠b} w(v_a·v_b)(v_a×v_b) vanishes IDENTICALLY (antisymmetry under
a↔b) — machine zero for w = 1, (v_a·v_b), (v_a·v_b)² (§5). Even a
hypothetical symmetric pair coupling produces no chiral vector.

**M-2 (separable pair kernels are safe).** If a future rule
introduced pair terms that FACTORIZE into single-vertex moment
factors: an isotropic factor (any moment of order ≤ 5, by the
5-design) is a multiple of I and cannot leak AT ALL — measured
machine-exact (2.1×10⁻¹⁶); a direction-coupled factor inherits the
single-edge suppression — measured slope 4.00 — because anisotropy
still requires an order-≥6 moment INSIDE one factor.

**M-3 (the excluded class is catastrophically leaky — which is the
point).** A non-separable asymmetric cross-product kernel (the class
Clauses 1–3 exclude) leaks the plane at ORDER UNITY: measured
out-of-plane fraction ≈ 0.70 at every wavelength tested, slope 0.00.
The excluded class is not merely "less suppressed" — it destroys the
U(1) reduction outright. This is why the registry exclusion, and not
a bound, is the correct closure shape: had the committed law
permitted this class, no wavelength suppression would have saved the
plane. The three ratified clauses are load-bearing, and the
demonstration quantifies exactly how much they bear.

## §4 — Status and honest limits

**OPEN-QMRG-R4-MULTILINK status: RESOLUTION CANDIDATE at
registry-theorem grade, PANEL-PENDING.** What is proved vs.
inherited:
- The exclusion (§1) is a theorem ABOUT THE COMMITTED LAW — its
  premises are the three ratified clauses, quoted from the registry.
  It does not claim no consistent ALTERNATIVE protocol could carry
  multi-edge terms; that would be a different substrate (and is
  exactly the F-AP3-1 elevation-falsifier territory already
  registered on AP-3).
- §2's chirality audit covers the COMMITTED mechanism (F.1
  Mechanism A); future chirality work introducing new dynamical
  entry points would re-open the audit (watch condition registered
  below).
- §3's moat covers factorizing pair kernels and the demonstrated
  excluded class; it is a margin analysis, not needed by §1.

**Watch condition W-MULTILINK-1 (registered):** any future patch
that (a) enriches DI-bit content beyond {charge, type, origin
address}, (b) amends the A3′ vector-sum or reset clauses, or (c)
introduces a dynamical chirality entry point other than per-edge
rate asymmetry, MUST re-run this analysis before the change ships.

**Enactment this patch:** QM-1 → v2.5 (Grade remark: MULTILINK →
resolution candidate, panel-pending). The E-1 widened bar scope and
the conditional note are UNCHANGED — trigger T1 moves only through
adjudication. T2 (OPEN-QMRG-B1-CONST) is the remaining trigger item.

## §5 — Verify stdout (EXECUTED, Patch 3005)

```
--- (1) CROSS-SUM: symmetric-weight chiral sums vanish identically ---
 w=1: |sum_(a!=b) w (va x vb)| = 1.755e-16
 w=(va.vb): |sum_(a!=b) w (va x vb)| = 1.010e-16
 w=(va.vb)^2: |sum_(a!=b) w (va x vb)| = 9.539e-17
 PASS: symmetric pair weights cannot source a chiral vector on the shell

--- (2a) SEPARABLE-PAIR, isotropic coupling factor: EXACT preservation ---
 M2 x scalar-stencil: max out-of-plane fraction at ks=0.3 = 2.106e-16
 PASS: an isotropic (order<=5 moment) coupling factor cannot leak AT ALL —
       exact, stronger than suppression; the design makes the factor a multiple of I

--- (2b) SEPARABLE-PAIR, direction-coupled deposit: inherits the (ks)^4 class ---
 separable (M2 x beta-stencil): out-of-plane fraction ['1.557e-05', '1.893e-07', '1.530e-09', '1.889e-11']; slope = 4.00
 PASS: separable pair kernels inherit the single-edge suppression —
       anisotropy still needs an order>=6 moment INSIDE one factor

--- (3) NON-SEPARABLE CHIRAL control: the excluded class leaks at low order ---
 non-separable chiral (excluded class): out-of-plane fraction ['7.047e-01', '7.004e-01', '7.000e-01', '6.999e-01']; slope = 0.00
 PASS: the excluded non-separable cross-product class is genuinely dangerous —
       the registry exclusion (A3' additivity + AP-2 minimality) is load-bearing

ALL ASSERTIONS PASS
```

**Ledger:** DM untouched; `data/kmem2` absent. QM: MULTILINK →
RESOLUTION CANDIDATE (panel-pending); B1-CONST remains open (T2,
next); bar scope unchanged; sector CONDITIONAL; nothing minted.

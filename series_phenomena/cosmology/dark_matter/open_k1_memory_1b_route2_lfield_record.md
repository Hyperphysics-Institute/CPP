# OPEN-K1-MEMORY-1B — ROUTE 2, STEP 2: L_field FOR THE BONDED SEA

**Patch 2855. Filed 2026-07-28 against the 2853 next-step
specification: *"compute L_field for the bonded dilute Sea — the
correlation length of the residual field after each pair's own partner
is subtracted. Analytic; no arc-inertia specification needed."***

**VERDICT: ROUTE 2 FAILS.** The pair-centre drift ratio at committed
Sea parameters is **0.711 (RMS)**, against an operative bar of 0.15 —
**4.74× the bar**. It is saturated at its statistically-independent
ceiling 1/√2 = 0.7071 to within 0.5%. **1B does not close by this
route.** Per the 2851 SS4 structural finding, PR7 now joins
PR4-COMPLETED behind the same wall.

Verify script: `code/2855_route2_lfield.py`. Reasoning:
`reasoning/2855.md`. No arc-inertia (C23/C24) input was used.

---

## §1 — The premise did not survive contact with the committed numbers

Route 2 rests on the 2853 result that a bonded pair's centre does not
move on a *uniform* field (C19/C20: opposite polarities, equal and
opposite displacements), so centre motion is **gradient**-driven:

> v_centre / v_CP ~ d_DP / L_field

**This is a suppression only if d_DP ≪ L_field.** Step 2 was chartered
to compute L_field. The committed parameters answer the question before
any simulation runs (`alpha1_s1_s2_record.md` §3, verbatim 21 July 2026
run; `alpha1_s4n_record.md`):

| quantity | committed value |
|---|---|
| DP bond length d_DP | **0.3640220 fm** |
| mean inter-pair spacing n_DP^(−1/3) | **0.3243 fm** |
| Debye screening length 1/κ_D | **0.1820 fm** (= d_DP/2) |
| κ·d_DP | **2.0000** exactly |
| Wigner–Seitz radius R_ws | 0.2012 fm |

**Both candidate correlation lengths are smaller than d_DP.** The
pair's own two CPs are farther apart than the distance to the
neighbouring pair, and farther apart than the distance over which the
Sea screens. The gradient expansion is not merely weak here — it is
inverted.

**The word "dilute" carried the error.** C26 rules the Sea to be
"DEDICATED, SEMI-PERSISTENT DP bonds… NOT a plasma gas of independent
± species." That is a **statement about bonding, not about geometry.**
The handover's phrase "the bonded dilute Sea" invites reading it as
geometric diluteness, which is what Route 2's suppression requires and
which the committed numbers deny. **κ·d_DP = 2.0 is the operating point
the programme has carried since the α1 arc; it says directly that the
bond length is two screening lengths.**

## §2 — L_field is regulator-sensitive and is therefore discarded

Computed as the 1/e crossing of the E²-weighted autocorrelation of the
residual field, across the **committed S4-N soft-core axis** (0.02,
0.04, 0.08 fm — reused precisely so the regulator is not a free
parameter chosen by this calculation):

| a_soft (fm) | L_field (fm) | d_DP/L_field | R_drift (RMS) |
|---|---|---|---|
| 0.020 | 0.0594 | 6.125 | **0.7099** |
| 0.040 | 0.1025 | 3.550 | **0.7132** |
| 0.080 | 0.1516 | 2.401 | **0.7163** |

**L_field varies by 2.6× across the axis. R_drift varies by 0.9%.**

L_field is dominated by close encounters, which is exactly where the
soft-core regulator lives, so it is not a well-conditioned quantity in
this Sea. **The proxy is discarded and the target computed directly.**
This is reported because the charter asked for L_field specifically: it
was the right question to ask of a dilute Sea and the wrong question to
ask of this one.

## §3 — The drift ratio, computed directly

Under C19/C20/C25 each CP displaces along its own perceived SSV_net
with polarity sign, so

> v_centre ∝ ½|**E**(+) − **E**(−)| , v_CP ∝ E_rms
> **R_drift ≡ |E(+) − E(−)| / (2·E_rms)**

and by C20, v_CP/c = |SSV_net|/SSV_abs ≤ 1, so **v_centre/c ≤ R_drift**
unconditionally. Screened Coulomb fields, pairs placed at the committed
density with random centres and orientations, probe pair's own partner
excluded by construction.

**Result: R_drift = 0.7108 (RMS), 0.7154 (median).**

The analytic ceiling for **statistically independent** E(+) and E(−) is
1/√2 = 0.70711. The measured value is **1.0052× that ceiling** — the
two CPs of a bonded pair sample effectively **independent** residual
environments. **The C19/C20 polarity cancellation that Route 2 was
built on provides no suppression whatsoever at committed parameters.**

## §4 — Dilution scan: how dilute would it have to be?

Diluting self-consistently (κ_D² = 4πn_CP q²/θ ⇒ κ ∝ √n; d_DP held
fixed, being a bond length not a density scale):

| n/n_ref | spacing (fm) | 1/κ (fm) | R_drift RMS | median | ≤ 0.15? |
|---|---|---|---|---|---|
| 1 | 0.324 | 0.182 | 0.7110 | 0.7058 | no |
| 0.1 | 0.699 | 0.576 | 0.6478 | 0.6498 | no |
| 0.01 | 1.505 | 1.820 | 0.4793 | 0.4289 | no |
| 0.001 | 3.243 | 5.756 | 0.2940 | 0.2170 | no |
| 0.0003 | 4.845 | 10.508 | 0.2195 | 0.1522 | no |

**Even at 3×10⁻⁴ of the committed density the RMS bar still fails.**
The decline is slow because the RMS is tail-dominated by close
encounters. No physically defensible dilution rescues the route.

## §5 — The one escape hatch, and why it is closed

The model places pairs at **random**. A strongly structured (liquid-
ordered) Sea could correlate E(+) with E(−) and reduce R_drift below
the independent ceiling.

**This is closed by a committed number.** The Sea's coupling parameter
is **Γ = 1/(√2π) = 0.2251** (`alpha1_s1_s2_record.md`, charge-
independent geometric identity Γ = κ³/4πn_CP). Γ ≪ 1 is the weakly
coupled regime — random placement is the appropriate model, and
structural corrections are O(Γ) ≈ 22%. S4-N's direct Metropolis
simulation independently confirms weak structure: monotonic screening,
κ_fit = 1.017 κ_D. **An O(Γ) correction cannot carry 0.711 to 0.15;
it would need a factor of 4.7.**

## §6 — What this does and does not do

**Does:** close Route 2 negative. Establish that the pair centre is not
protected. Confirm the 2851 SS4 reading — PR4-COMPLETED,
OPEN-C23-TRANSVERSE-VALIDATION, and 1B are **one obstacle wearing three
names**, and that obstacle is the C23/C24 arc-inertia specification.

**Does not:** touch Candidate B's 79.5%. Move PR1, PR2, PR3, PR5 or
PR6, all of which remain MET. Falsify C23, C26, or the bonded-Sea
picture — the Sea is exactly what C26 says it is; it is simply not
*geometrically* dilute. Bear on the banked findings (emergent Coulomb,
the measured ZBW Sea, the magnetic curl).

**PR ledger unchanged at SIX OF SEVEN. PR7 remains PARTIAL. B7 holds.**

## §7 — Worker self-check (the failure mode named three times)

The registered failure mode is converting "the parameter that controls
X" into "the value of X" **when the conversion is flattering**. This
result is unflattering, so the live risk is its mirror: over-claiming a
negative to display rigour.

Guards applied. Every input is a committed number with a cited patch;
none was chosen by this calculation, including the soft-core axis. The
one quantity the charter actually named (L_field) is reported as
**regulator-sensitive and unusable** rather than quoted at a
convenient value — had I wanted the negative cheaply, a_soft = 0.02
gives d_DP/L = 6.1 and I would have stopped there. The escape hatch of
§5 was constructed *for* the opposing case and closed on a committed
number rather than on assertion. The result rests on R_drift, which is
regulator-independent across the full committed axis and lands on an
**analytic** ceiling (1/√2) that is derivable without simulation.

**Challenge key set under the 2837 withheld-key protocol, deliberately
uncomputed by the worker:** the number of distinct values of
d_DP·n^(1/3) in the §4 scan table that exceed 1, computed from the
committed n_ref and the scan's own dilution factors.

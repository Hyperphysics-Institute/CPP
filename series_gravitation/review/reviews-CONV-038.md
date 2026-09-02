# CONV-038 — Returns receiver: the retired Exclusion Rule, the re-derived PSR floor (3367), and the SR-1 register cap

**Dispatched:** Patch 3368, 2 Sep 2026 (Session 161).
**Package:** `conv038_retired_rule_floor_rederived_review_package_v1.0.md`
(CONV-001 single block; founder ruling file, tombstone row, 3367 record,
verify script, SR-1 App. A.5 excerpt, GR-1b excerpt all inlined; the
3367 `.py` ships separately for own-run).

**What this round gates:** the standing of the PSR floor `l_P/2` — the
number under the Planck core, |R| = 1, the Buchdahl relocation, the Kerr
surface, the wall modes, GR-2 V1.6 and PRED-O-39 — after its only
derivation (GR-1c Thm 2, from the CP Exclusion Rule) was voided by founder
ruling R-EXCL-RETIRED. Route A (3367) re-derives it from Buchdahl +
incompressibility + the exact exterior, conditional on RCORE-4. Also under
review: **SR-1's own register cap `SSV_crit = E_P/l_P³`, which in the `u`
variable gives `u_max = α ≈ 0.56/0.24` or a collapse to PSR → 0 — not
obviously `u = 1`** (package §2.4, Q5); the mirror under a one-Moment-delay
compliant wall (Q4); the corrigenda scope (Q6).

**Binding rules:** majority per question; majority UNSOUND on Q2 leaves the
floor ORPHANED with a banner on the arc; majority CONTRADICTION on Q5
escalates to the founder and BLOCKS Q8b; majority YES on Q4(iii) obliges the
PRED-O-39/GR-2 caveat; Q7 items adopted regardless.

**Seat mandates riding:** IDENTITY, OWN-RUN (3367, seconds), COUNT-LINE
(`3367 verify: 25 passed, 0 failed`), **EK-1 sealed execution key (first
GR-lane use; SHA-256 in package §6)**, inline returns. Steers: Q5 (GPT),
T-1 (Grok), T-2/T-3 (Gemini), Q1/T-6 (Copilot), T-5/Q4 (DeepSeek).

**Returns: 4/5 distinct (Seat 2 EMPTY-AT-PASTE — the slot carried a duplicate of Seat 1; amendable on receipt). Adjudicated Patch 3369, 2 Sep 2026: `conv038_adjudication.md`.**

---

## Seat 1 — GPT (self-labelled GPT-5.6) — EK-1 HASH-MATCH (execution-verified)

```
REVIEWER: GPT-5.6
TIER LEGEND USED: T1 = independently computed or algebraically verified; T2 = premise-chain and internal-consistency audit; T3 = substrate-level physical interpretation requiring an additional founder rule or derivation

Q1: ESTABLISHED-WITH-GAPS [T2/T3] — The founder's explicit retirement ruling, absence from the registries, nonexistent cited source, and identification of the live GR invocations establish that the Exclusion Rule is void. The tombstone is adequate for the known GR sites. Gap: the claimed corpus-wide scope has not been established by a dependency audit; identity conservation, early-universe expansion, and any indirect descendants of the rule need named replacement mechanisms or orphan labels.

Q2: UNSOUND [T1/T2/T3] — The quadratic and branch algebra are sound: Buchdahl implies u ≤ 1 on the exterior branch. It does not imply u_max = 1. P4 supplies equality by assertion; a register saturating at u = 0.9 violates no stated premise. More seriously, P2 identifies a saturated incompressible interior with spatially constant u, while P1 uses u as the Schwarzschild metric/register variable. A positive-density Einstein interior does not have a constant gravitational potential or constant lapse. If u is instead a microscopic variable decoupled from the interior metric, the exterior u-to-PSR dictionary cannot be carried through the interior without another bridge. Thus P2–P3 are either inconsistent or equivocal. This is not circular reasoning, but inversion plus an unproved extremality premise does not constitute a derivation.

Q3: OVER-SCOPED [T2/T3] — "Conditional on RCORE-4" acknowledges the field-equation problem but not the independent P4 debt or the ambiguity between constant density and constant register. The earned result is a conditional upper bound u_surface ≤ 1, hence a conditional lower bound PSR ≥ l_P/2, not a derived attained floor PSR = l_P/2.

Q4: (i) SURVIVES-WITH-CAVEATS; (ii) DOES-NOT-SURVIVE; (iii) YES [T2/T3] — If the one-Moment response is lossless and has no other outgoing channels, unit total reflection is plausible. "No storage across Moments" alone does not exclude temporary absorption, mode conversion, transmission into substrate degrees of freedom, or secular work, so |R| = 1 remains conditional. A delayed compliant response does not impose a Dirichlet node and does not fix phase π; it generally produces a frequency-dependent complex impedance and phase. PRED-O-39 and GR-2 must therefore state that 191 Hz is conditional on X = 0 and carries an uncomputed boundary-phase shift.

Q5: UNDERDETERMINED [T1/T2/T3] — Setting α ≡ 1 is a rescue by redefinition, not a triangulating derivation. A physical dimensionless prediction such as PSR/l_P cannot be changed by choosing unit-circumradius rather than unit-insphere conventions. Absorbing α into SSV_crit is permissible only if "one Planck energy per physical cell" was never an independently fixed cap; doing so changes that claim rather than proving agreement with it. The record also fails to determine whether SR-1's Padé finite floor or its r_eff → 0 collapse statement is live. Resolution requires: (1) an invariant physical definition of cell volume and SSV_crit; (2) a derived mapping from stored energy or stress to u; and (3) an explicit ruling or derivation selecting the Padé limit, zero-radius collapse, or another saturation law. Until then, the candidate floors disagree and none may be silently normalised into another.

Q6: OVERCLAIMS [T2/T3] — The retirement notes are broadly faithful, but the GR-1c corrigendum turns u ≤ 1 into u_max = 1 without naming P4 as an additional assumption and presents l_P/2 as re-derived. It also describes incompressibility as "SSV_abs register at its maximum," conflating constant density with constant u. The text must say that Buchdahl establishes the conditional bound PSR ≥ l_P/2; attainment of l_P/2 is an extremality assumption pending derivation. The SR-1 cap conflict must remain prominently unresolved.

Q7: ITEMS-FOUND [T2/T3] —
1. "Buchdahl and extremality give u_max = 1" is narrower computationally than stated: Buchdahl gives only u ≤ 1; equality comes solely from P4.
2. "The saturated interior holds u = u_max throughout; density non-increasing outward" treats constant u as equivalent to incompressibility, which is not true for a GR uniform-density interior.
3. "The packing premise is excluded by P1–P3" is too strong if P2–P3 are inconsistent or if the exterior dictionary does not apply inside saturation.
4. "The physical normalisation … is α = 1" is not established by unit freedom; it changes the physical cap unless SSV_crit was conventional from the start.
5. "No headroom" does not universally imply |R| = 1 in the elastic gravitational channel; it does not exclude mode conversion or delayed energy exchange.
6. "One-Moment-delay compliant surface" does not make X = 0 its node limit without a derived impedance or zero-compliance limit.
7. "No other invocation found" does not establish that the retired rule has no indirect descendants outside the GR lane.
8. "The value l_P/2 recovered" exceeds the demonstrated result, which is a conditional bound plus an asserted saturation choice.

Q8a: IMPROPER  Q8b: BLOCK [T2/T3] — The retirement correction should proceed, and the Buchdahl algebra is useful, but the package does not supply a sound replacement derivation of the attained floor. Route A proves a conditional bound, not saturation at equality; the interior premise is unresolved; SR-1 contains incompatible cap descriptions; and the mirror phase underlying the registered spectrum is uncomputed. The R-core arc should carry "floor undetermined; Buchdahl conditional bound PSR ≥ l_P/2" until these issues clear.

SCRIPT: INDEPENDENT-HARNESS — independently evaluated the uniform-density Schwarzschild central-pressure formula p_c/ρ = (1−sqrt(1−2M/R))/(3sqrt(1−2M/R)−1), the isotropic radius map R/μ = (1/u)(1+u/2)^2, the lapse, the Buchdahl polynomial roots {1,4}, and the exterior-branch inequality. The executable 3367 script was not included in the uploaded packet, so I do not claim its reference count line as an own run.

EK-1: pc=7.6533;R=2.3361;lapse=0.3793

DEFECTS/OBJECTIONS:
1. P2 conflates incompressible density with constant gravitational/register potential.
2. P2 and P3 appear incompatible if u retains its metric meaning inside the body.
3. P4 is an independent saturation axiom, not a consequence of Buchdahl or register consistency.
4. α ≡ 1 is not earned by normalisation and cannot reconcile physical dimensionless floors by itself.
5. SR-1 does not decide between its finite Padé floor and zero-radius collapse.
6. The one-Moment-delay wall does not derive either Dirichlet phase π or channel-specific |R| = 1.
7. Corrigenda must distinguish the valid conditional lower bound from the unproved attained floor.
```

## Seat 2 — Grok — EMPTY-AT-PASTE

*The founder's paste for this slot was byte-identical to Seat 1's return (REVIEWER: GPT-5.6). A stale/duplicate re-paste is a known class (Session 160 standing caution; CONV-037 twice). No Grok return has been received. Amendable on receipt per the 3506/3507 precedent; the adjudication below is on four seats and will be amended if a Grok return arrives.*

## Seat 3 — Gemini — EK-1 no match (graded INSPECTED)

```
REVIEWER: Gemini
TIER LEGEND USED: ESTABLISHED/ESTABLISHED-WITH-GAPS/NOT-ESTABLISHED; SOUND/SOUND-WITH-CAVEATS/UNSOUND; CORRECTLY-SCOPED/UNDER-SCOPED/OVER-SCOPED; SURVIVES/SURVIVES-WITH-CAVEATS/DOES-NOT-SURVIVE; YES/NO; CONSISTENT-BY-NORMALISATION/SR-1-SUPERSEDED/CONTRADICTION/UNDERDETERMINED; FAITHFUL-AT-GRADE/OVERCLAIMS/UNDERCLAIMS; NONE-FOUND/ITEMS-FOUND; PROPER/PROPER-WITH-REVISIONS/IMPROPER; CORRIGENDA-CLEAR/RESTATE-REQUIRED/BLOCK.
Q1: ESTABLISHED [ESTABLISHED] — The founder's ruling is clear, the rule is absent from axiom registry and cited source, and a tombstone is added. No gaps in the retirement record itself, though potential orphans outside GR (T-6) are noted but not a gap in the retirement.
Q2: SOUND-WITH-CAVEATS [SOUND-WITH-CAVEATS] — P1 is fenced, P2 is founder ruling, P3 is conditional on RCORE-4, P4 (extremality) is asserted without derivation (why u must be exactly 1, not just ≤1). The inversion is not circular (premises differ), but the extremality step is a caveat.
Q3: CORRECTLY-SCOPED — The derivation explicitly assumes Einstein's equations at saturation, which is exactly the open item RCORE-4. The conditional label is accurate.
Q4: (i) SURVIVES-WITH-CAVEATS; (ii) DOES-NOT-SURVIVE; (iii) YES [SURVIVES-WITH-CAVEATS] — The "no headroom" argument survives because the register is saturated, so |R|=1 is plausible but the exact boundary condition is yet to be computed (caveat). The phase π was based on a two-sided clamp and does not obviously survive in the one-Moment-delay picture. Therefore, PRED-O-39 must note that the Dirichlet condition (X=0) is an approximation with uncomputed boundary-phase correction.
Q5: UNDERDETERMINED [UNDERDETERMINED] — SR-1 contains two conflicting statements: the Padé form (with α≠1) gives a floor > l_P/2, and the collapse statement (r_eff→0) gives 0. Route A gives l_P/2. The worker's "α≡1 by normalisation" is a possible resolution but is not derived. The record does not decide which SR-1 expression is physical. To decide: a founder ruling on whether the collapse statement is live or dead, and on the physical meaning of α (whether it is a pure convention or has a fixed value).
Q6: FAITHFUL-AT-GRADE — The corrigenda accurately note the retirement, replace the derivation with Buchdahl (with conditionality), and flag the SR-1 issue and boundary-phase caveat where applicable. It does not overclaim or underclaim.
Q7: NONE-FOUND — No universals found where the computation is narrower than the sentence in 3367 or this package.
Q8a: PROPER-WITH-REVISIONS  Q8b: RESTATE-REQUIRED — The assembly is proper, with clear documentation of the retirement and new derivation. However, the SR-1 issue (Q5) is underdetermined, and the corrigenda should explicitly state that the relation between SSV_crit and u=1 is unresolved (pending founder ruling) rather than just "under CONV-038 Q5". Also, the boundary-phase caveat (Q4(iii)) must be added to PRED-O-39/GR-2 if not already included.
SCRIPT: INSPECTED (reference run) — The provided verification record states "3367 verify: 25 passed, 0 failed". The script was not executed by this seat due to environment constraints; the reference run is trusted.
EK-1: pc=7.6543;R=2.3361;lapse=0.3793
DEFECTS/OBJECTIONS:
1. The extremality step (P4) is not derived; it is asserted that the register must saturate at the maximum allowed by Buchdahl (u=1), but a reason is not given.
2. The SR-1 register cap is inconsistent with Route A unless a specific normalisation (α=1) is imposed, which is not justified in SR-1. The collapse statement in SR-1 (r_eff→0) contradicts the existence of a finite floor.
3. The boundary condition for the wall (mirror) under the new one-Moment-delay picture is not computed; the phase π is lost, so the Teukolsky solver's Dirichlet condition (X=0) is approximate and carries an unquantified error.
```

## Seat 4 — Copilot — EK-1 no match (graded INSPECTED)

```
REVIEWER: Copilot
TIER LEGEND USED: FAST; THEORETICAL-GRADE; ARCHIVAL-GRADE
Q1: ESTABLISHED-WITH-GAPS [FAST] — The founder's ruling and the tombstone establish that the CP Exclusion Rule was retired and that the PSR floor lost its original derivation; the package documents the retirement and the replacement derivation. Gaps: the archival provenance of the original rule is incomplete (no commit containing the rule found), and the retirement's cross-cutting scope outside the GR lane (SR, cosmology) is not exhaustively audited.
Q2: SOUND-WITH-CAVEATS [THEORETICAL-GRADE] — Route A's algebraic application of Buchdahl in the saturation variable u is correct given P1–P4. Caveats: P3 (Einstein FE consistency at saturation) is conditional and not proven in the package; P4 (taking u_max = 1) is a modelling/extremality choice rather than a derived stability theorem.
Q3: VALID-WITH-CAVEATS — The premises are internally consistent given their stated assumptions: incompressibility (P2) is plausible under the founder's saturation hypothesis but needs microphysical justification; the Buchdahl reduction to u^2−5u+4≥0 is algebraically correct for the stated interior solution; the extremality choice u_max = 1 is defensible on the exterior-branch argument but is not derived from a stability principle and therefore remains a modelling choice.
Q4: (i) SURVIVES-WITH-CAVEATS; (ii) DOES-NOT-SURVIVE; (iii) YES [THEORETICAL-GRADE] — (i) |R| = 1 plausibly survives under a one‑Moment, one‑sided delayed (compliant) wall because the founder's replacement mechanism forbids net storage across Moments; caveat: the substrate‑level derivation tying the superposition/displacement rule to an amplitude node is not shown. (ii) The π phase flip does not survive as a guaranteed consequence of a one‑sided delayed response; the two‑sided clamp argument that produced a π phase is not applicable. (iii) Therefore PRED‑O‑39 / GR‑2 V1.6 should carry a boundary‑phase caveat until the mirror‑phase provenance is derived.
Q5: UNDERDETERMINED [ARCHIVAL-GRADE] — The record does not decide. Route A yields u_max = 1 (PSR = l_P/2). SR‑1 presents a Padé working form that gives u_max = α_geom (≈ 0.5594 or 0.2444 depending on unit choice) and also contains a collapse reading (PSR → 0). Without an explicit canonical normalisation mapping SR‑1's α into the GR lane's unitless u, or an SR‑1 corrigendum that removes/explains the collapse reading, the two sources are not reconciled. What would decide it: (a) an explicit canonical normalisation statement fixing α (for example, define SSV_crit so that α ≡ 1), or (b) an SR‑1 corrigendum that removes or explains the collapse statement and selects the Padé physical branch.
Q6: FAITHFUL-AT-GRADE — The proposed corrigenda correctly document the retirement, replace the proof with the conditional Buchdahl derivation, and register open dependencies (FE‑1, wall derivation, SR‑1 mapping) without overclaiming; the text is appropriately cautious and records follow‑ups.
Q7: ITEMS-FOUND — 
- Normalization convention missing between SR‑1 and the GR lane (α mapping). 
- SR‑1 internal inconsistency: Padé finite‑PSR form vs collapse (PSR → 0) statement. 
- FE‑1 at saturation unresolved (Einstein equations inside saturated body not demonstrated). 
- Mirror/phase provenance missing: derivation from founder's replacement boundary picture not provided. 
- Retirement scope audit incomplete: potential orphaned invocations outside GR lane not exhaustively checked. 
- Naming sweep deferred: "clamped register" appears in many files but is semantically one‑sided; renaming/notes required.
Q8a: PROPER-WITH-REVISIONS  Q8b: RESTATE-REQUIRED — The package is coherently assembled and reproducible, but the SR‑1 vs Route A indeterminacy is material and requires a restatement that either fixes the normalisation convention linking SR‑1 and Route A or explicitly declares which SR‑1 reading is physical and why the collapse reading is superseded.
SCRIPT: INSPECTED (reference run) — 3367 verify: 25 passed, 0 failed
EK-1: pc=7.6512;R=2.3361;lapse=0.3793
DEFECTS/OBJECTIONS:
1. Normalization ambiguity (critical) — SR‑1's α_geom is unit‑dependent; the package lacks the canonical map between SR‑1 units and the GR lane's unitless u. This is the root cause of the apparent disagreement and must be resolved before a flagship PSR is enacted.
2. SR‑1 internal contradiction — SR‑1 contains both a Padé working form (finite PSR) and a collapse statement (PSR → 0). The corpus must reconcile or correct this; as written both claims coexist and are inconsistent.
3. FE‑1 conditionality not closed — Route A depends on Einstein FE holding inside the saturated interior; no proof or counter‑analysis is provided. Require either a derivation or a sensitivity analysis.
4. Extremality step is modelling, not theorem — choosing u_max = 1 is defensible but not derived from stability; recommend an explicit stability/variational argument or bound.
5. Mirror phase provenance missing — the one‑Moment replacement picture is asserted to yield a mirror but the phase argument is not derived; PRED‑O‑39 must carry a phase caveat until derived.
6. Archival gap for retired rule — the CP Exclusion Rule's retirement is recorded but the original rule's provenance is not archived; add an explicit archival note explaining removal and listing corrected citations.
7. Scope audit incomplete — the worker's grep found no other invocations, but absence of evidence is not proof; require a targeted sweep of SR and cosmology files for orphaned uses.
```

## Seat 5 — DeepSeek — EK-1 no match (graded INSPECTED)

```
REVIEWER: DeepSeek
TIER LEGEND USED: Standard vocabulary as defined in package §4.
Q1: ESTABLISHED — Founder ruling R-EXCL-RETIRED is explicit; tombstone in axiom-registry.md documents the retirement; no gaps in the record (L1–L5 are complete).
Q2: SOUND-WITH-CAVEATS — P1 (exterior) and P2 (incompressibility) are valid; P3 is conditional on RCORE-4; P4 (extremality) is asserted but not derived; the quadratic derivation is mathematically correct.
Q3: CORRECTLY-SCOPED — The label DERIVED-CONDITIONAL accurately reflects that the derivation depends on FE‑1 holding at saturation (RCORE‑4), which is the appropriate open item.
Q4: (i) SURVIVES; (ii) DOES-NOT-SURVIVE; (iii) YES — The "no storage" argument survives the register‑limit picture, so |R| = 1 holds. The phase π from a node condition is not guaranteed by a one‑Moment‑delay compliant boundary; thus a phase‑error caveat is required for PRED‑O‑39/GR‑2.
Q5: UNDERDETERMINED — The record does not decide whether the SR‑1 collapse statement (PSR → 0) or the Padé form (with α ≠ 1) is the correct physical picture at saturation. A founder ruling on which expression is physically correct at the cap, or a substrate‑internal derivation that yields u = 1, is required to resolve.
Q6: FAITHFUL-AT-GRADE — The corrigenda text accurately describes the retirement, the new derivation (Route A), its conditionality, and the open issue with SR‑1, without over‑ or under‑claiming.
Q7: NONE-FOUND — No universal statements exceeding the computational scope were identified in 3367 or this package.
Q8a: PROPER  Q8b: CORRIGENDA-CLEAR — The package is well‑assembled; the proposed corrigenda are clear and address all necessary changes.
SCRIPT: INSPECTED (reference run) — The provided script 3367_psr_floor_from_buchdahl_verify.py passes 25/25 checks as reported.
EK-1: pc=7.6522;R=2.3361;lapse=0.3793
DEFECTS/OBJECTIONS: NONE
```

---

## Adjudication

Patch 3369 — `conv038_adjudication.md`. Verify `code/3369_conv038_ek1_verify.py`.

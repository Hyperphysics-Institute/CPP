# CONV-038 — ADJUDICATION (Patch 3369, 2 Sep 2026, Session 161)

**Returns:** 4 of 5 distinct. Seat 1 GPT (self-labelled GPT-5.6), Seat 3 Gemini, Seat 4 Copilot, Seat 5 DeepSeek. **Seat 2 (Grok) EMPTY-AT-PASTE** — the slot carried a byte-duplicate of Seat 1; amendable on receipt (3506/3507 precedent).
**Verify:** `code/3369_conv038_ek1_verify.py` (24/24) — hashes, tallies and rule-triggers asserted in code.
**Method:** majority per question where one exists; **adjudication by argument, not vote count, where none does** (K1 precedent, DM lane 3506). Where the argument goes against the worker, it is enacted against the worker.

---

## §0 Execution verification — the key worked, and it changed the reading of two returns

First GR-lane use of the sealed execution key. **One seat of four hash-matched: GPT** (`pc=7.6533`). Gemini (7.6543), Copilot (7.6512) and DeepSeek (7.6522) all returned the closed-form `R` and lapse correctly and the central-pressure value wrong — every miss within 0.003 of the truth, none exact. That is the signature of a seat that estimated the number rather than computed it. All three are graded **INSPECTED**, as the package said they would be regardless of what the SCRIPT line claims.

Two consequences. GPT, the only execution-verified seat, wrote *"the executable 3367 script was not included in the uploaded packet, so I do not claim its reference count line as an own run"* — it declined credit it could have asserted, and then earned it on the key. DeepSeek's SCRIPT line — *"passes 25/25 checks as reported"* — is a reading claim; with DEFECTS: NONE and CORRIGENDA-CLEAR it is also the least-engaged return, and it is weighted accordingly below. The key is now GR-lane standard.

## §1 Rulings

### Q1 — Retirement record: **ESTABLISHED-WITH-GAPS** (2–2 by count; gaps adopted by argument)

Void status of the rule: unanimous. The gap named by GPT and Copilot is real: the retirement's *scope* outside GR has not been audited by dependency, only by grep. GR-1c says the rule was "established … for CP identity conservation"; GR-1b says it "drives the initial expansion." Something now does those jobs or the jobs are orphaned. Copilot adds that the original rule's provenance is unarchived — the founder says it once existed; no repository version ever held it; the pre-repository history should be noted as such in the tombstone. **Adopted:** a targeted dependency sweep of SR and cosmology (Q7 item); tombstone amended with the provenance note.

### Q2 — Route A: **SOUND-WITH-CAVEATS by count (3–1); by argument, the UNSOUND seat is right about what was proven, and the worker rules against himself**

The three SOUND-WITH-CAVEATS seats and the UNSOUND seat agree on every fact: the algebra is correct; Buchdahl gives `u ≤ 1`; equality comes only from P4, which is asserted. They differ on whether "correct algebra + asserted extremality" deserves the word SOUND. GPT's objection goes further and is the one that decides it: **P2 says the register `u` is constant through the saturated interior; P3 says Einstein's equations hold there; but a positive-density Einstein interior does not have a constant potential — the Schwarzschild interior's `u` would climb toward 2 at the centre.** So either `u` inside is not the metric variable of P1 (and then the exterior dictionary cannot be carried in without a bridge nobody has written), or P2 and P3 contradict each other. The worker noted this tension in `reasoning/3367.md` and labelled it "conditional on RCORE-4." GPT is right that it is not merely conditional; it is *equivocal* — two meanings of `u` are in play. The 3367 record §5 said "Establishes … the saturation value is forced to `u_max = 1`." That sentence overclaims.

**Ruling:** Route A establishes a **conditional BOUND**, `u_surface ≤ 1 ⇒ PSR_surface ≥ l_P/2`, conditional on (i) Einstein-consistency of the saturated interior (RCORE-4) and (ii) the exterior `u`↔metric dictionary extending to the surface from outside (which it does — the bound is evaluated *at* the surface, where P1 holds; the equivocation bites only if one tries to say what `u` does *inside*). Attainment `u = 1` is an **extremality assumption, not a derivation.** The 3367 standing is downgraded accordingly. This is the strictly-weaker restatement and folds at enactment.

### Q3 — Standing label: **OVER-SCOPED** (by argument; count 2–1–1 with one nonconforming vocabulary)

Follows from Q2. "DERIVED-CONDITIONAL (floor)" is replaced by **"CONDITIONAL BOUND `PSR ≥ l_P/2` (Buchdahl, on RCORE-4); attainment open (extremality unproved)."** Copilot's off-vocabulary "VALID-WITH-CAVEATS" is recorded as nonconforming and read as agreement that the label needed the P4 debt named.

### Q4 — The mirror under the founder's replacement wall

- **(i) |R| = 1: SURVIVES-WITH-CAVEATS (3–1).** The "no headroom" step survives R-FLOOR-REGISTER. GPT names what "no storage across Moments" does not exclude: mode conversion, transient absorption within a Moment, transfer into substrate degrees of freedom. |R| = 1 stands as the 3297 result *in the channel 3297 computed*, with those channels registered as uncomputed.
- **(ii) phase π: DOES-NOT-SURVIVE (4–0).** Unanimous and correct. A one-sided, one-Moment-delay compliant response is a frequency-dependent impedance, not a node. The Dirichlet `X = 0` used by the Teukolsky ladder is the zero-compliance *limit* of that surface, and nothing in the corpus shows the limit is reached.
- **(iii) caveat obliged: YES (4–0) — BINDING.** PRED-O-39 and GR-2 carry, at the next version, the clause drafted in package §5, amended per GPT: *"conditional on the Dirichlet wall condition X = 0, the zero-compliance limit of a one-Moment-delay surface; the boundary-phase shift is uncomputed and the 188–194 Hz band does not include it."*

### Q5 — SR-1's cap vs Route A: **UNDERDETERMINED (4–0)**

No seat took the worker's rescue. GPT's argument is decisive and is adopted as the ruling's reasoning: **a dimensionless physical prediction, `PSR_floor/l_P`, cannot depend on whether one works in unit-circumradius or unit-insphere coordinates. Therefore "set α ≡ 1" is not a normalisation choice — it changes the physical cap.** It is permissible only if SR-1's "one Planck energy per physical cell" was never an independently fixed physical statement, and SR-1 presents it as exactly that ("purely geometric … no phenomenological fitting"). All four seats name the same deciders: (1) an invariant physical definition of the cell volume and hence of `SSV_crit`; (2) a derived map from stored energy/stress to the GR lane's `u`; (3) a ruling on whether SR-1's `r_eff → 0` collapse statement is live or superseded by the Padé working form.

Items (1) and (3) are **physical-picture questions** — under PD-006 they go to the founder. Item (2) is a derivation the worker owes once (1) is fixed. **Not escalated by binding rule** (no CONTRADICTION majority), **escalated by adjudication**: without them the corpus holds three floors and the flagship arc rests on one of them by choice.

### Q6 — Corrigenda text: **FAITHFUL-AT-GRADE by count (3–1); OVERCLAIMS by argument; restated**

GPT's two specific objections are both correct: the GR-1c note said "the exterior branch gives `u_max = 1`, hence `PSR_eff ≥ l_P/2`" — presenting attainment as derived — and described incompressibility as "SSV_abs register at its maximum," which is the P2/P3 equivocation in a sentence. Gemini asks that the SSV_crit relation be stated as *unresolved pending founder ruling* rather than "under CONV-038 Q5." Both are strictly weaker and fold. **Corrigenda v1.1** (§3 below) replaces §5 of the package.

### Q7 — Scope audit: **ITEMS-FOUND (adopted regardless of tally)**

GPT's eight and Copilot's six, deduplicated, become work:
1. Bound-vs-attainment (Q2) — enacted in this adjudication.
2. Constant-`u` vs constant-density equivocation (Q2) — registered as **OPEN-GR-FLOOR-1(b)**: write the interior bridge or show the bound needs none.
3. "Packing premise excluded by P1–P3" — narrowed to "excluded *at the surface* by P1 + Buchdahl."
4. α ≡ 1 not earned — enacted (Q5).
5. |R| = 1 channels (mode conversion, transient absorption) — registered under the wall-condition item.
6. `X = 0` as node limit — needs a derived impedance; registered under the wall-condition item.
7. Retirement dependency sweep (SR, cosmology) — owed.
8. "l_P/2 recovered" — withdrawn from 3367 §5 by dated note.
9. SR-1 internal inconsistency (Padé vs collapse) — to the founder (Q5).
10. FE-1 at saturation — RCORE-4, already open; Copilot's "or a sensitivity analysis" adopted as an interim deliverable.
11. Archival provenance of the retired rule — tombstone amended.
12. "Clamped register" sweep — Copilot says notes/renames required; the worker's deferral stands until the wall computation, but each of the 40 sites gets a dated pointer to this round at enactment (a pointer is not a rename).

### Q8 — Assembly and disposition

Q8a: IMPROPER / PROPER-WITH-REVISIONS ×2 / PROPER. Q8b: **BLOCK / RESTATE-REQUIRED ×2 / CORRIGENDA-CLEAR — no majority.**

By argument: the BLOCK seat's own text says *"the retirement correction should proceed, and the Buchdahl algebra is useful"* and names its conditions for the arc — *"floor undetermined; Buchdahl conditional bound PSR ≥ l_P/2 until these issues clear."* That banner is adopted verbatim. With the Q2/Q3/Q6 restatements enacted and the banner on the arc, the BLOCK seat's stated objections are met; the CLEAR seat is the un-executed one and is outweighed. **Disposition: RESTATE-REQUIRED — enacted as corrigenda v1.1 (below), the arc banner, the Q4(iii) caveat, and the Q5 escalation.** The corrigenda do not enter shipped `.tex` until the founder ratifies this bundle (3362 precedent).

## §2 What this round established, in one paragraph, against the worker

Patch 3367 claimed to re-derive the floor. It re-derived a *bound*. The half survives as the largest value a static saturated body can have at its surface, conditional on Einstein's equations holding inside it — a statement the corpus cannot currently make cleanly, because the same symbol `u` is used for the metric variable outside and a flat register inside. Whether the register actually reaches the bound, and what SR-1's own cap says it reaches, are open; three candidate floors stand in the corpus and the flagship prediction has been resting on one of them. The mirror's magnitude survives; its phase does not; the 191 Hz line inherits an uncomputed boundary shift. The panel found all of this, one seat found the sharpest of it, and that seat was the only one that ran the numbers.

## §3 Corrigenda v1.1 (supersedes package §5; enters shipped text on founder ratification)

> **GR-1c Theorem 2, proof — corrigendum note (CONV-038, adjudicated Patch 3369):** The proof above invokes the CP Exclusion Rule. That rule was retired by the founder before this paper's repository version (R-EXCL-RETIRED, `axiom-registry.md` §"Retired rules"); its cited source, the Absolute Moment companion, has never contained it. The proof's reading of `l_P` as the lattice spacing is also withdrawn (Patch 0733: `l_P` is the baseline PSR, ~10³⁰ sub-Planck grid points). **The bound `PSR_eff ≥ l_P/2` is retained as a conditional lower bound with a replaced derivation:** if the saturated body is static and Einstein's equations hold in its interior (OPEN-GR-RCORE-4), Buchdahl's theorem in the surface saturation variable `u = kΔ|SSV|` reads `u² − 5u + 4 ≥ 0`; the root `u = 4` lies inside the censored region, so the exterior branch gives `u_surface ≤ 1`, hence `PSR_surface ≥ l_P/2` (`rcore_derivation/3367_psr_floor_from_buchdahl.md`; verify 25/25). **Whether the register attains this bound (PSR = l_P/2 exactly) is an extremality assumption, not a derived result; and the relation between this bound and SR-1's register cap `SSV_crit = E_P/l_P³` is unresolved pending a founder ruling (CONV-038 Q5).** The R-core arc carries the standing banner: *floor undetermined; Buchdahl conditional bound PSR ≥ l_P/2.*

> **GR-1b, definitions and §"Effective Horizon and the GP Exclusion Rule" — corrigendum note:** the CP Exclusion Rule is retired (as above). The sentence "GPs become unavailable as destinations for infalling CPs, which are deflected to neighboring GPs" is superseded by the founder's replacement mechanism: a CP displaced onto an occupied GP superimposes for one Moment and is moved per the local SSV_net the next. The identification `kΔ|SSV| = 1 at r = r_s` is superseded by GR-1c Corrigendum 2. `SSV_crit` (SR-1 Eq. 1) is retained; its map to the GR-lane variable `u`, and the choice between SR-1's Padé working form and its `r_eff → 0` collapse statement, are unresolved pending a founder ruling (CONV-038 Q5).

> **RCORE_derivation.md §3, W-C ch. 2, and the 40 "clamped register" sites:** dated pointer to CONV-038 at each site; the term is flagged as a misnomer for a one-sided, one-Moment-delay compliant boundary whose impedance is uncomputed. Rename deferred to the wall computation (OPEN-GR-ROT-1).

> **PRED-O-39 and GR-2 (next version) — OBLIGED by Q4(iii) 4–0:** append to the conditionality clause: *"…and on the Dirichlet wall condition X = 0, the zero-compliance limit of a one-Moment-delay compliant surface; the boundary-phase shift is uncomputed and the stated 188–194 Hz band does not include it. |R| = 1 is established in the channel computed at Patch 3297; mode conversion and intra-Moment absorption are not excluded."*

## §4 Escalated to the founder (physical-picture questions; PD-006)

1. **SR-1's collapse statement.** Appendix A.5 Step 2 and D.4 say the Voronoi cell "collapses (r_eff → 0)" at `SSV_crit`. The Padé form in the same appendix gives a finite `l_P/(1+α)`. GR-1c gives `l_P/2`. **Which is the physics at the cap: does the perception sphere go to zero, or to a finite floor?** (The 31-Aug intuition said zero; the 1-Sep ruling said register limit, finite.)
2. **What is the invariant cell.** SR-1's cap is "one Planck energy per Voronoi cell." The cell volume is quoted in a unit-dependent convention. **Is the physical cell the insphere, the circumsphere, or the Voronoi cell at baseline PSR — and is `SSV_crit` a fixed physical stress or a unit-setting convention?** GPT: if it is physical, α cannot be set to 1 by hand.

## §5 Owed by the worker

- OPEN-GR-FLOOR-1(a): the extremality step — derive attainment or bound its failure.
- OPEN-GR-FLOOR-1(b): the interior bridge — what `u` means inside saturation, or a proof the bound needs no interior statement.
- OPEN-GR-FLOOR-1(c): after the founder's §4 rulings — the derived map `SSV_crit → u`.
- Retirement dependency sweep, SR + cosmology.
- The wall impedance (with OPEN-GR-ROT-1): |R| channels and the phase.
- Enactment patch on ratification: corrigenda v1.1 into GR-1b/GR-1c/RCORE/W-C; GR-2 V1.7 + PRED-O-39 caveat; 40-site pointers; tombstone provenance note.

---

## AMENDMENT — Patch 3370 (2 Sep 2026): Seat 2 (Grok) RECEIVED; panel 5/5; EK-1 two of five

Grok's return arrived after 3369 and **hash-matches EK-1** (`pc=7.6533`) — the second execution-verified seat. Verbatim in `reviews-CONV-038.md` Seat 2. Verify `code/3370_floor_sensitivity_conv038_amend_verify.py` (26/26).

**Tallies on five seats:** Q1 ESTABLISHED-WITH-GAPS **3–2** (now a majority; the SR/cosmology dependency sweep is owed by rule, not only by adoption). Q2 SOUND-WITH-CAVEATS 4–1. Q3 CORRECTLY-SCOPED 3 by count — but Grok's own Q2 (*"Route A therefore stands as a surface-compactness bound … not as a constructed interior solution"*) and Q7(2) (*"several sentences treat P4 equality as forced"*) endorse the substance of the BOUND relabel, which is strictly weaker and stands as enacted. Q4(ii) DOES-NOT-SURVIVE **5–0**; Q4(iii) YES **5–0**. Q5 UNDERDETERMINED **5–0**. Q6 FAITHFUL 4–1. Q7 ITEMS-FOUND 3–2. Q8b CLEAR 2 / RESTATE 2 / BLOCK 1 — still no majority; Grok's CLEAR is "clear with Q7 (1)–(3) folded at enactment," which is what the 3369 disposition already does. **Disposition unchanged.**

**Grok items adopted:** (1) the axiom-registry replacement row wrote "SSV_abs at k·u = 1," pre-judging Q5 — **corrected at 3370** (value no longer stated in the tombstone; bounds stated instead). (2)/(3) folded into the BOUND relabel. (4) §0's "no derivation" narrowed: SR-1 App. A.5 is a second cap, at a different number.

**Founder rulings on the §4 escalation (verbatim `founders_voice/founder_ruling_floor_finite_cell_size_open_2026-09-02.md`):** **R-FLOOR-FINITE** — the floor is finite; SR-1's `r_eff → 0` is superseded as physics (SR-1 corrigendum owed, SR lane). **R-CELL-SIZE-OPEN** — the founder has no argument for the cap's magnitude; neither `u = 1` nor `α_geom` has priority by authority.

**What the sensitivity shows (3370 verify):** both SR-1 candidates satisfy Buchdahl (`u ≤ 1`) — the two papers are *consistent* as bound-plus-candidate; only attainment was ever in dispute. But the flagship arc is **not robust to the value**: at `u = 0.5594` the wall moves out to 1.46 r_S and the Level-A cavity shrinks from 2.15 ms to 0.14 ms; at `u = 0.2444` the wall sits at 2.58 r_S, *outside the photon sphere* — no light ring, no Kerr-like ringdown, which GW150914 has. So reality bounds the cap from below: `R(u) < 3μ ⇔ u > 4 − √12 = 0.536`. **The cap is boxed: 0.536 < u_max ≤ 1, i.e. l_P/2 ≤ PSR_floor < 0.651 l_P.** The insphere reading of SR-1 is empirically dead; the circumradius reading survives by 4% and would kill the echo. PRED-O-39 carries a floor-value caveat in addition to the phase caveat.

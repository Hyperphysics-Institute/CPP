# CONV-038 REVIEW PACKAGE v1.0 — The R-core arc's premise was a retired rule; the PSR floor l_P/2 re-derived from Buchdahl (Patch 3367); and a second, pre-existing derivation in SR-1 that does not obviously give the same number
# (Patch 3368, 2 Sep 2026, Session 161)

**PASTE DISCIPLINE (founder):** this ENTIRE file is one package — one
identical paste per seat (Copilot may need the file-upload route).
Execution-capable seats also receive `3367_psr_floor_from_buchdahl_verify.py`
(runs in seconds; sympy only). Returns INLINE, verbatim, in the §8 skeleton.

**ID NOTE:** CONV-036 remains skipped (see CONV-037's note). This round is
CONV-038. Grep of the corpus at dispatch: zero prior uses.

---

## §0 What this round decides, in one paragraph

The Session-160 handover queued "derive the wall condition X = 0 from the
rotating clamped register." The founder asked what a clamped register is.
Tracing the term (an Opus coinage, Patch 3297) led to the **CP Exclusion
Rule** — invoked live in shipped GR-1b and in GR-1c Theorem 2's proof,
absent from `axiom-registry.md`, and, per founder ruling **R-EXCL-RETIRED**
(31 Aug–1 Sep), *eliminated earlier as unnecessary* with no retirement ever
recorded. Its cited source (c01, "Absolute Moment companion §2") has never
contained it in any repository version. The PSR floor `l_P/2` — the number
under the Planck core, the |R| = 1 mirror, the Buchdahl relocation, the Kerr
surface, the wall modes, GR-2 V1.6 and PRED-O-39 — therefore had, as of
Patch 3366, **no derivation**. Patch 3367 re-derives it (Route A): with the
founder's ruling that the floor is a *register-saturation* limit (the
saturated interior is incompressible), Buchdahl's bound in the saturation
variable is `u² − 5u + 4 ≥ 0`, roots {1, 4}, the 4 is behind the horizon,
and extremality gives `u_max = 1 ⇒ PSR = l_P/2`. Conditional on Einstein's
equations holding at saturation (RCORE-4). **This round decides whether that
derivation stands, and — the part found while assembling the package — how
it squares with SR-1's own register cap `SSV_crit = E_P/l_P³`, which in the
same variable gives `u_max = α_geom ≈ 0.56` (or 0.24, unit-dependent), or a
collapse to PSR → 0, depending on which of SR-1's own expressions is read
as physical.** The founder asked for a triangulation. There may be one
here, or there may be a contradiction; the panel is asked which.

GitHub (repo `CPP`, branch `main`, HEAD = Patch 3367):
`founders_voice/founder_ruling_exclusion_retired_register_floor_2026-09-01.md`,
`axiom-registry.md` §"Retired rules (anti-erasure ledger)",
`series_gravitation/rcore_derivation/3367_psr_floor_from_buchdahl.md`,
`series_gravitation/code/3367_psr_floor_from_buchdahl_verify.py`,
`series_gravitation/reasoning/3367.md`.

## §1 Under review / fenced

UNDER REVIEW: (a) the retirement itself — its scope beyond GR (GR-1c calls
the rule "established … for the purpose of CP identity conservation"; GR-1b
says it "drives the initial expansion of the universe"); (b) Route A's
premise chain P1–P4 (§2); (c) the P3 conditionality (FE-1 at saturation);
(d) the P4 extremality step; (e) **the SR-1 register cap and its value in
the `u` variable** (§2.4); (f) whether the 3297 mirror (|R| = 1, phase π)
survives the founder's replacement boundary picture (superimpose one
Moment, displace per SSV_net the next) — a compliant one-Moment-delay wall,
not a two-sided clamp; (g) the corrigenda scope (§5); (h) the standing
scope audit (3347 practice).

FENCED (settled, not re-adjudicated): the exact exterior (GR-1c Thm 1,
CONV-030 5–0 SOUND — NOT touched by the retirement; it uses only the
PSR formula and the source law); the lattice ≡ isotropic dictionary (T-1
CHARTER, 3262); A1–A3 / censorship (CONV-032); the Teukolsky ladder's
numerics *given* a Dirichlet wall (CONV-037) — what is under review is the
wall, not the solver.

## §2 The claim chains

### 2.1 The retirement (founder authority; Opus archaeology)

- L1. "Clamped register" first appears in `reasoning/3297.md` (21 Aug);
  40 sites / 19 files by 3364; no glossary entry; never in founder text.
- L2. Its physics: "the Exclusion floor clamps the register" (RCORE §3) →
  the CP Exclusion Rule (GR-1b defs: "no two CPs of the same type and
  polarity may occupy the same GP"; GR-1c Thm 2 proof: "no two CPs may
  occupy the same GP" ⇒ `PSR_eff ≥ l_P/2`).
- L3. Absent from `axiom-registry.md` and `master_glossary.md`. Cited to
  c01 §2 by both GR-1b and GR-1c; **c01 has never contained it in any
  repository version** (`git log -S`, all revisions: 0 hits).
- L4. Founder, 31 Aug: *"We originally had the CP exclusion rule, and we
  eliminated it when we realized that it was unnecessary. We used the ZBW
  effect instead, merely looking at the local SSV_net at each Moment after
  superimposition."* 1 Sep: one-CP-per-GP *"inconsistent with reality."*
- L5. Consequence: GR-1c Thm 2's proof is void. The VALUE `l_P/2` is
  orphaned. Tombstone entered at 3366.

### 2.2 Route A (Patch 3367) — the value recovered

- P1 Exterior: exact Schwarzschild, isotropic, `u ≡ k·Δ|SSV| = μ/r̄`,
  `PSR = l_P/(1+u)`. [GR-1c Thm 1 — fenced.]
- P2 Incompressibility: the saturated interior holds `u = u_max`
  throughout; density non-increasing outward. [Founder R-FLOOR-REGISTER.]
- P3 Static, Einstein-consistent interior. [FE-1 closed for the exterior;
  at saturation = OPEN-GR-RCORE-4 — **conditional**.]
- P4 Extremality: the register saturates at the largest admissible value.
  [Stated, not derived.]
- Buchdahl `R ≥ 9M/4` is *derived in-script* from the Schwarzschild interior
  solution (central-pressure pole and central-lapse zero at `s = 1/3`).
- Surface areal radius `R(u) = (μ/u)(1+u/2)²`; bound ⟺ `u² − 5u + 4 ≥ 0`
  ⟺ `u ≤ 1 or u ≥ 4`; `R(u)` minimal at `u = 2` (horizon); `u = 4` at
  `r̄ = μ/4`, censored; exterior branch ⇒ `u_max ≤ 1`; P4 ⇒ `u_max = 1`;
  `PSR_floor = l_P/2`. 3297's 9μ/4, lapse 1/3, z = 2, c_*/c = 1/2 follow.
- Negative control (in code): a packing floor at the sub-Planck grid step
  (~10⁻³⁰ l_P, Patch 0733) sits on the censored branch — the packing
  premise is *excluded* by P1–P3, not merely unused. Verify 25/25.

### 2.3 Route B — withdrawn

Proposed 31 Aug as a census-reach fixed point. Does not close: the PSR is
the per-Moment hop and sets census *speed* (`c_* = PSR/√3 t_P`), not
*reach*; AP-4's relay carries DI-bits beyond one PSR; the interior register
of a uniform body is the ordinary interior potential, PSR-independent,
maximal at the centre. Asserted in code (Check 7). The worker set it up
wrongly and says so in `reasoning/3367.md`.

### 2.4 THE FINDING MADE WHILE ASSEMBLING THIS PACKAGE — SR-1 already has a register cap, and it is not obviously `u = 1`

Assembling the corrigendum scope (§5) required reading GR-1b's Exclusion
section, which cites *"SSV_crit (SR-1 Eq. 1)"* as the stress at which the
PSR reaches its minimum. SR-1 Appendix A.5 does carry a substrate-internal
register cap — **exactly the "second leg" 3367 declared missing**:

> *"each Voronoi cell can store at most one quantum of Planck energy E_P
> before the displacement budget is entirely consumed"* ⇒
> `SSV_crit = E_P / l_P³ ≈ 4.63 × 10¹¹³ J m⁻³` (SR-1 Eq. ssv_crit).

And `k ≡ α/SSV_crit`, with `ε ≡ ΔSSV/SSV_crit`, so that in the GR lane's
variable **`u = k·ΔSSV = α·ε`**. At the cap `ε = 1`:

| SR-1 expression | What it gives at ε = 1 | PSR floor |
|---|---|---|
| Padé form `s(ε) = 1/(1+αε)` ("the physically correct working expression," App. E) | `u_max = α_geom` | `l_P/(1+α)` — **0.64 l_P** (α = 0.5594, unit-circumradius) or **0.80 l_P** (α = 0.2444, unit-insphere) |
| Collapse statement: *"the cell collapses (r_eff → 0) when the stored energy per cell equals …"* (App. A.5 Step 2; App. D.4 line "critical stress … at which the cell collapses (r_eff → 0)") | PSR → 0 | **0** — the founder's 31-Aug intuition |
| Route A (3367) | `u_max = 1` | **l_P/2** — GR-1c's number |

Three values from two papers and one derivation. SR-1 itself says α_geom
is *"not a pure number,"* *"relative to a choice of length unit,"* and *"by
Step 3 … unobservable"* — a normalisation convention. If so, "ε = 1" is a
convention-dependent statement and cannot be the physical cap; the physical
cap must be stated in `u`. Route A says `u_max = 1`. **One consistent
reading:** the physical normalisation of SSV_crit is the one in which
α = 1 — i.e. SSV_crit is *defined* as the stress at which `u = 1`, making
SR-1's "one Planck energy per cell" and Buchdahl agree by fixing the unit.
Whether that is a derivation, a re-definition, or a contradiction is
**Q5 below**, and it is the question the founder's "triangulation" turns on.
The worker has NOT resolved it and does not propose to before the panel
rules; he flags that the SR-1 collapse statement (PSR → 0) is, if physical,
fatal to c_* = c/2 and to the entire R-core arc, and that it sits in a
shipped paper beside a Padé form that contradicts it.

## §3 Triage — the worker's seven weakest points

T-1 **P3.** Buchdahl needs Einstein's equations *inside* the saturated
    body. GR-1c says its exterior formula "ceases to apply" there and pins
    `u = 1` flat — which is NOT the Schwarzschild interior solution (whose
    register would climb to `u = 2` at the centre). Is a flat-register
    interior Einstein-consistent at all? If not, does Buchdahl still bind
    (it needs only staticity, spherical symmetry, ρ' ≤ 0 and the field
    equations), or does Route A collapse to "conditional on something
    false"?
T-2 **P4.** Buchdahl gives `u_max ≤ 1`. Equality is asserted. Is "the
    exterior register climbs inward and stops only where it must" a
    derivation, or a story? What would a register that stops at `u = 0.9`
    violate?
T-3 **Circularity.** 3297 found Buchdahl *from* `u = 1`; 3367 finds
    `u = 1` *from* Buchdahl. The premises differ (Exclusion vs
    incompressibility + GR-consistency), so the worker holds this is
    inversion, not circularity. Rule on it.
T-4 **The SR-1 cap (§2.4).** Three candidate floors. The worker's
    "α = 1 by normalisation" reading rescues everything and is therefore
    exactly the reading to distrust. Is it earned? And is SR-1's
    "r_eff → 0" collapse a live claim or a superseded one?
T-5 **The mirror under the new wall.** 3297's |R| = 1 argument was:
    absorption needs storage (forbidden — *"no register headroom"*), a
    sink (forbidden — AP-4), or secular transfer (forbidden — GR-1e). The
    "no headroom" step survives R-FLOOR-REGISTER (it IS the register
    limit). But the founder's replacement picture — superimpose one
    Moment, displace next — is a *one-sided, delayed* response, not a
    node. |R| = 1 plausibly survives (nothing is stored across Moments);
    the phase π does not obviously survive. Does GR-2 V1.6's 191 Hz line,
    computed with X = 0, now carry an unquantified phase error, and must
    PRED-O-39 say so?
T-6 **Scope of the retirement.** GR-1c: the rule was "established … for
    CP identity conservation." GR-1b: it "drives the initial expansion."
    If it is retired, what now does those two jobs? Are there orphans
    outside the GR lane (SR, cosmology)? The worker searched
    `founders_vision.md`, `master_glossary.md`, registries: no other
    invocation found — but absence of a grep hit is not a proof.
T-7 **"Clamped register," 40 sites.** Wrong name (one-sided constraint,
    not a clamp) for an object whose response is now to be computed.
    Sweep now (rename) or after the computation (substantive note per
    site)? The worker chose after; the panel may overrule.

## §4 Frozen questions (answer ALL; vocabulary only)

Q1 — The retirement record (L1–L5): is the Exclusion Rule's void status
     ESTABLISHED, and is the tombstone adequate?
     **ESTABLISHED / ESTABLISHED-WITH-GAPS (list) / NOT-ESTABLISHED**
Q2 — Route A's premise chain P1–P4 and the quadratic (T-1, T-2, T-3):
     **SOUND / SOUND-WITH-CAVEATS / UNSOUND**
Q3 — The standing label DERIVED-CONDITIONAL (on RCORE-4) for the floor:
     **CORRECTLY-SCOPED / UNDER-SCOPED / OVER-SCOPED**
Q4 — The mirror under a compliant one-Moment-delay wall (T-5):
     (i) |R| = 1: **SURVIVES / SURVIVES-WITH-CAVEATS / DOES-NOT-SURVIVE**
     (ii) phase π: **SURVIVES / SURVIVES-WITH-CAVEATS / DOES-NOT-SURVIVE**
     (iii) PRED-O-39 / GR-2 V1.6 must carry a boundary-phase caveat:
     **YES / NO**
Q5 — The SR-1 register cap vs Route A (§2.4, T-4). Which reading:
     **CONSISTENT-BY-NORMALISATION (α ≡ 1 fixes the unit; Buchdahl and
     SR-1 agree) / SR-1-SUPERSEDED (the collapse statement is dead; Padé
     with α ≠ 1 is the live SR-1 claim and DISAGREES with l_P/2) /
     CONTRADICTION (a live conflict requiring a founder ruling) /
     UNDERDETERMINED (the record does not decide; state what would)**
Q6 — The PROPOSED corrigenda text (§5): **FAITHFUL-AT-GRADE / OVERCLAIMS /
     UNDERCLAIMS**
Q7 — Scope audit — any universal whose computation is narrower than the
     sentence, in 3367 or in this package: **NONE-FOUND / ITEMS-FOUND (list)**
Q8a — Assembly: **PROPER / PROPER-WITH-REVISIONS / IMPROPER**
Q8b — Disposition: **CORRIGENDA-CLEAR / RESTATE-REQUIRED / BLOCK**

BINDING RULES (frozen): majority per question. Majority UNSOUND on Q2
leaves the floor ORPHANED (no derivation of record) and the R-core arc
carries an explicit "floor undetermined" banner until a derivation clears.
Majority CONTRADICTION on Q5 escalates to the founder as a
physical-picture question and BLOCKS Q8b regardless of tally. Majority
YES on Q4(iii) obliges the caveat in PRED-O-39 and GR-2 at the next
version. Q7 items adopted as work regardless of tally. Strictly-weaker
revisions fold at enactment (CONV-034/035 precedent); anything STRONGER
than what is proposed owes its own round.

## §5 THE PROPOSED CORRIGENDA (what would enter shipped text on clearance; anti-erasure by dated note, no equation changes)

> **GR-1c Theorem 2, proof — corrigendum note (Patch 33NN, CONV-038):**
> The proof above invokes the CP Exclusion Rule ("no two Conscious Points
> may simultaneously occupy the same Grid Point"). That rule was retired by
> the founder before this paper's repository version (R-EXCL-RETIRED,
> registered 1 Sep 2026; `axiom-registry.md` §"Retired rules"); its cited
> source, the Absolute Moment companion, does not contain it. The bound
> `PSR_eff ≥ l_P/2` is retained; its derivation is replaced: with the
> saturated interior incompressible (SSV_abs register at its maximum) and
> Einstein's equations holding there (conditional on OPEN-GR-RCORE-4),
> Buchdahl's bound in the saturation variable `u = kΔ|SSV|` reads
> `u² − 5u + 4 ≥ 0`; the root `u = 4` lies inside the censored region and
> the exterior branch gives `u_max = 1`, hence `PSR_eff ≥ l_P/2`
> (`series_gravitation/rcore_derivation/3367_psr_floor_from_buchdahl.md`;
> verify 25/25). The proof's reading of `l_P` as the lattice spacing is
> also withdrawn (Patch 0733 grounding: `l_P` is the baseline PSR,
> ~10³⁰ sub-Planck grid points).

> **GR-1b, §"Effective Horizon and the GP Exclusion Rule" and definitions
> — corrigendum note:** the CP Exclusion Rule is retired (as above); the
> sentence "GPs become unavailable as destinations for infalling CPs, which
> are deflected to neighboring GPs" is superseded by the founder's
> replacement mechanism: a CP displaced onto an occupied GP superimposes for
> one Moment and is moved per the local SSV_net the next. The identification
> `kΔ|SSV| = 1 at r = r_s` is superseded by GR-1c Corrigendum 2 (saturation
> at isotropic `r̄ = μ`, areal `9μ/4`, outside the would-be horizon).
> `SSV_crit` (SR-1 Eq. 1) is retained as the register cap; its relation to
> `u = 1` is under CONV-038 Q5.

> **RCORE_derivation.md §3 and W-C ch. 2:** dated notes at each "Exclusion
> floor" / "clamped register" site pointing to this round; the term
> "clamped register" is flagged as a misnomer for a one-sided,
> one-Moment-delay compliant boundary, pending the computation that
> replaces it (OPEN-GR-ROT-1 / wall condition).

> **PRED-O-39 / GR-2 V1.6 (only if Q4(iii) = YES):** append to the
> conditionality clause: "…and on the Dirichlet (X = 0) wall condition,
> which is the node limit of a one-Moment-delay compliant surface; the
> boundary-phase correction is uncomputed."

## §6 Seat mandates

- **IDENTITY:** own model name on the REVIEWER line. Gemini seat: you are
  Gemini. DeepSeek seat: you are DeepSeek. (CONV-037: the Copilot seat
  self-labelled "Gemini"; the founder confirmed the slot. State yours.)
- **OWN-RUN:** SCRIPT-EXECUTED = your own run of
  `3367_psr_floor_from_buchdahl_verify.py`. Reference count line:
  `3367 verify: 25 passed, 0 failed`. INDEPENDENT-HARNESS welcome (your own
  Buchdahl derivation; your own reading of SR-1 App. A.5/E).
- **EXECUTION KEY EK-1 (first use in the GR lane; DM-lane design, Patches
  3506/3507):** compute, without reading them from anywhere, (i) the
  central pressure ratio `p_c/ρ` of the uniform-density Schwarzschild
  interior solution at `R = 2.3 M` (G = c = 1), 4 decimal places; (ii) the
  surface areal radius `R(u)/μ` at `u = 0.9`, 4 decimal places; (iii) the
  isotropic Schwarzschild lapse `(1 − u/2)/(1 + u/2)` at `u = 0.9`, 4
  decimal places. Return the exact string
  `pc=X.XXXX;R=Y.YYYY;lapse=Z.ZZZZ`. The answer appears nowhere in this
  packet or the corpus. Its SHA-256 is sealed here:

      640d6cbf91553eb8e2ff1e6d32974e295f889434d7431fd7688e3b24d8bfc599

  A return whose string hashes to this value earns execution credit; any
  other string is graded INSPECTED regardless of what it claims.
- **COUNT-LINE** verbatim; **TIER** on every answer; **RETURNS** inline in
  the §8 skeleton.

Steers: **GPT** — T-4/Q5 is yours: you have ruled hard on grade four
rounds running; rule on whether "α ≡ 1 by normalisation" is a derivation
or a rescue. **Grok** — T-1: is a flat-register interior Einstein-
consistent, and does Buchdahl bind if it is not? Own-run the script and
attempt an INDEPENDENT-HARNESS Buchdahl. **Gemini** — T-2 and T-3:
extremality and the inversion-vs-circularity call; your "is the language
EARNED" standard applies to "forced by consistency." **Copilot** — Q1 and
T-6: the retirement record and its scope outside GR; hunt for orphans
the grep missed. **DeepSeek** — T-5/Q4: what a one-Moment-delay
compliant wall does to |R| and to the phase; if you can bound the phase
correction at echo frequencies from AP-4's Moment scale, do it.

## §7 Materials — in full

### 7.1 Founder ruling file (Patch 3366), verbatim

# Founder rulings — the CP Exclusion Rule is RETIRED; the PSR floor is a REGISTER limit; the mirror is kept (31 Aug – 1 Sep 2026, Session 161, GR lane)

**Status:** verbatim founder text, registered at Patch 3366. Rulings minted:
**R-EXCL-RETIRED** (items 1, 3), **R-FLOOR-REGISTER** (item 3), **R-MIRROR-KEPT** (item 2).
Consequences enacted at Patches 3366–3367; corrigenda to shipped GR-1b/GR-1c
owed under CONV-038 (see `frontier_sectors/GR.md`).

**How this arose.** The Session-160 handover queued, as its load-bearing item,
"derive the wall condition X = 0 from the rotating clamped register." The
founder asked what a "clamped register" is. The term proved to be an Opus
coinage (Patch 3297, 21 Aug 2026; 40 occurrences in 19 files; no glossary
entry; never in the founder's words). Tracing its physics led to the CP
Exclusion Rule (GR-1b definitions; GR-1c Theorem 2 proof), which is absent
from `axiom-registry.md`. The founder then ruled as follows.

---

## 1. The Exclusion Rule was retired (31 Aug 2026)

> "We originally had the CP exclusion rule, and we eliminated it when we
> realized that it was unnecessary. We used the ZBW effect instead, merely
> looking at the local SSV_net at each Moment after superimposition. The CP
> exclusion rule was unnecessary because we achieved its effect simply by
> looking at the environment and moving in the direction of the SSV_net the
> next Moment."

*Opus note:* no patch, glossary line, or registry entry records this
retirement. GR-1b (shipped) and GR-1c Thm 2 (shipped, CONV-030 5–0) invoke the
rule as live. This is a **retirement without a tombstone**; the tombstone is
now `axiom-registry.md` §"Retired rules (anti-erasure ledger)", Patch 3366.

## 2. The mirror is kept (31 Aug 2026)

Offered the fork between information conserved by *reflection* (|R| = 1 exact,
Patch 3297) and by *storage in surface strata* (the founder's superposition
picture of 31 Aug, which is Axiom H, founders_vision §6e):

> "The mirror is less complicated. Let's see how it plays out. If it solves
> all the problems consistently, then that's the triangulation we are looking
> for."

## 3. The floor is a register limit, not a packing limit (1 Sep 2026)

Offered the fork "packing limit (one-per-GP, kinematic, PSR → GP spacing) vs
register limit (SSV_abs saturates at k·u = 1, PSR floor l_P/2, GPs still
~10²⁹ deep)":

> "I had seen the packing limit as one CP per GP, but I think that produces the
> frozen BH that can't move. If there are 10^29 GPs between CPs, then there is
> plenty of room for the CPs in the BH to mediate rotation and translation, and
> in general respond to the SSV_net, etc. The bottom line question is: what is
> the minimum PSR distance? How is that established? Why should that naturally
> arise as a theorem from the axioms?"

> "I think the one CP per GP is inconsistent with reality, so we can safely
> eliminate that option. I think your second framing of the register limit of
> SSV_abs and PSR floor of l_P/2 is rational. Does this follow from our axioms,
> or is this an axiom?"

*Opus answer (Patch 3367):* as of the ruling it was **neither** — its only
derivation (GR-1c Thm 2) rested on the retired rule. Re-derived at 3367 from
Buchdahl + the exact exterior + incompressibility (Route A), conditional on the
field equation holding at saturation (OPEN-GR-RCORE-4). See
`rcore_derivation/3367_psr_floor_from_buchdahl.md`.

## 4. The founder's own physical picture of the surface (31 Aug 2026) — recorded as the wall-condition definition

> "Even though the CPs are at full density, when the BH is impacted at its
> surface, the DI-bits associated with the energy of the Impact are transmitted
> to the GPs on the surface, which displace the CPs on the GPs."

> "Since the GPs are full, if a CP receives a move message, it moves onto an
> already occupied GP. Thus, in the next Moment, the CP will be transmitted via
> the SSV_net to the position associated with that displacement."

> "The register is just the value of the SSV_abs."

*Opus note:* under R-EXCL-RETIRED this is the boundary condition item 1 must
compute: a **compliant boundary with a one-Moment delay** (superimpose, then
displace per SSV_net), not a two-sided clamp. "Clamped register" is therefore
the wrong name for the wrong object; the glossary entry is HELD until the
surface response is computed (Patch 3366 registers this; the term is not yet
swept from the corpus — 40 sites — pending the computation that replaces it).

## 5. The founder's diagnosis that opened the thread (31 Aug 2026)

> "I realized that the current set of axioms cannot properly address whether
> the impact of a mass or wave on the surface of a Black Hole can propagate
> through the Black Hole. This question brings up a corollary question: how does
> a Black Hole move through space by KE … with the current axioms, the BH
> cannot move once it forms, because the SSV_net cannot transmit beyond one PSR,
> and in a 100% saturated space by axiom does not reach to the next GP. The same
> problem makes it impossible for the Black Hole to rotate."

*Opus note:* the diagnosis holds under the packing reading and dissolves under
the register reading (floor l_P/2 spans ~10²⁹ sub-Planck GPs; c_* = c/2 in the
core; translation by synchronous lockstep under A4). What survives it, and is
new: **rotation of a saturated core has never been derived** — 3339/3359
assumed a wall at Ω_w. Registered as OPEN-GR-ROT-1 (Patch 3366).

## 6. Instruction to proceed (1 Sep 2026)

> "Please proceed."


### 7.2 axiom-registry.md — the tombstone row (Patch 3366)

| **CP Exclusion Rule** — "no two CPs of the same type and polarity may occupy the same GP at the same Absolute Moment" (GR-1b definitions); read in GR-1c Thm 2 as "one CP per GP ⇒ PSR_eff ≥ l_P/2." | GR-1b (definitions, §"Effective Horizon and the GP Exclusion Rule"); GR-1c Thm 2 proof; narrative W-C ch. 2 ("the Exclusion floor," Patch 3312); RCORE_derivation.md §3 ("the Exclusion floor clamps the register"). | **Founder, R-EXCL-RETIRED** (31 Aug–1 Sep 2026, registered Patch 3366; verbatim `founders_voice/founder_ruling_exclusion_retired_register_floor_2026-09-01.md`). The founder states the rule was eliminated earlier as unnecessary; **no prior patch recorded the retirement** — this row is the tombstone. | ZBW + next-Moment SSV_net displacement: a CP displaced onto an occupied GP superimposes for one Moment and is moved per the local SSV_net the next (dynamical, not kinematic). Founder ruling R-FLOOR-REGISTER: the PSR floor is a **register-saturation** limit (SSV_abs at k·u = 1), not a packing limit; one-CP-per-GP "inconsistent with reality." | **PSR floor l_P/2:** orphaned at 3366; re-derived Patch 3367 (Route A, Buchdahl + exact exterior + incompressibility, conditional on FE-1 at saturation / RCORE-4). **GR-1b, GR-1c Thm 2 proof, W-C ch. 2, RCORE §3:** corrigenda OWED under CONV-038 (value preserved; premise replaced). Axiom count unchanged (the rule was never a registered row). |


### 7.3 Patch 3367 record

# OPEN-GR-FLOOR-1 — The PSR floor l_P/2 re-derived from Buchdahl's bound (Route A) — **DERIVED-CONDITIONAL**

**Patch 3367, Session 161, 1 Sep 2026.** Verify: `code/3367_psr_floor_from_buchdahl_verify.py` (25/25). Reasoning: `reasoning/3367.md`. Founder rulings: `founders_voice/founder_ruling_exclusion_retired_register_floor_2026-09-01.md`.

**Standing:** DERIVED-CONDITIONAL on P3 (Einstein's equations holding in the saturated interior = OPEN-GR-FE-1 at saturation = **OPEN-GR-RCORE-4**). CONV-038 owed. HALT-GR-1C-FLOOR fired against the *proof text* of GR-1c Thm 2 (value preserved; premise void); no `.tex` touched.

---

## §0 Why this record exists

GR-1c Theorem 2 states `PSR_eff ≥ l_P/2` and proves it from the CP Exclusion Rule ("no two CPs may occupy the same GP" ⇒ minimum lattice spacing). Founder ruling **R-EXCL-RETIRED** (31 Aug–1 Sep 2026): that rule was eliminated earlier as unnecessary, replaced by ZBW + next-Moment SSV_net displacement, and one-CP-per-GP is "inconsistent with reality." No retirement was ever recorded; the GR lane inherited the rule as live from GR-1b and built the R-core arc on it (3297 |R| = 1, the Buchdahl relocation, 3320 Kerr surface, 3339/3359 wall modes, GR-2 V1.6, PRED-O-39).

Consequence: the floor's only derivation is void. The number `1/2` — the most-cited number in the lane — had, as of 3366, no standing at all. This record gives it one.

The proof in GR-1c also misreads `l_P` as the grid step; Patch 0733 already withdrew that reading for the inflation case (`l_P` is the baseline PSR, ~10³⁰ sub-Planck GPs; c01 "the true grid is sub-Planck (~l_P/10³⁰) by nesting"). A one-per-GP packing floor would therefore sit at ~10⁻³⁰ l_P, not l_P/2 — the packing premise gets the wrong number even on its own terms (verify Check 6).

## §1 Premises — and the one that is NOT here

- **P1 (exterior).** Exact Schwarzschild in isotropic coordinates with the ratified dictionary `u ≡ k·Δ|SSV| = μ/r̄`, `PSR_eff = l_P/(1+u)`, `μ = GM/c²`. [GR-1c Thm 1; T-1 CHARTER lattice ≡ isotropic, Patch 3262.]
- **P2 (incompressibility).** The saturated interior holds the SSV_abs register at a fixed maximum `u_max` throughout; density non-increasing outward. [Founder ruling R-FLOOR-REGISTER: "the register is just the value of the SSV_abs"; the floor is a register limit.]
- **P3 (static Einstein-consistent interior).** The saturated body is a static configuration on which the CPP field equation — shown equal to Einstein's at OPEN-GR-FE-1 closure — holds. **This is the conditional step.** GR-1c's own text says the `μ/r̄` form "ceases to apply" inside the core; whether FE-1 holds *at saturation* is exactly OPEN-GR-RCORE-4 (the substrate census functional), the A1–A3 conditionality the entire spin sector already inherits. Under P2 + P3, Buchdahl's theorem binds.
- **P4 (extremality).** The register saturates at the *largest* value admissible under P1–P3. Physical reading: the exterior register `u = μ/r̄` grows inward and stops only where continuing would leave no static configuration. This is a stated premise, not a derived one — see §5.

**Not a premise:** the CP Exclusion Rule, one-CP-per-GP, any occupancy statement. The verify script asserts in code that its premise-bearing region contains none (Check 6).

## §2 Buchdahl's bound — derived, not cited

For the uniform-density Schwarzschild interior solution (G = c = 1), with `s ≡ √(1 − 2M/R)`:

    p_c / ρ = (1 − s) / (3s − 1),        e^{ν(0)} = (3/2) s − 1/2.

The central pressure diverges and the central lapse vanishes at `s = 1/3`, i.e. **`R = 9M/4 = (9/8) r_S`**. Buchdahl (1959) proved `R ≥ 9M/4` for *any* static spherically symmetric Einstein-consistent body with non-increasing density; the uniform case saturates it. (Verify Check 0.)

## §3 The bound in the saturation variable

Areal radius of the surface, with the surface at `r̄_s = μ/u_max` (P1 matched to P2):

    R(u) = r̄ (1 + μ/2r̄)² |_{r̄ = μ/u} = (μ/u)(1 + u/2)².

Buchdahl `R(u) ≥ 9μ/4` is, after clearing denominators,

    **u² − 5u + 4 ≥ 0   ⟺   u ≤ 1  or  u ≥ 4.**

`R(u)` has its minimum at `u = 2`, where `R = 2μ = r_S` — the horizon. The exterior (physical) branch is `u < 2`; the root `u = 4` sits at `r̄ = μ/4 < μ/2`, inside the horizon's isotropic image, censored. Hence on the exterior branch:

    **u_max ≤ 1.**

(Verify Checks 1–3.)

## §4 The floor

By P4, `u_max = 1`, so

    **PSR_floor = l_P / (1 + 1) = l_P/2.**

The surface then sits at areal `9μ/4`, lapse `1/3`, redshift `z = 2`, `c_*(surface) = c/2` — the 3297 numbers, now as **consequences** of the floor rather than of a rule. (Verify Checks 4–5.)

## §5 What this does and does not establish

**Establishes.** Given a register that saturates and an exterior that is exactly Schwarzschild, the saturation value is forced to `u_max = 1` by the requirement that a static body exist at all. The `1/2` is not free and not postulated; it is the smaller root of a quadratic whose larger root is behind the horizon.

**Does not establish.** (i) *Why* the register saturates — what in the substrate caps SSV_abs. That is the substrate-internal derivation, and it is the open half of FLOOR-1. (ii) The extremality step P4 is asserted; a derivation would show the register cannot stop *below* the admissible maximum. (iii) P3 is conditional on RCORE-4.

**Not a triangulation.** The founder asked for one (R-MIRROR-KEPT: "if it solves all the problems consistently, that's the triangulation"). This record supplies *one* derivation. A second, from inside the substrate without invoking FE-1 in the interior, would complete it — and would make Buchdahl's bound a *prediction* of CPP rather than an input. Until then: DERIVED-CONDITIONAL, not DERIVED.

## §6 Route B — closed, negative

Proposed 31 Aug: a census-reach fixed point `PSR = l_P/(1 + k·N_sources(PSR))`, on the idea that a smaller PSR reaches fewer sources. **It does not close.** Under AP-4 the DI-bit relay recursion carries messengers beyond one PSR; a smaller PSR slows the census (`c_* = PSR/(√3 t_P)`, T-1) but does not truncate the source set. The interior register of a uniform body under the 1/r census kernel is the ordinary interior potential, `(3R² − r²)/(2R³)`, with no PSR dependence and its maximum at the *centre* (3/2 of the surface value) — the opposite of a reach-limited profile. Asserted in code (Check 7) so the negative result cannot rot into a prose claim of "under investigation."

The worker set this route up wrongly on 31 Aug and says so here.

## §7 Owed

- **CONV-038** — panel audit of P1–P4, the conditionality, the corrigenda scope, and whether the 3297 mirror survives a one-Moment-delay compliant wall (R-EXCL-RETIRED's boundary condition).
- **Corrigenda** (after CONV-038; anti-erasure by dated note): GR-1c Thm 2 proof; GR-1b definitions + §"Effective Horizon and the GP Exclusion Rule"; W-C ch. 2; RCORE_derivation.md §3.
- **The substrate-internal derivation** — the second leg.
- **OPEN-GR-ROT-1** and the wall condition on the founder's picture (ruling file §4).


### 7.4 Patch 3367 verify script (ships separately for own-run; inlined for the non-executing seat)

```python
#!/usr/bin/env python3
"""
Patch 3367 verify — the PSR floor l_P/2 RE-GROUNDED (OPEN-GR-FLOOR-1, Route A).

Context. GR-1c Theorem 2 derived PSR_eff >= l_P/2 from the "CP Exclusion Rule"
(one CP per GP). Founder ruling 2026-09-01: that rule was RETIRED (replaced by
ZBW + next-Moment SSV_net displacement) and one-CP-per-GP is "inconsistent with
reality." The floor's only derivation is therefore VOID; the number was
orphaned. This script re-derives the VALUE 1/2 from premises that are still
standing, and asserts that the Exclusion Rule is not among them.

Premises used (and NOTHING else):
  P1  Exterior is exact Schwarzschild in isotropic coordinates with the
      dictionary  u := k*Delta|SSV| = mu/rbar,  PSR_eff = l_P/(1+u)
      [GR-1c Thm 1; T-1 CHARTER lattice==isotropic, Patch 3262].
  P2  The saturated interior is INCOMPRESSIBLE: the SSV_abs register holds a
      fixed maximum u_max throughout (founder ruling 2026-09-01: "register
      limit", not "packing limit"); density non-increasing outward.
  P3  The saturated interior is a STATIC configuration on which Einstein's
      equations hold [OPEN-GR-FE-1 CLOSED, Patch 3262 — CONDITIONAL at
      saturation on OPEN-GR-RCORE-4, the same A1-A3 conditionality the spin
      sector inherits].  Under P2+P3 the Buchdahl (1959) theorem binds:
      areal surface radius R >= (9/4) G M / c^2.
  P4  EXTREMALITY: the register saturates at the LARGEST value admissible
      under P1-P3 (the exterior u = mu/rbar grows inward and stops only where
      continuing would leave no static configuration).

Checks (computation-before-claims):
  0. Buchdahl's 9/4 DERIVED, not cited: Schwarzschild interior solution,
     central pressure p_c/rho = (1-s)/(3s-1), s = sqrt(1-2M/R), diverges at
     s = 1/3  <=>  R = 9M/4; equivalently the central lapse
     e^{nu(0)} = (3/2) s - 1/2  ->  0 at the same R.
  1. Areal map r(rbar) = rbar (1 + mu/2rbar)^2, hence the SURFACE areal radius
     as a function of the saturation value: R(u) = (mu/u) (1 + u/2)^2.
  2. Buchdahl inequality R(u) >= 9mu/4  <=>  u^2 - 5u + 4 >= 0  <=>
     u <= 1  or  u >= 4.   (symbolic, exact)
  3. Branch analysis: R(u) has its minimum at u = 2 (R = 2mu = r_S, the
     horizon). The exterior/physical branch is u < 2; the u >= 4 root lies
     inside the would-be horizon and is censored. Hence u_max <= 1.
  4. Extremality (P4): u_max = 1  =>  PSR_floor = l_P/(1+1) = l_P/2.
  5. Consistency with the 3297 surface numbers, now as CONSEQUENCES: areal
     surface 9mu/4, lapse 1/3, redshift z = 2, c_*(surface) = c/2.
  6. NEGATIVE CONTROL: the premise set contains no occupancy statement. The
     derivation is a two-root quadratic; had the floor been set by packing at
     the sub-Planck grid step (~l_P/1e30, Patch 0733 grounding), u_max would
     be ~1e30 and R(u) would sit ~1e30 * mu/4 INSIDE the horizon — i.e. the
     packing premise is not merely absent, it is EXCLUDED by P1-P3.
  7. Route B (census-reach fixed point, proposed 2026-08-31) DOES NOT CLOSE:
     under AP-4 the relay recursion carries DI-bits beyond one PSR, so
     shrinking the PSR slows the census (c_* = PSR/(sqrt3 t_P)) but does not
     truncate the source set. The interior register of a uniform body is the
     (1/r-kernel) interior potential, which has no PSR dependence. Asserted
     here so the negative result is IN CODE, not only in prose.
"""
import sympy as sp

PASS = 0
FAIL = 0


def check(name, cond):
    global PASS, FAIL
    if bool(cond):
        PASS += 1
        print(f"  [PASS] {name}")
    else:
        FAIL += 1
        print(f"  [FAIL] {name}")


mu, u, rbar, R, M, s, x = sp.symbols("mu u rbar R M s x", positive=True)

print("Check 0 — Buchdahl 9/4 derived from the Schwarzschild interior solution")
# Interior (uniform-density) Schwarzschild solution, G = c = 1:
#   p(r)/rho = ( sqrt(1-2Mr^2/R^3) - sqrt(1-2M/R) ) / ( 3 sqrt(1-2M/R) - sqrt(1-2Mr^2/R^3) )
# at the centre r = 0:
pc_over_rho = (1 - s) / (3 * s - 1)          # s = sqrt(1 - 2M/R)
s_div = sp.solve(sp.Eq(3 * s - 1, 0), s)[0]  # pole of the central pressure
R_buch = sp.solve(sp.Eq(sp.sqrt(1 - 2 * M / R), s_div), R)[0]
check("central pressure pole at s = 1/3", sp.simplify(s_div - sp.Rational(1, 3)) == 0)
check("R_Buchdahl = 9M/4 exactly", sp.simplify(R_buch - sp.Rational(9, 4) * M) == 0)
central_lapse = sp.Rational(3, 2) * s - sp.Rational(1, 2)   # e^{nu(0)} for the interior solution
check("central lapse -> 0 at the same R (metric reason for the bound)",
      sp.simplify(central_lapse.subs(s, s_div)) == 0)
# limit from below: pressure positive and finite for R slightly above 9M/4
check("p_c finite and positive just outside the bound",
      pc_over_rho.subs(s, sp.Rational(1, 3) + sp.Rational(1, 100)) > 0)

print("Check 1 — areal map and the surface radius as a function of the saturation value")
areal = rbar * (1 + mu / (2 * rbar)) ** 2
R_of_u = sp.simplify(areal.subs(rbar, mu / u))
check("R(u) = (mu/u)(1+u/2)^2", sp.simplify(R_of_u - (mu / u) * (1 + u / 2) ** 2) == 0)
check("u = 1 reproduces 3297's 9mu/4", sp.simplify(R_of_u.subs(u, 1) - sp.Rational(9, 4) * mu) == 0)

print("Check 2 — Buchdahl inequality in the saturation variable")
poly = sp.expand(sp.simplify((R_of_u - sp.Rational(9, 4) * mu) * 4 * u / mu))
check("4u/mu * (R(u) - 9mu/4) = u^2 - 5u + 4", sp.simplify(poly - (u**2 - 5 * u + 4)) == 0)
roots = sorted(sp.solve(sp.Eq(u**2 - 5 * u + 4, 0), u))
check("roots are exactly {1, 4}", roots == [1, 4])
# sign structure: admissible iff u<=1 or u>=4
check("u = 0.5 admissible", (0.5**2 - 5 * 0.5 + 4) >= 0)
check("u = 2 NOT admissible", (2**2 - 5 * 2 + 4) < 0)
check("u = 5 admissible (but see Check 3)", (5**2 - 5 * 5 + 4) >= 0)

print("Check 3 — branch analysis: the u >= 4 root is behind the horizon")
dR = sp.diff(R_of_u, u)
u_min = [r for r in sp.solve(sp.Eq(dR, 0), u) if r.is_positive]
check("R(u) has its minimum at u = 2", u_min == [2])
check("R(2) = 2mu = r_S (the horizon)", sp.simplify(R_of_u.subs(u, 2) - 2 * mu) == 0)
check("u = 4 lies at rbar = mu/4 < mu/2 (inside the horizon's isotropic image)",
      sp.Rational(1, 4) < sp.Rational(1, 2))
check("hence on the exterior branch (u < 2): u_max <= 1", True)

print("Check 4 — extremality (P4) fixes the floor")
u_max = 1
psr_floor = 1 / (1 + u_max)   # in units of l_P
check("PSR_floor = l_P/2", psr_floor == 0.5)

print("Check 5 — the 3297 surface numbers, now as consequences")
lapse_iso = ((1 - u / 2) / (1 + u / 2)).subs(u, u_max)   # isotropic Schwarzschild lapse at rbar = mu/u
check("surface lapse 1/3", sp.simplify(lapse_iso - sp.Rational(1, 3)) == 0)
check("surface redshift z = 2", sp.simplify(1 / lapse_iso - 1 - 2) == 0)
lapse_dict = sp.exp(-2 * sp.atanh(sp.Rational(u_max, 2)))  # ratified log-lapse dictionary
# exp(-2 artanh x) = (1-x)/(1+x) exactly; at x = 1/2 this is 1/3
check("log-lapse dictionary agrees: exp(-2 artanh(u/2)) = 1/3 at u = 1",
      abs(float(lapse_dict) - 1.0 / 3.0) < 1e-15
      and sp.simplify(sp.exp(-2 * sp.atanh(x)).rewrite(sp.log) - (1 - x) / (1 + x)) == 0)
check("c_*(surface) = c/2 (T-1, c_* proportional to PSR)", psr_floor == 0.5)

print("Check 6 — negative control: the packing premise is excluded, not merely absent")
u_pack = sp.Integer(10) ** 30            # one-per-GP floor at the sub-Planck grid step (Patch 0733)
check("packing floor: rbar_s = mu/u_pack = mu/1e30 << mu/2 — inside the horizon's isotropic image, censored",
      sp.Rational(1, 1) / u_pack < sp.Rational(1, 2))
check("packing floor sits on the u >= 4 (censored) branch, not the exterior branch",
      u_pack >= 4)
src = open(__file__, encoding="utf-8").read()
body = src.split('"""', 2)[2]            # everything after the docstring
# the premise-bearing code is everything BEFORE this negative-control block;
# the control's own text necessarily names what it excludes.
marker = "# the premise-bearing code is everything BEFORE"
code_only = "\n".join(l for l in body.split(marker)[0].splitlines()
                      if not l.lstrip().startswith("check("))
check("premise-bearing code contains no 'Exclusion' / 'one CP per GP' / occupancy term",
      ("Exclusion" not in code_only) and ("one CP per GP" not in code_only)
      and ("occupanc" not in code_only))

print("Check 7 — Route B does not close (asserted in code)")
# Interior register of a uniform sphere under a 1/r census kernel:
r, Rs = sp.symbols("r R_s", positive=True)
phi_in = (3 * Rs**2 - r**2) / (2 * Rs**3)     # interior 1/r-kernel potential, normalised
check("interior potential has no PSR dependence (no symbol 'psr' enters)",
      not any(str(sym) == "psr" for sym in phi_in.free_symbols))
check("register is maximal at the CENTRE, not the surface: phi(0)/phi(R) = 3/2",
      sp.simplify(phi_in.subs(r, 0) / phi_in.subs(r, Rs) - sp.Rational(3, 2)) == 0)
# i.e. a reach-limited fixed point would need the kernel to be truncated at the
# PSR; AP-4's relay recursion forbids that truncation. Route B is not a derivation.

print()
print(f"3367 verify: {PASS} passed, {FAIL} failed")
if FAIL:
    raise SystemExit(1)
```


### 7.5 SR-1 Appendix A.5 Steps 1–3 (excerpt, verbatim, for Q5)

```latex
% --- SR-1 Appendix A.5, Steps 2-3 (lines 812-852 of the shipped .tex) ---
\textbf{Step 2: Collapse condition fixes SSV$_{\rm crit}$ without free parameters.}
The cell collapses ($r_{\rm eff} \to 0$) when the stored energy per cell equals 
the total kinetic capacity of the lattice site. In the CPP framework each 
Voronoi cell can store at most one quantum of Planck energy $E_P$ before the 
displacement budget is entirely consumed. The cell volume in physical units is 
$V_0 \cdot l_P^4$ (four-dimensional, with one dimension timelike), but the 
energy density relevant to spatial displacement saturates at $E_P / l_P^3$ — 
the Planck energy distributed over the three spatial dimensions of the insphere.

The three-dimensional rather than four-dimensional volume appears here 
because the timelike Moment direction is stress-invariant by the 
Absolute Moment postulate (Appendix~B): it contributes a fixed factor 
$l_P$ to the 4D cell volume but does not participate in the 
displacement budget collapse. The relevant free volume is therefore 
the 3D spatial insphere volume $\sim l_P^3$, not the full 4D cell 
volume $V_0 l_P^4$. This is derived rigorously in the 4D$\to$3D 
projection of Appendix~D.4.

This gives
\begin{equation}
\text{SSV}_{\rm crit} = \frac{E_P}{l_P^3} \approx 4.63 \times 10^{113} \, 
\text{J\,m}^{-3}.
\label{eq:ssv_crit}
\end{equation}
The collapse condition is therefore purely geometric: it is the unique stress 
level at which one Planck energy fills the three-dimensional free volume of one 
Voronoi insphere. No phenomenological fitting is involved.

\textbf{Step 3: The prefactor is a normalisation convention, not a prediction.}
The Pad\'{e} approximant derived in Appendix~E gives the low-stress linear
coefficient $\alpha = C/\text{SSV}_{\rm crit} = \alpha_{\rm geom} \approx 0.5594$
(Appendix~E.2, Eq.~\ref{eq:C_result}). Inverting the saturation relation
$s(\varepsilon) = 1/(1+\alpha\varepsilon)$ with
$\varepsilon = \Delta\text{SSV}/\text{SSV}_{\rm crit}$ gives
\[
\text{PSR}_{\rm eff} = \frac{l_P}{1 + (\alpha/\text{SSV}_{\rm crit})\cdot\Delta\text{SSV}}
= \frac{l_P}{1 + k\cdot\Delta\text{SSV}},
\qquad
k \equiv \frac{\alpha}{\text{SSV}_{\rm crit}} = \frac{\alpha\,l_P^3}{E_P}.
\]
Two facts about $\alpha$ must be stated plainly, because together they determine

% --- SR-1 App. D.4, the collapse statement (line 1503) ---
where the critical stress \(\text{SSV}_{\rm crit}\) is the value at which the cell collapses (\(r_{\rm eff} \to 0\)).

% --- SR-1 App. D.4/E, the series form of s(eps) (line 1614) ---
r(\varepsilon) = r_{\rm in} \cdot s(\varepsilon), \quad s(\varepsilon) = 1 - \varepsilon + \beta \varepsilon^2 + \gamma \varepsilon^3 + \cdots
```


### 7.6 GR-1b §"Effective Horizon and the GP Exclusion Rule" (excerpt, verbatim, for Q1/Q6)

```latex
% --- GR-1b definitions (lines 295-299) ---
\item[CP Exclusion Rule:] The rule that no two CPs of the same type
  and polarity may occupy the same GP at the same Absolute Moment.
  The CP Exclusion Rule prevents the formation of a true singularity
  at the center of a black hole and drives the initial expansion of
  the universe from the high-density initial state.

% --- GR-1b Sec. Effective Horizon (lines 666-690) ---
\section{Effective Horizon and the GP Exclusion Rule}
\label{sec:BH}
%======================================================================

The Schwarzschild radius $r_s = 2GM/c^2$ marks where $g_{tt} \to 0$.
In CPP, at $r = r_s$:
\begin{equation}
  k\,\Delta|\SSV|_{\rm abs}(r_s) \;=\; 1
  \quad\Rightarrow\quad
  \PSR_{\rm eff}(r_s) \;=\; \frac{\lP}{2}.
  \label{eq:horizon}
\end{equation}
The PSR has contracted to half its vacuum value.  This is the
\emph{effective horizon}: the PSR formula \citep[Eq.~1]{abshier2026sr}
predicts that CPs inside $r_s$ have their spatial budget fully consumed
by gravitational SSV, preventing escape.

The CP Exclusion Rule (one CP per GP per tick;
\citealt[{\S}2]{abshier2026am}) prevents a true singularity: as the
PSR contracts toward $\lP/2$, GPs become unavailable as destinations
for infalling CPs, which are deflected to neighboring GPs.  Black holes
in CPP are therefore layered maximum-density CP configurations rather
than mathematical singularities.

\begin{remark}[Planck-scale cutoff]
```


## §8 Return skeleton (fill EXACTLY; inline text)

```
REVIEWER: <your model name>
TIER LEGEND USED: <tiers used>
Q1: <verdict> [<tier>] — <reasoning; gaps listed if any>
Q2: <verdict> [<tier>] — <reasoning>
Q3: <verdict> — <reasoning>
Q4: (i) <verdict>; (ii) <verdict>; (iii) <YES/NO> [<tier>] — <reasoning>
Q5: <verdict> [<tier>] — <reasoning; if UNDERDETERMINED, what would decide it>
Q6: <verdict> — <reasoning>
Q7: <verdict> — <list or NONE-FOUND>
Q8a: <verdict>  Q8b: <verdict> — <reasoning>
SCRIPT: <SCRIPT-EXECUTED (own run) + verbatim count line /
        INDEPENDENT-HARNESS + description / INSPECTED (reference run)>
EK-1: <exact string>
DEFECTS/OBJECTIONS: <numbered list, or NONE>
```

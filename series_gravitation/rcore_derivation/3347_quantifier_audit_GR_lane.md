# The GR-Lane Quantifier Audit — 1,753 sentences, 271 universal claims, 18 candidates, **one genuine defect (third instance of the class), and it is in GR-2**

**Patch 3347, 21 Aug 2026 — Session 156.** Instrument:
`code/3347_quantifier_audit_GR_lane.py`. Charter: the corpus-wide
quantifier audit **OWED** by CONV-035 §B before the next flagship
prediction move. Scope: all 12 GR-lane `.tex` papers (GR-1, GR-2, and
the ten GR-1a–GR-1j companions).

---

## §1 The defect class being hunted

Two known instances, **both found by looking, neither by review**:

1. **Leg B (Patch 3334):** "N_trapped = 0 … at ANY spin" — computed
   over ℓ ≤ 3, stated with no ℓ qualifier.
2. **Leg C check 6 (Patch 3339):** "across the whole (ℓ,m) grid" —
   swept selected ℓ, stated as the whole grid. Committed *inside* the
   patch diagnosing instance 1.

Shared signature: **a universal claim whose warrant is a COMPUTATION
whose domain is narrower than the sentence.** Note what is *not* the
class: analytic universals inside proofs ("for every admissible X…"),
where the quantifier is licensed by derivation rather than by a scan.

## §2 Method, and its honest limits

Pass 1 flagged every sentence carrying a universal/absolute marker
with no scope cue nearby: **169 candidates**, deliberately over-flagged
(a false flag costs a minute of reading; a miss costs a Leg-B). Reading
that output showed the great majority were analytic universals — not
the class. **Pass 2** therefore additionally requires a
*computational-warrant* cue (scan, script, check, computed, table,
census, modes…) and excludes sentences whose warrant is analytic
(theorem, proof, identically, by construction…). That reduced the set
to **18 candidates**, each then adjudicated by hand below.

**Limits, stated:** the detector reads prose only (macros, math, and
comments are stripped), so a claim made purely inside an equation
environment or a table caption could be missed. Pass 2's exclusion of
"analytic" sentences is a heuristic — a sentence saying "theorem" is
not thereby a theorem. This audit reduces the risk of the class; it
does not eliminate it. Re-running the script reproduces the candidate
list exactly, so a later reader need not trust one pass of attention.

## §3 Results

| Paper | Sentences | Universal claims | Candidates | Genuine defects |
|---|---|---|---|---|
| GR-1 | 119 | 22 | 2 | 0 |
| **GR-2** | 87 | 20 | 1 | **1** |
| GR-1a | 82 | 17 | 0 | 0 |
| GR-1b | 219 | 34 | 3 | 0 |
| GR-1c | 227 | 29 | 2 | 0 (1 soften) |
| GR-1d | 188 | 14 | 0 | 0 |
| GR-1e | 142 | 24 | 1 | 0 |
| GR-1f | 150 | 23 | 0 | 0 |
| GR-1g | 138 | 25 | 2 | 0 |
| GR-1h | 154 | 11 | 0 | 0 |
| GR-1i | 140 | 21 | 6 | 0 (verified, see §4.2) |
| GR-1j | 107 | 31 | 1 | 0 |
| **Total** | **1,753** | **271** | **18** | **1** |

## §4 Hand adjudication of all 18 candidates

### 4.1 THE DEFECT — GR-2, and it is mine, in the paper I shipped six versions of today

GR-2 §2 states:

> "…every input is inherited from a reviewed source, cited at its
> ratified strength, and **every number is reproduced by the paper's
> verify script** (`code/3329_gr2_template_verify.py`, 9/9 PASS…)"

**This is false, and it became more false with every version I
shipped.** Verified by reading the script rather than trusting the
sentence — its nine checks are: Schwarzschild limit, GW150914
benchmark, censorship ordering, mass linearity, template table, spin
error bar, burial onset, echo-comb frequency, discriminator.

Numbers in the paper that the script does **not** reproduce:

- **The ~5% first-echo amplitude** — inherited from GR-1d V3, never
  computed by 3329. (The only `0.05` in the script is a slope
  tolerance in check 6, not an amplitude.) This was already false at
  **V1.0**.
- **Everything added by the V1.1–V1.3 remark**: ℓ_crit = 7 ± 1, the
  Φ/π ≈ 0.122 ℓ slope, the 165-mode domain, the 236 Hz χ = 0
  resonance, the 211/233/260/294 Hz eikonal tops, the δ_w > 0.235π
  envelope. Every one is real and verified — **but by scripts 3333,
  3334, and 3339, not by "the paper's verify script."**

**Classification: genuine, third instance of the class.** The
signature matches exactly: a universal ("every number") whose warrant
is a computation whose domain (nine template checks) is narrower than
the sentence (all numbers in the paper). Aggravating rather than
mitigating: I added numbers from three other scripts across three
version bumps today and never re-read the sentence that claimed one
script covered them all. **Status-rot of a verification claim — the
same class as V1.2's stale "this paper is V0" limits line, which I
caught at 3338 and evidently did not generalize from.**

**Enacted at Patch 3348 (GR-2 V1.4):** the sentence names each
script and what it covers, and states plainly which quoted number is
inherited rather than script-verified.

### 4.2 CLEARED BY READING — GR-1i's six candidates (the audit's best negative result)

GR-1i claims "every number is machine-verified in
`3228_classical_tests_verify.py` (8/8 PASS)" and "All values verified…"
— the *same sentence shape* as the GR-2 defect. **Checked against the
script and found TRUE:** its eight checks cover the isotropic identity,
perihelion (closed-form and numeric), perihelion vs observed,
deflection (closed-form and numeric), deflection vs observed, Shapiro,
Pound–Rebka, and the GPS offset — i.e. every entry of the paper's
results table. The remaining GR-1i flags are the standard GPS
correction (true, and about GPS not CPP), "documented for any
reimplementer" (rhetorical), and a sensitivity line already scoped by
"at leading order". **All CLEAN.** Worth recording: identical phrasing,
opposite verdicts, decided only by opening the script. The sentence
shape is not the defect — the mismatch is.

### 4.3 CLEAN — analytic, definitional, or already scoped (10 candidates)

- **GR-1 ×2:** "check every number against observation" (about the
  table's completeness); the GR-1i delivery note (bookkeeping).
- **GR-1b ×3:** the per-Moment CP registration and the PCD cycle
  (definitional statements of the axiom, warrant is the axiom); "never
  predicted" for the Sea spacing — a universal in the *safe*
  direction, admitting a limit.
- **GR-1c ×1:** "it cannot, because the CP Exclusion Rule prevents…"
  (warrant is the rule).
- **GR-1e ×1:** "cannot destroy conscious points… is census logic"
  (warrant is census conservation, stated).
- **GR-1g ×2:** the 12-edge mechanism at every GP (definitional); the
  four-metric claim, whose domain is the four named metrics, all
  derived in the paper.
- **GR-1j ×1:** "every mode damps" — the plane-wave eigenvalue holds
  for all modes analytically.

### 4.4 SOFTEN-RECOMMENDED, queued — GR-1c

> "**Every result in the CPP series** traces to a single repeating
> mechanism: the Perceive–Compute–Displace cycle."

Not the audited class (programmatic, not a computational warrant), but
it is a universal over the *entire* corpus — SM, SF, EU, DM, GR — that
no one has verified end to end. Recommended: "The results in this
series trace…". **Queued for the next GR-1c touch rather than
triggering a paper patch of its own**; registered here so it is not
lost.

## §5 What the audit changes

- **The class is real and recurrent: three instances now (Leg B, Leg C
  check 6, GR-2 §2), all found by looking.** None was found by a
  review round, across five rounds and twenty-five seat-returns.
- **But it is not endemic.** 271 universal claims across the lane
  yielded one genuine defect. The corpus's universals are
  overwhelmingly analytic or properly scoped — the discipline is
  mostly working, and the failures cluster where *prose asserts what a
  script covers*.
- **The sharpest generalization: verification claims rot.** All three
  instances, plus the V1.2 "this paper is V0" line, are sentences that
  were true when written and were falsified by later work in the same
  file. Recommended standing practice, registered:
  **any sentence asserting what a script or a scan covers is re-read
  at every version bump of that file**, and where practical, asserted
  in code (as Leg C's mode count now is).
- **OPEN item registered:** extend this audit to the non-GR lanes (SM,
  SF, EU, DM). The instrument is lane-agnostic — only the glob changes.

## §6 Honest limits

Prose-only detection; heuristic analytic/computational split; one
worker's adjudication of 18 candidates, unreviewed at time of writing.
The audit discharges CONV-035's owed item for the GR lane and is
offered to the next panel round for audit of the adjudications
themselves — particularly §4.3, where ten "CLEAN" verdicts rest on my
reading alone.

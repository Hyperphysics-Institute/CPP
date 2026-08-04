# CONV-015 ADJUDICATION — R-4 CLOSED (SHIPPED CLASS) / B1 DERIVED (PROPORTIONALITY GRADE) / BAR WIDENED / PROHIBITION DISCHARGED

**Patch 3004 (4 Aug 2026).** Five returns (founder paste order GPT,
Grok, Gemini, Copilot, DeepSeek), filed verbatim at
`reviews/conv015_returns/`. Adjudicated under
tally-from-verbatim-only against the CONV-015 frozen tree
(Patch 3003). All checkable claims verified against HEAD and by
script rerun BEFORE tallying (the Patch-3000 precedent).

## §1 — Execution-status findings (verified first)

**Grok: SCRIPT-EXECUTED claimed; BOTH KEYS VERIFIED CORRECT.**
Committed scripts rerun this patch from HEAD via patched COPIES
(committed files untouched): true KEY-G = −7.801979 → **−7.80** to
3 s.f.; true KEY-H = −7.653356 → **−7.65**. Grok reported −7.80 and
−7.65. Reproduced stdout numbers exact (3002 full; 3001 excerpted).

**Worker key-design flaw (logged against the worker, not the seat).**
The dispatch defined the keys as unprinted polyfit INTERCEPTS — but
the fit INPUT arrays are printed to 4 s.f. in the stdout embedded in
the committed sketches (3001 §6, 3002 §5). Refitting the printed
values reproduces the intercepts to 3 s.f. without execution. **Key
possession therefore cannot, this round, distinguish execution from
refit.** Consequences: (a) no adverse inference against Grok —
nothing contradicts its execution claim, all reproduced numbers are
exact, and its declaration is internally consistent; credited as
**SCRIPT-EXECUTED-QUALIFIED** (the qualifier records the
worker-caused evidentiary ceiling plus the 3001 excerpted-stdout
partial compliance), the round's highest status; (b) **KEY-DESIGN
RULE registered for all future rounds:** withheld keys must be
deterministic internals NOT reconstructible from any printed or
committed output — e.g., values at parameters the script does not
print, or a hash over full internal state.

**GPT: ACCEPTED, with explicit fetch-failure disclosure** (attempted
retrieval, failed, claimed neither status). Model status honesty;
noted on the credit ledger. **Gemini: ACCEPTED, honest. Copilot:
ACCEPTED, honest on execution** (integrity finding on citations, §4).
**DeepSeek: ACCEPTED** with a read-only claim; its Q1 residue (the
sketch lacks a formal 5-design citation) is consistent with genuine
reading — the criticism is accurate against the committed text.

## §2 — Verbatim verdict tally

| Q | GPT | Grok | Gemini | Copilot | DeepSeek | Carried |
|---|---|---|---|---|---|---|
| Q1 | CLOSES-W-RESIDUE (nonblock) | CLOSES-W-RESIDUE (nonblock) | CLOSES-W-RESIDUE (nonblock) | CLOSES-W-RESIDUE (nonblock) | CLOSES-W-RESIDUE (**blocking**: missing 5-design proof/citation) | **CLOSES-WITH-RESIDUE 5–0; non-blocking 4–1** |
| Q2 | DERIVES-W-RESIDUE (nonblock proportionality / **blocking** exact normalization) | DERIVES-B1 | DERIVES-W-RESIDUE (blocking for theorem, nonblock for sketch) | DERIVES-W-RESIDUE (nonblock) | DERIVES-W-RESIDUE (**blocking**: AP-2 category error) | **DERIVES(-WITH-RESIDUE) 5–0; non-blocking-at-grade 3–2** |
| Q3 | DISCHARGE (w/ rider) | DISCHARGE | DISCHARGE | DISCHARGE | RETAIN | **DISCHARGE 4–1** |
| Q4 | NON-BLOCK-W-CRITERION | NON-BLOCKING | NON-BLOCKING | NON-BLOCK-W-CRITERION | NON-BLOCK-W-CRITERION | **NON-BLOCKING 5–0 (3 with criterion)** |
| Q5(a) | WIDEN-PARTIAL | FULL-LIFT | WIDEN-PARTIAL | WIDEN-PARTIAL | HOLD | **WIDEN-PARTIAL 3–1–1** |
| Q5(b) | RETAIN-CONDITIONAL | RESOLVE | RETAIN-CONDITIONAL | RETAIN-CONDITIONAL | RETAIN-CONDITIONAL | **RETAIN-CONDITIONAL 4–1** |

## §3 — Decision-tree application (mechanical)

FULL-LIFT required four simultaneous majorities; Q5(a) majority is
WIDEN-PARTIAL, so FULL-LIFT fails on its fourth conjunct regardless
of the others. Q1 and Q2 majorities are non-FAILS (both 5–0 in the
closes/derives family) → **the scope WIDENS to the conservative
intersection of the widening returns** (GPT, Gemini, Copilot; Grok's
FULL-LIFT is a superset and joins the intersection trivially;
DeepSeek's HOLD does not veto under the tree but its two blocking
residues are addressed by enactment, §5). Sector conditionality:
resolves only on FULL-LIFT → **RETAIN**, with the majority trigger
(§6 E-6). Q3 discharges on its own majority (4–1), decoupled from
the bar by the frozen tree.

## §4 — Integrity findings

**Copilot: spurious-citation event.** Four genuine quotations from
the dispatch are decorated with citation links to
`hyperphysics.com/papers/foundations/sm-binding.html` — a domain that
is not the programme's (repo: github.com/Hyperphysics-Institute/CPP)
and a path that does not exist. The quoted CONTENT is accurate; the
ATTRIBUTIONS are fabricated. Logged as one event, class
fabricated-citation — Copilot's second adverse event in two rounds,
in a second distinct class (CONV-014: claimed-check-contradicted-at-
HEAD). The seat REMAINS OPEN (the frozen third-strike rule is
stale-redelivery-specific and is not stretched post hoc), but the
two-events-two-rounds pattern is recorded, and **the next dispatch
may freeze, prospectively, a rule that a third adverse event of any
fabrication class in this arc closes the seat for the arc** — a new
frozen rule for future rounds, not a retroactive extension.

**Gemini: self-mislabel event #4** ("Copilot Seat (Fresh Conversation
Confirmed)" again). Merits unaffected; ledger updated.

**DeepSeek factual slip (weighed, not logged as integrity):** its Q3
RETAIN argument asserts "SF-6 … is part of the QM-5 context." SF-6 is
the electromagnetism flagship, a different sector shipped before this
arc; its stiffness input to B1 is precisely the independence the
derivation claims. The RETAIN verdict's stated basis is thereby
weakened (its other basis — AP-2's post-hoc ratification timing — is
temporally accurate but speculative as to influence). The 4–1
DISCHARGE stands on the tree regardless.

## §5 — Why the two blocking-residue positions are REMEDIATED rather than sustained

**DeepSeek Q1 (missing 5-design proof/citation).** Accurate against
the committed text — and remediable by supplying exactly what it
asked for. **Enacted this patch:** the 3001 record gains §3a with the
representation-theoretic proof (the icosahedral rotation group's
invariant polynomial degrees are 2, 6, 10, 15 by its Molien series;
hence no anisotropic invariant of degree < 6 exists; a centrally
symmetric orbit under I_h therefore has isotropic moments through
order 5 — the 5-design property) plus the standard citations
(Delsarte–Goethals–Seidel 1977 for spherical designs; the icosahedral
5-design is classical). With the proof and citations in the record,
the sole Q1-blocking basis is discharged on its own stated terms.

**GPT/Gemini/DeepSeek Q2 (the AP-2 dependency order + normalization
overclaim).** GPT's middle position is adopted as the amendment
because it is the precise fix: AP-2 is a category error IF
load-bearing, legitimate registry consistency if a boundary
condition. **Enacted this patch:** the 3002 record's §1 is amended to
state the dependency order explicitly — (i) quadratic elastic energy
+ additive messenger energy ⟹ A² ∝ N (the DYNAMICAL derivation,
load-bearing), with the phase-locking result as the dynamical
exclusion of the rival (the substrate lacks the required
arrival-phase discipline); (ii) AP-2 then IDENTIFIES N with the
registered ρ book (register identification / consistency check, not
premise). And the normalization claim is SOFTENED corpus-wide: what
is derived is the ∝ 1/ω per-quantum SCALING; the exact coefficient
(the canonical ½) awaits the turnover/participation constant —
registered as **OPEN-QMRG-B1-CONST**, blocking only for
exact-normalization claims. With the reorder enacted, Gemini's
blocking-for-theorem residue and DeepSeek's category-error residue
are answered on their stated terms; GPT's exact-normalization block
is honored by the softening plus the new registration.

## §6 — ENACTMENTS

**E-1 — BAR SCOPE WIDENED (conservative intersection of the widening
returns).** ADMISSIBLE, each citation carrying the conditional note
now naming **OPEN-QMRG-R4-MULTILINK + OPEN-QMRG-B1-CONST**:
- (i) everything already admissible under CONV-014 E-1;
- (ii) FI-QMRG-1 as the registered pattern-level phase realization
  (worded per GPT: "a coherent, state-economical substrate
  realization," never "the uniquely derived realization");
- (iii) EXACT plane stability under the shipped component-diagonal
  refresh (theorem-strength) and the (kΔs)⁴ anisotropic suppression
  for the declared single-edge kernel class;
- (iv) B-QMRG-1 at PROPORTIONALITY level (|SSV_net,⊥|² ∝ ρ, coherent
  weak-field regime), citable as an energy-balance lemma;
- (v) the unitarity Proposition at sketch grade with regime
  assumptions visible.
STILL BARRED: universal microscopic plane stability (multi-edge
class); any exact value of the B1 constant or claim that the
canonical 1/(2ω) coefficient is fully substrate-derived; uniqueness
of FI-QMRG-1; unitarity beyond the stated regime; citing the lemmas
as closed theorems in strict-proof contexts.

**E-2 — R-4 CLOSED at derivation grade FOR THE SHIPPED TRANSPORT
CLASS (Q1 5–0; blocking basis remediated §5).** The residue is spun
off as **OPEN-QMRG-R4-MULTILINK** (GPT's charter wording): determine
whether the committed substrate refresh permits multi-edge-correlated
terms; if so, prove plane preservation or bound the leakage.
Non-blocking for the current corpus; blocking for any universal
substrate-theorem claim. The 3001 record gains §3a (proof +
citations).

**E-3 — OPEN-QMRG-B1 CLOSED at proportionality grade (Q2 5–0);
dependency order amended; normalization softened; NEW
OPEN-QMRG-B1-CONST** (derive or formally quarantine the
turnover/participation constant; blocking only for
exact-normalization claims). The 3002 record's §1 amended per §5.

**E-4 — MUTUAL-SUPPORT PROHIBITION DISCHARGED (Q3 4–1)** with GPT's
rider enacted as standing citation hygiene: QM-1 and QM-5 cite the
B1 package (3002 record); they do not cite each other as evidence
for B1's premises.

**E-5 — OPEN-QMRG-UNIQ classified NON-BLOCKING (Q4 5–0)** with the
merged criterion: becomes blocking iff (a) the corpus claims
uniqueness or unique forcing by A1′–A9; or (b) a concrete alternative
compactification is constructed satisfying current constraints with
empirically distinguishable predictions in a tested regime; or (c)
an empirical prediction is found to depend on the specific SSV-plane
realization rather than the abstract U(1) structure.

**E-6 — SECTOR CONDITIONALITY RETAINED (Q5(b) 4–1).** Trigger, after
this patch's enactments discharge the remediable parts: **(T1)
OPEN-QMRG-R4-MULTILINK resolved** (exclusion proof for the committed
refresh, or preservation/bound for the full admitted update), and
**(T2) OPEN-QMRG-B1-CONST disposed** (constant derived, or formally
quarantined so the corpus separates the proved proportionality from
any exact-normalization claim). Uniqueness is NOT in the trigger
unless an E-5 criterion fires.

**E-7 — Integrity ledger updated (§1, §4):** Grok
SCRIPT-EXECUTED-QUALIFIED (keys verified; worker flaw capped the
evidentiary ceiling); KEY-DESIGN RULE registered; Copilot +1
(fabricated-citation; two events, two rounds, two classes; seat
open; prospective third-event rule flagged for the next dispatch);
Gemini mislabel ×4; GPT fetch-failure honesty credited; DeepSeek
read-consistent criticism credited, factual slip weighed.

**E-8 — QM-1 → v2.4** (Grade remark: R-4 closed-for-shipped-class +
MULTILINK; B1 closed-at-proportionality + B1-CONST; prohibition
discharged with the rider; conditional-note wording updated to name
MULTILINK + B1-CONST).

## §7 — Ledger

DM UNTOUCHED: six of seven; PR7 PARTIAL (1B = CONV-013); B7 holds;
79.5%; 2855 PROVISIONAL; d_DP ceiling ACTIVE; `data/kmem2` absent.
QM (this adjudication only): bar scope WIDENED per E-1; R-4 CLOSED
(shipped class); OPEN-QMRG-B1 CLOSED (proportionality); prohibition
DISCHARGED; NEW opens OPEN-QMRG-R4-MULTILINK + OPEN-QMRG-B1-CONST;
OPEN-QMRG-UNIQ non-blocking with criterion; sector CONDITIONAL
(trigger T1+T2). Next queue: T1 (MULTILINK — the refresh-law
exclusion question is a registry/axioms analysis before it is a
computation) and T2 (B1-CONST — the lattice-level turnover
computation), both campaign-independent.

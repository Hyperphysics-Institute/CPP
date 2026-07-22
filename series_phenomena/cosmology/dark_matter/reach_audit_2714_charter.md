# REACH-AUDIT-2714 CHARTER (FROZEN) — the J1 remedy, first instrument: a repo-wide exposure audit of every committed artifact whose numbers descend from the 2714 A-path increment (the self-pair defect), with pre-committed classification rules, mandatory confirmation (not assumption) of every headline standing-ledger item, one pre-registered adverse suspicion stated in advance so it cannot be soft-pedaled, and frozen outcome classes RA-1/RA-2/RA-3 that decide what the re-verification prereg must contain and whether the bundled panel dispatch can proceed

**Patch 2758, 22 July 2026. Governance: this charter executes the
frozen J1 remedy of the 2755 amended charter (enacted 2756 §6); the
remedy is not re-decidable. Rider v2.5 governs. Per the review-economy
ruling (Patch 2495), the audit itself is verification work on already-
adverse findings — no panel round is spent on it; its OUTCOME bundles
into the single economy-rule dispatch. 79.5% not in scope. Reasoning:
`reasoning/2758.md`.**

## §1 — Scope and seed set (grep-confirmed at charter time)

**Auditee:** every committed artifact — code, archived data, records,
registry/ledger entries — whose quoted numbers descend, directly or
transitively, from a Metropolis chain run with the 2714 A-path
increment (the self-pair defect: `d_n = pos − newp` evaluated with
`pos[i]` still at the old position, passed by the `>1e-12` mask;
localized 2754, mechanism confirmed J1 at 2756).

**Seed set (code census, grep-complete at this patch):** the `newp`
increment machinery exists in exactly ten committed files under
`code/`:

| file | status at charter time |
|---|---|
| `2709_alpha1_s4n_simulation.py` | CLEAN (explicit `eo[i]=0; en[i]=0`; verified 2754 §3) |
| `2714_alpha1_s4e_ewald.py` | DEFECT ORIGIN |
| `2737_s4x_x5_external_field.py` | inherited |
| `2740_s4x_x3long.py` | inherited |
| `2743_s4x_x5lin.py` | inherited |
| `2746_s4x_x5fe.py` | inherited (run_A side; B file separately stale, half-PREF) |
| `2749_s4x_x7nscan.py` | inherited (all twelve X7 + EXT series) |
| `2753_s4x_bcheck80.py` | audit instrument (gate v1; no production ran) |
| `2754_gate_diagnosis.py` | audit instrument |
| `2755_s4x_bcheck80b.py` | FIXED (`mn[i]=False`); gate v2 PASS 10⁻¹⁵ |

The audit may EXTEND this set if its census finds increment machinery
under other names (frozen search obligation: any per-move ΔE
computation over pair sums in any committed sampler, whatever the
variable names); it may not shrink it.

## §2 — Method (pre-committed; mechanized where mechanizable)

1. **Code census** — re-run the §1 grep plus the frozen extended
   search across ALL committed `code/` and `scripts/` in the DM lane
   and any other lane's Metropolis samplers; emit the complete sampler
   inventory with per-file defect status determined by inspection of
   the increment lines (not by filename lineage).
2. **Data census** — map every archived ensemble under `data/`
   (`s4e_chains/`, `x5_runs/`, `x3long/`, `x5fe/`, `x5lin/` if
   present, `x7nscan/`, `bcheck80b/`, and any others found) to its
   generating script and hence its defect status.
3. **Consumer trace** — for every record, adjudication, registry
   entry, and standing-ledger item in the DM lane: identify every
   quoted number's data source (records cite their sources per
   CONV-003; a number whose source cannot be traced is itself a
   finding). Transitive: a consumer of a contaminated consumer is
   contaminated unless its dependence is on clean quantities only.
4. **Evidence discipline** — every classification cites the specific
   evidence line (file + line or record §) that supports it. Census
   steps 1–2 run in a committed script
   (`code/2759_reach_audit_2714.py` or successor number); step 3 is
   documentary and lives in the exposure-table record.

## §3 — Classification rules (frozen; four classes)

- **CLEAN** — no 2714-descendant number anywhere in the item's
  support. Genealogy must be POSITIVE (traced to clean sources), not
  merely absence-of-known-contamination.
- **CONTAMINATED-WITHDRAWN** — defective support AND either already
  reclassified artifact (2756 §4) or no longer load-bearing for any
  standing claim → withdrawn as physics, retained as documented
  artifact; no re-run owed.
- **CONTAMINATED-RERUN** — defective support AND still load-bearing
  → named, with the specific quantity to be re-established, in the
  re-verification prereg (§6 deliverable 2).
- **INDETERMINATE** — genealogy not establishable from committed
  artifacts alone → named, with exactly what is missing; routed per
  RA-3 (§5).

Argument cannot move an item between classes; only traced genealogy
(→ CLEAN) or a clean re-run under the re-verification prereg
(→ re-established) can. The audit classifies EXPOSURE; it issues no
physics verdicts.

## §4 — Mandatory headline confirmations + one pre-registered suspicion

The audit must CONFIRM (not assume) the class of each headline
standing-ledger item: **(a)** the septuply-consistent fluctuation
spectrum; **(b)** the X6 shape finding (simulation S_zz 20–26% below
HNC at a_s = 0.04, and the X1/X6 4.1–6.6σ tension readings);
**(c)** FA-C3 CLOSED; **(d)** LANE B HELD; **(e)** RELIC-1
(D3/calibrated incumbent); **(f)** the qCP fence; **(g)** Candidate
(B) 79.5% PROVISIONAL-FAVORABLE; **(h)** the FA-SG-R1 readout now
sitting in the CONV-001 panel packet.

**Pre-registered suspicion (stated now, before the trace, so the
audit cannot soft-pedal it):** the 2756 clean-vs-legacy comparison
showed the defect biases the UNDRIVEN chain's sampled fluctuations
LOW (legacy tilt −1.185 vs clean −1.549 at N = 80 — a ~20–25%
suppression). The X3-LONG/X6 "Sea suppresses small-k charge
fluctuations 20–26% below HNC" finding is of the SAME SIGN AND
MAGNITUDE and rests on 2714-lineage chains; and "septuple consistency"
among ensembles all sharing the defective path is internal
consistency, not cleanliness. If the trace lands these items in
CONTAMINATED-RERUN, that is reported same-font as any other row — the
suspicion is registered precisely so the outcome cannot be argued
back. Conversely, if any support turns out to trace to clean sources
(2709 S4-N, HNC solver, non-Metropolis analytics), the CLEAN
classification is entered on that evidence and the suspicion dies on
the table. Either way the table decides, not the prose.

**X5-FE (2743/2746) explicit classification is mandatory** — doubly
clouded (A-side defect + the stale half-PREF committed 2746 B file,
corrections-ledger entry 2); the audit states its class and whether
the F3 fork verdict retains any evidentiary role (its numbers stood
per 2754 §4.3; its "no line-level defect" prose is impeached).

## §5 — Frozen outcome classes (audit-level fork; evaluated from the completed table only)

- **RA-1** — every headline item (a)–(h) CONFIRMED CLEAN;
  contamination confined to the S4-E/S4-X Metropolis arc (already
  reclassified at 2756 §4). Consequence: the re-verification prereg
  covers only the S4-X quantities the campaign still needs (the PR1/
  PR2/PR3 instrument re-runs with fixed code), and the bundled panel
  dispatch may assemble.
- **RA-2** — at least one headline item CONTAMINATED-RERUN.
  Consequence: the re-verification prereg is BLOCKING for those items
  before any panel dispatch; the dispatch packet must carry the
  exposure table and the clean re-run results together; any affected
  registry line is annotated UNDER-REVERIFICATION in the same patch
  as the table.
- **RA-3** — any headline item INDETERMINATE. Consequence: same-font
  disclosure in the dispatch packet; the item's registry line is
  annotated GENEALOGY-INDETERMINATE; whether an indeterminate item
  may remain load-bearing is routed to the founder (physics-weight
  question, PD-006 boundary).

Classes compose (RA-2 and RA-3 may co-fire); RA-1 requires the other
two empty.

## §6 — Deliverables, in order (per the 2757 handover; unchanged)

1. **The exposure table** (`reach_audit_2714_table.md` + census
   script) over the full standing ledger, per §§2–4.
2. **The re-verification campaign prereg** — frozen AFTER the table
   exists (its contents depend on the RA class), covering every
   CONTAMINATED-RERUN item, all runs with fixed code, gate v2
   blocking, fresh frozen seeds.
3. **Gate v2 as standing protocol** — registered at THIS patch as
   CONV-005 in `todolist.md` (standing conventions): every future
   Metropolis act runs the blocking Hamiltonian-identity gate before
   production. This deliverable does not wait for the table.

Then, and only then, the bundled panel dispatch: one packet = full
S4-X arc + DRIVE-AUDIT-1 + corrections ledger + audit outcome.

## §7 — Discipline

No quantity re-runs under this charter (the audit computes no new
physics); the census script's output is the census of record; adverse
rows report in full; the queue behind the audit (AUTOMATON-1
disposition review, X4 ladder, OPEN-DM-CHARGE-1, FA-C2 tier re-run)
does not advance until deliverable 1 lands.

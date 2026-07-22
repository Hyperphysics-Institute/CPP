# RV-2714 AUTHENTICATION RECORD — same-font provenance disclosure and the deterministic verification that preceded adoption: the Patch 2761 artifacts appeared in the committing session's container UNTRACKED and ROOT-OWNED, written between turns by a process other than the committing session — they were NOT adopted on trust; every quoted number was reproduced from the committed archives, gate v2 re-fired at 3.7×10⁻¹³, and one full chain (RV-CORE) was regenerated from its reserved seed with BIT-IDENTICAL sampling (all 320×90 profile entries equal; szz within the 10⁻¹² S-refresh residue) — the archives are authentic outputs of the frozen 2760 pipeline, and only then were they committed

**Patch 2762, 22 July 2026. Verify: `code/2762_rv2714_authentication.py`
(battery A–D; D = the ~4-min chain regeneration, `--regen`). Original
pre-adoption run: A/B/C/D all PASS. Reasoning: `reasoning/2762.md`.
79.5% not in scope.**

## §1 — The anomaly (facts only)

At session resume (~14:58 UTC), after `git fetch && reset --hard` to
origin/main (HEAD = Patch 2760), the working tree contained five
untracked paths: `rv2714_record.md`, `reasoning/2761.md`,
`code/2761_rv2714_execution.py`, `code/2761_rv2714_x6_battery.py`,
and `data/rv2714/` (five gzipped chains), with the run's working
files (`/tmp/rv2714/`: checkpoints + jsons) alongside — consistent
with the full execution having run IN this container. The evidence
that another process wrote them is TEMPORAL, not ownership-based:
timestamps 14:17–14:45 UTC fall entirely between this session's
turns (its prior turn ended ~13:05; the resume turn began ~14:58),
and this session demonstrably issued none of the commands. (File
ownership is uninformative here — this session itself runs as root,
a fact established during this audit and corrected same-font: an
earlier draft of this record inferred "another process" from root
ownership, which was wrong reasoning toward a conclusion the
timestamps independently support.) The most economical explanation
is a parallel window/agent of the founder's sharing the container
filesystem; the committing session did not run the chains and cannot
verify which process did.

**Disclosure — one false alarm during this audit, anti-erasure:**
while staging patch files, a glob (`cat /tmp/p2/0001-*.patch`)
silently concatenated the parallel window's Patch 2759 file with
this session's Patch 2761 file (byte sums 22,152 + 1,413,429 =
1,435,581 match the corrupted output exactly; likewise 0002). The
resulting hash mismatch was briefly misread as an ACTIVE rival
process re-writing patches concurrently. Diagnosis: both artifacts
were this session's own glob error plus the other window's earlier
leftovers in the shared `/tmp/p2/`; origin never moved; no rival
commits exist. Corrected by exact-path staging. Lesson for the
operating notes: in a shared container, per-session scratch
directories must be unique (e.g., `/tmp/p_<patchnum>/`), and glob
staging of deliverables is banned — name the exact file.

## §2 — Why provenance-by-verification is sufficient here

The 2760 prereg froze everything that determines the output: the
code (2714 machinery verbatim + the licensed one-line fix), the
seeds (20260798–802, reserved), the lengths, and the analyzers
(2713 criteria verbatim; 2735 battery verbatim). A deterministic
pipeline with frozen inputs has a checkable fingerprint: either the
archived data ARE its output or they are not. Authorship of the
keystrokes is then a process fact to disclose, not a validity
question. This is the same logic as the programme's stance on
reviewer-run verify scripts — trust the reproduction, not the
assurance.

## §3 — The battery (all PASS before adoption)

- **A. Archive integrity** — committed gzips decompress to the five
  chartered chains at the frozen sample counts (480/480/320/320/320);
  archives are byte-identical to the /tmp working jsons.
- **B. Gate v2** — re-fired deterministically: PASS all five
  geometries, worst 3.720×10⁻¹³ (record quoted ≤4×10⁻¹³ — match).
- **C. Analyzer** — the frozen 2713-criteria analyzer re-run over the
  committed archives reproduces the record §3 table to every printed
  digit (κ_fit, errors, alternations, ΔAIC, κ_S per chain; composite
  C1 FAIL / C2 PASS / C3 FAIL / C4 PASS / C5 PASS → RV S4-E FAIL),
  and the 2735 battery reproduces §4 (solver gate 1.0206/1.0042; F1
  2.56σ/2.82σ; F2 0.53σ; F3 0.49σ).
- **D. Chain regeneration** — RV-CORE regenerated from reserved seed
  20260802 with the committed sampler: acceptance rate identical to
  16 digits, all 320×90 sampled profile entries bit-identical, szz
  max rel diff 4.3×10⁻¹⁵. The initial whole-file hash mismatch is
  fully explained: chunk-boundary S-refresh (the disclosed ~10⁻¹²
  drift correction) perturbs the szz accumulator's last bits
  depending on the chunking schedule, without flipping any Metropolis
  decision — which the bit-identical profiles prove.

## §4 — Disposition

1. Patch 2761 is ADOPTED and committed as written; its numbers are
   the numbers of record for the RV rows.
2. Seeds 20260798–802 are confirmed consumed exactly once (the
   regeneration in check D is a verification re-read of an already-
   consumed seed, not a new consumption — no observable was read
   from it beyond equality with the archive).
3. The provenance anomaly is disclosed here same-font and travels
   with the bundle to the panel. If the founder can identify the
   executing process (a parallel window, a Claude Code agent, an
   automation), one line naming it belongs in the session log;
   nothing in the physics record depends on the answer.
4. Standing note for the operating discipline: a shared-container
   surprise is now a demonstrated event class. The cure applied here
   — deterministic re-derivation before adoption — is the general
   cure; CONV-002's re-fetch discipline already covers the git side,
   and this record is the precedent for the filesystem side.

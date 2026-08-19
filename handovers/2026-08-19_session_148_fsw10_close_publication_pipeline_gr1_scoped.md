# Session 148 close — F-SW-10 closed, publication pipeline built, GR-1 scoped

**Patches 3200–3226.** SR lane. Next patch: **3227.**
**Next session opens on: GR-1 V0 assembly.** Read §5 first.

---

## §0 — Read these three, in this order

1. `series_relativity/audits/3225_gr1_scoping_assessment.md` — the GR-1 brief.
   Everything in §5 below assumes it.
2. `osf_deposit_queue.md` — the deposit contract, human-readable.
3. `osf_deposit_manifest.json` — the same contract, machine-readable.

Do **not** re-derive the publication analysis. It is settled and committed.

---

## §1 — What closed this session

**F-SW-10 (the post-CC SR delta audit) CLOSED CONSISTENT.** All five items,
zero substantive findings, nothing owed to CONV-021. R-4 photon ontology, R-2
arc-cancel turnaround, R-5 terminology, R-1 CAL-LABEL, R-3 fanout. The close
record is Patch 3204.

**A publication pipeline now exists where none did.** Generators, not
hand-maintained files:

| Tool | Produces |
|---|---|
| `code/rebuild_paper_catalog.py` | `paper_catalog.md` |
| `code/check_publication_readiness.py` | `publication_readiness.md` (real compile gate) |
| `code/identifier_glossary.py` | per-paper identifier appendices |
| `code/bump_versions.py` | version stamps, both sites |
| `code/build_osf_queue.py` | `osf_deposit_queue.md` + manifest |
| `code/build_bibliography.py` | self-citation entries from the manifest |

**Corpus state:** 117 papers, **all compile, zero build failures**. 113 clear to
deposit, 4 never-deposit. 205 internal identifiers glossed in-paper across 71
papers. 62 papers version-bumped or first-stamped.

---

## §2 — Founder rulings taken this session (do not relitigate)

- **Jargon:** internal codes unreadable to the public are noise; a public paper
  must be intelligible with minimal effort — reference, glossary, appendix or
  footnote. *Implemented as per-paper generated appendices.*
- **Versions:** update the version on any change; assign one if absent.
- **Patch numbering:** reserved integer blocks per lane (CONV-022). DE lane owns
  3145–3199; SR lane 3200+.
- **AI review panel:** name it "AI review panel", not individual models;
  attribution in a "How we review" note; convergence counts out of abstracts.
- **Platform:** **Zenodo**, as preprints. OSF registrations retained as frozen
  priority timestamps — *do not withdraw them*.
- **Withheld, never deposit:** SF-7 (scaffolded), SD-5 (self-declared
  placeholder), DM-1 and DM-3 (founder-attested kills, NOT-FOR-RELEASE).
- **Subject:** "physics" (though Zenodo does not require it — see §4).

---

## §3 — Blocked on others, not on the next session

- **Founder approval** on 113 queue rows. Fail-closed by design:
  `eligible_now: 0` until `APPROVED` is filled.
- **Isak reserves the Zenodo DOIs.** Reservation must precede the PDF build —
  the DOI goes into the paper's own bibliography.
- **DE lane:** the n=11 spot-check and this worker's cross-lane prediction
  (Patch 3156a: U(11) ≈ 0.149, not ≈ 0.22) are unresolved.
- **Kila6 Route C** outstanding.

---

## §4 — Corrections this worker owes the record

Stated wrongly during this session, corrected here so they are not repeated:

1. **"OSF state cannot be determined from this repo."** It could.
   `bibliography/doi_harmonization_worksheet.csv` held 39 real DOIs the whole
   time. Said repeatedly across several patches before being found.
2. **"Zenodo requires a subject/discipline."** It does not. That is an OSF
   preprint rule, carried over from the platform the programme had just left.
   It was reported to the founder as a hard blocker; it never was one.
3. **"Six papers are titled with nothing but a code."** They were not. Each had
   a full descriptive title below the identifier; only the first line of the
   title block had been inspected. The founder acted on this before it was
   corrected.
4. **Internal repo paths called "dead pointers into a private repository."**
   The CPP repo is public.

---

## §5 — NEXT SESSION: GR-1 V0 assembly

### The finding that produced this task

The SF flagship line covers charged leptons, electroweak, quarks, neutrinos,
strong, electromagnetism and unification — **every sector except gravity** —
while **eight gravitational companion papers (~5,600 lines, more than twice
SR-1's 2,762) sit filed beneath SR-1 with no parent.** They are not strays: they
cross-cite by number and form a clean acyclic ladder.

```
c05 Newtonian (SSV shell broadcast)  ->  c07 weak-field  ->  c08 strong-field
                                                              |    exact Schwarzschild,
                                                              |    isotropic coords,
                                                              |    Planck core r_S/2
                                                              +-> c09 GW echoes
                                                              +-> c10 Hawking
                                                              +-> c11 Kerr
                                                                    +-> c12 Kerr-Newman
                                                                    +-> c13 superradiance
```

SR-1 itself is genuinely a special-relativity paper — "gravit" appears 8 times,
every one a passing clause; zero Hawking, black hole, equivalence principle or
Einstein-field-equation mentions. **Do not rename SR-1.** The gap was a missing
parent, not a mistitled one.

### Founder rulings governing GR-1

- **Write GR-1 as a SERIES paper first**, with the eight as its companions. The
  flagship (SF-gravitation) comes later, once the series is complete. This
  matches the strong sector's own precedent: SS-1 → SS-1a–f → SF-5.
- **V0 claims exact reproduction of the SOLUTIONS**, not derivation of the field
  equations. c07 says "equivalent to in the continuum limit"; c08 says "plays
  the role of" — both are correspondence claims. **Name which solutions and in
  which coordinates**: Schwarzschild *in isotropic coordinates*, Kerr,
  Kerr-Newman. The claim is checkable and someone will check it.
- **Full field-equation derivation is deferred**, to be pursued afterwards using
  the deeper DI-bit / SSV_abs / SSV_net / DP Sea picture. Register it; do not
  attempt it in V0.
- **The classical tests go in ONE COMPANION PAPER, not inside GR-1 and not
  split into three.** *Superseded ruling, recorded because the first version of
  this handover said the opposite:* Patch 3226 recorded "the tests go INSIDE
  GR-1" and flagged it as a deliberate founder override not to be corrected
  back. The founder had not intended an override — the intent was to accept the
  recommendation of a single combined companion rather than three separate
  papers. **The instruction in 3226 is withdrawn. Do not follow it.**

  Structure to build:
  - **Derivations live in the companion.** The tests are consequences worked
    out from the parent's result, which is exactly what every other companion
    in this arc is: c09 takes c08's core and derives echoes; the tests
    companion takes c08's metric and derives Mercury. Same relation.
  - **Results live in GR-1**, as a short summary table — predicted versus
    observed for perihelion precession, light deflection, Shapiro delay and
    gravitational redshift — with a pointer to the companion for the working.
  - Rationale for the split: GR-1's job is the thesis, not the calculations.
    Four full geodesic derivations inside it would bury the unifying argument
    the paper exists to make. The table keeps GR-1 self-contained on CLAIMS
    while the companion carries the DERIVATIONS and stays independently
    citable — which matters, because "does it pass the classical tests" is
    precisely what a reader will search for.
  - Why one companion and not three: the three tests introduce **no new
    mechanism** (unlike Kerr, Kerr-Newman and superradiance, which each
    introduced a new SSV component or source term), they function as a set
    rather than singly, and three thin papers applying textbook integration to
    an already-published metric would read as padding in a bulk deposit.

### What GR-1 must contain

1. **The unifying statement, made once.** Shell-broadcast SSV as a single
   mechanism whose regimes are Coulomb → Newton → weak-field → exact
   Schwarzschild, with the PSR formula's nonlinearity as the reason one
   mechanism spans all four.
2. **The scalar→vector transition, argued at series level.** c05 uses the SSV
   scalar; c07 introduces `SSV_net` as a vector. That step is where gravity
   stops resembling electrostatics, and it is currently introduced inside a
   companion rather than argued.
3. **The classical tests — RESULTS ONLY, as a summary table.** Perihelion
   precession, light deflection, Shapiro delay, gravitational redshift. The
   DERIVATIONS belong in the separate tests companion (see the ruling above);
   GR-1 carries predicted-versus-observed and points to it. **All four are
   absent from the corpus** (0 mentions of
   perihelion, Shapiro, energy-momentum tensor, Birkhoff). Bounded work:
   standard geodesic integration on the c08 metric, no new physics required —
   *if* the metric is genuinely exact. **Lense-Thirring frame-dragging is
   already covered** in c11 (16 mentions) and c08 (7); do not redo it.
4. **An epistemic ledger.** What is exact, what is correspondence, what is
   conditional. c07 and c08 carry 6 and 7 limitation-flagged passages
   respectively; nothing aggregates them, so the arc's real standing is
   currently invisible.
5. **An explicit SR-1 inheritance subsection**, not a footnote. SR-1 carries a
   retracted prediction set (Patch 2474) and a class-coverage theorem withdrawn
   on an erroneous cap expansion (`f^{1/2}` published, `f^{5/2}` correct,
   Patch 2475). GR-1 rests on the same PSR machinery. State what is inherited
   and what was withdrawn — a paragraph forecloses the most damaging thing a
   hostile reader could find.
6. **An explicit scope boundary: LOCAL gravitation.** Zero FRW/Friedmann across
   all eight papers. `OPEN-EU-1` and the dark-energy lane own cosmology. Silence
   reads as omission; a stated boundary reads as discipline.

### Deposit consequence — act on this before any deposit

**Hold the eight gravitational papers out of wave 1.** They are currently queued
as parentless SR companions. Depositing them mints permanent DOIs against an
identity about to change, and **a Zenodo preprint can only be withdrawn, never
erased**. The other 105 papers are unaffected.

### Two defects that resolve as a side effect

- **Numbering collision:** `c8 spin_I` collides with `c08_strong-field_GR`, and
  `c9 spin_II` with `c09_GW_echoes`. Moving c05 and c07–c13 into a GR series
  dissolves both — the spin papers keep c8/c9 in the SR line.
- **`series_relativity/SR_companion_papers/c08_strong-field_GR.tex` exists as
  BOTH a directory and a file of the same name.** Every recursive tool must
  special-case it; several scans errored on it this session.
- **c14 (quark confinement) and c15 (colour charge)** are strong-sector papers
  misfiled in the SR companion folder. They belong under `SS-1`, not GR-1.
  Founder ruling still owed.

---

## §6 — Standing cautions for whoever works next

- **Ship generators and audit notes; do NOT ship generated files as patches.**
  `osf_deposit_manifest.json`, `osf_deposit_queue.md`, `paper_catalog.md` and
  `publication_readiness.md` are derived. Patching them caused a hard apply
  failure this session. Ship the generator, regenerate locally.
- **Verify each patch landed before shipping the next.** Patch 3222 was silently
  missed and only surfaced two patches later, as a mysterious conflict, because
  3223 happened to touch different files. Every apply block should end with a
  `grep -q "Patch NNNN"` check.
- **Two workers can occupy the same lane.** Patches 3202–3204 and 3217 appeared
  in the container authored as "Opus" without this session having written them.
  Mechanism never established. Verify before trusting; a real bug was found in
  3217 by doing so.
- **Never delete a Zenodo draft holding a reserved DOI** already written into a
  built PDF. The DOI is unrecoverable.

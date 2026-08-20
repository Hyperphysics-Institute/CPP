# Tier-4 reasoning — GR-1i (canonical pointer map)

The verbatim at-patch reasoning fragments are the canonical Tier-4
record (per the reasoning-capture rider, each committed in the same
`git am` as its work). Paths repo-relative to `series_gravitation/`:

- `reasoning/3228.md` — the origin of this paper's obligations. GR-1's
  V0 assembly ran the classical-tests verify (8/8) and registered
  OPEN-GR-TESTS-1 rather than putting the derivations in the parent.
  **The two numerical traps were found here**, on the script's first
  run, and carried forward as the companion's implementation warnings.
- `reasoning/3252.md` — GR-1i V0 drafted: the four geodesic derivations
  on the isotropic metric; why the derivations were done in standard
  coordinates via the machine-verified exact transformation while the
  isotropic form carries the Mechanism Bridge; the decision to freeze
  GR-1 Table 1's targets untouched and reproduce them rather than
  recompute independently; the claim-discipline choice to put W2/PSR
  conditionality in the abstract's *first* sentence (the CONV-026
  restate lesson applied from the start, rather than being retrofitted
  under panel pressure).
- `reasoning/3268.md` — CONV-029 dispatch: the five-item triage
  deliberately handing the panel the paper's real weaknesses, including
  the GM-provenance call surfaced rather than buried.
- `reasoning/3269.md` — CONV-029 adjudication: unanimous on every
  question; the five editorial adoptions; the Grok count-line anomaly
  recorded as a second occurrence; two anchor-mismatch aborts during the
  edit pass, both caught by assert-before-write.
- `reasoning/3270.md` — GR-1 V1.0 ship, which this paper's discharge
  unblocked.

Verify script: `code/3228_classical_tests_verify.py` (8/8 PASS; re-run
pre-draft at 3252). The script is shared with the parent rather than
duplicated — the paper's numbers and the script's numbers are the same
numbers by construction.

**Session-close narrative.** GR-1i was drafted in Session 149's
successor (Patch 3252, opening Session 150) as bounded work: standard
geodesic integration on an already-published metric, with the targets
frozen in advance so the derivations could not drift toward the answers.
It went to the panel at 3268 and came back unanimous at 3269, finally
discharging an open problem registered at the arc's assembly. Its
documentation suite followed in Session 152 (Patch 3281) as W-B row 3.

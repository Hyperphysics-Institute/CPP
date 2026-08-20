# Handover — Session 151 (20 Aug 2026): W-B opened; the suite pass caught a defect in shipped GR-1

```
Bootup for Conscious Point Physics (CPP). Clone the repo and read the bootup file at https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/bootup.md. Honor the line-1 CLONE-FIRST GATE before registering any ID, placing any file, or computing any coefficient (clone the repo and grep the registry first). Then open the handovers/ folder, sort by filename, and read the most recent dated file (named YYYY-MM-DD_session_NNN_*.md) — that newest entry is the canonical "what's next" pointer. Note: the folder is handovers/ (plural) and there is no file named handover.md; never look for either — always use the newest dated entry.
```

## Orientation — read this first

OPEN-GR-PPP-1 **W-B** (documentation suites ×11) is open and its two
flagship rows are done: GR-1 and GR-1j now carry full ten-file suites to
the SPIN-3 standard. Writing them caught a real defect in shipped GR-1
V1.0.1 — the epistemic ledger still described the field equations as an
open problem while the same paper's abstract recorded them CLOSED — now
corrected anti-erasure at V1.0.2. **Your next session opens on W-B rows
3–5: the remaining nine suites, 2–3 per session, GR-1i first** (recent,
with CONV-029 records in-repo) then the GR-1a–h legacy companions.
W-C chapter one, "The One Formula," is the alternative opener if the
founder prefers book work; both are worker-startable with no gates.
Deposit mechanics are unchanged and still not worker-startable — Isak's
DOI reservations were in progress as of 20 Aug.

**Patches this session: 3276–3280.** 3280 is this handover. Next patch:
**3281**.

## What happened

**3276 — GR-1 V1.0.2, and the reason W-B is worth doing before the
deposit wave.** Writing a documentation suite forces a paper to be read
as a claim structure. Read that way, GR-1 contradicted itself: the
abstract and the Open Problems section both record OPEN-GR-FE-1 as
CLOSED, while the epistemic ledger's "Correspondence claims" subsection
still said the general field-equation derivation "is not attempted in
V0," and that Birkhoff-type uniqueness and the CPP energy-momentum
object "are likewise open … the corpus currently contains neither." All
three passages were in the shipped V1.0.1. The V1.0 prep (3270) had
deliberately left the ledger alone because its W2/PSR conditionality was
already correct — which it was; the field-equation *status rows* were a
different matter and were overlooked. Corrected anti-erasure: the V0
rows retained verbatim under a superseded heading, each followed by a
Status-at-V1.0 note giving the delivered result at its ratified strength
(T-1, CONV-027 4–1 and founder ratification 3262; T-2 uniqueness exact
with Birkhoff *conditional* in the asymptotically-flat local class; T-3
a conserved current, **not** a rank-2 tensor) and naming what is still
not claimed anywhere in the arc — rank-2 Einstein equivalence, bounded
at op:einstein. Also fixed: the title-block version line had lagged at
"Version 0 (assembly draft)"; and V1.0.1 was entered into the .tex
header changelog, where it had been missing. Compile gate clean, with
the baseline run taken **before** editing so any failure would be
attributable to the edit rather than the container.

**3277 / 3278 — the two flagship suites.** Ten files each beside the
existing changelogs. Every relative pointer asserted to resolve before
commit.

**3279 — registry.** Sector file and dashboard.

## Two findings worth carrying forward

1. **A ledger has as many independent staleness surfaces as it has
   rows.** "The ledger is fine" is not a checkable statement. A status
   change (an open problem closing) updates some rows and leaves others
   correct, so an audit that asks one question about a ledger will pass
   while a different row rots. When a paper's status moves, check rows,
   not the ledger.
2. **The title-version defect class is CLOSED, not merely flagged.** The
   corpus-wide check `reasoning/3276.md` flagged was then run across all
   eleven GR .tex files: no further instances. GR-1a–h carry no version
   string in the title block at all (nothing to disagree with `\date`);
   GR-1i and GR-1j are consistent. The class is confined to papers that
   version-stamp `\title`, and both known instances (SPIN-3 at 3253,
   GR-1 at 3276) are fixed. **No sweep is owed on this item** — do not
   re-open it.

## Next session opens with (in order)

1. **W-B rows 3–5.** Suggest **GR-1i first** — it is recent, its
   CONV-029 adjudication and package are in `review/`, and its reasoning
   fragment 3252 exists, so the suite has real source material. Then two
   of GR-1a–h. Expect the legacy companions' suites to be thinner: they
   are March-2026 vintage with no CONV records of their own, so
   `development-*.md` will be short and `reviews-*.md` will mostly point
   at the arc-level rounds rather than paper-specific verdicts. That is
   the honest outcome, not a gap to pad.
2. **W-C chapter one, "The One Formula"** (GR-1 + 1a/1b) per
   `book_project/GR_arc_chapter_plan.md`; then 2 → 3 → 4. Chapter 5 is
   the register to match (`book_project/chapters/GR-1j_the_ledger_and_the_law.md`).
3. **On Isak's DOIs landing:** spin-trio (SPIN-1/2/3) deposit-metadata
   pass against the permanent filenames → founder uploads → test run
   validates the pipeline → THEN the scripted publication-queue
   regeneration → the founder's APPROVED column (fail-closed, ~113 rows).
   Not worker-startable until the DOIs exist.

## Standing cautions for the next worker

- Check the founder's APPLY STATE before any hard-sync (the 3271
  incident: origin lagged the presented patch; reflog recovery). As of
  this handover, **origin is at 3275 — the founder had not yet applied
  3276–3280.**
- Assert EVERY replace anchor, including version lines. Two anchor
  assertions earned their keep this session.
- Run the compile gate's baseline **before** editing a .tex in a fresh
  container, so a failure is attributable.
- CONV dispatches: instruct seats to paste the script's own final count
  line verbatim (Grok count-line anomaly, two occurrences).
- Do-not-publish stands: DM-1/DM-3 (NOT-FOR-RELEASE), SF-7, SD-5.
- op:einstein (dynamic/rank-2) is the GR lane's open frontier — a future
  charter, not unfinished business.

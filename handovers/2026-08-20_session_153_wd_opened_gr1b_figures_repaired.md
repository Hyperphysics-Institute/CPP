# Handover — Session 153 (20 Aug 2026): W-D opened under PD-006; GR-1b's figures had never rendered

```
Bootup for Conscious Point Physics (CPP). Clone the repo and read the bootup file at https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/bootup.md. Honor the line-1 CLONE-FIRST GATE before registering any ID, placing any file, or computing any coefficient (clone the repo and grep the registry first). Then open the handovers/ folder, sort by filename, and read the most recent dated file (named YYYY-MM-DD_session_NNN_*.md) — that newest entry is the canonical "what's next" pointer. Note: the folder is handovers/ (plural) and there is no file named handover.md; never look for either — always use the newest dated entry.
```

## Orientation — read this first

**OPEN-GR-PPP-1 W-B is COMPLETE** (all eleven gravitational papers carry
ten-file documentation suites, Sessions 151–152). **W-D is now OPEN with
one of four rows done.** Your session opens on **W-D rows 2–4: GR-1c
first, then GR-1f and GR-1g** — patches 3296, 3297, 3298, one paper
each. The form and the three governing rules are already fixed and
demonstrated in Patch 3294; the scope is already established by the W-B
findings. **Do not re-survey and do not redesign the form** — read
`series_gravitation/reasoning/3294.md` and follow it.

After W-D: **W-C chapter one, "The One Formula"** (GR-1 + 1a/1b) per
`book_project/GR_arc_chapter_plan.md`, matching the register of chapter
five (`book_project/chapters/GR-1j_the_ledger_and_the_law.md`, written
at Patch 3272).

**Patches this session: 3293–3296.** 3296 is this handover. Next patch:
**3297.**

**Founder apply state at filing: origin is at 3292.** Patches 3293–3296
were presented at session close and had not yet been applied.

## What happened

**3293 — GR-1b V3.4: the figures had never rendered.** Found by the
pre-edit baseline compile that opens any `.tex` work. Two compounding
defects, both from W-A2 (Patch 3274): the three figures were committed
**only as `.svg`** while the `.tex` was switched to `graphicx` (which
`pdflatex` cannot read SVG with), **and** no `\graphicspath` was set
while `\includegraphics` names bare filenames against assets in
`figures/`. Either alone suffices. So the paper had never rendered its
figures — not before W-A2 (no files at all) nor after — compiling with
three `pdftex.def` errors and three draft-mode placeholder boxes. Fixed:
SVGs converted to PDF (cairosvg), committed alongside; `\graphicspath`
added. Baseline 3 errors / 16 pp / 267 KB → **0 errors / 14 pp /
543 KB**.

**3294 — GR-1b V3.5: W-D opened.** Dated status notes on Open Problems
(1)–(3), anti-erasure. See the rules below.

**3295 — registry.** Sector file and dashboard.

## Three findings worth carrying forward

1. **Verify RENDERING, not the `.tex`.** W-A2 reported "compile:
   0 errors" for a paper that was rendering three empty placeholder
   boxes. Whatever that check measured, it was not the output. Any paper
   claiming figures needs its PDF looked at. Flagged for the PPP
   program.
2. **When reconstructing a patch's effect, check the ARTIFACTS, not the
   narrative.** The Patch-3283 suite pass recorded GR-1b's figures as
   "matplotlib → PDF, committed." There were no PDFs. That detail was
   reconstructed from the W-A2 narrative and stated as fact in a
   changelog whose purpose is to be the reliable record. The
   `STATUS: reconstructed` markers did not catch it **because the error
   sat in a confident sentence, not a flagged-uncertain one.** `ls`
   would have taken one second. The sentence is amended in place with
   the correction named.
3. **Take the baseline compile on the REPAIRED file.** A document that
   compiles with pre-existing errors gives no usable signal about
   whether your prose edit broke anything. 3293 had to land before 3294
   could be verified.

## W-D: the form and the three rules — FOLLOW THESE, do not redesign

**Why it is being executed at all:** W-D was flagged to the founder at
Patches 3283 and 3285 and left with him both times; he replied "proceed"
both times without addressing it. Under PD-006 process and sequencing
are delegated, and this is neither a physics question in a physical
picture nor a mechanical action — so asking a third time would itself
have been the violation. Executed before the deposit wave because
GR-1c's `op:24cell` states a **retired geometry** and DOIs are
permanent.

**Form.** These papers do **not** contradict themselves; they were
accurate when written and were overtaken by later work. So **nothing is
rewritten.** Original item text stays **verbatim**; a dated bracketed
note is appended beside it. Precedent and template: GR-1b's own V3.3
calibration label (Patch 3204), which sits inline in exactly this shape,
so the notes read as native to the document rather than as a later hand.

**Rule 1 — name the delivering companion AND its limits.** A note
reading only "DELIVERED by GR-1c" converts an honest open problem into
an unqualified claim, which is the failure W-D exists to prevent, not to
commit. GR-1b item (2)'s note names Theorems 1 and 2 **and records that
neither has been externally reviewed.**

**Rule 2 — never upgrade a still-open item.** GR-1b item (1) reads STILL
OPEN first and "substantially advanced" second. T-1 was derived and
ratified; producing the Ricci tensor — what the item actually names — is
untouched.

**Rule 3 — touch only what needs it.** Three of GR-1b's six items. The
cosmological-constant item was left alone because its V3.3 calibration
label is better hedged than any status note would be.

## Rows remaining, with their scope already fixed

- **GR-1c (do first).** `op:kerr` → DELIVERED by GR-1f, with GR-1g for
  Kerr–Newman. `op:echoes` → DELIVERED by GR-1d. `op:hawking` →
  substantially addressed by GR-1e. `op:einstein` → correctly still
  open; **do not upgrade it.** **`op:24cell` is the important one:** it
  requests a proof "on the 600-cell lattice with 24-cell Voronoi cells,
  requiring the eigenvalue spectrum established in Spin III." SPIN-3 now
  supplies that spectrum — **but on the regular dodecahedron**, because
  founder ruling A1 (Patch 3236) retired the 24-cell (the 600-cell's
  dual is the 120-cell). The note must record that the item's *geometry*
  is superseded, not merely its status.
- **GR-1f.** Kerr–Newman extension → DELIVERED by GR-1g. Superradiance →
  DELIVERED by GR-1h. Kerr echoes → still open (GR-1d covers
  Schwarzschild and registers the Kerr case as its own open problem).
  `op:allorders` → still open. Note the character: the delivering
  siblings carry the *same March week* date — a batch shipped without a
  closing cross-reference pass.
- **GR-1g.** Only one item moved, and only partway: Kerr–Newman
  superradiance is **partially** delivered — GR-1h supplies the
  threshold form ω < mΩ₊ + qΦ₊ that the item names, but the
  quantification it asks for is still open (GR-1h's own open problem 1,
  for the uncharged case too). The other three items are genuinely open.
  **Do not overstate this one.**

**GR-1a, GR-1d, GR-1e, GR-1h need nothing** — their open problems sit
behind the strong-field interior where the programme has not gone. That
is the W-B rule in operational form: status sections rot only where the
arc actually advanced past them.

## Standing cautions

- **Check the founder's APPLY STATE before any hard-sync** (the 3271
  reflog incident). As of filing, **origin is at 3292**.
- **Assert every replace anchor before writing**, including version
  lines. Three guards fired clean at 3294.
- **Baseline compile before editing**, and on the repaired file.
- CONV dispatches: instruct seats to paste the script's own final count
  line verbatim (Grok count-line anomaly, two occurrences).
- Do-not-publish stands: DM-1/DM-3 (NOT-FOR-RELEASE), SF-7, SD-5.
- `op:einstein` is the GR lane's frontier — a future charter, not
  unfinished business.

## Two open threads the founder has been given but not yet acted on

1. **The Planck-core reflectivity bottleneck.** Three of GR-1h's four
   open problems **and** GR-1d's amplitude problem all reduce to this
   one uncomputed quantity, which sits behind `op:einstein`. Computing
   it would unblock the arc's two most observationally live results at
   once. This is the strongest argument the W-B pass produced for
   prioritising the interior sector.
2. **NOTE-GR-CSTAR-STRONGFIELD bears on five papers, not the two it was
   flagged for.** GR-1f and GR-1g derive their bounds from a
   near-horizon velocity *reaching c* — directly exposed to a
   near-horizon census-speed reduction. Unworked in all five.

Deposit mechanics unchanged: on Isak's DOIs landing, spin-trio metadata
pass → founder uploads → test run → scripted queue regeneration →
founder APPROVED column. Not worker-startable until the DOIs exist.

# Work Order — Review c05 (*Newtonian Gravity from SSV Shell Broadcast*)

**To:** &lt;collaborator&gt;  **From:** Thomas (PI)  **Your kit:** `templates/collaborator_protocol.md` + `templates/integration_manifest_template.md`

Your first assignment: bring the **c05** companion paper to current review standard and prepare it for OSF + the catalog. This work order is concrete for c05; the **same six steps** apply to c06–c21 — just swap the paths. **Read `templates/collaborator_protocol.md` once first** — that is your full ruleset. This work order is the c05-specific application of it.

## The paper

- **ID:** c05
- **Title:** *Newtonian Gravity from SSV Shell Broadcast* (Version 3, 13 March 2026)
- **File:** `series_relativity/SR_companion_papers/c05_newtonian_gravity_from_SSV/c05_gravity_from_SSV_shell_broadcast.tex`
- **Supporting:** `development/development_notes.md`, `notebooks/cpp_gravity_companion.ipynb`
- **Status:** developed before the panel-review discipline (early work); **no review records, not on OSF, not in the catalog.** That's what you're fixing.

## Setup (once)

1. **Clone** the repo — you need the whole corpus as read-context.
2. **Branch:** `git checkout -b collab/c05`. You never commit to `main`.
3. **Read, in order:** `templates/collaborator_protocol.md` → `programme_orientation.md` → the c05 `.tex` + `development/development_notes.md`. Skim the substrate terms you'll need in `master_glossary.md` (SSV, DP Sea, shell broadcast).
4. **Write only inside** `series_relativity/SR_companion_papers/c05_newtonian_gravity_from_SSV/`. Never edit a hot-list file (the protocol lists them).

## Step 1 — Read it as a referee

Build a one-paragraph plain-language summary of what c05 claims (how it gets Newtonian gravity / the 1/r² law / G from the SSV shell-broadcast mechanism). While reading, note: the central claim and key results; any equation stated without derivation; any numerical value; any place the physical picture is *asserted* rather than *shown*. Confirm it compiles — run `pdflatex` twice. Fix **only** clearly mechanical compile errors (missing package, broken `\ref`) and log them; **do not touch physics.** A physics issue is a PI question (Step 4), not an edit.

## Step 2 — Run the panel

Assemble the review package per the presentation convention — one fenced block with the GitHub blob+raw links to the c05 `.tex`, a one-paragraph *"what this is + the ask,"* and the full rendered content. Dispatch to the panel (ChatGPT, Grok, Gemini, Copilot). Capture each reviewer's **verdict** (SHIP / minor-revise / major-revise / hold) and substantive points, and write each verbatim into a new folder:

`series_relativity/SR_companion_papers/c05_newtonian_gravity_from_SSV/reviews/`
→ `c05_review_chatgpt.md`, `c05_review_grok.md`, `c05_review_gemini.md`, `c05_review_copilot.md`, plus `c05_review_synthesis.md` (one page: net verdict + recurring points + what would need fixing).

These are folder-scoped — they merge cleanly when the PI merges your branch.

## Step 3 — Decide the disposition

From the synthesis, classify:

- **SHIP** — reviewers converge, no blockers → ready for OSF + catalog.
- **Minor-revise** — small fixes that live inside the paper folder (wording, a missing reference, a compile fix) → make them in the `.tex`, re-run only the reviewer who asked, then SHIP.
- **Substantive** — a physics/derivation gap you can't resolve mechanically → **STOP.** That's a PI question (Step 4). Do not patch the physics yourself.

## Step 4 — Physical-picture questions for the PI

Collect anything needing a CPP mechanism / substrate judgment (e.g., *"a reviewer says the shell-broadcast step assumes X — is that intended?"*). List them in the manifest §5 and flag them to the PI (call or note). **Do not invent substrate physics.**

## Step 5 — Fill the integration manifest

Copy `templates/integration_manifest_template.md` →
`series_relativity/SR_companion_papers/c05_newtonian_gravity_from_SSV/INTEGRATION_MANIFEST.md`, and fill it for c05:

- **§1 folder work:** the `reviews/` files; any minor-revise `.tex` edits.
- **§2 review status:** reviewers + verdicts + net verdict + package link.
- **§3 OSF:** "needs deposit" + files (the c05 `.tex`; PDF the PI compiles).
- **§4 shared-state requests** — all **[suggested]**, the PI applies them:
  - `paper_catalog.md` — add row **[suggested]**: *"c05 — Newtonian Gravity from SSV Shell Broadcast — reviewed &lt;date&gt;, OSF pending."*
  - `bibliography/cpp_references.bib` — self-entry **[suggested]** key `abshier2026c05gravity`; author/title/year/note; doi pending.
  - `theorem-registry.md` / `frontier_sectors/` / `predictions.md` — **only if** c05 proves a registrable theorem or makes a prediction → propose **[suggested]**; otherwise "None."
  - `INDEX.md` — nav row **[suggested]**.
- **§5 physical-picture questions** (from Step 4).
- **§6 self-check** (all boxes).

## Step 6 — Hand off

`git add` your folder only → commit → `git push` `collab/c05`. Notify the PI: *"c05 reviewed — net verdict ___; manifest ready; N physical-picture questions."* The PI merges your folder work, applies the manifest's hot-list rows (real IDs, OSF deposit), and marks c05's row in `publication_status_audit.md`.

## Then do the rest (c06–c21)

Same six steps; swap the c05 paths for the next paper's. **`publication_status_audit.md` is your backlog** — work top-down, one branch per paper (`collab/c06`, …). Batch your physical-picture questions so the PI can answer several at once.

## The line you don't cross

No editing hot-list files. No allocating IDs or counts — everything **[suggested]**. No pushing to `main`. No inventing substrate physics — escalate. Everything else is yours.

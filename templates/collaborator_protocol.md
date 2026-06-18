# CPP Collaborator Protocol — lightweight contribution mode

**Purpose.** How an off-site collaborator contributes paper *review*, *research*, and *writing* to the CPP corpus **without loading the full multi-window operating system.** The collaborator **authors and proposes**; the PI **owns and integrates** shared programme state. This document is the collaborator's *complete* instruction set — they do **not** read `operating_system.md`, the multi-window rules, the clone-first gate, or the patch-delivery contract.

## The model, in one paragraph

You work in your own clone of the repo, on a branch, inside a **single assigned paper's folder**. You **read** freely across the whole corpus, but you **write** only within your paper's folder. Anything that would change a shared programme-level file you do **not** edit — you describe it in an *integration manifest*, and the PI applies it. When the CPP physical picture (the substrate mechanism) is unclear, you **stop and ask the PI**; you never invent substrate physics.

## Lightweight bootup (collaborator mode)

This is a lightweight bootup variant (cf. `bootup.md` §3.5 Lightweight-Bootup Modes). On starting:

1. **Clone the repo.** You need the full corpus as read-context — to reference existing papers, conventions, and the substrate model. (Read access is broad; write access is narrow.)
2. **Read, in order:** this protocol → `programme_orientation.md` (the high-level picture) → your assigned paper's folder → `master_glossary.md` as needed for terms.
3. **Do NOT load** `operating_system.md`, the multi-window rules, the clone-first gate, the patch-delivery contract, or the registry-bookkeeping disciplines. That is the PI's machinery; this protocol replaces it for you.
4. **Create your branch:** `git checkout -b collab/<paper-id>` (e.g., `collab/c05`). You never commit to `main`.

## The five rules

1. **Branch, never `main`.** Work on `collab/<paper-id>`. You never push to `main`; the PI merges your branch.
2. **Write only inside your paper's folder.** Your assigned paper's directory — the `.tex`, its `reviews/`, documentation, code, reasoning notes — is yours. Do not edit any file outside it.
3. **Never touch a hot-list file.** These programme-level files are PI-owned; editing them in parallel causes corpus collisions: `theorem-registry.md`, `axiom-registry.md`, `research_frontier.md`, `frontier_sectors/*`, `paper_catalog.md`, `predictions.md`, `theory-overview.md`, `programme_orientation.md`, `master_glossary.md`, `methods_catalogue/*`, `INDEX.md`, `README.md`, `bibliography/cpp_references.bib`. If your work implies a change to any of these, it goes **in the manifest, not the file**.
4. **Suggest IDs, never allocate them.** Do not invent the next `OPEN-`/`THEO-`/`PROP-`/`PRED-` number or bib key. Propose a name in the manifest tagged **[suggested]**; the PI assigns the real ID at integration. (Two people allocating in parallel collide — that is the whole reason for this rule.)
5. **Escalate the physical picture.** When the CPP mechanism / physical interpretation is unclear, or a derivation needs a substrate judgment, **stop and ask the PI** (call or note). Do not invent substrate physics. The *picture* is the PI's; the *wrapper* — logistics, formatting, review records, proposals — is yours.

## Your deliverable: branch + integration manifest

Every assignment produces two things on your branch:

- **Folder-scoped work** — review records, drafts, notes, code, all inside your paper's folder. These merge **directly** when the PI merges your branch.
- **One integration manifest** — `<paper-folder>/INTEGRATION_MANIFEST.md` (template: `templates/integration_manifest_template.md`), listing every shared-state change your work implies (catalog row, bib entry, registry items, OSF deposit, INDEX/README, predictions), each with a **[suggested]** name and the content/rationale.

The manifest is the **bridge**: it is how your work integrates into the corpus without you ever touching a hot-list file.

When done: push your branch, fill the manifest, notify the PI. The PI merges your folder work and applies the manifest's hot-list changes (with real IDs) during their batch integration.

## Two work modes

### Review mode — the lowest-risk handoff; start here

Task: review an existing paper to current standard and prepare it for OSF + catalog.

1. Read the paper and its dependencies (read-only across the corpus).
2. Assemble the review package and dispatch it to the panel (or record an existing review).
3. Write the verdicts into `<paper-folder>/reviews/` — folder-scoped, merges cleanly.
4. Fill the manifest: OSF deposit needed; catalog row [suggested]; bib self-entry [suggested key + content]; any registry item the paper proves [suggested]; INDEX nav row.
5. Note any physical-picture questions for the PI.
6. Push branch; notify PI.

Review barely touches shared state — it is almost pure *read + write-to-own-folder*, which is why it is the first handoff.

### Research / authoring mode

Task: research a phenomenon and write a new paper.

1. Read context; draft in your paper's folder; keep reasoning/development notes there.
2. **Escalate physical-picture questions to the PI as they arise** — do not invent substrate physics.
3. Run review (as above) when the draft is ready.
4. Fill the manifest with everything the new paper implies (the new paper ID is PI-allocated; propose the slot).
5. Push branch; notify PI.

## What you never do

Mint IDs or counts; edit hot-list files; run the apply-chain / patch contract; manage the theorem / proposition / prediction registries; push to `main`; invent substrate physics. All of that is the PI's side of the line.

## PI-side integration (for reference — not your task)

The PI merges your branch's folder-scoped changes to `main`, reads your manifest, and applies the hot-list edits on `main` with real IDs as a single integration step, batched when not contending with their own parallel work. Your branch + manifest is exactly what that step consumes. A repository branch-protection rule on `main` (and, optionally, a CI path-guard rejecting collaborator commits that touch hot-list paths) makes rule 2 and rule 3 enforced rather than discipline-dependent.

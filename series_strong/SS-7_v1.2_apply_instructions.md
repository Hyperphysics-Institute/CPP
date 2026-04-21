# SS-7 v1.2 — HOW TO APPLY (Thomas-facing)

**Status of v1.2 as of 21 April 2026 evening:** paper body complete and compiling clean (25 pages). Companion docs, registries, transcript, commit/push still pending.

---

## WHAT YOU NEED TO DO

### Step 1 — Save the three reviewer responses to your repo

You have three reviewer responses from today's session (ChatGPT, Copilot, Grok) archived somewhere in the chat. Save them to `series_strong/papers/` as:

- `SS-7_v1.2_chatgpt_verification_response.md`
- `SS-7_v1.2_copilot_verification_response.md`
- `SS-7_v1.2_grok_verification_response.md`

The next session will reference these when updating `reviews-SS-7.md`.

### Step 2 — Apply the v1.2 paper-body changes to your local repo

Two ways. Pick one.

**Option A (recommended) — git patch**

The patch file `0003-SS-7-v1.2-partial-paper-body-notebook-PH.patch` contains the full v1.2 paper-body commit. Apply in Git BASH from your CPP folder:

```bash
git am /path/to/0003-SS-7-v1.2-partial-paper-body-notebook-PH.patch
```

This creates a local commit (`7ce5015` in the sandbox; will get its own hash in your repo) with message `"SS-7 v1.2 partial: paper body, verification notebook, PH-OPEN-SS-22"`.

**Option B — drop-in whole files**

Copy these files to their destinations:

| File (in Downloads) | Goes to |
|---|---|
| `SS-7_alpha_cluster_edge_formula.tex` | `CPP/series_strong/papers/SS-7_alpha_cluster_edge_formula.tex` |
| `SS-7_alpha_cluster_edge_formula.py` | `CPP/series_strong/papers/SS-7_alpha_cluster_edge_formula.py` |
| `SS-7_alpha_cluster_edge_formula.pdf` | `CPP/series_strong/papers/SS-7_alpha_cluster_edge_formula.pdf` |
| `PH-OPEN-SS-22.md` | `CPP/problem_histories/PH-OPEN-SS-22.md` *(new)* |

Then commit in GitHub Desktop with summary:
> SS-7 v1.2 partial: paper body, verification notebook, PH-OPEN-SS-22

and description:
> Paper body complete and compiling clean (25 pages). Verification notebook produces 12-nucleus RMS 0.80%. PH-OPEN-SS-22.md documents first RETIRED open problem in CPP programme record. Companion docs, registries, transcript still pending — see SS-7_v1.2_handover.md for next session.

### Step 3 — DO NOT PUSH YET

The v1.2 state committed by Step 2 is **partial**. The paper body is revised and self-consistent, but:

- Companion docs (`mechanism-SS-7.md` etc.) still read v1.1
- `Research_Frontier.md`, `predictions.md`, `paper_catalog.md` still read v1.1
- v1.2 development transcript not yet curated

If you push right now, the paper PDF on GitHub will show 12 predictions but `predictions.md` will still show 8. That's exactly the kind of drift the 20 April consolidation was meant to prevent. Keep the commit local until the next session completes the companion/registry work, then push as one coherent v1.2 landing.

**Exception:** if you want SS-7 paper v1.2 available to reviewers RIGHT NOW for some reason, you can push `7ce5015` as a "paper-body-first landing" and flag that companions will land separately. This is a judgment call; default is "wait and land v1.2 as one commit."

### Step 4 — Hand `SS-7_v1.2_handover.md` to the next Opus session

That document gives the next session everything it needs to complete v1.2 in one focused sitting (or two shorter ones). Start a new chat window; paste `SS-7_v1.2_handover.md` as the opening context along with `bootup.md`.

---

## WHAT'S IN THE OUTPUTS FOLDER

**Apply to your repo:**
- `0003-SS-7-v1.2-partial-paper-body-notebook-PH.patch` — the v1.2 partial commit
- OR the four whole-file drop-ins: `SS-7_alpha_cluster_edge_formula.tex/.py/.pdf` + `PH-OPEN-SS-22.md`

**Hand to next session:**
- `SS-7_v1.2_handover.md` — the detailed continuation document

**Reference / already-committed-earlier-today:**
- `0001-Consolidate-paper-completion-procedures-into-single-.patch` — template extraction (already in origin as commit `837eed5`)
- `0002-Post-consolidation-hygiene-dates-version-history-boo.patch` — hygiene follow-up (part of the same push)
- `bootup.md`, `operating_system.md`, `paper_completion_checklist.md`, `paper_production_workflow.md` — updated template files (already in origin)

**Development-record / can be discarded or archived:**
- `SS-7_v1.2_reviewer_verification_letter.md` — the letter you sent to reviewers today
- `SS-7_v1.2_revision_plan.md` — planning doc; superseded by the committed work
- `SS-7_v1.2_scope_audit.md` — 16-location audit that drove the .tex edits
- `ss8_empirical_map.py` — the script that surfaced the Table 1 finding

---

## HONEST STATUS NOTE

The v1.2 cycle produced two artifacts of real quality:

1. A corrected SS-7 paper that extends the central claim from 8 predictions to 12, including the previously-missing ⁴⁸Cr, ⁵²Fe, ⁵⁶Ni.

2. The first retirement of an open problem in the CPP programme record, documented in PH-OPEN-SS-22.md following symmetric-honesty protocol.

It also exposed how much attention a revision cycle costs. The paper body alone was roughly one full session's worth of careful work. Companions + registries + transcript is another session. Split intentionally; don't hurry.

The checklist (`paper_completion_checklist.md`) is now being validated. If the next session finds a defect in the checklist during v1.2 completion, the checklist itself gets fixed as part of the work — that's the validation test doing its job.

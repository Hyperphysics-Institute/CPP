# Template: presenting a repo file to the swarm / panel

**Purpose.** Whenever Claude asks Thomas to hand a repo file to the AI review panel (swarm), Claude must
present it in this format **inside the chat response** — so Thomas never has to locate, open, and copy a
file buried in the repo tree (he has no clickable link from a patch alone). This is a standing convention
(see `todolist.md` → Standing conventions).

## What Claude always provides, in this order

1. **A clickable GitHub link to the file** (so Thomas — and the AI reviewers, who fetch raw URLs — can
   open it directly). Provide both forms:
   - human/blob: `https://github.com/Hyperphysics-Institute/CPP/blob/main/<path>`
   - raw (AI-fetchable): `https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/<path>`
   The links only work after the file is pushed to `main`, so present them after the apply-and-push.

2. **A one-paragraph intro** framing the file for the swarm: what it is, why it matters, and what is being
   asked of the reviewers. Written so Thomas can paste it directly as the lead-in to the panel.

3. **The full rendered file content**, in a copy-paste block (the rendered Markdown, NOT the patch/diff —
   no `+` prefixes, no commit header), so Thomas can copy it straight into the panel chat.

## Format Claude uses in the response

> **[intro paragraph]** — one paragraph framing the file for the swarm, ending with the clickable
> link(s).
>
> Then: the full file content, fenced for copy-paste.

## Notes

- This presentation package is **separate** from the apply-and-push patch block. The patch is for Thomas
  to apply the file to the repo; this package is for handing the (now-pushed) file to the swarm.
- Alternative Thomas has used: posting the presented `.patch` file directly to the swarm — it works
  (reviewers parse through the diff), but the rendered-content + link form is cleaner (no diff noise) and
  is the default.
- Keep the intro paragraph tight; the file itself carries the detail.

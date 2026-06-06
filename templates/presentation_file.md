# Template: presenting a repo file to the swarm / panel (single copy block)

**Purpose.** Whenever Claude asks Thomas to hand a repo file to the AI review panel (swarm), Claude
presents it as **ONE single fenced copy-paste block** inside the chat response — so Thomas can
one-click-copy and paste it to each panel member, without highlighting/copying multiple separate pieces,
and without ever having to locate and open a file buried in the repo tree. Standing convention CONV-001
(see `todolist.md` → Standing conventions).

## The single block contains, in this order

1. **The GitHub links to the file** (so Thomas — and the AI reviewers, who fetch raw URLs — can open it):
   - human/blob: `https://github.com/Hyperphysics-Institute/CPP/blob/main/<path>`
   - raw (AI-fetchable): `https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/<path>`
   The links only work after the file is pushed to `main`, so present them after the apply-and-push.

2. **A one-paragraph intro** framing the file for the swarm: what it is, why it matters, and what is being
   asked of the reviewers.

3. **The full rendered file content** (the rendered Markdown, NOT the patch/diff — no `+` prefixes, no
   commit header).

All three go **inside the same fenced block**, so it is a single copy and a single paste per reviewer.

## Format Claude uses in the response

A brief lead-in sentence (outside the block), then ONE fenced block, e.g.:

````
Links:
  blob: https://github.com/Hyperphysics-Institute/CPP/blob/main/<path>
  raw:  https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/<path>

Intro: [one paragraph framing the file for the swarm and stating what is asked of the reviewers.]

----- file content below -----

[full rendered Markdown content of the file]
````

(Use a 4-backtick outer fence so any 3-backtick code fences inside the file content render correctly
inside the single block.)

## Notes

- This single presentation block is **separate** from the apply-and-push patch block. The patch is for
  Thomas to apply the file to the repo; this block is for handing the (now-pushed) file to the swarm.
- Keep the intro tight; the file itself carries the detail.
- Updated 6 Jun 2026 Session 154 to the single-block format at Thomas's request (previously three separate
  elements requiring multiple highlight/copy/paste actions).

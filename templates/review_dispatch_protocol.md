# Review Dispatch Protocol

**Location:** `templates/review_dispatch_protocol.md`
**Purpose:** Turn a finished review *package* into **paste-ready dispatch text** Thomas can drop straight into each AI reviewer's input window — so he never has to know the file name, navigate the tree, or compose the framing himself.
**Companion files:** `operating_system.md` §5 (the Multi-AI Review Cycle — roles, tiers, lessons); `templates/AI_team_expectations.md`; `templates/reviewer_pause_template.md`; `programmatic_decisions/PD-002-verification-tier-taxonomy.md`.
**Relationship to the handover protocol:** this is the review-side analog of the §15 Session-close Handover Protocol. Handover preserves state at session close; review dispatch gets a registered artifact in front of the panel. Both are triggered by a canonical command and produce a standard, copy-paste-ready output.

---

## 1. Canonical command (the trigger)

When Thomas says **"initiate review protocol"** (or *"execute review protocol" / "review protocol" / "dispatch review" / "send it to the reviewers"*, minor variants), the AI assistant immediately produces the **Dispatch Output** of §3 for the artifact under discussion. No further prompting is needed; if the target artifact is ambiguous (more than one reviewable artifact is in play), the assistant asks exactly one clarifying question naming the candidates, then proceeds.

The assistant should also **proactively offer** — "Do you want to initiate the review protocol?" — right after registering any artifact that answers a registered open problem or advances a registered verdict single-pass (the AUDIT-1 / MERGE-2 / STATUS / TARROW precedent: such artifacts go to the panel before the "single-pass" qualifier is removed).

---

## 2. Precondition: the self-contained review package

Dispatch presupposes a **self-contained** review package exists at
`<paper-folder>/review/<artifact-slug>_review_package_v1.0.md`.
If it does not yet exist, the assistant creates it first (this is normally the cycle-opening patch). "Self-contained" is mandatory and means **all content is inline** — context, the claims, the scrutiny questions, the response format, **and the verify code embedded in full** (the Patch-0656 process-learning: a reviewer cannot reach the SCRIPT-EXECUTED tier from a filename reference alone). The package's own §6 carries reviewer-specific framing so each reviewer reads their own row.

The package is the immutable request record; reviewer responses aggregate later in the sibling `reviews-<ARTIFACT-ID>.md`.

---

## 3. The Dispatch Output (what the command produces)

The assistant emits **three** blocks, in this order. **The dispatch is a single shared document, identical for every reviewer** — the per-reviewer wrapper prompts of earlier versions are **retired** (Patch 1604). The package's own §6 (``read your own row'') already carries each reviewer's steer, so individualized wrappers are redundant; single-document was the design intent of the §6 steer rows all along.

### (a) Identification header — so Thomas is never lost
One short block naming, in plain words:
- **Programme:** Conscious Point Physics (CPP).
- **Artifact:** the ID + human title + version + patch (e.g. "THEO-CHIR-TARROW-1 v1.0, Patch 0658 — the time-reversal arrow status, OPEN-CHIR-2a").
- **One-line what-it-is:** a single sentence a reviewer could understand cold.
- **Package file:** the repo path **and** the raw GitHub URL (provenance pointer; the inline block of (b) is the delivery).
- **Responses land in:** the `reviews-<ARTIFACT-ID>.md` path.

### (b) The single shared document — **the delivery** (per CONV-001)
The full rendered package body delivered as **one copy-paste block** (4-backtick outer fence so the embedded code fences render), per CONV-001 / `templates/presentation_file.md`. This is the **default and the only delivery.** Empirically (CC-arc cycle, 13 Jun 2026) the repo's raw GitHub URL was **unreachable by every external reviewer** (private repo / CDN lag) — none of ChatGPT/Grok/Copilot could fetch it; all three reviewed cleanly from the inline block. So the inline block is authoritative. It carries, at its head, a one-paragraph ask plus a one-line GitHub pointer (blob/raw, **marked "likely unreachable; inline is authoritative"** — provenance only), then the full package §0–§8 **including the verify code in full**. It is **one identical document pasted to every active reviewer** (default panel: ChatGPT, Grok, Copilot; optional Gemini for breadth; a hostile pass can be requested from any panel member). The package's own §6 (``read your own row'') carries each reviewer's steer — **including any reviewer-specific disambiguation rider** (e.g. ChatGPT's) — so **no per-reviewer wrapper is built or needed.**

### (b-alt) The raw GitHub URL — secondary provenance pointer
`https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/<path-to-package>`
(Provenance/record only. **Do not rely on it for delivery** — for this repo it is generally not fetchable by external reviewers. The inline block (b) is the delivery.)

### (c) Delivery-mode note
**The single shared document (b) is the entire dispatch — zero-dependency, pasted identically to each reviewer; the per-reviewer wrapper prompts are retired.** The raw GitHub URL is a secondary provenance pointer only and is generally unreachable for external reviewers on this repo (private / CDN lag) — never gate a dispatch on it. Pastebin/raw-URL remain optional per OS §5 if a reviewer specifically prefers a link, but the inline block ships from the start and never requires Thomas to wait for, or reply "paste it" to, a failed fetch.

---

## 4. The single-document lead-in (the head of the shared block)

The shared document opens with a short, reviewer-agnostic framing paragraph — the same for everyone, because each reviewer finds their own steer in the package §6. Keep it short; the package carries the depth. Fill the `<…>` slots:

```
You are one of three independent reviewers (ChatGPT, Grok, Copilot) on the
Conscious Point Physics (CPP) review panel. CPP is a theoretical-physics
programme deriving Standard-Model structure from a 600-cell lattice substrate.
Please review <ARTIFACT-ID> — <ONE-LINE WHAT-IT-IS>. Everything you need is inline
below (context, claim chain, triage, verify code, response format). Find YOUR
reviewer-specific steer in §6 ("read your own row"). If you can run the §7 code,
please do and report SCRIPT-EXECUTED. Label every claim with its verification
tier — INSPECTED / INDEPENDENTLY RECOMPUTED / SCRIPT-EXECUTED (PD-002) — and
respond in the package's §8 format.

File (provenance only — likely unreachable for external reviewers on this private
repo; the inline content below is authoritative):
  blob: https://github.com/Hyperphysics-Institute/CPP/blob/main/<path-to-package>
  raw:  https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/<path-to-package>
```

**Reviewer-specific framing — including any disambiguation rider — lives in the package §6, not in a wrapper.** A reviewer prone to cross-wiring sessions (e.g. ChatGPT) gets its rider as a line inside its own §6 row, for example:
```
Disambiguation rider: this is the CPP <SECTOR> programme's <ARTIFACT-TYPE>; it is
NOT a nuclear-physics OPEN-SS audit, NOT a different paper, and NOT a request to
reconstruct from memory — engage the inline package content directly.
```
That way the single shared document remains one identical paste for all reviewers while still steering each one correctly.

---

## 5. Reviewer-steer cheat-sheet (defaults; the package §6 overrides)

- **Grok** — independent recompute (run the embedded code → SCRIPT-EXECUTED; recompute any tables/group-theory/symmetry assignments from first principles); strongest on numerical/structural verification and novel contributions.
- **Copilot** — per-question structural consistency; referee-grade framing; logic of the load-bearing steps.
- **ChatGPT** — press the hardest triage question(s) and the deflation/overclaim checks; verdict-honesty; the disambiguation rider applies.
- **Gemini** (optional) — breadth/confirmatory pass; use when a fourth independent read is wanted (note: on past cycles Gemini has been confirmatory rather than additive, and may self-report "simulated" rather than actually-run code — treat its SCRIPT-EXECUTED claims as RESTATE-tier unless it shows output).
- **Hostile pass** (no dedicated reviewer; Claude Sonnet 4.0 retired) — give any panel member the hostile steer: "this is wrong, find every flaw," aimed at the top-triage targets.

---

## 6. After dispatch (closing the loop)

Reviewer responses come back to Thomas, who relays them. The assistant then integrates them into `reviews-<ARTIFACT-ID>.md` (verdicts + cross-reviewer synthesis + triage) per the MERGE-2 / STATUS pattern: a verdict-flipping objection on a top-triage question → restate (artifact → v1.1); otherwise apply calibration and **close the cycle** (typically 3/3), removing the "single-pass" qualifier in the artifact CHANGELOG and the sector frontier file. The cycle-close is its own patch with a reasoning fragment.

---

*Created Patch 0660 (Session 150, 30 May 2026) at Thomas's request, after the TARROW-1 cycle-opening (Patch 0659) surfaced the missing piece: a finished review package is not actionable until it is turned into paste-ready, reviewer-addressed dispatch text. This protocol closes that gap and makes "initiate review protocol" a first-class command alongside "execute handover protocol."*

*Updated Patch 1604 (21 June 2026, SF-6 cycle) — **retired the per-reviewer dispatch prompts (old §3(c)/§4 skeleton) in favour of a single shared document.** The dispatch is now ONE identical copy-paste block pasted to every reviewer; each reviewer's steer (and any disambiguation rider) lives in the package's own §6 "read your own row," which made the per-reviewer wrappers redundant. §3 now emits three blocks (header, single shared document, delivery-mode note); §4 is the reviewer-agnostic single-document lead-in. Trigger and §5 cheat-sheet unchanged.*

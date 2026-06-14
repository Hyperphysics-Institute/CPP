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

The assistant emits four blocks, in this order:

### (a) Identification header — so Thomas is never lost
One short block naming, in plain words:
- **Programme:** Conscious Point Physics (CPP).
- **Artifact:** the ID + human title + version + patch (e.g. "THEO-CHIR-TARROW-1 v1.0, Patch 0658 — the time-reversal arrow status, OPEN-CHIR-2a").
- **One-line what-it-is:** a single sentence a reviewer could understand cold.
- **Package file:** the repo path **and** the raw GitHub URL (provenance pointer; the inline block of (b) is the delivery).
- **Responses land in:** the `reviews-<ARTIFACT-ID>.md` path.

### (b) The inline package block — **DEFAULT delivery** (per CONV-001)
The full rendered package body delivered as **one copy-paste block** (4-backtick outer fence so the embedded code fences render), per CONV-001 / `templates/presentation_file.md`. This is the **default, not a fallback.** Empirically (CC-arc cycle, 13 Jun 2026) the repo's raw GitHub URL was **unreachable by every external reviewer** (private repo / CDN lag) — none of ChatGPT/Grok/Copilot could fetch it; all three reviewed cleanly from the inline block. So the inline block is authoritative. It carries, at its head, a one-line GitHub pointer (blob/raw, **marked "likely unreachable; inline is authoritative"** — provenance only), then the one-paragraph ask, then the full package §0–§8 **including the verify code in full**. One block per reviewer; the package's own §6 lets each reviewer find their steer.

### (b-alt) The raw GitHub URL — secondary provenance pointer
`https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/<path-to-package>`
(Provenance/record only. **Do not rely on it for delivery** — for this repo it is generally not fetchable by external reviewers. The inline block (b) is the delivery.)

### (c) Per-reviewer dispatch prompts — paste-ready
One block **per active reviewer** (default panel: ChatGPT, Grok, Copilot; optional Sonnet hostile pass), each a complete copy-paste using the skeleton in §4. They differ only in the reviewer name and the one-line reviewer-specific steer (pulled from the package §6). Under inline-default delivery (b), each per-reviewer dispatch is the **steer line followed by the inline package block** — one paste, no link to open.

### (d) Delivery-mode note
**Inline single-block (b) is the default and is always sufficient (zero-dependency).** The raw GitHub URL is a secondary provenance pointer only and is generally unreachable for external reviewers on this repo (private / CDN lag) — never gate a dispatch on it. Pastebin/raw-URL remain optional per OS §5 if a reviewer specifically prefers a link, but the inline block does not require Thomas to wait for, or reply "paste it" to, a failed fetch — it ships inline from the start.

---

## 4. The dispatch-prompt skeleton (reusable)

Fill the `<…>` slots. Keep it short — the package carries the depth.

```
You are <REVIEWER>, one of three independent reviewers on the Conscious Point
Physics (CPP) review panel. CPP is a theoretical-physics programme deriving
Standard-Model structure from a 600-cell lattice substrate. I'd like your review
of <ARTIFACT-ID> — <ONE-LINE WHAT-IT-IS>.

The complete, self-contained review package is here:
  <RAW-URL>
(If you can't open the link, reply "paste it" and I'll paste the full text.)

Please:
- Read the whole package — everything you need is inline (context, the claims,
  the scrutiny questions, and the verify code in its §7; no other files needed).
- Work the triage order in the package's §5; your reviewer-specific steer is in
  its §6. <ONE-LINE REVIEWER STEER>
- Label every numerical/structural claim with its verification tier —
  INSPECTED / INDEPENDENTLY RECOMPUTED / SCRIPT-EXECUTED (the package §7/§8;
  PD-002). If you can run the embedded code, please do and report SCRIPT-EXECUTED.
- Respond in the package's §8 format: lead with a one-line verdict on the
  top-triage question(s), then per-question findings, and clearly separate
  verdict-flipping objections (with a worked argument) from calibration
  (wording/scope) suggestions.

Send your review back to me as text and I'll integrate it.
```

**Disambiguation rider (append for ChatGPT, and any reviewer prone to cross-wiring sessions):**
```
Note: this is the CPP <SECTOR> programme's <ARTIFACT-TYPE>; it is NOT a
nuclear-physics OPEN-SS audit, NOT a different paper, and NOT a request to
reconstruct from memory — engage the inline package content directly.
```

---

## 5. Reviewer-steer cheat-sheet (defaults; the package §6 overrides)

- **Grok** — independent recompute (run the embedded code → SCRIPT-EXECUTED; recompute any tables/group-theory/symmetry assignments from first principles); strongest on numerical/structural verification and novel contributions.
- **Copilot** — per-question structural consistency; referee-grade framing; logic of the load-bearing steps.
- **ChatGPT** — press the hardest triage question(s) and the deflation/overclaim checks; verdict-honesty; the disambiguation rider applies.
- **Sonnet** (optional) — hostile pass: "this is wrong, find every flaw," aimed at the top-triage targets.

---

## 6. After dispatch (closing the loop)

Reviewer responses come back to Thomas, who relays them. The assistant then integrates them into `reviews-<ARTIFACT-ID>.md` (verdicts + cross-reviewer synthesis + triage) per the MERGE-2 / STATUS pattern: a verdict-flipping objection on a top-triage question → restate (artifact → v1.1); otherwise apply calibration and **close the cycle** (typically 3/3), removing the "single-pass" qualifier in the artifact CHANGELOG and the sector frontier file. The cycle-close is its own patch with a reasoning fragment.

---

*Created Patch 0660 (Session 150, 30 May 2026) at Thomas's request, after the TARROW-1 cycle-opening (Patch 0659) surfaced the missing piece: a finished review package is not actionable until it is turned into paste-ready, reviewer-addressed dispatch text. This protocol closes that gap and makes "initiate review protocol" a first-class command alongside "execute handover protocol."*

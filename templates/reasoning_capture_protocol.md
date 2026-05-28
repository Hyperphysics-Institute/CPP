# Reasoning-Capture Protocol

**Status:** authoritative governance document (peer of `operating_system.md`,
`paper_completion_checklist.md`)
**Established:** Session 146, Patch 0608, 2026-05-27
**Problem it solves:** verbatim physics reasoning, sketches, and verification
scripts were being generated inside chat windows and lost when those windows
closed, forcing expensive post-hoc reconstruction every session.

---

## 0. The core principle

**Verbatim capture is only possible at patch-time.** Once a context window
closes, everything afterward is *reconstruction* — a lossier operation that
smooths, rationalizes, and fills gaps rather than reproducing the original.
Therefore capture is not a separate later task; it is part of shipping the
patch.

---

## 1. The extended patch-delivery contract

The existing contract (every `.patch` gets an apply-and-push block, unasked)
is **extended**, not replaced. Every **physics-bearing** patch now bundles,
in a **single `git am`**:

1. **The artifact** — the `.tex` (or other deliverable). *Already happens.*
2. **A reasoning fragment** — `reasoning/<patch>.md`. Verbatim physics, the
   sketches, and the dead-ends/ruled-out routes. **Mandatory.**
3. **A verification script** — `scripts/<patch>.py` — **only if** computation
   was performed (row-sum checks, numerical evaluations, symbolic identities).
   Omit for pure-synthesis patches (e.g. umbrella registrations) unless they
   contain a checkable claim.
4. **The apply-and-push block.** *Already happens.*

One patch, multiple files, one `git am`. **No change to the apply workflow.**
The capture stops being a thing to remember because it rides the contract.

> **Discipline metric evolution.** The "single-artifact discipline" counter
> (N-for-N since Patch 0585) was defined as *one `.tex` per patch*. Going
> forward the unit is *one coherent patch per unit of work*, which may bundle
> `.tex` + reasoning + script. The counter continues; its meaning broadens
> from "one file" to "one coherent commit."

**Pure-synthesis / registration / governance patches** (umbrellas, this
protocol, OS edits) still get a reasoning fragment if a non-trivial *decision*
was made (which findings to register and why, naming/structure choices), but
need no verification script.

---

## 2. Storage shape: fragments, not a monolith

**Do NOT concatenate reasoning into one growing per-paper file.** That is the
exact failure that fragmented this work across ~5 windows: a monolith
overflows, exactly as `research_frontier.md` did at 1852 lines before its
dashboard + sector-file decomposition. Reuse the pattern that already works.

- **Canonical store:** `reasoning/<patch>.md` — one fragment per patch.
  *Naturally bounded; can never overflow* because each is a single patch's
  worth of reasoning.
- **Per-paper reading view:** built **on demand** by concatenating fragments
  in patch order via `templates/build_reasoning.sh` (see §5). You get the
  single-file experience without the canonical store ever growing unbounded.

This is the dashboard/sector pattern applied to reasoning.

---

## 3. File types: exactly two

Resist proliferation; more than two types is how a protocol dies under time
pressure.

| Type | Path | Contents |
|---|---|---|
| **reasoning** | `reasoning/<patch>.md` | Verbatim physics derivations, sketches, dead-ends, and the *why* behind choices. Sketches and abandoned routes are just reasoning — no separate file. |
| **script** | `scripts/<patch>.py` | Only **physics** verification code. Throwaway tooling (patch construction, `git am` dry-runs) is NOT saved here. |

**Organizational / structural decisions** (filenames, what-to-register, layout)
already have homes: the `.tex` CHANGELOG header and the commit-message body.
Do not duplicate them into a third file type.

---

## 4. Provenance flag: verbatim vs reconstructed

Every fragment opens with a status line:

```
STATUS: verbatim (captured at patch-time, Session NNN)
```
or, for anything written after the originating window closed:
```
STATUS: reconstructed (NOT verbatim — captured post-hoc Session NNN from <source>)
```

Reconstructed fragments are a different, lower-confidence artifact. The flag
lets future readers calibrate trust. The Tier 4 convention specifies
*verbatim* precisely because reconstruction loses information; honor that
distinction explicitly rather than silently.

---

## 5. The build script

`templates/build_reasoning.sh` concatenates fragments for a bucket in patch
order into a single readable view, written to stdout or a target file. Usage:

```
bash templates/build_reasoning.sh hardened_theorems/reasoning > /tmp/dsl_reasoning_full.md
```

The compiled view is **ephemeral** (a reading convenience), never committed as
canonical — the fragments are the source of truth.

---

## 6. Bucketing and migration path

- **Canonical location (CORRECTED Session 146 remediation):** DSL hardened-theorem
  reasoning and verification live ALONGSIDE the theorem artifacts they document, in
  the Dynamical Substrate Law subfolder:
  `series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/hardened_theorems/reasoning/<patch>.md`
  and `.../hardened_theorems/scripts/<patch>.py`, indexed by **patch number** (the
  unambiguous anchor — every fragment maps to exactly one patch).
  **Do NOT create a top-level `hardened_theorems/` directory** — the original
  Session-146 capture mistakenly did this and was reverted. The DSL work already
  has a home; fragments go there, beside the `.tex` they describe.
- **Verify location before writing:** clone the repo and `ls` the live DSL folder
  before placing any fragment (see §0 + §9). The fragment must sit next to the
  artifact it documents — never in a parallel/orphan tree.
- **On paper consolidation:** if/when these theorems consolidate into a standalone
  paper, fragments stay within the SU/ substrate-chirality-arc tree and may be
  renamed to the sector-coded Tier 4 convention (`reasoning-SU-N.md` / per-paper
  `reasoning/`). They are already in `SU/` — no cross-sector migration needed.

Patch-number indexing + co-location with the artifact keeps provenance unambiguous.

---

## 7. The "DSL" definition (RESOLVED Session 146 remediation)

`THEO-DSL-N` = **Theorem — Dynamical Substrate Law, N**. The DSL series is the
theorem-registry sub-prefix for the **F.1 Dynamical Substrate Law** arc, whose
home is
`series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/`.

```
THEO-DSL = THEO- (theorem) + DSL (Dynamical Substrate Law)
```

The expansion had lived only in chat until this remediation — itself an instance
of the loss this protocol exists to prevent, now durably recorded.

**Registry numbering is reserved by orientation variant — DO NOT reuse a number
without checking `theorem-registry.md` live:**

| Variant | stabilizer / dim | structural | coefficient |
|---|---|---|---|
| vertex-aligned | $I_h$ / 1D | THEO-DSL-4 | THEO-DSL-3 ($\alpha_1$), THEO-DSL-5 ($\alpha_2$) |
| edge-aligned   | $D_5$ / 2D | THEO-DSL-6 | THEO-DSL-7 (RESERVED, Sequence-2A) |
| face-aligned   | $C_s$ / 3D | THEO-DSL-8 | THEO-DSL-9 (RESERVED, Sequence-2B) |

---

## 8. Backlog policy

Pre-protocol work (everything before Patch 0608) is **not** retroactively
required to have fragments. Backlog reconstruction is a *deliberate,
separately-scoped* cleanup — never rushed at the tail of a window — and every
backlog fragment carries the `STATUS: reconstructed` flag. The protocol's job
is to prevent recurrence from here forward; the backlog is a bounded one-time
debt, not an ongoing obligation.

---

## 9. STEP 0 — clone-first precondition + handover gate (root-cause fix)

The Session-146 misgrounding (five patches with collided THEO-DSL numbers,
duplicated theorems, wrong directory) had a single root cause: **work proceeded
from chat-prompt framing and `conversation_search` instead of the live
repository.** bootup.md says to clone, but a handover that does not *itself*
restate it lets the next instance skip it (instances follow the in-context
handover over the general bootup).

**Two non-negotiable gates:**

1. **Clone before claiming anything.** Before registering a THEO-DSL identifier,
   placing a file, or citing a patch number, clone the repo and verify against
   live ground truth:
   ```
   cd /home/claude && rm -rf CPP && git clone --depth 1 \
     https://github.com/Hyperphysics-Institute/CPP.git
   grep -n "THEO-DSL" CPP/theorem-registry.md          # check numbering
   ls CPP/series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/hardened_theorems/
   ```
   A green "single-artifact discipline" counter measures commit tidiness, NOT
   correctness or grounding. Do not let a clean counter substitute for this check.

2. **Every handover doc opens with a BLOCKING clone gate as line 1:**
   ```
   [ ] STEP 0 (BLOCKING): git clone the repo + grep theorem-registry.md.
       Do NOT proceed to any physics/registration work until done.
   ```
   The precondition must live IN the handover, not only in bootup.md.

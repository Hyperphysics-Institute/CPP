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

- **Now:** DSL hardened-theorem reasoning lives in
  `hardened_theorems/reasoning/<patch>.md` and verification in
  `hardened_theorems/scripts/<patch>.py`, indexed by **patch number** (the
  unambiguous anchor — every fragment maps to exactly one patch).
- **On paper consolidation:** these theorems are multi-sector
  $D_5$-symmetry / golden-ratio / orientation-phase-diagram **geometric
  infrastructure** — not SM/SS/EW content, but machinery those sectors draw
  on. The eventual consolidation paper is therefore an **`SU/`** (multi-sector
  combo) candidate. At consolidation, fragments migrate to
  `SU/<paper>/reasoning/` and may be renamed to the sector-coded Tier 4
  convention (`reasoning-SU-N.md`).

Patch-number indexing now + sector-coded indexing at consolidation keeps both
phases unambiguous.

---

## 7. The "DSL" definition slot

The `THEO-DSL-N` registry identifier is in active use (DSL-6 through DSL-9 as
of Session 146) but its expansion was **never recorded** in a durable file —
it lived only in chat. This is itself an instance of the problem this protocol
solves. **Definition to be supplied by Thomas and recorded here:**

```
THEO-DSL = THEO- + D__ S__ L__   [EXPANSION PENDING — fill in]
```

Until filled, treat `DSL` as an opaque registry label and do not confabulate
an expansion.

---

## 8. Backlog policy

Pre-protocol work (everything before Patch 0608) is **not** retroactively
required to have fragments. Backlog reconstruction is a *deliberate,
separately-scoped* cleanup — never rushed at the tail of a window — and every
backlog fragment carries the `STATUS: reconstructed` flag. The protocol's job
is to prevent recurrence from here forward; the backlog is a bounded one-time
debt, not an ongoing obligation.

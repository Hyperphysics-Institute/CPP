# methods_catalogue/

A central catalog of **physics derivation methods** used across CPP work. The catalog is **three-layered** by design — mathematical techniques at the substrate, methodological disciplines for physics derivation work as the load-bearing structure, heuristic strategies for physics problem-solving at the pattern-matching top.

## Scope: physics derivation methods only

**In scope.** Techniques, disciplines, and heuristics used to *derive physical results* — group-theoretic structure of substrate symmetries, geometric verification of substrate identities, matrix-element factorization techniques, epistemic decomposition of substrate-physics derivations, heuristics for substrate-physics problem-shapes, cross-sector unification audits, methodological discipline applied to physics closure work.

**Out of scope.** Protocol patterns, workflow heuristics, operating-system disciplines, handover discipline, commit-cadence rules, reviewer-interaction protocols, session-management methodology, anything that governs *how to organize the work* rather than *how to derive the physics*. These belong in their proper homes:

- **Protocol / workflow patterns** → `templates/operating_system.md` (the operating system itself codifies them)
- **Reviewer relationship discipline** → `relationship_protocol.md`
- **Voice / methodological observations** → `founders_voice/NNN_<topic>.md`
- **Meta-conversation capture** → `opus_voice/NNN_<topic>.md`
- **Programmatic decisions** → `programmatic_decisions/PD-NNN_<topic>.md`

Scope test before registering: *would the AI collaborator look up this method when deriving physics, or when organizing the work?* If the latter, it belongs in one of the homes above, not this catalog. (Scope clarification adopted Patch 0461, 19 May 2026, after the Patch 0460 misregistration of three protocol-pattern entries that were reversed in Patch 0461 and recodified in their proper home at `templates/operating_system.md` §15.10 + Step C/D amendments.)

## Why this exists

Across the Reading C closure trajectory (Sessions 124-133, Patches 0417-0443) and earlier closure arcs (SF-4 Sessions 37-54, SS-9 Sessions 12-32, the SM-line work), the same physics derivation methods got applied repeatedly to different sectors. The methods are real and reusable — but they were scattered across `templates/operating_system.md`, `founders_voice/NNN`, individual sketch files, and Tier 4 reasoning documents with no central listing. A future researcher (human, AI, or otherwise) inheriting CPP could not quickly answer "what physics-derivation techniques does this programme use?" without reading dozens of files.

The methods catalog answers that question — for physics derivation methods. Workflow / protocol questions are answered by the operating system and adjacent files (`relationship_protocol.md`, `founders_voice/`, `programmatic_decisions/`).

## The three layers

**Layer 1 — Mathematical techniques (for physics derivation).** Specific mathematical tools applied in physics derivations: theorems, lemmas, formal procedures, computational methods. Each is well-defined, instantiable, and produces concrete output when applied to concrete physical input. Examples: Schur orthogonality for cage-shell averaging, Wigner-Eckart factorization for chirality matrix elements, branching rule analysis $G \downarrow H$ for stabilizer reduction. These are the substrate of physics derivation work.

**Layer 2 — Methodological disciplines for physics derivation work.** Higher-order rules about how Layer 1 techniques get deployed in *physics derivation*: when to apply which technique to a physical problem, what counts as adequate rigor at which closure stage, how to organize derivation work across sectors. Examples: Layer A/B/C epistemic decomposition (separates derived physics content from imported formalism), register-then-resolve discipline (don't resolve an analytical complication in a physics closure under deadline pressure; register it explicitly and resolve in a dedicated patch), three converging arguments standard for Layer 2 physics closures. These are the load-bearing structure of physics derivation work.

**Layer 3 — Heuristic strategies (for physics problem-solving).** Pattern-recognition rules for which methodological discipline (and hence which mathematical technique) to apply to a given physics problem shape. Examples: when a physics matrix element vanishes under naive framing, look for combined-symmetry generators; when a physics-sector instance derives a result, audit whether sister sectors inherit structurally. These are the top-layer pattern matchers for physics problem-solving.

## How the layers relate (for physics work)

Layer 3 is what the AI collaborator does first when encountering a new *physics* problem — recognize the shape. Layer 2 is the discipline structure for how to convert that recognition into a closure sequence. Layer 1 is the technique stack the discipline draws from.

A worked example of all three layers operating together on a physics problem: Q6-PAIRING at Patch 0439. Layer 3 noticed the matrix element vanishing pattern (heuristic: vanishing under naive framing → look for combined-symmetry generators). Layer 2 applied the register-then-resolve discipline (Q6-PAIRING was registered Patch 0438, resolved Patch 0439). Layer 1 deployed Wigner-Eckart factorization on a $D_{5d}$ stabilizer with antipodal-pair refinement.

## Status

**Stub.** This catalog is a seed at Session 133 Patch 0449 close. Initial entries enumerate techniques and disciplines actually used in the Reading C closure trajectory plus reference earlier physics work. Full catalog completion is queued as **OPEN-ORG-016** (organizational frontier) for future-window work.

Two pre-existing Patch 0449 seed entries that described workflow patterns rather than physics derivation patterns (METH-L3-004 Closure trajectory saturation → consolidate via handover + outline; METH-L3-006 Meta-conversation surfacing → capture before window close) were removed at Patch 0462 per the explicit physics-derivation-only scope. Their content is preserved in its proper organizational home: METH-L3-004's content (closure-trajectory-saturation → consolidate via handover) is essentially captured in `templates/operating_system.md` §15 trigger criteria; METH-L3-006's content (meta-conversation → opus_voice/ capture) is essentially captured in the existing `opus_voice/` convention with `opus_voice/001` + `opus_voice/002` as canonical examples.

One pre-existing entry remains borderline by the new explicit scope: METH-L2-004 Symmetric-honesty discipline canonically cites `founders_voice/004_verbatim_substance_preservation_discipline.md` as its home, suggesting the discipline lives primarily in `founders_voice/` and only secondarily appears in physics-derivation work as an application. METH-L2-004 is preserved at Patch 0462 because its physics-derivation applications (§13 §12 geometric error preservation as substantive correction; Q5-PAIRING and Q6-PAIRING explicit registration rather than glossing) are real and the discipline is invoked routinely in physics closure work. Flag for review if a stricter scope-purity audit is desired.

## Current contents

- `methods_catalogue.md` — the catalog itself, organized by the three layers.

## Format conventions

Each entry includes: identifier (METH-L{1,2,3}-NNN), name, brief description, canonical citation (paper/patch/sketch section where the method was developed or first applied in physics work), and one or two example physics-derivation applications. Entries are append-only; new techniques get added as separate entries rather than expanding existing ones.

## Naming convention: METH-L{1,2,3}-NNN

Catalog entries are identified by `METH-L{layer}-NNN` where layer ∈ {1, 2, 3} and NNN is a zero-padded sequence number unique within the layer. This parallels existing programme registry identifiers (`OPEN-XX-NNN`, `THEO-NNN`, `PRED-NNN`, `FI-X-NNN`, `CONJ-NNN`) so methods are grep-able alongside them.

The layer prefix carries semantic content: `L1` is a mathematical technique for physics derivation, `L2` is a methodological discipline for physics derivation work, `L3` is a heuristic strategy for physics problem-solving. The triple of layers is independent inventories, not a strict hierarchy; cross-layer references appear inline within entries.

Numbering is monotonic within a layer; resolved or superseded entries retain their numbers (with status marked in the entry itself) rather than being renumbered, preserving citation stability. Reversed entries (entries that were registered and then removed as out-of-scope, e.g., the Patch 0460→0461 METH-L2-007/008 + METH-L3-007 reversal) leave the numbering slot vacant — METH-L2-007 and METH-L2-008 are available for *physics-scoped* future Layer 2 entries; METH-L3-007 is available for a *physics-scoped* future Layer 3 entry.

## The three categories of method entry

When a session uses a physics derivation method, classify it before deciding whether to register a catalog entry:

- **NEW METHOD.** A genuinely new physics-derivation technique invented during the session — not a specialization or variant of any existing catalog entry. Antipodal-pair refinement of stabilizers (METH-L1-005) was a NEW METHOD when introduced at Patch 0439; the technique did not exist in the catalog prior. NEW METHOD entries get a fresh METH-L{1,2,3}-NNN identifier and a full entry.

- **ADAPTED METHOD.** An existing physics-derivation method customized for a sector or context with sector-specific content. Combined-CP for qDP (Patch 0439) is the combined-symmetry-generator method (METH-L1-006) adapted with qCP-sign content; it warrants a variant entry pointing to its parent rather than treatment as a new method. ADAPTED METHOD entries get a sub-identifier like METH-L1-006a (or a parallel METH-L{1,2,3}-NNN entry with an explicit "Adapted from METH-L1-006 with content: ..." back-pointer), and a shorter entry that focuses on the adaptation rather than re-describing the parent technique.

- **STRAIGHT REUSE.** An existing physics-derivation method applied as-is to a new physics context, no new content added. K3-doublet cage-shell averaging via Schur orthogonality (Patch 0397) was new; W-bracelet cage-shell averaging via the same Schur orthogonality on a different stabilizer (Patch 0427) is STRAIGHT REUSE — same technique, different stabilizer. STRAIGHT REUSE does NOT warrant a new entry. The derivation cites the parent identifier (METH-L1-001) inline; the catalog stays clean.

The category boundary between ADAPTED METHOD and STRAIGHT REUSE will be slippery in some cases. When in doubt, register as ADAPTED and link to the parent retrospectively. The risk of under-registering an adaptation is loss of the discovery context; the risk of over-registering is at most some catalog clutter that can be merged later.

## Threshold rule (what warrants a catalog entry)

A physics-derivation method warrants a named entry only if **it is reusable across at least one other physics-derivation context** — meaning the AI collaborator (human or otherwise) could plausibly look it up and apply it to a different sector, paper, or physics problem shape. Single-application techniques (the specific algebraic manipulation in step 7 of THEO-CAP-1, say) do NOT get named entries. The derivation just cites the underlying named technique it specializes.

Without this threshold, the catalog inflates into noise and stops being useful. The threshold protects the catalog's signal-to-noise ratio as it grows.

The Reading C closure trajectory over 17 patches produced approximately 7 named Layer 1 techniques + 6 Layer 2 disciplines + 6 Layer 3 heuristics — roughly one named method per 2-3 patches across a substantive multi-session arc, with many patches producing zero new entries. That's the realistic rate for *physics-substantive* sessions. Sessions that introduce novel physics-analytical surprises (Q5-PAIRING resolution, Q6-PAIRING resolution, §13 §12 correction discovery) are the ones that produce catalog entries; routine sessions applying existing methods produce zero. Sessions whose substantive work is protocol-pattern or workflow-discipline rather than physics derivation produce zero methods_catalogue entries (their substantive content goes to the homes listed under "Out of scope" above).

## Inline-citation convention in derivations

Physics-derivation work (sketches, papers, reasoning files) cites catalog entries inline using the format `[METH-L{layer}-NNN method-name]`. Example uses in physics derivations:

- "By Schur orthogonality [METH-L1-001 Schur orthogonality for cage-shell averaging], the cage-shell factor equals $d_E/|I_h| = 2/12 = 1/6$."
- "Per the register-then-resolve discipline [METH-L2-002], Q6-PAIRING is registered as an explicit open structural sub-question rather than resolved under the current patch's deadline."
- "When the matrix element vanishes under naive 1-vertex framing, the heuristic [METH-L3-001 vanishing matrix element → look for combined-symmetry generators] points at antipodal-pair refinement and combined-CP $\zeta$ identification."

The inline-citation convention is the teaching-tool value: physics derivations become step-by-step legible because each move is anchored in a named method the reader can look up. Future-window AI collaborators (and human readers) can follow the proof move-by-move with full knowledge of which technique licenses each step.

## How to use this

When approaching a new physics-closure problem: skim Layer 3 to find heuristics matching the physics problem shape; the heuristic will point at a discipline in Layer 2; the discipline will draw from techniques in Layer 1. This is the same path the AI collaborator implicitly traverses when problem-solving in physics; making it explicit lets the path be checked, criticized, and improved.

When approaching a new protocol / workflow / discipline question (e.g., "how should we handle this kind of session close?", "how should reviewer disagreements be navigated?", "how should we structure this kind of patch?"), do *not* search this catalog — search `templates/operating_system.md`, `relationship_protocol.md`, `founders_voice/`, `programmatic_decisions/`, and `opus_voice/` instead.

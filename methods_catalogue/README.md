# methods_catalogue/

A central catalog of the problem-solving methods used across CPP work. The catalog is **three-layered** by design — mathematical techniques at the substrate, methodological disciplines as the load-bearing structure, heuristic strategies at the pattern-matching top.

## Why this exists

Across the Reading C closure trajectory (Sessions 124-133, Patches 0417-0443) and earlier closure arcs (SF-4 Sessions 37-54, SS-9 Sessions 12-32, the SM-line work), the same methods got applied repeatedly to different sectors. The methods are real and reusable — but they were scattered across `templates/operating_system.md`, `founders_voice/NNN`, individual sketch files, and Tier 4 reasoning documents with no central listing. A future researcher (human, AI, or otherwise) inheriting CPP could not quickly answer "what techniques does this programme use?" without reading dozens of files.

The methods catalog answers that question.

## The three layers

**Layer 1 — Mathematical techniques.** Specific mathematical tools: theorems, lemmas, formal procedures, computational methods. Each is well-defined, instantiable, and produces concrete output when applied to concrete input. Examples: Schur orthogonality, Wigner-Eckart factorization, branching rule analysis $G \downarrow H$. These are the substrate.

**Layer 2 — Methodological disciplines.** Higher-order rules about how Layer 1 techniques get deployed: when to apply which technique, what counts as adequate rigor at which stage, how to organize derivation work. Examples: Layer A/B/C epistemic decomposition (separates derived content from imported formalism), register-then-resolve discipline (don't resolve an analytical complication under deadline pressure; register it explicitly and resolve in a dedicated patch), three converging arguments standard for Layer 2 closures. These are the load-bearing structure.

**Layer 3 — Heuristic strategies.** Pattern-recognition rules for which methodological discipline (and hence which mathematical technique) to apply to a given problem shape. Examples: when a matrix element vanishes under naive framing, look for combined-symmetry generators; when a sector instance derives a result, audit whether sister sectors inherit structurally. These are the top-layer pattern matchers.

## How the layers relate

Layer 3 is what the AI collaborator does first when encountering a new problem — recognize the shape. Layer 2 is the discipline structure for how to convert that recognition into a closure sequence. Layer 1 is the technique stack the discipline draws from.

A worked example of all three layers operating together: Q6-PAIRING at Patch 0439. Layer 3 noticed the matrix element vanishing pattern (heuristic: vanishing under naive framing → look for combined-symmetry generators). Layer 2 applied the register-then-resolve discipline (Q6-PAIRING was registered Patch 0438, resolved Patch 0439). Layer 1 deployed Wigner-Eckart factorization on a $D_{5d}$ stabilizer with antipodal-pair refinement.

## Status

**Stub.** This catalog is a seed at Session 133 Patch 0449 close. Initial entries enumerate techniques and disciplines actually used in the Reading C closure trajectory plus reference earlier work. Full catalog completion is queued as **OPEN-ORG-016** (organizational frontier) for future-window work.

## Current contents

- `methods_catalogue.md` — the catalog itself, organized by the three layers.

## Format conventions

Each entry includes: name, brief description, canonical citation (paper/patch/sketch section where the method was developed or first applied), and one or two example applications. Entries are append-only; new techniques get added as separate entries rather than expanding existing ones.

## How to use this

When approaching a new closure problem: skim Layer 3 to find heuristics matching the problem shape; the heuristic will point at a discipline in Layer 2; the discipline will draw from techniques in Layer 1. This is the same path the AI collaborator implicitly traverses when problem-solving; making it explicit lets the path be checked, criticized, and improved.

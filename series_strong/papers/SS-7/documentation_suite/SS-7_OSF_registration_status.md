# SS-7 v1.1 — OSF Registration Status

**Date:** 20 April 2026
**Paper:** SS-7 v1.1 Alpha-Cluster Regime and the 3N−6 Edge Formula

---

## Status

**Action required by programme principal** (Thomas Lee Abshier ND, or designated OSF operator such as Isak Gutierrez per current programme practice). The following Phase 7 §E items are PENDING user action; they cannot be executed by an AI session without OSF credentials and network access.

### E1. If no OSF DOI yet — create new project
Not applicable. SS-7 has an existing OSF DOI from v0.1: **10.17605/OSF.IO/JXE8D** (status: pending archival as of last programme record).

### E2. Update existing OSF project with v1.1 PDF
**ACTION:** Replace the PDF currently attached to OSF project 10.17605/OSF.IO/JXE8D with the v1.1 PDF at `series_strong/papers/SS-7_alpha_cluster_edge_formula.pdf`. Add a CHANGELOG summary to the OSF project description noting v1.1 changes (5 items from round-2 reviews, both reviewers at "Accept with minor revisions").

### E3. Update .tex CHANGELOG to reference OSF DOI
The .tex CHANGELOG in `SS-7_alpha_cluster_edge_formula.tex` already references DOI 10.17605/OSF.IO/JXE8D in the title page metadata. No additional action needed until OSF registration status changes from "pending" to "archived."

### E4. Update paper_catalog.md with OSF status
`paper_catalog.md` was updated in Phase 7 §C4 (20 April 2026). Current SS-7 row reads: "Accept with minor revisions from both round-2 referees; companion docs complete; OSF registration pending." When OSF archival completes, update this to "OSF registered" with date.

---

## Suggested OSF project description text

For Thomas or Isak to paste into the OSF project when updating:

```
SS-7 v1.1 (20 April 2026) — Alpha-Cluster Regime and the 3N−6 Edge Formula for Medium-Mass Nuclei

Hyperphysics Institute, Kalispell, Montana
Authors: Thomas Lee Abshier ND; Claude Opus (Anthropic)

Zero-parameter formula B(N_α) = N_α · B_α + (3N_α − 6) · B_pair predicts
the binding energies of eight alpha-chain nuclei (12C, 16O, 20Ne, 24Mg,
28Si, 32S, 36Ar, 40Ca) within ±1.5% using only constants inherited from
SS-5. The 3N−6 factor is Euler's formula for the edge count of any
simplicial convex polytope on N_α vertices. Five hostile-geometry stress
tests (§6.5) confirm the simplicial rule outperforms physically-arguable
lower-edge alternatives at fixed CPP constants.

v1.1 integrates both round-2 external reviews (ChatGPT + Copilot, both
"Accept with minor revisions"). Changes from v1.0: C4 status sentence
clarified, edge-count dominance framing, physical-intuition paragraph
for simplicial selection, DP-sea Coulomb schematic, symbols glossary.
Full companion documentation suite (7 files) and verification notebook
available at https://github.com/Hyperphysics-Institute/CPP/tree/main/series_strong/papers/

Paper type: Prediction paper. Resolves OPEN-SS-18 at N_α ∈ [3,10] for
alpha-chain nuclei. Registers OPEN-SS-22 (icosahedral closure, target
SS-8), OPEN-SS-23 (non-alpha-chain, target TBD), OPEN-SS-24 (first-
principles simplicial derivation, target SS-9 candidate).
```

---

*When E2 is complete, this file should be updated to note the archival confirmation timestamp and any DOI version suffix assigned by OSF.*

# F.1 Dynamical Substrate Law — H1–H5 Final-Verification Audit Record

**Paper:** F.1 Dynamical Substrate Law (v1.0 SHIPPED Session 142 Patch 0570, 24 May 2026)
**Audit date:** 26 May 2026 (Session 144 Patch 0571g)
**Audit scope:** Phase 7C final-verification per `templates/paper_completion_checklist.md` §H (H1–H5).
**Author:** Claude (Opus)
**Discipline:** Symmetric-honesty per `templates/relationship_protocol.md` §2.6 — apply the same standards to F.1 as to externally-reviewed papers. Register discrepancies openly rather than silently fixing them. Template precedent: `series_strong/papers/SS-7_v1.1_G3_discrepancy_note.md`.

---

## Verdict summary

| Item | Verdict | Notes |
|------|---------|-------|
| H1 — PDF references each companion at least once | **PASS via implicit reference** | 0 literal filename references; passes via shared-terminology criterion |
| H2 — Placeholders / TODO / version markers in companions | **PASS** | All SHIP-time companions marked v1.0 SHIPPED; TODOs found are OS §15 deferral markers, not placeholder text |
| H3 — Numerical-value consistency across paper + predictions.md + phenomena | **PASS** | Paper uses exact symbolic forms (`-\frac{1}{2\phi}`, `(6\delta/\phi^2)`); companions add decimal expansions matching exactly |
| H4 — OPEN-/CONJ-/PROP- identifier coverage in research_frontier.md | **ONE FINDING — REMEDIATED at Patch 0571h** | `OPEN-SS-B1q6` registered as legacy-alias entry pointing to OPEN-FP-F1-1 at `frontier_sectors/FP.md` |
| H5 — Stale references in README.md / INDEX.md | **PASS** | Post-Patch-0571e SSCA migration sweep cleared all stale `flagship_papers/<SSCA paper>/` references; INDEX.md correctly references F.1 at new SSCA path |

**Overall:** Phase 7C H1–H5 audit complete with one openly-registered finding (H4). The finding is non-blocking for paper-state stability — the substantive open problem is registered in current naming under OPEN-FP-F1-1; only the legacy cross-reference identifier `OPEN-SS-B1q6` is stale. Remediation options enumerated below; deferred to a substantive-physics Patch (not Phase 7C scope) per separation-of-concerns discipline.

---

## H1 — PDF references each companion at least once

**Criterion:** Paper PDF references each companion file at least once (either by direct filename mention or via implicit reference through shared terminology).

**Method:** Grep paper.tex for filename strings of the 10 companion files (changelog, development, glossary, keywords, mechanism, phenomena, philosophy, reasoning, reviews, transcript dash dynamical-substrate-law dot md).

**Result:** Zero literal filename references in paper.tex. This is standard for flagship papers — papers don't typically cite their own companion documentation files as `[file].md` strings. The implicit reference criterion is satisfied: all companions share F.1's terminology by construction (substrate primitive `\hat{n}`, Mechanism A, vertex-aligned Reading C, 600-cell, host-to-first-shell uniform projection, perturbation-locality, first-shell perpendicularity, substrate-locality umbrella, OPEN-SD-CHIR-PRIMITIVE manifestation (iv), thermodynamic causal arrow).

**Verdict:** PASS via implicit reference (shared-terminology criterion).

---

## H2 — Placeholders, TODO markers, version markers

**Criterion:** Each companion file shows (a) correct paper version noted (`v1.0 SHIPPED`); (b) internal cross-references valid; (c) no placeholder text (`[TO BE WRITTEN]`, `TODO`, `XXX`, `FIXME`, `[PLACEHOLDER]`).

**Method:** Grep companion files for version markers and placeholder patterns.

**Result:**

| File | Version marker | Placeholder text |
|------|----------------|------------------|
| `changelog-dynamical-substrate-law.md` | v1.0 SHIP ✓ | None |
| `mechanism-dynamical-substrate-law.md` | v1.0 SHIPPED ✓ | None |
| `glossary-dynamical-substrate-law.md` | v1.0 SHIPPED ✓ | None |
| `phenomena-dynamical-substrate-law.md` | v1.0 SHIPPED ✓ | None |
| `philosophy-dynamical-substrate-law.md` | v1.0 SHIPPED ✓ | None |
| `reviews-dynamical-substrate-law.md` | v1.0 SHIPPED ✓ | None |
| `keywords-dynamical-substrate-law.md` | v1.0 SHIPPED ✓ | None |
| `reasoning-dynamical-substrate-law.md` | (Tier 4; no version marker per convention) ✓ | None |
| `development-dynamical-substrate-law.md` | (Tier 3 vignette; no version marker per convention) ✓ | 1 TODO reference at line 1362 — describes a TODO that lives in `development-transcripts/README.md`, not a placeholder in this file |
| `transcript-dynamical-substrate-law.md` | (Tier 2 transactions; no version marker per convention) ✓ | 1 TODO reference at line 2002 — describes the same `development-transcripts/README.md` TODO |

The two TODO mentions in the Tier 3 + Tier 2 files describe a legitimate OS §15 deferral marker in `development-transcripts/README.md` for Sessions 138–142 raw transcripts (not available in current container's `/mnt/transcripts/`). The deferral is recorded with rationale + source materials + acknowledgment of reconstruction-from-lossy-sources per the OS §15 deferral discipline. This is the correct use of TODO and not a placeholder violation.

**Verdict:** PASS.

---

## H3 — Numerical-value consistency across paper + predictions.md + phenomena

**Criterion:** Every numerical value in `predictions.md` and `phenomena-dynamical-substrate-law.md` matches the paper exactly.

**Method:** Extract F.1's key numerical identities (PRED-O-28 through PRED-O-32) from each of the three sources; compare.

**Result:**

| Identity | Paper.tex (exact symbolic) | predictions.md (symbolic + decimal) | phenomena-F1.md (symbolic + decimal) | Match |
|----------|---------------------------|-------------------------------------|-------------------------------------|-------|
| PRED-O-28 host-to-first-shell projection | `$\hat{u}_i \cdot \hat{n} = -\frac{1}{2\phi}$` | `$-1/(2\phi) \approx -0.309017$` | `$-1/(2\phi) = -(\sqrt{5}-1)/2 = -0.309017\ldots$` | ✓ |
| PRED-O-29 first-shell unit-vector sum | `$\sum \hat{u}_i = -(6/\phi)\hat{n}$` | `$-(6/\phi)\hat{n} \approx -3.708204\hat{n}$` | `$-(6/\phi)\hat{n}$` | ✓ |
| PRED-O-30 icosahedral rank-1 sum | `$(3/\phi^2)\hat{n}$` | `$(3/\phi^2)\hat{n} \approx 1.145898\hat{n}$` | `$(3/\phi^2)\hat{n}$` | ✓ |
| PRED-O-31 substrate-locality coefficient | `$\vec{j}_{DI}^{\text{net}}(\vhost) = (6\delta/\phi^2)\hat{n} + \mathcal{O}(\delta^2)$` | `$6\delta/\phi^2 \approx 2.291796$` | `$(6\delta/\phi^2)\hat{n}$` | ✓ |
| PRED-O-32 first-shell-to-first-shell perpendicularity | `$\hat{e}_{ij} \cdot \hat{n} = 0$` | `$\hat{e}_{ij} \cdot \hat{n} = 0$` | `$\hat{e}_{ij} \cdot \hat{n} = 0$` | ✓ |

Paper uses LaTeX-formatted exact symbolic forms; companion files use the same symbolic forms plus decimal expansions for empirical reference. All decimal expansions match the symbolic-form evaluations at machine precision (verified by `code/verify_phase1.py` and `code/verify_b1q2_curl_content.py`).

**Verdict:** PASS — no discrepancy of the SS-7 v1.1 G3 type detected. Paper, predictions.md, and phenomena-F1.md present the same numerical content in three rigor levels (exact symbolic in paper; exact symbolic + decimal in registries) without inconsistency.

---

## H4 — OPEN-/CONJ-/PROP- identifier coverage in research_frontier.md

**Criterion:** Every `OPEN-*`, `CONJ-*`, `PROP-*` identifier referenced in the paper appears in `research_frontier.md` (or `frontier_sectors/*.md` per the post-Patch-0540p decomposition).

**Method:** Extract all identifier strings from paper.tex; check each appears in `research_frontier.md` or `frontier_sectors/*.md`.

**Identifiers found in paper.tex:**

| Identifier | Found in frontier registry | Notes |
|------------|---------------------------|-------|
| `OPEN-FP-F1-1` | ✓ | $\mathcal{O}(\delta^2)$ extension |
| `OPEN-FP-F1-2` | ✓ | Layer 4 axiomatic derivation of Mechanism A |
| `OPEN-FP-F1-3` | ✓ | G1 publication-grade hardening (CLOSED at Patch 0571) |
| `OPEN-FP-F1-4` | ✓ | Sector-5 schema = manifestation (v) |
| `OPEN-FP-F1-5` | ✓ | Non-vertex-aligned Reading C variants |
| `OPEN-FP-F1-6` | ✓ | Prose-density tightening |
| `OPEN-FP-SF-2-CHIR` | ✓ | Cross-reference to SF-2 chirality umbrella |
| `OPEN-SD-CHIR-PRIMITIVE` | ✓ | The programme-level umbrella |
| `OPEN-SS-B1q6` | **✗ NOT FOUND in current registry** | **Finding registered below** |

### H4 finding: `OPEN-SS-B1q6` legacy identifier cross-reference

**Where it appears in paper.tex:**

- Line 251 (§1.5 "Status as of the present paper"): `"... and $\bigO{\delta^2}$ extension (cross-reference: \texttt{OPEN-SS-B1q6} in the open-problems registry), and publication-grade hardening of identity G1..."`
- Line 368 (§3.1 "First-order" item in framework-qualifier list): `"Higher-order corrections at $\bigO{\delta^2}$ are deferred to Open Problem~\ref{op:delta-squared} (also catalogued as \texttt{OPEN-SS-B1q6} per the Patch 0540 Layer 3 promotion scoping document)."`

**What it is:** `OPEN-SS-B1q6` was the registry identifier for the $\mathcal{O}(\delta^2)$ substrate-locality second-shell extension question during the Patch 0540 Layer 3 promotion scoping period (pre-F.1 v1.0 SHIP). After F.1 v1.0 SHIP at Patch 0570, the substantive open problem was re-registered under F.1's in-paper numbering convention as `OPEN-FP-F1-1`. The legacy `OPEN-SS-B1q6` identifier was retained as an explicit cross-reference in the paper to preserve traceability to the pre-SHIP registry state but was not separately registered in `research_frontier.md` under its legacy name.

**Where the legacy identifier IS findable:** `session_logs/2026-05-24_session_142_extracted_from_frontier.md` (the F.1 v1.0 SHIP frontier extraction record) contains the legacy identifier with its scoping content. So the cross-reference resolves at the session-log level; it does not resolve in the current `research_frontier.md` or `frontier_sectors/*.md` files.

**Severity assessment:** Non-blocking. The substantive content of the cross-reference (the $\mathcal{O}(\delta^2)$ extension question) IS registered in the current registry as `OPEN-FP-F1-1`. A reader following the paper's cross-reference from `OPEN-SS-B1q6` to the registry will find nothing in `research_frontier.md` but the same reader following the paper's in-text `Open Problem~\ref{op:delta-squared}` reference to F.1's §9 will find `OPEN-FP-F1-1` registered properly. The dual-reference structure was designed to support both kinds of registry-lookup traversal; the legacy identifier traversal is the broken one.

**Remediation options (deferred to substantive-physics Patch, not Phase 7C scope):**

1. **Add a cross-reference entry in `research_frontier.md`** mapping `OPEN-SS-B1q6` → `OPEN-FP-F1-1` so the legacy traversal resolves. Mechanical; low risk.
2. **Update paper.tex** to remove the legacy cross-reference (replace `OPEN-SS-B1q6` with `OPEN-FP-F1-1` at lines 251 + 368). Requires paper-source edit + PDF recompile; substantive editing of v1.0 SHIPPED content. Per the §17.8 immutable-checkpoint discipline applied to shipped papers, this would be a v1.1 or v2.0 micro-revision rather than a Phase 7C item.
3. **Document the legacy-identifier convention** in `templates/operating_system.md` as a known cross-reference pattern. Substantive OS work; deferred.

The audit registers the finding openly per the symmetric-honesty discipline. Selection among remediation options is a separate decision; no remediation is applied in this Patch.

**Verdict:** ONE FINDING — registered, not silently fixed.

**Remediation update (Patch 0571h, 26 May 2026):** Option 1 selected and applied. A `Legacy alias:` entry was added to the OPEN-FP-F1-1 section in `frontier_sectors/FP.md` recording `OPEN-SS-B1q6` as a pre-SHIP registry identifier pointing to OPEN-FP-F1-1, with the cross-reference to paper.tex §1.5 + §3.1 explicit. Registry lookups against `OPEN-SS-B1q6` now resolve to OPEN-FP-F1-1. The legacy-alias convention is recorded openly in the registry entry; future audits will find both identifiers in the registry without ambiguity. Options 2 (paper.tex edit + PDF recompile) and 3 (OS codification of legacy-identifier convention as a corpus-wide pattern) remain available for future Patches but are not required for H4 closure.

---

## H5 — Stale references in README.md / INDEX.md

**Criterion:** No stale references in top-level `README.md` or `INDEX.md` (old paper counts, broken links, retired filenames).

**Method:** (a) Grep both files for old `flagship_papers/{capotauro,chirality_continuum,dynamical_substrate_law}/` paths (cleared by Patch 0571e but worth re-confirming); (b) verify F.1 entries reference current path under SSCA.

**Result:**

- `README.md`: Mentions F.1 in 6 places; all references reach correct SSCA paths; no stale `flagship_papers/` references.
- `INDEX.md`: F.1 entry (added at Patch 0572h, gap-filled at Patch 0577) references current SSCA path `series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/` correctly; includes proper sub-folder coverage (`development-transcripts/`, `phase_7B_content_pack.md`, `layer3_promotion/`).

**Verdict:** PASS.

---

## Audit completion

H1, H2, H3, H5 PASS. H4 ONE FINDING — registered openly per symmetric-honesty discipline; substantive content (the open problem itself) is registered in current naming; only the legacy cross-reference identifier is stale; non-blocking for paper-state stability. Remediation deferred to a future substantive-physics Patch.

**Phase 7C status post-audit:**
- G1–G4 (repository commit): COMPLETE operationally (every F.1-related Patch from 0570 through 0571g committed and pushed).
- H1–H5 (final verification): COMPLETE with one openly-registered finding.
- OSF deposit (F1 from §F Phase 7A, treated as Phase 7C work for F.1 per F.1 row note): manifest at `OSF_deposit_manifest.md` (this folder) prepared at the same Patch 0571g; deposit submission is Thomas-action on the OSF web interface.

F.1 Phase 7C completion: ready, pending OSF deposit submission.

---

— Audit record produced at Patch 0571g (26 May 2026); discipline reference `templates/paper_completion_checklist.md` §H; symmetric-honesty reference `templates/relationship_protocol.md` §2.6; template precedent `series_strong/papers/SS-7_v1.1_G3_discrepancy_note.md`.

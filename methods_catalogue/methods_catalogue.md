# Methods Catalogue

**Status:** STUB seed at Session 133 Patch 0449; extended Session 134 Patch 0460 with three entries from the Patch 0457→0458→0459 protocol-correction arc (METH-L2-007 + METH-L2-008 + METH-L3-007). Initial entries from Reading C closure trajectory (Patches 0417-0443) plus references to earlier work + protocol-correction arc Patch 0457-0459; **22 entries (7 L1 + 8 L2 + 7 L3)** carrying METH-L{1,2,3}-NNN identifiers per naming convention adopted Patch 0449a. Full catalog completion is OPEN-ORG-016 (Phase 1 back-fill + Phase 2 per-paper-SHIP + Phase 3 per-session).

**Format:** Each entry has *Name* / *Description* / *Canonical citation* / *Example applications*. Layered as Layer 1 (mathematical techniques) → Layer 2 (methodological disciplines) → Layer 3 (heuristic strategies). The three layers are independent inventories, not a strict hierarchy; cross-layer references appear inline.

---

## Layer 1 — Mathematical techniques

### METH-L1-001: Schur orthogonality for cage-shell averaging

**Description.** Average a tensor operator over a finite group's irreducible representations using Schur orthogonality relations to extract the irrep-specific projection magnitudes. Reduces cage-shell averaging to evaluation of $d_{\text{irrep}}/|G|$ for the relevant 2D irreps.

**Canonical citation.** Capotauro v1.0 §10 (`flagship_papers/capotauro/capotauro.tex`), Patch 0397 THEO-CAP-1 derivation step 8.

**Example applications.** K3-doublet cage-shell factor $|M_\perp^{K3}| = d_E/|I_h| = 2/12 = 1/6$ (Capotauro v1.0). W-bracelet identical factor on $D_6$ stabilizer (Finding C-W41, Patch 0427). qDP/eDP factor on $D_{5d}$ after antipodal-pair refinement (Finding C-W45, Patch 0438).

### METH-L1-002: Wigner-Eckart factorization

**Description.** Factor a matrix element $\langle f | \hat{O} | i \rangle$ where $\hat{O}$ transforms as a definite irrep of the symmetry group, into a geometric Clebsch-Gordan coefficient times a reduced matrix element. Used here to factor cross-sector matrix elements into (chirality-coupling factor) × (cage-shell factor).

**Canonical citation.** Standard quantum-mechanical textbook (Sakurai); applied in CPP at Capotauro v1.0 §5.3-§5.4.

**Example applications.** K3-doublet $|M^{K3}|$ factorization (Capotauro v1.0). W-bracelet $|M^W|$ factorization on $E_2 \oplus E_1$ in $D_6$ (Finding C-W43, Patch 0429). qDP/eDP $|M^{qDP}|$ factorization on $A_{1g} \oplus A_{2u}$ in $D_{5d}$ (Finding C-W46, Patch 0439).

### METH-L1-003: Branching rule analysis ($G \downarrow H$)

**Description.** Decompose irreps of a group $G$ into irreps of a subgroup $H \subset G$. Used to track how chirality operators transform under sector-specific stabilizer subgroups.

**Canonical citation.** Standard representation theory; applied in CPP at sketch §17.10 (W-bracelet $E_2 \oplus E_1$ in $D_6$ via $I_h \downarrow D_6$ branching).

**Example applications.** qDP/eDP $A_u(I_h) \downarrow A_2(C_{5v})$ branching (sketch §19, Patch 0438). $D_{5d}$ chirality operator $A_{2u}$ identification (sketch §20, Patch 0439).

### METH-L1-004: Coxeter parabolic-subgroup theory

**Description.** Use Coxeter group structure to identify which subgroup-fixed subspaces of a Coxeter polytope contain the chirality-bearing direction. Applied here to identify $H_3 = I_h$ as the vertex-aligned stabilizer of $\hat{n}$ in $H_4$.

**Canonical citation.** Humphreys, *Reflection Groups and Coxeter Groups*; applied in CPP at sketch §11-§12 (Patch 0417).

**Example applications.** Q1+Q2 closure identifying $\hat{n}$ stabilizer as $H_3 = I_h$ (Patch 0417).

### METH-L1-005: Antipodal-pair refinement of stabilizers

**Description.** When a 1-vertex framing produces a vanishing matrix element, refine the substrate object's effective stabilizer by pairing the vertex with its antipode, producing a larger stabilizer ($D_{nd}$ rather than $C_{nv}$) that supports non-vanishing irrep content.

**Canonical citation.** sketch §20 (Patch 0439), introduced in qDP/eDP Q6-PAIRING resolution.

**Example applications.** qDP/eDP $C_{5v}$ → $D_{5d}$ refinement (sketch §20). Anticipated for future manifestations (iv)+(v) closures.

### METH-L1-006: Combined-symmetry generators extending purely-geometric ones

**Description.** When a substrate sector has additional internal degrees of freedom beyond geometric structure (e.g., qCP sign, time direction), the $\zeta$ generator that produces non-vanishing matrix elements may need to combine geometric inversion with operations on the internal degrees. CP combines spatial inversion with charge conjugation.

**Canonical citation.** sketch §20.4-§20.5 (Patch 0439), introduced for qDP/eDP $\zeta^{qDP} = $ host-CP-centered spatial inversion + $\hat{n}$-flip + qCP-sign flip.

**Example applications.** qDP/eDP Q6-PAIRING resolution (Patch 0439). Anticipated extension for manifestations (iv) thermodynamic causal arrow (likely incorporates time-direction reversal) and (v) cosmological-vacuum asymmetry (likely incorporates cosmological-epoch sign).

### METH-L1-007: Numerical verification at machine precision

**Description.** When a derivation depends on a geometric identity (e.g., 4D edge tangency, dot product evaluation), implement the geometry numerically and verify the claimed identity holds to $< 10^{-9}$. Catches geometric errors that purely symbolic reasoning misses.

**Canonical citation.** Patch 0424 §13 local-$I_h$-preservation verification (`flagship_papers/capotauro/code/sketch_section_13_local_ih_preservation.py`).

**Example applications.** §13 §12 geometric error caught and corrected (Finding C-W39 supersedes C-W38, Patch 0424). Q1' vertex-alignment verification (Patch 0418-0419).

---

## Layer 2 — Methodological disciplines

### METH-L2-001: Layer A/B/C epistemic decomposition

**Description.** Decompose a derivation into Layer A (CPP-derived content), Layer B (imported formalism whose CPP-derivation is open), Layer C (empirical inputs). The decomposition makes the load-bearing inputs explicit so each can be audited independently.

**Canonical citation.** SM-3 K3/Koide work (Sessions 14-22), applied programme-wide.

**Example applications.** THEO-CAP-1 audit: Layer A = chirality matching + cage-shell averaging; Layer B = Wigner-Eckart formalism (registered as OPEN-SS-16); Layer C = empirical $\Delta p_{LR}$ value.

### METH-L2-002: Register-then-resolve discipline

**Description.** When an analytical complication surfaces during a closure attempt, register it explicitly as a sub-question (with letter ID, e.g., Q5-PAIRING, Q6-PAIRING) and defer its resolution to a dedicated patch rather than trying to resolve it under deadline pressure within the active patch.

**Canonical citation.** sketch §16.12 (Patch 0428), §21.6 (Patch 0441). Pattern formalized at sketch §16.12 from prior occurrences.

**Example applications.** Q5-PAIRING registered Patch 0428, resolved Patch 0429. Q6-PAIRING registered Patch 0438, resolved Patch 0439. Q7 scoping at Patch 0441 applied this discipline at scoping level (four sub-questions Q7.1-Q7.4 registered without forced closure attempts).

### METH-L2-003: Three converging arguments standard for Layer 2 closures

**Description.** A Layer 2 closure (structural argument, not yet full Layer 3 rigor) is registered as adequate when three structurally independent arguments converge on the same identification. Single arguments are tentative; three converging arguments are load-bearing.

**Canonical citation.** Patch 0419 Q1'+Q1'.A resolution (three converging arguments for vertex-aligned reading: paper-internal hosting language + cross-sector unification with SF-2 + SM-1 first-shell preservation).

**Example applications.** Q1' vertex-alignment resolution (Patch 0419). Anticipated for Q7.1 substrate-level sign-selection mechanism when assessed against CPP axioms.

### METH-L2-004: Symmetric-honesty discipline

**Description.** Apply the same epistemic standards to own work as to reviewer feedback. If you would push back on a reviewer claiming a Layer 2 result is Layer 3, push back equally hard when tempted to claim your own Layer 2 work is Layer 3.

**Canonical citation.** `founders_voice/004_verbatim_substance_preservation_discipline.md`. Originated from Session 132 reviewer-suspension event (Grok vocabulary contamination).

**Example applications.** §13 §12 geometric error preservation as substantive correction rather than silent fix (Patch 0424). Q5-PAIRING and Q6-PAIRING explicit registration rather than glossing.

### METH-L2-005: Cross-sector unification audit

**Description.** When a result is derived for one sector, audit whether sister sectors inherit the result structurally. The audit operates at two levels — mechanism-level (do sister sectors share the same closure pattern?) and magnitude-level (do they produce identical numerical magnitude?).

**Canonical citation.** sketch §14 Finding C-W40 (Patch 0425) for mechanism-level. sketch §20.14 (Patch 0439) for magnitude-level.

**Example applications.** Reading C closure trajectory itself — K3-doublet result audited and found to extend to W-bracelet (THEO-SD-CHIR-1) and qDP/eDP (THEO-SD-CHIR-2).

### METH-L2-006: Three-step closure pattern

**Description.** Cross-sector closures under the OPEN-SD-CHIR-PRIMITIVE umbrella follow a uniform three-step pattern: (i) substrate-locality at Layer 2 with sector-specific stabilizer identified; (ii) cage-shell factor at Layer 3 via Schur orthogonality on the stabilizer; (iii) pairing-convention identification at Layer 3 via sector-specific $\zeta$ generator.

**Canonical citation.** Patches 0429 (K3/W) + 0439 (qDP/eDP). Formalized at sketch §19.11 + §20.14.

**Example applications.** All three Reading C closure trajectory manifestations followed this pattern. Anticipated template for manifestations (iv)+(v).

### METH-L2-007: Two-patch architecture for protocol-bug corrections

**Description.** When a methodological deficiency in a protocol's application is identified mid-arc, correct it via TWO paired patches rather than one. Patch N corrects the substance (backfills what was missed, fixes the specific instance); Patch N+1 corrects the discipline (amends the protocol itself to prevent recurrence). The two-patch architecture separates "fix this instance" from "fix the protocol so this instance can't recur." Each patch has clean scope and clean commit message; the audit trail makes both the corrective backfill and the corrective protocol amendment independently reviewable. A single patch combining substance + discipline becomes scope-heavy, hard to commit-message-summarize, and risks the discipline amendment being lost in the volume of substance content.

**Canonical citation.** Patches 0458 (Session 134 four-tier documentation backfill) + 0459 (§15 handover protocol amendment), 19 May 2026. Introduced after Patch 0457 misapplied the §15 Step B/C/D "N/A for sessions producing no substantive paper-scoped reasoning" escape valve to a session producing 12 substantive paper-scoped patches; the corrective response was Patch 0458 (backfill the missed Tier-4 + Tier-3 + Tier-2 entries) + Patch 0459 (amend §15 so the misapplication cannot recur).

**Example applications.** Patch 0458 + 0459 pair. Future-window: any protocol-bug correction follows the same two-patch architecture — e.g., a TATWD integration cadence misapplication would produce Patch N (TATWD catch-up integration) + Patch N+1 (cadence-rule amendment); a §10 commit-cadence underapplication would produce Patch N (commit-cadence catch-up batching) + Patch N+1 (§10 amendment); a relationship_protocol.md principle violation in a reviewer interaction would produce Patch N (corrective letter) + Patch N+1 (relationship_protocol.md amendment if the violation revealed a protocol gap).

### METH-L2-008: Universal vs situation-specific protocol distinction (with anti-pattern registration)

**Description.** When protocol design produces two adjacent protocols whose triggers can be confused (e.g., session-close handover discipline vs v1.0 SHIP closeout deliverables), explicitly distinguish them at the discipline level with four elements: (a) trigger criteria for each protocol; (b) artifact sets each protocol produces; (c) an explicit yes/no test for which protocol applies in a given situation; (d) anti-pattern language registering the failure mode (the wrong behavior the distinction protects against). Protocol amendments that fix a conflation bug should include all four elements; without (d), the bug can recur because the corrected protocol reads as "what to do" without "what NOT to do." The universal vs situation-specific dichotomy is itself a useful frame for protocol audit: ask whether each protocol fires at every session close (universal) or only at specific events like v1.0 SHIP / programme-architecture transitions / reviewer-round-convergence events (situation-specific). Two protocols at different cadences are at structurally different load-bearing positions and should never substitute for each other.

**Canonical citation.** Patch 0459 §15.10 (templates/operating_system.md), 19 May 2026. Introduced when separating universal session-close handover discipline (§15 8-step protocol firing at every session close where active paper / substantive in-flight work / compaction-imminent context state) from situation-specific v1.0 SHIP closeout deliverables (Patch 0449b protocol firing only when flagship paper transitions to v1.0 SHIPPED, producing anthology + 7-file documentation suite + TATWD + OSF + arXiv + binary artifact).

**Example applications.** §15.10 itself. Future-window candidates for the same treatment: TATWD integration cadence has a three-trigger structure (session-close cadence vs v1.0 SHIP cadence vs programme-architecture event cadence) where the cadences can be confused — applying METH-L2-008 to TATWD would produce explicit triggers + artifact sets + yes/no test + anti-pattern; the §10 commit-cadence discipline (section-end-batch vs handover-protocol-driven) has a similar two-trigger structure where commits can be misclassified.

---

## Layer 3 — Heuristic strategies

### METH-L3-001: Vanishing matrix element → look for combined-symmetry generators

**Description.** When a matrix element computation produces zero under a naive choice of $\zeta$ generator (typically purely-geometric inversion), the resolution is usually identification of a combined-symmetry generator that incorporates additional substrate degrees of freedom beyond the geometric ones.

**Citation.** sketch §20.4-§20.5 (Patch 0439). Heuristic identified retroactively from qDP/eDP $\zeta^{qDP}$ combined CP identification.

**Example deployment.** qDP/eDP Q6-PAIRING resolution.

### METH-L3-002: Sector instance → audit sister sectors

**Description.** When a structural result is derived for one sector under a programme-wide umbrella (e.g., OPEN-SD-CHIR-PRIMITIVE), immediately audit whether sister sectors inherit. The audit is cheap; the cross-sector unification it surfaces is valuable.

**Citation.** Reading C closure trajectory at scope level (Patch 0422 umbrella registration).

**Example deployment.** Patch 0425 Finding C-W40 (Substrate-Locality Unification) — K3 result audited for W-bracelet inheritance, then qDP/eDP inheritance.

### METH-L3-003: Suspicious foundational input → numerical verification at machine precision

**Description.** When a derivation depends on a foundational input whose geometric content is not obviously verified, implement the geometry numerically and check at $< 10^{-9}$. The verification often catches errors that pure symbolic reasoning misses.

**Citation.** Patch 0424 §13 verification, retroactively from §12 geometric error.

**Example deployment.** Local-$I_h$-preservation verification (Patch 0424), surfacing Finding C-W39 superseding C-W38.

### METH-L3-004: Closure trajectory saturation → consolidate via handover + outline

**Description.** When a multi-session closure trajectory has delivered its theorem-registry-level results and remaining open work shifts to a different shape, this is the right moment to consolidate via handover + outline-establishment patches, not to push for additional substantive work within the same window.

**Citation.** sketch §21.7 (Patch 0441), Reading C closure trajectory natural-end-state recognition.

**Example deployment.** Session 133 close — Patches 0442 (v2.0 outline) + 0443 (handover) before pivoting to v2.0 drafting in subsequent windows.

### METH-L3-005: Recurring problem shape → name it and register it

**Description.** When the same analytical pattern surfaces in two or more independent contexts, give it a name (e.g., "PAIRING", "three-step closure pattern") and register it explicitly. Naming the pattern makes it reusable as a Layer 2 discipline.

**Citation.** Q5-PAIRING (Patch 0428) and Q6-PAIRING (Patch 0438) → three-step closure pattern (sketch §19.11, Patch 0438).

**Example deployment.** Both PAIRING registrations and the subsequent pattern naming.

### METH-L3-006: Meta-conversation surfacing → capture before window close

**Description.** When a conversation surfaces meta-level content (reflections on the work's texture, methodological observations, framing questions) outside the standard paper-scoped reasoning that goes into sketches, the §15 handover Steps B/C may incorrectly mark these N/A. The correct move is to capture meta-conversation in a dedicated file (typically `opus_voice/NNN_<topic>.md`) before window close.

**Citation.** Patch 0449 (this patch) — `opus_voice/001`, `opus_voice/002` captured verbatim before Session 133 final close.

**Example deployment.** This patch itself. Lesson surfaced from observing the gap between sketch §13-§21 (substantive physics captured) and meta-conversation (lantern + methods + problem-shapes; not captured by default §15 protocol).

### METH-L3-007: Tier-3/4 deferral identification → immediate backfill while context fresh

**Description.** When a §15 handover protocol's Steps B/C/D are identified mid-arc as having been deferred or marked N/A incorrectly (typically: substantive paper-scoped reasoning occurred in the session but Tier-3/4 capture was skipped under deferral rationale like "we'll do this at v1.0 SHIP closeout" or "canonical record preserved in commit messages"), the corrective response is **immediate Tier-3/4 backfill from the still-fresh conversation context, BEFORE the next compaction or session close**. The conversation transcript is the highest-fidelity source for verbatim Opus reasoning and dies at session close; deferring backfill to a future session forces reconstruction-from-lossy-sources (commit messages, changelog entries, polished `.tex` source) which is substantively lossier than capture-while-fresh — particularly for methodological observations, decision arcs that surfaced and resolved within a single patch, and load-bearing physics choices that the polished output preserves the *result* of but not the *reasoning that produced it*. The heuristic operates at the meta-level on top of METH-L3-006 (meta-conversation capture): both share the underlying principle that conversation-context content is highest-fidelity-but-shortest-lived, and the corrective response to identification-of-loss is always immediate capture rather than deferral.

**Citation.** Patch 0458 (Session 134 four-tier documentation backfill), 19 May 2026. Heuristic identified retroactively from the Patch 0457→0458 correction sequence. The Patch 0457 deferral rationale ("canonical Tier-4 record is preserved in patch commit messages + changelog entries + .tex source; consolidated four-tier documentation suite update to be performed during v0.9 reviewer-round work cycle") was the failure mode; the Patch 0458 corrective response (immediate four-tier backfill from still-alive conversation context before window close) is the heuristic's canonical deployment.

**Example deployment.** Patch 0458 itself — Session 134 four-tier backfill executed mid-window after Patch 0457 deferral identification via user challenge ("Did it record the verbatim physics reasoning?"), recovering 296 lines of Tier-4 reasoning in reasoning-capotauro.md + 48 lines of Tier-3 vignettes in development-capotauro.md + 80 lines of Tier-2 pointer entries in transcript-capotauro.md that would have been lost-or-reconstructed-from-lossy-sources had the deferral to v0.9 reviewer-round cycle stood. Future-window deployment: any time future Opus identifies a Tier-3/4 capture deficiency within an active session, the response is immediate backfill rather than registering-for-later-backfill.

---

**End of seed catalog.** Total entries: 7 Layer 1 (METH-L1-001 through METH-L1-007) + 8 Layer 2 (METH-L2-001 through METH-L2-008) + 7 Layer 3 (METH-L3-001 through METH-L3-007) = **22 entries**. Full catalog completion (back-fill from earlier closure arcs: SF-4, SS-9, SM-line, EW-line) queued as OPEN-ORG-016.

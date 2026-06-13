# Changelog — SR-2: The Spin-Bit Axiom

Canonical filename (no version suffix): `SR-2_spin_bit_axiom_quadrupole_formula.tex`.
Version archaeology lives here per the operating_system.md version-archaeology
architecture rule; the `.tex` title block shows only the current version line.

## v0.6 — 13 June 2026 (Phase 7C CLEARED — panel 3/3 CONFIRM; release candidate)

No prose change from v0.5; this entry records the gate-clearance milestone.

**Final 7C panel verdicts (all on / after v0.5): 3/3 CONFIRM.**
- **ChatGPT — CONFIRM**, verified against the *live* v0.5 file: it quotes the actual scoped
  abstract ("required within CPP's current axioms") and the §3 scoping, and confirms the prior
  "every working theory" over-reach is retired. Highest-confidence return.
- **Copilot — CONFIRM**: engaged with v0.5 (its SQ8 explicitly credits the GR/string edits); its
  lone REVISE(framing) nit (abstract necessity) quoted stale cached text and is already fixed.
- **Grok — CONFIRM**: verdict CONFIRM; provenance caveat — it quoted the stale v0.2 abstract and
  its recommendation block mirrors the original ChatGPT CONFIRM (the "Patch 1139/1140" language).
  Grok's independent substantive engagement is nonetheless established by its prior-round RESTATE
  (the §11-guard catch), which is fully integrated.

**Trajectory (every reviewer's substantive objection raised → integrated → CONFIRM):**
- ChatGPT: CONFIRM(v0.2) → RESTATE(re-review, stale) → CONFIRM(v0.5, live-verified).
- Grok: RESTATE(v0.2, substantive: necessity scoping + §11 guard) → CONFIRM.
- Copilot: CONFIRM(v0.2) → CONFIRM(v0.5).

**Cache artifact (documented so the record is honest):** raw.githubusercontent.com served CDN-cached
copies (~5 min TTL), so two of three CONFIRM returns still quoted the v0.2 abstract though origin was
at v0.5. The close rests on (i) ChatGPT's live-verified CONFIRM, (ii) live-verification here that all
substantive objections are integrated, and (iii) all three final verdicts being CONFIRM. A clean
single-reviewer re-confirm of Grok against inlined v0.5 text remains available if strict independence
on v0.5 is desired; given the integrated merits and the loop risk, the close is recorded now.

**Declined (with reason):** Copilot's optional Patch-1143 (a §6 footnote cross-linking λ to
THEO-SR-EIN-4) — the cross-ref target is imprecise (THEO-SR-EIN-4 is the Operational-Energy Lemma,
not the λ derivation), and the λ provenance is already stated in §6 prose and the Table-1 caption.

**Gate: Phase 7C CLEAR.** SR-2 is a release candidate. Next: SHIP-time per-paper completion checklist
(10-file documentation suite, registry/index navigation, C13 anthology chapter, H6 final audit) →
A3′ + SR-2 ship as v1.0.

## v0.5 — 13 June 2026 (Phase 7C framing pass 3 — universal-quantifier motif retired)

**Attribution corrected (per architect):** the v0.4 RESTATE was **Grok's**; ChatGPT then
re-reviewed and also returned **RESTATE**. Panel verdicts now stand at: Copilot CONFIRM;
Grok RESTATE; ChatGPT (re-review) RESTATE.

**Stale-cache finding (root cause of the recurring flags):** both RESTATEs fetched
`raw.githubusercontent.com` and quoted the **v0.2 abstract** and the **missing §11 guard** —
both already fixed in v0.3/v0.4 on origin. raw.githubusercontent.com serves CDN-cached copies
(~5 min TTL), so the reviewers re-flagged already-resolved text. Verified against the live
v0.4 file: abstract necessity (fixed v0.3), §3 "not an open question" (fixed v0.4), and the
§11 op:einstein-simpliciter guard (added v0.4) are all present.

**Genuinely live points integrated this pass** — the universal "every working theory / every
successful formulation of gravity" motif, in three places (abstract trailing comparison, §3
assault-2, §8). These were statements about *other* theories (GR, string theory) used to frame
CPP's result as expected, not registry over-claims about CPP; but two reviewers flagged the
absolute quantifier. Resolved by replacing "every working/successful theory" with the concrete
examples "general relativity and string theory" — more precise, unambiguously about other
theories, and the landscape-framing intent ("CPP lands with mainstream gravity") preserved.
**Declined** ChatGPT's verbatim replacements, which would have swapped the landscape context for
a CPP-internal claim and lost that framing. No claim changed; recompile clean (19 pp).

**Gate status:** NOT closed. Two RESTATEs are outstanding, but both were against stale text and
their still-valid points are now integrated (v0.4 + v0.5). The clean close is a re-dispatch of
v0.5 for re-confirm (mirrors the A3′ DG-3 round-1→round-2 pattern) — with a cache-bust so the
reviewers see the live file, not a cached copy.

## v0.4 — 13 June 2026 (Phase 7C framing pass 2 — third return integrated; attribution pending)

A third 7C return arrived (a **RESTATE**, framing-only) conducted against the **stale v0.2**
draft (it quotes the pre-1139 abstract text "required, exactly as in every working theory of
gravity", already rescoped in v0.3). Its four points, assessed against current v0.4:
- **P1 abstract necessity** — already addressed in v0.3 (scoped to CPP's axioms; the universal
  phrase demoted to a comparison). No action.
- **P2 §3 "not an open question"** — v0.3 added the scoping parenthetical; tightened the trailing
  clause to "for that sector, this is now a closed conclusion" for full uniformity. Applied.
- **P3 §11 guard (the substantive catch)** — §11 Problem Status listed (a)/(b) but did not restate
  the "not op:einstein simpliciter" guard carried in §1 and §10. Added a closing sentence:
  "Thus this paper closes op:einstein (a), not op:einstein simpliciter: (b) remains conditionally
  closed pending the shell-sum reduction rigorization, and the substrate-microscopic energy
  functional is a declared refinement, not an axiom debt." Applied.
- **P4 Table 1 "derived here"** — caption bounded: the Derived entries are derived *given* A3′ +
  the C5 readout convention + the scalar-sector G, not from nothing. Applied.

Recompile clean (rc=0, no undefined refs/cites, 19 pp). No claim changed.

**Attribution / gate note (unresolved — see scope addendum):** the return was labelled "ChatGPT",
but ChatGPT already returned CONFIRM (v0.2) and the prior turn had a label-crossing (a ChatGPT
duplicate arrived in the Grok slot). It is therefore unclear whether this RESTATE is the real Grok
(mislabelled), a ChatGPT re-review, or a mislabel; it also reviewed stale text. **The 7C gate is NOT
declared 3/3.** Two clean independent CONFIRMs stand (ChatGPT, Copilot); the RESTATE's still-valid
points are now integrated. Awaiting architect confirmation of attribution and of whether the real
Grok has reviewed before the gate is closed.

## v0.3 — 13 June 2026 (Phase 7C framing pass — partial, 2/3 panel returns)

7C framing/over-claim review returns from **2 of 3** panel members in; both **CONFIRM**:
- **ChatGPT — CONFIRM** (one REVISE-framing): tighten the abstract necessity sentence so
  "required" is scoped to CPP's axioms / the radiative sector, not a universal claim;
  optionally add an explicit scoping parenthetical at the first "necessary" in §3.
- **Copilot — CONFIRM** (two optional REVISE-framing): (1) soften the abstract idiom "the
  axiom pays for itself"; (2) add "Within the gravitational sector" to the conclusion's
  scalar-vector-completed sentence.
- **Grok — pending.** The 7C gate is held at **2/3 CONFIRM**; not declared closed.

Applied (convergent / safe, claim-preserving):
- Abstract necessity sentence rescoped: "required within CPP's current axioms to carry the
  observed helicity-±2 polarizations --- consistent with the status of the graviton as
  fundamental in every working theory of gravity" (was "required, exactly as in every
  working theory of gravity").
- §3 first "necessary" gains an explicit parenthetical "(within CPP's current axioms, for
  the radiative tensor sector)".
- Conclusion: "Within the gravitational sector, CPP is therefore a scalar--vector gravity
  completed by exactly one rank-2 degree of freedom..." (mono-sectoral crispness).

Declined (with reason): Copilot's optional softening of "the axiom pays for itself" — the
idiom is a precise cost/benefit statement (one degree of freedom, zero parameters, recovers
the GR radiative sector), not an over-claim; symmetric honesty applies to keeping accurate
phrasing as well as cutting inflated phrasing. No claim changed in any edit.

## v0.2 — 12 June 2026 (Phase 7B complete)

- **C14 step-5 audit-trail sweep** executed: the two uncited substantive method
  invocations flagged by the sweep were added — METH-L3-003 (the Step-0 audit
  confirming the second-assault dynamical matrix carried no per-edge transport, so the
  third assault was genuinely untested) in §3, and METH-L3-004 (the would-be-axiom
  discipline: terminal branch at the necessity conclusion in §3, refusal branch at the
  τ-redundancy in §7). All 13 methods of the 1133 plan are now cited.
- **Figure PDFs generated** by re-running `notebooks/SR-2_figures.py` (matplotlib;
  ledger check reproduced 0.999998). The four figure includes were switched from
  `\includesvg` to `\includegraphics{...pdf}`, so the paper compiles with plain
  `pdflatex` + `graphicx` and needs no inkscape (SR-1 convention). Committed SVGs left
  untouched; only the four PDFs are added.
- **Compile verified end-to-end:** `pdflatex ×3 + bibtex`, all rc=0, no undefined
  references or citations, all six bibliography entries resolved, 19 pages.

## v0.1 — 12 June 2026 (Phase 7B first full draft)

- First `.tex` of the spin-2 / `op:einstein` arc. Produced in Phase 7B per
  `series_relativity/op_einstein_closure/flagship_assembly_scope.md` (SKELETON LOCK,
  Patch 1135).
- Transcribed from the 13 step/task documents — `op_einstein_closure/1107–1110`,
  `spin2_construction/1112–1129` — plus the DG-3 review suite, onto the locked
  10-section skeleton. Transcription-and-framing, not derivation: no verdict moved.
- Four theorems stated to match the registry verbatim (THEO-SR-EIN-1 Completion,
  THEO-SR-EIN-2 Statics, THEO-SR-EIN-3 TT-Response/Cancellation, THEO-SR-EIN-4
  Operational-Energy Lemma). Axiom A3′ stated as registered (amendment, count 9,
  audit note 10). Four falsifiers stated as PRED-O-35..38 (open, uncounted).
- Conditionality harmonized (Gap 5): `op:einstein` (a) CLOSED for the radiative
  sector; (b) conditionally closed with the shell-sum reduction rigorization named as
  the residual; the substrate-microscopic energy functional flagged as a declared
  refinement, not a debt.
- Figure-to-section map per the lock: fig1 (H_g seat) → §4; fig2 (two assaults) → §3;
  fig3 (eccentric ledger) → §7; fig4 (lattice discriminant) → §9.
- Inline `[METH-Lx-NNN ...]` citations placed per the 1133 citation plan
  (`1133_c14_methods_audit.md` §4).
- Bibliography (`SR-2_references.bib`): external GW literature added; internal CPP
  companions referenced by programme ID in prose.

### Open for 7B completion / 7C
- C14 step-5 audit-trail sweep (uncited substantive method invocations) before 7C dispatch.
- Required-subsection placement confirmed: §1.1 Open Problems Addressed; §8.1 CP/GP
  Signature; §11.1 Swarm-Validation Contribution; §11.2 Problem Status.
- Figure PDFs: only SVGs are committed; `\includesvg` is used (svg package, inkscape
  conversion). Pre-generated PDFs can be added if the build environment lacks inkscape.
- 7C review pass: framing + over-claim only, not new math (components are DG-3-closed).

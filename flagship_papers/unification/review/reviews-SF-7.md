# reviews-SF-7.md — Review aggregation

Aggregated reviewer verdicts and cross-reviewer synthesis for SF-7. Append-only per cycle.

---

## Review cycle 1 — SF-7 v0.1 skeleton, ARCHITECTURAL review (Patch 1315 package → Patch 1316 close)

**Artifact:** SF-7 v0.1 skeleton (Patch 1314). **Scope:** architectural / scoping (not ship-readiness). **Package:** `review/sf-7_skeleton_review_package_v1.0.md`. **Panel:** ChatGPT, Grok, Copilot (default) + Gemini (optional breadth).

### Verdicts

| Reviewer | Verdict | Tier | One-line |
|---|---|---|---|
| Grok | **(A) sound** | SCRIPT-EXECUTED | Ran §7 code, all assertions pass; one numeric note (χ/6). |
| Copilot | **(A) sound** | INSPECTED | No revisions required; proceed to build-out. |
| ChatGPT | **(B) sound w/ revisions** | INSPECTED | Deflate C3 + headline; downgrade C2 *unless* independence proven; add closure column; non-overlap guardrail. |
| Gemini | **(B) sound w/ revisions** | INSPECTED (no code run) | Deflate C3; soften headline; circularity guardrails. |

**Net:** 2× (A), 2× (B), **zero (C)** — unanimous "proceed to the §10 build-out." The two (A)s are the reviewers who engaged the math hardest (Grok recomputed; Copilot structural). The two (B)s are the assigned overclaim/breadth reviewers; their dissent is framing-rigor, not a load-bearing flaw.

### Per-scrutiny synthesis

- **A1 (ledger honesty).** Grok/Copilot: honest as stated (η quarantined as open, not a knob). ChatGPT/Gemini: honest *provided* the qualifier rides the slogan everywhere. → **Resolved:** standardised qualifier "one calibration; zero additional fitted shape parameters in the closed sectors" adopted in §9 prose.
- **A2 (accounting).** Defensible (4/4), with ChatGPT's constructive ask for a closure-status column. → **Resolved:** Closed/Partial/Open column added to Table~\ref{tab:ledger}.
- **B1 (is C2 theorem-level?).** Grok/Copilot/Gemini: yes. **ChatGPT alone: not yet — the three independence conditions (disjoint state variables; perturbation invariance; no shared hidden parameter) are asserted, not demonstrated.** → **Resolved by meeting the conditions, not softening:** the Z/ν₂ independence Lemma (`lem:c2indep`) was written, discharging all three from the shipped SF-2/SF-4 material (parameter sets enumerated; fitted-DOF intersection empty; sole coupling = the single m_e calibration). C2 is now theorem-level on an explicit proof. Net C2 position: **4/4.**
- **B2 (C3 overclaim).** ChatGPT/Gemini: "same χ handle" reads as same *mechanism*; only a shared *quantity* is established. Grok/Copilot: already scoped. → **Resolved:** C3 reworded to "same substrate *quantity* χ … a shared quantity, not a shared mechanism (OP-SM-7d open)."
- **C1 (circularity).** All four: not fatally circular; C1-clause (calibration coherence) is the most inherited; non-trivial weight lives in C2/C3. → **Resolved:** a panel-adopted build rule added to §10 (every member must prove a genuine cross-sector constraint, not "both use the 600-cell"; each carries a unique non-overlap obligation; the M₀/phase-leaning members must not collapse into one argument).
- **C2 (roadmap threads).** Correctly assigned (4/4). ChatGPT flag: SF-1↔SF-4, SF-3↔SF-4, SF-3↔SF-1 risk collapsing into one M₀/phase argument. → folded into the build rule.
- **χ/6 (Grok, SCRIPT-EXECUTED).** Exact value 0.0393446…; corpus standardises ≈0.0394. → **Resolved:** precise-value footnote added.

### Cycle outcome

**Closed at v0.2 (Patch 1316), pre-build calibration — no restate-to-v1.1, no redesign.** The architecture is validated for the §10 build-out. ChatGPT's one substantive downgrade (C2) was converted to a satisfied condition by writing the independence lemma rather than softening the label; the remaining four convergent items were applied as deflations/additions. The circularity guardrail is now a standing build rule for the ten remaining members.

**Deferred (ship-time flagged integration):** registration of THEO-SF7-CONSIST-1 + Lemma `lem:c2indep` in `theorem-registry.md`; `paper_catalog.md`, `predictions.md`, `frontier_sectors/*`, `master_glossary.md`, bibliography master entry.
